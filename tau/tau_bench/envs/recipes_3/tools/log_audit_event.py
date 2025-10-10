# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogAuditEvent(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        user_id: int,
        entity_type: str,
        entity_id: int,
        action_enum: str,
        payload_json: Dict[str, Any],
    ) -> str:
        tbl = _tbl(data, "audit_logs")
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": str(entity_type),
            "entity_id": int(entity_id),
            "action_enum": str(action_enum),
            "payload_json": payload_json,
            "created_at": "2025-01-03T10:00:00",
        }
        tbl.append(row)
        return _json({"audit_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_audit_event",
                "description": "Append an audit log entry and return audit_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "entity_type": {"type": "string"},
                        "entity_id": {"type": "integer"},
                        "action_enum": {"type": "string"},
                        "payload_json": {"type": "object"},
                    },
                    "required": [
                        "household_id",
                        "user_id",
                        "entity_type",
                        "entity_id",
                        "action_enum",
                    ],
                },
            },
        }
