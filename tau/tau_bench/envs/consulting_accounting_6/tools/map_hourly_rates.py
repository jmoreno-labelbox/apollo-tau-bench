# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MapHourlyRates(Tool):
    """Resolve hourly rate per project (override → default)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_ids = kwargs.get("project_id_list") or []
        projects = _by_key(list(data.get("projects", {}).values()), "project_id")
        rate_map = {pid: (projects.get(pid, {}).get("override_hourly_rate")
                          or projects.get(pid, {}).get("default_hourly_rate") or 0)
                    for pid in project_ids}
        return json.dumps({"rate_map": rate_map}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "map_hourly_rates",
            "description": "Resolve hourly rate for each project.",
            "parameters": {"type": "object", "properties": {
                "project_id_list": {"type": "array", "items": {"type": "string"}}
            }, "required": ["project_id_list"]}
        }}
