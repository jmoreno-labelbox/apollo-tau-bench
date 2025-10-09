from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetManagerCandidateAssignmentsTool(Tool):
    """Examines the candidates table to grasp the distribution of manager workloads and patterns of onboarding supervision."""

    @staticmethod
    def invoke(data: dict[str, Any], manager_email: str = None) -> str:
        candidates = data.get("candidates", [])

        if manager_email:
            candidates = [
                c
                for c in candidates
                if c.get("manager_email_nullable") == manager_email
            ]

        manager_workload = {}
        for candidate in candidates:
            manager = candidate.get("manager_email_nullable")
            if manager:
                if manager not in manager_workload:
                    manager_workload[manager] = {"count": 0, "candidates": []}
                manager_workload[manager]["count"] += 1
                manager_workload[manager]["candidates"].append(
                    {
                        "candidate_id": candidate.get("candidate_id"),
                        "candidate_name": candidate.get("candidate_name"),
                        "status": candidate.get("onboarding_status"),
                    }
                )
        payload = manager_workload
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetManagerCandidateAssignments",
                "description": "Analyzes candidates table to understand manager workload distribution and onboarding supervision patterns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "manager_email": {
                            "type": "string",
                            "description": "Specific manager or null for all managers",
                        }
                    },
                    "required": [],
                },
            },
        }
