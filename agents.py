import functools
from typing import List, Tuple
from agent_build import agent_creator_temp
from mtools import toolmap

class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)

class Agent(object):
    __metaclass__ = IterRegistry
    _registry = []
    def __init__(self, agent_name: str, tools: List, system_prompt: str) -> None:
        self._registry.append(self)
        self.agent_name = agent_name
        self.tools = tools
        self.system_prompt = system_prompt
        self.agent_prop = None
        self.agent_node = None
    def _create_agent(self) -> None:
        self.agent_node = agent_creator_temp(self.agent_name, self.tools, self.system_prompt)
    def get_agent(self):
        if self.agent_prop is None or self.agent_node is None:
            self._create_agent()
        return self.agent_node
    def __str__(self) -> str:
        return self.agent_name
    
db_agent = Agent('database_reader', [toolmap[x] for x in ['read_db_for_roster', 'get_current_date', 'get_current_time']], "You are a database reader, you will read the db and perform the necessary operations.")
notifier_agent = Agent('notifier', [toolmap[x] for x in ['get_current_time' , 'notify_roster_personnel']], "You are a notifier, you should take the data provided by the db_reader agent and notify the personnel.")
# validator_agent = Agent('validator', [toolmap[x] for x in ['counter']], "You are a validator, you will keep track of each task performed by the agents.")

agents = [agent.get_agent() for agent in Agent._registry]
members = [str(agent) for agent in Agent._registry]
