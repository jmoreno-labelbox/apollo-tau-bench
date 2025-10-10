# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ResolveHourlyRate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id) -> str:
        pid = project_id
        proj = next((p for p in list(data.get("projects", {}).values()) if p.get("project_id") == pid), None)
        if not proj:
            return json.dumps({"error": f"Project {pid} not found"}, indent=2)
        rate = proj.get("override_hourly_rate") or proj.get("default_hourly_rate") or 0.0
        return json.dumps({"project_id": pid,"hourly_rate": float(rate)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "resolve_hourly_rate","description": "Return effective hourly rate for a project (override > default).","parameters": {"type": "object","properties": {"project_id": {"type": "string"}},"required": ["project_id"]}}}
