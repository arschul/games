/**
 * Facts Database
 * Contains 200 verified true facts and 200 common false facts (misconceptions, myths, lies)
 * Each fact is tagged with categories for easy filtering
 */

const factsDatabase = {
  trueFacts: [
    // Science & Nature (50 facts)
    { id: 1, fact: "Water covers approximately 71% of Earth's surface", category: "science" },
    { id: 2, fact: "The human body contains about 37.2 trillion cells", category: "biology" },
    { id: 3, fact: "Light travels at approximately 299,792 kilometers per second in a vacuum", category: "physics" },
    { id: 4, fact: "Honey never spoils and can last thousands of years", category: "nature" },
    { id: 5, fact: "Octopuses have three hearts and blue blood", category: "biology" },
    { id: 6, fact: "The Sahara Desert is the largest hot desert in the world", category: "geography" },
    { id: 7, fact: "DNA was first isolated by Friedrich Miescher in 1869", category: "biology" },
    { id: 8, fact: "Venus is the hottest planet in our solar system despite not being closest to the Sun", category: "astronomy" },
    { id: 9, fact: "Sharks have been around longer than trees", category: "biology" },
    { id: 10, fact: "The Amazon rainforest produces about 20% of the world's oxygen", category: "nature" },
    { id: 11, fact: "Bananas are berries, but strawberries are not", category: "botany" },
    { id: 12, fact: "A day on Venus is longer than a year on Venus", category: "astronomy" },
    { id: 13, fact: "Neutron stars are so dense that a teaspoon would weigh about 6 billion tons", category: "astronomy" },
    { id: 14, fact: "The human brain uses about 20% of the body's energy", category: "biology" },
    { id: 15, fact: "Polar bears have black skin under their white fur", category: "biology" },
    { id: 16, fact: "The Great Barrier Reef is the largest living structure on Earth", category: "nature" },
    { id: 17, fact: "Lightning is five times hotter than the surface of the Sun", category: "physics" },
    { id: 18, fact: "The human nose can detect over 1 trillion different scents", category: "biology" },
    { id: 19, fact: "Butterflies taste with their feet", category: "biology" },
    { id: 20, fact: "The speed of sound is approximately 343 meters per second at sea level", category: "physics" },
    { id: 21, fact: "Elephants are the only mammals that cannot jump", category: "biology" },
    { id: 22, fact: "The human stomach produces a new layer of mucus every two weeks", category: "biology" },
    { id: 23, fact: "Water expands by about 9% when it freezes", category: "physics" },
    { id: 24, fact: "The average person walks the equivalent of three times around the world in a lifetime", category: "human" },
    { id: 25, fact: "Bamboo is the fastest-growing plant, growing up to 91 cm per day", category: "botany" },
    { id: 26, fact: "The Pacific Ocean is larger than all of Earth's land area combined", category: "geography" },
    { id: 27, fact: "A single bolt of lightning contains enough energy to toast 100,000 slices of bread", category: "physics" },
    { id: 28, fact: "The human eye can distinguish about 10 million different colors", category: "biology" },
    { id: 29, fact: "Mount Everest grows about 4 millimeters each year", category: "geology" },
    { id: 30, fact: "A year on Mercury is only 88 Earth days", category: "astronomy" },
    { id: 31, fact: "The human heart beats about 100,000 times per day", category: "biology" },
    { id: 32, fact: "Fingernails grow about 3.5 millimeters per month", category: "biology" },
    { id: 33, fact: "The Mariana Trench is the deepest point in the ocean at about 11,000 meters", category: "geography" },
    { id: 34, fact: "Cats have 32 muscles in each ear", category: "biology" },
    { id: 35, fact: "A single sneeze can travel up to 160 kilometers per hour", category: "biology" },
    { id: 36, fact: "The Moon is moving away from Earth at about 3.8 centimeters per year", category: "astronomy" },
    { id: 37, fact: "Koalas sleep up to 22 hours per day", category: "biology" },
    { id: 38, fact: "The human body contains enough iron to make a 3-inch nail", category: "biology" },
    { id: 39, fact: "Sea otters hold hands while sleeping to avoid drifting apart", category: "biology" },
    { id: 40, fact: "The Earth's core is as hot as the surface of the Sun", category: "geology" },
    { id: 41, fact: "Hummingbirds are the only birds that can fly backwards", category: "biology" },
    { id: 42, fact: "A cockroach can live for weeks without its head", category: "biology" },
    { id: 43, fact: "The average cloud weighs about 1.1 million pounds", category: "meteorology" },
    { id: 44, fact: "Sloths can hold their breath longer than dolphins", category: "biology" },
    { id: 45, fact: "The human body produces about 25 million new cells each second", category: "biology" },
    { id: 46, fact: "A single tree can absorb about 48 pounds of CO2 per year", category: "botany" },
    { id: 47, fact: "The strongest muscle in the human body relative to its size is the masseter (jaw muscle)", category: "biology" },
    { id: 48, fact: "Snails can sleep for up to three years", category: "biology" },
    { id: 49, fact: "The average person spends about six months of their lifetime waiting for red lights to turn green", category: "human" },
    { id: 50, fact: "There are more stars in the universe than grains of sand on all Earth's beaches", category: "astronomy" },

    // History (40 facts)
    { id: 51, fact: "The Great Wall of China took over 2,000 years to build", category: "history" },
    { id: 52, fact: "Cleopatra lived closer in time to the Moon landing than to the construction of the Great Pyramid", category: "history" },
    { id: 53, fact: "The shortest war in history lasted 38 to 45 minutes between Britain and Zanzibar", category: "history" },
    { id: 54, fact: "The ancient Egyptians used moldy bread as an antibiotic", category: "history" },
    { id: 55, fact: "Vikings never wore horned helmets", category: "history" },
    { id: 56, fact: "The printing press was invented by Johannes Gutenberg around 1440", category: "history" },
    { id: 57, fact: "Oxford University is older than the Aztec Empire", category: "history" },
    { id: 58, fact: "Napoleon Bonaparte was actually average height for his time", category: "history" },
    { id: 59, fact: "The first email was sent in 1971 by Ray Tomlinson", category: "history" },
    { id: 60, fact: "Ancient Romans used urine as mouthwash", category: "history" },
    { id: 61, fact: "The first airplane flight by the Wright Brothers lasted only 12 seconds", category: "history" },
    { id: 62, fact: "Ketchup was sold as medicine in the 1830s", category: "history" },
    { id: 63, fact: "The Eiffel Tower was originally intended to be temporary", category: "history" },
    { id: 64, fact: "The first computer programmer was Ada Lovelace, a woman, in the 1840s", category: "history" },
    { id: 65, fact: "Woolly mammoths were still alive when the pyramids were being built", category: "history" },
    { id: 66, fact: "The first webcam was created to monitor a coffee pot at Cambridge University", category: "history" },
    { id: 67, fact: "The French Revolution began in 1789", category: "history" },
    { id: 68, fact: "The Black Death killed between 75-200 million people in the 14th century", category: "history" },
    { id: 69, fact: "Ancient Greeks used stones as toilet paper", category: "history" },
    { id: 70, fact: "The longest reign of any monarch was Louis XIV of France at 72 years", category: "history" },
    { id: 71, fact: "The first known use of the word 'hello' was in 1827", category: "history" },
    { id: 72, fact: "The Library of Alexandria was one of the largest libraries of the ancient world", category: "history" },
    { id: 73, fact: "The first credit card was introduced in 1950", category: "history" },
    { id: 74, fact: "Alexander the Great conquered most of the known world by age 30", category: "history" },
    { id: 75, fact: "The first photograph ever taken was in 1826", category: "history" },
    { id: 76, fact: "The Ottoman Empire ended in 1922, the same year the USSR was formed", category: "history" },
    { id: 77, fact: "The first electric traffic light was installed in 1914", category: "history" },
    { id: 78, fact: "Julius Caesar was kidnapped by pirates and later had them crucified", category: "history" },
    { id: 79, fact: "The Titanic sank in 1912 on its maiden voyage", category: "history" },
    { id: 80, fact: "Anne Frank and Martin Luther King Jr. were born in the same year (1929)", category: "history" },
    { id: 81, fact: "The first vending machine dispensed holy water in ancient Egypt", category: "history" },
    { id: 82, fact: "Abraham Lincoln was a licensed bartender", category: "history" },
    { id: 83, fact: "The first television commercial aired in 1941", category: "history" },
    { id: 84, fact: "The Spanish Flu pandemic of 1918 killed more people than World War I", category: "history" },
    { id: 85, fact: "The first ATM was installed in London in 1967", category: "history" },
    { id: 86, fact: "Genghis Khan's empire was the largest contiguous land empire in history", category: "history" },
    { id: 87, fact: "The first successful human heart transplant was performed in 1967", category: "history" },
    { id: 88, fact: "The Berlin Wall fell in 1989", category: "history" },
    { id: 89, fact: "The Colosseum in Rome could hold between 50,000 to 80,000 spectators", category: "history" },
    { id: 90, fact: "The first mobile phone call was made in 1973", category: "history" },

    // Geography & Culture (40 facts)
    { id: 91, fact: "There are 195 countries in the world as of 2024", category: "geography" },
    { id: 92, fact: "Vatican City is the smallest country in the world", category: "geography" },
    { id: 93, fact: "Russia spans 11 time zones", category: "geography" },
    { id: 94, fact: "Istanbul is the only city located on two continents", category: "geography" },
    { id: 95, fact: "Africa is the only continent in all four hemispheres", category: "geography" },
    { id: 96, fact: "Canada has the longest coastline of any country", category: "geography" },
    { id: 97, fact: "There are more than 7,000 languages spoken in the world", category: "culture" },
    { id: 98, fact: "The Dead Sea is the lowest point on Earth's surface", category: "geography" },
    { id: 99, fact: "More people live in Tokyo than in all of Canada", category: "geography" },
    { id: 100, fact: "The Nile is generally considered the longest river in the world", category: "geography" },
    { id: 101, fact: "Alaska is both the westernmost and easternmost state in the US", category: "geography" },
    { id: 102, fact: "Antarctica is the driest continent on Earth", category: "geography" },
    { id: 103, fact: "Monaco is the most densely populated country in the world", category: "geography" },
    { id: 104, fact: "The Philippines consists of 7,641 islands", category: "geography" },
    { id: 105, fact: "Indonesia is made up of over 17,000 islands", category: "geography" },
    { id: 106, fact: "China has only one time zone despite spanning five geographical zones", category: "geography" },
    { id: 107, fact: "There are more than 1,000 different types of bananas in the world", category: "nature" },
    { id: 108, fact: "The Netherlands is the world's largest exporter of flowers", category: "geography" },
    { id: 109, fact: "Finland has the most islands of any country in the world", category: "geography" },
    { id: 110, fact: "The Amazon River discharges more water than the next seven largest rivers combined", category: "geography" },
    { id: 111, fact: "Madagascar is home to 5% of all known animal and plant species", category: "geography" },
    { id: 112, fact: "Australia is wider than the Moon", category: "geography" },
    { id: 113, fact: "The Arctic Ocean is the smallest ocean", category: "geography" },
    { id: 114, fact: "Nepal is the only country with a non-rectangular flag", category: "geography" },
    { id: 115, fact: "Lake Baikal in Russia is the deepest lake in the world", category: "geography" },
    { id: 116, fact: "The Andes is the longest mountain range in the world", category: "geography" },
    { id: 117, fact: "Singapore is both a city and a country", category: "geography" },
    { id: 118, fact: "The Sahara Desert is expanding southward", category: "geography" },
    { id: 119, fact: "Mount Kilimanjaro is the tallest free-standing mountain in the world", category: "geography" },
    { id: 120, fact: "The Grand Canyon is about 277 miles long", category: "geography" },
    { id: 121, fact: "Norway has the longest coastline in Europe", category: "geography" },
    { id: 122, fact: "The Atacama Desert in Chile is the driest place on Earth", category: "geography" },
    { id: 123, fact: "Greenland is the world's largest island", category: "geography" },
    { id: 124, fact: "New Zealand was the first country to give women the right to vote", category: "history" },
    { id: 125, fact: "The Great Barrier Reef can be seen from space", category: "geography" },
    { id: 126, fact: "Switzerland has not been in a state of war since 1815", category: "history" },
    { id: 127, fact: "Japan has over 6,800 islands", category: "geography" },
    { id: 128, fact: "The Red Sea got its name from algae that occasionally blooms red", category: "geography" },
    { id: 129, fact: "The longest place name in the world has 85 letters and is in New Zealand", category: "geography" },
    { id: 130, fact: "Dubai's Burj Khalifa is the tallest building in the world", category: "geography" },

    // Technology & Innovation (35 facts)
    { id: 131, fact: "The first computer bug was an actual moth trapped in a computer", category: "technology" },
    { id: 132, fact: "The first computer mouse was made of wood", category: "technology" },
    { id: 133, fact: "More than 90% of the world's currency is digital", category: "technology" },
    { id: 134, fact: "The first iPhone was released in 2007", category: "technology" },
    { id: 135, fact: "Google processes over 8.5 billion searches per day", category: "technology" },
    { id: 136, fact: "The first 1GB hard drive weighed over 500 pounds", category: "technology" },
    { id: 137, fact: "WiFi stands for Wireless Fidelity", category: "technology" },
    { id: 138, fact: "The first website ever created is still online", category: "technology" },
    { id: 139, fact: "More than 500 hours of video are uploaded to YouTube every minute", category: "technology" },
    { id: 140, fact: "The password for the computer controls of nuclear missiles was '00000000' for 20 years", category: "technology" },
    { id: 141, fact: "Amazon was originally going to be called 'Cadabra'", category: "technology" },
    { id: 142, fact: "Nokia was originally founded as a paper mill company in 1865", category: "technology" },
    { id: 143, fact: "The first alarm clock could only ring at 4 AM", category: "technology" },
    { id: 144, fact: "The average person unlocks their phone 150 times per day", category: "technology" },
    { id: 145, fact: "Bitcoin was created in 2009 by an unknown person using the pseudonym Satoshi Nakamoto", category: "technology" },
    { id: 146, fact: "The first computer virus was created in 1983", category: "technology" },
    { id: 147, fact: "USB stands for Universal Serial Bus", category: "technology" },
    { id: 148, fact: "The @ symbol was used in 1971 for the first email address", category: "technology" },
    { id: 149, fact: "Facebook has over 3 billion monthly active users", category: "technology" },
    { id: 150, fact: "The first YouTube video was uploaded on April 23, 2005", category: "technology" },
    { id: 151, fact: "GPS technology is free and maintained by the US government", category: "technology" },
    { id: 152, fact: "The first 3D printer was created in 1984", category: "technology" },
    { id: 153, fact: "Bluetooth is named after a 10th century Viking king", category: "technology" },
    { id: 154, fact: "The first domain name ever registered was Symbolics.com in 1985", category: "technology" },
    { id: 155, fact: "QR codes were invented in Japan in 1994", category: "technology" },
    { id: 156, fact: "The camera on smartphones was originally developed for video calling", category: "technology" },
    { id: 157, fact: "The first text message was sent in 1992", category: "technology" },
    { id: 158, fact: "The term 'bug' in computing comes from a real moth found in a computer", category: "technology" },
    { id: 159, fact: "The first webcam was created to watch a coffee pot", category: "technology" },
    { id: 160, fact: "Computer monitors emit no radiation harmful to humans", category: "technology" },
    { id: 161, fact: "The first computer weighed more than 27 tons", category: "technology" },
    { id: 162, fact: "Email existed before the World Wide Web", category: "technology" },
    { id: 163, fact: "The first video game was created in 1958", category: "technology" },
    { id: 164, fact: "The original name for Windows was Interface Manager", category: "technology" },
    { id: 165, fact: "The first online banner ad appeared in 1994", category: "technology" },

    // Human Body & Health (35 facts)
    { id: 166, fact: "The human body has 206 bones in adulthood", category: "biology" },
    { id: 167, fact: "Your brain is about 73% water", category: "biology" },
    { id: 168, fact: "The human body is made up of about 60% water", category: "biology" },
    { id: 169, fact: "Your left lung is smaller than your right lung to make room for your heart", category: "biology" },
    { id: 170, fact: "The human body has enough carbon to make 900 pencils", category: "biology" },
    { id: 171, fact: "Babies are born with about 300 bones, but adults have 206", category: "biology" },
    { id: 172, fact: "The human brain can generate about 23 watts of power", category: "biology" },
    { id: 173, fact: "Your nose can remember 50,000 different scents", category: "biology" },
    { id: 174, fact: "The average person blinks about 15-20 times per minute", category: "biology" },
    { id: 175, fact: "Human teeth are just as strong as shark teeth", category: "biology" },
    { id: 176, fact: "The human body sheds about 600,000 particles of skin every hour", category: "biology" },
    { id: 177, fact: "Your stomach acid is strong enough to dissolve metal", category: "biology" },
    { id: 178, fact: "The human brain weighs about 3 pounds", category: "biology" },
    { id: 179, fact: "Red blood cells live for about 120 days", category: "biology" },
    { id: 180, fact: "The average person produces about 25,000 quarts of saliva in a lifetime", category: "biology" },
    { id: 181, fact: "Your body has about 60,000 miles of blood vessels", category: "biology" },
    { id: 182, fact: "The average person farts about 14 times a day", category: "biology" },
    { id: 183, fact: "Human bones are 5 times stronger than steel of the same density", category: "biology" },
    { id: 184, fact: "Your sense of smell is about 10,000 times more sensitive than your sense of taste", category: "biology" },
    { id: 185, fact: "The human body contains about 0.2 milligrams of gold", category: "biology" },
    { id: 186, fact: "Your small intestine is about 22 feet long", category: "biology" },
    { id: 187, fact: "The average person walks about 110,000 miles in their lifetime", category: "biology" },
    { id: 188, fact: "Human hair grows about 6 inches per year", category: "biology" },
    { id: 189, fact: "Your brain uses about 20% of your body's oxygen", category: "biology" },
    { id: 190, fact: "The human body has more than 600 muscles", category: "biology" },
    { id: 191, fact: "Your heart beats about 100,000 times a day", category: "biology" },
    { id: 192, fact: "The average person spends about 26 years sleeping", category: "human" },
    { id: 193, fact: "Your tongue print is unique, just like your fingerprints", category: "biology" },
    { id: 194, fact: "The human body can detect taste in 0.0015 seconds", category: "biology" },
    { id: 195, fact: "Your eyes can distinguish approximately 10 million different colors", category: "biology" },
    { id: 196, fact: "The human body produces about 1 liter of mucus per day", category: "biology" },
    { id: 197, fact: "Your skin is the largest organ of your body", category: "biology" },
    { id: 198, fact: "The average person breathes about 20,000 times per day", category: "biology" },
    { id: 199, fact: "Your body has more bacterial cells than human cells", category: "biology" },
    { id: 200, fact: "The human brain can process images in as little as 13 milliseconds", category: "biology" }
  ],

  falseFacts: [
    // Science Myths (50 facts)
    { id: 1, fact: "Lightning never strikes the same place twice", category: "science", truth: "Lightning often strikes the same place multiple times, especially tall structures" },
    { id: 2, fact: "Humans only use 10% of their brain", category: "science", truth: "Humans use virtually all of their brain, just not all at once" },
    { id: 3, fact: "Cracking your knuckles causes arthritis", category: "health", truth: "No scientific evidence links knuckle cracking to arthritis" },
    { id: 4, fact: "Sugar makes children hyperactive", category: "health", truth: "Studies show no direct link between sugar and hyperactivity" },
    { id: 5, fact: "Goldfish have a 3-second memory", category: "biology", truth: "Goldfish can remember things for months" },
    { id: 6, fact: "Humans can see the Great Wall of China from space", category: "science", truth: "The Great Wall is not visible from space with the naked eye" },
    { id: 7, fact: "Shaving makes hair grow back thicker", category: "biology", truth: "Shaving doesn't change hair thickness or growth rate" },
    { id: 8, fact: "Bats are blind", category: "biology", truth: "Bats can see, though many use echolocation" },
    { id: 9, fact: "Chameleons change color to match their surroundings", category: "biology", truth: "Chameleons change color for communication and temperature regulation" },
    { id: 10, fact: "Different parts of the tongue taste different flavors", category: "biology", truth: "All taste buds can detect all flavors" },
    { id: 11, fact: "Bulls are enraged by the color red", category: "biology", truth: "Bulls are colorblind to red; they react to movement" },
    { id: 12, fact: "You lose most body heat through your head", category: "science", truth: "Heat loss is proportional to surface area exposed" },
    { id: 13, fact: "Water conducts electricity", category: "physics", truth: "Pure water is a poor conductor; impurities conduct electricity" },
    { id: 14, fact: "Ostriches bury their heads in sand when scared", category: "biology", truth: "Ostriches lower their heads to tend to eggs, not from fear" },
    { id: 15, fact: "Touching a baby bird will make its mother reject it", category: "biology", truth: "Most birds have a poor sense of smell and won't reject touched babies" },
    { id: 16, fact: "You need to wait 24 hours before reporting a missing person", category: "law", truth: "You can report someone missing immediately" },
    { id: 17, fact: "Caffeine dehydrates you", category: "health", truth: "Caffeine has a mild diuretic effect but doesn't cause dehydration" },
    { id: 18, fact: "Eating carrots improves your night vision", category: "health", truth: "Carrots are healthy but won't give you night vision beyond normal" },
    { id: 19, fact: "Pennies dropped from tall buildings can kill", category: "physics", truth: "Terminal velocity and tumbling make pennies non-lethal" },
    { id: 20, fact: "Swimming after eating causes cramps", category: "health", truth: "No evidence supports waiting to swim after eating" },
    { id: 21, fact: "Sharks can smell a drop of blood from miles away", category: "biology", truth: "Sharks have good smell but not from miles away" },
    { id: 22, fact: "Dogs sweat by salivating", category: "biology", truth: "Dogs sweat through their paw pads and cool through panting" },
    { id: 23, fact: "The Earth's seasons are caused by distance from the Sun", category: "astronomy", truth: "Seasons are caused by Earth's axial tilt, not distance" },
    { id: 24, fact: "Glass is a slow-flowing liquid", category: "physics", truth: "Glass is an amorphous solid, not a liquid" },
    { id: 25, fact: "Mount Everest is the tallest mountain on Earth", category: "geography", truth: "Mauna Kea is taller from base to peak; Everest is highest above sea level" },
    { id: 26, fact: "Veins are blue because they carry blue blood", category: "biology", truth: "Blood is always red; veins look blue due to light absorption" },
    { id: 27, fact: "Alcohol kills brain cells", category: "health", truth: "Alcohol damages connections but doesn't directly kill neurons" },
    { id: 28, fact: "The five-second rule for dropped food is safe", category: "health", truth: "Bacteria transfer happens instantly, not after five seconds" },
    { id: 29, fact: "Antibiotics cure viral infections", category: "health", truth: "Antibiotics only work on bacterial infections, not viruses" },
    { id: 30, fact: "Humans evolved from chimpanzees", category: "biology", truth: "Humans and chimps share a common ancestor, we didn't evolve from them" },
    { id: 31, fact: "You can catch a cold from being cold", category: "health", truth: "Colds are caused by viruses, not temperature" },
    { id: 32, fact: "Eating at night makes you gain more weight", category: "health", truth: "Total calories matter, not timing of meals" },
    { id: 33, fact: "MSG is dangerous and causes headaches", category: "health", truth: "Scientific studies show MSG is safe for most people" },
    { id: 34, fact: "Vaccines cause autism", category: "health", truth: "Numerous studies prove no link between vaccines and autism" },
    { id: 35, fact: "You only catch a cold once per virus strain", category: "health", truth: "Viruses mutate and immunity wanes over time" },
    { id: 36, fact: "Lemmings commit mass suicide", category: "biology", truth: "This myth came from a staged documentary; lemmings don't do this" },
    { id: 37, fact: "Organic food is pesticide-free", category: "agriculture", truth: "Organic farming uses certain approved pesticides" },
    { id: 38, fact: "Microwaves cook food from the inside out", category: "physics", truth: "Microwaves penetrate food but cook from outside in" },
    { id: 39, fact: "Hair and nails continue growing after death", category: "biology", truth: "Skin dehydration creates this illusion; growth stops at death" },
    { id: 40, fact: "A falling cat always lands on its feet", category: "biology", truth: "Cats often land on their feet but not always safely" },
    { id: 41, fact: "You should tilt your head back during a nosebleed", category: "health", truth: "Lean forward to prevent blood from going down your throat" },
    { id: 42, fact: "Reading in dim light damages your eyes", category: "health", truth: "It may cause eye strain but no permanent damage" },
    { id: 43, fact: "Natural sweeteners are healthier than sugar", category: "health", truth: "Most natural sweeteners have similar effects on the body as sugar" },
    { id: 44, fact: "You can detox your body with special diets", category: "health", truth: "Your liver and kidneys naturally detox; special diets aren't necessary" },
    { id: 45, fact: "Knives are safer dull than sharp", category: "safety", truth: "Dull knives require more force and slip more easily, causing injuries" },
    { id: 46, fact: "Electric cars produce zero emissions", category: "environment", truth: "Emissions depend on electricity source; manufacturing has impact too" },
    { id: 47, fact: "Toilet water swirls opposite directions in different hemispheres", category: "physics", truth: "Toilet design determines swirl direction, not the Coriolis effect" },
    { id: 48, fact: "Frogs in boiling water is a real phenomenon", category: "biology", truth: "Frogs will jump out when water gets too hot; this is a myth" },
    { id: 49, fact: "Waking a sleepwalker is dangerous", category: "health", truth: "It's not dangerous, though they may be confused or startled" },
    { id: 50, fact: "Eating turkey makes you sleepy because of tryptophan", category: "health", truth: "Many foods have tryptophan; overeating causes the sleepiness" },

    // Historical Myths (40 facts)
    { id: 51, fact: "Vikings wore horned helmets", category: "history", truth: "No archaeological evidence supports horned Viking helmets" },
    { id: 52, fact: "Napoleon was very short", category: "history", truth: "Napoleon was average height for his time (5'7\")" },
    { id: 53, fact: "Columbus discovered America", category: "history", truth: "Indigenous peoples were already there; Vikings arrived centuries before Columbus" },
    { id: 54, fact: "Medieval people thought the Earth was flat", category: "history", truth: "Educated people knew Earth was round since ancient times" },
    { id: 55, fact: "Einstein failed math in school", category: "history", truth: "Einstein excelled at math from a young age" },
    { id: 56, fact: "The Romans invented the vomitorium to vomit during feasts", category: "history", truth: "Vomitoria were passages for crowds, not vomiting rooms" },
    { id: 57, fact: "People in medieval times rarely bathed", category: "history", truth: "Medieval people bathed more regularly than Victorian-era stereotypes suggest" },
    { id: 58, fact: "George Washington had wooden teeth", category: "history", truth: "His dentures were made of ivory, metal, and human/animal teeth" },
    { id: 59, fact: "The Great Wall of China is the only man-made structure visible from space", category: "history", truth: "Many structures are visible from space; the Wall is hard to see" },
    { id: 60, fact: "Iron maidens were medieval torture devices", category: "history", truth: "Iron maidens were 18th-19th century hoaxes" },
    { id: 61, fact: "Salem witch trials burned witches at the stake", category: "history", truth: "Salem witches were hanged, not burned" },
    { id: 62, fact: "Nero fiddled while Rome burned", category: "history", truth: "The fiddle wasn't invented yet; Nero may have played the lyre" },
    { id: 63, fact: "Edison invented the light bulb", category: "history", truth: "Edison improved existing designs; others invented light bulbs first" },
    { id: 64, fact: "Thanksgiving was the first harvest celebration between Pilgrims and Native Americans", category: "history", truth: "Many cultures had harvest celebrations; the 'first Thanksgiving' is mythologized" },
    { id: 65, fact: "Cleopatra was Egyptian", category: "history", truth: "Cleopatra was of Greek Macedonian descent" },
    { id: 66, fact: "Henry VIII had six wives and beheaded them all", category: "history", truth: "He had six wives but only beheaded two of them" },
    { id: 67, fact: "Marie Antoinette said 'Let them eat cake'", category: "history", truth: "No evidence she said this; likely propaganda" },
    { id: 68, fact: "The Pyramids were built by slaves", category: "history", truth: "Evidence suggests paid workers built the pyramids" },
    { id: 69, fact: "Abraham Lincoln wrote the Gettysburg Address on the back of an envelope", category: "history", truth: "Lincoln prepared the speech in advance" },
    { id: 70, fact: "Paul Revere shouted 'The British are coming!'", category: "history", truth: "He warned quietly to avoid British patrols; colonists considered themselves British" },
    { id: 71, fact: "The apple fell on Newton's head and he discovered gravity", category: "history", truth: "The apple story is likely embellished; gravity theory took years" },
    { id: 72, fact: "Rosa Parks was just tired when she refused to give up her seat", category: "history", truth: "Parks was an activist who planned her protest" },
    { id: 73, fact: "Viking funerals involved burning bodies on boats set out to sea", category: "history", truth: "This dramatic depiction is largely fictional" },
    { id: 74, fact: "The Wild West was extremely violent and lawless", category: "history", truth: "Many frontier towns had lower crime rates than modern cities" },
    { id: 75, fact: "Medieval chastity belts were common", category: "history", truth: "Chastity belts are largely Victorian-era fabrications" },
    { id: 76, fact: "Pocahontas fell in love with John Smith", category: "history", truth: "Pocahontas was a child when they met; the romance is fictional" },
    { id: 77, fact: "The forbidden fruit in Eden was an apple", category: "religion", truth: "The Bible doesn't specify the fruit type" },
    { id: 78, fact: "Mussolini made the trains run on time", category: "history", truth: "This was propaganda; Italian railways improved before he took power" },
    { id: 79, fact: "Gladiators fought to the death every time", category: "history", truth: "Many gladiator fights weren't fatal; gladiators were valuable" },
    { id: 80, fact: "The Library of Alexandria was destroyed in one fire", category: "history", truth: "It declined over centuries through multiple incidents" },
    { id: 81, fact: "Catherine the Great died having sex with a horse", category: "history", truth: "This is a malicious rumor; she died of a stroke" },
    { id: 82, fact: "Ancient Greeks and Romans had white marble statues", category: "history", truth: "Statues were originally painted in bright colors" },
    { id: 83, fact: "Hitler was a vegetarian who loved animals", category: "history", truth: "Nazi propaganda; evidence shows he ate meat" },
    { id: 84, fact: "The Forbidden City was always called that", category: "history", truth: "The name 'Forbidden City' is a Western invention" },
    { id: 85, fact: "Vikings discovered America and settled permanently", category: "history", truth: "Vikings visited briefly but didn't establish lasting settlements" },
    { id: 86, fact: "Medieval peasants only lived to age 30", category: "history", truth: "High infant mortality skewed average; adults often lived to 60+" },
    { id: 87, fact: "The Boston Tea Party was a protest against high tea taxes", category: "history", truth: "It protested taxation without representation and monopoly, not high taxes" },
    { id: 88, fact: "Witches were burned at the stake throughout medieval Europe", category: "history", truth: "Witch hunts peaked in early modern period, not medieval times" },
    { id: 89, fact: "Beethoven was completely deaf when he composed his best works", category: "history", truth: "He had severe hearing loss but wasn't completely deaf" },
    { id: 90, fact: "Spartans threw weak babies off cliffs", category: "history", truth: "No archaeological evidence supports this practice" },

    // Food & Nutrition Myths (30 facts)
    { id: 91, fact: "MSG is bad for your health", category: "health", truth: "FDA considers MSG safe; reactions are rare" },
    { id: 92, fact: "Brown eggs are healthier than white eggs", category: "nutrition", truth: "Eggshell color doesn't affect nutrition" },
    { id: 93, fact: "You need to drink 8 glasses of water daily", category: "health", truth: "Water needs vary; food provides water too" },
    { id: 94, fact: "Breakfast is the most important meal of the day", category: "nutrition", truth: "This originated from marketing; no scientific consensus" },
    { id: 95, fact: "Eating late at night causes weight gain", category: "nutrition", truth: "Total calories matter more than timing" },
    { id: 96, fact: "Fat-free foods are always healthier", category: "nutrition", truth: "Fat-free often means added sugar and less nutrition" },
    { id: 97, fact: "Fresh vegetables are always more nutritious than frozen", category: "nutrition", truth: "Frozen vegetables often retain more nutrients" },
    { id: 98, fact: "You should never reheat rice", category: "food", truth: "Properly stored and reheated rice is safe" },
    { id: 99, fact: "Microwaving food destroys nutrients", category: "nutrition", truth: "Microwaving preserves nutrients better than some cooking methods" },
    { id: 100, fact: "Sugar causes diabetes", category: "health", truth: "Type 2 diabetes is complex; sugar alone doesn't cause it" },
    { id: 101, fact: "All bacteria in food are harmful", category: "health", truth: "Many bacteria are beneficial, like probiotics" },
    { id: 102, fact: "Carbs are bad and should be avoided", category: "nutrition", truth: "Complex carbs are essential for health" },
    { id: 103, fact: "You can't eat protein and carbs together", category: "nutrition", truth: "No scientific basis for food combining rules" },
    { id: 104, fact: "Double-dipping chips spreads massive bacteria", category: "health", truth: "Risk is minimal; saliva has antibacterial properties" },
    { id: 105, fact: "Brown sugar is healthier than white sugar", category: "nutrition", truth: "Both are nutritionally similar" },
    { id: 106, fact: "Egg yolks are bad for your heart", category: "nutrition", truth: "Dietary cholesterol has less impact than once thought" },
    { id: 107, fact: "All fats are unhealthy", category: "nutrition", truth: "Healthy fats are essential for the body" },
    { id: 108, fact: "Juice cleanses detox your body", category: "health", truth: "Your liver and kidneys naturally detox" },
    { id: 109, fact: "Gluten is bad for everyone", category: "health", truth: "Only problematic for those with celiac disease or sensitivity" },
    { id: 110, fact: "You should avoid all GMO foods", category: "nutrition", truth: "Scientific consensus is that GMOs are safe" },
    { id: 111, fact: "Spicy food causes stomach ulcers", category: "health", truth: "Most ulcers are caused by H. pylori bacteria" },
    { id: 112, fact: "Raw cookie dough is dangerous only because of eggs", category: "health", truth: "Raw flour can also contain harmful bacteria" },
    { id: 113, fact: "Spinach is the best source of iron", category: "nutrition", truth: "Many foods have more bioavailable iron than spinach" },
    { id: 114, fact: "Cracking eggs on the side of a bowl is best", category: "cooking", truth: "Cracking on a flat surface reduces shell fragments" },
    { id: 115, fact: "You need milk for strong bones", category: "nutrition", truth: "Many non-dairy sources provide calcium" },
    { id: 116, fact: "Eating celery burns more calories than it contains", category: "nutrition", truth: "The calorie difference is negligible" },
    { id: 117, fact: "Chocolate causes acne", category: "health", truth: "No strong scientific link between chocolate and acne" },
    { id: 118, fact: "Coconut oil is a superfood", category: "nutrition", truth: "Coconut oil is high in saturated fat with mixed health effects" },
    { id: 119, fact: "Raw food diets are healthier", category: "nutrition", truth: "Cooking can increase nutrient availability in many foods" },
    { id: 120, fact: "You should wash chicken before cooking", category: "food", truth: "Washing spreads bacteria; cooking kills it" },

    // Animal Myths (30 facts)
    { id: 121, fact: "Elephants are afraid of mice", category: "biology", truth: "No evidence elephants fear mice specifically" },
    { id: 122, fact: "Owls can turn their heads 360 degrees", category: "biology", truth: "Owls can rotate their heads about 270 degrees" },
    { id: 123, fact: "Dogs age 7 years for every human year", category: "biology", truth: "Dog aging is more complex and varies by size" },
    { id: 124, fact: "Cats always land on their feet unharmed", category: "biology", truth: "Cats have a righting reflex but can still be injured" },
    { id: 125, fact: "Dolphins are fish", category: "biology", truth: "Dolphins are mammals" },
    { id: 126, fact: "Piranhas can strip a human to bones in minutes", category: "biology", truth: "Piranhas are generally not aggressive toward humans" },
    { id: 127, fact: "All dinosaurs were huge", category: "biology", truth: "Many dinosaurs were small, some chicken-sized" },
    { id: 128, fact: "Camels store water in their humps", category: "biology", truth: "Camel humps store fat, not water" },
    { id: 129, fact: "Snakes are slimy", category: "biology", truth: "Snake skin is dry and smooth" },
    { id: 130, fact: "Penguins mate for life", category: "biology", truth: "Most penguin species find new partners each year" },
    { id: 131, fact: "A woodpecker's tongue wraps around its brain", category: "biology", truth: "The tongue wraps around the skull, not the brain" },
    { id: 132, fact: "Sharks can smell fear", category: "biology", truth: "Sharks can't detect emotions, only chemicals in water" },
    { id: 133, fact: "All spiders are poisonous", category: "biology", truth: "Most spiders are venomous, not poisonous, and most are harmless to humans" },
    { id: 134, fact: "Opossums hang from their tails", category: "biology", truth: "Adult opossums are too heavy to hang by their tails" },
    { id: 135, fact: "You can tell a dog's age by its nose wetness", category: "biology", truth: "Nose wetness indicates hydration, not age" },
    { id: 136, fact: "All sharks must keep swimming or they'll die", category: "biology", truth: "Many shark species can pump water through their gills while stationary" },
    { id: 137, fact: "Porcupines can shoot their quills", category: "biology", truth: "Quills detach on contact but aren't shot" },
    { id: 138, fact: "Mice love cheese", category: "biology", truth: "Mice prefer grains and sweets over cheese" },
    { id: 139, fact: "Wolves howl at the moon", category: "biology", truth: "Wolves howl to communicate, not at the moon" },
    { id: 140, fact: "Mother birds reject babies touched by humans", category: "biology", truth: "Birds have poor sense of smell and won't reject touched babies" },
    { id: 141, fact: "Daddy longlegs are the most venomous spiders", category: "biology", truth: "They have weak venom and can't bite humans effectively" },
    { id: 142, fact: "Earwigs crawl into people's ears to lay eggs", category: "biology", truth: "This is a myth; earwigs don't target human ears" },
    { id: 143, fact: "Houseflies only live for 24 hours", category: "biology", truth: "Houseflies typically live 15-30 days" },
    { id: 144, fact: "Bumblebees shouldn't be able to fly", category: "biology", truth: "Physics fully explains bumblebee flight" },
    { id: 145, fact: "All pit bulls are naturally aggressive", category: "biology", truth: "Temperament depends on training and socialization, not breed" },
    { id: 146, fact: "Lizards can regenerate their entire bodies", category: "biology", truth: "Only tails can regenerate in some species" },
    { id: 147, fact: "Koalas are bears", category: "biology", truth: "Koalas are marsupials, not bears" },
    { id: 148, fact: "Crocodiles cry when they eat", category: "biology", truth: "Crocodile tears lubricate eyes, not from emotion" },
    { id: 149, fact: "Frogs give you warts", category: "biology", truth: "Warts are caused by viruses, not frogs" },
    { id: 150, fact: "Turkeys drown in the rain by looking up", category: "biology", truth: "This is false; turkeys are not that unintelligent" },

    // Common Misconceptions (50 facts)
    { id: 151, fact: "Shaving causes hair to grow back darker and thicker", category: "health", truth: "Hair appears coarser because it's blunt cut, not because it's thicker" },
    { id: 152, fact: "You lose most of your body heat through your head", category: "science", truth: "Heat loss is proportional to exposed surface area" },
    { id: 153, fact: "Toilets flush in opposite directions in different hemispheres", category: "science", truth: "Toilet design determines direction, not Coriolis effect" },
    { id: 154, fact: "You need to wait an hour after eating before swimming", category: "health", truth: "No evidence supports this; you can swim after eating" },
    { id: 155, fact: "Fan death is real (sleeping with a fan kills you)", category: "myth", truth: "This is a Korean urban legend with no scientific basis" },
    { id: 156, fact: "Undercover cops must identify themselves if asked", category: "law", truth: "Undercover officers can lie about their identity" },
    { id: 157, fact: "Sitting too close to the TV damages your eyes", category: "health", truth: "May cause eye strain but no permanent damage" },
    { id: 158, fact: "You can see the Great Wall of China from the Moon", category: "science", truth: "You cannot see the Great Wall from the Moon" },
    { id: 159, fact: "Searing meat seals in juices", category: "cooking", truth: "Searing creates flavor through Maillard reaction, doesn't seal juices" },
    { id: 160, fact: "Diamonds are formed from compressed coal", category: "geology", truth: "Most diamonds form from carbon in the mantle, predating coal" },
    { id: 161, fact: "Vikings used skulls as drinking cups", category: "history", truth: "No archaeological evidence supports this" },
    { id: 162, fact: "Fortune cookies are Chinese", category: "culture", truth: "Fortune cookies were invented in California" },
    { id: 163, fact: "Chicken soup cures colds", category: "health", truth: "It may ease symptoms but doesn't cure colds" },
    { id: 164, fact: "Lightning never strikes the same place twice", category: "science", truth: "Lightning frequently strikes the same place" },
    { id: 165, fact: "Alcohol warms you up when cold", category: "health", truth: "Alcohol makes you feel warm but actually lowers core temperature" },
    { id: 166, fact: "You eat spiders in your sleep", category: "myth", truth: "This is an internet hoax; it rarely if ever happens" },
    { id: 167, fact: "Blood is blue before it's oxygenated", category: "biology", truth: "Blood is always red; deoxygenated blood is darker red" },
    { id: 168, fact: "Different sections of the tongue taste different flavors", category: "biology", truth: "All taste buds can detect all basic tastes" },
    { id: 169, fact: "Goldfish will grow to the size of their tank", category: "biology", truth: "Stunted growth from small tanks is unhealthy, not natural" },
    { id: 170, fact: "You can get the flu from the flu vaccine", category: "health", truth: "The vaccine contains dead virus and can't cause flu" },
    { id: 171, fact: "Chewing gum takes 7 years to digest", category: "health", truth: "Gum passes through your system like other foods" },
    { id: 172, fact: "Peeing on a jellyfish sting helps", category: "health", truth: "This can make stings worse; use vinegar or hot water" },
    { id: 173, fact: "Bottled water is healthier than tap water", category: "health", truth: "Tap water is often equally safe and more regulated" },
    { id: 174, fact: "Vikings wore horned helmets in battle", category: "history", truth: "Horned helmets are a 19th-century invention" },
    { id: 175, fact: "Coffee is made from beans", category: "botany", truth: "Coffee 'beans' are actually seeds" },
    { id: 176, fact: "Waking a sleepwalker will harm them", category: "health", truth: "It's safe, though they may be confused" },
    { id: 177, fact: "Poinsettias are deadly poisonous", category: "botany", truth: "Poinsettias are mildly toxic but rarely harmful" },
    { id: 178, fact: "You should put butter on burns", category: "health", truth: "Butter can trap heat; use cool water instead" },
    { id: 179, fact: "Swallowed gum stays in your stomach for years", category: "health", truth: "Gum passes through the digestive system normally" },
    { id: 180, fact: "Police need a warrant to enter your home", category: "law", truth: "There are many exceptions to warrant requirements" },
    { id: 181, fact: "Cracking your knuckles will give you arthritis", category: "health", truth: "No evidence links knuckle cracking to arthritis" },
    { id: 182, fact: "Bees die immediately after stinging", category: "biology", truth: "Only honey bees die; other bees and wasps can sting multiple times" },
    { id: 183, fact: "Stress causes gray hair", category: "biology", truth: "Graying is primarily genetic and age-related" },
    { id: 184, fact: "Eating before bed gives you nightmares", category: "health", truth: "No strong scientific evidence supports this" },
    { id: 185, fact: "Green mucus means you need antibiotics", category: "health", truth: "Color doesn't indicate bacterial infection" },
    { id: 186, fact: "Reading in poor light will ruin your eyesight", category: "health", truth: "Causes temporary eye strain, not permanent damage" },
    { id: 187, fact: "Teething babies get fevers", category: "health", truth: "Teething doesn't cause significant fevers" },
    { id: 188, fact: "You need to starve a fever and feed a cold", category: "health", truth: "Stay hydrated and nourished for both" },
    { id: 189, fact: "Drinking coffee sobers you up", category: "health", truth: "Coffee doesn't reduce blood alcohol content" },
    { id: 190, fact: "Violent video games cause violent behavior", category: "psychology", truth: "Research shows no clear causal link" },
    { id: 191, fact: "Breaking a mirror brings 7 years of bad luck", category: "superstition", truth: "This is a superstition with no basis in reality" },
    { id: 192, fact: "Friday the 13th is unlucky", category: "superstition", truth: "This is a superstition; no evidence of increased bad luck" },
    { id: 193, fact: "Black cats are bad luck", category: "superstition", truth: "This is a superstition; cats don't affect luck" },
    { id: 194, fact: "Touching frogs gives you warts", category: "biology", truth: "Warts are caused by viruses, not frogs" },
    { id: 195, fact: "Eating watermelon seeds will make a watermelon grow in your stomach", category: "biology", truth: "Seeds pass through digestive system without growing" },
    { id: 196, fact: "Crossing your eyes will make them stay that way", category: "health", truth: "Eyes will return to normal position" },
    { id: 197, fact: "If you shave, hair grows back thicker", category: "biology", truth: "Shaving doesn't change hair growth or thickness" },
    { id: 198, fact: "Eating poppy seeds will make you fail a drug test", category: "health", truth: "Modern tests can distinguish poppy seeds from drugs" },
    { id: 199, fact: "Sharks don't get cancer", category: "biology", truth: "Sharks do get cancer, though perhaps at lower rates" },
    { id: 200, fact: "Medieval people had terrible teeth", category: "history", truth: "Before refined sugar, dental health was often better than later periods" }
  ]
};

