from datetime import datetime, timezone, timedelta
from models.capability import Capability
from models.agent import Agent
from engine.policy_loader import load_policy, load_global_policy


'''
cap = Capability("fs.read", "/public/*", datetime(2030, 1, 1, tzinfo=timezone.utc))
print(cap)
print(cap.capability_id, cap.tool, cap.scope, cap.constraints)

try:
    cap.tool = "fs.delete"
except AttributeError as e:
    print("blocked 1:", e)

try:
    cap.constraints["max_bytes"] = 999999
except TypeError as e:
    print("blocked 2:", e)

agent = Agent("agent_1")
agent.add_capability(cap)
print(agent.capabilities)

try:
    agent.add_capability("fake")
except TypeError as e:
    print("blocked 3:", e)

print()
print(cap.is_expired())
print(cap.is_expired(now=datetime(2031, 1, 1, tzinfo=timezone.utc)))
print(cap.is_expired(now=cap.expires_at))

cap.record_usage()
print(cap.usage_count)
'''
'''
agent = load_policy("policies/agent_policy.json")
print(agent)
for c in agent.capabilities:
    print(c, c.constraints, c.expires_at)
'''
print(load_global_policy("policies/global_policy.json"))