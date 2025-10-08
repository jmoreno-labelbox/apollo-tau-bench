from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateMailbox(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        mailbox_id: str,
        employee_id: str,
        address: str,
        retention_policy: str,
        created_at: str,
        status: str = "active",
    ) -> str:
        pass
        if retention_policy not in {"std_2y", "finance_7y"}:
            payload = {"status": "error", "reason": "invalid_retention"}
            out = json.dumps(payload)
            return out
        row = {
            "mailbox_id": mailbox_id,
            "employee_id": employee_id,
            "address": address,
            "status": status,
            "retention_policy": retention_policy,
            "created_at": created_at,
        }
        _append_row(data["mailboxes"], row)
        payload = {"status": "ok", "mailbox": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMailbox",
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
                    "required": [
                        "mailbox_id",
                        "employee_id",
                        "address",
                        "retention_policy",
                        "created_at",
                    ],
                },
            },
        }
