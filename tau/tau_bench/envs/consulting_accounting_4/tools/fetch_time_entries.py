# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchTimeEntries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], period_end, period_start, project_id_list) -> str:
        prj_ids = set(project_id_list or [])
        start = period_start
        end = period_end
        rows = []
        for t in data.get("time_entries", []) or []:
            if prj_ids and t.get("project_id") not in prj_ids:
                continue
            if start and t.get("entry_date","") < start:
                continue
            if end and t.get("entry_date","") > end:
                continue
            rows.append(t)
        return json.dumps({"rows": rows}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"fetch_time_entries",
            "description":"Fetch time entries by project(s) and period.",
            "parameters":{"type":"object","properties":{
                "project_id_list":{"type":"array","items":{"type":"string"}},
                "period_start":{"type":"string"},
                "period_end":{"type":"string"}
            },"required":["project_id_list","period_start","period_end"]}
        }}
