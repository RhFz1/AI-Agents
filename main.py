from graph import graph
from langchain_core.messages import HumanMessage

text = ''

with open("prompt.txt", "r") as file:
    text = file.read()

for s in graph.stream(
    {
        "messages": [
            HumanMessage(text)
        ]
    }
        
):
    if '__end__' not in s:
        print(s)
        print('-----------')
