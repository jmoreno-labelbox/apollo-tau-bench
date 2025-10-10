# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _max_id, _json_dump


class LogAuditEvent(Tool):
    """Insert an audit_logs row with deterministic timestamp; returns audit_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        user_id = kwargs.get("user_id")
        entity_type = kwargs.get("entity_type")
        entity_id = kwargs.get("entity_id")
        action_enum = kwargs.get("action_enum")
        payload_json = kwargs.get("payload_json", {})
        if household_id is None or user_id is None or not entity_type or entity_id is None or not action_enum:
            return _json_dump({"error": "household_id, user_id, entity_type, entity_id, action_enum are required"})
        tbl = data.setdefault("audit_logs", [])
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": str(entity_type),
            "entity_id": int(entity_id),
            "action_enum": str(action_enum),
            "payload_json": payload_json,
            "created_at": "2025-01-03T10:00:00Z"
        }
        tbl.append(row)
        return _json_dump({"audit_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"log_audit_event",
            "description":"Append an audit log entry with a deterministic timestamp.",
            "parameters":{"type":"object","properties":{
                "household_id":{"type":"integer"},
                "user_id":{"type":"integer"},
                "entity_type":{"type":"string"},
                "entity_id":{"type":"integer"},
                "action_enum":{"type":"string"},
                "payload_json":{"type":"object"}
            },"required":["household_id","user_id","entity_type","entity_id","action_enum"]}
        }}
