
https://github.com/user-attachments/assets/c2076f75-a5bf-4433-852e-e8bf6f97157e
Uploading AI Chatbot - Opera 2025-05-31 02-57-45.mp4…


**AI Chatbot with LangChain, HuggingFace, and Streamlit
This is a simple AI chatbot web app built with:**

LangChain — for easy integration and chaining of LLMs

HuggingFaceEndpoint — to connect with the powerful HuggingFaceH4/zephyr-7b-beta model via Hugging Face Inference API

Streamlit — for an interactive and user-friendly chat interface

**Features**
Chat with a 7-billion parameter language model in real time

Conversation history with session state

Typing effect for a more natural chat experience

Sidebar with model status and chat statistics

Example questions to get started quickly

**Notes**
Inference speed is relatively slow when using public Hugging Face endpoints for large models like Zephyr-7B. This is expected due to API network latency and shared compute resources.

The app is intended as a prototype/demo to showcase LangChain integration with Hugging Face models.

For faster and more scalable usage, consider running models locally or on dedicated GPU servers.

**How to Run**
Clone the repo

Create and activate a Python environment

Install requirements from requirements.txt

Set your Hugging Face API token in .env file

Run streamlit run app.py

**Future Work**
Support for local model inference to reduce latency

Add more customizable model parameters

Improve UI/UX for a richer chat experience

