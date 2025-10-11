# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso
from . import _next_int_id






def _next_int_id(rows: List[Dict[str, Any]], key: str) -> int:
    return max((int(r.get(key, 0)) for r in rows), default=0) + 1

def _fixed_now_iso() -> str:
    return "2025-08-20T00:00:00Z"

class PostAuditEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], action, actor_id, entity_id, entity_type, metadata_json) -> str:
        audits = data.get("audit_events", [])
        new_id = _next_int_id(audits, "event_id")
        row = {
            "event_id": new_id,
            "actor_id": actor_id,
            "action": action,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "occurred_at": _fixed_now_iso(),
            "metadata_json": metadata_json or {}
        }
        audits.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"post_audit_event",
            "description":"Append an audit_events row.",
            "parameters":{"type":"object","properties":{
                "actor_id":{"type":"integer"},"action":{"type":"string"},
                "entity_type":{"type":"string"},"entity_id":{"type":["integer","string"]},
                "metadata_json":{"type":"object"}
            },"required":["actor_id","action","entity_type","entity_id"]}
        }}