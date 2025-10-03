from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class CompleteAutomationRun(Tool):
    """Conclude a consistent automation run; calculates duration based on supplied or default times."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        run_id: str,
        started_at: str = None,
        ended_at: str = None,
        outputs_json: dict[str, Any] = None,
        errors_json: dict[str, Any] = None
,
    status: Any = None,
    ) -> str:
        started_at = started_at or _iso_at(current_date, current_time)
        ended_at = ended_at or _iso_at(current_date, end_time)
        outputs_json = outputs_json or {}
        errors_json = errors_json or {}
        duration_repr = f"{started_at}..{ended_at}"
        status = "success"
        payload = {
            "success": True,
            "run_id": run_id,
            "status": status,
            "started_at": started_at,
            "ended_at": ended_at,
            "duration_repr": duration_repr,
            "outputs_json": outputs_json,
            "errors_json": errors_json,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CompleteAutomationRun",
                "description": "End a deterministic automation run; echoes start/end and returns a duration representation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "started_at": {
                            "type": "string",
                            "description": "ISO datetime. Defaults to current_date + current_time.",
                        },
                        "ended_at": {
                            "type": "string",
                            "description": "ISO datetime. Defaults to current_date + end_time.",
                        },
                        "status": {"type": "string"},
                        "outputs_json": {"type": "object"},
                        "errors_json": {"type": "object"},
                    },
                    "required": ["run_id"],
                    "additionalProperties": False,
                },
            },
        }
