from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateMailbox(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, upn: str = None) -> str:
        mailboxes = data.setdefault("mailboxes", [])
        mailbox_id = _get_next_id(mailboxes, "mailbox_id", "mbx")
        new_mailbox = {
            "mailbox_id": mailbox_id,
            "employee_id": employee_id,
            "address": upn,
            "status": "active",
            "retention_policy": "std_2y",
            "created_at": FIXED_NOW,
        }
        mailboxes.append(new_mailbox)
        payload = new_mailbox
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createMailbox",
                "description": "Creates an Exchange Online mailbox for a new user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "upn": {"type": "string"},
                    },
                    "required": ["employee_id", "upn"],
                },
            },
        }
