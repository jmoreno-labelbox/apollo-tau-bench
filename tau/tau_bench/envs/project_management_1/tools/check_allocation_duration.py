from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CheckAllocationDuration(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, project_id: str = None) -> str:
        if not all([employee_id, project_id]):
            payload = {"error": "employee_id and project_id are required"}
            out = json.dumps(payload)
            return out

        allocations = data.get("allocations", {}).values()

        for allocation in allocations.values():
            if (
                allocation.get("employee_id") == employee_id
                and allocation.get("project_id") == project_id
            ):
                start_date = datetime.fromisoformat(allocation.get("start_date"))
                duration_days = (datetime.now() - start_date).days
                duration_months = duration_days / 30
                payload = {
                    "employee_id": employee_id,
                    "project_id": project_id,
                    "start_date": allocation.get("start_date"),
                    "duration_days": duration_days,
                    "duration_months": round(duration_months, 1),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Allocation not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckAllocationDuration",
                "description": "Check how long an employee has been allocated to a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        },
                    },
                    "required": ["employee_id", "project_id"],
                },
            },
        }
