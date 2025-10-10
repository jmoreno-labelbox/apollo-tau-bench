# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMilestoneDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        milestone_id = kwargs.get("milestone_id")
        if not milestone_id:
            return json.dumps({"error": "milestone_id is required"})

        milestones = list(data.get("milestones", {}).values())
        for milestone in milestones:
            if milestone.get("milestone_id") == milestone_id:
                return json.dumps(milestone, indent=2)

        return json.dumps({"error": f"Milestone '{milestone_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_milestone_details",
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
