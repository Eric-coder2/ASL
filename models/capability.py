"""
author: Eric Penkala
date: 03/30/2026
"""

"""
tool = what your doing(read, write, etc)
scope = what your touching(file:/data/*)
constraints = optional limits
effect = allow/deny
"""

import uuid
from datetime import datetime, timezone
from types import MappingProxyType
class Capability:
    #initialize tool, scope, expires_at, constraints, and capability_id
    def __init__(self, tool: str, scope: str, expires_at: datetime, constraints: dict | None = None, capability_id : str | None = None):
        self._capability_id = capability_id or f"cap_{uuid.uuid4().hex[:12]}"
        self._tool = tool
        self._scope = scope
        self._constraints = dict(constraints or {})
        self._issued_at = datetime.now(timezone.utc)
        self._expires_at = expires_at
        self._usage_count = 0
    
    @property
    def capability_id(self):
        return self._capability_id

    @property
    def tool(self):
        return self._tool
    
    @property
    def scope(self):
        return self._scope
    
    @property
    def constraints(self):
        #returns read only view, writes raises TypeError
        return MappingProxyType(self._constraints)
    
    @property
    def issued_at(self):
        return self._issued_at
    
    @property
    def expires_at(self):
        return self._expires_at
    
    @property
    def usage_count(self):
        return self._usage_count
    
    def is_expired(self, now: datetime | None = None) -> bool:
        now = now or datetime.now(timezone.utc)
        return now >= self._expires_at
    
    def record_usage(self):
        self._usage_count += 1
    
    #return agent
    def __repr__(self):
        return f"<Capability: tool={self._tool} : scope={self._scope} : id={self._capability_id}>"