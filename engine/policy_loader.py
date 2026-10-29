"""
author: Eric Penkala
date: 06/29/2026
"""

import json
from datetime import datetime
from models.capability import Capability
from models.agent import Agent

def load_policy(path):
    with open(path, "r") as f:
        data = json.load(f)

    agent = Agent(data["agent"])

    for cap in data["capabilities"]:
        expires_at = datetime.fromisoformat(cap["expires_at"])
        #a datetime without a timezone cant be compared safely later,
        #so reject it here, at load time, instead of failing mid request
        if expires_at.tzinfo is None:
            raise ValueError("expires_at must include a timezone")
        
        capability = Capability(
            tool=cap["tool"],
            scope=cap["scope"],
            expires_at=expires_at,
            constraints=cap.get("constraints"),
        )

        agent.add_capability(capability) #the one valid door to add a new capability

    return agent

def load_global_policy(path):
    with open(path, "r") as f:
        data = json.load(f)
    
    deny_rules = data["deny"] #required: policy file with no "deny" key is malformed
    return deny_rules