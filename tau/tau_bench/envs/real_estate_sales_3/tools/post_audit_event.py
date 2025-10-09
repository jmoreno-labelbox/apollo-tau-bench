from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class PostAuditEvent(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        actor_id: str = None,
        action: str = None,
        entity_type: str = None,
        entity_id: str = None,
        metadata_json: dict = None
    ) -> str:
        audits = data.get("audit_events", [])
        new_id = _next_int_id(audits, "event_id")
        row = {
            "event_id": new_id,
            "actor_id": actor_id,
            "action": action,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "occurred_at": _fixed_now_iso(),
            "metadata_json": metadata_json or {},
        }
        audits.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PostAuditEvent",
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
