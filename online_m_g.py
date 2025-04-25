import streamlit as st

# Title of the game
st.title("Online Multiplayer Game")

# Create a session state to store player names and messages
if 'players' not in st.session_state:
    st.session_state.players = []
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to add a player
def add_player(name):
    if name and name not in st.session_state.players:
        st.session_state.players.append(name)

# Input for player name
player_name = st.text_input("Enter your name:")
if st.button("Join Game"):
    add_player(player_name)

# Display current players
st.subheader("Current Players:")
st.write(st.session_state.players)

# Input for messages
message = st.text_input("Send a message:")
if st.button("Send"):
    if message:
        st.session_state.messages.append(f"{player_name}: {message}")

# Display messages
st.subheader("Messages:")
for msg in st.session_state.messages:
    st.write(msg)



