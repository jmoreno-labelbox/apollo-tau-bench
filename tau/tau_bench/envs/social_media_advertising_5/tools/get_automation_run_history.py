# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAutomationRunHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_type, status, limit = 10) -> str:
        rtype = run_type
        limit = int(limit)
        runs = list(data.get("automation_runs", {}).values())
        if rtype:
            runs = [r for r in runs if r.get("run_type") == rtype]
        if status:
            runs = [r for r in runs if r.get("status") == status]
        runs.sort(key=lambda x: x.get("started_at", ""), reverse=True)
        runs = runs[:limit]
        total = len(runs)
        succ = len([r for r in runs if r.get("status") == "completed"])
        fail = len([r for r in runs if r.get("status") == "failed"])
        rate = round((succ / total * 100), 2) if total > 0 else 0
        return json.dumps({"summary": {"total_runs": total, "success_count": succ, "failure_count": fail,
                                       "success_rate_percent": rate}, "runs": runs})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_automation_run_history", "description": "Gets automation runs with summary.",
                             "parameters": {"type": "object",
                                            "properties": {"run_type": {"type": "string"}, "status": {"type": "string"},
                                                           "limit": {"type": "number"}}, "required": []}}}
