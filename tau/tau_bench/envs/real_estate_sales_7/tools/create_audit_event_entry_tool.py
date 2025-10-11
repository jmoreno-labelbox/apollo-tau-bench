# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAuditEventEntryTool(Tool):
    """Creates entry in audit_events table for compliance tracking."""

    @staticmethod
    def invoke(data: Dict[str, Any], action, actor_id, entity_id, entity_type, metadata_json) -> str:

        if actor_id is None or not action or not entity_type or entity_id is None:
            return _err("actor_id, action, entity_type, entity_id are required")

        if metadata_json is not None and not isinstance(metadata_json, (dict, list)):
            return _err("metadata_json must be an object or array if provided")

        rows = data.setdefault("audit_events", [])
        event_id = _next_int_id(rows, "event_id")
        rec = {
            "event_id": event_id,
            "actor_id": int(actor_id),
            "action": str(action),
            "entity_type": str(entity_type),
            "entity_id": str(entity_id),
            "occurred_at": HARD_TS,
            "metadata_json": metadata_json if metadata_json is not None else {},
        }
        rows.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_audit_event_entry",
                "description": (
                    "Creates entry in audit_events table for compliance tracking."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {"type": "integer"},
                        "action": {"type": "string"},
                        "entity_type": {"type": "string"},
                        "entity_id": {"type": "string"},
                        "metadata_json": {"type": ["object", "array", "null"]},
                    },
                    "required": ["actor_id", "action", "entity_type", "entity_id"],
                },
            },
        }
