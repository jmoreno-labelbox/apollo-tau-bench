from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateMailboxStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], mailbox_id: str, status: str) -> str:
        pass
        mbx = _find_one(data["mailboxes"], mailbox_id=mailbox_id)
        if not mbx:
            payload = {"status": "error", "reason": "mailbox_not_found"}
            out = json.dumps(payload)
            return out
        if status not in {"active", "inactive"}:
            payload = {"status": "error", "reason": "invalid_status"}
            out = json.dumps(payload)
            return out
        mbx["status"] = status
        payload = {"status": "ok", "mailbox": mbx}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateMailboxStatus",
                "description": "Set mailbox status to active or inactive.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mailbox_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["mailbox_id", "status"],
                },
            },
        }
