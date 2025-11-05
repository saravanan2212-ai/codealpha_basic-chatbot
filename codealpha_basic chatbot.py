

def chatbot():
    print("🤖 Chatbot: Hello! I'm your friendly assistant.")
    print("Type 'bye' anytime to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("🤖 Chatbot: Hi there! How can I help you today?")

        elif user_input in ["how are you", "how are you doing"]:
            print("🤖 Chatbot: I'm doing great, thanks for asking! 😊")

        elif user_input in ["what is your name", "who are you"]:
            print("🤖 Chatbot: I'm a simple Python chatbot created by Saravanan!")

        elif user_input in ["bye", "goodbye", "exit"]:
            print("🤖 Chatbot: Goodbye! Have a nice day! 👋")
            break

        elif user_input in ["thank you", "thanks"]:
            print("🤖 Chatbot: You're welcome! 😄")

        elif user_input in ["what can you do", "help"]:
            print("🤖 Chatbot: I can reply to simple greetings and questions.")

        elif user_input == "":
            print("🤖 Chatbot: Hmm... you didn’t type anything!")

        else:
            print("🤖 Chatbot: Sorry, I didn’t understand that. Can you try again?")

chatbot()

print("\n✨ Program finished successfully!")


