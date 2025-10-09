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

class SearchChangeRequests(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str = None,
        status: str = None,
        priority: str = None,
        change_type: str = None,
        requester_id: str = None,
        include_impact: bool = False
    ) -> str:
        change_requests = data.get("change_requests", [])
        results = []

        for cr in change_requests:
            match = True

            if project_id and cr.get("project_id") != project_id:
                match = False
            if status and cr.get("status") != status:
                match = False
            if priority and cr.get("priority") != priority:
                match = False
            if change_type and cr.get("change_type") != change_type:
                match = False
            if requester_id and cr.get("requester_id") != requester_id:
                match = False

            if match:
                result = cr.copy()
                if not include_impact and "impact_assessment" in result:
                    result["has_impact_assessment"] = True
                    result["overall_risk"] = cr.get("impact_assessment", {}).get(
                        "overall_risk"
                    )
                    del result["impact_assessment"]
                results.append(result)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchChangeRequests",
                "description": "Search for change requests by various criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "Filter by project ID",
                        },
                        "status": {"type": "string", "description": "Filter by status"},
                        "priority": {
                            "type": "string",
                            "description": "Filter by priority",
                        },
                        "change_type": {
                            "type": "string",
                            "description": "Filter by change type",
                        },
                        "requester_id": {
                            "type": "string",
                            "description": "Filter by requester",
                        },
                        "include_impact": {
                            "type": "boolean",
                            "description": "Include full impact assessment details",
                        },
                    },
                },
            },
        }
