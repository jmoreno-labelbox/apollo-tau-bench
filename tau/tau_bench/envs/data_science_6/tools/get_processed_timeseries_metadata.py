# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProcessedTimeseriesMetadata(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], csv_path) -> str:
        if not csv_path:
            return json.dumps({"error": "Missing csv_path"})
        items = data.get("processed_timeseries", [])
        for rec in items:
            if rec.get("csv_path") == csv_path:
                return json.dumps({
                    "csv_path": rec.get("csv_path"),
                    "row_count": rec.get("row_count"),
                    "min_timestamp": rec.get("min_timestamp"),
                    "max_timestamp": rec.get("max_timestamp"),
                    "columns": rec.get("columns")
                })
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"get_processed_timeseries_metadata",
                "description":"Returns row_count and metadata for a processed timeseries CSV path.",
                "parameters":{"type":"object","properties":{"csv_path":{"type":"string"}},"required":["csv_path"]}
            }
        }
