# Copyright Sierra

import datetime, uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateSprintRetrospective(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sprint_id, action_items = [], what_needs_improvement = [], what_went_well = []) -> str:

        if not sprint_id:
            return json.dumps({"error": "sprint_id is required"})

        sprints = list(data.get("sprints", {}).values())
        retrospectives = data.get("retrospectives", [])

        sprint = next((s for s in sprints if s.get("sprint_id") == sprint_id), None)
        if not sprint:
            return json.dumps({"error": f"Sprint '{sprint_id}' not found"})

        # if sprint["status"] != "completed":
        # output json serialization of
        # {"error": "Retrospectives are only permissible for finished sprints"}
        #     )

        if len(what_went_well) < 1:
            return json.dumps(
                {
                    "error": "Retrospective must include at least 3 items for 'what went well'",
                    "current_count": len(what_went_well),
                    "required": 3,
                }
            )

        if len(what_needs_improvement) < 1:
            return json.dumps(
                {
                    "error": "Retrospective must include at least 3 items for 'what needs improvement'",
                    "current_count": len(what_needs_improvement),
                    "required": 3,
                }
            )

        # if not action_items:
        # return json.dump(
        #         {
        # "error": "A minimum of 3 action items is required for the retrospective",
        # "current_count": count(action_items),
        # "mandatory": 3,
        #         }
        #     )

        if sprint.get("completed_date"):
            try:
                completed_date = datetime.fromisoformat(
                    sprint["completed_date"].replace("Z", "+00:00")
                )
                days_since_completion = (datetime.now() - completed_date).days
                if days_since_completion > 2:
                    return json.dumps(
                        {
                            "warning": f"Retrospective is being created {days_since_completion} days after sprint completion",
                        }
                    )
            except:
                pass

        retro_id = f"retro_{uuid.uuid4().hex[:8]}"

        retrospective = {
            "retrospective_id": retro_id,
            "sprint_id": sprint_id,
            "what_went_well": what_went_well,
            "what_needs_improvement": what_needs_improvement,
            "action_items": action_items,
            "created_date": datetime.now().isoformat(),
            "team_id": sprint.get("team_id"),
        }

        retrospectives.append(retrospective)

        return json.dumps({"success": True, "retrospective": retrospective})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_sprint_retrospective",
                "description": "Create a retrospective for a completed sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {"type": "string", "description": "The sprint ID"},
                        "what_went_well": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of things that went well (minimum 1)",
                        },
                        "what_needs_improvement": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of areas for improvement (minimum 1)",
                        },
                        "action_items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Action items for next sprint",
                        },
                    },
                    "required": ["sprint_id", "what_went_well", "what_needs_improvement"],
                },
            },
        }
