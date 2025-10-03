from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetMailbox(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str | None = None,
        mailbox_id: str | None = None,
    ) -> str:
        pass
        mbx = None
        if mailbox_id:
            mbx = _find_one(data["mailboxes"], mailbox_id=mailbox_id)
        elif employee_id:
            mbx = _find_one(data["mailboxes"], employee_id=employee_id)
        payload = {"status": "ok", "mailbox": mbx}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMailbox",
                "description": "Get a mailbox by employee_id or mailbox_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "mailbox_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
