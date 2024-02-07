import random

def greeting():
    responses = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
    return random.choice(responses)

def farewell():
    responses = ["Goodbye!", "See you later!", "Bye for now!", "Farewell!"]
    return random.choice(responses)

def respond(message):
    if "hello" in message.lower() or "hi" in message.lower() or "hey" in message.lower():
        return greeting()
    elif "bye" in message.lower() or "goodbye" in message.lower():
        return farewell()
    else:
        return "I'm sorry, I didn't understand that."

def chat():
    print("Hello! I'm a simple chatbot. You can start talking to me. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print(f"You: {farewell()}")
            break
        else:
            print(f"You: {respond(user_input)}")