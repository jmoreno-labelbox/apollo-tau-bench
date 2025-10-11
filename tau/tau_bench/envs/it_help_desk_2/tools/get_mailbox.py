# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_one(collection: List[Dict[str, Any]], ) -> Optional[Dict[str, Any]]:
    for row in collection:
        if all(row.get(k) == v for k, v in filters.items()):
            return row
    return None

class GetMailbox(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: Optional[str] = None, mailbox_id: Optional[str] = None) -> str:
        mbx = None
        if mailbox_id:
            mbx = _find_one(data["mailboxes"], mailbox_id=mailbox_id)
        elif employee_id:
            mbx = _find_one(data["mailboxes"], employee_id=employee_id)
        return json.dumps({"status": "ok", "mailbox": mbx})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_mailbox",
                "description": "Get a mailbox by employee_id or mailbox_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}, "mailbox_id": {"type": "string"}},
                    "required": [],
                },
            },
        }