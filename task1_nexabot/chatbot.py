"""
NexaBot - Rule-Based AI Chatbot

A simple rule-based chatbot built with Python.
It uses input sanitization, a dictionary-based knowledge base,
if/elif control flow, a continuous loop, and fallback handling.
"""

# Knowledge base: predefined intents and responses
KNOWLEDGE_BASE = {
    "hello": "Hello! 👋 I'm NexaBot. How can I help you?",
    "hi": "Hi there! I'm NexaBot. What would you like to know?",
    "hey": "Hey! 👋 How can I help you today?",
    "how are you": "I'm doing great! Thanks for asking. 😊",
    "what is your name": "I'm NexaBot, a rule-based AI chatbot.",
    "who are you": "I'm NexaBot, a simple AI assistant built with Python rules.",
    "help": "You can ask me about my name, how I am, or simply say hello. Type 'bye' or 'quit' to exit.",
    "thanks": "You're welcome! 😊",
    "thank you": "You're welcome! 😊",
}

EXIT_COMMANDS = {"bye", "goodbye", "exit", "quit"}

def sanitize_input(user_input):
    """Normalize user input for reliable matching."""
    return " ".join(user_input.lower().strip().split())

def get_response(user_input):
    """Return a rule-based response for the given input."""
    if user_input in EXIT_COMMANDS:
        return "Goodbye! Have a great day! 👋"

    # Exact intent lookup
    if user_input in KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE[user_input]

    # A few natural variations handled with explicit rules
    if "your name" in user_input:
        return KNOWLEDGE_BASE["what is your name"]

    if user_input.startswith("how are") or "how are you" in user_input:
        return KNOWLEDGE_BASE["how are you"]

    return "I'm sorry, I don't understand that yet. Try 'help' to see what I can answer."

def run_chatbot():
    """Run NexaBot in a continuous conversation loop."""
    print("=" * 52)
    print("              🤖 Welcome to NexaBot")
    print("          Rule-Based AI Chatbot")
    print("=" * 52)
    print("Type 'help' for options or 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        message = sanitize_input(user_input)

        if message in EXIT_COMMANDS:
            print("NexaBot:", get_response(message))
            break

        print("NexaBot:", get_response(message))

if __name__ == "__main__":
    run_chatbot()
