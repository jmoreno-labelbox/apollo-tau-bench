# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _ensure_list(data: Dict[str, Any], key: str):
    if key not in data or not isinstance(data[key], list):
        data[key] = []

class RecordAutomationRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        _ensure_list(data, "automation_runs")
        row = dict(kwargs)
        # attempt:
        # t0 = datetime.fromisoformat(row["started_at"].replace("Z", "+00:00"))
        # t1 = datetime.fromisoformat(row["ended_at"].replace("Z", "+00:00"))
        # row["duration_ms"] = int((t1 - t0).total_seconds() * 1000)
        # catch Exception:
        # row["duration_ms"] = null
        data["automation_runs"].append(row)
        return json.dumps(row)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "record_automation_run", "description": "Append an automation run log entry.",
                             "parameters": {"type": "object", "properties": {"run_type": {"type": "string"},
                                                                             "started_at": {"type": "string"},
                                                                             "ended_at": {"type": "string"},
                                                                             "status": {"type": "string"},
                                                                             "input_ref": {"type": "string"},
                                                                             "outputs_json": {"type": "object"},
                                                                             "errors_json": {
                                                                                 "type": ["object", "null"]}},
                                            "required": ["run_type", "started_at", "ended_at", "status", "input_ref",
                                                         "outputs_json"]}}}