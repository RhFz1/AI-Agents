import os
import csv
import datetime
from io import StringIO
from typing import Annotated, Optional, Tuple
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langchain_experimental import repl

# Warning: This executes code locally, which can be unsafe when not sandboxed

@tool
def read_db_for_roster(date: str) -> str:
    """This function reads a database which contains data regarding the availabilities of the personnel for the following passed date i.e., fetching the roster of personnel."""

    # lets assume here we are making an API call to the database which fetches the roster data for the current day.
    # for now, lets assume the API call returns a csv file.
    # lets try to read the contents of the file and save it temporarily.
    # here i should write a logic to fetch the file with the given date and return the data.
    temp = __file__
    csv_data = StringIO(temp)

    csv_string_data = ''
    csv_reader = csv.reader(csv_data)

    for row in csv_reader:
        csv_string_data += ','.join(row) + '\n'
    
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
def notify_roster_personnel(id: list, message: str) -> str:
    """This function expects a list of tuples which is (mobile number, first name) in str format of all the available personnel according to their today's roster, and a """

    if len(id) == 0:
        return "No personnel available today."
    
    sent = []

    for num, name in id:
        if notification_logic(num):
            sent.append(name)
    return ' '.join(sent) + " have been notified."