from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class WriteProcessedSeries(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], series_name: str = None, items: list = None) -> str:
        table = data.get("processed_timeseries", [])
        items = items or []
        inserted = []
        max_id = 0
        for r in table:
            try:
                rid = int(r.get("row_id", 0))
                if rid > max_id:
                    max_id = rid
            except (ValueError, TypeError):
                continue
        for it in items:
            max_id += 1
            rid = max_id
            row = {
                "row_id": rid,
                "series_name": series_name,
                "timestamp": it.get("timestamp"),
                "value": it.get("value"),
                "source": it.get("source"),
            }
            table.append(row)
            inserted.append(rid)
        payload = {"series_name": series_name, "inserted_row_ids": inserted}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteProcessedSeries",
                "description": "Insert derived/processed time-series points.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "series_name": {"type": "string"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["series_name", "items"],
                },
            },
        }
