# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AppendAuditEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], action, actor_id, entity_id, entity_type, metadata_json) -> str:
        audits = data.get("audit_events", [])
        new_id = _next_auto_id(audits, "event_id")
        row = {
            "event_id": new_id,
            "actor_id": actor_id,
            "action": action,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "occurred_at": _now_iso_fixed(),
            "metadata_json": metadata_json or {},
        }
        audits.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_audit_event",
                "description": "Append an audit_events row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {"type": "integer"},
                        "action": {"type": "string"},
                        "entity_type": {"type": "string"},
                        "entity_id": {"type": ["integer", "string"]},
                        "metadata_json": {"type": "object"},
                    },
                    "required": ["actor_id", "action", "entity_type", "entity_id"],
                },
            },
        }
