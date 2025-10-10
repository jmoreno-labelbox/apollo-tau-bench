# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PostAuditEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        audits = data.get("audit_events", [])
        new_id = _next_int_id(audits, "event_id")
        row = {
            "event_id": new_id,
            "actor_id": kwargs.get("actor_id"),
            "action": kwargs.get("action"),
            "entity_type": kwargs.get("entity_type"),
            "entity_id": kwargs.get("entity_id"),
            "occurred_at": _fixed_now_iso(),
            "metadata_json": kwargs.get("metadata_json") or {}
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
