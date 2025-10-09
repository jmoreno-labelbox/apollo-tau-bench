from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FetchBrokerDetailsTool(Tool):
    """Retrieves broker details for coordinating workflows."""

    @staticmethod
    def invoke(data: dict[str, Any], broker_id: int = None) -> str:
        broker_id = _as_int(broker_id)
        if broker_id is None:
            return _err("broker_id (int) is required")

        rec = next(
            (
                b
                for b in data.get("brokers", {}).values()
                if _as_int(b.get("broker_id")) == broker_id
            ),
            None,
        )
        if not rec:
            return _err(f"broker_id {broker_id} not found", code="not_found")

        out = {
            "broker_id": broker_id,
            "name": rec.get("name"),
            "email": rec.get("email"),
            "phone": rec.get("phone"),
            "office_location": rec.get("office_location"),
            "calendar_uri": rec.get("calendar_uri"),
            "active": bool(rec.get("active", False)),
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetchBrokerDetails",
                "description": "Gets broker information for workflow coordination.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "broker_id": {"type": "integer"},
                    },
                    "required": ["broker_id"],
                },
            },
        }
