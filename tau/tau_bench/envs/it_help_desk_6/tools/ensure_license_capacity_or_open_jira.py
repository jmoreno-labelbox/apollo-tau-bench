# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EnsureLicenseCapacityOrOpenJira(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        license_id: str,
        needed_count: int,
        jira_id: str,
        priority: str,
        created_at: str,
    ) -> str:
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            return json.dumps({"status": "error", "reason": "license_not_found"})
        if inv["used_seats"] + inv["reserved_seats"] + needed_count <= inv["total_seats"]:
            return json.dumps({"status": "ok", "capacity": True})
        # Access Jira and mark the issue as blocked.
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
        return json.dumps({"status": "ok", "capacity": False, "jira": jira})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ensure_license_capacity_or_open_jira",
                "description": "Check capacity for a license; otherwise create a Jira 'License Shortage'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {"type": "string"},
                        "needed_count": {"type": "integer"},
                        "jira_id": {"type": "string"},
                        "priority": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["license_id", "needed_count", "jira_id", "priority", "created_at"],
                },
            },
        }
