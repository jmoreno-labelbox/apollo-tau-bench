# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_one(collection: List[Dict[str, Any]], **filters: Any) -> Optional[Dict[str, Any]]:
    for row in collection:
        if all(row.get(k) == v for k, v in filters.items()):
            return row
    return None

class UpdateMailboxStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], mailbox_id: str, status: str) -> str:
        mbx = _find_one(data["mailboxes"], mailbox_id=mailbox_id)
        if not mbx:
            return json.dumps({"status": "error", "reason": "mailbox_not_found"})
        if status not in {"active", "inactive"}:
            return json.dumps({"status": "error", "reason": "invalid_status"})
        mbx["status"] = status
        return json.dumps({"status": "ok", "mailbox": mbx})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_mailbox_status",
                "description": "Set mailbox status to active or inactive.",
                "parameters": {
                    "type": "object",
                    "properties": {"mailbox_id": {"type": "string"}, "status": {"type": "string"}},
                    "required": ["mailbox_id", "status"],
                },
            },
        }