# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsertProjectRevenueRows(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows_tbl = data.get("project_revenue", [])
        snapshot_id = kwargs.get("snapshot_id")
        items = kwargs.get("items") or []
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
            rows_tbl.append({"row_id": rid, "snapshot_id": snapshot_id, "project_id": it.get("project_id"), "ytd_revenue": it.get("ytd_revenue")})
            inserted.append(rid)
        return json.dumps({"snapshot_id": snapshot_id, "inserted_row_ids": inserted}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"insert_project_revenue_rows",
            "description":"Insert project revenue rows for a snapshot.",
            "parameters":{"type":"object","properties":{
                "snapshot_id":{"type":"string"},
                "items":{"type":"array","items":{"type":"object"}}
            },"required":["snapshot_id","items"]}
        }}
