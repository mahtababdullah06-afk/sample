import random
import datetime

print("🤖 Smart Python Chatbot")
print("Type 'bye' to exit.\n")

user_name = ""

responses = {
"greetings":[
"Hello!", "Hi there!", "Hey!", "Nice to see you!", "Greetings!",
"Hey friend!", "Hi! How can I help?", "Hello there!", "Hey! What's up?", "Hi human!"
],

"how_are_you":[
"I'm doing great!", "All good here!", "I'm fine, thanks!",
"I'm feeling digital today!", "Everything is running smoothly!",
"I'm ready to chat!", "Feeling smart today!", "I'm good, how about you?",
"Doing awesome!", "All systems working!"
],

"about_you":[
"I'm a Python chatbot.", "I'm a program created in Python.",
"I love talking with people!", "I'm here to chat with you.",
"I'm a learning chatbot.", "I'm still learning new things!",
"I'm powered by Python.", "I exist inside your computer!",
"I like answering questions.", "Chatting is my favorite job!"
],

"jokes":[
"Why do programmers prefer dark mode? Because light attracts bugs.",
"I told my computer a joke… it didn't laugh.",
"Why do Python programmers wear glasses? Because they can't C.",
"What’s a computer’s favorite snack? Microchips!",
"I would tell you a UDP joke, but you might not get it.",
"Debugging: removing the needles from the haystack.",
"Why was the computer cold? It forgot to close Windows.",
"Programmers don't die, they just stop responding.",
"Why did the developer go broke? Because he used up all his cache.",
"Why was the JavaScript developer sad? Because he didn't Node how to Express himself."
],

"learning":[
"Learning is awesome!", "Knowledge makes you powerful.",
"Studying every day improves your brain.",
"Python is a great language to learn.",
"Practice coding often!",
"Learning programming opens many opportunities.",
"Curiosity is the key to learning.",
"Never stop learning new things.",
"Every expert was once a beginner.",
"Keep practicing and you will improve!"
],

"fallback":[
"Interesting!", "Tell me more.", "That's cool.",
"I'm not sure I understand.", "Can you explain that?",
"That sounds interesting.", "Hmm okay.", "Really?",
"I see.", "Let's talk more!"
]
}

while True:
    user_input = input("You: ").lower()

    if "bye" in user_input:
        print("Bot: Goodbye! 👋")
        break

    elif any(word in user_input for word in ["hello","hi","hey"]):
        print("Bot:", random.choice(responses["greetings"]))

    elif "how are you" in user_input:
        print("Bot:", random.choice(responses["how_are_you"]))

    elif "your name" in user_input:
        print("Bot: I'm SmartPyBot 🤖")

    elif "my name is" in user_input:
        user_name = user_input.replace("my name is","").strip()
        print("Bot: Nice to meet you", user_name + "!")

    elif "my name" in user_input and user_name != "":
        print("Bot: Your name is", user_name)

    elif "time" in user_input:
        now = datetime.datetime.now()
        print("Bot: Current time is", now.strftime("%H:%M:%S"))

    elif "date" in user_input:
        today = datetime.date.today()
        print("Bot: Today's date is", today)

    elif "joke" in user_input:
        print("Bot:", random.choice(responses["jokes"]))

    elif any(word in user_input for word in ["learn","study","school","python"]):
        print("Bot:", random.choice(responses["learning"]))

    elif any(word in user_input for word in ["who are you","what are you"]):
        print("Bot:", random.choice(responses["about_you"]))

    else:
        print("Bot:", random.choice(responses["fallback"]))