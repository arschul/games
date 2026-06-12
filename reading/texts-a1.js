/**
 * texts-a1.js
 * Shared reading text database — A1 level (CEFR)
 * 20 texts, ~100–150 words each
 * Topics: work, travel, technology, food, habits & routine,
 *         health, sports, nature, movies & series, music, and more.
 *
 * Companion files:
 *   texts-a2.js (150–250 words, A2 level)
 *   texts-b1.js (250–350 words, B1 level)
 *   texts-b2.js (400–500 words, B2 level)
 *
 * USAGE (ES Module):
 *   import { texts } from './texts-a1.js';
 *
 * USAGE (plain <script> tag — no module needed):
 *   <script src="texts-a1.js"></script>
 *   // then access window.A1Texts.texts
 *
 * USAGE (GitHub raw URL, any app in the same repo):
 *   import { texts } from 'https://raw.githubusercontent.com/YOUR_USER/YOUR_REPO/main/texts-a1.js';
 *   // or via jsDelivr CDN (recommended for raw GitHub files):
 *   import { texts } from 'https://cdn.jsdelivr.net/gh/YOUR_USER/YOUR_REPO@main/texts-a1.js';
 */

const texts = [
  // ── 1. WORK ──────────────────────────────────────────────────────────────
  {
    id: 1,
    title: "My First Day at Work",
    topic: "work",
    level: "A1",
    wordCount: 120,
    text: `My name is Lena. Today is my first day at my new job. I work in a small office in the city center. My desk is near the window. I have a computer, a phone, and a notebook on my desk.

My manager is very friendly. Her name is Maria. She shows me where everything is. There is a kitchen on the second floor. We can eat lunch there.

My colleagues are nice too. There are ten people in the office. We start work at nine o'clock in the morning and finish at six o'clock in the evening. We have one hour for lunch.

I am a little nervous, but I am also very happy. I think this is a good place to work.`
  },

  // ── 2. TRAVEL ────────────────────────────────────────────────────────────
  {
    id: 2,
    title: "A Weekend Trip",
    topic: "travel",
    level: "A1",
    wordCount: 118,
    text: `Last weekend, Tom and his sister went to the beach. They live in the city, so they took the train. The trip was about two hours long.

The beach was beautiful. The water was warm and the sky was blue. Tom swam in the sea. His sister sat on the sand and read a book.

They ate lunch at a small restaurant near the beach. Tom had fish and salad. His sister had pasta. The food was delicious.

In the afternoon, they walked along the beach and took many photos. They saw a beautiful sunset before they got on the train to go home.

Tom says he wants to go back next summer.`
  },

  // ── 3. TECHNOLOGY ────────────────────────────────────────────────────────
  {
    id: 3,
    title: "My Smartphone",
    topic: "technology",
    level: "A1",
    wordCount: 115,
    text: `I have a smartphone. I use it every day. My phone is very important for me.

In the morning, I use my phone to check the time. I also read the news and check my messages. I have many apps on my phone. I use a maps app when I go to a new place. I use a music app when I exercise.

My phone has a camera. I take photos of food, friends, and beautiful places. I share the photos online.

At night, I put my phone on my desk to charge. My parents always say I use my phone too much. Maybe they are right! But it is very useful. I cannot imagine my life without my smartphone.`
  },

  // ── 4. FOOD ──────────────────────────────────────────────────────────────
  {
    id: 4,
    title: "Cooking at Home",
    topic: "food",
    level: "A1",
    wordCount: 122,
    text: `Sara likes to cook. She cooks dinner every day at home. She thinks cooking is fun and healthy.

On Monday, she made vegetable soup. She used carrots, potatoes, and onions. It was easy to make. She ate the soup with bread.

On Wednesday, she made pasta with tomato sauce. She added garlic and olive oil. The pasta was very tasty.

Sara always goes to the market on Saturday morning. She buys fresh vegetables, fruit, and sometimes fish or chicken. She does not eat red meat.

Her friends love her cooking. They often come to her house for dinner. Sara is happy when people enjoy her food. She says the secret is to use fresh ingredients and cook with love.`
  },

  // ── 5. HABITS & ROUTINE ──────────────────────────────────────────────────
  {
    id: 5,
    title: "A Normal Morning",
    topic: "habits and routine",
    level: "A1",
    wordCount: 119,
    text: `Every morning, David wakes up at seven o'clock. He does not use an alarm. He just wakes up at the same time every day.

First, he drinks a glass of water. Then he goes to the bathroom to wash his face and brush his teeth. After that, he makes breakfast. He usually eats eggs and toast. He drinks one cup of coffee.

At eight o'clock, David leaves the house. He walks to the bus stop. The bus ride takes twenty minutes. He listens to a podcast on the bus.

He arrives at work at half past eight. He says good morning to his colleagues and starts his computer.

David thinks a good morning routine is very important for a happy day.`
  },

  // ── 6. HEALTH ────────────────────────────────────────────────────────────
  {
    id: 6,
    title: "Staying Healthy",
    topic: "health",
    level: "A1",
    wordCount: 121,
    text: `Ana wants to be healthy. She follows some simple rules every day.

She drinks eight glasses of water every day. She eats a lot of vegetables and fruit. She tries not to eat too much sugar. She does not smoke.

Ana goes to bed at ten o'clock every night. She sleeps for eight hours. She says sleep is very important for health.

Three times a week, she goes for a walk in the park. She also does yoga at home on the other days. She does not go to the gym. She says you do not need a gym to stay active.

Every year, she visits her doctor for a check-up. She believes that prevention is better than medicine. Ana feels happy and full of energy.`
  },

  // ── 7. SPORTS ────────────────────────────────────────────────────────────
  {
    id: 7,
    title: "Playing Football",
    topic: "sports",
    level: "A1",
    wordCount: 117,
    text: `Carlos loves football. He plays football every Saturday morning with his friends. They meet at the park at nine o'clock.

There are ten players on the field. They play for one hour. Carlos is a midfielder. He runs a lot during the game. He is very fast.

After the game, they are all tired and happy. They sit on the grass and drink water. Sometimes they go to a café near the park for coffee and sandwiches.

Carlos also watches football on television. His favorite team is from his city. He goes to the stadium a few times a year with his father.

Carlos says football is more than a sport. It is a way to make friends and have fun together.`
  },

  // ── 8. NATURE ────────────────────────────────────────────────────────────
  {
    id: 8,
    title: "The Forest",
    topic: "nature",
    level: "A1",
    wordCount: 116,
    text: `Near my town there is a big forest. I love going there on weekends.

The trees are very tall. In spring, the forest is full of green leaves and flowers. Birds sing in the morning. You can hear the sound of a small river too.

I often walk on the paths in the forest with my dog. My dog loves to run and play in the leaves. We walk for about one hour.

In autumn, the leaves turn orange, red, and yellow. It is very beautiful. I take many photos.

The forest is a quiet place. There are no cars or noise. I feel calm and relaxed when I am there. I think it is important to have nature near where we live.`
  },

  // ── 9. MOVIES & SERIES ───────────────────────────────────────────────────
  {
    id: 9,
    title: "Movie Night",
    topic: "movies and series",
    level: "A1",
    wordCount: 120,
    text: `On Friday evenings, Julia and her roommate watch a movie together. They call it "movie night." It is their favorite weekly tradition.

They take turns choosing the film. This week, Julia chose a comedy. Her roommate likes action movies, but he agreed. They made popcorn and sat on the sofa together.

The movie was about a man who loses his job and starts a new life in a small village. It was very funny. They laughed a lot.

Julia uses a streaming service to watch movies and series. She pays about ten dollars a month. She thinks it is a good price for so much content.

After the movie, they talked about their favorite scenes. Julia says movie night is a great way to relax after a long week.`
  },

  // ── 10. MUSIC ────────────────────────────────────────────────────────────
  {
    id: 10,
    title: "Learning the Guitar",
    topic: "music",
    level: "A1",
    wordCount: 118,
    text: `Mike started to learn the guitar six months ago. He always wanted to play a musical instrument.

He has lessons once a week with a teacher. His teacher is very patient. Mike also practices at home every evening for thirty minutes.

At first, it was difficult. His fingers hurt and the chords were hard. But now it is easier. He knows ten chords and can play some simple songs.

His favorite song to play is an old rock song. His family loves to listen when he plays.

Mike watches videos online to learn new techniques. He says the internet is a great resource for learning music.

He wants to play in front of people one day. Maybe at a small party or a family dinner. He is nervous but excited about that idea.`
  },

  // ── 11. SHOPPING ─────────────────────────────────────────────────────────
  {
    id: 11,
    title: "At the Supermarket",
    topic: "shopping",
    level: "A1",
    wordCount: 115,
    text: `Every Sunday, Grace goes to the supermarket. She makes a list before she leaves the house. She writes down everything she needs for the week.

At the supermarket, she starts with fruit and vegetables. Then she goes to the dairy section to get milk, cheese, and yogurt. She also buys bread, pasta, and rice.

Grace always looks at the prices. She buys products that are on sale when she can. She uses a loyalty card to get points and save money.

At the checkout, she pays by card. She uses reusable bags because she wants to protect the environment.

Shopping usually takes about forty-five minutes. She goes home, puts everything away, and makes a cup of tea. She says Sunday shopping is a very calm and satisfying activity.`
  },

  // ── 12. ANIMALS & PETS ───────────────────────────────────────────────────
  {
    id: 12,
    title: "My Cat",
    topic: "animals and pets",
    level: "A1",
    wordCount: 112,
    text: `I have a cat. Her name is Luna. She is two years old and she has grey and white fur.

Luna sleeps a lot. She usually sleeps on the sofa or on my bed. She wakes up when she is hungry. Her favorite food is tuna.

Every morning, I give Luna fresh water and food. I also clean her litter box. It is a little job, but I don't mind.

Luna loves to play. I have a small toy mouse for her. She runs and jumps when we play together.

She does not go outside. She is an indoor cat. But she sits by the window and looks at the birds outside.

I love Luna very much. She is good company, especially when I am alone at home.`
  },

  // ── 13. EDUCATION ────────────────────────────────────────────────────────
  {
    id: 13,
    title: "English Class",
    topic: "education",
    level: "A1",
    wordCount: 119,
    text: `My name is Paulo. I study English twice a week. My class is on Tuesday and Thursday evenings.

There are twelve students in my class. We are all adults. Some students want to travel. Others want to use English for work. I want to use English to watch movies without subtitles.

Our teacher is from Canada. Her name is Ms. Clark. She is funny and explains things very clearly. We do a lot of speaking activities in class.

We also have homework. I study for about twenty minutes at home every day. I use a vocabulary app on my phone to practice new words.

I started this class three months ago. At first, I was shy. Now I feel more confident when I speak. I am happy with my progress.`
  },

  // ── 14. WEATHER ──────────────────────────────────────────────────────────
  {
    id: 14,
    title: "A Rainy Day",
    topic: "weather",
    level: "A1",
    wordCount: 113,
    text: `Today it is raining. The sky is grey and it is cold outside. I do not want to go out.

I stay at home and drink hot tea. I look out the window and watch the rain fall on the street. The trees move in the wind.

On rainy days, I like to read a book or watch a series. Today I am reading a mystery novel. It is very interesting.

My cat Luna is sleeping next to me on the sofa. She looks very comfortable.

In the afternoon, the rain stops. The sun comes out for a short time. The street is wet and shiny. I open the window and I can smell the fresh air.

I actually like rainy days. They make me feel calm and cozy.`
  },

  // ── 15. SOCIAL MEDIA & THE INTERNET ──────────────────────────────────────
  {
    id: 15,
    title: "Using the Internet",
    topic: "technology",
    level: "A1",
    wordCount: 121,
    text: `Most people use the internet every day. We use it for many different things.

We use it to find information. If I have a question, I search for the answer online. It is very fast and easy.

I also use the internet to stay in contact with friends and family. I send messages and video call my parents, who live in another city. We talk on the weekend.

I watch videos and listen to music online too. I have a favorite channel about cooking. I learn new recipes from it.

For work, I send emails and join online meetings. My company uses the internet for almost everything.

Sometimes I worry about spending too much time online. It is important to take breaks and spend time away from screens. Balance is the key.`
  },

  // ── 16. HOLIDAYS & CELEBRATIONS ──────────────────────────────────────────
  {
    id: 16,
    title: "New Year's Eve",
    topic: "holidays and celebrations",
    level: "A1",
    wordCount: 116,
    text: `New Year's Eve is my favorite night of the year. It is the last day of December. People celebrate the end of the old year and the beginning of the new one.

In my family, we always have dinner together. My grandmother makes her special soup. We also eat rice, salad, and grilled chicken. After dinner, we play board games.

At midnight, we go outside to watch the fireworks. The sky is full of colors. Everyone shouts "Happy New Year!" and hugs.

We stay up late and talk about our memories from the year. We also talk about our plans and hopes for the next year.

I always feel excited and a little emotional on this night. It is a moment to be grateful and to look forward to new things.`
  },

  // ── 17. TRANSPORT & GETTING AROUND ───────────────────────────────────────
  {
    id: 17,
    title: "Getting to Work",
    topic: "travel",
    level: "A1",
    wordCount: 117,
    text: `My office is twelve kilometers from my home. I have different ways to get there.

On nice days, I ride my bicycle. It takes about thirty-five minutes. I enjoy the fresh air and the exercise. I go through a park, which is very pleasant.

When it rains or when I am late, I take the metro. There is a station near my house. The metro is fast. It takes only fifteen minutes. But it is often crowded in the morning.

Sometimes I take the bus. The bus is cheaper than the metro, but it is slower. I sit by the window and listen to music.

I never drive to work. There is a lot of traffic and parking is very expensive. I think public transport and cycling are better for the city and for health.`
  },

  // ── 18. SPORTS & FITNESS ─────────────────────────────────────────────────
  {
    id: 18,
    title: "Running in the Park",
    topic: "sports",
    level: "A1",
    wordCount: 114,
    text: `Elena started running six weeks ago. She runs three times a week in the park near her house.

At first, she could only run for five minutes. She stopped because she was out of breath. But she did not give up. She continued to practice.

Now she can run for thirty minutes without stopping. She is very proud of herself. She runs in the morning before work. She wakes up early, puts on her shoes, and goes to the park.

She wears comfortable clothes and uses a fitness app on her phone to track her distance and time.

Running makes Elena feel good. After a run, she has more energy for the rest of the day. She sleeps better too.

She wants to run a five-kilometer race before the end of the year.`
  },

  // ── 19. FOOD & RESTAURANTS ───────────────────────────────────────────────
  {
    id: 19,
    title: "Eating Out",
    topic: "food",
    level: "A1",
    wordCount: 118,
    text: `On Saturday, Jack and his friend went to a new restaurant in the city. The restaurant was Italian. Jack loves Italian food.

The waiter gave them the menu. There were many options. Jack chose pizza with tomatoes, cheese, and mushrooms. His friend chose pasta with cream sauce.

The restaurant was busy but not too noisy. The decoration was simple and nice. There were candles on the tables.

The food arrived in about twenty minutes. Jack's pizza was very good. The crust was thin and crispy. His friend said the pasta was delicious too.

For dessert, they shared a chocolate cake. It was rich and sweet.

The bill came to thirty-two euros for two people. Jack paid by card. He left a small tip because the service was excellent.

He wants to go back next month.`
  },

  // ── 20. ENVIRONMENT & NATURE ─────────────────────────────────────────────
  {
    id: 20,
    title: "Taking Care of the Planet",
    topic: "nature",
    level: "A1",
    wordCount: 120,
    text: `Many people today think about the environment. They want to take care of the planet.

There are simple things we can do every day. We can turn off the lights when we leave a room. We can take short showers to save water. We can walk or cycle instead of using a car.

We can also reduce waste. We can use reusable bags when we go shopping. We can recycle paper, plastic, and glass. We can buy less plastic.

In my neighborhood, there is a community garden. People grow vegetables there. It is a good way to produce food without much pollution.

I try to make small changes in my life. I know one person cannot change everything, but I believe that many small actions together can make a big difference for the future.`
  }
];

/**
 * Helper: get all unique topics in the database.
 * @returns {string[]}
 */
function getTopics() {
  return [...new Set(texts.map(t => t.topic))];
}

/**
 * Helper: filter texts by topic (case-insensitive, partial match).
 * @param {string} topic
 * @returns {object[]}
 */
function getByTopic(topic) {
  const q = topic.toLowerCase();
  return texts.filter(t => t.topic.toLowerCase().includes(q));
}

/**
 * Helper: get a single random text.
 * @returns {object}
 */
function getRandom() {
  return texts[Math.floor(Math.random() * texts.length)];
}

// ── Export ────────────────────────────────────────────────────────────────

// ES Module export (works with import/export syntax)
export { texts, getTopics, getByTopic, getRandom };
export default texts;

// Browser global (works with a plain <script src="texts-a1.js"> tag)
if (typeof window !== 'undefined') {
  window.A1Texts = { texts, getTopics, getByTopic, getRandom };
}
