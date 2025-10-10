# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EventsAtAirportOn(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], airport_id: str, date: str) -> str:
        out=[]
        for e in data.get("operational_events", []):
            ap=(e.get("airport") or {}).get("airport_id")
            ts=e.get("event_timestamp_utc","")
            if ap==airport_id and isinstance(ts,str) and ts[:10]==date:
                out.append(e)
        return _j(out)

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"events_at_airport_on",
            "description":"Return operational events at an airport on a date (UTC) for verification.",
            "parameters":{"type":"object","properties":{
                "airport_id":{"type":"string"},
                "date":{"type":"string"}
            },"required":["airport_id","date"]}
        }}
