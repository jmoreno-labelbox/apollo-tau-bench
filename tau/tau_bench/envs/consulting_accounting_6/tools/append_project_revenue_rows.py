from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AppendProjectRevenueRows(Tool):
    """Add project revenue entries for a specific snapshot."""

    @staticmethod
    def invoke(data: dict[str, Any], snapshot_id: str = None, items: list = None) -> str:
        rows_tbl = data.get("project_revenue", {}).values()
        items = items or []
        inserted = []

        max_id = 0
        for r in rows_tbl:
            try:
                max_id = max(max_id, int(r.get("row_id", 0)))
            except (ValueError, TypeError):
                pass

        for it in items:
            max_id += 1
            rows_tbl.append(
                {
                    "row_id": max_id,
                    "snapshot_id": snapshot_id,
                    "project_id": it.get("project_id"),
                    "ytd_revenue": it.get("ytd_revenue"),
                }
            )
            inserted.append(max_id)
        payload = {"snapshot_id": snapshot_id, "inserted_row_ids": inserted}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "appendProjectRevenueRows",
                "description": "Insert project revenue items for a snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["snapshot_id", "items"],
                },
            },
        }
