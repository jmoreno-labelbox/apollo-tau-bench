# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _err(msg: str, code: str = "bad_request", **extra) -> str:
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

def _as_int(x) -> Optional[int]:
    try:
        return int(x)
    except Exception:
        return None

class FetchBrokerDetailsTool(Tool):
    """Gets broker information for workflow coordination."""

    @staticmethod
    def invoke(data: Dict[str, Any], broker_id) -> str:
        broker_id = _as_int(broker_id)
        if broker_id is None:
            return _err("broker_id (int) is required")

        rec = next(
            (
                b
                for b in data.get("brokers", [])
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
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_broker_details",
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