/**
 * TRIVIA QUESTION DATABASE
 * For use with Brazilian teen students (ages 10-17)
 * Language: English
 * 20 categories, 357 questions (>= 3 at every point value in every category)
 *
 * Structure per question:
 *   id       – unique string "CAT-001"
 *   q        – question text (<= 110 chars; it gets projected in a classroom)
 *   a        – correct answer
 *   wrong    – array of 3 plausible wrong answers
 *   points   – Jeopardy-style value 100-500: how hard the ANSWER is to know
 *   cefr     – "A2" | "B1" | "B2": how hard the QUESTION is to READ.
 *              Deliberately independent of points — plenty of 500-point
 *              questions are written in simple A2 English so that lower-level
 *              classes can still play for the big values.
 *              A2 = high-frequency words, short simple sentences
 *              B1 = some lower-frequency vocabulary, longer sentences
 *              B2 = academic/technical register, dense noun phrases
 *   hint     – one-line clue; Trivia Badge Hunters sells it for half points
 *
 * Usage in any HTML app:
 *   <script src="questions-db.js"></script>
 *
 *   TriviaDB.getAllQuestions()
 *   TriviaDB.getByCategory("Brazil")
 *   TriviaDB.getRandom(10)
 *   TriviaDB.getRandom(10, ["Brazil", "Football"])
 *   TriviaDB.getByLevel(["A2", "B1"])                 // filter by reading level
 *   TriviaDB.getCategoriesByLevel(["A2"])             // categories, questions filtered
 *   TriviaDB.getShuffledOptions(question)   // returns [{text, correct}, ...] shuffled
 *   TriviaDB.buildJeopardyBoard(["Brazil", "Football"], [100,200,300,400,500])
 */

