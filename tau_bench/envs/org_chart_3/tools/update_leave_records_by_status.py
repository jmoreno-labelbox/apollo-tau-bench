from tau_bench.envs.tool import Tool
import json
from typing import Any

class update_leave_records_by_status(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        current_status: str,
        new_status: str,
        notes: str = ""
    ) -> str:
        leave_records = data.get("leave_records", [])
        updated_count = 0

        for record in leave_records:
            if (
                record.get("employee_id") == employee_id
                and record.get("status") == current_status
            ):
                record["status"] = new_status
                if notes:
                    record["notes"] = f"{record.get('notes', '')} {notes}".strip()
                updated_count += 1

        data["leave_records"] = leave_records
        payload = {
            "success": f"Updated {updated_count} leave records from {current_status} to {new_status} for employee {employee_id}"
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        leave_records = data.get("leave_records", [])
        updated_count = 0

        for record in leave_records:
            if (
                record.get("employee_id") == employee_id
                and record.get("status") == current_status
            ):
                record["status"] = new_status
                if notes:
                    record["notes"] = f"{record.get('notes', '')} {notes}".strip()
                updated_count += 1

        data["leave_records"] = leave_records
        payload = {
                "success": f"Updated {updated_count} leave records from {current_status} to {new_status} for employee {employee_id}"
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateLeaveRecordsByStatus",
                "description": "Update all leave records for an employee that match a specific status to a new status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "current_status": {
                            "type": "string",
                            "description": "Current status to match (e.g., 'Pending')",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status to set (e.g., 'Approved', 'Cancelled')",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes to append",
                        },
                    },
                    "required": ["employee_id", "current_status", "new_status"],
                    "additionalProperties": False,
                },
            },
        }
