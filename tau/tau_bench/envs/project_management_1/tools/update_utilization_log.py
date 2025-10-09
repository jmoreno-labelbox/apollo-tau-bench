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

class UpdateUtilizationLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, new_utilization: float = None) -> str:
        if not all([employee_id, new_utilization is not None]):
            payload = {"error": "employee_id and new_utilization are required"}
            out = json.dumps(payload)
            return out

        utilization_logs = data.get("utilization_logs", {}).values()

        log_entry = {
            "log_id": f"log_{uuid.uuid4().hex[:8]}",
            "employee_id": employee_id,
            "utilization": new_utilization,
            "timestamp": datetime.now().isoformat(),
        }

        data["utilization_logs"][log_entry["utilization_log_id"]] = log_entry

        employees = data.get("employees", {}).values()
        for employee in employees.values():
            if employee.get("employee_id") == employee_id:
                employee["current_utilization"] = new_utilization
                break
        payload = {"success": True, "log_entry": log_entry}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUtilizationLog",
                "description": "Log utilization changes for an employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "new_utilization": {
                            "type": "number",
                            "description": "New utilization percentage",
                        },
                    },
                    "required": ["employee_id", "new_utilization"],
                },
            },
        }
