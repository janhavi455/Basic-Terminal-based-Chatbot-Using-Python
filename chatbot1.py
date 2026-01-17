#create main funct
def main():
    print("Chatbot has started, enter 'bye' to exit.")
    while True:
        user_ip= input("User: ")
        if user_ip.lower().strip()=="bye":
            print("Bot: GoodBye")
            break
        print(f"Bot: user said '{user_ip}'")


if __name__== "__main__":
    main()