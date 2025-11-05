

# --- Step 1: Define chatbot function ---
def chatbot():
    print("🤖 Chatbot: Hello! I'm your friendly assistant.")
    print("Type 'bye' anytime to exit.\n")

    # --- Step 2: Start chat loop ---
    while True:
        user_input = input("You: ").lower().strip()

        # --- Step 3: Match user input with predefined responses ---
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

# --- Step 4: Run chatbot ---
chatbot()

# --- Step 5: End of program ---
print("\n✨ Program finished successfully!")

