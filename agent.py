from typing import Literal, List, Any
from langchain_core.tools import tool
from langgraph.types import Command
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict, Annotated
from langchain_core.prompts.chat import ChatPromptTemplate
from langgraph.graph import START, StateGraph, END
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage
from prompt_library.prompt import system_prompt
from utils.llms import LLMModel
from toolkit.toolkits import *

class Router(TypedDict):
    next : Literal['information_node' , "booking_node" , "FINISH"]
    resoning : str

class AgentState(TypedDict) : 
    messages : Annotated[list[Any] , add_messages] # where add_messages is a reducer that only just append messages in List any kind of message like AiMessage , HumanMessage , System_Message
    query : str
    next : str
    id_number : str
    current_reasoning : str

class DoctorAppointmentAgent:
    def __init__(self ):
        llm_model = LLMModel()
        self.llm_model = llm_model.get_model()
    def supervisor_node (self , state : AgentState) -> Command[Literal['information_node' , 'booking_node' , "__end__"]]:
        
