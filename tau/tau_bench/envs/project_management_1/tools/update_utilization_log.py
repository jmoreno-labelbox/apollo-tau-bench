# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUtilizationLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id, new_utilization) -> str:

        if not all([employee_id, new_utilization is not None]):
            return json.dumps({"error": "employee_id and new_utilization are required"})

        utilization_logs = data.get("utilization_logs", [])

        log_entry = {
            "log_id": f"log_{uuid.uuid4().hex[:8]}",
            "employee_id": employee_id,
            "utilization": new_utilization,
            "timestamp": datetime.now().isoformat(),
        }

        utilization_logs.append(log_entry)

        employees = list(data.get("employees", {}).values())
        for employee in employees:
            if employee.get("employee_id") == employee_id:
                employee["current_utilization"] = new_utilization
                break

        return json.dumps({"success": True, "log_entry": log_entry})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_utilization_log",
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
