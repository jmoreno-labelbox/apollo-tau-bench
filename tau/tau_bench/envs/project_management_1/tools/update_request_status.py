# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateRequestStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        status = kwargs.get("status")
        assigned_employees = kwargs.get("assigned_employees", [])
        allocated_hours = kwargs.get("allocated_hours", 0)

        if not all([request_id, status]):
            return json.dumps({"error": "request_id and status are required"})

        resource_requests = data.get("resource_requests", [])

        for request in resource_requests:
            if request.get("request_id") == request_id:
                request["status"] = status
                request["assigned_employees"] = assigned_employees
                request["allocated_hours"] = allocated_hours

                result = {"success": True, "request": request}
                if status == "partially_fulfilled":
                    hours_needed = request.get("hours_needed", 0)
                    skill_gap = hours_needed - allocated_hours
                    result["skill_gap"] = skill_gap

                return json.dumps(result)

        return json.dumps({"error": f"Request with ID '{request_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_request_status",
                "description": "Update the status of a resource request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "The request ID",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status: pending, partially_fulfilled, fulfilled, cancelled",
                        },
                        "assigned_employees": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of assigned employee IDs",
                        },
                        "allocated_hours": {
                            "type": "number",
                            "description": "Total hours allocated",
                        },
                    },
                    "required": ["request_id", "status"],
                },
            },
        }
