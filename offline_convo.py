# Import necessary modules
import time

# Logo (ASCII Art)
logo = """
██╗███╗   ██╗██████╗  ██████╗  ██████╗ ██╗  ██╗██╗   ██╗
██║████╗  ██║██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝╚██╗ ██╔╝
██║██╔██╗ ██║██║  ██║██║   ██║██║   ██║█████╔╝  ╚████╔╝ 
██║██║╚██╗██║██║  ██║██║   ██║██║   ██║██╔═██╗   ╚██╔╝  
██║██║ ╚████║██████╔╝╚██████╔╝╚██████╔╝██║  ██╗   ██║   
╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
"""
print(logo)
print("Welcome to the Offline Multi-Conversation Inbox!\n")

# Store conversations in a dictionary where each key is a convo ID
conversations = {}

# Predefined responses for conversation
responses = {
    "hello": "Hello! How can I assist you?",
    "how are you": "I'm here to help you in this conversation!",
    "bye": "Goodbye! Ending this conversation."
}

# Function to display current conversations
def show_inbox():
    print("\n--- Inbox ---")
    if conversations:
        for convo_id in conversations:
            print(f"Convo ID: {convo_id} - Messages: {len(conversations[convo_id])}")
    else:
        print("No active conversations.")
    print("--- End of Inbox ---\n")

# Function to handle a specific conversation
def handle_conversation(convo_id):
    if convo_id not in conversations:
        conversations[convo_id] = []
    print(f"\n--- Conversation with ID: {convo_id} ---")
    while True:
        user_input = input(f"You ({convo_id}): ").strip().lower()
        
        # Exit condition for this conversation
        if user_input == "exit":
            print(f"Exiting conversation {convo_id}.\n")
            break
        
        # Store user message
        conversations[convo_id].append(f"You: {user_input}")
        
        # Generate bot response
        response = responses.get(user_input, "I didn't understand that.")
        conversations[convo_id].append(f"Bot: {response}")
        
        # Display bot response
        print(f"Bot ({convo_id}): {response}")

# Main loop
while True:
    # Display inbox
    show_inbox()
    print("Options: \n1. Start new conversation\n2. Open existing conversation\n3. Quit")
    choice = input("Choose an option (1, 2, or 3): ").strip()
    
    if choice == "1":
        # Start a new conversation
        convo_id = input("Enter new Convo ID: ").strip()
        if convo_id in conversations:
            print("Conversation ID already exists. Try a different one.\n")
        else:
            handle_conversation(convo_id)
    
    elif choice == "2":
        # Open an existing conversation
        convo_id = input("Enter existing Convo ID: ").strip()
        if convo_id in conversations:
            handle_conversation(convo_id)
        else:
            print("Conversation ID not found.\n")
    
    elif choice == "3":
        # Exit the program
        print("Exiting the inbox. Goodbye!")
        break
    
    else:
        print("Invalid option. Please choose 1, 2, or 3.\n")
