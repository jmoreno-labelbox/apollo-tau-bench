# Copyright Sierra Inc.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RetrieveWaterLevels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], end, start, station_id) -> str:
        station = station_id
        rows = []
        for r in data.get("water_levels", []) or []:
            if station and r.get("station_id") != station:
                continue
            ts = r.get("timestamp","")
            if start and ts < start: continue
            if end and ts > end: continue
            rows.append(r)
        return json.dumps({"rows": rows}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"fetch_water_levels",
            "description":"Fetch water level rows (optional station/time filters).",
            "parameters":{"type":"object","properties":{
                "station_id":{"type":"string"},
                "start":{"type":"string"},"end":{"type":"string"}
            },"required":[]}
        }}
