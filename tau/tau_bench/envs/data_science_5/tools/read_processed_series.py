# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadProcessedSeries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("series_name")
        start = kwargs.get("start")
        end = kwargs.get("end")
        rows = []
        for r in list(data.get("processed_timeseries", {}).values()) or []:
            if name and r.get("series_name") != name:
                continue
            ts = r.get("timestamp", "")
            if start and ts < start:
                continue
            if end and ts > end:
                continue
            rows.append(r)
        return json.dumps({"series_name": name, "rows": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_processed_series",
            "description": "Read processed series rows by name and optional range.",
            "parameters": {"type": "object", "properties": {
                "series_name": {"type": "string"},
                "start": {"type": "string"},
                "end": {"type": "string"}
            }, "required": ["series_name"]}
        }}
