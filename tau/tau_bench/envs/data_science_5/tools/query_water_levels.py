# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class QueryWaterLevels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        station = kwargs.get("station_id")
        start = kwargs.get("start")
        end = kwargs.get("end")
        out = []
        for r in list(data.get("water_levels", {}).values()) or []:
            if station and r.get("station_id") != station:
                continue
            ts = r.get("timestamp", "")
            if start and ts < start:
                continue
            if end and ts > end:
                continue
            out.append(r)
        return json.dumps({"rows": out}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "query_water_levels",
            "description": "Read observed water-level rows (optional station/time filters).",
            "parameters": {"type": "object", "properties": {
                "station_id": {"type": "string"},
                "start": {"type": "string"},
                "end": {"type": "string"}
            }, "required": []}
        }}
