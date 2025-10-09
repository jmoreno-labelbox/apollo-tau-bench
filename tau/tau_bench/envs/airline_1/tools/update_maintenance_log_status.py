from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateMaintenanceLogStatus(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], log_id: str, new_status: str) -> str:
        logs = data.get("maintenance_logs", {}).values()
        for log in logs.values():
            if log.get("log_id") == log_id:
                log["status"] = new_status
                payload = log
                out = json.dumps(payload)
                return out
        payload = {"error": "Maintenance log not found", "log_id": log_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateMaintenanceLogStatus",
                "description": "Updates the status of a specific maintenance log (e.g., 'Halted', 'Completed').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_id": {
                            "type": "string",
                            "description": "The unique ID of the maintenance log to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the log.",
                        },
                    },
                    "required": ["log_id", "new_status"],
                },
            },
        }
