/**
 * texts-a1-new.js
 * Additional A1 reading texts — IDs 81–100
 * ~100–150 words each. New topics expand the original set.
 * Merge with texts-a1.js for the full A1 library.
 *
 * window.A1TextsNew / ES export: { texts, getTopics, getByTopic, getRandom }
 */

const texts = [
  {
    id: 81, title: "My Family", topic: "family and relationships", level: "A1", wordCount: 112,
    text: `My name is Sofia. I have a small family. There are four people in my family: my mother, my father, my brother, and me.

My mother's name is Clara. She is a nurse. She works at the hospital. My father's name is Paul. He is a teacher. He teaches mathematics at a school.

My brother is twelve years old. His name is Ben. He likes video games and football. I am fifteen years old. I like reading and drawing.

We live in a small house near the park. We have a garden with flowers and a vegetable patch.

On weekends, we often eat dinner together and watch a film. I love my family very much. We are happy together.`
  },
  {
    id: 82, title: "My Bedroom", topic: "housing and home", level: "A1", wordCount: 108,
    text: `My bedroom is my favorite room in the house. It is not very big, but it is very comfortable.

I have a bed near the window. There is a blue blanket on my bed. I also have a desk where I do my homework. My computer is on the desk.

On the wall, I have posters of my favorite music artists. I have a bookshelf with many books and comics. There is a small lamp on the shelf.

The floor has a soft carpet. The walls are light yellow. My bedroom is always a little messy, but I know where everything is.

I like to read in bed before I sleep. My bedroom is my special place.`
  },
  {
    id: 83, title: "My Clothes", topic: "clothing and fashion", level: "A1", wordCount: 110,
    text: `I do not have many clothes, but I like the clothes I have. I usually wear simple and comfortable things.

For school, I wear jeans and a T-shirt. I have five T-shirts in different colors: white, blue, grey, red, and black. I also have two pairs of jeans.

In winter, I wear a warm jacket and a scarf. My jacket is dark green. I love it because it is very warm.

On special occasions, I wear smarter clothes. I have a white shirt and dark trousers.

I wear trainers every day. They are comfortable and I can walk a lot in them. My favorite color for clothes is blue. Simple and clean is my style.`
  },
  {
    id: 84, title: "Drawing and Painting", topic: "art and creativity", level: "A1", wordCount: 113,
    text: `I love to draw and paint. It is my favorite hobby. I do it every weekend.

I have many colored pencils, pens, and paints. I keep them in a big box under my desk. I draw animals, people, and nature. My favorite thing to draw is birds.

I also like to paint with watercolors. I paint flowers and landscapes. My paintings are not perfect, but I enjoy making them.

I have a sketchbook where I draw every week. I also have some paintings on my bedroom wall.

My art teacher says I have a good eye for color. She encourages me to draw more. I would like to take art classes one day. Drawing makes me feel calm and happy.`
  },
  {
    id: 85, title: "Playing Video Games", topic: "games and hobbies", level: "A1", wordCount: 115,
    text: `My name is Alex. I like playing video games. I usually play for one hour after school.

I have a games console in my room. I play adventure games and racing games. My favorite game is a racing game. I play it with my brother online. It is very exciting.

I also play games on my phone. I play simple puzzle games when I am on the bus.

My parents say I should not play too many hours. They want me to do sport and read books too. I think they are right. I try to do other activities as well.

Playing video games is fun, but it is important to have balance. I also go to football practice on Tuesdays and Thursdays.`
  },
  {
    id: 86, title: "The Farmer's Market", topic: "agriculture and farming", level: "A1", wordCount: 109,
    text: `Every Saturday morning, there is a farmers' market in my town. I love going there with my mother.

The market has many stalls. Farmers sell vegetables, fruit, eggs, honey, and bread. The food is fresh and local. It comes from farms near our town.

My favorite stall sells tomatoes, peppers, and cucumbers. The tomatoes are red and very tasty. I also like the honey stall. The honey is sweet and golden.

The market is very busy and noisy. People talk and children laugh. There is often music playing too.

We always buy more food than we plan. My mother says fresh food is always better than supermarket food. I agree. Everything from the market tastes delicious.`
  },
  {
    id: 87, title: "A Visit to the Doctor", topic: "medicine and body", level: "A1", wordCount: 114,
    text: `Last week, I was not feeling well. I had a sore throat and a temperature. My mother took me to the doctor.

The doctor's name was Dr. Santos. She was very kind. She looked at my throat and listened to my heart. She asked me how long I was sick.

She told me I had a small infection. She gave me some medicine. She also told me to drink a lot of water and rest at home for three days.

I stayed in bed and watched television. My mother made me soup. After two days, I started to feel better.

On the fourth day, I went back to school. I felt much better. I was happy to see my friends again. I always feel safe when I visit Dr. Santos.`
  },
  {
    id: 88, title: "My Town", topic: "city life", level: "A1", wordCount: 116,
    text: `I live in a small town. It is not very big, but I like it a lot.

In the center of the town, there is a main square. There are shops, a café, and a small supermarket. There is also an old church. On Sundays, many people go to the church.

Near the square, there is a park with a fountain. Children play there in the afternoon. I often sit on a bench and read a book.

My town has a library, a post office, and a small hospital. There is a bus station too. The buses go to the big city every hour.

My favorite place is the café near the square. They make the best chocolate cake. I go there on Saturday mornings with my friends.`
  },
  {
    id: 89, title: "Learning to Cook", topic: "food", level: "A1", wordCount: 111,
    text: `My grandmother is teaching me to cook. We cook together every Sunday. It is a lot of fun.

Last Sunday, she taught me how to make rice with vegetables. First, we cut the vegetables: carrots, onions, and peppers. Then, we cooked the rice. We added the vegetables and some olive oil. It was delicious.

My grandmother knows many recipes. She learned them from her mother. She always cooks with love and patience.

I am not a good cook yet, but I am learning. I can now make an omelet, pasta, and rice dishes. I write the recipes in a notebook.

One day, I want to cook a big family dinner. I want to make my grandmother proud. Cooking is a skill for life.`
  },
  {
    id: 90, title: "My Favorite Sport: Swimming", topic: "sports", level: "A1", wordCount: 113,
    text: `My name is Laura. My favorite sport is swimming. I swim every Tuesday and Thursday at the local swimming pool.

I started swimming when I was five years old. My father taught me. Now I am a good swimmer. I can swim four different strokes: freestyle, backstroke, breaststroke, and butterfly.

The pool is five minutes from my home. I go with my friend Ana. We race each other in the pool. It is very fun.

Swimming is very good for your body. It makes your arms, legs, and back strong. It is also good for breathing.

After swimming, I always feel great. I sleep very well on Tuesday and Thursday nights.

My goal is to join the school swimming team this year. I practice very hard.`
  },
  {
    id: 91, title: "An Email to a Friend", topic: "language and communication", level: "A1", wordCount: 108,
    text: `Hi Maria,

How are you? I hope you are well. I am writing to tell you about my week.

On Monday, I started a new English class. There are eight students in the class. My teacher is very nice. Her name is Miss Lee. We practice speaking and listening every lesson.

On Wednesday, I went to the cinema with my brother. We watched a comedy film. It was very funny.

On Friday, I cooked dinner for my family. I made pasta with tomato sauce. Everyone liked it.

This weekend, I am going to visit my grandparents. They live in a village near the mountains.

Please write back soon! Tell me about your week too.

Your friend,
Sofia`
  },
  {
    id: 92, title: "A Trip to the Museum", topic: "art and creativity", level: "A1", wordCount: 115,
    text: `Last month, my school class visited the city museum. It was a great day.

The museum is a big old building in the city center. Inside, there are many rooms with different things to see. We saw paintings, old furniture, and objects from history.

My favorite room was the room about ancient history. There were old coins, clay pots, and stone tools. The teacher explained how people lived long ago. It was very interesting.

We also saw a room with modern art. Some paintings were very colorful. Some were abstract and I did not understand them. But I liked the bright colors.

We ate lunch in the museum café. The teacher bought everyone a cold drink.

I would like to go back to the museum with my family. There is so much to learn there.`
  },
  {
    id: 93, title: "My Grandfather's Garden", topic: "agriculture and farming", level: "A1", wordCount: 112,
    text: `My grandfather has a big garden. He grows vegetables and fruit. He spends many hours there every week.

In the garden, there are tomatoes, beans, lettuce, and cucumbers. There are also apple trees and a pear tree. In summer, the garden is full of color.

My grandfather does not use any chemicals on his plants. He uses water and natural compost. He says this makes the food healthier and tastier.

Every summer, I help him in the garden. I water the plants and pick the fruit. It is hard work but very satisfying.

He gives bags of vegetables to the neighbors. Everyone in the street loves his tomatoes.

My grandfather says that a garden teaches you to be patient. You plant, you wait, and you watch things grow. I think he is right.`
  },
  {
    id: 94, title: "A Simple Science Experiment", topic: "science and discovery", level: "A1", wordCount: 111,
    text: `At school, we did a science experiment with plants. We wanted to find out if plants need light to grow.

Our teacher gave each group two small pots with soil. We planted seeds in both pots. One pot went on the windowsill in the sun. The other pot went in a dark cupboard.

We watered both pots every day. After two weeks, we checked the plants. The plant in the sun was tall and green. The plant in the dark was small, yellow, and weak.

We learned that plants need light to make food. This process is called photosynthesis.

I found this experiment very interesting. I like science because we learn by doing. Our teacher says that asking questions is the first step in science.`
  },
  {
    id: 95, title: "Celebrations at Home", topic: "holidays and celebrations", level: "A1", wordCount: 110,
    text: `In my family, we celebrate many special days. My favorite celebration is my mother's birthday.

Every year, we make a surprise party for her. My father bakes a cake. My brother and I decorate the house with balloons and flowers. We hide in the living room and wait for her to come home.

When she comes in, we shout "Surprise!" She always laughs and looks very happy.

We eat dinner together and sing happy birthday. After the cake, we give her presents. This year, I gave her a drawing I made.

She said it was the best present of all. That made me very happy.

Seeing my mother smile is the best part of any celebration. We do not need a lot of money to have a happy time together.`
  },
  {
    id: 96, title: "My Neighbor", topic: "family and relationships", level: "A1", wordCount: 109,
    text: `My neighbor's name is Mr. Costa. He is an old man. He lives alone next door to us.

Mr. Costa is very friendly. He always says hello when I leave for school. Sometimes he gives us vegetables from his garden.

He has a small dog called Pipo. I sometimes take Pipo for a walk when Mr. Costa is not feeling well. Pipo is brown and white. He is very energetic and loves to run.

My mother often makes extra food for Mr. Costa. She says it is important to look after people who live alone. Mr. Costa always says thank you and looks very happy.

I think good neighbors are like a second family. We are lucky to have Mr. Costa next door.`
  },
  {
    id: 97, title: "Reading Books", topic: "games and hobbies", level: "A1", wordCount: 107,
    text: `I love reading books. I read every day before I go to sleep. I have about fifty books on my shelf.

My favorite books are adventure stories. I like stories about people who travel to new places and solve problems. My favorite book is about a girl who explores a mysterious island.

I get books from the school library. Every two weeks, I borrow two or three books. The librarian knows my name and often recommends books to me.

My parents also give me books as presents. For my last birthday, I got three new books.

Reading is good for learning new words and ideas. My English teacher says that people who read a lot write better too.

I think a good book is like a friend. It is always there for you.`
  },
  {
    id: 98, title: "A Cold Winter Day", topic: "weather", level: "A1", wordCount: 108,
    text: `Today is a very cold winter day. The temperature outside is below zero. There is ice on the ground and frost on the windows.

I put on my warmest clothes: thick socks, a heavy jumper, and my long coat. I also wore gloves and a hat.

On the way to school, I walked carefully because the pavement was slippery. The sky was grey and there were no clouds, just cold blue air.

At school, the heating was on and it was warm inside. We drank hot chocolate at break time.

After school, I came home quickly. My mother made hot soup. We sat by the window and watched the ice outside.

I do not like the cold very much, but I love coming home to a warm house. Winter has a special feeling.`
  },
  {
    id: 99, title: "A Story About Honesty", topic: "family and relationships", level: "A1", wordCount: 113,
    text: `One day at school, I broke a window. I was playing with a ball in the classroom. The ball hit the window and it cracked. I was very scared.

My first thought was to say nothing. But then I thought about what my parents always tell me: be honest.

I went to the teacher and told her what happened. I said I was sorry. The teacher looked serious, but she was not very angry. She said she was happy that I told the truth.

She called my parents. My father said he was proud of me for being honest. He paid for the window.

I learned something important that day. It is always better to tell the truth, even when you are scared. Honesty is not easy, but it makes you feel better in the end.`
  },
  {
    id: 100, title: "At the Post Office", topic: "city life", level: "A1", wordCount: 107,
    text: `Last week, I went to the post office with my father. He needed to send a package to my aunt in another city.

The post office was not very big. There were four people waiting in the queue. We waited for about ten minutes.

When it was our turn, my father gave the package to the person behind the counter. She weighed it and told us the price. My father paid by card.

She gave us a receipt and a tracking number. My father explained that we can use the tracking number to see where the package is.

I thought it was interesting. The package would travel by van and train to reach my aunt in one day.

When my aunt received it, she called us to say thank you. It was a book I chose for her.`
  },
];

function getTopics() { return [...new Set(texts.map(t => t.topic))]; }
function getByTopic(topic) { const q = topic.toLowerCase(); return texts.filter(t => t.topic.toLowerCase().includes(q)); }
function getRandom() { return texts[Math.floor(Math.random() * texts.length)]; }

export { texts, getTopics, getByTopic, getRandom };
export default texts;
if (typeof window !== 'undefined') window.A1TextsNew = { texts, getTopics, getByTopic, getRandom };
