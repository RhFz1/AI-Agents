import os
import csv
import datetime
from io import StringIO
from typing import Annotated, Optional, Tuple, List
from langchain_core.tools import tool
from dotenv import load_dotenv
load_dotenv()

# Warning: This executes code locally, which can be unsafe when not sandboxed

@tool
def read_db_for_roster(date: str) -> str:
    """This function reads a database which contains data regarding the availabilities of the personnel for the following passed date (dd-mm-yyyy format) i.e., fetching the roster of personnel."""
    # lets assume here we are making an API call to the database which fetches the roster data for the current day.
    # for now, lets assume the API call returns a csv file.
    # lets try to read the contents of the file and save it temporarily.
    # here i should write a logic to fetch the file with the given date and return the data.
    datadir_path = os.path.join(os.environ.get('data_path') , 'roster_data')
    file_path = os.path.join(datadir_path, f'{date}.csv')

    csv_string_data = ''
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            csv_string_data += ','.join(row) + '\n'
    
    file.close()

    return csv_string_data

def notification_logic(num: int) -> bool:
    return True

@tool
def get_current_date() -> Tuple[datetime.date, str]:
    """This function returns the current date and day of the week for calculation purposes"""
    return datetime.date.today(), datetime.date.today().strftime("%A")
@tool
def get_current_time() -> datetime.datetime:
    """This function returns the current time for calculation purposes"""
    return datetime.datetime.now()  

@tool
def counter(x: int) -> int:
    """This function increments the passed value by 1 and returns the result, it basically functions as a counter."""
    return x + 1

@tool
def notify_roster_personnel(id: List, message: str) -> str:
    """This function takes in mobile numbers list of personnel who are available at the time of emergency and sends them a notification, and returns a confirmation message."""

    if len(id) == 0:
        return "No personnel available today."
    sent = []
    for num in id:
        if notification_logic(num):
            sent.append(num)
    return ' '.join(sent) + " have been notified."

tools = [read_db_for_roster, get_current_date, get_current_time, counter, notify_roster_personnel]
tool_names = ['read_db_for_roster', 'get_current_date', 'get_current_time', 'counter', 'notify_roster_personnel']
toolmap = {toolname: tool for (tool, toolname) in zip(tools, tool_names)}