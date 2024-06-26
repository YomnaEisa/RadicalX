import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

#project = "gemini-explorer"
project = "gemini-explorer-418219"
vertexai.init(project = project)

config = generative_models.GenerationConfig(
    temperature=0.4
)

# Load model with config
model = GenerativeModel(
    "gemini-pro",
    generation_config= config
)
chat = model.start_chat()

# Helper function to display and send streamlot messages
def llm_function(chat: ChatSession, query):
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text

    with st.chat_message("model"):
        st.markdown(output)
    
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    st.session_state.messages.append(
        {
           "role": "model",
           "content": output 
        }
    )
# end of helper function

st.title("Gemini Explorer")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display and load to chat history
for index, message in enumerate(st.session_state.messages):
    content = Content(
        role = message["role"],
        parts = [Part.from_text(message['content'])] 
      )
    
    chat.history.append(content)


if len(st.session_state.messages) == 0:
    
    initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. After that, ask the user for their name and include personalized greetings for them. You use emojis to be interactive"
    llm_function(chat, initial_prompt)

# For Capture user input
query = st.chat_input("Message ReX") 
if query:
    with st.chat_message("user"):
        st.markdown(query)
    
    llm_function(chat, query)



        
    
