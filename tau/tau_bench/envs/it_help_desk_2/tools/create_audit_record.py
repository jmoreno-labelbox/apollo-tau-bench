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

class CreateAuditRecord(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], details, event, lifecycle_id, actor = "SYSTEM", timestamp = FIXED_NOW) -> str:
        audit_table = data.setdefault("lifecycle_audit", [])
        audit_id = _get_next_id(audit_table, "audit_id", "lcaud")
        audit_table.append({"audit_id": audit_id, "lifecycle_id": lifecycle_id, "event": event, "details": details, "timestamp": timestamp, "actor": actor})
        return json.dumps({"status": "success", "event_logged": event}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_audit_record", "description": "Create a deterministic record in the lifecycle audit log.", "parameters": {"type": "object", "properties": {"lifecycle_id": {"type": "string"}, "event": {"type": "string"}, "details": {"type": "object"}, "actor": {"type": "string"}, "timestamp": {"type": "string"}}, "required": ["lifecycle_id", "event", "details", "actor", "timestamp"]}}}