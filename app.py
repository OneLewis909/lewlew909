import streamlit as st

# Set the title of the app
st.title("Welcome to the Caribbean Disaster Preparedness Chat")

# Initialize session state for the messages if not already set
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Function to add a message to the chat log
def add_message(sender, message):
    st.session_state["messages"].append({"sender": sender, "message": message})

# Display chat messages
for chat in st.session_state["messages"]:
    with st.chat_message(chat["sender"]):
        st.write(chat["message"])

# User input for chat
user_input = st.chat_input("Type your message about natural disaster preparedness...")

# Respond to the user's input
if user_input:
    add_message("user", user_input)
    add_message("ai", "This is a response based on your input.")
