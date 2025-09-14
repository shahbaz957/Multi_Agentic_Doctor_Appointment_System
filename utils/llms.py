import os 
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

class LLM_Model:
    def __init__(self , model_name = "deepseek-r1-distill-llama-70b"):
        self.model_name = model_name
        self.groq_model = ChatGroq(model=model_name)

    def get_model(self): # this is known as instance method
        return self.groq_model
    

if __name__ == "__main__" :
    llm_instance = LLM_Model()
    llm_model = llm_instance.get_model()
    response = llm_model.invoke("Hi")
    print(response)
