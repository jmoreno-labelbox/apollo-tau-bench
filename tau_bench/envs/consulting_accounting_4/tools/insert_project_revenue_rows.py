from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class InsertProjectRevenueRows(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], snapshot_id: int = None, items: list = None) -> str:
        rows_tbl = data.get("project_revenue", [])
        items = items or []
        inserted = []

        max_id = 0
        for r in rows_tbl:
            try:
                row_id = int(r.get("row_id", 0))
                if row_id > max_id:
                    max_id = row_id
            except (ValueError, TypeError):
                continue

        for it in items:
            max_id += 1
            rid = max_id
            rows_tbl.append(
                {
                    "row_id": rid,
                    "snapshot_id": snapshot_id,
                    "project_id": it.get("project_id"),
                    "ytd_revenue": it.get("ytd_revenue"),
                }
            )
            inserted.append(rid)
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
                "name": "insertProjectRevenueRows",
                "description": "Insert project revenue rows for a snapshot.",
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
