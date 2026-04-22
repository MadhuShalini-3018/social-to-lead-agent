import json

# Load RAG knowledge base
with open("rag_data.json", "r") as f:
    data = json.load(f)

# Mock lead capture tool
def mock_lead_capture(name, email, platform):
    print("\nLead captured successfully!")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Platform: {platform}")

# Intent detection
def detect_intent(user_input):
    user_input = user_input.lower()

    greetings = ["hi", "hello", "hey"]
    inquiry = ["price", "pricing", "plan", "feature", "features"]
    high_intent = ["buy", "purchase", "subscribe", "sign up", "want pro", "i want"]

    if any(word in user_input for word in greetings):
        return "greeting"

    elif any(word in user_input for word in inquiry):
        return "inquiry"

    elif any(word in user_input for word in high_intent):
        return "high_intent"

    else:
        return "unknown"

# RAG response
def answer_query():
    print("\nBot: Here are our plans:\n")

    print("Basic Plan:")
    print(data["plans"]["basic"])

    print("\nPro Plan:")
    print(data["plans"]["pro"])

    print("\nPolicies:")
    print("- Refund:", data["policies"]["refund"])
    print("- Support:", data["policies"]["support"])

# Chatbot
def chatbot():

    print("===== AutoStream AI Assistant =====")
    print("Bot: Hello! Welcome to AutoStream.")
    print("Bot: Ask me about pricing or plans.\n")

    while True:

        user = input("You: ")

        intent = detect_intent(user)

        # Greeting
        if intent == "greeting":
            print("Bot: Hi! How can I help you today?\n")

        # Pricing / product inquiry
        elif intent == "inquiry":
            answer_query()
            print()

        # High intent detection
        elif intent == "high_intent":

            print("\nBot: Awesome! You seem interested in our Pro Plan.")
            print("Bot: Please provide your details.\n")

            name = input("Enter your name: ")
            email = input("Enter your email: ")
            platform = input("Enter your creator platform: ")

            # Tool execution
            mock_lead_capture(name, email, platform)

            print("\nBot: Thank you! Our team will contact you soon.")
            break

        # Unknown input
        else:
            print("Bot: Sorry, I didn't understand that.")
            print("Bot: Please ask about pricing or plans.\n")

# Run chatbot
chatbot()
