from intents import INTENTS
from db import doctor_slots
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
        elif intent== "book_appointment":
            print("Can you please tell me which doctor would you like to see and when? in the format '[name] [DD/MM/YYYY]'.")
            doc_name,doc_date = input("User: ").split()
            doctor_slots[doc_name]= doc_date
            print(f"Your booking with {doc_name} on {doctor_slots[doc_name]} is succesfully completed!")
        else:
            pass
    print("Bot: Do you want to see the your schedule?")
    que= input("User: ")
    if que.lower()=="yes":
        print(doctor_slots)
    



if __name__=="__main__":
    main()

    
    
    
    



