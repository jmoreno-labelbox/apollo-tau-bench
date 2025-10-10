# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsertMonthlyRevenueRows(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows_tbl = data.get("monthly_revenue", [])
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
            rows_tbl.append({"row_id": rid, "snapshot_id": snapshot_id, "month_year": it.get("month_year"),
                                "revenue": it.get("revenue"), "tax_reserve": it.get("tax_reserve"),
                                "profit_flag": it.get("profit_flag")})
            inserted.append(rid)
        return json.dumps({"snapshot_id": snapshot_id, "inserted_row_ids": inserted}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"insert_monthly_revenue_rows",
            "description":"Insert monthly revenue rows for a snapshot.",
            "parameters":{"type":"object","properties":{
                "snapshot_id":{"type":"string"},
                "items":{"type":"array","items":{"type":"object"}}
            },"required":["snapshot_id","items"]}
        }}
