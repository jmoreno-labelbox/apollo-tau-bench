from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateSprintRetrospective(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sprint_id: str,
        what_went_well: list = [],
        what_needs_improvement: list = [],
        action_items: list = []
    ) -> str:
        pass

        if not sprint_id:
            payload = {"error": "sprint_id is required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", [])
        retrospectives = data.get("retrospectives", [])

        sprint = next((s for s in sprints if s.get("sprint_id") == sprint_id), None)
        if not sprint:
            payload = {"error": f"Sprint '{sprint_id}' not found"}
            out = json.dumps(payload)
            return out

        #if sprint.get("status") != "completed":
        #return json.dumps(
        #{"error": "Retrospective can only be created for completed sprints"}
        #)

        if len(what_went_well) < 1:
            payload = {
                    "error": "Retrospective must include at least 3 items for 'what went well'",
                    "current_count": len(what_went_well),
                    "required": 3,
                }
            out = json.dumps(
                payload)
            return out

        if len(what_needs_improvement) < 1:
            payload = {
                    "error": "Retrospective must include at least 3 items for 'what needs improvement'",
                    "current_count": len(what_needs_improvement),
                    "required": 3,
                }
            out = json.dumps(
                payload)
            return out

        #if len(action_items) < 1:
        #return json.dumps(
        #{
        #"error": "Retrospective must include at least 3 action items",
        #"current_count": len(action_items),
        #"required": 3,
        #}
        #)

        if sprint.get("completed_date"):
            try:
                completed_date = datetime.fromisoformat(
                    sprint["completed_date"].replace("Z", "+00:00")
                )
                days_since_completion = (datetime.now() - completed_date).days
                if days_since_completion > 2:
                    payload = {
                            "warning": f"Retrospective is being created {days_since_completion} days after sprint completion",
                        }
                    out = json.dumps(
                        payload)
                    return out
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
        payload = {"success": True, "retrospective": retrospective}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSprintRetrospective",
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
                    "required": [
                        "sprint_id",
                        "what_went_well",
                        "what_needs_improvement",
                    ],
                },
            },
        }
