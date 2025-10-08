from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class RecordAutomationRun(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_type: str = None, started_at: str = None, ended_at: str = None, status: str = None, input_ref: str = None, outputs_json: dict = None, errors_json: dict = None, request_id: str = None) -> str:
        pass
        _ensure_list(data, "automation_runs")
        row = {
            "run_type": run_type,
            "started_at": started_at,
            "ended_at": ended_at,
            "status": status,
            "input_ref": input_ref,
            "outputs_json": outputs_json,
            "errors_json": errors_json,
        }
        #try:
        #t0 = datetime.fromisoformat(row["started_at"].replace("Z","+00:00"))
        #t1 = datetime.fromisoformat(row["ended_at"].replace("Z","+00:00"))
        #row["duration_ms"] = int((t1 - t0).total_seconds()*1000)
        #except Exception:
        #row["duration_ms"] = None
        data["automation_runs"].append(row)
        payload = row
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordAutomationRun",
                "description": "Append an automation run log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_type": {"type": "string"},
                        "started_at": {"type": "string"},
                        "ended_at": {"type": "string"},
                        "status": {"type": "string"},
                        "input_ref": {"type": "string"},
                        "outputs_json": {"type": "object"},
                        "errors_json": {"type": ["object", "null"]},
                    },
                    "required": [
                        "run_type",
                        "started_at",
                        "ended_at",
                        "status",
                        "input_ref",
                        "outputs_json",
                    ],
                },
            },
        }
