from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetProcessedTimeseriesSummary(Tool):
    """Fetches processed_timeseries using csv_path."""

    @staticmethod
    def invoke(data: dict[str, Any], csv_path: str) -> str:
        rows = data.get("processed_timeseries", {}).values()
        for row in rows:
            if row.get("csv_path") == csv_path:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {"error": "processed_timeseries not found", "csv_path": csv_path}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProcessedTimeseriesSummary",
                "description": "Retrieves processed_timeseries record by csv_path.",
                "parameters": {
                    "type": "object",
                    "properties": {"csv_path": {"type": "string"}},
                    "required": ["csv_path"],
                },
            },
        }
