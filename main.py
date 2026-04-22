import json

# Load knowledge base (RAG)
with open("rag_data.json", "r") as file:
    data = json.load(file)

# Mock Lead Capture Function
def mock_lead_capture(name, email, platform):

    print("\n===== LEAD CAPTURED SUCCESSFULLY =====")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Platform: {platform}")
    print("======================================")

# Intent Detection Function
def detect_intent(user_input):

    user_input = user_input.lower()

    greetings = [
        "hi",
        "hello",
        "hey"
    ]

    inquiry = [
        "price",
        "pricing",
        "plan",
        "plans",
        "feature",
        "features",
        "refund",
        "support"
    ]

    high_intent = [
        "buy",
        "purchase",
        "subscribe",
        "sign up",
        "i want",
        "want pro",
        "interested"
    ]

    # Greeting Intent
    if any(word in user_input for word in greetings):
        return "greeting"

    # High Intent FIRST
    elif any(word in user_input for word in high_intent):
        return "high_intent"

    # Inquiry Intent
    elif any(word in user_input for word in inquiry):
        return "inquiry"

    # Unknown Intent
    else:
        return "unknown"

# RAG-Based Answer Function
def answer_query():

    print("\n===== AUTOSTREAM PLANS =====\n")

    print("Basic Plan:")
    print(data["plans"]["basic"])

    print("\nPro Plan:")
    print(data["plans"]["pro"])

    print("\n===== COMPANY POLICIES =====")

    print("Refund Policy:")
    print(data["policies"]["refund"])

    print("\nSupport Policy:")
    print(data["policies"]["support"])

    print()

# Main Chatbot Function
def chatbot():

    print("===================================")
    print("      AutoStream AI Assistant")
    print("===================================")

    print("Bot: Hello! Welcome to AutoStream.")
    print("Bot: Ask me about pricing, plans, or features.\n")

    while True:

        user_input = input("You: ")

        intent = detect_intent(user_input)

        # Greeting
        if intent == "greeting":

            print("\nBot: Hi! How can I help you today?\n")

        # High Intent
        elif intent == "high_intent":

            print("\nBot: Great! You seem interested in our Pro Plan.")
            print("Bot: Please provide your details.\n")

            name = input("Enter your name: ")
            email = input("Enter your email: ")
            platform = input("Enter your creator platform: ")

            # Tool Execution
            mock_lead_capture(name, email, platform)

            print("\nBot: Thank you!")
            print("Bot: Our team will contact you soon.\n")

            break

        # Inquiry
        elif intent == "inquiry":

            answer_query()

        # Unknown Query
        else:

            print("\nBot: Sorry, I didn't understand that.")
            print("Bot: Please ask about pricing or plans.\n")

# Run Chatbot
chatbot()
