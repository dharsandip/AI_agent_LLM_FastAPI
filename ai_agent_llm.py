

from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_openai_functions_agent, load_tools, initialize_agent, AgentType
from langchain.tools.tavily_search import TavilySearchResults
from langchain.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_community.llms import Ollama


load_dotenv()


def get_function_tools():
  search = TavilySearchAPIWrapper()
  tavily_tool = TavilySearchResults(api_wrapper=search)

  tools = [
      tavily_tool
  ]

  tools.extend(load_tools(['wikipedia', 'serpapi']))

  return tools


def init_action(query):
     
  model_local = Ollama(model="mistral", temperature=0.6)
  llm = model_local

  tools = get_function_tools()
  agent = initialize_agent(tools=tools, llm=llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
  response = agent.run(query)
  
  return response