const TriviaDB = (() => {

  const categories = [

    // ─────────────────────────────────────────────
    //  1. BRAZIL
    // ─────────────────────────────────────────────
    {
      id: "Brazil",
      label: "Brazil",
      emoji: "🇧🇷",
      color: "green",
      questions: [
        {
          id: "BR-001", points: 100, cefr: "A2",
          q: "What is the capital of Tocantins?",
          a: "Palmas",
          wrong: ["Belém", "Salvador", "Natal"],
          hint: "It was built specifically to be the capital."
        },
        {
          id: "BR-002", points: 100, cefr: "A2",
          q: "How many states does Brazil have?",
          a: "26",
          wrong: ["24", "28", "30"],
          hint: "Plus the Federal District, which is not a state."
        },
        {
          id: "BR-003", points: 200, cefr: "B1",
          q: "What is the longest river entirely within Brazil?",
          a: "Rio São Francisco",
          wrong: ["Rio Tocantins", "Rio Paraná", "Rio Negro"],
          hint: "It is also called 'Velho Chico'."
        },
        {
          id: "BR-004", points: 200, cefr: "A2",
          q: "Which Brazilian state is the largest by area?",
          a: "Amazonas",
          wrong: ["Pará", "Mato Grosso", "Bahia"],
          hint: "It is in the Amazon region."
        },
        {
          id: "BR-005", points: 200, cefr: "A2",
          q: "What is the capital of the state of Minas Gerais?",
          a: "Belo Horizonte",
          wrong: ["Ouro Preto", "Uberlândia", "Juiz de Fora"],
          hint: "Its name means 'beautiful horizon'."
        },
        {
          id: "BR-006", points: 300, cefr: "B1",
          q: "The Pantanal, the world's largest tropical wetland, is mostly in which Brazilian state?",
          a: "Mato Grosso do Sul",
          wrong: ["Mato Grosso", "Tocantins", "Goiás"],
          hint: "Part of it also extends into Mato Grosso."
        },
        {
          id: "BR-007", points: 100, cefr: "B1",
          q: "Which Brazilian city is known as 'Cidade Maravilhosa' (Marvelous City)?",
          a: "Rio de Janeiro",
          wrong: ["São Paulo", "Recife", "Florianópolis"],
          hint: "It has a famous carnival and Sugarloaf Mountain."
        },
        {
          id: "BR-008", points: 200, cefr: "A2",
          q: "What is the capital of the state of Paraíba?",
          a: "João Pessoa",
          wrong: ["Maceió", "Fortaleza", "Recife"],
          hint: "It is known for its natural beauty."
        },
        {
          id: "BR-009", points: 200, cefr: "A2",
          q: "The Iguaçu Falls are on the border between Brazil and which other country?",
          a: "Argentina",
          wrong: ["Paraguay", "Uruguay", "Bolivia"],
          hint: "The falls are wider than Niagara."
        },
        {
          id: "BR-010", points: 400, cefr: "B2",
          q: "Which biome covers most of northeastern Brazil and is known for its dry climate and thorny vegetation?",
          a: "Caatinga",
          wrong: ["Cerrado", "Pampa", "Mata Atlântica"],
          hint: "It is a biome unique to Brazil."
        },
        {
          id: "BR-011", points: 500, cefr: "B1",
          q: "Which Brazilian state has the longest Atlantic coastline?",
          a: "Bahia",
          wrong: ["Maranhão", "Rio Grande do Norte", "Ceará"],
          hint: "It stretches roughly 1,100 km along the coast."
        },
        {
          id: "BR-012", points: 300, cefr: "A2",
          q: "Which Brazilian state is the smallest by area?",
          a: "Sergipe",
          wrong: ["Alagoas", "Espírito Santo", "Rio de Janeiro"],
          hint: "It is the smallest state in the Northeast region."
        },
        {
          id: "BR-013", points: 300, cefr: "B1",
          q: "Which two South American countries do NOT share a land border with Brazil?",
          a: "Chile and Ecuador",
          wrong: ["Chile and Peru", "Ecuador and Peru", "Bolivia and Paraguay"],
          hint: "One is long and thin in the south-west; the other is named after the Equator."
        },
        {
          id: "BR-014", points: 400, cefr: "A2",
          q: "Which city was the capital of Brazil before Rio de Janeiro?",
          a: "Salvador",
          wrong: ["Recife", "Olinda", "São Paulo"],
          hint: "It was the colonial capital until 1763, in the Northeast."
        },
        {
          id: "BR-015", points: 400, cefr: "B2",
          q: "Which Brazilian state administers the volcanic archipelago of Fernando de Noronha?",
          a: "Pernambuco",
          wrong: ["Rio Grande do Norte", "Ceará", "Bahia"],
          hint: "The same state is famous for the Olinda Carnival."
        },
        {
          id: "BR-016", points: 500, cefr: "B1",
          q: "Which Brazilian state is divided into the most municipalities?",
          a: "Minas Gerais",
          wrong: ["São Paulo", "Bahia", "Rio Grande do Sul"],
          hint: "It is in the Southeast and has 853 of them."
        },
        {
          id: "BR-017", points: 500, cefr: "A2",
          q: "What is the highest mountain in Brazil?",
          a: "Pico da Neblina",
          wrong: ["Pico da Bandeira", "Pico Paraná", "Monte Roraima"],
          hint: "At 2,995 m it rises in the Amazon rainforest, in the state of Amazonas."
        }
      ]
    },

    // ─────────────────────────────────────────────
    //  2. BRAZIL: HISTORY & CULTURE
    // ─────────────────────────────────────────────
    {
      id: "BrazilHistory",
      label: "Brazil: History & Culture",
      emoji: "🏛️",
      color: "amber",
      questions: [
        {
          id: "BH-001", points: 100, cefr: "B1",
          q: "In what year did Brazil declare independence from Portugal?",
          a: "1822",
          wrong: ["1800", "1889", "1750"],
          hint: "Dom Pedro I proclaimed it on the banks of the Ipiranga river."
        },
        {
          id: "BH-002", points: 300, cefr: "A2",
          q: "Who was the first president of the Brazilian Republic?",
          a: "Deodoro da Fonseca",
          wrong: ["Floriano Peixoto", "Getúlio Vargas", "Dom Pedro II"],
          hint: "He was a military marshal who led the proclamation of the Republic."
        },
        {
          id: "BH-003", points: 200, cefr: "B1",
          q: "What was the name of the first Portuguese navigator to arrive in Brazil?",
          a: "Pedro Álvares Cabral",
          wrong: ["Vasco da Gama", "Fernão de Magalhães", "Bartolomeu Dias"],
          hint: "He arrived in 1500."
        },
        {
          id: "BH-004", points: 200, cefr: "B2",
          q: "The movement that ended slavery in Brazil in 1888 is associated with which princess?",
          a: "Princess Isabel",
          wrong: ["Princess Leopoldina", "Queen Maria I", "Princess Teresa Cristina"],
          hint: "She signed the Lei Áurea (Golden Law)."
        },
        {
          id: "BH-005", points: 300, cefr: "B2",
          q: "Which Indigenous group did Pero Vaz de Caminha describe in his letter of 1500?",
          a: "Tupi",
          wrong: ["Guarani", "Yanomami", "Kayapó"],
          hint: "They lived along the Brazilian coast."
        },
        {
          id: "BH-006", points: 400, cefr: "B1",
          q: "The Semana de Arte Moderna (Modern Art Week) took place in São Paulo in which year?",
          a: "1922",
          wrong: ["1910", "1930", "1945"],
          hint: "It happened in the same year as the centenary of independence."
        },
        {
          id: "BH-007", points: 200, cefr: "B1",
          q: "What is Carnaval's most famous parade venue in Rio de Janeiro called?",
          a: "Sambódromo (Marquês de Sapucaí)",
          wrong: ["Maracanã", "Quinta da Boa Vista", "Aterro do Flamengo"],
          hint: "It was designed by Oscar Niemeyer."
        },
        {
          id: "BH-008", points: 100, cefr: "B1",
          q: "Brazil's official language is Portuguese because of its colonization by which country?",
          a: "Portugal",
          wrong: ["Spain", "France", "Netherlands"],
          hint: "A small European nation on the Atlantic coast."
        },
        {
          id: "BH-009", points: 300, cefr: "B2",
          q: "The city of Ouro Preto in Minas Gerais was the center of which historical economic cycle?",
          a: "Gold",
          wrong: ["Sugar", "Rubber", "Coffee"],
          hint: "Its name literally means 'black gold'."
        },
        {
          id: "BH-010", points: 300, cefr: "B1",
          q: "What famous Brazilian architect designed the main public buildings of Brasília?",
          a: "Oscar Niemeyer",
          wrong: ["Lúcio Costa", "Paulo Mendes da Rocha", "Ruy Ohtake"],
          hint: "He lived to be 104 years old."
        },
        {
          id: "BH-011", points: 500, cefr: "B2",
          q: "What was the name of the treaty signed in 1494 that divided the New World between Portugal and Spain?",
          a: "Treaty of Tordesillas",
          wrong: ["Treaty of Lisbon", "Treaty of Madrid", "Treaty of Utrecht"],
          hint: "It drew an imaginary line in the Atlantic Ocean."
        },
        {
          id: "BH-012", points: 100, cefr: "A2",
          q: "In which city is the Christ the Redeemer statue?",
          a: "Rio de Janeiro",
          wrong: ["São Paulo", "Salvador", "Belo Horizonte"],
          hint: "The statue stands on Corcovado mountain."
        },
        {
          id: "BH-013", points: 400, cefr: "B1",
          q: "Which Brazilian writer wrote the novel 'Dom Casmurro'?",
          a: "Machado de Assis",
          wrong: ["José de Alencar", "Jorge Amado", "Graciliano Ramos"],
          hint: "He was the first president of the Brazilian Academy of Letters."
        },
        {
          id: "BH-014", points: 400, cefr: "B1",
          q: "In which year was Brasília inaugurated as the capital of Brazil?",
          a: "1960",
          wrong: ["1950", "1956", "1964"],
          hint: "Building the new capital took about four years."
        },
        {
          id: "BH-015", points: 500, cefr: "B2",
          q: "Which city became the capital of Dutch Brazil under Johan Maurits of Nassau?",
          a: "Recife",
          wrong: ["Salvador", "Natal", "Fortaleza"],
          hint: "It is now the capital of Pernambuco, famous for its rivers and bridges."
        },
        {
          id: "BH-016", points: 500, cefr: "A2",
          q: "Which Brazilian composer wrote the 'Bachianas Brasileiras'?",
          a: "Heitor Villa-Lobos",
          wrong: ["Carlos Gomes", "Tom Jobim", "Chiquinha Gonzaga"],
          hint: "He is Brazil's best-known classical composer, born in Rio de Janeiro in 1887."
        }
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
          id: "BIO-001", points: 100, cefr: "B1",
          q: "What is the powerhouse of the cell?",
          a: "Mitochondria",
          wrong: ["Nucleus", "Ribosome", "Vacuole"],
          hint: "It produces ATP energy for the cell."
        },
        {
          id: "BIO-002", points: 100, cefr: "B1",
          q: "How many chromosomes do humans normally have?",
          a: "46",
          wrong: ["23", "48", "44"],
          hint: "They come in 23 pairs."
        },
        {
          id: "BIO-003", points: 100, cefr: "B1",
          q: "What gas do plants absorb from the air during photosynthesis?",
          a: "Carbon dioxide (CO₂)",
          wrong: ["Oxygen (O₂)", "Nitrogen (N₂)", "Hydrogen (H₂)"],
          hint: "Humans breathe this gas out."
        },
        {
          id: "BIO-004", points: 200, cefr: "B2",
          q: "What is the name of the process by which cells divide into two identical copies?",
          a: "Mitosis",
          wrong: ["Meiosis", "Osmosis", "Photosynthesis"],
          hint: "It produces genetically identical daughter cells."
        },
        {
          id: "BIO-005", points: 200, cefr: "A2",
          q: "Which organ produces insulin in the human body?",
          a: "Pancreas",
          wrong: ["Liver", "Kidney", "Spleen"],
          hint: "It is located near the stomach."
        },
        {
          id: "BIO-006", points: 300, cefr: "B1",
          q: "What is the scientific name for the domesticated dog?",
          a: "Canis lupus familiaris",
          wrong: ["Canis domesticus", "Felis catus", "Canis aureus"],
          hint: "It is classified as a subspecies of the wolf."
        },
        {
          id: "BIO-007", points: 100, cefr: "B1",
          q: "What type of blood cells carry oxygen through the body?",
          a: "Red blood cells (erythrocytes)",
          wrong: ["White blood cells", "Platelets", "Plasma cells"],
          hint: "They contain hemoglobin, which gives them their color."
        },
        {
          id: "BIO-008", points: 200, cefr: "A2",
          q: "What is the largest organ of the human body?",
          a: "Skin",
          wrong: ["Liver", "Brain", "Intestine"],
          hint: "It covers your entire body."
        },
        {
          id: "BIO-009", points: 100, cefr: "B1",
          q: "What molecule carries genetic information in living cells?",
          a: "DNA",
          wrong: ["RNA", "ATP", "Protein"],
          hint: "It has a famous double-helix shape."
        },
        {
          id: "BIO-010", points: 100, cefr: "A2",
          q: "Which animal is the largest on Earth?",
          a: "Blue whale",
          wrong: ["African elephant", "Giant squid", "Whale shark"],
          hint: "It lives in the ocean and is a mammal."
        },
        {
          id: "BIO-011", points: 400, cefr: "B2",
          q: "What is the name of the process by which plants lose water through their leaves?",
          a: "Transpiration",
          wrong: ["Evaporation", "Osmosis", "Respiration"],
          hint: "It is the plant equivalent of sweating."
        },
        {
          id: "BIO-012", points: 500, cefr: "B2",
          q: "What is the term for when a species mimics the appearance of a toxic species to avoid predators?",
          a: "Batesian mimicry",
          wrong: ["Müllerian mimicry", "Camouflage", "Aposematism"],
          hint: "Named after the English naturalist Henry Bates, who studied it in the Amazon."
        },
        {
          id: "BIO-013", points: 300, cefr: "A2",
          q: "How many bones are there in the adult human body?",
          a: "206",
          wrong: ["186", "226", "306"],
          hint: "The number is between 200 and 210."
        },
        {
          id: "BIO-014", points: 300, cefr: "B1",
          q: "Which human organ can grow back after part of it is removed?",
          a: "Liver",
          wrong: ["Kidney", "Heart", "Lung"],
          hint: "It sits on the right side of the body, under the ribs."
        },
        {
          id: "BIO-015", points: 400, cefr: "B1",
          q: "Which vitamin is produced by human skin when it is exposed to sunlight?",
          a: "Vitamin D",
          wrong: ["Vitamin A", "Vitamin C", "Vitamin K"],
          hint: "People who get very little sun often do not have enough of it."
        },
        {
          id: "BIO-016", points: 400, cefr: "A2",
          q: "Which sea animal has three hearts?",
          a: "Octopus",
          wrong: ["Shark", "Dolphin", "Sea turtle"],
          hint: "It has eight arms and blue blood."
        },
        {
          id: "BIO-017", points: 500, cefr: "B2",
          q: "What word describes animals that are most active at dawn and dusk?",
          a: "Crepuscular",
          wrong: ["Nocturnal", "Diurnal", "Migratory"],
          hint: "In Portuguese, the related word means twilight."
        },
        {
          id: "BIO-018", points: 500, cefr: "B1",
          q: "How many compartments does a cow's stomach have?",
          a: "Four",
          wrong: ["Two", "Three", "Seven"],
          hint: "Grass is fermented in the first and largest one, called the rumen."
        }
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
          id: "PC-001", points: 100, cefr: "A2",
          q: "What is the chemical symbol for water?",
          a: "H₂O",
          wrong: ["HO₂", "H₃O", "O₂H"],
          hint: "Two hydrogen atoms, one oxygen atom."
        },
        {
          id: "PC-002", points: 200, cefr: "B1",
          q: "What is the approximate speed of light in a vacuum?",
          a: "300,000 km/s",
          wrong: ["150,000 km/s", "500,000 km/s", "3,000 km/s"],
          hint: "Nothing in the universe travels faster."
        },
        {
          id: "PC-003", points: 200, cefr: "B1",
          q: "What is the atomic number of carbon?",
          a: "6",
          wrong: ["8", "12", "4"],
          hint: "It is the foundation of all organic life."
        },
        {
          id: "PC-004", points: 100, cefr: "A2",
          q: "What force keeps planets in orbit around the Sun?",
          a: "Gravity",
          wrong: ["Magnetism", "Friction", "Electrostatic force"],
          hint: "It also keeps you on the ground."
        },
        {
          id: "PC-005", points: 100, cefr: "B1",
          q: "On the Celsius scale, at what temperature does water boil at sea level?",
          a: "100°C",
          wrong: ["80°C", "120°C", "212°C"],
          hint: "Think of a pot of boiling water on a stove."
        },
        {
          id: "PC-006", points: 100, cefr: "B1",
          q: "What is the name of the negatively charged particle in an atom?",
          a: "Electron",
          wrong: ["Proton", "Neutron", "Photon"],
          hint: "It orbits the nucleus of the atom."
        },
        {
          id: "PC-007", points: 200, cefr: "B1",
          q: "What gas makes up about 78% of Earth's atmosphere?",
          a: "Nitrogen (N₂)",
          wrong: ["Oxygen (O₂)", "Carbon dioxide (CO₂)", "Argon (Ar)"],
          hint: "It is not the gas we breathe to survive."
        },
        {
          id: "PC-008", points: 200, cefr: "B1",
          q: "Which scientist formulated the three laws of motion?",
          a: "Isaac Newton",
          wrong: ["Albert Einstein", "Galileo Galilei", "Nikola Tesla"],
          hint: "An apple allegedly fell on his head."
        },
        {
          id: "PC-009", points: 200, cefr: "A2",
          q: "What is the chemical symbol for gold?",
          a: "Au",
          wrong: ["Go", "Gd", "Ag"],
          hint: "It comes from the Latin word 'aurum'."
        },
        {
          id: "PC-010", points: 200, cefr: "A2",
          q: "What type of energy is stored in food?",
          a: "Chemical energy",
          wrong: ["Kinetic energy", "Nuclear energy", "Thermal energy"],
          hint: "Your body converts it into movement and heat."
        },
        {
          id: "PC-011", points: 300, cefr: "B1",
          q: "What is the SI unit of electrical resistance?",
          a: "Ohm (Ω)",
          wrong: ["Volt (V)", "Ampere (A)", "Watt (W)"],
          hint: "Named after German physicist Georg Simon Ohm."
        },
        {
          id: "PC-012", points: 400, cefr: "A2",
          q: "What is the chemical symbol for iron on the periodic table?",
          a: "Fe",
          wrong: ["Ir", "In", "Fr"],
          hint: "It comes from the Latin word 'ferrum', meaning iron."
        },
        {
          id: "PC-013", points: 500, cefr: "B2",
          q: "What does Einstein's equation E=mc² say that energy equals?",
          a: "Mass times the speed of light squared",
          wrong: ["Mass times the speed of sound squared", "Mass times gravitational acceleration squared", "Momentum times the speed of light"],
          hint: "The 'c' stands for 'celeritas', the Latin word for speed."
        },
        {
          id: "PC-014", points: 300, cefr: "A2",
          q: "Which metal is liquid at room temperature?",
          a: "Mercury",
          wrong: ["Lead", "Zinc", "Aluminum"],
          hint: "It shares its name with a planet."
        },
        {
          id: "PC-015", points: 300, cefr: "B1",
          q: "Which element is the most abundant in the universe?",
          a: "Hydrogen",
          wrong: ["Helium", "Oxygen", "Carbon"],
          hint: "It is the lightest and simplest of all the elements."
        },
        {
          id: "PC-016", points: 400, cefr: "A2",
          q: "What is the pH of pure water at 25°C?",
          a: "7",
          wrong: ["3", "5", "9"],
          hint: "Pure water is exactly neutral: not an acid, not a base."
        },
        {
          id: "PC-017", points: 400, cefr: "B1",
          q: "What is the SI unit of force?",
          a: "Newton",
          wrong: ["Joule", "Pascal", "Watt"],
          hint: "It is named after the scientist who described gravity."
        },
        {
          id: "PC-018", points: 500, cefr: "A2",
          q: "Which metal has the highest melting point?",
          a: "Tungsten",
          wrong: ["Titanium", "Platinum", "Iron"],
          hint: "It was used for the thin wire inside old light bulbs."
        },
        {
          id: "PC-019", points: 500, cefr: "B2",
          q: "Which chemist created the first widely accepted periodic table of the elements?",
          a: "Dmitri Mendeleev",
          wrong: ["Antoine Lavoisier", "John Dalton", "Niels Bohr"],
          hint: "He was Russian and left gaps for elements not yet discovered."
        }
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
          id: "MA-001", points: 100, cefr: "A2",
          q: "What is the value of π (pi) to two decimal places?",
          a: "3.14",
          wrong: ["3.16", "3.12", "3.41"],
          hint: "It relates a circle's circumference to its diameter."
        },
        {
          id: "MA-002", points: 100, cefr: "A2",
          q: "What is the square root of 144?",
          a: "12",
          wrong: ["14", "11", "13"],
          hint: "Think: what number times itself equals 144?"
        },
        {
          id: "MA-003", points: 200, cefr: "B1",
          q: "In a right triangle, what is the name of the side opposite the right angle?",
          a: "Hypotenuse",
          wrong: ["Adjacent", "Opposite", "Bisector"],
          hint: "It is always the longest side of the triangle."
        },
        {
          id: "MA-004", points: 100, cefr: "A2",
          q: "What is 15% of 200?",
          a: "30",
          wrong: ["25", "35", "20"],
          hint: "10% of 200 is 20. Then add half of that."
        },
        {
          id: "MA-005", points: 100, cefr: "A2",
          q: "How many sides does a hexagon have?",
          a: "6",
          wrong: ["5", "7", "8"],
          hint: "Like a honeycomb cell."
        },
        {
          id: "MA-006", points: 200, cefr: "B1",
          q: "What is the formula for the area of a circle?",
          a: "A = πr²",
          wrong: ["A = 2πr", "A = πd", "A = r²"],
          hint: "r is the radius of the circle."
        },
        {
          id: "MA-007", points: 100, cefr: "B1",
          q: "What do you call a number that can only be divided by 1 and itself?",
          a: "Prime number",
          wrong: ["Even number", "Composite number", "Rational number"],
          hint: "Examples: 2, 3, 5, 7, 11…"
        },
        {
          id: "MA-008", points: 300, cefr: "B1",
          q: "What is 2 to the power of 10 (2¹⁰)?",
          a: "1024",
          wrong: ["512", "2048", "1000"],
          hint: "This number is also used in computing as 1 kilobyte."
        },
        {
          id: "MA-009", points: 300, cefr: "B1",
          q: "In the Fibonacci sequence (1, 1, 2, 3, 5…), what is the next number?",
          a: "8",
          wrong: ["7", "9", "10"],
          hint: "Each number is the sum of the two before it."
        },
        {
          id: "MA-010", points: 100, cefr: "B1",
          q: "What is the sum of all interior angles of a triangle?",
          a: "180 degrees",
          wrong: ["90 degrees", "270 degrees", "360 degrees"],
          hint: "This is true for any triangle, in any shape."
        },
        {
          id: "MA-011", points: 400, cefr: "B2",
          q: "What is the name of the theorem that states: in a right triangle, a² + b² = c²?",
          a: "Pythagorean theorem",
          wrong: ["Euclidean theorem", "Fermat's theorem", "Binomial theorem"],
          hint: "Named after an ancient Greek mathematician and philosopher."
        },
        {
          id: "MA-012", points: 500, cefr: "A2",
          q: "What is the only even prime number?",
          a: "2",
          wrong: ["0", "1", "4"],
          hint: "All other prime numbers are odd."
        },
        {
          id: "MA-013", points: 200, cefr: "B1",
          q: "What is the perimeter of a square with sides of 5 cm?",
          a: "20 cm",
          wrong: ["10 cm", "25 cm", "15 cm"],
          hint: "Add the length of all four sides together."
        },
        {
          id: "MA-014", points: 300, cefr: "B1",
          q: "In a list of numbers, what do we call the number that appears most often?",
          a: "The mode",
          wrong: ["The median", "The mean", "The range"],
          hint: "You find it just by counting repeats; no adding or ordering is needed."
        },
        {
          id: "MA-015", points: 400, cefr: "A2",
          q: "How many flat faces does a dodecahedron have?",
          a: "12",
          wrong: ["10", "20", "8"],
          hint: "The Greek prefix 'dodeca-' is itself a number."
        },
        {
          id: "MA-016", points: 400, cefr: "A2",
          q: "A googol is the digit 1 followed by how many zeros?",
          a: "100",
          wrong: ["50", "200", "1,000"],
          hint: "A famous search engine misspelled this word as its name."
        },
        {
          id: "MA-017", points: 500, cefr: "B2",
          q: "What do we call a number equal to the sum of its smaller divisors, such as 6?",
          a: "Perfect number",
          wrong: ["Prime number", "Square number", "Rational number"],
          hint: "6 = 1 + 2 + 3, exactly. The name sounds like praise."
        },
        {
          id: "MA-018", points: 500, cefr: "A2",
          q: "Which mathematician's name gave us the word 'algorithm'?",
          a: "Al-Khwarizmi",
          wrong: ["Euclid", "Fibonacci", "Pythagoras"],
          hint: "He worked in Baghdad in the 9th century."
        }
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
          id: "WG-001", points: 100, cefr: "A2",
          q: "What is the largest country in the world by area?",
          a: "Russia",
          wrong: ["Canada", "China", "United States"],
          hint: "It spans 11 time zones."
        },
        {
          id: "WG-002", points: 100, cefr: "A2",
          q: "What is the capital of Japan?",
          a: "Tokyo",
          wrong: ["Osaka", "Kyoto", "Hiroshima"],
          hint: "One of the world's most populated cities."
        },
        {
          id: "WG-003", points: 100, cefr: "A2",
          q: "On which continent is Egypt located?",
          a: "Africa",
          wrong: ["Asia", "Europe", "Middle East"],
          hint: "The Nile River flows through it."
        },
        {
          id: "WG-004", points: 200, cefr: "B1",
          q: "What is generally considered the longest river in the world?",
          a: "The Nile",
          wrong: ["The Amazon", "The Yangtze", "The Mississippi"],
          hint: "It flows through northeastern Africa into the Mediterranean Sea."
        },
        {
          id: "WG-005", points: 100, cefr: "A2",
          q: "What ocean lies between Europe/Africa and the Americas?",
          a: "Atlantic Ocean",
          wrong: ["Pacific Ocean", "Indian Ocean", "Arctic Ocean"],
          hint: "Brazil's coastline faces this ocean."
        },
        {
          id: "WG-006", points: 300, cefr: "A2",
          q: "What is the capital of Australia?",
          a: "Canberra",
          wrong: ["Sydney", "Melbourne", "Brisbane"],
          hint: "It is not the largest or most famous city."
        },
        {
          id: "WG-007", points: 200, cefr: "A2",
          q: "Which country has the largest population in the world?",
          a: "India",
          wrong: ["China", "United States", "Indonesia"],
          hint: "It recently surpassed its neighbor to the north."
        },
        {
          id: "WG-008", points: 200, cefr: "B1",
          q: "Mount Everest, the world's highest peak, is in which mountain range?",
          a: "The Himalayas",
          wrong: ["The Andes", "The Alps", "The Rockies"],
          hint: "Located on the border between Nepal and Tibet."
        },
        {
          id: "WG-009", points: 200, cefr: "A2",
          q: "What is the smallest country in the world?",
          a: "Vatican City",
          wrong: ["Monaco", "San Marino", "Liechtenstein"],
          hint: "It is located entirely within the city of Rome, Italy."
        },
        {
          id: "WG-010", points: 100, cefr: "B1",
          q: "The Sahara, the world's largest hot desert, is on which continent?",
          a: "Africa",
          wrong: ["Asia", "Australia", "South America"],
          hint: "It covers most of the northern part of that continent."
        },
        {
          id: "WG-011", points: 400, cefr: "B2",
          q: "What is the name of the narrow strip of land connecting North and South America?",
          a: "Isthmus of Panama",
          wrong: ["Strait of Magellan", "Isthmus of Suez", "Bering Strait"],
          hint: "A famous canal was built through it in 1914."
        },
        {
          id: "WG-012", points: 500, cefr: "A2",
          q: "Which African country has more pyramids than Egypt?",
          a: "Sudan",
          wrong: ["Ethiopia", "Libya", "Chad"],
          hint: "They were built by the ancient Nubian kingdoms."
        },
        {
          id: "WG-013", points: 300, cefr: "B1",
          q: "Which country is famous for its fjords and the coastal city of Bergen?",
          a: "Norway",
          wrong: ["Sweden", "Finland", "Denmark"],
          hint: "It is the western part of Scandinavia."
        },
        {
          id: "WG-014", points: 300, cefr: "A2",
          q: "Which river runs through the city of Paris?",
          a: "The Seine",
          wrong: ["The Loire", "The Rhône", "The Danube"],
          hint: "Boat tours on it pass close to the Eiffel Tower."
        },
        {
          id: "WG-015", points: 400, cefr: "A2",
          q: "Lake Titicaca is on the border of Peru and which country?",
          a: "Bolivia",
          wrong: ["Chile", "Ecuador", "Paraguay"],
          hint: "It has no coast, and its main city sits very high up."
        },
        {
          id: "WG-016", points: 400, cefr: "B1",
          q: "Mount Kilimanjaro, the highest mountain in Africa, is in which country?",
          a: "Tanzania",
          wrong: ["Kenya", "Uganda", "Ethiopia"],
          hint: "Its largest city is Dar es Salaam."
        },
        {
          id: "WG-017", points: 500, cefr: "A2",
          q: "In which South American country is Dutch an official language?",
          a: "Suriname",
          wrong: ["Guyana", "Paraguay", "Ecuador"],
          hint: "It is a small country on the north coast, next to Guyana."
        },
        {
          id: "WG-018", points: 500, cefr: "B1",
          q: "Which country has the only national flag that is not a rectangle or a square?",
          a: "Nepal",
          wrong: ["Bhutan", "Sri Lanka", "Mongolia"],
          hint: "It lies in the Himalayas, between India and China."
        }
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
          id: "WH-001", points: 100, cefr: "A2",
          q: "In which year did World War II end?",
          a: "1945",
          wrong: ["1943", "1918", "1950"],
          hint: "V-E Day (Europe) was in May; V-J Day (Japan) in September."
        },
        {
          id: "WH-002", points: 100, cefr: "A2",
          q: "Who was the first person to walk on the Moon?",
          a: "Neil Armstrong",
          wrong: ["Buzz Aldrin", "Yuri Gagarin", "John Glenn"],
          hint: "Apollo 11 mission, July 1969."
        },
        {
          id: "WH-003", points: 100, cefr: "A2",
          q: "The Great Pyramid of Giza is in which country?",
          a: "Egypt",
          wrong: ["Iraq", "Saudi Arabia", "Sudan"],
          hint: "It is near the capital city Cairo."
        },
        {
          id: "WH-004", points: 200, cefr: "B1",
          q: "The Berlin Wall fell in which year, reuniting East and West Germany?",
          a: "1989",
          wrong: ["1991", "1985", "1975"],
          hint: "It was a defining moment of the end of the Cold War."
        },
        {
          id: "WH-005", points: 200, cefr: "B1",
          q: "Which civilization built Machu Picchu in Peru?",
          a: "The Inca",
          wrong: ["The Aztec", "The Maya", "The Olmec"],
          hint: "A great South American empire centered in the Andes."
        },
        {
          id: "WH-006", points: 100, cefr: "A2",
          q: "Who painted the Mona Lisa?",
          a: "Leonardo da Vinci",
          wrong: ["Michelangelo", "Raphael", "Caravaggio"],
          hint: "An Italian Renaissance genius who also studied science."
        },
        {
          id: "WH-007", points: 100, cefr: "A2",
          q: "In what year did Columbus first reach the Americas?",
          a: "1492",
          wrong: ["1500", "1488", "1510"],
          hint: "'In 1492, Columbus sailed the ocean blue.'"
        },
        {
          id: "WH-008", points: 200, cefr: "A2",
          q: "The French Revolution began in which year?",
          a: "1789",
          wrong: ["1776", "1804", "1799"],
          hint: "The storming of the Bastille prison."
        },
        {
          id: "WH-009", points: 200, cefr: "A2",
          q: "Who was the first woman to win a Nobel Prize?",
          a: "Marie Curie",
          wrong: ["Ada Lovelace", "Rosalind Franklin", "Florence Nightingale"],
          hint: "She actually won it twice — in Physics and Chemistry."
        },
        {
          id: "WH-010", points: 200, cefr: "B1",
          q: "Julius Caesar was a leader of which ancient civilization?",
          a: "Rome",
          wrong: ["Greece", "Egypt", "Carthage"],
          hint: "He was assassinated on the Ides of March, 44 BC."
        },
        {
          id: "WH-011", points: 300, cefr: "B2",
          q: "Which Wonder of the Ancient World was a tower guiding ships into an Egyptian harbor?",
          a: "The Lighthouse of Alexandria",
          wrong: ["The Colossus of Rhodes", "The Hanging Gardens of Babylon", "The Temple of Artemis"],
          hint: "It stood on the island of Pharos and was one of the tallest man-made structures for centuries."
        },
        {
          id: "WH-012", points: 400, cefr: "B2",
          q: "The 'Black Death' in 14th-century Europe was caused by which bacterium?",
          a: "Yersinia pestis",
          wrong: ["Mycobacterium tuberculosis", "Vibrio cholerae", "Clostridium botulinum"],
          hint: "It was spread mainly through fleas carried by rats."
        },
        {
          id: "WH-013", points: 500, cefr: "B1",
          q: "Which Roman emperor ordered the construction of the Colosseum in 72 AD?",
          a: "Vespasian",
          wrong: ["Nero", "Augustus", "Constantine"],
          hint: "He founded the Flavian dynasty."
        },
        {
          id: "WH-014", points: 300, cefr: "B2",
          q: "Which ancient civilization developed cuneiform, one of the earliest writing systems?",
          a: "The Sumerians",
          wrong: ["The Egyptians", "The Phoenicians", "The Minoans"],
          hint: "They lived in Mesopotamia, in what is now Iraq."
        },
        {
          id: "WH-015", points: 300, cefr: "B1",
          q: "In which city were the first modern Olympic Games held in 1896?",
          a: "Athens",
          wrong: ["Paris", "London", "Rome"],
          hint: "The country is the home of the ancient Games."
        },
        {
          id: "WH-016", points: 400, cefr: "A2",
          q: "In which year did the Titanic sink on its first voyage?",
          a: "1912",
          wrong: ["1905", "1918", "1923"],
          hint: "It happened two years before World War I began."
        },
        {
          id: "WH-017", points: 400, cefr: "A2",
          q: "The ancient city of Petra is in which modern country?",
          a: "Jordan",
          wrong: ["Egypt", "Turkey", "Morocco"],
          hint: "Its buildings are carved into pink desert rock."
        },
        {
          id: "WH-018", points: 500, cefr: "B1",
          q: "Which West African empire was ruled by Mansa Musa in the 14th century?",
          a: "The Mali Empire",
          wrong: ["The Songhai Empire", "The Kingdom of Aksum", "The Benin Kingdom"],
          hint: "Its most famous city was Timbuktu."
        },
        {
          id: "WH-019", points: 500, cefr: "B2",
          q: "How many years did the Hundred Years' War between England and France actually last?",
          a: "116",
          wrong: ["100", "75", "130"],
          hint: "It ran from 1337 to 1453, so the name is misleading."
        }
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
          id: "FB-001", points: 100, cefr: "A2",
          q: "How many times has Brazil won the FIFA World Cup?",
          a: "5 times",
          wrong: ["4 times", "6 times", "3 times"],
          hint: "More than any other country in the world."
        },
        {
          id: "FB-002", points: 100, cefr: "B1",
          q: "Which Brazilian player is considered by many to be the greatest of all time and wore number 10?",
          a: "Pelé",
          wrong: ["Ronaldo Fenômeno", "Zico", "Romário"],
          hint: "He won three World Cups with Brazil."
        },
        {
          id: "FB-003", points: 100, cefr: "A2",
          q: "What is the name of the famous football stadium in Rio de Janeiro?",
          a: "Maracanã",
          wrong: ["Morumbis", "Arena Corinthians", "Mineirão"],
          hint: "It hosted the 2014 World Cup final."
        },
        {
          id: "FB-004", points: 100, cefr: "A2",
          q: "In football, how many players are on the field per team?",
          a: "11",
          wrong: ["10", "12", "9"],
          hint: "This includes the goalkeeper."
        },
        {
          id: "FB-005", points: 100, cefr: "A2",
          q: "Which country hosted the 2014 FIFA World Cup?",
          a: "Brazil",
          wrong: ["South Africa", "Russia", "Germany"],
          hint: "It was the second time this country hosted the tournament."
        },
        {
          id: "FB-006", points: 200, cefr: "A2",
          q: "Neymar Jr. played for which Spanish club before moving to PSG?",
          a: "FC Barcelona",
          wrong: ["Real Madrid", "Atletico Madrid", "Valencia"],
          hint: "He played alongside Messi and Suárez in a famous trio."
        },
        {
          id: "FB-007", points: 200, cefr: "B1",
          q: "In which year did Brazil suffer the famous 7-1 defeat to Germany at the World Cup?",
          a: "2014",
          wrong: ["2010", "2018", "2006"],
          hint: "The match was played in Belo Horizonte, Brazil."
        },
        {
          id: "FB-008", points: 200, cefr: "B1",
          q: "The Copa Libertadores is the most important club competition on which continent?",
          a: "South America",
          wrong: ["Europe", "Africa", "North America"],
          hint: "It is similar to the UEFA Champions League."
        },
        {
          id: "FB-009", points: 200, cefr: "B1",
          q: "Which Brazilian club is nicknamed 'Mengão' and is based in Rio de Janeiro?",
          a: "Flamengo",
          wrong: ["Fluminense", "Vasco da Gama", "Botafogo"],
          hint: "It has one of the largest fan bases in Brazil."
        },
        {
          id: "FB-010", points: 100, cefr: "A2",
          q: "What does VAR stand for in modern football?",
          a: "Video Assistant Referee",
          wrong: ["Visual Action Review", "Video Action Referee", "Virtual Assistant Review"],
          hint: "It uses video replay to review controversial decisions."
        },
        {
          id: "FB-011", points: 300, cefr: "A2",
          q: "Which country won the first ever FIFA World Cup in 1930?",
          a: "Uruguay",
          wrong: ["Argentina", "Brazil", "Italy"],
          hint: "The tournament was held on their home soil."
        },
        {
          id: "FB-012", points: 400, cefr: "B1",
          q: "Which player holds the record for most goals in a single World Cup tournament (13 goals in 1958)?",
          a: "Just Fontaine",
          wrong: ["Ronaldo", "Gerd Müller", "Eusébio"],
          hint: "He was a French striker of Moroccan descent."
        },
        {
          id: "FB-013", points: 500, cefr: "B2",
          q: "According to current FIFA rules, can a player be offside directly from a goal kick?",
          a: "No — there is no offside from a goal kick",
          wrong: ["Yes, the normal offside rule applies", "Only in extra time", "Only if the keeper takes it outside the box"],
          hint: "This rule was clarified and confirmed in 2019."
        },
        {
          id: "FB-014", points: 300, cefr: "B1",
          q: "How many minutes long is a football match, not counting stoppage time or extra time?",
          a: "90 minutes",
          wrong: ["80 minutes", "100 minutes", "120 minutes"],
          hint: "It is divided into two equal halves of the same length."
        },
        {
          id: "FB-015", points: 300, cefr: "A2",
          q: "Which Brazilian club did Pelé play for during most of his career?",
          a: "Santos",
          wrong: ["Corinthians", "Palmeiras", "São Paulo"],
          hint: "The club is from a port city in São Paulo state."
        },
        {
          id: "FB-016", points: 400, cefr: "B2",
          q: "Which nation won the inaugural Women's World Cup, staged in China in 1991?",
          a: "United States",
          wrong: ["Norway", "Germany", "Sweden"],
          hint: "The same country won the tournament again in 1999."
        },
        {
          id: "FB-017", points: 400, cefr: "A2",
          q: "Who was Brazil's goalkeeper when they won the 1994 World Cup?",
          a: "Cláudio Taffarel",
          wrong: ["Dida", "Marcos", "Rogério Ceni"],
          hint: "He was also in goal for the 1998 final."
        },
        {
          id: "FB-018", points: 500, cefr: "B1",
          q: "Which African country was the first to reach a World Cup quarter-final?",
          a: "Cameroon",
          wrong: ["Senegal", "Ghana", "Nigeria"],
          hint: "It happened in Italy in 1990, with Roger Milla in the team."
        },
        {
          id: "FB-019", points: 500, cefr: "A2",
          q: "Which team did Brazil beat in the 1958 World Cup final?",
          a: "Sweden",
          wrong: ["Hungary", "Czechoslovakia", "Italy"],
          hint: "Brazil won 5-2 against the host country."
        }
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
          id: "SM-001", points: 100, cefr: "A2",
          q: "How many rings are in the Olympic symbol?",
          a: "5",
          wrong: ["4", "6", "7"],
          hint: "Each ring represents one of the five continents."
        },
        {
          id: "SM-002", points: 100, cefr: "B1",
          q: "In basketball, how many points is a shot worth when scored from behind the arc?",
          a: "3 points",
          wrong: ["2 points", "4 points", "1 point"],
          hint: "It is called a 'three-pointer'."
        },
        {
          id: "SM-003", points: 100, cefr: "B1",
          q: "Capoeira is a martial art that originated in which country?",
          a: "Brazil",
          wrong: ["Angola", "Cuba", "Colombia"],
          hint: "It blends fighting with music and dance."
        },
        {
          id: "SM-004", points: 200, cefr: "B1",
          q: "In tennis, what is the score called when both players are tied at 40-40?",
          a: "Deuce",
          wrong: ["Tie", "Advantage", "Love"],
          hint: "The next point gives one player an 'advantage'."
        },
        {
          id: "SM-005", points: 100, cefr: "A2",
          q: "How long is an Olympic-size swimming pool?",
          a: "50 meters",
          wrong: ["25 meters", "100 meters", "75 meters"],
          hint: "Half the length is called a 'short course' pool."
        },
        {
          id: "SM-006", points: 200, cefr: "A2",
          q: "Brazilian athlete Rebeca Andrade won Olympic medals in which sport?",
          a: "Artistic gymnastics",
          wrong: ["Athletics (track and field)", "Swimming", "Rhythmic gymnastics"],
          hint: "She competed at the Tokyo and Paris Olympics."
        },
        {
          id: "SM-007", points: 100, cefr: "B1",
          q: "In volleyball, how many touches is a team allowed before sending the ball over the net?",
          a: "3",
          wrong: ["2", "4", "5"],
          hint: "Usually: receive, set, then attack."
        },
        {
          id: "SM-008", points: 200, cefr: "B2",
          q: "What is the name of the Brazilian martial art using grappling and ground fighting, now practiced worldwide?",
          a: "Brazilian Jiu-Jitsu (BJJ)",
          wrong: ["Capoeira", "Luta Livre", "Judo"],
          hint: "The Gracie family helped spread it globally."
        },
        {
          id: "SM-009", points: 400, cefr: "B1",
          q: "At the Paris 2024 Olympics, which sport made its Olympic debut?",
          a: "Breakdancing",
          wrong: ["Skateboarding", "Sport climbing", "Surfing"],
          hint: "It is a hip-hop street art form."
        },
        {
          id: "SM-010", points: 100, cefr: "B1",
          q: "In which sport would you perform a 'slam dunk'?",
          a: "Basketball",
          wrong: ["Volleyball", "Handball", "Water polo"],
          hint: "You jump and force the ball through the hoop."
        },
        {
          id: "SM-011", points: 300, cefr: "B1",
          q: "In the ancient Olympic Games, athletes originally competed in how many events?",
          a: "One (the stadion footrace)",
          wrong: ["Five", "Ten", "Three"],
          hint: "The Games started with just a single sprint of about 192 metres."
        },
        {
          id: "SM-012", points: 500, cefr: "B2",
          q: "What rule prevents a basketball team from moving back across the half-court line after crossing it?",
          a: "Backcourt violation",
          wrong: ["Goaltending", "Three-second violation", "Palming violation"],
          hint: "Once you cross mid-court, you cannot return to the backcourt."
        },
        {
          id: "SM-013", points: 300, cefr: "A2",
          q: "The first modern Olympic Games in 1896 took place in which country?",
          a: "Greece",
          wrong: ["France", "Italy", "England"],
          hint: "The ancient Olympic Games began in the same country."
        },
        {
          id: "SM-014", points: 300, cefr: "B1",
          q: "In tennis, what is the name for a serve the opponent cannot touch at all?",
          a: "Ace",
          wrong: ["Fault", "Let", "Lob"],
          hint: "It is also the name of the highest card in a deck."
        },
        {
          id: "SM-015", points: 400, cefr: "B1",
          q: "What does the Olympic motto 'Citius, Altius, Fortius' mean in English?",
          a: "Faster, Higher, Stronger",
          wrong: ["Stronger, Braver, Wiser", "Higher, Longer, Bolder", "Swifter, Calmer, Kinder"],
          hint: "Three comparative adjectives about speed, height and power."
        },
        {
          id: "SM-016", points: 400, cefr: "A2",
          q: "Which color jersey does the overall leader wear in the Tour de France?",
          a: "Yellow",
          wrong: ["Green", "White", "Blue"],
          hint: "It is the same color as the diamond on the Brazilian flag."
        },
        {
          id: "SM-017", points: 500, cefr: "A2",
          q: "The Thomas Cup is a world team competition in which sport?",
          a: "Badminton",
          wrong: ["Table tennis", "Squash", "Volleyball"],
          hint: "Players hit a shuttlecock over a high net."
        },
        {
          id: "SM-018", points: 500, cefr: "B2",
          q: "In sailing, what is the manoeuvre called when the bow turns through the wind?",
          a: "Tacking",
          wrong: ["Jibing", "Heeling", "Trimming"],
          hint: "The opposite manoeuvre turns the stern through the wind."
        }
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
          id: "PM-001", points: 100, cefr: "B1",
          q: "Which Brazilian singer had a global hit with 'Vai Malandra' and is known as Brazil's biggest pop star?",
          a: "Anitta",
          wrong: ["Claudia Leitte", "Ludmilla", "IZA"],
          hint: "She was the first Brazilian to top the Spotify global chart."
        },
        {
          id: "PM-002", points: 100, cefr: "A2",
          q: "The song 'Blinding Lights' was a massive hit for which artist?",
          a: "The Weeknd",
          wrong: ["Drake", "Post Malone", "Bruno Mars"],
          hint: "His real name is Abel Tesfaye, and he is Canadian."
        },
        {
          id: "PM-003", points: 200, cefr: "B1",
          q: "Taylor Swift's album 'Midnights' was released in which year?",
          a: "2022",
          wrong: ["2020", "2021", "2023"],
          hint: "It broke several streaming records on release night."
        },
        {
          id: "PM-004", points: 100, cefr: "A2",
          q: "The K-pop group BTS is from which country?",
          a: "South Korea",
          wrong: ["Japan", "China", "Thailand"],
          hint: "K-pop stands for 'Korean pop'."
        },
        {
          id: "PM-005", points: 100, cefr: "B1",
          q: "What music genre originated in Jamaica and is associated with Bob Marley?",
          a: "Reggae",
          wrong: ["Ska", "Reggaeton", "Calypso"],
          hint: "Characterized by offbeat rhythms and messages of peace."
        },
        {
          id: "PM-006", points: 200, cefr: "B1",
          q: "What was Billie Eilish's breakthrough hit song?",
          a: "Bad Guy",
          wrong: ["Lovely", "Ocean Eyes", "Happier Than Ever"],
          hint: "Famous for the whispered lyric 'duh'."
        },
        {
          id: "PM-007", points: 100, cefr: "B1",
          q: "Which music streaming platform is the most widely used in the world?",
          a: "Spotify",
          wrong: ["Apple Music", "YouTube Music", "Deezer"],
          hint: "It is a Swedish company founded in 2006."
        },
        {
          id: "PM-008", points: 200, cefr: "B1",
          q: "The musical genre 'Funk Carioca' (baile funk) originated in which Brazilian city?",
          a: "Rio de Janeiro",
          wrong: ["São Paulo", "Salvador", "Recife"],
          hint: "'Carioca' is the word for someone from that city."
        },
        {
          id: "PM-009", points: 100, cefr: "A2",
          q: "Shakira is a famous pop singer originally from which country?",
          a: "Colombia",
          wrong: ["Venezuela", "Argentina", "Mexico"],
          hint: "She also performed the FIFA World Cup song 'Waka Waka'."
        },
        {
          id: "PM-010", points: 100, cefr: "B1",
          q: "Which global pop star performed at the free concert on Copacabana beach in Rio in May 2024?",
          a: "Madonna",
          wrong: ["Beyoncé", "Lady Gaga", "Rihanna"],
          hint: "Over 1.6 million people attended."
        },
        {
          id: "PM-011", points: 300, cefr: "B2",
          q: "What genre blends rap and country music, popularized partly by Lil Nas X?",
          a: "Country rap (hick-hop)",
          wrong: ["Pop country", "Trap soul", "Americana rap"],
          hint: "Lil Nas X's 'Old Town Road' was a famous example."
        },
        {
          id: "PM-012", points: 400, cefr: "B2",
          q: "What is the term for the wavering effect a singer creates by rapidly varying pitch slightly?",
          a: "Vibrato",
          wrong: ["Falsetto", "Melisma", "Glissando"],
          hint: "Opera singers are particularly known for it."
        },
        {
          id: "PM-013", points: 500, cefr: "B2",
          q: "The opening riff of 'Satisfaction' was originally meant for which instrument?",
          a: "Horns (brass section)",
          wrong: ["Keyboard", "Bass guitar", "Violin"],
          hint: "Keith Richards recorded it as a demo placeholder but the band kept it."
        },
        {
          id: "PM-014", points: 300, cefr: "A2",
          q: "Which British band recorded the album 'Abbey Road'?",
          a: "The Beatles",
          wrong: ["The Rolling Stones", "Queen", "Pink Floyd"],
          hint: "The cover shows four men walking on a zebra crossing."
        },
        {
          id: "PM-015", points: 300, cefr: "A2",
          q: "The band Coldplay comes from which country?",
          a: "England",
          wrong: ["Ireland", "Australia", "Canada"],
          hint: "The singer Chris Martin was born there."
        },
        {
          id: "PM-016", points: 400, cefr: "B1",
          q: "Which Brazilian singer sang the English words on the 1964 hit 'The Girl from Ipanema'?",
          a: "Astrud Gilberto",
          wrong: ["Elis Regina", "Gal Costa", "Maria Bethânia"],
          hint: "She shares a surname with the guitarist João on the same record."
        },
        {
          id: "PM-017", points: 400, cefr: "A2",
          q: "Which album has sold more copies than any other album in history?",
          a: "Thriller",
          wrong: ["Back in Black", "Rumours", "The Dark Side of the Moon"],
          hint: "It came out in 1982 and its singer is called the King of Pop."
        },
        {
          id: "PM-018", points: 500, cefr: "B2",
          q: "What is the musical term for accenting beats that fall off the main pulse?",
          a: "Syncopation",
          wrong: ["Modulation", "Reverberation", "Improvisation"],
          hint: "It is everywhere in samba, jazz and funk rhythms."
        },
        {
          id: "PM-019", points: 500, cefr: "A2",
          q: "How many strings does a Brazilian cavaquinho have?",
          a: "4",
          wrong: ["5", "6", "7"],
          hint: "It has the same number of strings as a ukulele."
        }
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
          id: "MS-001", points: 100, cefr: "A2",
          q: "In the Marvel Cinematic Universe, what is Iron Man's real name?",
          a: "Tony Stark",
          wrong: ["Steve Rogers", "Bruce Banner", "Peter Parker"],
          hint: "Played by Robert Downey Jr."
        },
        {
          id: "MS-002", points: 100, cefr: "B1",
          q: "The Brazilian film 'Cidade de Deus' (City of God) is set in which city?",
          a: "Rio de Janeiro",
          wrong: ["São Paulo", "Salvador", "Recife"],
          hint: "It was directed by Fernando Meirelles and released in 2002."
        },
        {
          id: "MS-003", points: 100, cefr: "A2",
          q: "In Harry Potter, what is the name of Harry's owl?",
          a: "Hedwig",
          wrong: ["Errol", "Pigwidgeon", "Fawkes"],
          hint: "A beautiful snowy white owl."
        },
        {
          id: "MS-004", points: 100, cefr: "A2",
          q: "The Netflix series 'Squid Game' is originally from which country?",
          a: "South Korea",
          wrong: ["Japan", "China", "Thailand"],
          hint: "It broke all Netflix viewing records when it launched."
        },
        {
          id: "MS-005", points: 100, cefr: "B1",
          q: "Which animated Disney film features the song 'Let It Go'?",
          a: "Frozen",
          wrong: ["Brave", "Moana", "Tangled"],
          hint: "It features two sister princesses, Elsa and Anna."
        },
        {
          id: "MS-006", points: 100, cefr: "A2",
          q: "In The Lion King, what is the name of Simba's evil uncle?",
          a: "Scar",
          wrong: ["Mufasa", "Shenzi", "Banzai"],
          hint: "He has a distinctive scar over one eye."
        },
        {
          id: "MS-007", points: 200, cefr: "B1",
          q: "The TV series 'Chaves', beloved in Brazil, was originally produced in which country?",
          a: "Mexico",
          wrong: ["Brazil", "Argentina", "Colombia"],
          hint: "It was created by comedian Roberto Bolaños ('Chespirito')."
        },
        {
          id: "MS-008", points: 100, cefr: "B1",
          q: "In Spider-Man, what gives Peter Parker his superpowers?",
          a: "A radioactive spider bite",
          wrong: ["A chemistry experiment gone wrong", "A gamma ray blast", "A serum injection"],
          hint: "It happens during a school field trip."
        },
        {
          id: "MS-009", points: 200, cefr: "B1",
          q: "What is the subtitle of the third Avengers movie, released in 2018?",
          a: "Infinity War",
          wrong: ["Age of Ultron", "Endgame", "Civil War"],
          hint: "The villain Thanos collects all six Infinity Stones."
        },
        {
          id: "MS-010", points: 300, cefr: "B1",
          q: "The animated film 'Encanto' (2021) is set in which country?",
          a: "Colombia",
          wrong: ["Brazil", "Mexico", "Peru"],
          hint: "It features the Madrigal family and the song 'We Don't Talk About Bruno'."
        },
        {
          id: "MS-011", points: 400, cefr: "B2",
          q: "What is the film technique of filming a long scene in a single unbroken take called?",
          a: "Long take",
          wrong: ["Match cut", "Tracking shot", "Dolly zoom"],
          hint: "Used famously in '1917' and 'Children of Men'."
        },
        {
          id: "MS-012", points: 500, cefr: "B2",
          q: "The 'Kuleshov Effect' in cinema states that:",
          a: "A shot's meaning changes with what comes before or after",
          wrong: ["Miniature models can simulate large sets convincingly", "Two actors can be filmed separately and appear to interact", "Color grading changes the emotional tone of a scene"],
          hint: "Demonstrated by a Soviet filmmaker in the 1920s using the same neutral face next to different images."
        },
        {
          id: "MS-013", points: 200, cefr: "A2",
          q: "In 'Toy Story', what kind of toy is Woody?",
          a: "A cowboy doll",
          wrong: ["A space ranger", "A toy dinosaur", "A piggy bank"],
          hint: "He wears a hat and boots and has a pull string."
        },
        {
          id: "MS-014", points: 300, cefr: "B1",
          q: "In 'Stranger Things', what is the name of the dark parallel world?",
          a: "The Upside Down",
          wrong: ["The Shadow Realm", "The Void", "The Underworld"],
          hint: "Its name describes something that has been flipped over."
        },
        {
          id: "MS-015", points: 300, cefr: "B1",
          q: "Which Japanese studio made the animated film 'Spirited Away'?",
          a: "Studio Ghibli",
          wrong: ["Toei Animation", "Madhouse", "Studio Pierrot"],
          hint: "It was co-founded by the director Hayao Miyazaki."
        },
        {
          id: "MS-016", points: 400, cefr: "A2",
          q: "Which Brazilian actress starred in the film 'Central do Brasil'?",
          a: "Fernanda Montenegro",
          wrong: ["Sonia Braga", "Regina Casé", "Glória Pires"],
          hint: "She was nominated for an Oscar for this role in 1999."
        },
        {
          id: "MS-017", points: 400, cefr: "B1",
          q: "What was the first feature-length animated film made by Walt Disney?",
          a: "Snow White and the Seven Dwarfs",
          wrong: ["Pinocchio", "Bambi", "Fantasia"],
          hint: "It reached cinemas in 1937 and the heroine has seven small friends."
        },
        {
          id: "MS-018", points: 500, cefr: "A2",
          q: "Which film won the first Academy Award for Best Picture?",
          a: "Wings",
          wrong: ["The Broadway Melody", "The Jazz Singer", "Metropolis"],
          hint: "It is a silent film from 1927 about young pilots."
        },
        {
          id: "MS-019", points: 500, cefr: "B2",
          q: "Which French term describes the final part of a story, after the climax?",
          a: "Denouement",
          wrong: ["Prologue", "Montage", "Flashback"],
          hint: "The French word behind it means 'untying' a knot."
        }
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
          id: "VG-001", points: 100, cefr: "B1",
          q: "In Minecraft, what is the main material used to build the Nether Portal?",
          a: "Obsidian",
          wrong: ["Blackstone", "Basalt", "Iron blocks"],
          hint: "It is formed when lava meets water."
        },
        {
          id: "VG-002", points: 100, cefr: "B1",
          q: "What is the name of the battle royale game developed by Epic Games?",
          a: "Fortnite",
          wrong: ["PUBG", "Warzone", "Free Fire"],
          hint: "Known for its building mechanic and colorful style."
        },
        {
          id: "VG-003", points: 100, cefr: "B1",
          q: "In the Super Mario franchise, which princess does Mario usually rescue?",
          a: "Princess Peach",
          wrong: ["Princess Zelda", "Princess Daisy", "Princess Rosalina"],
          hint: "She lives in the Mushroom Kingdom."
        },
        {
          id: "VG-004", points: 100, cefr: "B2",
          q: "What is the objective of the impostors in 'Among Us'?",
          a: "Eliminate crewmates without being identified",
          wrong: ["Complete tasks before crewmates", "Sabotage the ship and escape", "Collect all keys before crewmates"],
          hint: "They must avoid getting voted out."
        },
        {
          id: "VG-005", points: 100, cefr: "B1",
          q: "In Pokémon, what are the three starter types available at the beginning of a new game?",
          a: "Fire, Water, and Grass",
          wrong: ["Fire, Water, and Electric", "Fire, Rock, and Water", "Grass, Psychic, and Water"],
          hint: "Each type is strong against one and weak against another."
        },
        {
          id: "VG-006", points: 200, cefr: "B1",
          q: "What is the name of the main playable character in 'The Legend of Zelda' series?",
          a: "Link",
          wrong: ["Zelda", "Ganon", "Sheik"],
          hint: "Many people mistakenly call him by the title character's name."
        },
        {
          id: "VG-007", points: 200, cefr: "B1",
          q: "In which fighting game would you perform a 'Hadouken' (fireball move)?",
          a: "Street Fighter",
          wrong: ["Mortal Kombat", "Tekken", "Dragon Ball FighterZ"],
          hint: "It is Ryu's signature move."
        },
        {
          id: "VG-008", points: 100, cefr: "B1",
          q: "The EA Sports FC game series simulates which sport?",
          a: "Football (soccer)",
          wrong: ["Basketball", "American football", "Rugby"],
          hint: "Updated every year with real-world players and clubs."
        },
        {
          id: "VG-009", points: 100, cefr: "B1",
          q: "In Roblox, what is the in-game currency called?",
          a: "Robux",
          wrong: ["Roblox Coins", "R-Dollars", "V-Bucks"],
          hint: "You can use it to buy items and avatar accessories."
        },
        {
          id: "VG-010", points: 100, cefr: "A2",
          q: "In Minecraft, what is the name of the final boss?",
          a: "The Ender Dragon",
          wrong: ["The Wither", "The Elder Guardian", "The Evoker"],
          hint: "It lives in The End dimension."
        },
        {
          id: "VG-011", points: 300, cefr: "A2",
          q: "In online gaming, what does 'GG' stand for?",
          a: "Good game",
          wrong: ["Great going", "Get going", "Go go"],
          hint: "Typed in chat at the end of a match as a sign of sportsmanship."
        },
        {
          id: "VG-012", points: 400, cefr: "B2",
          q: "What programming language is most commonly used to develop games in the Unity engine?",
          a: "C#",
          wrong: ["C++", "Python", "Java"],
          hint: "It is pronounced 'C sharp'."
        },
        {
          id: "VG-013", points: 500, cefr: "B2",
          q: "The very first home video game console ever sold commercially was released in 1972. What was it called?",
          a: "Odyssey",
          wrong: ["Atari 2600", "Intellivision", "Coleco Telstar"],
          hint: "It was made by a company whose name means 'great voice' in Latin."
        },
        {
          id: "VG-014", points: 200, cefr: "A2",
          q: "In Pac-Man, what does Pac-Man eat to turn the ghosts blue?",
          a: "Power pellets",
          wrong: ["Cherries", "Keys", "Bells"],
          hint: "There are four of them, one near each corner of the maze."
        },
        {
          id: "VG-015", points: 300, cefr: "A2",
          q: "In Tetris, which piece is the long straight one made of four blocks?",
          a: "The I-piece",
          wrong: ["The L-piece", "The T-piece", "The S-piece"],
          hint: "It is the only piece that can clear four rows at once."
        },
        {
          id: "VG-016", points: 300, cefr: "B1",
          q: "In 'League of Legends', what is the name of the main ranked map?",
          a: "Summoner's Rift",
          wrong: ["Howling Abyss", "Twisted Treeline", "Crystal Scar"],
          hint: "It has three lanes and a jungle between them."
        },
        {
          id: "VG-017", points: 400, cefr: "A2",
          q: "The game company Ubisoft was founded in which country?",
          a: "France",
          wrong: ["Canada", "Germany", "Sweden"],
          hint: "The Guillemot brothers started it there in 1986."
        },
        {
          id: "VG-018", points: 400, cefr: "B2",
          q: "What do players call the barrier that stops them leaving the edge of a game map?",
          a: "An invisible wall",
          wrong: ["A hitbox", "A render limit", "A clipping plane"],
          hint: "You cannot see it, but your character simply stops."
        },
        {
          id: "VG-019", points: 500, cefr: "A2",
          q: "In which year did the first Pokémon games come out in Japan?",
          a: "1996",
          wrong: ["1990", "1999", "2002"],
          hint: "It was the same decade as the Nintendo 64."
        },
        {
          id: "VG-020", points: 500, cefr: "B2",
          q: "In gaming, what does 'frame rate' actually measure?",
          a: "Images displayed on screen each second",
          wrong: ["Time needed to load a level", "Memory a game uses while running", "Speed of the internet connection"],
          hint: "It is written as FPS in the settings menu."
        }
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
          id: "TI-001", points: 100, cefr: "A2",
          q: "What does 'www' stand for in a website address?",
          a: "World Wide Web",
          wrong: ["World Wire Web", "Wireless World Web", "Wide World Web"],
          hint: "Invented by Tim Berners-Lee in 1989."
        },
        {
          id: "TI-002", points: 100, cefr: "A2",
          q: "What does 'AI' stand for?",
          a: "Artificial Intelligence",
          wrong: ["Automated Internet", "Advanced Integration", "Assisted Input"],
          hint: "ChatGPT and Claude are well-known examples."
        },
        {
          id: "TI-003", points: 100, cefr: "B1",
          q: "Which company created the Android operating system?",
          a: "Google",
          wrong: ["Samsung", "Apple", "Microsoft"],
          hint: "It is now owned by Google's parent company, Alphabet."
        },
        {
          id: "TI-004", points: 200, cefr: "A2",
          q: "How many bits are in one byte?",
          a: "8",
          wrong: ["4", "16", "10"],
          hint: "Each bit is a single 0 or 1."
        },
        {
          id: "TI-005", points: 200, cefr: "B1",
          q: "What programming language makes websites interactive directly in the browser?",
          a: "JavaScript",
          wrong: ["Python", "Java", "PHP"],
          hint: "Despite the name, it is very different from Java."
        },
        {
          id: "TI-006", points: 200, cefr: "B2",
          q: "What does 'URL' stand for?",
          a: "Uniform Resource Locator",
          wrong: ["Universal Resource Link", "Unified Remote Location", "Universal Reference Locator"],
          hint: "It is the address you type to visit a website."
        },
        {
          id: "TI-007", points: 100, cefr: "A2",
          q: "Which company owns Instagram, WhatsApp, and Facebook?",
          a: "Meta",
          wrong: ["Alphabet", "Microsoft", "ByteDance"],
          hint: "It was formerly known as Facebook, Inc."
        },
        {
          id: "TI-008", points: 300, cefr: "B1",
          q: "What does 'Wi-Fi' officially stand for?",
          a: "Wireless Fidelity",
          wrong: ["Wireless Finder", "Wide Field Internet", "Wireless Frequency Interface"],
          hint: "It was a marketing term modeled after the audio term 'Hi-Fi'."
        },
        {
          id: "TI-009", points: 100, cefr: "B1",
          q: "What is the most popular video-sharing platform in the world?",
          a: "YouTube",
          wrong: ["TikTok", "Instagram", "Twitch"],
          hint: "It is owned by Google."
        },
        {
          id: "TI-010", points: 300, cefr: "B2",
          q: "A hacker who tests systems with permission to find vulnerabilities is called what?",
          a: "White hat hacker",
          wrong: ["Black hat hacker", "Grey hat hacker", "Script kiddie"],
          hint: "The 'good' kind of hacker — hired to find weaknesses."
        },
        {
          id: "TI-011", points: 400, cefr: "B2",
          q: "What does 'HTTP' stand for?",
          a: "Hypertext Transfer Protocol",
          wrong: ["Hypertext Transmission Process", "High Transfer Text Protocol", "Hybrid Text Transfer Protocol"],
          hint: "The 'S' version (HTTPS) adds security encryption."
        },
        {
          id: "TI-012", points: 500, cefr: "B2",
          q: "In cybersecurity, what is a 'Trojan horse'?",
          a: "Malware disguised as software the user wants to install",
          wrong: ["A virus that spreads by duplicating itself across a network", "A program that encrypts files and demands a ransom", "A bot that floods a server with traffic"],
          hint: "Named after the wooden horse used by the Greeks to sneak into Troy."
        },
        {
          id: "TI-013", points: 300, cefr: "A2",
          q: "What does the letter 'G' in '5G' stand for?",
          a: "Generation",
          wrong: ["Gigabyte", "Global", "Gateway"],
          hint: "Each one replaces the phone network before it, about every ten years."
        },
        {
          id: "TI-014", points: 400, cefr: "A2",
          q: "In which year did Apple sell the first iPhone?",
          a: "2007",
          wrong: ["2003", "2005", "2010"],
          hint: "It was one year before the first Android phone went on sale."
        },
        {
          id: "TI-015", points: 400, cefr: "B2",
          q: "Which experimental network, funded by a US research agency, grew into the modern Internet?",
          a: "ARPANET",
          wrong: ["Ethernet", "Usenet", "Bitnet"],
          hint: "It connected a handful of American university computers in 1969."
        },
        {
          id: "TI-016", points: 500, cefr: "B1",
          q: "Who is credited with writing the first computer program, back in the 1840s?",
          a: "Ada Lovelace",
          wrong: ["Grace Hopper", "Hedy Lamarr", "Katherine Johnson"],
          hint: "A British mathematician who worked on Charles Babbage's Analytical Engine."
        },
        {
          id: "TI-017", points: 500, cefr: "A2",
          q: "In which country was the world's first text message sent, in 1992?",
          a: "United Kingdom",
          wrong: ["Finland", "Japan", "United States"],
          hint: "It happened in Europe, but not in the home country of Nokia."
        }
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
          id: "AN-001", points: 100, cefr: "A2",
          q: "What is the fastest land animal on Earth?",
          a: "Cheetah",
          wrong: ["Leopard", "Pronghorn antelope", "Lion"],
          hint: "It can reach over 100 km/h in short bursts."
        },
        {
          id: "AN-002", points: 300, cefr: "A2",
          q: "How many hearts does an octopus have?",
          a: "3",
          wrong: ["1", "2", "4"],
          hint: "Two pump blood to the gills; one pumps to the rest of the body."
        },
        {
          id: "AN-003", points: 100, cefr: "B1",
          q: "Which Amazon animal is the world's largest rodent?",
          a: "Capybara",
          wrong: ["Nutria", "Beaver", "Paca"],
          hint: "It is semi-aquatic, social, and very friendly."
        },
        {
          id: "AN-004", points: 100, cefr: "B1",
          q: "What is the term for an animal that eats only plants?",
          a: "Herbivore",
          wrong: ["Carnivore", "Omnivore", "Insectivore"],
          hint: "The opposite of a carnivore."
        },
        {
          id: "AN-005", points: 100, cefr: "B1",
          q: "Which bear is native to China and eats mostly bamboo?",
          a: "Giant panda",
          wrong: ["Red panda", "Sun bear", "Brown bear"],
          hint: "Black and white, and endangered."
        },
        {
          id: "AN-006", points: 200, cefr: "B2",
          q: "What is the only mammal capable of true, sustained flight?",
          a: "Bat",
          wrong: ["Flying squirrel", "Sugar glider", "Colugo"],
          hint: "It uses echolocation to navigate in the dark."
        },
        {
          id: "AN-007", points: 100, cefr: "A2",
          q: "On which continent is the Amazon rainforest located?",
          a: "South America",
          wrong: ["Africa", "Asia", "Central America"],
          hint: "Most of it is in Brazil."
        },
        {
          id: "AN-008", points: 100, cefr: "A2",
          q: "Which is the largest wild cat in the Americas?",
          a: "Jaguar",
          wrong: ["Puma (mountain lion)", "Ocelot", "Leopard"],
          hint: "In Brazil it is called 'onça-pintada'."
        },
        {
          id: "AN-009", points: 400, cefr: "B1",
          q: "How long is a typical elephant pregnancy (gestation period)?",
          a: "About 22 months",
          wrong: ["About 12 months", "About 9 months", "About 18 months"],
          hint: "The longest gestation of any land animal."
        },
        {
          id: "AN-010", points: 100, cefr: "B1",
          q: "What is the name of the process by which a caterpillar transforms into a butterfly?",
          a: "Metamorphosis",
          wrong: ["Evolution", "Molting", "Pupation"],
          hint: "It happens while the caterpillar is inside a chrysalis."
        },
        {
          id: "AN-011", points: 500, cefr: "B2",
          q: "What is the biological process by which organisms like fireflies and deep-sea fish produce their own light?",
          a: "Bioluminescence",
          wrong: ["Phosphorescence", "Fluorescence", "Chemiluminescence"],
          hint: "It involves a chemical reaction between luciferin and an enzyme."
        },
        {
          id: "AN-012", points: 200, cefr: "A2",
          q: "What do we call a group of lions?",
          a: "A pride",
          wrong: ["A herd", "A pack", "A flock"],
          hint: "The word also means a strong feeling of self-respect."
        },
        {
          id: "AN-013", points: 200, cefr: "B1",
          q: "What is the largest animal that has ever lived on Earth?",
          a: "Blue whale",
          wrong: ["African elephant", "Sperm whale", "Giraffe"],
          hint: "It lives in the ocean and feeds mainly on tiny krill."
        },
        {
          id: "AN-014", points: 300, cefr: "A2",
          q: "Which bird lays the biggest egg?",
          a: "Ostrich",
          wrong: ["Emu", "Albatross", "Condor"],
          hint: "It is also the biggest living bird, and it cannot fly."
        },
        {
          id: "AN-015", points: 300, cefr: "B2",
          q: "What term describes an animal that is active mainly at night and rests during the day?",
          a: "Nocturnal",
          wrong: ["Diurnal", "Crepuscular", "Solitary"],
          hint: "Owls and bats both live this way."
        },
        {
          id: "AN-016", points: 400, cefr: "A2",
          q: "Which bird can hover in one spot and fly backwards?",
          a: "Hummingbird",
          wrong: ["Kingfisher", "Swift", "Sparrow"],
          hint: "It is very small and beats its wings dozens of times a second."
        },
        {
          id: "AN-017", points: 400, cefr: "B1",
          q: "Which bird makes the longest migration of any animal in the world?",
          a: "Arctic tern",
          wrong: ["Canada goose", "Barn swallow", "Wandering albatross"],
          hint: "This seabird chases summer from one end of the planet to the other."
        },
        {
          id: "AN-018", points: 500, cefr: "A2",
          q: "What color is the skin of a polar bear, under its fur?",
          a: "Black",
          wrong: ["White", "Pink", "Grey"],
          hint: "Look at the color of its nose."
        },
        {
          id: "AN-019", points: 500, cefr: "B2",
          q: "What is the scientific term for the release of water vapour from the leaves of plants?",
          a: "Transpiration",
          wrong: ["Condensation", "Respiration", "Germination"],
          hint: "It works like sweating and helps pull water up from the roots."
        }
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
          id: "EL-001", points: 200, cefr: "B2",
          q: "What are the three degrees of comparison for adjectives in English?",
          a: "Positive, comparative, superlative",
          wrong: ["Simple, compound, complex", "Basic, relative, absolute", "Primary, secondary, tertiary"],
          hint: "Example: good → better → best."
        },
        {
          id: "EL-002", points: 100, cefr: "B1",
          q: "What word class (part of speech) does 'quickly' belong to?",
          a: "Adverb",
          wrong: ["Adjective", "Verb", "Preposition"],
          hint: "It modifies a verb — 'he ran quickly'."
        },
        {
          id: "EL-003", points: 100, cefr: "A2",
          q: "What is the past tense of the verb 'to go'?",
          a: "Went",
          wrong: ["Goed", "Gone", "Goes"],
          hint: "It is an irregular verb — does not follow the normal -ed rule."
        },
        {
          id: "EL-004", points: 300, cefr: "A2",
          q: "Which sentence is correct?",
          a: "Their dog is friendly",
          wrong: ["There dog is friendly", "They're dog is friendly", "Thier dog is friendly"],
          hint: "'Their' shows that something belongs to them."
        },
        {
          id: "EL-005", points: 100, cefr: "A2",
          q: "What is a synonym for the word 'enormous'?",
          a: "Huge",
          wrong: ["Tiny", "Moderate", "Average"],
          hint: "It means very large in size."
        },
        {
          id: "EL-006", points: 200, cefr: "A2",
          q: "Which letter is silent in the word 'knife'?",
          a: "K",
          wrong: ["N", "I", "F"],
          hint: "The word was once pronounced more fully in Old English."
        },
        {
          id: "EL-007", points: 100, cefr: "A2",
          q: "What is the plural of 'child'?",
          a: "Children",
          wrong: ["Childs", "Childes", "Childrens"],
          hint: "An irregular plural — it does not end in -s."
        },
        {
          id: "EL-008", points: 300, cefr: "B2",
          q: "What literary device is it when a character speaks their private thoughts aloud, alone on stage?",
          a: "Soliloquy",
          wrong: ["Monologue", "Aside", "Dialogue"],
          hint: "Hamlet's 'To be or not to be' is the most famous example."
        },
        {
          id: "EL-009", points: 100, cefr: "B1",
          q: "What does the prefix 'un-' mean in words like 'unhappy' or 'undo'?",
          a: "Not / reversal of action",
          wrong: ["Again", "Before", "Under"],
          hint: "It negates or reverses the meaning of the base word."
        },
        {
          id: "EL-010", points: 300, cefr: "B1",
          q: "Which sentence uses the present perfect tense correctly?",
          a: "I have finished my homework",
          wrong: ["I finished my homework yesterday", "I am finishing my homework", "I had finish my homework"],
          hint: "It uses 'have/has' + past participle."
        },
        {
          id: "EL-011", points: 400, cefr: "B2",
          q: "What is the grammatical term for words like 'although', 'because', and 'while' that connect clauses?",
          a: "Conjunction",
          wrong: ["Preposition", "Determiner", "Interjection"],
          hint: "They join two ideas and show the relationship between them."
        },
        {
          id: "EL-012", points: 500, cefr: "B2",
          q: "What figure of speech describes a word that imitates the natural sound it refers to, like 'buzz' or 'crash'?",
          a: "Onomatopoeia",
          wrong: ["Alliteration", "Assonance", "Synesthesia"],
          hint: "The word itself sounds like it means."
        },
        {
          id: "EL-013", points: 200, cefr: "A2",
          q: "Which of these words is a preposition?",
          a: "Between",
          wrong: ["Because", "Quickly", "Happy"],
          hint: "It shows the position of one thing in relation to others."
        },
        {
          id: "EL-014", points: 400, cefr: "A2",
          q: "Which two words does the contraction 'won't' come from?",
          a: "Will not",
          wrong: ["Would not", "Was not", "Want not"],
          hint: "The short form hides a future auxiliary verb, not the verb 'want'."
        },
        {
          id: "EL-015", points: 400, cefr: "B1",
          q: "What do we call a word that reads the same forwards and backwards, like 'level'?",
          a: "Palindrome",
          wrong: ["Anagram", "Acronym", "Homophone"],
          hint: "'Radar' and 'Ana' are famous examples."
        },
        {
          id: "EL-016", points: 500, cefr: "B2",
          q: "What is the grammatical name for an '-ing' form used as a noun, as in 'Swimming is fun'?",
          a: "Gerund",
          wrong: ["Participle", "Infinitive", "Auxiliary"],
          hint: "It looks like a verb but does the job of a noun in the sentence."
        },
        {
          id: "EL-017", points: 500, cefr: "A2",
          q: "Which English animal name comes from Tupi, an indigenous language of Brazil?",
          a: "Jaguar",
          wrong: ["Tiger", "Panther", "Leopard"],
          hint: "Portuguese borrowed this big cat's name from Tupi; it prowls the Amazon."
        }
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
          id: "SP-001", points: 100, cefr: "A2",
          q: "How many planets are in our solar system?",
          a: "8",
          wrong: ["9", "7", "10"],
          hint: "Pluto was reclassified as a dwarf planet in 2006."
        },
        {
          id: "SP-002", points: 100, cefr: "B1",
          q: "What is the name of Earth's natural satellite?",
          a: "The Moon",
          wrong: ["Titan", "Io", "Ganymede"],
          hint: "It takes about 27 days to complete one orbit."
        },
        {
          id: "SP-003", points: 100, cefr: "A2",
          q: "Which planet is known as the Red Planet?",
          a: "Mars",
          wrong: ["Jupiter", "Saturn", "Venus"],
          hint: "NASA has sent several rovers there."
        },
        {
          id: "SP-004", points: 200, cefr: "B1",
          q: "What does a light-year actually measure?",
          a: "Distance",
          wrong: ["Time", "Speed", "Brightness of a star"],
          hint: "It is the distance light travels in one year."
        },
        {
          id: "SP-005", points: 100, cefr: "B1",
          q: "What is the name of the galaxy that contains our solar system?",
          a: "The Milky Way",
          wrong: ["Andromeda", "Triangulum", "Centaurus A"],
          hint: "You can see part of it as a band of light on clear nights."
        },
        {
          id: "SP-006", points: 300, cefr: "A2",
          q: "What is the closest star to Earth, after the Sun?",
          a: "Proxima Centauri",
          wrong: ["Sirius", "Alpha Centauri A", "Barnard's Star"],
          hint: "It is about 4.2 light-years away."
        },
        {
          id: "SP-007", points: 300, cefr: "B2",
          q: "At approximately what altitude does the International Space Station orbit Earth?",
          a: "About 400 km",
          wrong: ["About 100 km", "About 1,000 km", "About 36,000 km"],
          hint: "It travels at roughly 28,000 km/h."
        },
        {
          id: "SP-008", points: 200, cefr: "B2",
          q: "What astronomical event occurs when the Moon passes between the Earth and the Sun?",
          a: "Solar eclipse",
          wrong: ["Lunar eclipse", "Transit of Venus", "Supernova"],
          hint: "The Moon's shadow falls on part of Earth."
        },
        {
          id: "SP-009", points: 100, cefr: "A2",
          q: "Which is the largest planet in our solar system?",
          a: "Jupiter",
          wrong: ["Saturn", "Uranus", "Neptune"],
          hint: "It has a famous storm called the Great Red Spot."
        },
        {
          id: "SP-010", points: 200, cefr: "B2",
          q: "What is the name of NASA's space telescope, launched in 1990, that orbits above Earth's atmosphere?",
          a: "Hubble Space Telescope",
          wrong: ["James Webb Space Telescope", "Chandra X-ray Observatory", "Spitzer Space Telescope"],
          hint: "It has produced many iconic images of distant galaxies."
        },
        {
          id: "SP-011", points: 400, cefr: "B2",
          q: "What is the boundary around a black hole beyond which nothing — not even light — can escape?",
          a: "Event horizon",
          wrong: ["Schwarzschild radius", "Photon sphere", "Singularity"],
          hint: "Once crossed, there is no return."
        },
        {
          id: "SP-012", points: 500, cefr: "B2",
          q: "What is the theoretical point of infinite density at the center of a black hole called?",
          a: "Singularity",
          wrong: ["Neutron core", "Event horizon", "Quasar nucleus"],
          hint: "At this point, the known laws of physics break down completely."
        },
        {
          id: "SP-013", points: 300, cefr: "A2",
          q: "Which planet has the hottest surface in our solar system?",
          a: "Venus",
          wrong: ["Mercury", "Mars", "Jupiter"],
          hint: "It is not the closest planet to the Sun, but thick clouds trap the heat."
        },
        {
          id: "SP-014", points: 400, cefr: "A2",
          q: "How long does sunlight take to travel from the Sun to Earth?",
          a: "About 8 minutes",
          wrong: ["About 8 seconds", "About 1 hour", "About 8 hours"],
          hint: "Light travels about 300,000 kilometres every second."
        },
        {
          id: "SP-015", points: 400, cefr: "B2",
          q: "Which spacecraft, launched in 1977, was the first to reach interstellar space?",
          a: "Voyager 1",
          wrong: ["Pioneer 10", "New Horizons", "Cassini"],
          hint: "Its twin probe crossed the same boundary six years after it did."
        },
        {
          id: "SP-016", points: 500, cefr: "A2",
          q: "Who was the first woman to travel into space?",
          a: "Valentina Tereshkova",
          wrong: ["Sally Ride", "Mae Jemison", "Svetlana Savitskaya"],
          hint: "She flew alone on a Soviet mission in 1963."
        },
        {
          id: "SP-017", points: 500, cefr: "B1",
          q: "What is the name of the giant canyon system on Mars, the longest in the solar system?",
          a: "Valles Marineris",
          wrong: ["Olympus Mons", "Hellas Planitia", "Tharsis Ridge"],
          hint: "It is named after the space probe that photographed it in 1971."
        }
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
          id: "FC-001", points: 100, cefr: "A2",
          q: "What is the national dish of Brazil?",
          a: "Feijoada",
          wrong: ["Moqueca", "Churrasco", "Coxinha"],
          hint: "A slow-cooked black bean and pork stew."
        },
        {
          id: "FC-002", points: 100, cefr: "A2",
          q: "From which country does sushi originally come?",
          a: "Japan",
          wrong: ["China", "South Korea", "Vietnam"],
          hint: "It uses vinegared rice and often raw fish."
        },
        {
          id: "FC-003", points: 100, cefr: "A2",
          q: "What is the main ingredient in guacamole?",
          a: "Avocado",
          wrong: ["Tomato", "Mango", "Papaya"],
          hint: "A creamy green fruit."
        },
        {
          id: "FC-004", points: 100, cefr: "A2",
          q: "Pizza is originally from which country?",
          a: "Italy",
          wrong: ["Greece", "United States", "France"],
          hint: "Specifically from the city of Naples."
        },
        {
          id: "FC-005", points: 100, cefr: "B1",
          q: "What traditional Brazilian sweet is covered in chocolate sprinkles and served at every birthday party?",
          a: "Brigadeiro",
          wrong: ["Cocada", "Paçoca", "Beijinho"],
          hint: "Made from condensed milk, cocoa powder, and butter."
        },
        {
          id: "FC-006", points: 100, cefr: "B1",
          q: "Açaí berries, popular in Brazilian bowls, grow in which biome?",
          a: "Amazon rainforest",
          wrong: ["Cerrado", "Mata Atlântica", "Pantanal"],
          hint: "They come from a type of palm tree."
        },
        {
          id: "FC-007", points: 100, cefr: "A2",
          q: "Coxinha is a popular Brazilian street food. What is its traditional filling?",
          a: "Shredded chicken",
          wrong: ["Cheese and ham", "Ground beef", "Shrimp"],
          hint: "It is shaped like a teardrop and fried in batter."
        },
        {
          id: "FC-008", points: 200, cefr: "B1",
          q: "From which country does the dish ramen (noodle soup) originate?",
          a: "Japan",
          wrong: ["China", "South Korea", "Vietnam"],
          hint: "It became iconic Japanese street food in the 20th century."
        },
        {
          id: "FC-009", points: 200, cefr: "B1",
          q: "Tapioca, a popular Brazilian snack, is made from flour extracted from which plant?",
          a: "Cassava",
          wrong: ["Corn", "Wheat", "Rice"],
          hint: "It is a starchy root widely grown in Brazil."
        },
        {
          id: "FC-010", points: 200, cefr: "B1",
          q: "Which traditional Brazilian festival is famous for forró music, quadrilha dancing, and foods like pamonha?",
          a: "Festa Junina",
          wrong: ["Carnaval", "Bumba Meu Boi", "Círio de Nazaré"],
          hint: "Celebrated every June, especially in the Northeast."
        },
        {
          id: "FC-011", points: 300, cefr: "A2",
          q: "What is the traditional Japanese rice wine called?",
          a: "Sake",
          wrong: ["Soju", "Mirin", "Shochu"],
          hint: "It is brewed from fermented rice and served warm or cold."
        },
        {
          id: "FC-012", points: 400, cefr: "B2",
          q: "Which reaction causes the browning of meat or bread cooked at high heat?",
          a: "Maillard reaction",
          wrong: ["Caramelization", "Fermentation", "Emulsification"],
          hint: "It involves a reaction between amino acids and sugars at high temperatures."
        },
        {
          id: "FC-013", points: 500, cefr: "B2",
          q: "Which spice, worth more than gold by weight, comes from the stigmas of a crocus?",
          a: "Saffron",
          wrong: ["Cardamom", "Vanilla", "White truffle"],
          hint: "It gives paella and risotto Milanese their distinctive golden color."
        },
        {
          id: "FC-014", points: 300, cefr: "A2",
          q: "Acarajé is a traditional street food from which Brazilian state?",
          a: "Bahia",
          wrong: ["Minas Gerais", "Paraná", "Ceará"],
          hint: "Think of the Northeast coast and Afro-Brazilian culture."
        },
        {
          id: "FC-015", points: 300, cefr: "B1",
          q: "Kimchi, a dish of salted and fermented vegetables, comes from which country?",
          a: "South Korea",
          wrong: ["Thailand", "Vietnam", "Japan"],
          hint: "It is a country on a peninsula in East Asia."
        },
        {
          id: "FC-016", points: 400, cefr: "A2",
          q: "Which spice gives curry powder its bright yellow color?",
          a: "Turmeric",
          wrong: ["Paprika", "Cumin", "Cinnamon"],
          hint: "Its powder stains hands and clothes yellow very easily."
        },
        {
          id: "FC-017", points: 400, cefr: "B1",
          q: "The Japanese paste miso is made by fermenting which main ingredient?",
          a: "Soybeans",
          wrong: ["Rice grains", "Barley", "Peanuts"],
          hint: "It is a bean, not a grain, and it is very rich in protein."
        },
        {
          id: "FC-018", points: 500, cefr: "A2",
          q: "Vanilla comes from the seed pods of which kind of plant?",
          a: "An orchid",
          wrong: ["A fern", "A cactus", "A palm tree"],
          hint: "It is a flower people often keep in pots at home."
        },
        {
          id: "FC-019", points: 500, cefr: "B2",
          q: "The Asian sauce whose name became 'ketchup' was originally made from what?",
          a: "Fermented fish",
          wrong: ["Sweet plums", "Hot chilli peppers", "Sour limes"],
          hint: "Nothing to do with tomatoes at first; the main ingredient came from the sea."
        }
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
          id: "HB-001", points: 200, cefr: "A2",
          q: "How many bones are in the adult human body?",
          a: "206",
          wrong: ["212", "198", "300"],
          hint: "Babies are born with more — some fuse together over time."
        },
        {
          id: "HB-002", points: 200, cefr: "A2",
          q: "What is the longest bone in the human body?",
          a: "Femur (thigh bone)",
          wrong: ["Tibia (shin bone)", "Humerus (upper arm)", "Fibula"],
          hint: "It is located in your upper leg."
        },
        {
          id: "HB-003", points: 100, cefr: "A2",
          q: "What does the heart pump throughout the body?",
          a: "Blood",
          wrong: ["Oxygen", "Lymph fluid", "Water"],
          hint: "It carries oxygen, nutrients, and waste products."
        },
        {
          id: "HB-004", points: 100, cefr: "B1",
          q: "How many hours of sleep per night are generally recommended for teenagers?",
          a: "8–10 hours",
          wrong: ["6–7 hours", "5–6 hours", "10–12 hours"],
          hint: "Teenagers need more sleep than adults."
        },
        {
          id: "HB-005", points: 200, cefr: "B1",
          q: "Which vitamin is produced by the human skin when exposed to sunlight?",
          a: "Vitamin D",
          wrong: ["Vitamin C", "Vitamin A", "Vitamin B12"],
          hint: "It is essential for bone health and the immune system."
        },
        {
          id: "HB-006", points: 300, cefr: "B1",
          q: "What part of the eye gives it its color and controls how much light enters?",
          a: "Iris",
          wrong: ["Pupil", "Cornea", "Retina"],
          hint: "The pupil is the dark opening in the center of it."
        },
        {
          id: "HB-007", points: 200, cefr: "A2",
          q: "What are the four main human blood types?",
          a: "A, B, AB, and O",
          wrong: ["A, B, C, and D", "A, B, O, and Z", "A, B, AB, and C"],
          hint: "They can also be positive or negative (Rh factor)."
        },
        {
          id: "HB-008", points: 100, cefr: "B1",
          q: "Which organ filters waste from the blood and produces urine?",
          a: "Kidneys",
          wrong: ["Liver", "Bladder", "Spleen"],
          hint: "You have two of them, on either side of your spine."
        },
        {
          id: "HB-009", points: 400, cefr: "B2",
          q: "What brain region, shaped like a seahorse, is responsible for memory formation?",
          a: "Hippocampus",
          wrong: ["Amygdala", "Cerebellum", "Frontal lobe"],
          hint: "Its name comes from the Greek word for 'seahorse'."
        },
        {
          id: "HB-010", points: 100, cefr: "B1",
          q: "How many teeth do adult humans typically have, including wisdom teeth?",
          a: "32",
          wrong: ["28", "30", "36"],
          hint: "Children have only 20 baby teeth."
        },
        {
          id: "HB-011", points: 500, cefr: "B2",
          q: "What is the name of the pigment protein responsible for the color of human skin, hair, and eyes?",
          a: "Melanin",
          wrong: ["Keratin", "Collagen", "Hemoglobin"],
          hint: "It is produced by specialized cells called melanocytes."
        },
        {
          id: "HB-012", points: 300, cefr: "A2",
          q: "Which is the largest organ of the human body?",
          a: "The skin",
          wrong: ["The liver", "The lungs", "The brain"],
          hint: "It is the only organ you can see and touch every day."
        },
        {
          id: "HB-013", points: 300, cefr: "B1",
          q: "Which organ produces bile, the liquid that helps the body digest fats?",
          a: "The liver",
          wrong: ["The pancreas", "The spleen", "The stomach"],
          hint: "It also stores energy and cleans chemicals out of the blood."
        },
        {
          id: "HB-014", points: 400, cefr: "A2",
          q: "How many bones are there in one human hand and wrist?",
          a: "27",
          wrong: ["19", "22", "34"],
          hint: "Eight in the wrist, five in the palm, fourteen in the fingers and thumb."
        },
        {
          id: "HB-015", points: 400, cefr: "B1",
          q: "What is the normal resting heart rate for a healthy adult, in beats per minute?",
          a: "60–100",
          wrong: ["30–50", "110–140", "150–180"],
          hint: "It is slower than a baby's heart and about one beat per second."
        },
        {
          id: "HB-016", points: 500, cefr: "A2",
          q: "How long does a red blood cell live in the human body?",
          a: "About 120 days",
          wrong: ["About 10 days", "About 30 hours", "About 2 years"],
          hint: "Longer than one month, but much less than one year."
        },
        {
          id: "HB-017", points: 500, cefr: "B2",
          q: "Which tiny structures in the small intestine increase the surface area for absorption?",
          a: "Villi",
          wrong: ["Alveoli", "Nephrons", "Follicles"],
          hint: "Their name comes from a Latin word meaning 'shaggy hair'."
        }
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
          id: "EN-001", points: 100, cefr: "B1",
          q: "What gas, released by burning fossil fuels, is most responsible for climate change?",
          a: "Carbon dioxide (CO₂)",
          wrong: ["Oxygen (O₂)", "Methane (CH₄)", "Nitrogen (N₂)"],
          hint: "Plants absorb it during photosynthesis."
        },
        {
          id: "EN-002", points: 100, cefr: "B1",
          q: "What term describes energy sources like solar, wind, and hydropower that do not run out?",
          a: "Renewable energy",
          wrong: ["Nuclear energy", "Fossil fuel energy", "Thermal energy"],
          hint: "The opposite of coal, oil, and gas."
        },
        {
          id: "EN-003", points: 200, cefr: "B1",
          q: "What is the term for the variety of plant and animal life in a particular habitat?",
          a: "Biodiversity",
          wrong: ["Ecosystem", "Biosphere", "Food chain"],
          hint: "Brazil has the highest level of this in the world."
        },
        {
          id: "EN-004", points: 100, cefr: "B1",
          q: "The '3 R's' of sustainability are Reduce, Reuse, and ___?",
          a: "Recycle",
          wrong: ["Repair", "Refuse", "Replace"],
          hint: "Turning waste materials into new products."
        },
        {
          id: "EN-005", points: 200, cefr: "B1",
          q: "What is one of the main causes of rising sea levels worldwide?",
          a: "Melting ice caps and glaciers due to global warming",
          wrong: ["More rain falling into the ocean", "Tectonic plates shifting ocean floors", "Increased river flow into the sea"],
          hint: "As Earth's temperature rises, polar ice melts into the sea."
        },
        {
          id: "EN-006", points: 300, cefr: "B1",
          q: "What is the name of the 2015 international climate agreement signed in France?",
          a: "Paris Agreement",
          wrong: ["Kyoto Protocol", "Montreal Protocol", "Copenhagen Accord"],
          hint: "Countries pledged to limit global temperature rise."
        },
        {
          id: "EN-007", points: 300, cefr: "B2",
          q: "What type of pollution refers to excessive artificial light at night?",
          a: "Light pollution",
          wrong: ["Visual pollution", "Thermal pollution", "Noise pollution"],
          hint: "It prevents us from seeing stars and harms nocturnal animals."
        },
        {
          id: "EN-008", points: 300, cefr: "B1",
          q: "Approximately how many years does it take a plastic bottle to decompose in nature?",
          a: "About 450 years",
          wrong: ["About 50 years", "About 100 years", "About 20 years"],
          hint: "Far longer than any human lifetime."
        },
        {
          id: "EN-009", points: 200, cefr: "B1",
          q: "The hole in the ozone layer is mainly found above which region of Earth?",
          a: "Antarctica",
          wrong: ["The Arctic", "The Sahara Desert", "The Amazon rainforest"],
          hint: "It is at the South Pole."
        },
        {
          id: "EN-010", points: 400, cefr: "B1",
          q: "Approximately what percentage of the world's freshwater is found in Brazil?",
          a: "About 12%",
          wrong: ["About 5%", "About 25%", "About 3%"],
          hint: "Brazil holds the Amazon River and the Pantanal."
        },
        {
          id: "EN-011", points: 500, cefr: "B2",
          q: "Around when did all the plastic ever made outweigh all living animals on Earth?",
          a: "Around 2020",
          wrong: ["Around 2050", "Around 2075", "Around 2100"],
          hint: "Plastic production accelerated so fast that this milestone came much earlier than scientists predicted."
        },
        {
          id: "EN-012", points: 400, cefr: "A2",
          q: "What is the name of the huge area of floating plastic in the North Pacific Ocean?",
          a: "The Great Pacific Garbage Patch",
          wrong: ["The Atlantic Waste Gyre", "The Coral Sea Rubbish Belt", "The Arctic Plastic Field"],
          hint: "It floats in the water between California and Hawaii."
        },
        {
          id: "EN-013", points: 400, cefr: "B1",
          q: "Recycling which metal saves about 95% of the energy needed to make it from ore?",
          a: "Aluminum",
          wrong: ["Steel", "Copper", "Tin"],
          hint: "It is light, silver in color, and it does not rust."
        },
        {
          id: "EN-014", points: 500, cefr: "A2",
          q: "About how much of the world's plastic waste is really recycled?",
          a: "About 9%",
          wrong: ["About 25%", "About 40%", "About 60%"],
          hint: "Most plastic waste is burned or buried instead."
        },
        {
          id: "EN-015", points: 500, cefr: "B2",
          q: "What term describes excess nutrients causing algae blooms that strip oxygen from water?",
          a: "Eutrophication",
          wrong: ["Desalination", "Sedimentation", "Acidification"],
          hint: "The word comes from Greek and means 'well nourished'."
        }
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
          id: "FF-001", points: 400, cefr: "A2",
          q: "Which children's toy was originally sold as a wallpaper cleaner?",
          a: "Play-Doh",
          wrong: ["Silly Putty", "Slinky", "Lego bricks"],
          hint: "It comes in small tubs and smells unmistakable."
        },
        {
          id: "FF-002", points: 300, cefr: "B1",
          q: "Approximately how many languages are spoken in the world today?",
          a: "About 7,000",
          wrong: ["About 700", "About 200", "About 3,000"],
          hint: "About half of them are considered endangered."
        },
        {
          id: "FF-003", points: 300, cefr: "B1",
          q: "Approximately what percentage of Earth's oceans have been explored by humans?",
          a: "About 20%",
          wrong: ["About 80%", "About 50%", "About 5%"],
          hint: "We actually know more about the surface of the Moon."
        },
        {
          id: "FF-004", points: 300, cefr: "B1",
          q: "The hashtag symbol (#) is officially called what?",
          a: "Octothorpe",
          wrong: ["Pound sign", "Hash mark", "Crosshatch"],
          hint: "Most people don't know its official name."
        },
        {
          id: "FF-005", points: 400, cefr: "B2",
          q: "Honey found in ancient Egyptian tombs was still edible after how many years?",
          a: "Over 3,000 years",
          wrong: ["About 100 years", "About 500 years", "About 1,000 years"],
          hint: "Honey never spoils if stored sealed and dry."
        },
        {
          id: "FF-006", points: 400, cefr: "B1",
          q: "Approximately how many muscles does the human body use to take a single step?",
          a: "About 200",
          wrong: ["About 60", "About 120", "About 350"],
          hint: "Walking is far more complex than it seems."
        },
        {
          id: "FF-007", points: 400, cefr: "B1",
          q: "The word 'robot' comes from a Czech word that means what?",
          a: "Forced labor",
          wrong: ["Metal man", "Thinking machine", "Servant"],
          hint: "From Karel Čapek's 1920 play 'R.U.R.'."
        },
        {
          id: "FF-008", points: 500, cefr: "B2",
          q: "If you removed all the empty space from atoms in every human on Earth, we would all fit inside what?",
          a: "A sugar cube",
          wrong: ["A football stadium", "A house", "A city block"],
          hint: "Atoms are almost entirely empty space."
        },
        {
          id: "FF-009", points: 500, cefr: "B1",
          q: "How many times does a hummingbird flap its wings per second?",
          a: "About 50–80 times",
          wrong: ["About 5–10 times", "About 200 times", "About 20–30 times"],
          hint: "This is what creates their distinctive humming sound."
        },
        {
          id: "FF-010", points: 500, cefr: "B1",
          q: "Cleopatra of Egypt lived closer in time to which of these?",
          a: "The Moon landing (1969)",
          wrong: ["The construction of the Great Pyramid", "The invention of the wheel", "The invention of writing"],
          hint: "The Great Pyramid was built ~2560 BC; Cleopatra lived ~50 BC."
        },
        {
          id: "FF-011", points: 100, cefr: "A2",
          q: "How many sides does a standard die (dice) have?",
          a: "6",
          wrong: ["4", "8", "12"],
          hint: "It is a cube."
        },
        {
          id: "FF-012", points: 200, cefr: "A2",
          q: "What is the name of the fear of spiders?",
          a: "Arachnophobia",
          wrong: ["Agoraphobia", "Claustrophobia", "Acrophobia"],
          hint: "'Arachne' is the Greek word for spider."
        },
        {
          id: "FF-013", points: 100, cefr: "A2",
          q: "How many colors does a rainbow traditionally have?",
          a: "Seven",
          wrong: ["Five", "Six", "Eight"],
          hint: "It is the same number as the days in a week."
        },
        {
          id: "FF-014", points: 100, cefr: "A2",
          q: "Which planet is closest to the Sun?",
          a: "Mercury",
          wrong: ["Venus", "Mars", "Earth"],
          hint: "It is also the smallest planet in the Solar System."
        },
        {
          id: "FF-015", points: 200, cefr: "A2",
          q: "What do we call a group of wolves?",
          a: "A pack",
          wrong: ["A pride", "A swarm", "A school"],
          hint: "We use the same word for a set of playing cards."
        },
        {
          id: "FF-016", points: 200, cefr: "B1",
          q: "What do we call a word made by rearranging all the letters of another word?",
          a: "An anagram",
          wrong: ["A palindrome", "An acronym", "A synonym"],
          hint: "'Listen' and 'silent' use exactly the same letters."
        }
      ]
    }
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

  /** CEFR reading levels present in the database, easiest first */
  const CEFR_LEVELS = ["A2", "B1", "B2"];

  /** All questions at the given reading level(s), e.g. getByLevel(["A2","B1"]) */
  function getByLevel(levels) {
    if (!levels || !levels.length) return getAllQuestions();
    const set = new Set(levels);
    return getAllQuestions().filter(q => set.has(q.cefr));
  }

  /**
   * Categories with their questions filtered to the given reading level(s).
   * Returns copies, so the caller can't mutate the source data.
   * Pass nothing (or an empty array) to get everything.
   */
  function getCategoriesByLevel(levels) {
    if (!levels || !levels.length) return categories.map(c => ({ ...c, questions: c.questions.slice() }));
    const set = new Set(levels);
    return categories.map(c => ({ ...c, questions: c.questions.filter(q => set.has(q.cefr)) }));
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
    CEFR_LEVELS,
    getCategories,
    getCategoriesByLevel,
    getByLevel,
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
