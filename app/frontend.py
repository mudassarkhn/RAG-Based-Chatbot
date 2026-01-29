import streamlit as st
from chain import chain,memory



# Page config
st.set_page_config(
    page_title="Ninesol ChatBot ",
    page_icon="🧑‍💼 ChatBot",
    layout="centered",
  
)
#fixed title
st.title("Ninesol ChatBot 🧑‍💼" )
st.caption("Ask questions about Ninesol technologies")

# st.sidebar.header("About")
# st.sidebar.info("""AI-powered HR bot That's asnwers to attendance, trends, and employee performance questions.""")

# reset button
if st.button("Reset Chat"):
    st.session_state.messages = []  

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask a question about attendance...")

if user_input:
    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call the agent
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            try:
                response = chain.invoke(user_input)
                memory.chat_memory.add_user_message(user_input)
                memory.chat_memory.add_ai_message(response)

                # Agent output handling - AgentExecutor returns {"output": "..."}
                if isinstance(response, dict) and "output" in response:
                    answer = response["output"]
                    if not answer or answer == "":
                        answer = "No response generated."
                else:
                    answer = str(response.content)if response else "No response generated."

            except Exception as e:
                answer = f"Error: {str(e)}"

        st.markdown(answer)

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
