# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOperationalEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], airport_id: str, event_type: str, details: str, event_timestamp_utc: str, aircraft_id: Optional[str]=None) -> str:
        events = data.setdefault("operational_events", [])
        new_id = _next_numeric_suffix("OE", events, "event_id")
        rec = {
            "event_id": new_id,
            "aircraft": {"aircraft_id": aircraft_id} if aircraft_id else None,
            "airport": {"airport_id": airport_id},
            "event_type": event_type,
            "event_timestamp_utc": event_timestamp_utc or "2025-01-05T09:00:00Z",
            "status": "Logged",
            "details": details
        }
        events.append(rec)
        return _j(rec)

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"create_operational_event",
            "description":"Append an operational event; deterministic ID (OE###); ",
            "parameters":{"type":"object","properties":{
                "airport_id":{"type":"string"},
                "event_type":{"type":"string"},
                "details":{"type":"string"},
                "event_timestamp_utc":{"type":"string"},
                "aircraft_id":{"type":"string"},
            },"required":["airport_id","event_type","details","event_timestamp_utc"]}
        }}
