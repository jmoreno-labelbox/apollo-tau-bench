# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_next_id(table: List[Dict[str, Any]], key: str, prefix: str) -> str:
    if not table:
        return f"{prefix}_00001"
    max_id = 0
    for item in table:
        try:
            num = int(item[key].split('_')[-1])
            if num > max_id:
                max_id = num
        except (ValueError, IndexError):
            continue
    return f"{prefix}_{max_id + 1:05d}"

class CreateMailbox(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id, upn) -> str:
        mailboxes = data.setdefault("mailboxes", [])
        mailbox_id = _get_next_id(mailboxes, "mailbox_id", "mbx")
        new_mailbox = {"mailbox_id": mailbox_id, "employee_id": employee_id, "address": upn, "status": "active", "retention_policy": "std_2y", "created_at": FIXED_NOW}
        mailboxes.append(new_mailbox)
        return json.dumps(new_mailbox, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_mailbox", "description": "Creates an Exchange Online mailbox for a new user.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}, "upn": {"type": "string"}}, "required": ["employee_id", "upn"]}}}