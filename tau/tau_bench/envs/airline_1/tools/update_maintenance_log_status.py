# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateMaintenanceLogStatus(Tool):
    """A tool to update the status of an existing maintenance log."""
    @staticmethod
    def invoke(data: Dict[str, Any], log_id: str, new_status: str) -> str:
        logs = list(data.get("maintenance_logs", {}).values())
        for log in logs:
            if log.get("log_id") == log_id:
                log["status"] = new_status
                return json.dumps(log)
        return json.dumps({"error": "Maintenance log not found", "log_id": log_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "update_maintenance_log_status",
                "description": "Updates the status of a specific maintenance log (e.g., 'Halted', 'Completed').",
                "parameters": {
                    "type": "object", "properties": {
                        "log_id": {"type": "string", "description": "The unique ID of the maintenance log to update."},
                        "new_status": {"type": "string", "description": "The new status for the log."}
                    }, "required": ["log_id", "new_status"]
                }
            }
        }
