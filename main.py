import json

# Load knowledge base
with open("rag_data.json") as f:
    data = json.load(f)

def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")

def detect_intent(user_input):
    user_input = user_input.lower()
    if "hi" in user_input or "hello" in user_input:
        return "greeting"
    elif "price" in user_input or "plan" in user_input:
        return "inquiry"
    elif "buy" in user_input or "want" in user_input:
        return "high_intent"
    return "unknown"

def chatbot():
    print("Bot: Hello! How can I help you?")
    
    lead_data = {}

    while True:
        user = input("You: ")
        intent = detect_intent(user)

        if intent == "greeting":
            print("Bot: Hi! Ask me about our plans.")

        elif intent == "inquiry":
            print("Bot: We have:")
            print("Basic:", data["plans"]["basic"])
            print("Pro:", data["plans"]["pro"])

        elif intent == "high_intent":
            print("Bot: Great! Let's get your details.")
            
            lead_data["name"] = input("Enter your name: ")
            lead_data["email"] = input("Enter your email: ")
            lead_data["platform"] = input("Enter your platform: ")

            mock_lead_capture(
                lead_data["name"],
                lead_data["email"],
                lead_data["platform"]
            )
            break

        else:
            print("Bot: Sorry, I didn’t understand.")

chatbot()
