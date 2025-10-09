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

class UpdateRequestStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], request_id: str, status: str, assigned_employees: list = [], allocated_hours: int = 0) -> str:
        if not all([request_id, status]):
            payload = {"error": "request_id and status are required"}
            out = json.dumps(payload)
            return out

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
                payload = result
                out = json.dumps(payload)
                return out
        payload = {"error": f"Request with ID '{request_id}' not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateRequestStatus",
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
