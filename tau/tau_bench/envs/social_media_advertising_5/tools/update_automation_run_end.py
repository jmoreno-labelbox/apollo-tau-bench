# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAutomationRunEnd(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ended_at, run_id, status) -> str:
        rid = run_id
        st = status
        ea = ended_at
        for r in list(data.get("automation_runs", {}).values()):
            if r.get("run_id") == rid:
                r["status"] = st
                r["ended_at"] = ea
                return json.dumps(r)
        return json.dumps({"error": f"run {rid} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_automation_run_end",
                                                 "description": "Sets final status and end time for a run.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"run_id": {"type": "string"},
                                                                               "status": {"type": "string"},
                                                                               "ended_at": {"type": "string"}},
                                                                "required": ["run_id", "status", "ended_at"]}}}
