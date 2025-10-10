# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetManagerCandidateAssignmentsTool(Tool):
    """Analyzes candidates table to understand manager workload distribution and onboarding supervision patterns."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        manager_email = kwargs.get("manager_email")

        candidates = data.get("candidates", [])

        if manager_email:
            candidates = [c for c in candidates if c.get("manager_email_nullable") == manager_email]

        manager_workload = {}
        for candidate in candidates:
            manager = candidate.get("manager_email_nullable")
            if manager:
                if manager not in manager_workload:
                    manager_workload[manager] = {"count": 0, "candidates": []}
                manager_workload[manager]["count"] += 1
                manager_workload[manager]["candidates"].append({
                    "candidate_id": candidate.get("candidate_id"),
                    "candidate_name": candidate.get("candidate_name"),
                    "status": candidate.get("onboarding_status")
                })

        return json.dumps(manager_workload, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_manager_candidate_assignments",
                "description": "Analyzes candidates table to understand manager workload distribution and onboarding supervision patterns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "manager_email": {"type": "string", "description": "Specific manager or null for all managers"}
                    },
                    "required": [],
                },
            },
        }
