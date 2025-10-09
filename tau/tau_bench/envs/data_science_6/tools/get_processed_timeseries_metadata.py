from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetProcessedTimeseriesMetadata(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], csv_path: str = None) -> str:
        if not csv_path:
            payload = {"error": "Missing csv_path"}
            out = json.dumps(payload)
            return out
        items = data.get("processed_timeseries", {}).values()
        for rec in items.values():
            if rec.get("csv_path") == csv_path:
                payload = {
                        "csv_path": rec.get("csv_path"),
                        "row_count": rec.get("row_count"),
                        "min_timestamp": rec.get("min_timestamp"),
                        "max_timestamp": rec.get("max_timestamp"),
                        "columns": rec.get("columns"),
                    }
                out = json.dumps(
                    payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProcessedTimeseriesMetadata",
                "description": "Returns row_count and metadata for a processed timeseries CSV path.",
                "parameters": {
                    "type": "object",
                    "properties": {"csv_path": {"type": "string"}},
                    "required": ["csv_path"],
                },
            },
        }
