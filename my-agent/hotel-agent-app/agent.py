from google.adk import Agent
from toolbox_core import ToolboxSyncClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the ToolboxSyncClient with the URL of the Toolbox server   

toolbox = ToolboxSyncClient("http://127.0.0.1:5000")


# load the tools
tools = toolbox.load_toolset("hotel-management")


# Create an ADK Agent
root_agent = Agent(
    name="hotel_agent",
    model="gemini-2.5-flash",  # Or another suitable LLM
    description="An agent that can assist with hotel management tasks.",
    instruction="You are a helpful assistant for hotel management tasks. Use the tools provided to answer questions and perform tasks related to hotel management.",
    tools=tools,  # Attach the loaded tools
)

# # Interact with the agent, which will use the MCP tool
# response = agent.answer("hotel Hilton")
# print(f"Agent's response: {response.text}")
