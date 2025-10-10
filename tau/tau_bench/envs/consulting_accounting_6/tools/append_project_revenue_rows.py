# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AppendProjectRevenueRows(Tool):
    """Insert project revenue rows for a given snapshot."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows_tbl = data.get("project_revenue", [])
        snapshot_id = kwargs.get("snapshot_id")
        items = kwargs.get("items") or []
        inserted = []

        max_id = 0
        for r in rows_tbl:
            try:
                max_id = max(max_id, int(r.get("row_id", 0)))
            except (ValueError, TypeError):
                pass

        for it in items:
            max_id += 1
            rows_tbl.append({
                "row_id": max_id,
                "snapshot_id": snapshot_id,
                "project_id": it.get("project_id"),
                "ytd_revenue": it.get("ytd_revenue")
            })
            inserted.append(max_id)
        return json.dumps({"snapshot_id": snapshot_id, "inserted_row_ids": inserted}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "append_project_revenue_rows",
            "description": "Insert project revenue items for a snapshot.",
            "parameters": {"type": "object", "properties": {
                "snapshot_id": {"type": "string"},
                "items": {"type": "array", "items": {"type": "object"}}
            }, "required": ["snapshot_id", "items"]}
        }}
