from llama_cpp import Llama
from fastapi import FastAPI
from pydantic import BaseModel
# creating an Fast api app
app=FastAPI()
# loading the llama model to the memory n_ctx denotes number of tokens or context lngth
llm=Llama(model_path="llama-2-7b.Q2_K.gguf",n_ctx=512)

print("welcome to LLAMA CHATBOT")
print("Type EXIT to quit.\n")
# defines data type of incoming requests
class chatRequest(BaseModel):
    message:str
# defines  end point and accept post request only..
@app.post("/chat")
def chat(chat:chatRequest):
    prompt=f"User:{chat.message}\nAI:"
    output=llm(prompt,max_tokens=128,stop=["User:","AI:"],echo=False)
    reply=output["choices"][0]["text"].strip()
    return {"response":reply}

#to run use uvicorn main:app --reload
