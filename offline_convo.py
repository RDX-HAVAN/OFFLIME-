# Import necessary module
import time

# Logo (ASCII Art)
logo = """
████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║██║ ██╔╝
   ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║█████╔╝ 
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║██╔═██╗ 
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║  ██╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
"""

# Display Logo
print(logo)
print("Welcome to the Offline Termux Chatbot!")
print("Type 'exit' to end the conversation.\n")

# Predefined responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a script, but thank you for asking! How can I help?",
    "your name": "I’m an Offline Termux Chatbot.",
    "bye": "Goodbye! Have a great day!"
}

# Conversation loop
while True:
    # Take user input
    user_input = input("You: ").strip().lower()
    
    # Check if user wants to exit
    if user_input == "exit":
        print("Chatbot: Goodbye! Take care.")
        break
    
    # Respond based on predefined responses
    response = responses.get(user_input, "Sorry, I didn't understand that.")
    print("Chatbot:", response)
    
    # Small delay for readability
    time.sleep(1)
