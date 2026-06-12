/**
 * texts-a2.js
 * Shared reading text database — A2 level (CEFR)
 * 20 texts, ~150–250 words each
 * Topics: work, travel, technology, food, habits & routine,
 *         health, sports, nature, movies & series, music, and more.
 *
 * Companion files:
 *   texts-a1.js (100–150 words, A1 level)
 *   texts-b1.js (250–350 words, B1 level)
 *   texts-b2.js (400–500 words, B2 level)
 *
 * USAGE (ES Module):
 *   import { texts } from './texts-a2.js';
 *
 * USAGE (plain <script> tag — no module needed):
 *   <script src="texts-a2.js"></script>
 *   // then access window.A2Texts.texts
 *
 * USAGE (GitHub raw URL / jsDelivr CDN):
 *   import { texts } from 'https://cdn.jsdelivr.net/gh/YOUR_USER/YOUR_REPO@main/texts-a2.js';
 */

const texts = [
  // ── 1. WORK ──────────────────────────────────────────────────────────────
  {
    id: 21,
    title: "Working from Home",
    topic: "work",
    level: "A2",
    wordCount: 197,
    text: `In recent years, many companies have started to allow their employees to work from home. This arrangement is called remote work, and it has become very popular since the pandemic.

Working from home has several advantages. You do not need to travel to the office every day, which saves time and money. You can also organize your workspace the way you like and often feel more comfortable at home than in a formal office environment.

However, there are also some challenges. It can be difficult to separate your work life from your personal life when both happen in the same place. Some people also feel lonely because they miss the social interaction they have with colleagues in an office.

Lena has been working remotely for two years. She says the key to making it work is having a clear routine. She starts and finishes at the same time every day. She has a dedicated desk in her bedroom where she only works, so her mind knows when it is time to focus and when it is time to relax.

She also has a video call with her team every morning to stay connected. She thinks remote work is here to stay, and she would not go back to a traditional office full-time.`
  },

  // ── 2. TRAVEL ────────────────────────────────────────────────────────────
  {
    id: 22,
    title: "Planning a Trip Abroad",
    topic: "travel",
    level: "A2",
    wordCount: 210,
    text: `Travelling to another country requires more preparation than a simple weekend trip. You need to think about several things before you leave.

First, you have to check whether you need a visa. This depends on your nationality and the country you are visiting. Some countries allow tourists to enter without a visa for a limited period, while others require you to apply in advance. The application process can take a few weeks, so it is important to plan early.

Second, you should think about travel insurance. This can cover medical expenses if you get sick or have an accident while abroad. It can also protect you if your flight is cancelled or your luggage is lost.

Third, it is a good idea to learn a few basic phrases in the local language. Even simple expressions like "hello," "please," and "thank you" are appreciated by local people and can make your experience much more pleasant.

Tom has been planning a trip to Japan for several months. He has already booked his flights and accommodation. He is studying Japanese on a language app every day. He has also researched the best places to visit and has made a rough itinerary.

He says the planning process is almost as exciting as the trip itself. He cannot wait to try authentic Japanese food and experience a completely different culture.`
  },

  // ── 3. TECHNOLOGY ────────────────────────────────────────────────────────
  {
    id: 23,
    title: "Artificial Intelligence in Daily Life",
    topic: "technology",
    level: "A2",
    wordCount: 205,
    text: `Artificial intelligence, or AI, is no longer something from science fiction movies. It is already part of our everyday lives, even if we do not always notice it.

When you use a music streaming app, AI recommends songs based on what you have listened to before. When you type a message on your phone, AI suggests the next word. When you shop online, AI shows you products similar to the ones you have already looked at. These systems learn from your behavior and try to predict what you want.

AI is also used in more serious areas. Doctors use AI tools to help diagnose diseases by analyzing medical images. Banks use AI to detect unusual transactions that might indicate fraud. Self-driving cars use AI to make decisions while on the road.

However, many people have concerns about AI. One common worry is about privacy. These systems collect and analyze enormous amounts of personal data. Another concern is that AI might replace human workers in many industries, which could cause unemployment.

Despite these concerns, most experts agree that AI will continue to develop rapidly. The challenge for society is to find ways to use this technology responsibly, making sure it benefits everyone and not just a small group of companies or individuals. Understanding how AI works is becoming an important skill for people of all ages.`
  },

  // ── 4. FOOD ──────────────────────────────────────────────────────────────
  {
    id: 24,
    title: "Street Food Around the World",
    topic: "food",
    level: "A2",
    wordCount: 208,
    text: `Street food is one of the best ways to experience a country's culture. It is affordable, delicious, and often reflects recipes that have been passed down through generations.

In Thailand, one of the most popular street foods is pad thai — a stir-fried noodle dish with shrimp, tofu, eggs, and a tangy sauce made from tamarind. Vendors cook it quickly on high heat in a large wok, and the result is a rich, smoky flavor that is hard to find in restaurants.

In Mexico, tacos are sold at almost every street corner. The tortillas are freshly made and filled with meat, salsa, avocado, and lime juice. There are countless varieties, and locals often have strong opinions about which taco stand in their neighborhood is the best.

In India, chaat is a popular snack sold on busy streets. It combines crispy fried dough with chickpeas, yogurt, and chutneys. It is a complex mix of sweet, sour, and spicy flavors all in one bite.

Sara has tried street food in several countries during her travels. She says it always tells you more about a place than any guidebook can. Her advice is simple: find the vendor with the longest queue of local people, because that is usually where the best food is.`
  },

  // ── 5. HABITS & ROUTINE ──────────────────────────────────────────────────
  {
    id: 25,
    title: "Breaking a Bad Habit",
    topic: "habits and routine",
    level: "A2",
    wordCount: 200,
    text: `Everyone has habits — some good and some bad. A habit is something we do automatically, without really thinking about it. The challenge is that bad habits can be very difficult to change, even when we know they are harmful.

David had a habit of checking his phone immediately after waking up. He would spend thirty to forty-five minutes scrolling through news and social media before even getting out of bed. He noticed that this made him feel anxious and unmotivated at the start of every day.

He decided to change this behavior. He read that replacing a habit is more effective than simply trying to stop it. So instead of just telling himself not to check his phone, he replaced the habit with a new one. He started reading a few pages of a book every morning.

The first week was difficult. He often reached for his phone without thinking. But he moved his phone charger to another room so it was not within easy reach. This small change helped a lot.

After about three weeks, the new habit started to feel natural. He says his mornings are now calmer and more productive. He feels ready to start the day instead of feeling overwhelmed by information.

His experience shows that small, consistent changes are often more powerful than dramatic decisions.`
  },

  // ── 6. HEALTH ────────────────────────────────────────────────────────────
  {
    id: 26,
    title: "The Importance of Sleep",
    topic: "health",
    level: "A2",
    wordCount: 203,
    text: `Most adults need between seven and nine hours of sleep per night, but many people regularly sleep much less than this. Sleep deprivation has become a common problem in modern society, and its effects on health are more serious than many people realize.

When we sleep, our bodies repair damaged cells and our brains process and store the information we have learned during the day. Without enough sleep, concentration and memory are significantly affected. People who are sleep-deprived tend to make more mistakes and have slower reaction times. This can be dangerous, especially when driving.

Long-term sleep deprivation is also linked to more serious health conditions, including high blood pressure, obesity, and a weakened immune system, which means the body is less able to fight infections.

Ana, a nurse, works night shifts twice a week. She found it very difficult to maintain a healthy sleep schedule at first. She started experimenting with different strategies: she bought blackout curtains to block daylight, she avoided caffeine after midday, and she tried to go to sleep at the same time even on her days off.

She says there is no perfect solution, but these changes made a noticeable difference. She feels less tired and more focused at work. Sleep, she says, is not a luxury. It is as essential as food and water.`
  },

  // ── 7. SPORTS ────────────────────────────────────────────────────────────
  {
    id: 27,
    title: "The Rise of Women's Football",
    topic: "sports",
    level: "A2",
    wordCount: 206,
    text: `Women's football has grown enormously in popularity over the past decade. Matches that once attracted only a few hundred spectators now fill large stadiums, and international tournaments are broadcast to millions of viewers around the world.

One of the most significant moments was the 2019 FIFA Women's World Cup, held in France, which broke television viewing records in many countries. The final match was watched by nearly 1.2 billion people globally. This was a clear sign that the sport had moved into the mainstream.

Despite this progress, women's football still faces challenges. Female players generally earn much less than their male counterparts, even at the highest professional level. Investment in training facilities, medical support, and coaching for women's teams is often lower than for men's teams.

However, change is happening. Several major clubs have significantly increased their investment in women's football. Sponsorship deals have grown, and media coverage has improved. Young girls growing up today have professional female players as role models in a way that was not possible a generation ago.

Carlos, who coaches a youth football team with both boys and girls, says the attitude of young players has shifted noticeably. Girls now talk confidently about their favorite professional players and their ambitions to play competitively. He believes the future of women's football is very bright.`
  },

  // ── 8. NATURE ────────────────────────────────────────────────────────────
  {
    id: 28,
    title: "Coral Reefs in Danger",
    topic: "nature",
    level: "A2",
    wordCount: 211,
    text: `Coral reefs are among the most diverse ecosystems on Earth. Although they cover less than one percent of the ocean floor, they provide a habitat for roughly twenty-five percent of all marine species. Fish, turtles, sharks, and thousands of other creatures depend on coral reefs to feed, shelter, and reproduce.

Unfortunately, coral reefs around the world are in serious trouble. The main threat is rising ocean temperatures caused by climate change. When water becomes too warm, corals expel the tiny algae that live inside them and give them color and nutrients. This process is called coral bleaching. If the water stays warm for too long, the coral dies.

Pollution is another major problem. Chemicals from agriculture and plastic waste from land end up in the ocean and damage the fragile reef ecosystem. Destructive fishing practices also cause significant harm.

Scientists estimate that up to fifty percent of the world's coral reefs have already been lost. If current trends continue, the situation could become much worse within our lifetimes.

There are efforts to protect and restore coral reefs. Some researchers are growing coral in laboratories and transplanting it onto damaged reefs. Marine protected areas restrict human activity in certain zones to allow recovery.

Experts agree that the most important step is reducing carbon emissions globally to slow down ocean warming before it is too late.`
  },

  // ── 9. MOVIES & SERIES ───────────────────────────────────────────────────
  {
    id: 29,
    title: "The Golden Age of Streaming",
    topic: "movies and series",
    level: "A2",
    wordCount: 207,
    text: `The way people watch films and television series has changed dramatically in the last ten years. Streaming platforms have replaced traditional television as the primary way that most people consume video content, particularly among younger generations.

The appeal is easy to understand. Streaming services give users access to thousands of films and series at any time, without commercial breaks, for a monthly subscription fee. You can watch on a television, a laptop, a tablet, or a phone. You can pause, rewind, and watch at your own pace.

Another major change is the rise of international content. Thanks to streaming, series from South Korea, Spain, Brazil, and other countries have found audiences around the world. The Spanish thriller series "Money Heist" became a global phenomenon, and the South Korean drama "Squid Game" broke records for the number of viewers in its first month.

However, streaming has also created new challenges. The sheer amount of available content can feel overwhelming. Many users spend more time choosing what to watch than actually watching anything — a phenomenon that some call "decision fatigue."

Julia, who works in film production, says the industry has changed more in the last decade than in the fifty years before. She believes the future will bring even more personalized content, with AI helping to match viewers with shows perfectly suited to their tastes.`
  },

  // ── 10. MUSIC ────────────────────────────────────────────────────────────
  {
    id: 30,
    title: "Music and Emotion",
    topic: "music",
    level: "A2",
    wordCount: 198,
    text: `It is something almost everyone has experienced: you hear a song and suddenly you feel happy, sad, nostalgic, or energized. Music has a powerful effect on our emotions, and scientists have been studying this connection for many years.

Research shows that listening to music activates multiple areas of the brain simultaneously, including regions associated with emotion, memory, and movement. This is why a song from your teenage years can instantly bring back vivid memories and feelings from that time.

Music is also used therapeutically. In hospitals and care homes, music therapy has been shown to reduce anxiety, lower blood pressure, and even help patients with dementia to recall memories when other methods have failed.

Different types of music affect us differently. Slow, quiet music tends to calm the nervous system. Fast, rhythmic music can increase energy and motivation, which is why so many people listen to upbeat music while exercising.

Mike, who has been playing guitar for two years, says he first started learning because he wanted to express emotions that he found difficult to put into words. Playing an instrument, he says, is different from listening to music. It requires complete concentration, which means your mind cannot focus on worries or stress at the same time.

For him, music is both an emotional outlet and a form of meditation.`
  },

  // ── 11. SHOPPING ─────────────────────────────────────────────────────────
  {
    id: 31,
    title: "The Shift to Online Shopping",
    topic: "shopping",
    level: "A2",
    wordCount: 204,
    text: `Online shopping has transformed the way people buy goods. What began as a convenient way to purchase books and electronics has expanded to cover almost every product imaginable, from groceries to furniture to luxury fashion.

The advantages are clear. You can shop at any hour of the day without leaving your home. You can easily compare prices from multiple sellers in seconds. Product reviews written by other customers help you make more informed decisions. And most platforms offer free returns if you are not satisfied.

However, online shopping also has drawbacks. You cannot try on clothes or test a product before buying it. The packaging used in delivery generates a significant amount of waste. And the rapid growth of e-commerce has put enormous pressure on small, local shops that cannot compete with the prices and convenience of large online retailers.

Grace used to prefer shopping in physical stores. She liked being able to see and touch what she was buying. But after the pandemic made this more difficult, she shifted most of her shopping online. Now she uses a combination of both, depending on what she needs.

She still visits her local bookshop and bakery every week. She says these places offer something that an online platform cannot: a sense of community, personal recommendation, and the simple pleasure of being somewhere you enjoy.`
  },

  // ── 12. ANIMALS & PETS ───────────────────────────────────────────────────
  {
    id: 32,
    title: "The Benefits of Having a Pet",
    topic: "animals and pets",
    level: "A2",
    wordCount: 196,
    text: `Research consistently shows that having a pet can have a positive impact on a person's mental and physical health. Pet owners tend to experience lower levels of stress, reduced feelings of loneliness, and even lower blood pressure compared to people who do not have pets.

Dogs in particular encourage physical activity. Owners who walk their dogs regularly get considerably more exercise than people without dogs. This not only benefits physical health but also provides regular opportunities to spend time outdoors and interact with other people.

Cats, on the other hand, are often chosen for their more independent nature. The simple act of stroking a cat has been shown to lower cortisol, the hormone associated with stress, and increase the production of serotonin, which improves mood.

Pets are also particularly beneficial for elderly people who live alone. They provide companionship, a sense of purpose, and a daily routine, all of which are important for emotional well-being.

Of course, owning a pet is a significant responsibility. Animals require time, attention, regular veterinary care, and financial commitment. It is important to choose a pet that suits your lifestyle and living situation.

Despite the responsibilities involved, many pet owners say they cannot imagine life without their animals. The bond between a person and a pet can be remarkably deep and meaningful.`
  },

  // ── 13. EDUCATION ────────────────────────────────────────────────────────
  {
    id: 33,
    title: "Learning a Language as an Adult",
    topic: "education",
    level: "A2",
    wordCount: 201,
    text: `There is a common belief that children learn languages more easily than adults. While it is true that children have certain neurological advantages, research suggests that adults are actually capable of making very rapid progress, especially in the early stages.

Adults have significant advantages that children do not. They already understand grammar concepts in their native language, they have a larger vocabulary to draw from when making connections, and they can use deliberate study strategies. Adults are also highly motivated when they choose to learn a language, which is a powerful driver of success.

The main challenge for adult learners is finding enough time. Most adults have jobs, families, and other responsibilities that limit their study time. This is why consistency is more important than the number of hours spent studying. Fifteen minutes of practice every day produces better results than a two-hour session once a week.

Paulo has been learning English for six months. He uses a combination of methods: formal classes twice a week, a vocabulary app on his commute, and watching English-language series with subtitles in the evenings. He recently started having short conversations with a language exchange partner online.

He says the most important thing he has learned is not to be afraid of making mistakes. Errors are an inevitable part of the learning process. The people who progress fastest are those who are willing to speak, even when they are not confident.`
  },

  // ── 14. WEATHER & CLIMATE ────────────────────────────────────────────────
  {
    id: 34,
    title: "Extreme Weather Events",
    topic: "weather",
    level: "A2",
    wordCount: 202,
    text: `In recent years, extreme weather events have become more frequent and more intense around the world. Heatwaves, floods, droughts, and powerful storms are occurring in places that historically experienced relatively mild conditions. Scientists are increasingly confident that these changes are linked to global climate change caused by human activity.

In the summer of 2023, several European countries experienced temperatures that broke historical records. Wildfires burned for weeks across parts of southern Europe and North Africa. At the same time, other regions were dealing with severe flooding caused by unusually heavy rainfall.

These events have serious consequences. Infrastructure such as roads, railways, and buildings can be damaged. Agricultural land can be destroyed, leading to food shortages and higher prices. People who live in affected areas may be forced to evacuate, sometimes permanently.

Climate scientists explain that rising global temperatures increase the energy in the atmosphere, which makes weather patterns more extreme and unpredictable. The warmer the planet becomes, the more frequent and severe these events are likely to be.

Governments, businesses, and individuals are all being called to take action. Reducing carbon emissions through cleaner energy sources, changing consumption habits, and investing in better infrastructure are among the key strategies being discussed.

Many experts warn that the time for gradual, comfortable change has passed. Urgent, coordinated global action is now essential.`
  },

  // ── 15. TECHNOLOGY & SOCIETY ─────────────────────────────────────────────
  {
    id: 35,
    title: "Social Media and Mental Health",
    topic: "technology",
    level: "A2",
    wordCount: 209,
    text: `Social media platforms have connected billions of people around the world, allowing friends and family to stay in touch regardless of distance. They have also given ordinary people the ability to share ideas, start businesses, and participate in global conversations.

However, a growing body of research suggests that heavy use of social media, particularly among teenagers and young adults, is associated with increased levels of anxiety, depression, and low self-esteem. One reason is the constant exposure to carefully curated images of other people's lives. Users tend to post their best moments — holidays, achievements, social events — which creates an unrealistic impression that everyone else is living a happier and more successful life.

The "like" system on many platforms also encourages users to seek validation from others. When a post does not receive many likes, people can feel rejected or unpopular, even though this response is completely disproportionate to reality.

Some platforms are experimenting with changes to address these problems, such as hiding like counts or adding tools that remind users how long they have been scrolling.

Grace, a secondary school teacher, says she has noticed a significant change in her students in the past five years. Many of them struggle to concentrate for long periods and seem to need constant stimulation.

She encourages her students to take regular breaks from their phones and to practice activities that require sustained attention, such as reading or drawing.`
  },

  // ── 16. HOLIDAYS & CELEBRATIONS ──────────────────────────────────────────
  {
    id: 36,
    title: "Carnival Around the World",
    topic: "holidays and celebrations",
    level: "A2",
    wordCount: 200,
    text: `Carnival is one of the most celebrated festivals in the world. Although it is most famously associated with Brazil, it is actually observed in hundreds of countries across different continents, each with its own unique traditions and character.

In Brazil, the most spectacular celebrations take place in Rio de Janeiro. Samba schools — large community organizations that spend the entire year preparing — compete in an enormous parade through a purpose-built stadium called the Sambadrome. The floats are elaborately decorated, the costumes are dazzling, and the music is constant and infectious.

In Trinidad and Tobago, Carnival is considered the greatest street party in the world. Thousands of participants dressed in brightly colored costumes move through the streets to the sound of calypso and soca music.

In Europe, Venice's carnival is famous for its elegant masked costumes, which date back to the medieval period. Participants dress in historical Venetian clothing and ornate masks and gather in the city's picturesque squares and along its canals.

In all its forms, carnival represents a time when social differences are temporarily set aside and communities come together to celebrate through music, dance, and creativity.

Many people who experience carnival for the first time say it is unlike anything else they have seen. The energy, the color, and the sense of collective joy are genuinely unforgettable.`
  },

  // ── 17. TRANSPORT & URBAN LIFE ───────────────────────────────────────────
  {
    id: 37,
    title: "Cities of the Future",
    topic: "travel",
    level: "A2",
    wordCount: 203,
    text: `Urban populations around the world are growing rapidly. By 2050, it is estimated that nearly seventy percent of all people will live in cities. This creates significant challenges around housing, transport, energy, and the environment — but it also creates exciting opportunities for innovation.

The concept of the "smart city" is already being tested in various places. Smart cities use technology to improve the lives of residents and make urban systems more efficient. Sensors placed around the city collect data on traffic, air quality, energy use, and waste. This information is then used to make real-time adjustments that reduce congestion, pollution, and costs.

In some cities, the focus is on creating more walkable and cyclable neighborhoods. The idea is to design areas where residents can access schools, shops, parks, and workplaces within a short walk or cycle ride from home. This reduces car dependency and improves quality of life.

Green spaces are also being prioritized. Trees, parks, and green roofs help to reduce temperatures in cities, improve air quality, and provide residents with places to relax.

Elena, who works as an urban planner, says the most livable cities of the future will be those that put people before cars. She believes that investing in public spaces, green infrastructure, and accessible public transport is the most effective way to create cities where people genuinely want to live.`
  },

  // ── 18. SPORTS & WELL-BEING ──────────────────────────────────────────────
  {
    id: 38,
    title: "Why We Should Play More",
    topic: "sports",
    level: "A2",
    wordCount: 197,
    text: `In childhood, play is recognized as essential for development. Children learn social skills, develop creativity, and build physical coordination through playing. But somewhere in the transition to adulthood, most people stop playing altogether. This, according to many psychologists and health experts, is a serious mistake.

Play for adults does not have to mean competitive sports, though it can. It includes any activity done purely for enjoyment and without a specific goal or outcome — a spontaneous game, an improvised dance, building something just for fun. The key characteristic of play is that it is intrinsically motivated, meaning you do it because you enjoy it, not because you have to.

Research suggests that adults who engage in regular play have lower stress levels, better relationships, and higher levels of creative thinking at work. Play activates the same neural pathways as humor and social bonding, which are important for mental health.

Carlos coaches a youth football team but also plays five-a-side football himself with a group of friends every Thursday evening. He says this is the hour in his week when he completely forgets about work and responsibilities.

He believes that society places too much value on productivity and too little on leisure and play. "We should not wait until retirement to start having fun," he says. "A playful life is a healthier life."`
  },

  // ── 19. FOOD & SUSTAINABILITY ─────────────────────────────────────────────
  {
    id: 39,
    title: "Eating Less Meat",
    topic: "food",
    level: "A2",
    wordCount: 207,
    text: `In many parts of the world, meat has traditionally been considered the centerpiece of a meal. However, attitudes toward meat consumption are changing, particularly among younger generations. A growing number of people are choosing to reduce or eliminate meat from their diets for reasons related to health, the environment, and animal welfare.

From an environmental perspective, the arguments are significant. The production of red meat, especially beef, generates far more greenhouse gas emissions per kilogram than the production of vegetables, legumes, or grains. Livestock farming also uses large amounts of land and water.

From a health perspective, research suggests that diets high in processed and red meat are associated with a higher risk of certain diseases, including heart disease and some types of cancer. On the other hand, diets rich in plants, whole grains, and legumes are linked to better long-term health outcomes.

Many people who reduce their meat consumption do not become vegetarian or vegan. They simply eat meat less often and pay more attention to where their meat comes from, choosing products from farms with higher animal welfare standards.

Jack started cooking plant-based meals twice a week about a year ago. He admits he was sceptical at first, but he has discovered that vegetables can be genuinely exciting when prepared with the right techniques and spices. He says the change has made him a more creative cook, and he no longer misses the meat on those evenings.`
  },

  // ── 20. ENVIRONMENT & SUSTAINABILITY ─────────────────────────────────────
  {
    id: 40,
    title: "The Circular Economy",
    topic: "nature",
    level: "A2",
    wordCount: 208,
    text: `The way our economy currently works is often described as "linear." We extract raw materials from the earth, use them to make products, and then throw those products away when we no longer need them. This linear model generates enormous amounts of waste and puts constant pressure on natural resources.

An alternative model, called the circular economy, is attracting increasing interest from businesses, governments, and environmental organizations. In a circular economy, the aim is to keep materials and products in use for as long as possible. Rather than disposing of a product at the end of its life, it is repaired, refurbished, remanufactured, or recycled so that its materials can be used again.

Some companies are already adopting circular principles. Furniture manufacturers are designing products that can be easily disassembled and their parts reused. Clothing brands are offering repair services and take-back programs where customers return old garments instead of throwing them away. Electronic companies are making devices that can be upgraded rather than replaced.

There are also economic benefits. Businesses that transition to circular models often reduce their costs by using fewer raw materials and creating less waste.

The transition to a circular economy requires changes at every level — in product design, in business models, in consumer behavior, and in government regulation.

Experts say it is not just an environmental ideal. It is a practical and necessary step toward a more sustainable and resilient global economy.`
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

// Browser global (works with a plain <script src="texts-a2.js"> tag)
if (typeof window !== 'undefined') {
  window.A2Texts = { texts, getTopics, getByTopic, getRandom };
}
