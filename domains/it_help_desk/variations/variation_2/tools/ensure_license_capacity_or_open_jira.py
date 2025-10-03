from tau_bench.envs.tool import Tool
import json
from typing import Any

class EnsureLicenseCapacityOrOpenJira(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        license_id: str,
        needed_count: int,
        jira_id: str,
        priority: str,
        created_at: str
    ) -> str:
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            payload = {"status": "error", "reason": "license_not_found"}
            out = json.dumps(payload)
            return out
        if (
            inv["used_seats"] + inv["reserved_seats"] + needed_count
            <= inv["total_seats"]
        ):
            payload = {"status": "ok", "capacity": True}
            out = json.dumps(payload)
            return out
        jira = {
            "jira_id": jira_id,
            "issue_type": "License Shortage",
            "summary": f"License shortage for {license_id}",
            "priority": priority,
            "status": "To Do",
            "created_at": created_at,
            "updated_at": created_at,
        }
        _append_row(data["jira_tickets"], jira)
        payload = {"status": "ok", "capacity": False, "jira": jira}
        out = json.dumps(payload)
        return out
        pass
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            payload = {"status": "error", "reason": "license_not_found"}
            out = json.dumps(payload)
            return out
        if (
            inv["used_seats"] + inv["reserved_seats"] + needed_count
            <= inv["total_seats"]
        ):
            payload = {"status": "ok", "capacity": True}
            out = json.dumps(payload)
            return out
        jira = {
            "jira_id": jira_id,
            "issue_type": "License Shortage",
            "summary": f"License shortage for {license_id}",
            "priority": priority,
            "status": "To Do",
            "created_at": created_at,
            "updated_at": created_at,
        }
        _append_row(data["jira_tickets"], jira)
        payload = {"status": "ok", "capacity": False, "jira": jira}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ensureLicenseCapacityOrOpenJira",
                "description": "Check capacity for a license; otherwise create a TaskTrack 'License Shortage'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {"type": "string"},
                        "needed_count": {"type": "integer"},
                        "jira_id": {"type": "string"},
                        "priority": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "license_id",
                        "needed_count",
                        "jira_id",
                        "priority",
                        "created_at",
                    ],
                },
            },
        }
