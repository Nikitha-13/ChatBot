import nltk
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses for the chatbot
chatbot_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I'm Nikitha's ChatBot and I'm here to assist you.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!",]
    ],
    [
        r"(.*) (good|well)",
        ["That's great to hear! How can I assist you?",]
    ],
    [
        r"bye",
        ["Goodbye! Have a great day.",]
    ],
]

# Create and train the chatbot
chatbot = Chat(chatbot_pairs, reflections)

# Start the chatbot
print("Hello! I'm your chatbot. How can I help you today? (type 'bye' to exit)")
chatbot.converse()
