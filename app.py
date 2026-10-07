import streamlit as st
from datetime import datetime
import random

# Page configuration
st.set_page_config(
    page_title="Python Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 Python Chatbot")
st.write("Welcome! I'm a simple chatbot built with Python and Streamlit.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chatbot response function
def get_response(user_input):
    message = user_input.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return random.choice([
            "Hello! 👋",
            "Hi! How can I help you?",
            "Hey! Nice to meet you!"
        ])

    elif "how are you" in message:
        return random.choice([
            "I'm doing great! 😊",
            "I'm fine, thanks for asking!",
            "I'm ready to chat with you!"
        ])

    elif "your name" in message or "who are you" in message:
        return "I'm PyBot, a chatbot created using Python and Streamlit. 🤖"

    elif "time" in message:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "date" in message:
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {current_date}."

    elif "python" in message:
        return "Python is a popular programming language known for its simplicity and versatility. 🐍"

    elif "streamlit" in message:
        return "Streamlit is a Python framework used to quickly build interactive web applications."

    elif message in ["bye", "goodbye"]:
        return "Goodbye! Have a great day! 👋"

    elif "thank" in message:
        return "You're welcome! 😊"

    else:
        return "I'm still learning. Could you ask me something else?"


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Generate response
    response = get_response(user_input)

    # Display chatbot response
    with st.chat_message("assistant"):
        st.write(response)

    # Save chatbot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })


# Sidebar
with st.sidebar:
    st.header("⚙️ Options")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.write("### About")
    st.write(
        "This chatbot is built using Python and Streamlit."
    )
