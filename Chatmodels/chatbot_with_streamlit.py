import streamlit as st
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="AI Teacher",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Teacher")
st.caption("Ask me anything — I'll explain it like you're a kid.")

# -----------------------------
# Create model
# -----------------------------
model = ChatMistralAI(
    model="ministral-3b-2512"
)

# -----------------------------
# Store conversation history
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(
            content="You are a like a teacher who explain thing like explaining to a kid."
        )
    ]

# -----------------------------
# Display previous messages
# -----------------------------
for msg in st.session_state.messages:

    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# -----------------------------
# User input
# -----------------------------
prompt = st.chat_input("Ask me something...")

if prompt:

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Add user message to history
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # Get response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = model.invoke(
                st.session_state.messages
            )

            st.write(response.content)

    # Add AI response to history
    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

# -----------------------------
# Clear chat button
# -----------------------------
if st.sidebar.button("🗑️ Clear Chat"):

    st.session_state.messages = [
        SystemMessage(
            content="You are a like a teacher who explain thing like explaining to a kid."
        )
    ]

    st.rerun()
