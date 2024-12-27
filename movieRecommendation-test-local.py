from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load environment variables from .env file
# load_dotenv(r"C:\Users\SHIVAMIKA\Desktop\IIT Patna Doc\New folder\Hackethon\building-your-own-flows-main (1)\building-your-own-flows-main\.env")

client = MiraClient(config={"API_KEY": "sb-f915fc31d83eed93780402d2eec45787"})
# api_key = os.getenv("API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": "sb-f915fc31d83eed93780402d2eec45787"})

flow = Flow(source="flow.yaml")

input_dict = {"topic": "3 idiots", "style": "amir khan   "}

response = client.flow.test(flow, input_dict)

print(response)