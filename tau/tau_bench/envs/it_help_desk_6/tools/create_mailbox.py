# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _append_row(table: List[Dict[str, Any]], row: Dict[str, Any]) -> None:
    table.append(row)

class CreateMailbox(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        mailbox_id: str,
        employee_id: str,
        address: str,
        retention_policy: str,
        created_at: str,
        status: str = "active",
    ) -> str:
        if retention_policy not in {"std_2y", "finance_7y"}:
            return json.dumps({"status": "error", "reason": "invalid_retention"})
        row = {
            "mailbox_id": mailbox_id,
            "employee_id": employee_id,
            "address": address,
            "status": status,
            "retention_policy": retention_policy,
            "created_at": created_at,
        }
        _append_row(data["mailboxes"], row)
        return json.dumps({"status": "ok", "mailbox": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_mailbox",
                "description": "Create a mailbox with a fixed retention policy and status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mailbox_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "address": {"type": "string"},
                        "retention_policy": {"type": "string"},
                        "created_at": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["mailbox_id", "employee_id", "address", "retention_policy", "created_at"],
                },
            },
        }