# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLastSuccessfulRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_type) -> str:
        rtype = run_type
        runs = [r for r in list(data.get("automation_runs", {}).values()) if
                r.get("run_type") == rtype and r.get("status") == "completed"]
        if not runs:
            return json.dumps({"error": f"no successful run for {rtype}"})
        last = max(runs, key=lambda x: x.get("ended_at", ""))
        return json.dumps(last)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_last_successful_run",
                                                 "description": "Gets most recent successful run of a type.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"run_type": {"type": "string"}},
                                                                "required": ["run_type"]}}}
