# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchChangeRequests(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        status = kwargs.get("status")
        priority = kwargs.get("priority")
        change_type = kwargs.get("change_type")
        requester_id = kwargs.get("requester_id")
        include_impact = kwargs.get("include_impact", False)

        change_requests = list(data.get("change_requests", {}).values())
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

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_change_requests",
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
