import os
import csv
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
def automate_leave_application(name: str, start: str, end: str, reason: Optional[str]) -> str:
    """If given the start and end date, this function will automate the leave application for the given reason which is optional"""
    return f"Leave has been applied for {name} from {start} to {end} for the reason: {reason}"
@tool
def send_mail(text: Optional[str], subject: Optional[str], recipient: Optional[str], cc: Optional[str]) -> str:
    """This function sends an email to the recipient with the given subject and text"""
    return f"Email has been sent to {recipient} with subject: {subject} and text: {text}"


mail_tools = [read_csv, get_current_date, send_mail, automate_leave_application, get_current_time]