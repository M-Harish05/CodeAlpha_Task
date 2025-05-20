import re

print("ChatBot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input in ["bye", "exit", "quit"]:
        print("ChatBot: Goodbye!")
        break

    elif re.search(r'\bhi\b|\bhello\b|\bhey\b', user_input):
        print("ChatBot: Hello there!")

    elif "how are you" in user_input:
        print("ChatBot: I'm good, how about you?")

    elif "your name" in user_input:
        print("ChatBot: I'm just a chatbot.")

    elif "help" in user_input:
        print("ChatBot: I can answer simple questions. Try saying 'hi' or ask my name.")

    else:
        print("ChatBot: Interesting... Tell me more.")
