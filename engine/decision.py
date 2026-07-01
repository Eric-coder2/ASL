"""
author: Eric Penkala
date: 06/29/2026
"""

class Decision:
    def __init__(self, allowed, reason, capability=None):
        self.allowed = allowed
        self.reason = reason
        self.capability = capability
    
    def __repr__(self):
        return f"Decision(allowed={self.allowed}, reason={self.reason})"