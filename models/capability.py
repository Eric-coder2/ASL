"""
author: Eric Penkala
date: 03/30/2026
"""

"""
action = what your doing(read, write, etc)
resource = what your touching(file:/data/*)
constraints = optional limits
effect = allow/deny
"""
class Capability:
    #initialize action, resource, constraints, and effect
    def __init__(self, action, resource, constraints=None, effect="allow"):
        self.action = action
        self.resource = resource
        self.constraints = constraints or {}
        self.effect = effect  # "allow" or "deny"
        self.usage_count = 0 # how many times a capability is used
    
    #return agent
    def __repr__(self):
        return f"<Capability {self.effect.upper()} {self.action}:{self.resource}>"