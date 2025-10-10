# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LinkChangeToMilestone(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cr_id, milestone_id, impact_type = "schedule") -> str:

        if not all([cr_id, milestone_id]):
            return json.dumps({"error": "cr_id and milestone_id are required"})

        change_requests = list(data.get("change_requests", {}).values())
        milestones = list(data.get("milestones", {}).values())

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        milestone = next(
            (m for m in milestones if m.get("milestone_id") == milestone_id), None
        )

        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})
        if not milestone:
            return json.dumps({"error": f"Milestone '{milestone_id}' not found"})

        if cr.get("project_id") != milestone.get("project_id"):
            return json.dumps(
                {"error": "Change request and milestone must be in the same project"}
            )

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

        return json.dumps(
            {
                "success": True,
                "link_created": {
                    "cr_id": cr_id,
                    "milestone_id": milestone_id,
                    "impact_type": impact_type,
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_change_to_milestone",
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
