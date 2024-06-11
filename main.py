import os
from agent import agent_executor

list(agent_executor.stream({"input": "I have met a person named Noah who is 25 years, it was nice talking to the person. Can you help me in storing the relevant data in the db?"}))