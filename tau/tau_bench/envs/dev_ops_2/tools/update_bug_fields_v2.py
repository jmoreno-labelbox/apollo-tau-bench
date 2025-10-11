# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateBugFieldsV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ticket_key: str, fields: Dict[str, Any]) -> str:
        work_items = _get_table(data, "work_items")
        item = next((w for w in work_items if w.get("ticket_key") == ticket_key or w.get("id") == ticket_key), None)
        if not item:
            return _error(f"Ticket '{ticket_key}' not found.")
        item.update(fields or {})
        return json.dumps({"updated": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_bug_fields_v2", "description": "Updates fields on a ticket deterministically.", "parameters": {"type": "object", "properties": {"ticket_key": {"type": "string"}, "fields": {"type": "object"}}, "required": ["ticket_key", "fields"]}}}
