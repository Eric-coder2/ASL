"""
author: Eric Penkala
date: 06/29/2026
"""

import json
from models.capability import Capability
from models.agent import Agent

def load_policy(path):
    with open(path, "r") as f:
        data = json.load(f)

    agent = Agent(data["agent"])

    for cap in data["capabilities"]:
        capability = Capability(
            effect=cap["effect"],
            action=cap["action"],
            resource=cap["resource"],
            max_uses=cap.get("max_uses"),
        )

        agent.capabilities.append(capability)

    return agent