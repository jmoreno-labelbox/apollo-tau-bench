# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchProcessedTimeseries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], end, series_name, start) -> str:
        name = series_name
        rows = []
        for r in data.get("processed_timeseries", []) or []:
            if name and r.get("series_name") != name:
                continue
            ts = r.get("timestamp","")
            if start and ts < start: continue
            if end and ts > end: continue
            rows.append(r)
        return json.dumps({"series_name": name, "rows": rows}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_processed_timeseries",
            "description":"Read processed timeseries rows by series_name and optional time range.",
            "parameters":{"type":"object","properties":{
                "series_name":{"type":"string"},
                "start":{"type":"string"},"end":{"type":"string"}
            },"required":["series_name"]}
        }}
