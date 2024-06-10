import os
import pandas as pd
import csv
from langchain.agents import initialize_agent, Tool, AgentExecutor
from langchain.agents import tool
from langchain.prompts import PromptTemplate
from langchain_together import Together
from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.agents.format_scratchpad.openai_tools import format_to_openai_tool_messages
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain.agents import AgentExecutor
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

prompt_template = PromptTemplate(input_variables=["input"], template="Convert the following text to uppercase: {input}")

@tool
def read_csv(input_path: str) -> str:
    """This functions read a CSV file from the given input path and returns the string representation of the file"""
    with open(input_path, 'r') as file:
        csv_data = ''
        reader = csv.reader(file)
        for row in reader:
            csv_data += ','.join(row) + '\n'
    return csv_data

@tool
def convert_to_uppercase(text: str) -> str:
    """This function converts the given text to uppercase"""
    return text.upper()

@tool
def save_the_gathered_data(name: str, age: int, gender: str) -> str:
    """This function takes in name, age and gender of the person and stores it in db"""
    return f"Name: {name}, Age: {age} and Gender: {gender} has been stored in the database\n"

@tool
def do_something(text: str) -> str:
    """This function is responsile for performing a zugzugwang operation on the string"""
    return text + "asdfjkl;"

tools = [read_csv, convert_to_uppercase, save_the_gathered_data, do_something]

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are very powerful assistant, but don't know current events",
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

llm_with_tools = llm.bind_tools(tools)

agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

list(agent_executor.stream({"input": "Can you perform the zugzugwang operation on this text?: hehehhehe hehehe"}))