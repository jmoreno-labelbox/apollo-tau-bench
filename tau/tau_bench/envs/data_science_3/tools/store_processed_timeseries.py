# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class StoreProcessedTimeseries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], items, series_name) -> str:
        table = data.get("processed_timeseries", [])
        items = items or []
        inserted = []
        max_id = 0
        for r in table:
            try:
                rid = int(r.get("row_id", 0))
                if rid > max_id: max_id = rid
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
                "source": it.get("source")
            }
            table.append(row)
            inserted.append(rid)
        return json.dumps({"series_name": series_name, "inserted_row_ids": inserted}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"insert_processed_timeseries",
            "description":"Insert processed timeseries points for a named series.",
            "parameters":{"type":"object","properties":{
                "series_name":{"type":"string"},
                "items":{"type":"array","items":{"type":"object"}}
            },"required":["series_name","items"]}
        }}
