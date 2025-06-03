import time

def bot_chat(Respond):
    match Respond:
        case "Hello" | "Hi" | "Hi there" | "Hello chatbot":
            return "Hello there, please state your concern"
        
        case "Are you a real Human?" | "How old are you?" | "Do you have parents?":
            return "Sorry but I am just a AI tool to assist on any inquiry you need"
        case _:
            return "Sorry, I am not familiar with what you just said"



print("----------------------------")
print("    PYTHON AI CHATBOT")
print("----------------------------")

time.sleep(1)
print("How may I help you for today")

while True:
    Respond = input("Chat:")
    time.sleep(1)
    print(bot_chat(Respond))

