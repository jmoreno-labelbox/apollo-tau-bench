# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAutomationRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ended_at, errors_json, input_ref, run_id, run_type, started_at, status) -> str:
        rec = {"run_id": run_id, "run_type": run_type,
               "started_at": started_at, "ended_at": ended_at,
               "status": status, "input_ref": input_ref,
               "errors_json": errors_json}
        data.setdefault("automation_runs", []).append(rec)
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "create_automation_run", "description": "Creates an automation run record.",
                             "parameters": {"type": "object",
                                            "properties": {"run_id": {"type": "string"}, "run_type": {"type": "string"},
                                                           "started_at": {"type": "string"},
                                                           "ended_at": {"type": "string"}, "status": {"type": "string"},
                                                           "input_ref": {"type": "string"},
                                                           "errors_json": {"type": "string"}},
                                            "required": ["run_id", "run_type", "started_at", "ended_at", "status",
                                                         "input_ref", "errors_json"]}}}
