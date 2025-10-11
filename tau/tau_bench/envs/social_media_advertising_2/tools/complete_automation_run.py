# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CompleteAutomationRun(Tool):
    """End a deterministic automation run; computes duration from provided or defaulted times."""

    @staticmethod
    def invoke(data: Dict[str, Any], ended_at, run_id, started_at, errors_json = {}, outputs_json = {}) -> str:
        run_id: str = run_id
        started_at: str = started_at or _iso_at(current_date, current_time)
        ended_at: str = ended_at or _iso_at(current_date, end_time)
        outputs_json: Dict[str, Any] = outputs_json
        errors_json: Dict[str, Any] = errors_json
        duration_repr = f"{started_at}..{ended_at}"
        status = "success"
        return json.dumps({
            "success": True,
            "run_id": run_id,
            "status": status,
            "started_at": started_at,
            "ended_at": ended_at,
            "duration_repr": duration_repr,
            "outputs_json": outputs_json,
            "errors_json": errors_json
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "complete_automation_run",
                "description": "End a deterministic automation run; echoes start/end and returns a duration representation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "started_at": {
                            "type": "string",
                            "description": "ISO datetime. Defaults to current_date + current_time."
                        },
                        "ended_at": {
                            "type": "string",
                            "description": "ISO datetime. Defaults to current_date + end_time."
                        },
                        "status": {"type": "string"},
                        "outputs_json": {"type": "object"},
                        "errors_json": {"type": "object"}
                    },
                    "required": ["run_id"],
                    "additionalProperties": False
                }
            }
        }
