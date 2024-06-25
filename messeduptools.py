import os
import csv
import datetime
import pandas as pd
from io import StringIO
from typing import Annotated, Optional, Tuple, List
from langchain_core.tools import tool
from dotenv import load_dotenv
load_dotenv()


# Warning: This executes code locally, which can be unsafe when not sandboxed

@tool
def get_db_folders() -> str:
    """This function returns the list of folders in the database directory (for eg. general_roster_data contains data for general medical personnel) you can use this to read the data which is relevant to the current task."""
    return os.listdir(os.environ.get('data_path'))

@tool
def construct_path_to_file(folder_name: str, date: str) -> str:
    """This function constructs the path to the file in the database directory for the given folder_name and date (strict dd-mm-yyyy format)."""
    return os.path.join(os.environ.get('data_path'), folder_name, f'{date}.csv')

@tool
def read_data_from_file(file_path: str, designation: str, available_time: str) -> str:
    """This function reads the data from the file path and returns the data of the personnel for the designation(lowercase) and available time(strict hh:mm:ss format)."""
    data = pd.read_csv(file_path)
    filter1 = data['Designation'] == designation
    now = datetime.datetime.strptime(available_time, '%H:%M:%S')
    for i in range(len(data)):
        data.loc[i, 'Availability Start'] = datetime.datetime.strptime(data.loc[i, 'Availability Start'], '%H:%M:%S')
        data.loc[i, 'Availability End'] = datetime.datetime.strptime(data.loc[i, 'Availability End'], '%H:%M:%S')
    filter2 = data['Availability Start'] <= now
    filter3 = data['Availability End'] >= now
    return data[filter1 & filter2 & filter3]

# @tool
# def read_db_for_roster(folder_name: str, date: str) -> str:
#     """This function takes in a folder_name which is present in db and a date (strict dd-mm-yyyy format) for which the data is supposed to be fetched. It returns the data from the folder for the given date."""
#     # lets assume here we are making an API call to the database which fetches the roster data for the current day.
#     # for now, lets assume the API call returns a csv file.
#     # lets try to read the contents of the file and save it temporarily.
#     # here i should write a logic to fetch the file with the given date and return the data.
#     datadir_path = os.path.join(os.environ.get('data_path') , folder_name)
#     file_path = os.path.join(datadir_path, f'{date}.csv')

#     csv_string_data = ''
#     with open(file_path, 'r') as file:
#         csv_reader = csv.reader(file)
        
#         for row in csv_reader:
#             csv_string_data += ','.join(row) + '\n'
    
#     file.close()

#     return csv_string_data

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
def notify_roster_personnel(id: List, message: Optional[str]) -> str:
    """This function takes in a python list of personnel mobile numbers whom are available and notifies them, returns a string of the personnel notified."""

    if len(id) == 0:
        return "No personnel available today."
    sent = []
    for num in id:
        if notification_logic(num):
            sent.append(num)
    return ' '.join(sent) + " have been notified."

# tools = [read_db_for_roster, get_current_date, get_current_time, counter, notify_roster_personnel]
# tool_names = ['read_db_for_roster', 'get_current_date', 'get_current_time', 'counter', 'notify_roster_personnel', 'read_db_for_roster_chunks']
# toolmap = {toolname: tool for (tool, toolname) in zip(tools, tool_names)}