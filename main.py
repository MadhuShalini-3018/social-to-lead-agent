import json

# Load knowledge base
with open("rag_data.json", "r") as file:
    data = json.load(file)

# Mock Lead Capture
def mock_lead_capture(name, email, platform):

    print("\n===== LEAD CAPTURED SUCCESSFULLY =====")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Platform: {platform}")
    print("======================================")

# Intent Detection
def detect_intent(user_input):

    user_input = user_input.lower()

    # HIGH INTENT FIRST
    if (
        "i want" in user_input
        or "buy" in user_input
        or "subscribe" in user_input
        or "want pro" in user_input
        or "purchase" in user_input
    ):
        return "high_intent"

    # Greeting
    elif (
        "hi" in user_input
        or "hello" in user_input
        or "hey" in user_input
    ):
        return "greeting"

    # Inquiry
    elif (
        "price" in user_input
        or "pricing" in user_input
        or "plan" in user_input
        or "plans" in user_input
        or "feature" in user_input
        or "support" in user_input
        or "refund" in user_input
    ):
        return "inquiry"

    else:
        return "unknown"

# RAG Answer
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

# Main Chatbot
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

        # HIGH INTENT
        elif intent == "high_intent":

            print("\nBot: Great! You seem interested in our Pro Plan.")
            print("Bot: Please provide your details.\n")

            name = input("Enter your name: ")
            email = input("Enter your email: ")
            platform = input("Enter your creator platform: ")

            mock_lead_capture(name, email, platform)

            print("\nBot: Thank you!")
            print("Bot: Our team will contact you soon.\n")

            break

        # Inquiry
        elif intent == "inquiry":

            answer_query()

        # Unknown
        else:

            print("\nBot: Sorry, I didn't understand that.")
            print("Bot: Please ask about pricing or plans.\n")

# Run chatbot
chatbot()
