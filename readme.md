🦙 LLaMA Chatbot API (FastAPI)

A simple RESTful chatbot powered by LLaMA 2 and FastAPI.

 🚀 How to Run

1. **Clone this repository**
   
   git clone https://github.com/yourusername/llama-chatbot-api.git
   cd llama-chatbot-api



   ###  Model File (Important ❗)
   
⚠️Note: The LLaMA model file (llama-2-7b.Q2_K.gguf) is not included in this repository due to licensing and size restrictions.

To run this project:

Download the quantized .gguf model file from official sources like Hugging Face.

Place the file in the project root or specify the correct path in main.py.



### Start the FastAPI server:

uvicorn main:app --reload

