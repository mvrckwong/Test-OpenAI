import dotenv

import openai
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

ENV_FILE = ".env"

print(dotenv.get_key(ENV_FILE, "openai_api_key"))