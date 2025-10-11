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

class AddMemoToLifecycleQueue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], event_type, hr_id, memo_id) -> str:
        queue = data.setdefault("lifecycle_queue", [])
        lifecycle_id = _get_next_id(queue, "lifecycle_id", "lcq")
        new_entry = {"lifecycle_id": lifecycle_id, "memo_id": memo_id, "employee_ref": hr_id, "event": event_type, "status": "queued", "created_at": FIXED_NOW}
        queue.append(new_entry)
        return json.dumps(new_entry, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "add_memo_to_lifecycle_queue", "description": "Adds a new memo to the lifecycle queue to initiate a process like onboarding or offboarding.", "parameters": {"type": "object", "properties": {"memo_id": {"type": "string"}, "hr_id": {"type": "string"}, "event_type": {"type": "string"}}, "required": ["memo_id", "hr_id", "event_type"]}}}