import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Initialize the model
@st.cache_resource
def load_model():
    """Load and cache the HuggingFace model"""
    try:
        # Create HuggingFaceEndpoint
        llm = HuggingFaceEndpoint(
            repo_id="HuggingFaceH4/zephyr-7b-beta",
            task="text-generation",
            temperature=0.5
        )
        
        # Wrap in ChatHuggingFace
        model = ChatHuggingFace(llm=llm)
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "model" not in st.session_state:
    st.session_state.model = load_model()

# App header
st.title("🤖 AI Chatbot")
st.markdown("Powered by HuggingFace Zephyr-7B")

# Sidebar with model info and controls
with st.sidebar:
    st.header("🛠️ Model Settings")
    
    # Model status
    if st.session_state.model:
        st.success("✅ Model loaded successfully")
    else:
        st.error("❌ Model failed to load")
    
    st.markdown("**Model:** HuggingFaceH4/zephyr-7b-beta")
    st.markdown("**Temperature:** 0.5")
    
    st.markdown("---")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    # Chat statistics
    st.markdown("### 📊 Chat Stats")
    st.metric("Messages", len(st.session_state.messages))
    
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.markdown("""
    - Ask questions naturally
    - Be specific for better responses
    - Use clear, concise language
    - Try different topics!
    """)

# Main chat interface
chat_container = st.container()

with chat_container:
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Check if model is loaded
    if not st.session_state.model:
        st.error("Model not loaded. Please check your setup and refresh the page.")
        st.stop()
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Show thinking indicator
            with st.spinner("Thinking..."):
                # Get response from model
                response = st.session_state.model.invoke(prompt)
                full_response = response.content
            
            # Display the response with typing effect
            displayed_response = ""
            for char in full_response:
                displayed_response += char
                message_placeholder.markdown(displayed_response + "▌")
                time.sleep(0.01)  # Typing effect speed
            
            # Final response without cursor
            message_placeholder.markdown(full_response)
            
        except Exception as e:
            error_message = f"Sorry, I encountered an error: {str(e)}"
            message_placeholder.error(error_message)
            full_response = error_message
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        Built with Streamlit and HuggingFace 🚀
    </div>
    """,
    unsafe_allow_html=True
)

# Optional: Add some example prompts
if len(st.session_state.messages) == 0:
    st.markdown("### 💬 Try asking me about:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🌍 Geography", use_container_width=True):
            example_prompt = "What is the capital of Pakistan?"
            st.session_state.messages.append({"role": "user", "content": example_prompt})
            st.rerun()
    
    with col2:
        if st.button("🔬 Science", use_container_width=True):
            example_prompt = "Explain how photosynthesis works"
            st.session_state.messages.append({"role": "user", "content": example_prompt})
            st.rerun()
    
    with col3:
        if st.button("💻 Technology", use_container_width=True):
            example_prompt = "What is machine learning?"
            st.session_state.messages.append({"role": "user", "content": example_prompt})
            st.rerun()