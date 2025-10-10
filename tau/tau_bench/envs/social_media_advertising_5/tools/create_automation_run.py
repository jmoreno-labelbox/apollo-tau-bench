# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAutomationRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rec = {"run_id": kwargs.get("run_id"), "run_type": kwargs.get("run_type"),
               "started_at": kwargs.get("started_at"), "ended_at": kwargs.get("ended_at"),
               "status": kwargs.get("status"), "input_ref": kwargs.get("input_ref"),
               "errors_json": kwargs.get("errors_json")}
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
