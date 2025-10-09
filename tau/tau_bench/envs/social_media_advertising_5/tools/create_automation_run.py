from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any

class CreateAutomationRun(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        run_id: str = None,
        run_type: str = None,
        started_at: str = None,
        ended_at: str = None,
        status: str = None,
        input_ref: str = None,
        errors_json: str = None
    ) -> str:
        rec = {
            "run_id": run_id,
            "run_type": run_type,
            "started_at": started_at,
            "ended_at": ended_at,
            "status": status,
            "input_ref": input_ref,
            "errors_json": errors_json,
        }
        data.setdefault("automation_runs", []).append(rec)
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAutomationRun",
                "description": "Creates an automation run record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "run_type": {"type": "string"},
                        "started_at": {"type": "string"},
                        "ended_at": {"type": "string"},
                        "status": {"type": "string"},
                        "input_ref": {"type": "string"},
                        "errors_json": {"type": "string"},
                    },
                    "required": [
                        "run_id",
                        "run_type",
                        "started_at",
                        "ended_at",
                        "status",
                        "input_ref",
                        "errors_json",
                    ],
                },
            },
        }
