"""
author: Eric Penkala
data: 04/01/2026
"""

from engine.matcher import match_resource
from engine.logger import log_decision
from engine.decision import Decision

"""
checks to see if agent is allowed to make action on specific resource

@param agent - agent requesting action
@param action - what action the agent wants to make
@param resource - what resource the agent wants to act upon
"""

# returns true if constraints are satisfied
def check_constraints(cap):
    #returns true if constraints are satisfied
    if "rate_limit" in cap.constraints:
        limit = cap.constraints["rate_limit"]

        if cap.usage_count >= limit: 
            print(f"Rate limit exceeded for {cap}")
            return False
    return True

def is_allowed(agent, action, resource):
    # check DENY rules first
    for cap in agent.capabilities:
        if cap.effect == "deny":
            if cap.action == action and match_resource(cap.resource, resource):
                #log decision
                log_decision(
                    agent.name,
                    action,
                    resource,
                    "DENIED",
                    f"Matched DENY {cap}"
                )

                return Decision(allowed=False,
                                reason=f"Matched DENY {cap}",
                                capability=cap
                                )

    # check ALLOW rules
    for cap in agent.capabilities:
        if cap.effect == "allow":
            if cap.action == action and match_resource(cap.resource, resource):
                # make sure you still have cap usage
                if not check_constraints(cap):
                    #log decision
                    log_decision(
                        agent.name,
                        action,
                        resource,
                        "DENIED",
                        f"Constraint failed {cap}"
                    )

                    return Decision(
                        allowed=False,
                        reason=f"Constraint failed {cap}",
                        capability=cap
                    )

                # keeps track of capability usage
                cap.usage_count += 1
                
                #log decision
                log_decision(
                    agent.name,
                    action,
                    resource,
                    "ALLOWED",
                    f"Matched {cap}"
                )
                
                return Decision(
                    allowed=True,
                    reason=f"Matched ALLOW {cap}",
                    capability=cap
                )

    # Step 4: Default deny
    #log decision
    log_decision(
        agent.name,
        action,
        resource,
        "DENIED",
        "No matching capability found"
    )
    print("No matching capability found → DENY")

    return Decision(
        allowed=False,
        reason="No matching capability found",
        capability=None
    )