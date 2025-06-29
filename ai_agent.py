import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
load_dotenv()

#setup environment variables
groq_api=os.getenv("GROQ_API_KEY")
tavily_api=os.getenv("TAVILY_API_KEY")

def response_from_agent(query,system_prompt,model,allow_search):
    llm_groq = ChatGroq(
    model=model,
    groq_api_key=groq_api)

    tools = [TavilySearch(
        api_key=tavily_api, 
        max_results=2)] if allow_search else []
    
    agent = create_react_agent(
        model=llm_groq,
        tools=tools,
        prompt=system_prompt
    )

    State={"messages": query}
    response = agent.invoke(State)
    messages = response.get("messages", [])
    print(f"Messages: {messages}")
    ai_message= [message.content for message in messages if isinstance(message, AIMessage)]
    print(f"AI Message: {ai_message}")
    print(f"Allowed search is {allow_search}")
    return ai_message[-1]