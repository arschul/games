/* Game Hub music picker: lets the teacher play any game's soundtrack in any game.
   Load after index.js:
     <script src="../shared/music/index.js"></script>
     <script src="../shared/music/picker.js" data-game="cant-stop"></script>
   Then, in the game's Music controller, create players through the picker:
     player = ArschulMusic.make(createPlayer, ctx, { mode })      // was: createPlayer(ctx, { mode })
   The returned player has the same API as the game's own player. When the teacher picks another
   track, the picker swaps the engine underneath (lazy-loading tracks/<id>.js), translating the game's
   modes and cues through index.js and matching loudness, so the game's controller never notices.
   Games without a score of their own pass createPlayer = null and get a library track.
   Choice is stored per game in localStorage 'arschul:music:<game>': '' (own theme), a track id, or 'shuffle'.
   UI: a "Track" button is added after every music volume slider (input[type=range][aria-label="Music volume"])
   or inside any element marked data-music-picker; it opens a touch-friendly track sheet. */
(function () {
  'use strict';
  var M = window.ArschulMusic = window.ArschulMusic || {};
  var me = document.currentScript;
  var BASE = me && me.src ? me.src.replace(/[^\/]*$/, '') : '../shared/music/';
  var GAME = (me && me.getAttribute('data-game')) || (location.pathname.split('/').filter(Boolean).slice(-2, -1)[0] || 'game');
  var KEY = 'arschul:music:' + GAME;
  if (me && me.getAttribute('data-default')) M.defaultTrack = me.getAttribute('data-default');
  // data-own="Title": the game plays its own score through its own engine (not a createPlayer); it listens to
  // ArschulMusic.onChange and asks ArschulMusic.current() whether a library track is wanted ('' = its own).
  if (me && me.getAttribute('data-own')) M.externalOwn = me.getAttribute('data-own');
  var IDX = (M.index && M.index.tracks) || [];
  var MOODS = (M.index && M.index.moods) || [];
  var BY = {}; IDX.forEach(function (t) { BY[t.id] = t; });
  var HOST = BY[GAME] || null;            // this game's own track entry (null = no own score)
  var REF_RMS = 0.06;                     // loudness a library track is matched to in games with no score of their own
  var live = [], loaded = {}, loading = {}, listeners = [];

  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); } catch (e) { } }

  /* ---------- choice ---------- */
  var choice = lsGet(KEY); if (choice == null) choice = M.defaultTrack || '';
  if (choice && choice !== 'shuffle' && !BY[choice]) choice = '';
  var shuffled = null;
  function pickShuffle() {
    var pool = IDX.filter(function (t) { return t.id !== GAME; });
    return pool.length ? pool[Math.floor(Math.random() * pool.length)].id : '';
  }
  // The track that should be playing now: a library id, or '' for the game's own score.
  function wanted() {
    var c = choice;
    if (c === 'shuffle') { if (!shuffled) shuffled = pickShuffle(); c = shuffled; }
    if (c === GAME) c = '';
    if (!c && !M.hostCreate && !HOST && !M.externalOwn) c = M.defaultTrack || (IDX[0] && IDX[0].id) || '';
    return c;
  }

  /* ---------- loading ---------- */
  function load(id) {
    if (loaded[id] || (M.factories && M.factories[id])) { loaded[id] = true; return Promise.resolve(); }
    if (loading[id]) return loading[id];
    loading[id] = new Promise(function (res, rej) {
      var s = document.createElement('script');
      s.src = BASE + 'tracks/' + id + '.js'; s.async = true;
      s.onload = function () { loaded[id] = true; res(); };
      s.onerror = function () { delete loading[id]; rej(new Error('music track failed to load: ' + id)); };
      document.head.appendChild(s);
    });
    return loading[id];
  }
  var factoryCache = {};
  function factory(id) { return factoryCache[id] || (factoryCache[id] = M.factories[id]()); }

  /* ---------- the proxy player ---------- */
  function num(x) { return typeof x === 'number' && isFinite(x); }
  function make(hostCreate, ctx, opts) {
    opts = opts || {};
    if (hostCreate) M.hostCreate = hostCreate;
    var st = {
      ctx: ctx, opts: opts, mode: opts.mode, intensity: null, hostVol: num(opts.volume) ? opts.volume : null,
      started: false, stopped: false, duckCall: null, cur: null
    };
    var out = opts.out || ctx.destination;

    function genericMode() {
      if (!HOST) return st.mode && /^(calm|active|tense)$/.test(st.mode) ? st.mode : 'calm';
      return (HOST.modes && HOST.modes[st.mode]) || 'calm';
    }
    function ratio(trk) {
      var hr = HOST ? HOST.rms : REF_RMS;
      return trk.rms && hr ? Math.min(6, Math.max(0.15, hr / trk.rms)) : 1;
    }
    function shellGain(trk) {
      var v = st.hostVol == null ? 0 : st.hostVol;
      if (!HOST) v = v * v;          // games without a score pass the 0..1 slider value: perceptual curve
      return Math.max(0, v * ratio(trk));
    }

    function buildOwn() {
      var o = Object.assign({}, opts, { mode: st.mode });
      return { kind: 'own', id: '', p: hostCreate(ctx, o) };
    }
    function buildForeign(id) {
      var trk = BY[id];
      var sh = { input: ctx.createGain(), duck: ctx.createGain(), vol: ctx.createGain() };
      sh.vol.gain.value = 0;
      sh.input.connect(sh.duck); sh.duck.connect(sh.vol); sh.vol.connect(out);
      var pctx = new Proxy(ctx, {
        get: function (t, k) {
          if (k === 'destination') return sh.input;
          var v = t[k];
          return typeof v === 'function' ? v.bind(t) : v;
        }
      });
      var fm = (trk.play && (trk.play[genericMode()] || trk.play.active || trk.play.calm)) || undefined;
      var p = factory(id)(pctx, { mode: fm, seed: (Math.random() * 1e9) | 0, volume: 1 });
      return { kind: 'foreign', id: id, p: p, trk: trk, sh: sh, fmode: fm };
    }
    function startCur(t, fadeIn) {
      var c = st.cur; if (!c || c.kind === 'pending') return;
      if (c.kind === 'own') {
        if (HOST && HOST.startVol !== false) c.p.start(t, st.hostVol == null ? undefined : st.hostVol); else c.p.start(t);
        if (st.hostVol != null && c.p.setVolume) c.p.setVolume(st.hostVol, t);
        if (st.intensity != null && c.p.setIntensity) c.p.setIntensity(st.intensity, t);
        if (st.duckCall && typeof c.p[st.duckCall[0]] === 'function') c.p[st.duckCall[0]].apply(c.p, st.duckCall[1]);
      } else {
        if (c.trk.startVol !== false) c.p.start(t, 1); else c.p.start(t);
        if (c.p.setVolume) c.p.setVolume(1, t);
        if (st.intensity != null && c.p.setIntensity) c.p.setIntensity(st.intensity, t);
        var g = c.sh.vol.gain, target = shellGain(c.trk);
        g.cancelScheduledValues(t);
        if (fadeIn) { g.setValueAtTime(0.0001, t); g.linearRampToValueAtTime(Math.max(0.0001, target), t + 1.2); }
        else g.setValueAtTime(target, t);
      }
    }
    function retire(c, t) {
      if (!c || c.kind === 'pending') return;
      try { if (c.kind === 'foreign') { c.sh.vol.gain.cancelScheduledValues(t); c.sh.vol.gain.setTargetAtTime(0, t, 0.15); } } catch (e) { }
      try { if (c.p.stop) c.p.stop(t + (c.kind === 'foreign' ? 0.6 : 0)); } catch (e) { }
      if (c.kind === 'foreign') setTimeout(function () { try { c.sh.vol.disconnect(); } catch (e) { } try { c.p.disconnect && c.p.disconnect(); } catch (e) { } }, 3000);
    }
    function setCur(next, swapping) {
      var t = ctx.currentTime + 0.05, old = st.cur;
      st.cur = next;
      if (old && st.started && !st.stopped) retire(old, t);
      if (st.started && !st.stopped) startCur(t + (swapping ? 0.15 : 0), swapping);
    }
    function want(id) {
      if (!id) {
        if (st.cur && st.cur.kind === 'own') return;
        if (!hostCreate) return;
        setCur(buildOwn(), !!st.cur);
        return;
      }
      if (st.cur && st.cur.kind === 'foreign' && st.cur.id === id) return;
      if (loaded[id] || (M.factories && M.factories[id])) { loaded[id] = true; setCur(buildForeign(id), !!(st.cur && st.cur.kind !== 'pending')); return; }
      if (!st.cur) st.cur = hostCreate ? buildOwn() : { kind: 'pending' };
      load(id).then(function () { if (!st.stopped && wantedFor(api) === id) setCur(buildForeign(id), st.cur.kind !== 'pending'); }, function () { });
    }

    function fwd(name) {
      return function () {
        var c = st.cur; if (!c || c.kind === 'pending') return;
        var f = c.p[name]; if (typeof f === 'function') return f.apply(c.p, arguments);
      };
    }
    var handlers = {
      start: function (t, v) {
        st.started = true; st.stopped = false;
        if ((HOST ? HOST.startVol !== false : true) && num(v)) st.hostVol = v;
        startCur(num(t) ? t : ctx.currentTime, false);
      },
      setVolume: function (v, t) {
        if (num(v)) st.hostVol = v;
        var c = st.cur; if (!c || c.kind === 'pending') return;
        if (c.kind === 'own') return c.p.setVolume && c.p.setVolume.apply(c.p, arguments);
        c.sh.vol.gain.setTargetAtTime(shellGain(c.trk), num(t) ? t : ctx.currentTime, 0.05);
      },
      setMode: function (m, t) {
        st.mode = m;
        var c = st.cur; if (!c || c.kind === 'pending') return;
        if (c.kind === 'own') return c.p.setMode && c.p.setMode.apply(c.p, arguments);
        var fm = c.trk.play && (c.trk.play[genericMode()] || c.trk.play.active);
        if (fm && fm !== c.fmode && c.p.setMode) { c.fmode = fm; c.p.setMode(fm, num(t) ? t : ctx.currentTime); }
      },
      setIntensity: function (x) {
        st.intensity = x;
        var c = st.cur; if (!c || c.kind === 'pending') return;
        if (c.p.setIntensity) return c.p.setIntensity.apply(c.p, arguments);
      },
      cue: function (name, t) {
        var c = st.cur; if (!c || c.kind === 'pending' || !c.p.cue) return 0;
        if (c.kind === 'own') return c.p.cue.apply(c.p, arguments);
        var gen = HOST ? (HOST.cues && HOST.cues[name]) : name;
        var fc = gen && c.trk.cueOut && c.trk.cueOut[gen];
        if (!fc) return 0;
        return c.trk.cueAt !== false ? c.p.cue(fc, ctx.currentTime + 0.03) : c.p.cue(fc);
      },
      stop: function (t) {
        st.stopped = true; st.started = false;
        var i = live.indexOf(api); if (i >= 0) live.splice(i, 1);
        var c = st.cur; if (!c || c.kind === 'pending') return;
        if (c.kind === 'own') return c.p.stop && c.p.stop.apply(c.p, arguments);
        try { c.sh.vol.gain.setTargetAtTime(0, num(t) ? t : ctx.currentTime, 0.2); } catch (e) { }
        try { c.p.stop && c.p.stop(t); } catch (e) { }
      },
      disconnect: function () {
        var c = st.cur; if (!c || c.kind === 'pending') return;
        if (c.kind === 'foreign') { try { c.sh.vol.disconnect(); } catch (e) { } }
        if (c.p.disconnect) try { c.p.disconnect(); } catch (e) { }
      }
    };
    // Duck calls: forwarded to the game's own player, applied to the shell for library tracks.
    function duckHandler(name) {
      return function () {
        var args = [].slice.call(arguments);
        st.duckCall = name === 'setDuck' || name === 'duckTo' ? [name, args] : null;
        var c = st.cur; if (!c || c.kind === 'pending') return;
        if (c.kind === 'own') { var f = c.p[name]; return typeof f === 'function' ? f.apply(c.p, args) : undefined; }
        var g = c.sh.duck.gain, now = ctx.currentTime;
        if (name === 'setDuck') { g.setTargetAtTime(Math.max(0, +args[0] || 0), num(args[1]) ? args[1] : now, 0.08); return; }
        if (name === 'duckTo') { g.setTargetAtTime(Math.max(0, +args[0] || 0), num(args[1]) ? args[1] : now, num(args[2]) ? args[2] : 0.1); return; }
        // duck(sec[, t]) or duck(level, t, sec)
        var lvl = 0.25, sec = args[0], t0 = now;
        if (args.length >= 3 && num(args[2])) { lvl = num(args[0]) ? args[0] : 0.25; t0 = num(args[1]) ? args[1] : now; sec = args[2]; }
        else if (num(args[1])) t0 = args[1];
        if (!num(sec)) sec = 2;
        g.cancelScheduledValues(t0); g.setTargetAtTime(lvl, t0, 0.06); g.setTargetAtTime(1, t0 + sec, 0.4);
      };
    }
    ['duck', 'setDuck', 'duckTo'].forEach(function (n) { handlers[n] = duckHandler(n); });
    function shellNodes(c) {
      return { input: c.sh.input, duck: c.sh.duck, vol: c.sh.vol, volume: c.sh.vol, master: c.sh.input, out: c.sh.vol };
    }
    var api = new Proxy({}, {
      get: function (_, k) {
        if (k === '__music') return st;
        if (k === '__want') return want;
        if (k === 'track') return st.cur && st.cur.kind === 'foreign' ? st.cur.id : '';
        if (Object.prototype.hasOwnProperty.call(handlers, k)) return handlers[k];
        var c = st.cur;
        if (!c || c.kind === 'pending') {
          if (k === 'bars') return 0;
          if (k === 'mode') return st.mode;
          return typeof k === 'string' && /^(scheduleUntil|resync|setBed)$/.test(k) ? function () { } : undefined;
        }
        if (c.kind === 'own') { var v = c.p[k]; return typeof v === 'function' ? v.bind(c.p) : v; }
        if (k === 'mode') return st.mode;
        if (k === 'intensity') return st.intensity == null ? 0 : st.intensity;
        if (k === 'gains' || k === 'nodes') return shellNodes(c);
        if (k === 'volumeGain' || k === 'volGain' || k === 'volumeNode' || k === 'output') return c.sh.vol;
        if (k === 'duckGain' || k === 'duckNode') return c.sh.duck;
        if (k === 'setBed') return function () { };
        var fv = c.p[k];
        if (typeof fv === 'function') return fv.bind(c.p);
        if (fv !== undefined) return fv;
        return typeof k === 'string' && /^(set|res)/.test(k) ? function () { } : undefined;
      },
      has: function (_, k) { return k in handlers || !!(st.cur && st.cur.p && k in st.cur.p); }
    });
    live.push(api);
    want(wantedFor(api));
    return api;
  }
  function wantedFor() { return wanted(); }

  function setChoice(c) {
    choice = c || '';
    shuffled = null;
    lsSet(KEY, choice);
    var id = wanted();
    if (id) load(id).catch(function () { });
    live.slice().forEach(function (p) { try { p.__want(id); } catch (e) { } });
    listeners.forEach(function (f) { try { f(); } catch (e) { } });
    paintTriggers();
  }
  function currentLabel() {
    var id = wanted();
    if (!id) return 'This game\'s theme';
    var t = BY[id]; return t ? t.title : id;
  }

  /* ---------- UI ---------- */
  var css = '' +
    '.mp-trigger{display:inline-flex;align-items:center;gap:.5em;font:inherit;font-size:1em;font-weight:600;color:inherit;background:transparent;' +
    'border:2px solid color-mix(in srgb,currentColor 45%,transparent);border-radius:999px;padding:.4em 1em .4em .8em;min-height:2.6em;' +
    'cursor:pointer;max-width:100%;white-space:nowrap;line-height:1.1;vertical-align:middle;touch-action:manipulation}' +
    '.mp-trigger:hover,.mp-trigger:focus-visible{border-color:currentColor}' +
    '.mp-trigger svg{width:1.15em;height:1.15em;flex:none}' +
    '.mp-trigger span{overflow:hidden;text-overflow:ellipsis}' +
    '.mp-sheet{position:fixed;inset:0;z-index:2147483000;display:flex;align-items:center;justify-content:center;' +
    'background:rgba(0,0,0,.55);font-family:var(--mp-font,inherit)}' +
    '.mp-panel{width:min(980px,94vw);max-height:90vh;display:flex;flex-direction:column;border-radius:22px;overflow:hidden;' +
    'background:var(--mp-bg);color:var(--mp-ink);box-shadow:0 30px 80px rgba(0,0,0,.6),0 0 0 2px color-mix(in srgb,var(--mp-accent) 50%,transparent);' +
    'animation:mp-in .32s cubic-bezier(.2,1.3,.4,1) both}' +
    '@keyframes mp-in{from{transform:translateY(40px) scale(.96);opacity:0}}' +
    '.mp-head{display:flex;align-items:center;gap:16px;padding:clamp(14px,2.2vh,26px) clamp(18px,2.4vw,32px);' +
    'border-bottom:2px solid color-mix(in srgb,var(--mp-ink) 12%,transparent)}' +
    '.mp-head h2{margin:0;font-size:clamp(24px,3.4vh,40px);flex:1;font-weight:800;letter-spacing:0}' +
    '.mp-head p{margin:0;opacity:.7;font-size:clamp(14px,1.8vh,20px)}' +
    '.mp-done{font:inherit;font-weight:700;font-size:clamp(18px,2.4vh,26px);min-height:clamp(48px,6.4vh,68px);padding:0 1.2em;border:0;border-radius:14px;' +
    'cursor:pointer;background:var(--mp-accent);color:var(--mp-accent-ink);box-shadow:0 5px 0 color-mix(in srgb,var(--mp-accent) 55%,#000)}' +
    '.mp-done:active{transform:translateY(4px);box-shadow:0 1px 0 color-mix(in srgb,var(--mp-accent) 55%,#000)}' +
    '.mp-body{overflow:auto;padding:8px clamp(14px,2vw,26px) 22px;-webkit-overflow-scrolling:touch}' +
    '.mp-group{margin:16px 4px 6px;font-size:clamp(15px,1.9vh,20px);font-weight:700;opacity:.65}' +
    '.mp-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:10px}' +
    '.mp-row{display:flex;align-items:center;gap:14px;text-align:left;font:inherit;color:inherit;cursor:pointer;min-height:clamp(60px,7.6vh,82px);' +
    'padding:10px 16px;border-radius:14px;border:2px solid color-mix(in srgb,var(--mp-ink) 14%,transparent);' +
    'background:color-mix(in srgb,var(--mp-ink) 5%,transparent);touch-action:manipulation}' +
    '.mp-row:hover{border-color:color-mix(in srgb,var(--mp-ink) 40%,transparent)}' +
    '.mp-row[aria-checked=true]{border-color:var(--mp-accent);background:color-mix(in srgb,var(--mp-accent) 22%,transparent)}' +
    '.mp-dot{flex:none;width:22px;height:22px;border-radius:50%;border:3px solid color-mix(in srgb,var(--mp-ink) 40%,transparent)}' +
    '.mp-row[aria-checked=true] .mp-dot{border-color:var(--mp-accent);background:radial-gradient(circle,var(--mp-accent) 45%,transparent 50%)}' +
    '.mp-t{display:flex;flex-direction:column;gap:2px;min-width:0}' +
    '.mp-t b{font-size:clamp(18px,2.3vh,24px);font-weight:700;line-height:1.15}' +
    '.mp-t small{font-size:clamp(13px,1.6vh,17px);opacity:.65;line-height:1.2}' +
    '@media (prefers-reduced-motion:reduce){.mp-panel{animation:none}}';
  var ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M3 5h11v2H3zm0 4h11v2H3zm0 4h7v2H3zm14-8v8.6a3 3 0 1 0 2 2.8V8h3V5z"/></svg>';
  var styled = false;
  function ensureCss() {
    if (styled) return; styled = true;
    var s = document.createElement('style'); s.id = 'mp-style'; s.textContent = css; document.head.appendChild(s);
  }
  function triggerHtml() { return ICON + '<span>' + esc(currentLabel()) + '</span>'; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function makeTrigger() {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'mp-trigger';
    b.setAttribute('aria-label', 'Choose music track'); b.title = 'Choose music track';
    b.innerHTML = triggerHtml();
    b.addEventListener('click', function (e) { e.preventDefault(); e.stopPropagation(); open(b); });
    ['pointerdown', 'mousedown', 'touchstart'].forEach(function (ev) { b.addEventListener(ev, function (e) { e.stopPropagation(); }, { passive: true }); });
    return b;
  }
  function paintTriggers() {
    var h = triggerHtml();
    [].forEach.call(document.querySelectorAll('.mp-trigger'), function (b) { if (b.innerHTML !== h) b.innerHTML = h; });
    [].forEach.call(document.querySelectorAll('.mp-icon'), function (b) { var t = 'Music track: ' + currentLabel(); if (b.title !== t) b.title = t; });
    var rows = document.querySelectorAll('.mp-row');
    var c = choice === GAME ? '' : choice;
    [].forEach.call(rows, function (r) { r.setAttribute('aria-checked', String(r.getAttribute('data-id') === c)); });
  }
  function attach() {
    ensureCss();
    var marks = document.querySelectorAll('[data-music-picker]');
    [].forEach.call(marks, function (m) {
      if (m.querySelector('.mp-trigger,.mp-icon')) return;
      if (m.getAttribute('data-music-picker') === 'icon') {
        // icon-only button dressed like the toolbar button before it
        var sib = m.previousElementSibling; while (sib && sib.tagName !== 'BUTTON') sib = sib.previousElementSibling;
        var b = makeTrigger();
        b.className = ((sib && sib.className) || '').split(/\s+/).filter(function (c) { return c && !/^(on|off|active|muted)$/.test(c) && !/toggle|mute|sound|theme|music/i.test(c); }).join(' ') + ' mp-icon';
        b.innerHTML = ICON; m.appendChild(b);
      } else m.appendChild(makeTrigger());
    });
    if (marks.length) return;
    [].forEach.call(document.querySelectorAll('input[type=range][aria-label="Music volume"]'), function (r) {
      if (r.closest('.mp-pop')) return;
      var at = r, nx = r.nextElementSibling;
      // keep a "70%" readout next to its slider
      if (nx && !nx.querySelector('input,button,select') && /^\s*\d+\s*%\s*$/.test(nx.textContent || '')) { at = nx; nx = nx.nextElementSibling; }
      if (nx && nx.classList && nx.classList.contains('mp-trigger')) return;
      at.insertAdjacentElement('afterend', makeTrigger());
    });
  }

  function lum(rgb) {
    var m = String(rgb).match(/[\d.]+/g); if (!m) return 0;
    var a = m.slice(0, 3).map(function (x) { x = x / 255; return x <= 0.03928 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4); });
    return 0.2126 * a[0] + 0.7152 * a[1] + 0.0722 * a[2];
  }
  function opaque(c) { var m = String(c).match(/[\d.]+/g); return m && (m.length < 4 || +m[3] > 0.6); }
  function themeVars(from) {
    var root = getComputedStyle(document.documentElement);
    var bs = getComputedStyle(document.body);
    var dark = document.documentElement.getAttribute('data-theme') !== 'light';
    var bg = root.getPropertyValue('--mp-bg').trim() || (opaque(bs.backgroundColor) ? bs.backgroundColor : (dark ? '#16181d' : '#f4efe6'));
    var ink = root.getPropertyValue('--mp-ink').trim() || bs.color || (dark ? '#f2efe8' : '#1b1b1b');
    var lb = lum(bg);
    if (Math.abs(lum(ink) - lb) < 0.4) ink = lb < 0.4 ? '#f4f1ea' : '#17181c';
    var acc = root.getPropertyValue('--mp-accent').trim();
    if (!acc && from) {
      var fs = getComputedStyle(from), host = from.closest('button,[class*=music],[id*=music]') || from;
      var cands = [getComputedStyle(host.parentElement || host).color, fs.color];
      acc = cands.filter(function (c) { return opaque(c) && Math.abs(lum(c) - lum(bg)) > 0.25; })[0];
    }
    if (!acc) acc = dark ? '#f2b84b' : '#b5531a';
    return { bg: bg, ink: ink, acc: acc, accInk: lum(acc) > 0.35 ? '#141414' : '#ffffff', font: bs.fontFamily };
  }

  var sheet = null, lastFocus = null;
  function row(id, title, sub) {
    var c = choice === GAME ? '' : choice;
    return '<button type="button" class="mp-row" role="radio" data-id="' + esc(id) + '" aria-checked="' + (c === id) + '">' +
      '<i class="mp-dot"></i><span class="mp-t"><b>' + esc(title) + '</b>' + (sub ? '<small>' + esc(sub) + '</small>' : '') + '</span></button>';
  }
  function open(from) {
    if (sheet) return;
    ensureCss(); lastFocus = document.activeElement;
    var v = themeVars(from);
    var h = '<div class="mp-panel" role="dialog" aria-modal="true" aria-label="Music track"><div class="mp-head"><div style="flex:1"><h2>Music</h2>' +
      '<p>Pick the soundtrack for this game. It changes right away.</p></div><button type="button" class="mp-done">Done</button></div><div class="mp-body">';
    h += '<div class="mp-grid" role="radiogroup" aria-label="Track">';
    if (HOST || M.hostCreate || M.externalOwn) h += row('', 'This game\'s theme', HOST ? HOST.title : (M.externalOwn || 'Default'));
    else h += row('', 'Default', BY[M.defaultTrack] ? BY[M.defaultTrack].title + ', from ' + BY[M.defaultTrack].from : '');
    h += row('shuffle', 'Shuffle', 'A different track each time the game opens') + '</div>';
    var moods = MOODS.length ? MOODS : IDX.map(function (t) { return t.mood; }).filter(function (m, i, a) { return a.indexOf(m) === i; });
    moods.forEach(function (m) {
      var ts = IDX.filter(function (t) { return t.mood === m && t.id !== GAME; });
      if (!ts.length) return;
      h += '<div class="mp-group">' + esc(m) + '</div><div class="mp-grid" role="radiogroup" aria-label="' + esc(m) + '">';
      ts.forEach(function (t) { h += row(t.id, t.title, 'from ' + t.from); });
      h += '</div>';
    });
    h += '</div></div>';
    sheet = document.createElement('div');
    sheet.className = 'mp-sheet';
    sheet.style.setProperty('--mp-bg', v.bg); sheet.style.setProperty('--mp-ink', v.ink);
    sheet.style.setProperty('--mp-accent', v.acc); sheet.style.setProperty('--mp-accent-ink', v.accInk);
    sheet.style.setProperty('--mp-font', v.font);
    sheet.innerHTML = h;
    var stopAll = function (e) { e.stopPropagation(); };
    ['pointerdown', 'mousedown', 'touchstart', 'click', 'pointerup', 'mouseup'].forEach(function (ev) { sheet.addEventListener(ev, stopAll); });
    sheet.addEventListener('click', function (e) {
      var r = e.target.closest('.mp-row');
      if (r) { setChoice(r.getAttribute('data-id')); return; }
      if (e.target.closest('.mp-done') || e.target === sheet) close();
    });
    document.body.appendChild(sheet);
    document.addEventListener('keydown', onKey, true);
    var cur = sheet.querySelector('.mp-row[aria-checked=true]') || sheet.querySelector('.mp-row');
    if (cur) { cur.focus({ preventScroll: true }); cur.scrollIntoView && cur.scrollIntoView({ block: 'nearest' }); }
  }
  function onKey(e) {
    if (!sheet) return;
    e.stopPropagation();
    if (e.key === 'Escape') { e.preventDefault(); close(); }
    else if ((e.key === 'Enter' || e.key === ' ') && document.activeElement && document.activeElement.closest && document.activeElement.closest('.mp-sheet')) { e.preventDefault(); document.activeElement.click(); }
    else if (/^Arrow/.test(e.key)) {
      e.preventDefault();
      var rows = [].slice.call(sheet.querySelectorAll('.mp-row')), i = rows.indexOf(document.activeElement);
      var n = rows[Math.max(0, Math.min(rows.length - 1, i + (e.key === 'ArrowUp' || e.key === 'ArrowLeft' ? -1 : 1)))];
      if (n) n.focus();
    }
  }
  function close() {
    if (!sheet) return;
    document.removeEventListener('keydown', onKey, true);
    sheet.remove(); sheet = null;
    if (lastFocus && lastFocus.focus) try { lastFocus.focus({ preventScroll: true }); } catch (e) { }
  }

  /* ---------- public ---------- */
  M.make = make;
  M.game = GAME;
  M.open = function () { open(document.querySelector('.mp-trigger')); };
  M.close = close;
  M.setChoice = setChoice;
  M.getChoice = function () { return choice; };
  M.current = function () { return wanted(); };
  M.onChange = function (f) { listeners.push(f); };
  M.attach = attach;
  M._live = live;


  /* ---------- drop-in controller (games without a score of their own) ----------
     <script src="../shared/music/picker.js" data-game="hex-duel" data-default="crown-lands" data-controller></script>
     plus <span data-music-controls></span> in the teacher toolbar (a music button with an On/Off, volume and
     track popover is built there, styled like the toolbar button next to it).
     Hooks for the game: ArschulMusic.setMuted(bool) from its sound toggle (M), ArschulMusic.cue('fail'|'success'|'win'|'turn'),
     ArschulMusic.duck(sec), ArschulMusic.setMode('calm'|'active'|'tense') (default follows the theme: dark = calm). */
  function controller() {
    var ON = KEY + ':on', VOL = KEY + ':vol';
    var on = lsGet(ON) !== '0', vol = +(lsGet(VOL) || 60), muted = false, modeOver = null;
    if (!(vol >= 0 && vol <= 100)) vol = 60;
    var ac = null, player = null, timer = 0;
    function themeMode() { return document.documentElement.getAttribute('data-theme') === 'light' ? 'active' : 'calm'; }
    function mode() { return modeOver || themeMode(); }
    function audible() { return on && !muted; }
    function tick() {
      if (!player || !ac) return;
      if (document.hidden) return;
      player.scheduleUntil(ac.currentTime + 0.6);
    }
    function start() {
      if (player || !ac || !audible()) return;
      if (ac.state === 'suspended') ac.resume();
      player = make(null, ac, { mode: mode() });
      player.start(ac.currentTime + 0.05, vol / 100);
      timer = setInterval(tick, 50); tick();
    }
    function stop() {
      if (!player) return;
      try { player.stop(ac.currentTime + 0.05); } catch (e) { }
      player = null; clearInterval(timer); timer = 0;
    }
    function apply() { if (audible()) start(); else stop(); paint(); }
    function unlock() {
      if (!ac) { var C = window.AudioContext || window.webkitAudioContext; if (!C) return; ac = new C(); }
      if (ac.state === 'suspended') ac.resume();
      apply();
    }
    ['pointerdown', 'keydown'].forEach(function (ev) { document.addEventListener(ev, unlock, { capture: true, once: false, passive: true }); });
    try { new MutationObserver(function () { if (player) player.setMode(mode()); }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] }); } catch (e) { }
    function setVol(v, flash) {
      vol = Math.max(0, Math.min(100, Math.round(+v || 0))); lsSet(VOL, String(vol));
      if (player) player.setVolume(vol / 100);
      paint(flash);
    }
    function setOn(v) { on = !!v; lsSet(ON, on ? '1' : '0'); apply(); }
    document.addEventListener('keydown', function (e) {
      if (e.target && /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName) && e.target.type !== 'range') return;
      if (e.target && e.target.isContentEditable) return;
      if (!e.shiftKey || e.ctrlKey || e.metaKey || e.altKey) return;
      if (e.code === 'KeyN') { e.preventDefault(); e.stopImmediatePropagation(); setOn(!on); }
      else if (e.code === 'BracketLeft') { e.preventDefault(); setVol(vol - 10, true); }
      else if (e.code === 'BracketRight') { e.preventDefault(); setVol(vol + 10, true); }
    }, true);

    /* toolbar button + popover */
    var NOTE = '<path d="M9 18V5l11-2v13"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="17.5" cy="16" r="2.5"/>';
    var SLASH = '<path d="M3 3l18 18"/>';
    var pop = null, popFrom = null;
    var popCss = '.mp-pop{position:fixed;z-index:2147482000;min-width:300px;padding:16px 18px;border-radius:16px;background:var(--mp-bg);color:var(--mp-ink);' +
      'box-shadow:0 18px 48px rgba(0,0,0,.55),0 0 0 2px color-mix(in srgb,var(--mp-accent) 45%,transparent);font-family:var(--mp-font,inherit);display:flex;flex-direction:column;gap:12px;' +
      'animation:mp-in .22s cubic-bezier(.2,1.3,.4,1) both}' +
      '.mp-pop h3{margin:0;font-size:20px;font-weight:800}' +
      '.mp-seg{display:flex;gap:8px}.mp-seg button{flex:1;font:inherit;font-weight:700;font-size:18px;min-height:48px;border-radius:12px;cursor:pointer;color:inherit;' +
      'background:color-mix(in srgb,var(--mp-ink) 6%,transparent);border:2px solid color-mix(in srgb,var(--mp-ink) 20%,transparent)}' +
      '.mp-seg button[aria-pressed=true]{background:var(--mp-accent);color:var(--mp-accent-ink);border-color:var(--mp-accent)}' +
      '.mp-volrow{display:flex;align-items:center;gap:12px;font-size:17px;font-weight:700}.mp-volrow output{min-width:3.2em;text-align:right}' +
      '.mp-range{-webkit-appearance:none;appearance:none;flex:1;height:10px;border-radius:6px;cursor:pointer;' +
      'background:linear-gradient(90deg,var(--mp-accent) var(--p,60%),color-mix(in srgb,var(--mp-ink) 18%,transparent) var(--p,60%))}' +
      '.mp-range::-webkit-slider-thumb{-webkit-appearance:none;width:30px;height:30px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#fff,var(--mp-accent) 60%);' +
      'border:2px solid color-mix(in srgb,var(--mp-accent) 60%,#000);box-shadow:0 3px 6px rgba(0,0,0,.4)}' +
      '.mp-range::-moz-range-thumb{width:28px;height:28px;border-radius:50%;background:var(--mp-accent);border:2px solid #0006}' +
      '.mp-pop .mp-trigger{width:100%;justify-content:flex-start;font-size:17px;min-height:48px}' +
      '.mp-btn.mp-off{opacity:.6}' +
      '.mp-flash{position:fixed;z-index:2147482500;left:50%;top:18px;transform:translateX(-50%);padding:10px 18px;border-radius:12px;background:#000c;color:#fff;font:700 20px/1 system-ui,sans-serif;pointer-events:none}';
    function iconSvg(sib) {
      var vb = (sib && sib.getAttribute('viewBox')) || '0 0 24 24', cls = sib && sib.getAttribute('class');
      var w = sib && sib.getAttribute('width'), h = sib && sib.getAttribute('height');
      return '<svg viewBox="' + vb + '"' + (cls ? ' class="' + cls + '"' : '') + (w ? ' width="' + w + '"' : '') + (h ? ' height="' + h + '"' : '') +
        ' fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + NOTE +
        '<g class="mp-slash" style="display:none">' + SLASH + '</g></svg>';
    }
    function mountControls() {
      var added = 0;
      [].forEach.call(document.querySelectorAll('[data-music-controls]'), function (slot) {
        if (slot.querySelector('.mp-btn')) return;
        added++;
        var like = slot.getAttribute('data-music-controls'), sib = null;
        if (like) try { sib = document.querySelector(like); } catch (e) { }
        if (!sib) {
          sib = slot.previousElementSibling; var guard = 0;
          while (sib && sib.tagName !== 'BUTTON' && guard++ < 4) sib = sib.previousElementSibling;
          if (!sib || sib.tagName !== 'BUTTON') { sib = slot.nextElementSibling; if (sib && sib.tagName !== 'BUTTON') sib = null; }
        }
        var b = document.createElement('button'); b.type = 'button';
        b.className = ((sib && sib.className) || '').split(/\s+/).filter(function (c) { return c && !/^(on|off|active|is-\w+|muted)$/.test(c) && !/toggle|mute|sound|theme|music/i.test(c); }).join(' ') + ' mp-btn';
        b.setAttribute('aria-label', 'Music'); b.setAttribute('aria-haspopup', 'dialog');
        b.title = 'Music (Shift+N)';
        b.innerHTML = iconSvg(sib && sib.querySelector('svg'));
        b.addEventListener('click', function (e) { e.preventDefault(); e.stopPropagation(); if (pop) closePop(); else openPop(b); });
        ['pointerdown', 'mousedown', 'touchstart'].forEach(function (ev) { b.addEventListener(ev, function (e) { e.stopPropagation(); }, { passive: true }); });
        slot.appendChild(b);
      });
      if (added) paint();
    }
    function paint(flash) {
      var off = !on || vol === 0;
      [].forEach.call(document.querySelectorAll('.mp-btn'), function (b) {
        // write only real changes: other observers on the page may react to any attribute write
        if (b.classList.contains('mp-off') !== off) b.classList.toggle('mp-off', off);
        var sl = b.querySelector('.mp-slash'), d = off ? '' : 'none'; if (sl && sl.style.display !== d) sl.style.display = d;
        var t = 'Music: ' + (on ? vol + '%' : 'off') + ' (Shift+N)'; if (b.title !== t) b.title = t;
      });
      if (pop) {
        pop.querySelectorAll('.mp-seg button').forEach(function (x) { x.setAttribute('aria-pressed', String((x.getAttribute('data-on') === '1') === on)); });
        var r = pop.querySelector('.mp-range'); if (r && +r.value !== vol) r.value = vol;
        if (r) { r.style.setProperty('--p', vol + '%'); r.setAttribute('aria-valuetext', vol + '%'); }
        var o = pop.querySelector('output'); if (o) o.textContent = vol + '%';
      }
      if (flash) {
        var f = document.querySelector('.mp-flash');
        if (!f) { f = document.createElement('div'); f.className = 'mp-flash'; document.body.appendChild(f); }
        f.textContent = 'Music ' + vol + '%'; clearTimeout(f._t); f._t = setTimeout(function () { f.remove(); }, 1500);
      }
    }
    function openPop(from) {
      ensureCss();
      if (!document.getElementById('mp-pop-style')) { var st = document.createElement('style'); st.id = 'mp-pop-style'; st.textContent = popCss; document.head.appendChild(st); }
      var v = themeVars(from);
      pop = document.createElement('div'); pop.className = 'mp-pop'; pop.setAttribute('role', 'dialog'); pop.setAttribute('aria-label', 'Music');
      ['--mp-bg', v.bg, '--mp-ink', v.ink, '--mp-accent', v.acc, '--mp-accent-ink', v.accInk, '--mp-font', v.font].reduce(function (k, x, i, a) { if (i % 2) pop.style.setProperty(a[i - 1], x); return 0; }, 0);
      pop.innerHTML = '<h3>Music</h3><div class="mp-seg"><button type="button" data-on="1">On</button><button type="button" data-on="0">Off</button></div>' +
        '<label class="mp-volrow"><input class="mp-range" type="range" min="0" max="100" step="1" aria-label="Music volume" value="' + vol + '"><output>' + vol + '%</output></label>';
      pop.appendChild(makeTrigger());
      var stopAll = function (e) { e.stopPropagation(); };
      ['pointerdown', 'mousedown', 'touchstart', 'click', 'keydown'].forEach(function (ev) { pop.addEventListener(ev, stopAll); });
      pop.addEventListener('click', function (e) { var x = e.target.closest('.mp-seg button'); if (x) setOn(x.getAttribute('data-on') === '1'); });
      var r = pop.querySelector('.mp-range');
      r.addEventListener('input', function () { setVol(r.value); });
      r.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowUp' || e.key === 'ArrowRight') { e.preventDefault(); setVol(vol + 5); }
        else if (e.key === 'ArrowDown' || e.key === 'ArrowLeft') { e.preventDefault(); setVol(vol - 5); }
        else if (e.key === 'Escape') closePop();
      });
      document.body.appendChild(pop); popFrom = from;
      var br = from.getBoundingClientRect(), pw = pop.offsetWidth, ph = pop.offsetHeight;
      var x = Math.min(window.innerWidth - pw - 10, Math.max(10, br.left + br.width / 2 - pw / 2));
      var y = br.bottom + 10; if (y + ph > window.innerHeight - 10) y = Math.max(10, br.top - ph - 10);
      pop.style.left = x + 'px'; pop.style.top = y + 'px';
      paint();
      setTimeout(function () { document.addEventListener('pointerdown', outside, true); document.addEventListener('keydown', escKey, true); }, 0);
    }
    function outside(e) { if (pop && !pop.contains(e.target) && !(popFrom && popFrom.contains(e.target)) && !(sheet && sheet.contains(e.target))) closePop(); }
    function escKey(e) { if (e.key === 'Escape' && pop && !sheet) { e.stopPropagation(); closePop(); } }
    function closePop() {
      if (!pop) return; pop.remove(); pop = null; popFrom = null;
      document.removeEventListener('pointerdown', outside, true); document.removeEventListener('keydown', escKey, true);
    }
    function bootUi() {
      mountControls();
      try { new MutationObserver(function () { mountControls(); }).observe(document.body, { childList: true, subtree: true }); } catch (e) { }
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', bootUi); else bootUi();
    M.setMuted = function (m) { muted = !!m; apply(); };
    // Fire music cues from the game's existing sound effects: hookSfx(sfx, { fanfare: 'win', buzz: 'fail' }).
    M.hookSfx = function (obj, map) {
      if (!obj) return 0; var n = 0;
      Object.keys(map).forEach(function (k) {
        var f = obj[k]; if (typeof f !== 'function' || f.__mp) return;
        var w = function () { var r = f.apply(this, arguments); try { M.cue(map[k]); if (map[k] === 'win') M.duck(3); } catch (e) { } return r; };
        w.__mp = true; obj[k] = w; n++;
      });
      M._hooked = (M._hooked || 0) + n; return n;
    };
    M.cue = function (name) { if (player) try { return player.cue(name); } catch (e) { } };
    M.duck = function (sec) { if (player) player.duck(sec || 2); };
    M.setMode = function (m) { modeOver = m || null; if (player) player.setMode(mode()); };
    M.setIntensity = function (x) { if (player) player.setIntensity(x); };
    M.toggle = function () { setOn(!on); };
    M.setVolume = function (v) { setVol(v); };
    M.state = function () { return { on: on, muted: muted, vol: vol, playing: !!player, track: player ? player.track : '', mode: mode(), bars: player ? player.bars : 0 }; };
  }
  if (me && me.hasAttribute('data-controller')) controller();

  // Preload the chosen track so it is ready by the first click.
  var first = wanted(); if (first) load(first).catch(function () { });
  function boot() {
    attach();
    try {
      var pending = 0;
      new MutationObserver(function () { if (pending) return; pending = requestAnimationFrame(function () { pending = 0; attach(); }); })
        .observe(document.body, { childList: true, subtree: true });
    } catch (e) { }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
