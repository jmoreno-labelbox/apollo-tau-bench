# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProcessedTimeseriesSummary(Tool):
    """
    Retrieves processed_timeseries by csv_path.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], csv_path: str) -> str:
        rows = data.get("processed_timeseries", [])
        for row in rows:
            if row.get("csv_path") == csv_path:
                return json.dumps(row)
        return json.dumps({"error": "processed_timeseries not found", "csv_path": csv_path})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_processed_timeseries_summary",
                "description": "Retrieves processed_timeseries record by csv_path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "csv_path": {"type": "string"}
                    },
                    "required": ["csv_path"]
                }
            }
        }
