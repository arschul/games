/**
 * texts-a2-new.js
 * Additional A2 reading texts — IDs 101–120
 * ~150–250 words each. New topics expand the original set.
 * window.A2TextsNew / ES export: { texts, getTopics, getByTopic, getRandom }
 */

const texts = [
  {
    id: 101, title: "Moving to a New City", topic: "housing and home", level: "A2", wordCount: 192,
    text: `Six months ago, Mia moved to a new city for work. She left her hometown for the first time. It was both exciting and frightening.

Finding an apartment was the first challenge. She searched online for weeks. Most apartments were too expensive or too far from the office. Finally, she found a small studio near the city center. It was on the fourth floor with a view of the street.

The apartment was unfurnished. Mia had to buy everything: a bed, a desk, a sofa, and kitchen equipment. She bought most things second-hand from online marketplaces to save money. Little by little, the empty apartment began to feel like a home.

In the beginning, Mia felt very lonely. She did not know anyone in the city. She missed her friends and family. She called her mother every day.

But slowly, things got better. She made friends at work. She joined a yoga class in her neighborhood and met people there. She discovered a good café near her apartment where she likes to read on Sunday mornings.

Now Mia says the move was the best decision she ever made. She has grown more independent and confident. She visits her hometown once a month, but the new city is home now.`
  },
  {
    id: 102, title: "Fashion and Identity", topic: "clothing and fashion", level: "A2", wordCount: 185,
    text: `The clothes we wear say a lot about who we are. Fashion is not just about looking good. It is a way of expressing our personality and values.

Some people follow the latest trends carefully. They read fashion magazines and check social media to know what is popular. For them, wearing stylish clothes is important for their confidence and social image.

Others prefer a more personal style. They choose clothes based on how comfortable they feel rather than what is fashionable. They might mix vintage pieces with modern items or always wear the same simple, practical style.

There is also a growing movement of people who think about the environmental impact of their clothing choices. They buy second-hand clothes, choose sustainable brands, or simply buy fewer items and wear them for longer.

Fashion also reflects culture. Traditional clothing from different countries often carries deep historical meaning. Wearing cultural dress can be a source of pride and identity.

What is clear is that fashion is never neutral. Every choice we make about what to wear sends a message to the world about who we are and what matters to us. Whether we think about it or not, we are all making a statement every time we get dressed.`
  },
  {
    id: 103, title: "The History of My Street", topic: "history", level: "A2", wordCount: 190,
    text: `I have lived on the same street all my life. Recently, I became curious about its history and started to do some research.

I found out that my street is over two hundred years old. In the nineteenth century, it was a busy trading route. Merchants used it to bring goods from the port to the city market. Some of the buildings on my street were built during that period and are still standing today.

In the early twentieth century, the street changed character. Several of the large merchant houses were divided into smaller apartments as the city grew and more workers moved in from the countryside. A small factory was also built at the end of the street, which closed in the 1970s.

Today, the old factory is an arts center. Artists have studios there, and there are regular exhibitions and events. It is a popular place in the neighborhood.

I spoke to an old man who has lived on the street for seventy years. He remembers when it was much noisier and busier with small shops on every corner. He says the street is quieter now, but more pleasant.

Learning about the history of my street made me look at it differently. The ordinary places around us often have extraordinary stories hidden inside them.`
  },
  {
    id: 104, title: "Body Language", topic: "language and communication", level: "A2", wordCount: 193,
    text: `When we communicate with other people, we use much more than words. The way we move our bodies, make eye contact, and position ourselves tells others a great deal about what we are thinking and feeling. This is called body language, and it is a significant part of all human communication.

Some experts estimate that more than half of all communication is non-verbal. The tone of our voice and our body language often communicate more than the words themselves. For example, you can say "I'm fine" with your words while your crossed arms, low voice, and downward gaze tell a completely different story.

Different cultures have different norms for body language. In some cultures, direct eye contact is a sign of confidence and honesty. In others, it can be considered rude or aggressive, particularly toward older people or authority figures. Similarly, the appropriate amount of physical distance between two people having a conversation varies significantly across cultures.

Being aware of body language can improve our relationships and communication. A simple adjustment — like uncrossing your arms, making more eye contact, or leaning slightly forward when someone is speaking — can make the other person feel much more heard and respected.

Learning to read and adjust your body language is a skill, but one that anyone can develop with a little practice and attention.`
  },
  {
    id: 105, title: "Urban Farming", topic: "agriculture and farming", level: "A2", wordCount: 188,
    text: `In cities around the world, a growing number of people are growing their own food. Urban farming — the practice of cultivating plants and sometimes raising animals within a city — is becoming increasingly popular for many reasons.

Some urban farmers grow food in community gardens, where a group of neighbors share a plot of land. Others grow plants on rooftops, on balconies, or even inside their homes under artificial lighting. These small-scale farms can produce herbs, salad leaves, tomatoes, and other vegetables.

Urban farming offers several benefits. It gives city residents access to fresh, local food at a lower cost. It also provides a sense of community, as people work together and share produce. For many people, gardening is also a relaxing and satisfying activity that reduces stress.

From an environmental perspective, urban farming can reduce the distance food needs to travel before it is eaten, which lowers carbon emissions from transportation. Rooftop gardens can also help to insulate buildings and reduce urban heat.

However, urban farming has limits. Most city spaces can only produce a small fraction of the food their residents need. Space, soil quality, water access, and the high cost of urban land are all significant challenges.

Still, many city planners see urban farming as a small but valuable part of making cities more sustainable and liveable in the future.`
  },
  {
    id: 106, title: "The Human Brain", topic: "science and discovery", level: "A2", wordCount: 191,
    text: `The human brain is the most complex organ in the known universe. It contains approximately 86 billion neurons — nerve cells that communicate with each other through electrical and chemical signals. These connections form the basis of everything we think, feel, remember, and do.

The brain is divided into different regions, each with specialized functions. The frontal lobe, at the front of the brain, is associated with planning, decision-making, and personality. The temporal lobes, on the sides, are involved in language and memory. The cerebellum, at the back and bottom, coordinates movement and balance.

One of the most remarkable properties of the brain is its plasticity — its ability to change and reorganize itself in response to experience. When we learn something new, new connections form between neurons. When we practice a skill repeatedly, those connections become stronger and faster. This is the biological basis of all learning and habit formation.

Scientists still have many unanswered questions about the brain. We do not fully understand consciousness — the experience of being aware and feeling things from the inside. We also do not fully understand why we dream or exactly how long-term memories are stored.

Brain research is one of the most active and exciting areas of science today. New imaging technologies are allowing researchers to observe brain activity in real time and reveal secrets that were completely hidden just a generation ago.`
  },
  {
    id: 107, title: "Pocket Money and Saving", topic: "business and money", level: "A2", wordCount: 187,
    text: `Many parents give their children a small amount of money each week, known as pocket money or an allowance. This practice is common in many countries and is often seen as a way to teach children about the value of money from an early age.

With pocket money, children learn to make choices. If they spend all their money on sweets or games at the beginning of the week, they will have nothing left for something they want at the end. This experience of making decisions and accepting the consequences is valuable preparation for adult financial life.

Some parents connect pocket money to chores or responsibilities. Children might earn their allowance by washing the dishes, cleaning their room, or helping with the shopping. This approach links money to work, which is how most adults experience it.

Financial experts generally recommend encouraging children to divide their pocket money into three categories: spending, saving, and giving. Saving a portion each week, even a small amount, teaches the habit of putting money aside for the future. Giving a portion teaches generosity and the idea that money can be used to help others.

Carlos, who is twelve, saves half of his pocket money every week. He is saving for a new bicycle. He says it feels much better to buy something with your own saved money than to simply ask for it as a gift.`
  },
  {
    id: 108, title: "A Day in Court", topic: "crime and justice", level: "A2", wordCount: 194,
    text: `Last year, I was selected for jury duty. I had to go to the local court and help decide a case. It was a new and interesting experience.

The case was about a person accused of stealing from a shop. In court, there was a judge, a lawyer for the prosecution, a lawyer for the defence, and twelve members of the jury, including me.

The prosecution presented evidence: a security camera video and the statements of two shop workers. The defence lawyer argued that the video was not clear enough to be certain.

Both lawyers asked questions to witnesses. The judge made sure the proceedings were fair and orderly.

After both sides finished, the jury went to a separate room to discuss. We talked for about two hours. Each person gave their opinion. We had to reach a unanimous decision — all twelve of us had to agree.

In the end, we decided the person was not guilty. The evidence was not strong enough to be certain.

The experience made me understand how important courts are in a fair society. It also showed me how much care and time is needed to make a judgment about another person's life. I have a much deeper respect for justice now.`
  },
  {
    id: 109, title: "Traditional Food and Family Memory", topic: "food", level: "A2", wordCount: 189,
    text: `For many people, food is not just about nutrition. It is connected to memory, identity, and the feeling of belonging to a family or a culture.

When we eat a dish that a parent or grandparent used to make, we often feel a powerful emotional connection. The smell of a soup or the taste of a particular cake can instantly bring back childhood memories that we thought we had forgotten. Food is one of the strongest triggers for memory in the human brain.

Traditional family recipes are often passed down from one generation to the next, sometimes without ever being written down. A grandmother teaches a daughter by standing beside her in the kitchen, showing her how much salt to add or how to fold a pastry by touch and feel. This kind of knowledge is sometimes called "embodied knowledge" — it lives in the hands and the senses, not in books.

As families move to different cities or countries, traditional food can become even more important. Making a dish from the homeland is a way of staying connected to an identity that might otherwise fade. Many immigrant communities maintain their cultural traditions most powerfully through food.

Ana's family came to Brazil from Italy three generations ago. Every Christmas, her family still makes the same pasta dish her great-grandmother brought from Sicily. For them, it is not just food. It is the thread that connects them to their history.`
  },
  {
    id: 110, title: "Staying Safe Online", topic: "technology", level: "A2", wordCount: 186,
    text: `As more of our daily lives move online, the importance of digital safety has grown significantly. Young people in particular spend a lot of time on the internet, and it is important to understand the risks involved.

One of the most common risks is phishing — when someone sends a fake email or message pretending to be a bank, a company, or even a friend, in order to get personal information such as passwords or payment details. These messages often look very convincing. The key sign that something is wrong is often a sense of urgency: the message tells you to act immediately or something bad will happen.

Another risk is oversharing personal information on social media. Posting your home address, school name, or daily routine can make you vulnerable to people with bad intentions. It is generally a good idea to keep personal details private and to review your privacy settings regularly.

Creating strong, unique passwords for different accounts is also essential. Using the same simple password for multiple sites means that if one account is hacked, the others are at risk too.

Many schools now include digital literacy in their curriculum, teaching students to evaluate online information critically and to recognize potential dangers.

The internet is an extraordinary resource, but using it safely requires knowledge and attention, just like any other powerful tool.`
  },
  {
    id: 111, title: "A Wedding", topic: "holidays and celebrations", level: "A2", wordCount: 191,
    text: `Last summer, I attended my cousin's wedding. It was one of the most beautiful events I have ever been to.

The wedding ceremony took place in a small chapel in the countryside. The bride wore a long white dress with flowers in her hair. The groom wore a dark suit with a white flower in his pocket. They looked very happy and a little nervous.

The ceremony lasted about forty minutes. The couple exchanged rings and made promises to each other in front of all the guests. Many people were crying, including my aunt.

After the ceremony, we went to a large venue nearby for the reception. There were about one hundred and twenty guests. The tables were decorated with candles and flowers. We ate a four-course dinner: soup, salad, roast meat, and a beautiful three-layer cake.

In the evening, there was music and dancing. Even the grandparents were dancing. My little cousin fell asleep on a chair in the corner.

What I liked most was seeing how happy the couple were throughout the day. They laughed and danced all evening.

Weddings are a reminder that celebrating important moments with the people we love is one of the most valuable things in life. I went home that night feeling full of warmth.`
  },
  {
    id: 112, title: "Money and Happiness", topic: "business and money", level: "A2", wordCount: 192,
    text: `Most people have heard the phrase "money cannot buy happiness." But the relationship between money and happiness is more complicated than this simple saying suggests.

Research in psychology shows that money does increase happiness — but only up to a certain level. When people do not have enough money to cover their basic needs — food, housing, healthcare, security — their wellbeing suffers significantly. In this situation, more money clearly leads to more happiness because it removes stress and provides stability.

However, once basic needs are comfortably met, the relationship changes. Studies have found that beyond a certain income level, earning more money has a much smaller effect on how happy a person feels day to day. At this level, the factors that matter most for happiness are not financial — they are things like strong relationships, meaningful work, good health, and a sense of purpose.

This does not mean wealthy people are unhappy. But it does suggest that focusing only on earning more, at the expense of relationships, rest, and meaningful activities, is unlikely to make a person significantly happier.

Interestingly, research also shows that spending money on others — buying gifts, donating to charity, or paying for an experience to share with friends — produces more happiness than spending the same amount on yourself.

The conclusion seems to be that how we use money matters as much as how much of it we have.`
  },
  {
    id: 113, title: "The History of Writing", topic: "history", level: "A2", wordCount: 187,
    text: `Writing is one of the most important inventions in human history. Before writing existed, knowledge was passed from person to person through spoken language and memory. This meant that information could easily be lost or changed over time.

The earliest writing systems appeared approximately five thousand years ago in ancient Mesopotamia, in the region that is now Iraq. This writing, called cuneiform, was made by pressing a reed into soft clay tablets. It was used mainly to keep records of goods and trade.

Around the same time, ancient Egyptians developed a writing system called hieroglyphics, which used pictures and symbols to represent words and sounds. Hieroglyphics were carved into stone walls, painted on pottery, and written on papyrus — an early form of paper made from plants.

Over thousands of years, writing systems became simpler and more flexible. The alphabet, as we know it today, developed gradually from earlier symbol-based systems. Our modern Latin alphabet is descended from Phoenician writing, which was later adapted by the Greeks and Romans.

The invention of the printing press in the fifteenth century transformed writing again. Books could be produced quickly and cheaply, making knowledge available to many more people.

Today, digital technology has transformed writing once more. The act of reading and writing now happens on screens as much as on paper, and information can be shared globally in seconds.`
  },
  {
    id: 114, title: "Volunteering", topic: "family and relationships", level: "A2", wordCount: 189,
    text: `Volunteering means giving your time and skills to help others without receiving payment. Millions of people around the world volunteer, and the benefits are felt both by those who help and those who receive help.

There are many types of volunteering. Some people volunteer at food banks, helping to distribute food to families who cannot afford it. Others volunteer at hospitals, care homes, or schools. Some people clean up parks and beaches, while others help with disaster relief after floods, earthquakes, or fires.

Research shows that volunteering has significant benefits for the volunteers themselves. People who volunteer regularly report higher levels of happiness and satisfaction than those who do not. They also tend to feel a stronger sense of connection to their community and a clearer sense of purpose.

For young people, volunteering can provide valuable experience and skills that are useful when applying for jobs or university. It also helps develop empathy — the ability to understand and share the feelings of others.

Tom started volunteering at a local food bank when he was seventeen. He works there two Saturday mornings a month. He says the experience has changed how he sees the world. He meets people whose lives are very different from his own, and he feels a deep sense of satisfaction knowing that the work he does makes a real difference to families in his community.`
  },
  {
    id: 115, title: "How Vaccines Work", topic: "medicine and body", level: "A2", wordCount: 193,
    text: `Vaccines are one of the greatest achievements of modern medicine. They have saved hundreds of millions of lives and eliminated or significantly reduced many dangerous diseases.

To understand how vaccines work, you need to understand a little about the immune system. When a dangerous virus or bacteria enters the body, the immune system produces proteins called antibodies to fight the infection. This process takes time, and in the meantime, the person becomes ill. However, once the body has fought an infection, it "remembers" how to produce the right antibodies quickly. If the same infection returns, the response is much faster, and the person may not become ill at all.

Vaccines work by training the immune system without causing the actual disease. Traditional vaccines introduce a weakened or dead version of the pathogen — the virus or bacteria — into the body. The immune system recognizes it as a threat and produces antibodies. If the real pathogen appears later, the body is already prepared.

More recent vaccines, like the mRNA vaccines developed for COVID-19, work differently. Instead of introducing a piece of the pathogen, they contain instructions that teach the body's own cells to produce a specific protein that the immune system then learns to recognize.

Vaccines require a significant proportion of the population to be vaccinated to be fully effective — this is called herd immunity. When enough people are protected, it becomes difficult for the disease to spread.`
  },
  {
    id: 116, title: "Board Games Are Back", topic: "games and hobbies", level: "A2", wordCount: 188,
    text: `In an age of smartphones, video games, and streaming services, something unexpected is happening: board games are more popular than ever. Sales of board games have been growing strongly for over a decade, and the variety available has expanded enormously.

The traditional games that most people grew up with — chess, draughts, Scrabble, and Monopoly — are still popular. But thousands of new games have been designed and published in recent years, covering every imaginable theme and level of complexity. Some games last fifteen minutes; others can take an entire day.

So why are people turning to board games in the digital age? Many players say they value the face-to-face interaction that board games require. Unlike video games, which are often played alone or through a screen, board games bring people together physically around a table. The experience of looking at the faces of the people you are playing with is something that screen-based games cannot replicate.

Parents also appreciate board games as a way to spend quality time with their children away from screens. Research suggests that playing games as a family helps to develop communication, strategic thinking, and the ability to manage both victory and defeat gracefully.

Board game cafés, where customers pay to play from a large collection while enjoying food and drinks, have opened in many cities. For Grace, who visits one with her friends every month, it is simply the best social activity she knows.`
  },
  {
    id: 117, title: "A Short History of Football", topic: "sports", level: "A2", wordCount: 190,
    text: `Football — known as soccer in some countries — is the most popular sport in the world. Approximately four billion people consider themselves fans of the game, and it is played professionally in almost every country on Earth.

The origins of modern football can be traced to England in the nineteenth century. At the time, various versions of football were played in schools with different and sometimes conflicting rules. In 1863, a group of clubs met in London and agreed on a standard set of rules. This was the founding of the Football Association, the world's oldest football organization.

The game spread rapidly through British influence. British sailors, traders, and workers took the game with them as they travelled. By the early twentieth century, football was being played throughout South America, Europe, and Africa.

The first FIFA World Cup was held in Uruguay in 1930 and was won by the host nation. Today, the World Cup, held every four years, is the most watched sporting event in the world.

Football has also reflected the social and political history of its times. Clubs often reflect the communities that created them — working class neighborhoods, immigrant populations, religious groups. Some have become symbols of regional or national identity far beyond sport.

Carlos says that for many people in his country, football is not just a game. It is a language shared by everyone, regardless of age, class, or background.`
  },
  {
    id: 118, title: "Religion and Daily Life", topic: "religion and culture", level: "A2", wordCount: 188,
    text: `Religion is one of the most significant forces shaping human culture, history, and daily life. Around the world, the majority of people identify with a religious tradition, and even in increasingly secular societies, religious ideas, values, and practices continue to influence art, law, food, festivals, and social norms.

For many people, religion is a central part of daily routine. A devout Muslim may pray five times a day. An observant Jewish person may follow specific dietary laws, avoiding certain foods or keeping meat and dairy separate. A practicing Hindu may begin the day with a ritual at a home shrine.

Religion provides frameworks for understanding life's big questions — why we exist, what happens after death, how we should treat other people. It also provides community. Religious congregations bring people together regularly, creating social bonds and support networks that can be especially important at difficult times such as illness, loss, or economic hardship.

At the same time, religion is a personal and often complex matter. People within the same tradition can have very different beliefs and practices. Some people follow the formal requirements of a religion closely; others identify culturally with a religion without following its rules strictly.

Understanding religion — even if you do not personally follow one — is essential for understanding human history, culture, and the motivations of billions of people around the world.`
  },
  {
    id: 119, title: "The Psychology of Fear", topic: "psychology", level: "A2", wordCount: 193,
    text: `Fear is one of the most basic human emotions. It evolved to protect us from danger. When we sense a threat, the brain triggers a physical response: the heart beats faster, the muscles tense, and the senses become sharper. This is sometimes called the "fight or flight" response, because it prepares the body to either confront the danger or escape from it.

In everyday modern life, most of us rarely face the kinds of physical dangers — predators, starvation, extreme weather — that our ancestors encountered. But fear has not disappeared. Instead, it has been redirected toward modern sources of anxiety: social rejection, failure, illness, financial insecurity, and an uncertain future.

Phobias are intense, irrational fears of specific things or situations. Common phobias include fear of spiders, heights, enclosed spaces, and public speaking. A phobia is different from ordinary caution because it is disproportionate to the actual risk involved and can significantly limit a person's daily life.

Most phobias can be effectively treated with a type of therapy called cognitive behavioral therapy, which helps the person gradually confront the source of their fear in a safe and controlled way. Over time, the fear response becomes less intense.

What is important to understand is that fear itself is not the enemy. It is a normal and necessary emotion. The goal is not to eliminate it, but to ensure it does not prevent us from living fully.`
  },
  {
    id: 120, title: "The Art of Conversation", topic: "language and communication", level: "A2", wordCount: 186,
    text: `Having a good conversation sounds simple, but it is actually a complex skill that many people find difficult. The ability to communicate well is one of the most valued qualities in both professional and personal life, yet few of us are ever formally taught how to do it.

One of the most important elements of good conversation is listening. Many people think of conversation primarily as speaking, but listening is equally important. Genuinely paying attention to what the other person is saying — rather than simply waiting for your turn to speak — makes the other person feel respected and valued. It also means you can respond meaningfully to what they have actually said.

Asking good questions is another key skill. Open questions — those that cannot be answered with a simple "yes" or "no" — invite the other person to share more and show that you are genuinely interested. "What was that like for you?" is a better question than "Was it good?"

Body language also plays an important role. Maintaining comfortable eye contact, nodding occasionally, and turning your body toward the speaker all communicate that you are engaged.

Good conversation also requires a willingness to be vulnerable — to share your own thoughts, feelings, and uncertainties, rather than only presenting your most polished, certain self.

These skills can be learned and improved with practice. The best conversationalists are usually not the most brilliant talkers, but the most attentive listeners.`
  },
];

function getTopics() { return [...new Set(texts.map(t => t.topic))]; }
function getByTopic(topic) { const q = topic.toLowerCase(); return texts.filter(t => t.topic.toLowerCase().includes(q)); }
function getRandom() { return texts[Math.floor(Math.random() * texts.length)]; }

export { texts, getTopics, getByTopic, getRandom };
export default texts;
if (typeof window !== 'undefined') window.A2TextsNew = { texts, getTopics, getByTopic, getRandom };
