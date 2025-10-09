from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class CreateAuditEventEntryTool(Tool):
    """Inserts a record into the audit_events table for compliance monitoring."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        actor_id: int = None,
        action: str = None,
        entity_type: str = None,
        entity_id: str = None,
        metadata_json: Any = None
    ) -> str:
        if actor_id is None or not action or not entity_type or entity_id is None:
            return _err("actor_id, action, entity_type, entity_id are required")

        if metadata_json is not None and not isinstance(metadata_json, (dict, list)):
            return _err("metadata_json must be an object WA array if provided")

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
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAuditEventEntry",
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
                        "metadata_json": {
                            "oneOf": [
                                {"type": "object"},
                                {"type": "array", "items": {"type": "object"}},
                                {"type": "null"}
                            ]
                        },
                    },
                    "required": ["actor_id", "action", "entity_type", "entity_id"],
                },
            },
        }
