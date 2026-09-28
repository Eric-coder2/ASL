"""
author: Eric Penkala
date: 03/30/2026
"""

from models.capability import Capability

"""
 Each agent has an ID and a list of capabilities.
 Capablities can only be added through add_capability(), 
 which is a single validated entry point
"""
class Agent:
    #initialize ID
    def __init__(self, agent_id: str):
        self.id = agent_id
        self._capabilities = [] # uses a convention ("_") to discourage access

    #returns list copy
    @property
    def capabilities(self):
        return tuple(self._capabilities) #returns read only copy of list
    
    #add capability
    def add_capability(self, capability):
        #doesnt authorize capability, structural check only
        #policy_engine checks if its allowed
        if not isinstance(capability, Capability):
            raise TypeError(f"Expected Capability object, got {type(capability.__name__)}")
        self._capabilities.append(capability)

    def __repr__(self):
        return f"<Agent {self.id}>"
        
        
    