// Helper functions
const factUtils = {
  /**
   * Get all true facts
   */
  getAllTrueFacts: () => factsDatabase.trueFacts,

  /**
   * Get all false facts
   */
  getAllFalseFacts: () => factsDatabase.falseFacts,

  /**
   * Get random fact from either category
   * @param {string} type - 'true', 'false', or 'random'
   * @returns {object} Random fact object
   */
  getRandomFact: (type = 'random') => {
    let pool;
    if (type === 'true') {
      pool = factsDatabase.trueFacts;
    } else if (type === 'false') {
      pool = factsDatabase.falseFacts;
    } else {
      pool = [...factsDatabase.trueFacts, ...factsDatabase.falseFacts];
    }
    return pool[Math.floor(Math.random() * pool.length)];
  },

  /**
   * Get facts by category
   * @param {string} category - Category name
   * @param {string} type - 'true', 'false', or 'both'
   * @returns {array} Array of facts in that category
   */
  getFactsByCategory: (category, type = 'both') => {
    const results = [];
    
    if (type === 'true' || type === 'both') {
      results.push(...factsDatabase.trueFacts.filter(f => f.category === category));
    }
    
    if (type === 'false' || type === 'both') {
      results.push(...factsDatabase.falseFacts.filter(f => f.category === category));
    }
    
    return results;
  },

  /**
   * Get all unique categories
   * @param {string} type - 'true', 'false', or 'both'
   * @returns {array} Array of category names
   */
  getCategories: (type = 'both') => {
    const categories = new Set();
    
    if (type === 'true' || type === 'both') {
      factsDatabase.trueFacts.forEach(f => categories.add(f.category));
    }
    
    if (type === 'false' || type === 'both') {
      factsDatabase.falseFacts.forEach(f => categories.add(f.category));
    }
    
    return Array.from(categories).sort();
  },

  /**
   * Search facts by keyword
   * @param {string} keyword - Search term
   * @param {string} type - 'true', 'false', or 'both'
   * @returns {array} Array of matching facts
   */
  searchFacts: (keyword, type = 'both') => {
    const results = [];
    const searchTerm = keyword.toLowerCase();
    
    if (type === 'true' || type === 'both') {
      results.push(...factsDatabase.trueFacts.filter(f => 
        f.fact.toLowerCase().includes(searchTerm)
      ));
    }
    
    if (type === 'false' || type === 'both') {
      results.push(...factsDatabase.falseFacts.filter(f => 
        f.fact.toLowerCase().includes(searchTerm) ||
        (f.truth && f.truth.toLowerCase().includes(searchTerm))
      ));
    }
    
    return results;
  },

  /**
   * Get a quiz set of mixed true/false facts
   * @param {number} count - Number of facts to return
   * @returns {array} Shuffled array of facts
   */
  getQuizSet: (count = 10) => {
    const allFacts = [
      ...factsDatabase.trueFacts.map(f => ({ ...f, isTrue: true })),
      ...factsDatabase.falseFacts.map(f => ({ ...f, isTrue: false }))
    ];
    
    // Shuffle array
    const shuffled = allFacts.sort(() => 0.5 - Math.random());
    
    // Return requested count
    return shuffled.slice(0, count);
  }
};

// Export for use in Node.js or browser
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { factsDatabase, factUtils };
}
