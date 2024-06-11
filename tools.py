import os
import csv
from typing import Optional
from datetime import datetime
from dateutil import parser
from langchain.agents import tool

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
def extract_dates(text: str):
    """This function takes in a relevant text body which contain a single date context and returns a date object, in case of multiple dates try to run the function multiple times only with the relevant body of text which contains a single date"""
    return parser.parse(text).date()
@tool
def convert_to_time(text: str) -> datetime.time:
    """This function takes in a relevant text body which contain a single time context and returns a time object, in case of multiple times try to run the function multiple times only with the relevant body of text which contains a single time"""
    return datetime.strptime(text, "%H:%M:%S").time()
@tool
def send_mail(text: Optional[str], subject: Optional[str], recipient: Optional[str], cc: Optional[str]) -> str:
    """This function sends an email to the recipient with the given subject and text"""
    return f"Email has been sent to {recipient} with subject: {subject} and text: {text}"


mail_tools = [read_csv, extract_dates, send_mail, convert_to_time]