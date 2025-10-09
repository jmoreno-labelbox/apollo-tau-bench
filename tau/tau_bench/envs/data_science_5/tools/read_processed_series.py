from tau_bench.envs.tool import Tool
import json
from typing import Any

class ReadProcessedSeries(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], series_name: str = None, start: str = None, end: str = None) -> str:
        rows = []
        for r in data.get("processed_timeseries", []) or []:
            if series_name and r.get("series_name") != series_name:
                continue
            ts = r.get("timestamp", "")
            if start and ts < start:
                continue
            if end and ts > end:
                continue
            rows.append(r)
        payload = {"series_name": series_name, "rows": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReadProcessedSeries",
                "description": "Read processed series rows by name and optional range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "series_name": {"type": "string"},
                        "start": {"type": "string"},
                        "end": {"type": "string"},
                    },
                    "required": ["series_name"],
                },
            },
        }
