"""
author: Eric Penkala
date: 03/30/2026
"""

"""
 each agent has an ID and a list of capabilities.
 you can dynamically assign permissions.
"""
class Agent:
    #initialize ID
    def __init__(self, agent_id):
        self.id = agent_id
        self.capabilities = []
    #add a capability
    def add_capability(self, capability):
        self.capabilities.append(capability)
    #return agent
    def __repr__(self):
        return f"<Agent {self.id}>"