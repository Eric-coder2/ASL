"""
author: Eric Penkala
date: 03/30/2026
"""

"""
checks to see if the capability_resource equals requested_resource

@param capability_resource - type str. It is the resource pattern defined in a capability
@param requested_resource - type str. The actual resource that the agent is trying to access
"""
def match_resource(capability_resource, requested_resource):
    """
    Supports:
    - Exact match
    - Wildcard match using *
    """

    # Exact match
    if capability_resource == requested_resource:
        return True

    # Wildcard match
    if "*" in capability_resource:
        prefix = capability_resource.split("*")[0]
        return requested_resource.startswith(prefix)

    return False