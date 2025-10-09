from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LinkChangeToMilestone(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cr_id: str = None, milestone_id: str = None, impact_type: str = "schedule") -> str:
        if not all([cr_id, milestone_id]):
            payload = {"error": "cr_id and milestone_id are required"}
            out = json.dumps(payload)
            return out

        change_requests = data.get("change_requests", [])
        milestones = data.get("milestones", [])

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        milestone = next(
            (m for m in milestones if m.get("milestone_id") == milestone_id), None
        )

        if not cr:
            payload = {"error": f"Change request '{cr_id}' not found"}
            out = json.dumps(payload)
            return out
        if not milestone:
            payload = {"error": f"Milestone '{milestone_id}' not found"}
            out = json.dumps(payload)
            return out

        if cr.get("project_id") != milestone.get("project_id"):
            payload = {"error": "Change request and milestone must be in the same project"}
            out = json.dumps(payload)
            return out

        if "linked_milestones" not in cr:
            cr["linked_milestones"] = []

        link_info = {
            "milestone_id": milestone_id,
            "milestone_name": milestone.get("milestone_name"),
            "impact_type": impact_type,
            "linked_date": datetime.now().isoformat(),
        }

        cr["linked_milestones"].append(link_info)

        if cr.get("status") == "approved" and cr.get("impact_assessment"):
            impact = cr["impact_assessment"]
            if impact_type == "schedule" and impact.get("timeline_impact_weeks", 0) > 0:

                milestone["change_impact_weeks"] = (
                    milestone.get("change_impact_weeks", 0)
                    + impact["timeline_impact_weeks"]
                )
                milestone["impacted_by_changes"] = milestone.get(
                    "impacted_by_changes", []
                )
                milestone["impacted_by_changes"].append(cr_id)
        payload = {
                "success": True,
                "link_created": {
                    "cr_id": cr_id,
                    "milestone_id": milestone_id,
                    "impact_type": impact_type,
                },
            }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkChangeToMilestone",
                "description": "Link a change request to affected project milestones",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        },
                        "impact_type": {
                            "type": "string",
                            "description": "Type of impact: schedule, scope, resource",
                        },
                    },
                    "required": ["cr_id", "milestone_id"],
                },
            },
        }
