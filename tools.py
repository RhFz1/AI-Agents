import os
import csv
import numpy as np
from typing import Optional
import datetime
from dateutil import parser
from langchain.agents import tool
from typing import Tuple


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
def get_current_date() -> Tuple[datetime.date, str]:
    """This function returns the current date and day of the week for calculation purposes"""
    return datetime.date.today(), datetime.date.today().strftime("%A")
@tool
def get_current_time() -> datetime.datetime:
    """This function returns the current time for calculation purposes"""
    return datetime.datetime.now()
@tool           
def get_time_difference(start: str, end: str) -> int:
    """This function takes in start time and end time in HH:MM:SS format and returns the total number of hours between these two times"""
    start = datetime.datetime.strptime(start, "%H:%M:%S")
    end = datetime.datetime.strptime(end, "%H:%M:%S")
    diff = (end - start).total_seconds() / 3600
    return diff
@tool
def automate_leave_application(name: str, start: str, end: str) -> str:
    """If given the start and end date, this function will automate the leave application."""
    return f"Leave has been applied for {name} from {start} to {end} date."
@tool
def send_mail(text: Optional[str], subject: Optional[str], recipient: Optional[str], cc: Optional[str]) -> None:
    """This function sends an email to the recipient with the given subject and text"""
    with open("mails.txt", "a") as file:
        file.write(f"Email has been sent to {recipient} with subject: {subject} and text: {text}\n")
@tool
def can_apply_leave(emp_name: str) -> int:
    """This function takes in employee name and fetches the number of available leaves the employee has which can be used to approve leave applications."""
    return np.random.randint(0, 10)
@tool
def date_diff(start: str, end: str) -> int:
    """This function takes in start date and end date strings in (dd/mm/yyyy format) and returns the total number of days between these two dates."""
    start = parser.parse(start)
    end = parser.parse(end)
    diff = end - start
    return diff.days + 1    
@tool
def read_from_db(date: str) -> str:
    """This function reads the attendance data from a database for the given date"""
    return "YES i have read the attendance data for " + date
    
mail_tools = [read_csv, get_current_date, send_mail, automate_leave_application, can_apply_leave, date_diff]