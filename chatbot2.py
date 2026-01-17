from intents import INTENTS
def preprocess(text):
    return text.lower().strip()
def detect_intent(text):
    for intent,data in INTENTS.items():
        for keyword in data["keywords"]:
            if keyword in text:
                return intent
    return "unknown"
def respond(intent):
    print("Bot: ", INTENTS[intent]["response"])
    
def main():
    print("Chatbot has started!")
    while True:
        user_ip= input("User: ")
        user_ip= preprocess(user_ip)
        intent= detect_intent(user_ip)
        respond(intent)
        if intent=="exit":
            break
if __name__=="__main__":
    main()

    
    
    
    



