from openai import OpenAI
from dotenv import load_dotenv
import os
import aisuite as ai

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
aisuite_client = ai.Client()
openai_client = OpenAI(api_key=api_key)