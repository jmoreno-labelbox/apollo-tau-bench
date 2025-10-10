# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ResolveHourlyRates(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id_list = kwargs.get("project_id_list") or []
        projects = _index_by(list(data.get("projects", {}).values()), "project_id")
        rate_map = {}
        for pid in project_id_list:
            pr = projects.get(pid) or {}
            rate_map[pid] = pr.get("override_hourly_rate") or pr.get("default_hourly_rate") or 0
        return json.dumps({"rate_map": rate_map}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"resolve_hourly_rates",
            "description":"Resolve hourly rate per project (override else default).",
            "parameters":{"type":"object","properties":{"project_id_list":{"type":"array","items":{"type":"string"}}},"required":["project_id_list"]}
        }}
