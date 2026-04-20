/**
 * TRIVIA QUESTION DATABASE
 * For use with Brazilian teen students (ages 10-17)
 * Language: English
 * 20 categories × 10 questions each = 200 questions
 *
 * Structure per question:
 *   id       – unique string "CAT-001"
 *   q        – question text
 *   a        – correct answer
 *   wrong    – array of 3 plausible wrong answers
 *   points   – suggested Jeopardy-style value (100–500)
 *   hint     – optional one-line hint (can be shown after a wrong guess)
 *
 * Usage in any HTML app:
 *   <script src="questions-db.js"></script>
 *
 *   TriviaDB.getAllQuestions()
 *   TriviaDB.getByCategory("Brazil")
 *   TriviaDB.getRandom(10)
 *   TriviaDB.getRandom(10, ["Brazil", "Football"])
 *   TriviaDB.getShuffledOptions(question)   // returns [{text, correct}, ...] shuffled
 *   TriviaDB.buildJeopardyBoard(["Brazil", "Football"], [100,200,300,400,500])
 */

const TriviaDB = (() => {

  const categories = [

    // ─────────────────────────────────────────────
    //  1. BRAZIL — GEOGRAPHY & STATES
    // ─────────────────────────────────────────────
    {
      id: "Brazil",
      label: "Brazil",
      emoji: "🇧🇷",
      color: "green",
      questions: [
        {
          id: "BR-001", points: 100,
          q: "What is the capital of Tocantins?",
          a: "Palmas",
          wrong: ["Belém", "Salvador", "Natal"],
          hint: "It was built specifically to be the capital."
        },
        {
          id: "BR-002", points: 100,
          q: "How many states does Brazil have?",
          a: "26",
          wrong: ["24", "28", "30"],
          hint: "Plus the Federal District, which is not a state."
        },
        {
          id: "BR-003", points: 200,
          q: "What is the longest river entirely within Brazil?",
          a: "Rio São Francisco",
          wrong: ["Rio Tocantins", "Rio Paraná", "Rio Negro"],
          hint: "It is also called 'Velho Chico'."
        },
        {
          id: "BR-004", points: 200,
          q: "Which Brazilian state is the largest by area?",
          a: "Amazonas",
          wrong: ["Pará", "Mato Grosso", "Bahia"],
          hint: "It is in the Amazon region."
        },
        {
          id: "BR-005", points: 200,
          q: "What is the capital of the state of Minas Gerais?",
          a: "Belo Horizonte",
          wrong: ["Ouro Preto", "Uberlândia", "Juiz de Fora"],
          hint: "Its name means 'beautiful horizon'."
        },
        {
          id: "BR-006", points: 300,
          q: "The Pantanal, the world's largest tropical wetland, is mostly in which Brazilian state?",
          a: "Mato Grosso do Sul",
          wrong: ["Mato Grosso", "Tocantins", "Goiás"],
          hint: "Part of it also extends into Mato Grosso."
        },
        {
          id: "BR-007", points: 100,
          q: "Which Brazilian city is known as 'Cidade Maravilhosa' (Marvelous City)?",
          a: "Rio de Janeiro",
          wrong: ["São Paulo", "Recife", "Florianópolis"],
          hint: "It has a famous carnival and Sugarloaf Mountain."
        },
        {
          id: "BR-008", points: 200,
          q: "What is the capital of the state of Paraíba?",
          a: "João Pessoa",
          wrong: ["Maceió", "Fortaleza", "Recife"],
          hint: "It is known for its natural beauty."
        },
        {
          id: "BR-009", points: 200,
          q: "The Iguaçu Falls are on the border between Brazil and which other country?",
          a: "Argentina",
          wrong: ["Paraguay", "Uruguay", "Bolivia"],
          hint: "The falls are wider than Niagara."
        },
        {
          id: "BR-010", points: 400,
          q: "Which biome covers most of northeastern Brazil and is known for its dry climate and thorny vegetation?",
          a: "Caatinga",
          wrong: ["Cerrado", "Pampa", "Mata Atlântica"],
          hint: "It is a biome unique to Brazil."
        },
        {
          id: "BR-011", points: 500,
          q: "Which Brazilian state has the longest Atlantic coastline?",
          a: "Bahia",
          wrong: ["Maranhão", "Rio Grande do Norte", "Ceará"],
          hint: "It stretches roughly 1,100 km along the coast."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  2. BRAZIL — HISTORY & CULTURE
    // ─────────────────────────────────────────────
    {
      id: "BrazilHistory",
      label: "Brazil: History & Culture",
      emoji: "🏛️",
      color: "amber",
      questions: [
        {
          id: "BH-001", points: 100,
          q: "In what year did Brazil declare independence from Portugal?",
          a: "1822",
          wrong: ["1800", "1889", "1750"],
          hint: "Dom Pedro I proclaimed it on the banks of the Ipiranga river."
        },
        {
          id: "BH-002", points: 300,
          q: "Who was the first president of the Brazilian Republic?",
          a: "Deodoro da Fonseca",
          wrong: ["Floriano Peixoto", "Getúlio Vargas", "Dom Pedro II"],
          hint: "He was a military marshal who led the proclamation of the Republic."
        },
        {
          id: "BH-003", points: 200,
          q: "What was the name of the first Portuguese navigator to arrive in Brazil?",
          a: "Pedro Álvares Cabral",
          wrong: ["Vasco da Gama", "Fernão de Magalhães", "Bartolomeu Dias"],
          hint: "He arrived in 1500."
        },
        {
          id: "BH-004", points: 200,
          q: "The movement that ended slavery in Brazil in 1888 is associated with which princess?",
          a: "Princess Isabel",
          wrong: ["Princess Leopoldina", "Queen Maria I", "Princess Teresa Cristina"],
          hint: "She signed the Lei Áurea (Golden Law)."
        },
        {
          id: "BH-005", points: 300,
          q: "What is the name of the Indigenous group famous for first contact documented in the Carta de Pero Vaz de Caminha?",
          a: "Tupi",
          wrong: ["Guarani", "Yanomami", "Kayapó"],
          hint: "They lived along the Brazilian coast."
        },
        {
          id: "BH-006", points: 400,
          q: "The Semana de Arte Moderna (Modern Art Week) took place in São Paulo in which year?",
          a: "1922",
          wrong: ["1910", "1930", "1945"],
          hint: "It happened in the same year as the centenary of independence."
        },
        {
          id: "BH-007", points: 200,
          q: "What is Carnaval's most famous parade venue in Rio de Janeiro called?",
          a: "Sambódromo (Marquês de Sapucaí)",
          wrong: ["Maracanã", "Quinta da Boa Vista", "Aterro do Flamengo"],
          hint: "It was designed by Oscar Niemeyer."
        },
        {
          id: "BH-008", points: 100,
          q: "Brazil's official language is Portuguese because of its colonization by which country?",
          a: "Portugal",
          wrong: ["Spain", "France", "Netherlands"],
          hint: "A small European nation on the Atlantic coast."
        },
        {
          id: "BH-009", points: 300,
          q: "The city of Ouro Preto in Minas Gerais was the center of which historical economic cycle?",
          a: "Gold",
          wrong: ["Sugar", "Rubber", "Coffee"],
          hint: "Its name literally means 'black gold'."
        },
        {
          id: "BH-010", points: 300,
          q: "What famous Brazilian architect designed the main public buildings of Brasília?",
          a: "Oscar Niemeyer",
          wrong: ["Lúcio Costa", "Paulo Mendes da Rocha", "Ruy Ohtake"],
          hint: "He lived to be 104 years old."
        },
        {
          id: "BH-011", points: 500,
          q: "What was the name of the treaty signed in 1494 that divided the New World between Portugal and Spain?",
          a: "Treaty of Tordesillas",
          wrong: ["Treaty of Lisbon", "Treaty of Madrid", "Treaty of Utrecht"],
          hint: "It drew an imaginary line in the Atlantic Ocean."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  3. BIOLOGY
    // ─────────────────────────────────────────────
    {
      id: "Biology",
      label: "Biology",
      emoji: "🧬",
      color: "teal",
      questions: [
        {
          id: "BIO-001", points: 100,
          q: "What is the powerhouse of the cell?",
          a: "Mitochondria",
          wrong: ["Nucleus", "Ribosome", "Vacuole"],
          hint: "It produces ATP energy for the cell."
        },
        {
          id: "BIO-002", points: 100,
          q: "How many chromosomes do humans normally have?",
          a: "46",
          wrong: ["23", "48", "44"],
          hint: "They come in 23 pairs."
        },
        {
          id: "BIO-003", points: 100,
          q: "What gas do plants absorb from the air during photosynthesis?",
          a: "Carbon dioxide (CO₂)",
          wrong: ["Oxygen (O₂)", "Nitrogen (N₂)", "Hydrogen (H₂)"],
          hint: "Humans breathe this gas out."
        },
        {
          id: "BIO-004", points: 200,
          q: "What is the name of the process by which cells divide into two identical copies?",
          a: "Mitosis",
          wrong: ["Meiosis", "Osmosis", "Photosynthesis"],
          hint: "It produces genetically identical daughter cells."
        },
        {
          id: "BIO-005", points: 200,
          q: "Which organ produces insulin in the human body?",
          a: "Pancreas",
          wrong: ["Liver", "Kidney", "Spleen"],
          hint: "It is located near the stomach."
        },
        {
          id: "BIO-006", points: 300,
          q: "What is the scientific name for the domesticated dog?",
          a: "Canis lupus familiaris",
          wrong: ["Canis domesticus", "Felis catus", "Canis aureus"],
          hint: "It is classified as a subspecies of the wolf."
        },
        {
          id: "BIO-007", points: 100,
          q: "What type of blood cells carry oxygen through the body?",
          a: "Red blood cells (erythrocytes)",
          wrong: ["White blood cells", "Platelets", "Plasma cells"],
          hint: "They contain hemoglobin, which gives them their color."
        },
        {
          id: "BIO-008", points: 200,
          q: "What is the largest organ of the human body?",
          a: "Skin",
          wrong: ["Liver", "Brain", "Intestine"],
          hint: "It covers your entire body."
        },
        {
          id: "BIO-009", points: 100,
          q: "What molecule carries genetic information in living cells?",
          a: "DNA",
          wrong: ["RNA", "ATP", "Protein"],
          hint: "It has a famous double-helix shape."
        },
        {
          id: "BIO-010", points: 100,
          q: "Which animal is the largest on Earth?",
          a: "Blue whale",
          wrong: ["African elephant", "Giant squid", "Whale shark"],
          hint: "It lives in the ocean and is a mammal."
        },
        {
          id: "BIO-011", points: 400,
          q: "What is the name of the process by which plants lose water through their leaves?",
          a: "Transpiration",
          wrong: ["Evaporation", "Osmosis", "Respiration"],
          hint: "It is the plant equivalent of sweating."
        },
        {
          id: "BIO-012", points: 500,
          q: "What is the term for when a species mimics the appearance of a toxic species to avoid predators?",
          a: "Batesian mimicry",
          wrong: ["Müllerian mimicry", "Camouflage", "Aposematism"],
          hint: "Named after the English naturalist Henry Bates, who studied it in the Amazon."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  4. PHYSICS & CHEMISTRY
    // ─────────────────────────────────────────────
    {
      id: "PhysicsChem",
      label: "Physics & Chemistry",
      emoji: "⚗️",
      color: "blue",
      questions: [
        {
          id: "PC-001", points: 100,
          q: "What is the chemical symbol for water?",
          a: "H₂O",
          wrong: ["HO₂", "H₃O", "O₂H"],
          hint: "Two hydrogen atoms, one oxygen atom."
        },
        {
          id: "PC-002", points: 200,
          q: "What is the approximate speed of light in a vacuum?",
          a: "300,000 km/s",
          wrong: ["150,000 km/s", "500,000 km/s", "3,000 km/s"],
          hint: "Nothing in the universe travels faster."
        },
        {
          id: "PC-003", points: 200,
          q: "What is the atomic number of carbon?",
          a: "6",
          wrong: ["8", "12", "4"],
          hint: "It is the foundation of all organic life."
        },
        {
          id: "PC-004", points: 100,
          q: "What force keeps planets in orbit around the Sun?",
          a: "Gravity",
          wrong: ["Magnetism", "Friction", "Electrostatic force"],
          hint: "It also keeps you on the ground."
        },
        {
          id: "PC-005", points: 100,
          q: "On the Celsius scale, at what temperature does water boil at sea level?",
          a: "100°C",
          wrong: ["80°C", "120°C", "212°C"],
          hint: "Think of a pot of boiling water on a stove."
        },
        {
          id: "PC-006", points: 100,
          q: "What is the name of the negatively charged particle in an atom?",
          a: "Electron",
          wrong: ["Proton", "Neutron", "Photon"],
          hint: "It orbits the nucleus of the atom."
        },
        {
          id: "PC-007", points: 200,
          q: "What gas makes up about 78% of Earth's atmosphere?",
          a: "Nitrogen (N₂)",
          wrong: ["Oxygen (O₂)", "Carbon dioxide (CO₂)", "Argon (Ar)"],
          hint: "It is not the gas we breathe to survive."
        },
        {
          id: "PC-008", points: 200,
          q: "Which scientist formulated the three laws of motion?",
          a: "Isaac Newton",
          wrong: ["Albert Einstein", "Galileo Galilei", "Nikola Tesla"],
          hint: "An apple allegedly fell on his head."
        },
        {
          id: "PC-009", points: 200,
          q: "What is the chemical symbol for gold?",
          a: "Au",
          wrong: ["Go", "Gd", "Ag"],
          hint: "It comes from the Latin word 'aurum'."
        },
        {
          id: "PC-010", points: 200,
          q: "What type of energy is stored in food?",
          a: "Chemical energy",
          wrong: ["Kinetic energy", "Nuclear energy", "Thermal energy"],
          hint: "Your body converts it into movement and heat."
        },
        {
          id: "PC-011", points: 300,
          q: "What is the SI unit of electrical resistance?",
          a: "Ohm (Ω)",
          wrong: ["Volt (V)", "Ampere (A)", "Watt (W)"],
          hint: "Named after German physicist Georg Simon Ohm."
        },
        {
          id: "PC-012", points: 400,
          q: "What is the chemical symbol for iron on the periodic table?",
          a: "Fe",
          wrong: ["Ir", "In", "Fr"],
          hint: "It comes from the Latin word 'ferrum', meaning iron."
        },
        {
          id: "PC-013", points: 500,
          q: "What does Einstein's equation E=mc² say that energy equals?",
          a: "Mass times the speed of light squared",
          wrong: ["Mass times the speed of sound squared", "Mass times gravitational acceleration squared", "Momentum times the speed of light"],
          hint: "The 'c' stands for 'celeritas', the Latin word for speed."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  5. MATHEMATICS
    // ─────────────────────────────────────────────
    {
      id: "Math",
      label: "Mathematics",
      emoji: "📐",
      color: "purple",
      questions: [
        {
          id: "MA-001", points: 100,
          q: "What is the value of π (pi) to two decimal places?",
          a: "3.14",
          wrong: ["3.16", "3.12", "3.41"],
          hint: "It relates a circle's circumference to its diameter."
        },
        {
          id: "MA-002", points: 100,
          q: "What is the square root of 144?",
          a: "12",
          wrong: ["14", "11", "13"],
          hint: "Think: what number times itself equals 144?"
        },
        {
          id: "MA-003", points: 200,
          q: "In a right triangle, what is the name of the side opposite the right angle?",
          a: "Hypotenuse",
          wrong: ["Adjacent", "Opposite", "Bisector"],
          hint: "It is always the longest side of the triangle."
        },
        {
          id: "MA-004", points: 100,
          q: "What is 15% of 200?",
          a: "30",
          wrong: ["25", "35", "20"],
          hint: "10% of 200 is 20. Then add half of that."
        },
        {
          id: "MA-005", points: 100,
          q: "How many sides does a hexagon have?",
          a: "6",
          wrong: ["5", "7", "8"],
          hint: "Like a honeycomb cell."
        },
        {
          id: "MA-006", points: 200,
          q: "What is the formula for the area of a circle?",
          a: "A = πr²",
          wrong: ["A = 2πr", "A = πd", "A = r²"],
          hint: "r is the radius of the circle."
        },
        {
          id: "MA-007", points: 100,
          q: "What do you call a number that can only be divided by 1 and itself?",
          a: "Prime number",
          wrong: ["Even number", "Composite number", "Rational number"],
          hint: "Examples: 2, 3, 5, 7, 11…"
        },
        {
          id: "MA-008", points: 300,
          q: "What is 2 to the power of 10 (2¹⁰)?",
          a: "1024",
          wrong: ["512", "2048", "1000"],
          hint: "This number is also used in computing as 1 kilobyte."
        },
        {
          id: "MA-009", points: 300,
          q: "In the Fibonacci sequence (1, 1, 2, 3, 5…), what is the next number?",
          a: "8",
          wrong: ["7", "9", "10"],
          hint: "Each number is the sum of the two before it."
        },
        {
          id: "MA-010", points: 100,
          q: "What is the sum of all interior angles of a triangle?",
          a: "180 degrees",
          wrong: ["90 degrees", "270 degrees", "360 degrees"],
          hint: "This is true for any triangle, in any shape."
        },
        {
          id: "MA-011", points: 400,
          q: "What is the name of the theorem that states: in a right triangle, a² + b² = c²?",
          a: "Pythagorean theorem",
          wrong: ["Euclidean theorem", "Fermat's theorem", "Binomial theorem"],
          hint: "Named after an ancient Greek mathematician and philosopher."
        },
        {
          id: "MA-012", points: 500,
          q: "What is the only even prime number?",
          a: "2",
          wrong: ["0", "1", "4"],
          hint: "All other prime numbers are odd."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  6. WORLD GEOGRAPHY
    // ─────────────────────────────────────────────
    {
      id: "WorldGeo",
      label: "World Geography",
      emoji: "🌍",
      color: "teal",
      questions: [
        {
          id: "WG-001", points: 100,
          q: "What is the largest country in the world by area?",
          a: "Russia",
          wrong: ["Canada", "China", "United States"],
          hint: "It spans 11 time zones."
        },
        {
          id: "WG-002", points: 100,
          q: "What is the capital of Japan?",
          a: "Tokyo",
          wrong: ["Osaka", "Kyoto", "Hiroshima"],
          hint: "One of the world's most populated cities."
        },
        {
          id: "WG-003", points: 100,
          q: "On which continent is Egypt located?",
          a: "Africa",
          wrong: ["Asia", "Europe", "Middle East"],
          hint: "The Nile River flows through it."
        },
        {
          id: "WG-004", points: 200,
          q: "What is generally considered the longest river in the world?",
          a: "The Nile",
          wrong: ["The Amazon", "The Yangtze", "The Mississippi"],
          hint: "It flows through northeastern Africa into the Mediterranean Sea."
        },
        {
          id: "WG-005", points: 100,
          q: "What ocean lies between Europe/Africa and the Americas?",
          a: "Atlantic Ocean",
          wrong: ["Pacific Ocean", "Indian Ocean", "Arctic Ocean"],
          hint: "Brazil's coastline faces this ocean."
        },
        {
          id: "WG-006", points: 300,
          q: "What is the capital of Australia?",
          a: "Canberra",
          wrong: ["Sydney", "Melbourne", "Brisbane"],
          hint: "It is not the largest or most famous city."
        },
        {
          id: "WG-007", points: 200,
          q: "Which country has the largest population in the world?",
          a: "India",
          wrong: ["China", "United States", "Indonesia"],
          hint: "It recently surpassed its neighbor to the north."
        },
        {
          id: "WG-008", points: 200,
          q: "Mount Everest, the world's highest peak, is in which mountain range?",
          a: "The Himalayas",
          wrong: ["The Andes", "The Alps", "The Rockies"],
          hint: "Located on the border between Nepal and Tibet."
        },
        {
          id: "WG-009", points: 200,
          q: "What is the smallest country in the world?",
          a: "Vatican City",
          wrong: ["Monaco", "San Marino", "Liechtenstein"],
          hint: "It is located entirely within the city of Rome, Italy."
        },
        {
          id: "WG-010", points: 100,
          q: "The Sahara, the world's largest hot desert, is on which continent?",
          a: "Africa",
          wrong: ["Asia", "Australia", "South America"],
          hint: "It covers most of the northern part of that continent."
        },
        {
          id: "WG-011", points: 400,
          q: "What is the name of the narrow strip of land connecting North and South America?",
          a: "Isthmus of Panama",
          wrong: ["Strait of Magellan", "Isthmus of Suez", "Bering Strait"],
          hint: "A famous canal was built through it in 1914."
        },
        {
          id: "WG-012", points: 500,
          q: "Which African country has more pyramids than Egypt?",
          a: "Sudan",
          wrong: ["Ethiopia", "Libya", "Chad"],
          hint: "They were built by the ancient Nubian kingdoms."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  7. WORLD HISTORY
    // ─────────────────────────────────────────────
    {
      id: "WorldHistory",
      label: "World History",
      emoji: "📜",
      color: "amber",
      questions: [
        {
          id: "WH-001", points: 100,
          q: "In which year did World War II end?",
          a: "1945",
          wrong: ["1943", "1918", "1950"],
          hint: "V-E Day (Europe) was in May; V-J Day (Japan) in September."
        },
        {
          id: "WH-002", points: 100,
          q: "Who was the first person to walk on the Moon?",
          a: "Neil Armstrong",
          wrong: ["Buzz Aldrin", "Yuri Gagarin", "John Glenn"],
          hint: "Apollo 11 mission, July 1969."
        },
        {
          id: "WH-003", points: 100,
          q: "The Great Pyramid of Giza is in which country?",
          a: "Egypt",
          wrong: ["Iraq", "Saudi Arabia", "Sudan"],
          hint: "It is near the capital city Cairo."
        },
        {
          id: "WH-004", points: 200,
          q: "The Berlin Wall fell in which year, reuniting East and West Germany?",
          a: "1989",
          wrong: ["1991", "1985", "1975"],
          hint: "It was a defining moment of the end of the Cold War."
        },
        {
          id: "WH-005", points: 200,
          q: "Which civilization built Machu Picchu in Peru?",
          a: "The Inca",
          wrong: ["The Aztec", "The Maya", "The Olmec"],
          hint: "A great South American empire centered in the Andes."
        },
        {
          id: "WH-006", points: 100,
          q: "Who painted the Mona Lisa?",
          a: "Leonardo da Vinci",
          wrong: ["Michelangelo", "Raphael", "Caravaggio"],
          hint: "An Italian Renaissance genius who also studied science."
        },
        {
          id: "WH-007", points: 100,
          q: "In what year did Columbus first reach the Americas?",
          a: "1492",
          wrong: ["1500", "1488", "1510"],
          hint: "'In 1492, Columbus sailed the ocean blue.'"
        },
        {
          id: "WH-008", points: 200,
          q: "The French Revolution began in which year?",
          a: "1789",
          wrong: ["1776", "1804", "1799"],
          hint: "The storming of the Bastille prison."
        },
        {
          id: "WH-009", points: 200,
          q: "Who was the first woman to win a Nobel Prize?",
          a: "Marie Curie",
          wrong: ["Ada Lovelace", "Rosalind Franklin", "Florence Nightingale"],
          hint: "She actually won it twice — in Physics and Chemistry."
        },
        {
          id: "WH-010", points: 200,
          q: "Julius Caesar was a leader of which ancient civilization?",
          a: "Rome",
          wrong: ["Greece", "Egypt", "Carthage"],
          hint: "He was assassinated on the Ides of March, 44 BC."
        },
        {
          id: "WH-011", points: 300,
          q: "One of the Seven Wonders of the Ancient World was a towering structure built to guide sailors into a harbour in Egypt. What was it?",
          a: "The Lighthouse of Alexandria",
          wrong: ["The Colossus of Rhodes", "The Hanging Gardens of Babylon", "The Temple of Artemis"],
          hint: "It stood on the island of Pharos and was one of the tallest man-made structures for centuries."
        },
        {
          id: "WH-012", points: 400,
          q: "The 'Black Death' in 14th-century Europe was caused by which bacterium?",
          a: "Yersinia pestis",
          wrong: ["Mycobacterium tuberculosis", "Vibrio cholerae", "Clostridium botulinum"],
          hint: "It was spread mainly through fleas carried by rats."
        },
        {
          id: "WH-013", points: 500,
          q: "Which Roman emperor ordered the construction of the Colosseum in 72 AD?",
          a: "Vespasian",
          wrong: ["Nero", "Augustus", "Constantine"],
          hint: "He founded the Flavian dynasty."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  8. FOOTBALL (SOCCER)
    // ─────────────────────────────────────────────
    {
      id: "Football",
      label: "Football (Soccer)",
      emoji: "⚽",
      color: "green",
      questions: [
        {
          id: "FB-001", points: 100,
          q: "How many times has Brazil won the FIFA World Cup?",
          a: "5 times",
          wrong: ["4 times", "6 times", "3 times"],
          hint: "More than any other country in the world."
        },
        {
          id: "FB-002", points: 100,
          q: "Which Brazilian player is considered by many to be the greatest of all time and wore number 10?",
          a: "Pelé",
          wrong: ["Ronaldo Fenômeno", "Zico", "Romário"],
          hint: "He won three World Cups with Brazil."
        },
        {
          id: "FB-003", points: 100,
          q: "What is the name of the famous football stadium in Rio de Janeiro?",
          a: "Maracanã",
          wrong: ["Morumbis", "Arena Corinthians", "Mineirão"],
          hint: "It hosted the 2014 World Cup final."
        },
        {
          id: "FB-004", points: 100,
          q: "In football, how many players are on the field per team?",
          a: "11",
          wrong: ["10", "12", "9"],
          hint: "This includes the goalkeeper."
        },
        {
          id: "FB-005", points: 100,
          q: "Which country hosted the 2014 FIFA World Cup?",
          a: "Brazil",
          wrong: ["South Africa", "Russia", "Germany"],
          hint: "It was the second time this country hosted the tournament."
        },
        {
          id: "FB-006", points: 200,
          q: "Neymar Jr. played for which Spanish club before moving to PSG?",
          a: "FC Barcelona",
          wrong: ["Real Madrid", "Atletico Madrid", "Valencia"],
          hint: "He played alongside Messi and Suárez in a famous trio."
        },
        {
          id: "FB-007", points: 200,
          q: "In which year did Brazil suffer the famous 7-1 defeat to Germany at the World Cup?",
          a: "2014",
          wrong: ["2010", "2018", "2006"],
          hint: "The match was played in Belo Horizonte, Brazil."
        },
        {
          id: "FB-008", points: 200,
          q: "The Copa Libertadores is the most important club competition on which continent?",
          a: "South America",
          wrong: ["Europe", "Africa", "North America"],
          hint: "It is similar to the UEFA Champions League."
        },
        {
          id: "FB-009", points: 200,
          q: "Which Brazilian club is nicknamed 'Mengão' and is based in Rio de Janeiro?",
          a: "Flamengo",
          wrong: ["Fluminense", "Vasco da Gama", "Botafogo"],
          hint: "It has one of the largest fan bases in Brazil."
        },
        {
          id: "FB-010", points: 100,
          q: "What does VAR stand for in modern football?",
          a: "Video Assistant Referee",
          wrong: ["Visual Action Review", "Video Action Referee", "Virtual Assistant Review"],
          hint: "It uses video replay to review controversial decisions."
        },
        {
          id: "FB-011", points: 300,
          q: "Which country won the first ever FIFA World Cup in 1930?",
          a: "Uruguay",
          wrong: ["Argentina", "Brazil", "Italy"],
          hint: "The tournament was held on their home soil."
        },
        {
          id: "FB-012", points: 400,
          q: "Which player holds the record for most goals in a single World Cup tournament (13 goals in 1958)?",
          a: "Just Fontaine",
          wrong: ["Ronaldo", "Gerd Müller", "Eusébio"],
          hint: "He was a French striker of Moroccan descent."
        },
        {
          id: "FB-013", points: 500,
          q: "According to current FIFA rules, can a player be offside directly from a goal kick?",
          a: "No — there is no offside from a goal kick",
          wrong: ["Yes, the normal offside rule applies", "Only in extra time", "Only if the keeper takes it outside the box"],
          hint: "This rule was clarified and confirmed in 2019."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  9. SPORTS & OLYMPICS
    // ─────────────────────────────────────────────
    {
      id: "SportsMixed",
      label: "Sports & Olympics",
      emoji: "🏅",
      color: "coral",
      questions: [
        {
          id: "SM-001", points: 100,
          q: "How many rings are in the Olympic symbol?",
          a: "5",
          wrong: ["4", "6", "7"],
          hint: "Each ring represents one of the five continents."
        },
        {
          id: "SM-002", points: 100,
          q: "In basketball, how many points is a shot worth when scored from behind the arc?",
          a: "3 points",
          wrong: ["2 points", "4 points", "1 point"],
          hint: "It is called a 'three-pointer'."
        },
        {
          id: "SM-003", points: 100,
          q: "Capoeira is a martial art that originated in which country?",
          a: "Brazil",
          wrong: ["Angola", "Cuba", "Colombia"],
          hint: "It blends fighting with music and dance."
        },
        {
          id: "SM-004", points: 200,
          q: "In tennis, what is the score called when both players are tied at 40-40?",
          a: "Deuce",
          wrong: ["Tie", "Advantage", "Love"],
          hint: "The next point gives one player an 'advantage'."
        },
        {
          id: "SM-005", points: 100,
          q: "How long is an Olympic-size swimming pool?",
          a: "50 meters",
          wrong: ["25 meters", "100 meters", "75 meters"],
          hint: "Half the length is called a 'short course' pool."
        },
        {
          id: "SM-006", points: 200,
          q: "Brazilian athlete Rebeca Andrade won Olympic medals in which sport?",
          a: "Artistic gymnastics",
          wrong: ["Athletics (track and field)", "Swimming", "Rhythmic gymnastics"],
          hint: "She competed at the Tokyo and Paris Olympics."
        },
        {
          id: "SM-007", points: 100,
          q: "In volleyball, how many touches is a team allowed before sending the ball over the net?",
          a: "3",
          wrong: ["2", "4", "5"],
          hint: "Usually: receive, set, then attack."
        },
        {
          id: "SM-008", points: 200,
          q: "What is the name of the Brazilian martial art using grappling and ground fighting, now practiced worldwide?",
          a: "Brazilian Jiu-Jitsu (BJJ)",
          wrong: ["Capoeira", "Luta Livre", "Judo"],
          hint: "The Gracie family helped spread it globally."
        },
        {
          id: "SM-009", points: 400,
          q: "At the Paris 2024 Olympics, which sport made its Olympic debut?",
          a: "Breakdancing",
          wrong: ["Skateboarding", "Sport climbing", "Surfing"],
          hint: "It is a hip-hop street art form."
        },
        {
          id: "SM-010", points: 100,
          q: "In which sport would you perform a 'slam dunk'?",
          a: "Basketball",
          wrong: ["Volleyball", "Handball", "Water polo"],
          hint: "You jump and force the ball through the hoop."
        },
        {
          id: "SM-011", points: 300,
          q: "In the ancient Olympic Games, athletes originally competed in how many events?",
          a: "One (the stadion footrace)",
          wrong: ["Five", "Ten", "Three"],
          hint: "The Games started with just a single sprint of about 192 metres."
        },
        {
          id: "SM-012", points: 500,
          q: "What rule prevents a basketball team from moving back across the half-court line after crossing it?",
          a: "Backcourt violation",
          wrong: ["Goaltending", "Three-second violation", "Palming violation"],
          hint: "Once you cross mid-court, you cannot return to the backcourt."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  10. POP MUSIC
    // ─────────────────────────────────────────────
    {
      id: "PopMusic",
      label: "Pop Music",
      emoji: "🎵",
      color: "pink",
      questions: [
        {
          id: "PM-001", points: 100,
          q: "Which Brazilian singer had a global hit with 'Vai Malandra' and is known as Brazil's biggest pop star?",
          a: "Anitta",
          wrong: ["Claudia Leitte", "Ludmilla", "IZA"],
          hint: "She was the first Brazilian to top the Spotify global chart."
        },
        {
          id: "PM-002", points: 100,
          q: "The song 'Blinding Lights' was a massive hit for which artist?",
          a: "The Weeknd",
          wrong: ["Drake", "Post Malone", "Bruno Mars"],
          hint: "His real name is Abel Tesfaye, and he is Canadian."
        },
        {
          id: "PM-003", points: 200,
          q: "Taylor Swift's album 'Midnights' was released in which year?",
          a: "2022",
          wrong: ["2020", "2021", "2023"],
          hint: "It broke several streaming records on release night."
        },
        {
          id: "PM-004", points: 100,
          q: "The K-pop group BTS is from which country?",
          a: "South Korea",
          wrong: ["Japan", "China", "Thailand"],
          hint: "K-pop stands for 'Korean pop'."
        },
        {
          id: "PM-005", points: 100,
          q: "What music genre originated in Jamaica and is associated with Bob Marley?",
          a: "Reggae",
          wrong: ["Ska", "Reggaeton", "Calypso"],
          hint: "Characterized by offbeat rhythms and messages of peace."
        },
        {
          id: "PM-006", points: 200,
          q: "What was Billie Eilish's breakthrough hit song?",
          a: "Bad Guy",
          wrong: ["Lovely", "Ocean Eyes", "Happier Than Ever"],
          hint: "Famous for the whispered lyric 'duh'."
        },
        {
          id: "PM-007", points: 100,
          q: "Which music streaming platform is the most widely used in the world?",
          a: "Spotify",
          wrong: ["Apple Music", "YouTube Music", "Deezer"],
          hint: "It is a Swedish company founded in 2006."
        },
        {
          id: "PM-008", points: 200,
          q: "The musical genre 'Funk Carioca' (baile funk) originated in which Brazilian city?",
          a: "Rio de Janeiro",
          wrong: ["São Paulo", "Salvador", "Recife"],
          hint: "'Carioca' is the word for someone from that city."
        },
        {
          id: "PM-009", points: 100,
          q: "Shakira is a famous pop singer originally from which country?",
          a: "Colombia",
          wrong: ["Venezuela", "Argentina", "Mexico"],
          hint: "She also performed the FIFA World Cup song 'Waka Waka'."
        },
        {
          id: "PM-010", points: 100,
          q: "Which global pop star performed at the free concert on Copacabana beach in Rio in May 2024?",
          a: "Madonna",
          wrong: ["Beyoncé", "Lady Gaga", "Rihanna"],
          hint: "Over 1.6 million people attended."
        },
        {
          id: "PM-011", points: 300,
          q: "What genre blends rap and country music, popularized partly by Lil Nas X?",
          a: "Country rap (hick-hop)",
          wrong: ["Pop country", "Trap soul", "Americana rap"],
          hint: "Lil Nas X's 'Old Town Road' was a famous example."
        },
        {
          id: "PM-012", points: 400,
          q: "What is the term for the wavering effect a singer creates by rapidly varying pitch slightly?",
          a: "Vibrato",
          wrong: ["Falsetto", "Melisma", "Glissando"],
          hint: "Opera singers are particularly known for it."
        },
        {
          id: "PM-013", points: 500,
          q: "The opening guitar riff of 'Satisfaction' by The Rolling Stones was originally meant to be played by what instrument?",
          a: "Horns (brass section)",
          wrong: ["Keyboard", "Bass guitar", "Violin"],
          hint: "Keith Richards recorded it as a demo placeholder but the band kept it."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  11. MOVIES & SERIES
    // ─────────────────────────────────────────────
    {
      id: "MoviesSeries",
      label: "Movies & Series",
      emoji: "🎬",
      color: "purple",
      questions: [
        {
          id: "MS-001", points: 100,
          q: "In the Marvel Cinematic Universe, what is Iron Man's real name?",
          a: "Tony Stark",
          wrong: ["Steve Rogers", "Bruce Banner", "Peter Parker"],
          hint: "Played by Robert Downey Jr."
        },
        {
          id: "MS-002", points: 100,
          q: "The Brazilian film 'Cidade de Deus' (City of God) is set in which city?",
          a: "Rio de Janeiro",
          wrong: ["São Paulo", "Salvador", "Recife"],
          hint: "It was directed by Fernando Meirelles and released in 2002."
        },
        {
          id: "MS-003", points: 100,
          q: "In Harry Potter, what is the name of Harry's owl?",
          a: "Hedwig",
          wrong: ["Errol", "Pigwidgeon", "Fawkes"],
          hint: "A beautiful snowy white owl."
        },
        {
          id: "MS-004", points: 100,
          q: "The Netflix series 'Squid Game' is originally from which country?",
          a: "South Korea",
          wrong: ["Japan", "China", "Thailand"],
          hint: "It broke all Netflix viewing records when it launched."
        },
        {
          id: "MS-005", points: 100,
          q: "Which animated Disney film features the song 'Let It Go'?",
          a: "Frozen",
          wrong: ["Brave", "Moana", "Tangled"],
          hint: "It features two sister princesses, Elsa and Anna."
        },
        {
          id: "MS-006", points: 100,
          q: "In The Lion King, what is the name of Simba's evil uncle?",
          a: "Scar",
          wrong: ["Mufasa", "Shenzi", "Banzai"],
          hint: "He has a distinctive scar over one eye."
        },
        {
          id: "MS-007", points: 200,
          q: "The TV series 'Chaves', beloved in Brazil, was originally produced in which country?",
          a: "Mexico",
          wrong: ["Brazil", "Argentina", "Colombia"],
          hint: "It was created by comedian Roberto Bolaños ('Chespirito')."
        },
        {
          id: "MS-008", points: 100,
          q: "In Spider-Man, what gives Peter Parker his superpowers?",
          a: "A radioactive spider bite",
          wrong: ["A chemistry experiment gone wrong", "A gamma ray blast", "A serum injection"],
          hint: "It happens during a school field trip."
        },
        {
          id: "MS-009", points: 200,
          q: "What is the subtitle of the third Avengers movie, released in 2018?",
          a: "Infinity War",
          wrong: ["Age of Ultron", "Endgame", "Civil War"],
          hint: "The villain Thanos collects all six Infinity Stones."
        },
        {
          id: "MS-010", points: 300,
          q: "The animated film 'Encanto' (2021) is set in which country?",
          a: "Colombia",
          wrong: ["Brazil", "Mexico", "Peru"],
          hint: "It features the Madrigal family and the song 'We Don't Talk About Bruno'."
        },
        {
          id: "MS-011", points: 400,
          q: "What is the film technique of filming a long scene in a single unbroken take called?",
          a: "Long take",
          wrong: ["Match cut", "Tracking shot", "Dolly zoom"],
          hint: "Used famously in '1917' and 'Children of Men'."
        },
        {
          id: "MS-012", points: 500,
          q: "The 'Kuleshov Effect' in cinema states that:",
          a: "A shot's meaning changes depending on what comes before or after it",
          wrong: ["Miniature models can simulate large sets convincingly", "Two actors can be filmed separately and appear to interact", "Color grading changes the emotional tone of a scene"],
          hint: "Demonstrated by a Soviet filmmaker in the 1920s using the same neutral face next to different images."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  12. VIDEO GAMES
    // ─────────────────────────────────────────────
    {
      id: "VideoGames",
      label: "Video Games",
      emoji: "🎮",
      color: "blue",
      questions: [
        {
          id: "VG-001", points: 100,
          q: "In Minecraft, what is the main material used to build the Nether Portal?",
          a: "Obsidian",
          wrong: ["Blackstone", "Basalt", "Iron blocks"],
          hint: "It is formed when lava meets water."
        },
        {
          id: "VG-002", points: 100,
          q: "What is the name of the battle royale game developed by Epic Games?",
          a: "Fortnite",
          wrong: ["PUBG", "Warzone", "Free Fire"],
          hint: "Known for its building mechanic and colorful style."
        },
        {
          id: "VG-003", points: 100,
          q: "In the Super Mario franchise, which princess does Mario usually rescue?",
          a: "Princess Peach",
          wrong: ["Princess Zelda", "Princess Daisy", "Princess Rosalina"],
          hint: "She lives in the Mushroom Kingdom."
        },
        {
          id: "VG-004", points: 100,
          q: "What is the objective of the impostors in 'Among Us'?",
          a: "Eliminate crewmates without being identified",
          wrong: ["Complete tasks before crewmates", "Sabotage the ship and escape", "Collect all keys before crewmates"],
          hint: "They must avoid getting voted out."
        },
        {
          id: "VG-005", points: 100,
          q: "In Pokémon, what are the three starter types available at the beginning of a new game?",
          a: "Fire, Water, and Grass",
          wrong: ["Fire, Water, and Electric", "Fire, Rock, and Water", "Grass, Psychic, and Water"],
          hint: "Each type is strong against one and weak against another."
        },
        {
          id: "VG-006", points: 200,
          q: "What is the name of the main playable character in 'The Legend of Zelda' series?",
          a: "Link",
          wrong: ["Zelda", "Ganon", "Sheik"],
          hint: "Many people mistakenly call him by the title character's name."
        },
        {
          id: "VG-007", points: 200,
          q: "In which fighting game would you perform a 'Hadouken' (fireball move)?",
          a: "Street Fighter",
          wrong: ["Mortal Kombat", "Tekken", "Dragon Ball FighterZ"],
          hint: "It is Ryu's signature move."
        },
        {
          id: "VG-008", points: 100,
          q: "The EA Sports FC game series simulates which sport?",
          a: "Football (soccer)",
          wrong: ["Basketball", "American football", "Rugby"],
          hint: "Updated every year with real-world players and clubs."
        },
        {
          id: "VG-009", points: 100,
          q: "In Roblox, what is the in-game currency called?",
          a: "Robux",
          wrong: ["Roblox Coins", "R-Dollars", "V-Bucks"],
          hint: "You can use it to buy items and avatar accessories."
        },
        {
          id: "VG-010", points: 100,
          q: "In Minecraft, what is the name of the final boss?",
          a: "The Ender Dragon",
          wrong: ["The Wither", "The Elder Guardian", "The Evoker"],
          hint: "It lives in The End dimension."
        },
        {
          id: "VG-011", points: 300,
          q: "In online gaming, what does 'GG' stand for?",
          a: "Good game",
          wrong: ["Great going", "Get going", "Go go"],
          hint: "Typed in chat at the end of a match as a sign of sportsmanship."
        },
        {
          id: "VG-012", points: 400,
          q: "What programming language is most commonly used to develop games in the Unity engine?",
          a: "C#",
          wrong: ["C++", "Python", "Java"],
          hint: "It is pronounced 'C sharp'."
        },
        {
          id: "VG-013", points: 500,
          q: "The very first home video game console ever sold commercially was released in 1972. What was it called?",
          a: "Odyssey",
          wrong: ["Atari 2600", "Intellivision", "Coleco Telstar"],
          hint: "It was made by a company whose name means 'great voice' in Latin."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  13. TECHNOLOGY & INTERNET
    // ─────────────────────────────────────────────
    {
      id: "TechInternet",
      label: "Technology & Internet",
      emoji: "💻",
      color: "gray",
      questions: [
        {
          id: "TI-001", points: 100,
          q: "What does 'www' stand for in a website address?",
          a: "World Wide Web",
          wrong: ["World Wire Web", "Wireless World Web", "Wide World Web"],
          hint: "Invented by Tim Berners-Lee in 1989."
        },
        {
          id: "TI-002", points: 100,
          q: "What does 'AI' stand for?",
          a: "Artificial Intelligence",
          wrong: ["Automated Internet", "Advanced Integration", "Assisted Input"],
          hint: "ChatGPT and Claude are well-known examples."
        },
        {
          id: "TI-003", points: 100,
          q: "Which company created the Android operating system?",
          a: "Google",
          wrong: ["Samsung", "Apple", "Microsoft"],
          hint: "It is now owned by Google's parent company, Alphabet."
        },
        {
          id: "TI-004", points: 200,
          q: "How many bits are in one byte?",
          a: "8",
          wrong: ["4", "16", "10"],
          hint: "Each bit is a single 0 or 1."
        },
        {
          id: "TI-005", points: 200,
          q: "What programming language makes websites interactive directly in the browser?",
          a: "JavaScript",
          wrong: ["Python", "Java", "PHP"],
          hint: "Despite the name, it is very different from Java."
        },
        {
          id: "TI-006", points: 200,
          q: "What does 'URL' stand for?",
          a: "Uniform Resource Locator",
          wrong: ["Universal Resource Link", "Unified Remote Location", "Universal Reference Locator"],
          hint: "It is the address you type to visit a website."
        },
        {
          id: "TI-007", points: 100,
          q: "Which company owns Instagram, WhatsApp, and Facebook?",
          a: "Meta",
          wrong: ["Alphabet", "Microsoft", "ByteDance"],
          hint: "It was formerly known as Facebook, Inc."
        },
        {
          id: "TI-008", points: 300,
          q: "What does 'Wi-Fi' officially stand for?",
          a: "Wireless Fidelity",
          wrong: ["Wireless Finder", "Wide Field Internet", "Wireless Frequency Interface"],
          hint: "It was a marketing term modeled after the audio term 'Hi-Fi'."
        },
        {
          id: "TI-009", points: 100,
          q: "What is the most popular video-sharing platform in the world?",
          a: "YouTube",
          wrong: ["TikTok", "Instagram", "Twitch"],
          hint: "It is owned by Google."
        },
        {
          id: "TI-010", points: 300,
          q: "A hacker who tests systems with permission to find vulnerabilities is called what?",
          a: "White hat hacker",
          wrong: ["Black hat hacker", "Grey hat hacker", "Script kiddie"],
          hint: "The 'good' kind of hacker — hired to find weaknesses."
        },
        {
          id: "TI-011", points: 400,
          q: "What does 'HTTP' stand for?",
          a: "Hypertext Transfer Protocol",
          wrong: ["Hypertext Transmission Process", "High Transfer Text Protocol", "Hybrid Text Transfer Protocol"],
          hint: "The 'S' version (HTTPS) adds security encryption."
        },
        {
          id: "TI-012", points: 500,
          q: "In cybersecurity, what is a 'Trojan horse'?",
          a: "Malware disguised as legitimate software to trick users into installing it",
          wrong: ["A virus that spreads by duplicating itself across a network", "A program that encrypts files and demands a ransom", "A bot that floods a server with traffic"],
          hint: "Named after the wooden horse used by the Greeks to sneak into Troy."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  14. ANIMALS & NATURE
    // ─────────────────────────────────────────────
    {
      id: "AnimalsNature",
      label: "Animals & Nature",
      emoji: "🦁",
      color: "amber",
      questions: [
        {
          id: "AN-001", points: 100,
          q: "What is the fastest land animal on Earth?",
          a: "Cheetah",
          wrong: ["Leopard", "Pronghorn antelope", "Lion"],
          hint: "It can reach over 100 km/h in short bursts."
        },
        {
          id: "AN-002", points: 300,
          q: "How many hearts does an octopus have?",
          a: "3",
          wrong: ["1", "2", "4"],
          hint: "Two pump blood to the gills; one pumps to the rest of the body."
        },
        {
          id: "AN-003", points: 100,
          q: "Which Amazon animal is the world's largest rodent?",
          a: "Capybara",
          wrong: ["Nutria", "Beaver", "Paca"],
          hint: "It is semi-aquatic, social, and very friendly."
        },
        {
          id: "AN-004", points: 100,
          q: "What is the term for an animal that eats only plants?",
          a: "Herbivore",
          wrong: ["Carnivore", "Omnivore", "Insectivore"],
          hint: "The opposite of a carnivore."
        },
        {
          id: "AN-005", points: 100,
          q: "Which bear is native to China and eats mostly bamboo?",
          a: "Giant panda",
          wrong: ["Red panda", "Sun bear", "Brown bear"],
          hint: "Black and white, and endangered."
        },
        {
          id: "AN-006", points: 200,
          q: "What is the only mammal capable of true, sustained flight?",
          a: "Bat",
          wrong: ["Flying squirrel", "Sugar glider", "Colugo"],
          hint: "It uses echolocation to navigate in the dark."
        },
        {
          id: "AN-007", points: 100,
          q: "On which continent is the Amazon rainforest located?",
          a: "South America",
          wrong: ["Africa", "Asia", "Central America"],
          hint: "Most of it is in Brazil."
        },
        {
          id: "AN-008", points: 100,
          q: "Which is the largest wild cat in the Americas?",
          a: "Jaguar",
          wrong: ["Puma (mountain lion)", "Ocelot", "Leopard"],
          hint: "In Brazil it is called 'onça-pintada'."
        },
        {
          id: "AN-009", points: 400,
          q: "How long is a typical elephant pregnancy (gestation period)?",
          a: "About 22 months",
          wrong: ["About 12 months", "About 9 months", "About 18 months"],
          hint: "The longest gestation of any land animal."
        },
        {
          id: "AN-010", points: 100,
          q: "What is the name of the process by which a caterpillar transforms into a butterfly?",
          a: "Metamorphosis",
          wrong: ["Evolution", "Molting", "Pupation"],
          hint: "It happens while the caterpillar is inside a chrysalis."
        },
        {
          id: "AN-011", points: 500,
          q: "What is the biological process by which organisms like fireflies and deep-sea fish produce their own light?",
          a: "Bioluminescence",
          wrong: ["Phosphorescence", "Fluorescence", "Chemiluminescence"],
          hint: "It involves a chemical reaction between luciferin and an enzyme."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  15. ENGLISH LANGUAGE
    // ─────────────────────────────────────────────
    {
      id: "EnglishLang",
      label: "English Language",
      emoji: "📖",
      color: "coral",
      questions: [
        {
          id: "EL-001", points: 200,
          q: "What are the three degrees of comparison for adjectives in English?",
          a: "Positive, comparative, superlative",
          wrong: ["Simple, compound, complex", "Basic, relative, absolute", "Primary, secondary, tertiary"],
          hint: "Example: good → better → best."
        },
        {
          id: "EL-002", points: 100,
          q: "What word class (part of speech) does 'quickly' belong to?",
          a: "Adverb",
          wrong: ["Adjective", "Verb", "Preposition"],
          hint: "It modifies a verb — 'he ran quickly'."
        },
        {
          id: "EL-003", points: 100,
          q: "What is the past tense of the verb 'to go'?",
          a: "Went",
          wrong: ["Goed", "Gone", "Goes"],
          hint: "It is an irregular verb — does not follow the normal -ed rule."
        },
        {
          id: "EL-004", points: 300,
          q: "Which sentence is correct?",
          a: "Their dog is friendly",
          wrong: ["There dog is friendly", "They're dog is friendly", "Thier dog is friendly"],
          hint: "'Their' shows that something belongs to them."
        },
        {
          id: "EL-005", points: 100,
          q: "What is a synonym for the word 'enormous'?",
          a: "Huge",
          wrong: ["Tiny", "Moderate", "Average"],
          hint: "It means very large in size."
        },
        {
          id: "EL-006", points: 200,
          q: "Which letter is silent in the word 'knife'?",
          a: "K",
          wrong: ["N", "I", "F"],
          hint: "The word was once pronounced more fully in Old English."
        },
        {
          id: "EL-007", points: 100,
          q: "What is the plural of 'child'?",
          a: "Children",
          wrong: ["Childs", "Childes", "Childrens"],
          hint: "An irregular plural — it does not end in -s."
        },
        {
          id: "EL-008", points: 300,
          q: "What literary device is it when a character speaks their private thoughts aloud, alone on stage?",
          a: "Soliloquy",
          wrong: ["Monologue", "Aside", "Dialogue"],
          hint: "Hamlet's 'To be or not to be' is the most famous example."
        },
        {
          id: "EL-009", points: 100,
          q: "What does the prefix 'un-' mean in words like 'unhappy' or 'undo'?",
          a: "Not / reversal of action",
          wrong: ["Again", "Before", "Under"],
          hint: "It negates or reverses the meaning of the base word."
        },
        {
          id: "EL-010", points: 300,
          q: "Which sentence uses the present perfect tense correctly?",
          a: "I have finished my homework",
          wrong: ["I finished my homework yesterday", "I am finishing my homework", "I had finish my homework"],
          hint: "It uses 'have/has' + past participle."
        },
        {
          id: "EL-011", points: 400,
          q: "What is the grammatical term for words like 'although', 'because', and 'while' that connect clauses?",
          a: "Conjunction",
          wrong: ["Preposition", "Determiner", "Interjection"],
          hint: "They join two ideas and show the relationship between them."
        },
        {
          id: "EL-012", points: 500,
          q: "What figure of speech describes a word that imitates the natural sound it refers to, like 'buzz' or 'crash'?",
          a: "Onomatopoeia",
          wrong: ["Alliteration", "Assonance", "Synesthesia"],
          hint: "The word itself sounds like it means."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  16. SPACE & ASTRONOMY
    // ─────────────────────────────────────────────
    {
      id: "Space",
      label: "Space & Astronomy",
      emoji: "🚀",
      color: "blue",
      questions: [
        {
          id: "SP-001", points: 100,
          q: "How many planets are in our solar system?",
          a: "8",
          wrong: ["9", "7", "10"],
          hint: "Pluto was reclassified as a dwarf planet in 2006."
        },
        {
          id: "SP-002", points: 100,
          q: "What is the name of Earth's natural satellite?",
          a: "The Moon",
          wrong: ["Titan", "Io", "Ganymede"],
          hint: "It takes about 27 days to complete one orbit."
        },
        {
          id: "SP-003", points: 100,
          q: "Which planet is known as the Red Planet?",
          a: "Mars",
          wrong: ["Jupiter", "Saturn", "Venus"],
          hint: "NASA has sent several rovers there."
        },
        {
          id: "SP-004", points: 200,
          q: "What does a light-year actually measure?",
          a: "Distance",
          wrong: ["Time", "Speed", "Brightness of a star"],
          hint: "It is the distance light travels in one year."
        },
        {
          id: "SP-005", points: 100,
          q: "What is the name of the galaxy that contains our solar system?",
          a: "The Milky Way",
          wrong: ["Andromeda", "Triangulum", "Centaurus A"],
          hint: "You can see part of it as a band of light on clear nights."
        },
        {
          id: "SP-006", points: 300,
          q: "What is the closest star to Earth, after the Sun?",
          a: "Proxima Centauri",
          wrong: ["Sirius", "Alpha Centauri A", "Barnard's Star"],
          hint: "It is about 4.2 light-years away."
        },
        {
          id: "SP-007", points: 300,
          q: "At approximately what altitude does the International Space Station orbit Earth?",
          a: "About 400 km",
          wrong: ["About 100 km", "About 1,000 km", "About 36,000 km"],
          hint: "It travels at roughly 28,000 km/h."
        },
        {
          id: "SP-008", points: 200,
          q: "What astronomical event occurs when the Moon passes between the Earth and the Sun?",
          a: "Solar eclipse",
          wrong: ["Lunar eclipse", "Transit of Venus", "Supernova"],
          hint: "The Moon's shadow falls on part of Earth."
        },
        {
          id: "SP-009", points: 100,
          q: "Which is the largest planet in our solar system?",
          a: "Jupiter",
          wrong: ["Saturn", "Uranus", "Neptune"],
          hint: "It has a famous storm called the Great Red Spot."
        },
        {
          id: "SP-010", points: 200,
          q: "What is the name of NASA's space telescope, launched in 1990, that orbits above Earth's atmosphere?",
          a: "Hubble Space Telescope",
          wrong: ["James Webb Space Telescope", "Chandra X-ray Observatory", "Spitzer Space Telescope"],
          hint: "It has produced many iconic images of distant galaxies."
        },
        {
          id: "SP-011", points: 400,
          q: "What is the boundary around a black hole beyond which nothing — not even light — can escape?",
          a: "Event horizon",
          wrong: ["Schwarzschild radius", "Photon sphere", "Singularity"],
          hint: "Once crossed, there is no return."
        },
        {
          id: "SP-012", points: 500,
          q: "What is the theoretical point of infinite density at the center of a black hole called?",
          a: "Singularity",
          wrong: ["Neutron core", "Event horizon", "Quasar nucleus"],
          hint: "At this point, the known laws of physics break down completely."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  17. FOOD & CULTURE
    // ─────────────────────────────────────────────
    {
      id: "FoodCulture",
      label: "Food & Culture",
      emoji: "🍽️",
      color: "coral",
      questions: [
        {
          id: "FC-001", points: 100,
          q: "What is the national dish of Brazil?",
          a: "Feijoada",
          wrong: ["Moqueca", "Churrasco", "Coxinha"],
          hint: "A slow-cooked black bean and pork stew."
        },
        {
          id: "FC-002", points: 100,
          q: "From which country does sushi originally come?",
          a: "Japan",
          wrong: ["China", "South Korea", "Vietnam"],
          hint: "It uses vinegared rice and often raw fish."
        },
        {
          id: "FC-003", points: 100,
          q: "What is the main ingredient in guacamole?",
          a: "Avocado",
          wrong: ["Tomato", "Mango", "Papaya"],
          hint: "A creamy green fruit."
        },
        {
          id: "FC-004", points: 100,
          q: "Pizza is originally from which country?",
          a: "Italy",
          wrong: ["Greece", "United States", "France"],
          hint: "Specifically from the city of Naples."
        },
        {
          id: "FC-005", points: 100,
          q: "What traditional Brazilian sweet is covered in chocolate sprinkles and served at every birthday party?",
          a: "Brigadeiro",
          wrong: ["Cocada", "Paçoca", "Beijinho"],
          hint: "Made from condensed milk, cocoa powder, and butter."
        },
        {
          id: "FC-006", points: 100,
          q: "Açaí berries, popular in Brazilian bowls, grow in which biome?",
          a: "Amazon rainforest",
          wrong: ["Cerrado", "Mata Atlântica", "Pantanal"],
          hint: "They come from a type of palm tree."
        },
        {
          id: "FC-007", points: 100,
          q: "Coxinha is a popular Brazilian street food. What is its traditional filling?",
          a: "Shredded chicken",
          wrong: ["Cheese and ham", "Ground beef", "Shrimp"],
          hint: "It is shaped like a teardrop and fried in batter."
        },
        {
          id: "FC-008", points: 200,
          q: "From which country does the dish ramen (noodle soup) originate?",
          a: "Japan",
          wrong: ["China", "South Korea", "Vietnam"],
          hint: "It became iconic Japanese street food in the 20th century."
        },
        {
          id: "FC-009", points: 200,
          q: "Tapioca, a popular Brazilian snack, is made from flour extracted from which plant?",
          a: "Cassava",
          wrong: ["Corn", "Wheat", "Rice"],
          hint: "It is a starchy root widely grown in Brazil."
        },
        {
          id: "FC-010", points: 200,
          q: "Which traditional Brazilian festival is famous for forró music, quadrilha dancing, and foods like pamonha?",
          a: "Festa Junina",
          wrong: ["Carnaval", "Bumba Meu Boi", "Círio de Nazaré"],
          hint: "Celebrated every June, especially in the Northeast."
        },
        {
          id: "FC-011", points: 300,
          q: "What is the traditional Japanese rice wine called?",
          a: "Sake",
          wrong: ["Soju", "Mirin", "Shochu"],
          hint: "It is brewed from fermented rice and served warm or cold."
        },
        {
          id: "FC-012", points: 400,
          q: "What chemical reaction is responsible for the browning and crust formation when meat or bread is cooked at high heat?",
          a: "Maillard reaction",
          wrong: ["Caramelization", "Fermentation", "Emulsification"],
          hint: "It involves a reaction between amino acids and sugars at high temperatures."
        },
        {
          id: "FC-013", points: 500,
          q: "Which spice — historically more valuable than gold by weight — comes from the stigmas of the Crocus sativus flower and requires over 75,000 flowers to produce 500g?",
          a: "Saffron",
          wrong: ["Cardamom", "Vanilla", "White truffle"],
          hint: "It gives paella and risotto Milanese their distinctive golden color."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  18. HUMAN BODY & HEALTH
    // ─────────────────────────────────────────────
    {
      id: "HumanBody",
      label: "Human Body & Health",
      emoji: "🫀",
      color: "red",
      questions: [
        {
          id: "HB-001", points: 200,
          q: "How many bones are in the adult human body?",
          a: "206",
          wrong: ["212", "198", "300"],
          hint: "Babies are born with more — some fuse together over time."
        },
        {
          id: "HB-002", points: 200,
          q: "What is the longest bone in the human body?",
          a: "Femur (thigh bone)",
          wrong: ["Tibia (shin bone)", "Humerus (upper arm)", "Fibula"],
          hint: "It is located in your upper leg."
        },
        {
          id: "HB-003", points: 100,
          q: "What does the heart pump throughout the body?",
          a: "Blood",
          wrong: ["Oxygen", "Lymph fluid", "Water"],
          hint: "It carries oxygen, nutrients, and waste products."
        },
        {
          id: "HB-004", points: 100,
          q: "How many hours of sleep per night are generally recommended for teenagers?",
          a: "8–10 hours",
          wrong: ["6–7 hours", "5–6 hours", "10–12 hours"],
          hint: "Teenagers need more sleep than adults."
        },
        {
          id: "HB-005", points: 200,
          q: "Which vitamin is produced by the human skin when exposed to sunlight?",
          a: "Vitamin D",
          wrong: ["Vitamin C", "Vitamin A", "Vitamin B12"],
          hint: "It is essential for bone health and the immune system."
        },
        {
          id: "HB-006", points: 300,
          q: "What part of the eye gives it its color and controls how much light enters?",
          a: "Iris",
          wrong: ["Pupil", "Cornea", "Retina"],
          hint: "The pupil is the dark opening in the center of it."
        },
        {
          id: "HB-007", points: 200,
          q: "What are the four main human blood types?",
          a: "A, B, AB, and O",
          wrong: ["A, B, C, and D", "A, B, O, and Z", "A, B, AB, and C"],
          hint: "They can also be positive or negative (Rh factor)."
        },
        {
          id: "HB-008", points: 100,
          q: "Which organ filters waste from the blood and produces urine?",
          a: "Kidneys",
          wrong: ["Liver", "Bladder", "Spleen"],
          hint: "You have two of them, on either side of your spine."
        },
        {
          id: "HB-009", points: 400,
          q: "What brain region, shaped like a seahorse, is responsible for memory formation?",
          a: "Hippocampus",
          wrong: ["Amygdala", "Cerebellum", "Frontal lobe"],
          hint: "Its name comes from the Greek word for 'seahorse'."
        },
        {
          id: "HB-010", points: 100,
          q: "How many teeth do adult humans typically have, including wisdom teeth?",
          a: "32",
          wrong: ["28", "30", "36"],
          hint: "Children have only 20 baby teeth."
        },
        {
          id: "HB-011", points: 500,
          q: "What is the name of the pigment protein responsible for the color of human skin, hair, and eyes?",
          a: "Melanin",
          wrong: ["Keratin", "Collagen", "Hemoglobin"],
          hint: "It is produced by specialized cells called melanocytes."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  19. ENVIRONMENT & SUSTAINABILITY
    // ─────────────────────────────────────────────
    {
      id: "Environment",
      label: "Environment & Sustainability",
      emoji: "🌱",
      color: "green",
      questions: [
        {
          id: "EN-001", points: 100,
          q: "What gas, released by burning fossil fuels, is most responsible for climate change?",
          a: "Carbon dioxide (CO₂)",
          wrong: ["Oxygen (O₂)", "Methane (CH₄)", "Nitrogen (N₂)"],
          hint: "Plants absorb it during photosynthesis."
        },
        {
          id: "EN-002", points: 100,
          q: "What term describes energy sources like solar, wind, and hydropower that do not run out?",
          a: "Renewable energy",
          wrong: ["Nuclear energy", "Fossil fuel energy", "Thermal energy"],
          hint: "The opposite of coal, oil, and gas."
        },
        {
          id: "EN-003", points: 200,
          q: "What is the term for the variety of plant and animal life in a particular habitat?",
          a: "Biodiversity",
          wrong: ["Ecosystem", "Biosphere", "Food chain"],
          hint: "Brazil has the highest level of this in the world."
        },
        {
          id: "EN-004", points: 100,
          q: "The '3 R's' of sustainability are Reduce, Reuse, and ___?",
          a: "Recycle",
          wrong: ["Repair", "Refuse", "Replace"],
          hint: "Turning waste materials into new products."
        },
        {
          id: "EN-005", points: 200,
          q: "What is one of the main causes of rising sea levels worldwide?",
          a: "Melting ice caps and glaciers due to global warming",
          wrong: ["More rain falling into the ocean", "Tectonic plates shifting ocean floors", "Increased river flow into the sea"],
          hint: "As Earth's temperature rises, polar ice melts into the sea."
        },
        {
          id: "EN-006", points: 300,
          q: "What is the name of the 2015 international climate agreement signed in France?",
          a: "Paris Agreement",
          wrong: ["Kyoto Protocol", "Montreal Protocol", "Copenhagen Accord"],
          hint: "Countries pledged to limit global temperature rise."
        },
        {
          id: "EN-007", points: 300,
          q: "What type of pollution refers to excessive artificial light at night?",
          a: "Light pollution",
          wrong: ["Visual pollution", "Thermal pollution", "Noise pollution"],
          hint: "It prevents us from seeing stars and harms nocturnal animals."
        },
        {
          id: "EN-008", points: 300,
          q: "Approximately how many years does it take a plastic bottle to decompose in nature?",
          a: "About 450 years",
          wrong: ["About 50 years", "About 100 years", "About 20 years"],
          hint: "Far longer than any human lifetime."
        },
        {
          id: "EN-009", points: 200,
          q: "The hole in the ozone layer is mainly found above which region of Earth?",
          a: "Antarctica",
          wrong: ["The Arctic", "The Sahara Desert", "The Amazon rainforest"],
          hint: "It is at the South Pole."
        },
        {
          id: "EN-010", points: 400,
          q: "Approximately what percentage of the world's freshwater is found in Brazil?",
          a: "About 12%",
          wrong: ["About 5%", "About 25%", "About 3%"],
          hint: "Brazil holds the Amazon River and the Pantanal."
        },
        {
          id: "EN-011", points: 500,
          q: "Approximately when did the total mass of all plastic ever produced surpass the total mass of all living animals on Earth?",
          a: "Around 2020",
          wrong: ["Around 2050", "Around 2075", "Around 2100"],
          hint: "Plastic production accelerated so fast that this milestone came much earlier than scientists predicted."
        },
      ]
    },

    // ─────────────────────────────────────────────
    //  20. FUN FACTS
    // ─────────────────────────────────────────────
    {
      id: "FunFacts",
      label: "Fun Facts",
      emoji: "🤯",
      color: "pink",
      questions: [
        {
          id: "FF-001", points: 400,
          q: "A snail can sleep for how long at a time?",
          a: "Up to 3 years",
          wrong: ["Up to 3 months", "Up to 6 weeks", "Up to 1 year"],
          hint: "It hibernates during periods of drought."
        },
        {
          id: "FF-002", points: 300,
          q: "Approximately how many languages are spoken in the world today?",
          a: "About 7,000",
          wrong: ["About 700", "About 200", "About 3,000"],
          hint: "About half of them are considered endangered."
        },
        {
          id: "FF-003", points: 300,
          q: "Approximately what percentage of Earth's oceans have been explored by humans?",
          a: "About 20%",
          wrong: ["About 80%", "About 50%", "About 5%"],
          hint: "We actually know more about the surface of the Moon."
        },
        {
          id: "FF-004", points: 300,
          q: "The hashtag symbol (#) is officially called what?",
          a: "Octothorpe",
          wrong: ["Pound sign", "Hash mark", "Crosshatch"],
          hint: "Most people don't know its official name."
        },
        {
          id: "FF-005", points: 400,
          q: "Honey found in ancient Egyptian tombs was still edible after how many years?",
          a: "Over 3,000 years",
          wrong: ["About 100 years", "About 500 years", "About 1,000 years"],
          hint: "Honey never spoils if stored sealed and dry."
        },
        {
          id: "FF-006", points: 400,
          q: "Approximately how many muscles does the human body use to take a single step?",
          a: "About 200",
          wrong: ["About 20", "About 50", "About 500"],
          hint: "Walking is far more complex than it seems."
        },
        {
          id: "FF-007", points: 400,
          q: "The word 'robot' comes from a Czech word that means what?",
          a: "Forced labor",
          wrong: ["Metal man", "Thinking machine", "Servant"],
          hint: "From Karel Čapek's 1920 play 'R.U.R.'."
        },
        {
          id: "FF-008", points: 500,
          q: "If you removed all the empty space from atoms in every human on Earth, we would all fit inside what?",
          a: "A sugar cube",
          wrong: ["A football stadium", "A house", "A city block"],
          hint: "Atoms are almost entirely empty space."
        },
        {
          id: "FF-009", points: 500,
          q: "How many times does a hummingbird flap its wings per second?",
          a: "About 50–80 times",
          wrong: ["About 5–10 times", "About 200 times", "About 20–30 times"],
          hint: "This is what creates their distinctive humming sound."
        },
        {
          id: "FF-010", points: 500,
          q: "Cleopatra of Egypt lived closer in time to which historical event?",
          a: "The Moon landing (1969)",
          wrong: ["The construction of the Great Pyramid", "The invention of the wheel", "The invention of writing"],
          hint: "The Great Pyramid was built ~2560 BC; Cleopatra lived ~50 BC."
        },
        {
          id: "FF-011", points: 100,
          q: "How many sides does a standard die (dice) have?",
          a: "6",
          wrong: ["4", "8", "12"],
          hint: "It is a cube."
        },
        {
          id: "FF-012", points: 200,
          q: "What is the name of the fear of spiders?",
          a: "Arachnophobia",
          wrong: ["Agoraphobia", "Claustrophobia", "Acrophobia"],
          hint: "'Arachne' is the Greek word for spider."
        },
      ]
    },

  ]; // end categories


  // ─────────────────────────────────────────────
  //  PUBLIC API
  // ─────────────────────────────────────────────

  /** Return all categories */
  function getCategories() {
    return categories;
  }

  /** Flat array of every question across all categories */
  function getAllQuestions() {
    return categories.flatMap(cat =>
      cat.questions.map(q => ({ ...q, category: cat.id, categoryLabel: cat.label }))
    );
  }

  /**
   * Questions for one or more category ids.
   * @param {string|string[]} ids
   */
  function getByCategory(ids) {
    const target = Array.isArray(ids) ? ids : [ids];
    return categories
      .filter(cat => target.includes(cat.id))
      .flatMap(cat =>
        cat.questions.map(q => ({ ...q, category: cat.id, categoryLabel: cat.label }))
      );
  }

  /**
   * Random sample of N questions.
   * @param {number} n
   * @param {string[]} [fromCategories] - optional category filter
   */
  function getRandom(n, fromCategories) {
    const pool = fromCategories ? getByCategory(fromCategories) : getAllQuestions();
    return [...pool].sort(() => Math.random() - 0.5).slice(0, n);
  }

  /** All questions matching a specific point value */
  function getByPoints(points) {
    return getAllQuestions().filter(q => q.points === points);
  }

  /**
   * Returns all 4 answer options shuffled in random order.
   * Each item: { text: string, correct: boolean }
   * Perfect for multiple-choice rendering.
   * @param {object} question
   */
  function getShuffledOptions(question) {
    const options = [
      { text: question.a, correct: true },
      ...question.wrong.map(w => ({ text: w, correct: false }))
    ];
    return options.sort(() => Math.random() - 0.5);
  }

  /**
   * Build a Jeopardy-style board structure.
   * @param {string[]} [catIds] - which categories to include (defaults to all)
   * @param {number[]} [tiers]  - point value rows (default [100,200,300,400,500])
   */
  function buildJeopardyBoard(catIds, tiers = [100, 200, 300, 400, 500]) {
    const cats = catIds
      ? categories.filter(c => catIds.includes(c.id))
      : categories;

    return cats.map(cat => ({
      id: cat.id,
      label: cat.label,
      emoji: cat.emoji,
      color: cat.color,
      clues: tiers.map(pts => {
        const match = cat.questions.find(q => q.points === pts);
        return match ? { ...match, category: cat.id, categoryLabel: cat.label } : null;
      })
    }));
  }

  return {
    categories,
    getCategories,
    getAllQuestions,
    getByCategory,
    getRandom,
    getByPoints,
    getShuffledOptions,
    buildJeopardyBoard,
  };

})();

// CommonJS / Node support
if (typeof module !== "undefined" && module.exports) {
  module.exports = TriviaDB;
}
