from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

class GetMilestoneDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], milestone_id: str = None) -> str:
        if not milestone_id:
            payload = {"error": "milestone_id is required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", [])
        for milestone in milestones:
            if milestone.get("milestone_id") == milestone_id:
                payload = milestone
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Milestone '{milestone_id}' not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMilestoneDetails",
                "description": "Get detailed information about a specific milestone",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "The milestone ID",
                        }
                    },
                    "required": ["milestone_id"],
                },
            },
        }
