# Basic Chatbot

def chatbot():
    print("Chatbot: Hello! Welcome to my chatbot.")
    print("Chatbot: You can type hello, how are you, or bye.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

# Calling the function
chatbot()
