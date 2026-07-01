"""
author: Eric Penkala
date: 06/29/2026
"""

import os
from datetime import datetime

'''logs everything that happens in this program to the audit log'''


LOG_PATH = "logs/audits.log"

def log_decision(agent, action, resource, result, reason):
    timestamp = datetime.utcnow().isoformat()
    
    # what shoes in each entry in audit log
    entry= (
        f"{timestamp} | "
        f"agent={agent} | "
        f"action={action} | "
        f"resource={resource} | "
        f"result={result} | "
        f"reason={reason}\n"
    )

    with open(LOG_PATH, "a") as f:
        f.write(entry)