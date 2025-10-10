# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class record_automation_run(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], task_name: str, status: str, started_at: str, ended_at: str, timestamp: str, request_id: str) -> str:
        runs = _table(data, "automation_runs")
        run_id = _id_from_request("run", request_id)
        if run_id:
            for r in runs:
                if isinstance(r, dict) and r.get("run_id") == run_id:
                    return json.dumps(r, indent=2)
        row = {
            "run_id": run_id or _get_next_id("run", [r.get("run_id", "") for r in runs if isinstance(r, dict)]),
            "task_name": task_name,
            "status": status,
            "started_at": started_at,
            "ended_at": ended_at,
            "day": _ymd(timestamp),
        }
        runs.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"record_automation_run","description":"Record/reuse a deterministic automation run row (run_<request_id>).","parameters":{"type":"object","properties":{"task_name":{"type":"string"},"status":{"type":"string"},"started_at":{"type":"string"},"ended_at":{"type":"string"},"timestamp":{"type":"string"},"request_id":{"type":"string"}},"required":["task_name","status","started_at","ended_at","timestamp","request_id"]}}}
