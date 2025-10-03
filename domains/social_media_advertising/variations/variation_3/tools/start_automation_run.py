from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class StartAutomationRun(Tool):
    """Initiate a deterministic automation process; the caller supplies all timestamps/refs, using plan-date defaults."""

    @staticmethod
    def invoke(data: dict[str, Any], run_type: str, started_at: str = None, input_ref: dict[str, Any] = None) -> str:
        if started_at is None:
            started_at = _iso_at(current_date, current_time)
        if input_ref is None:
            input_ref = {}
        run_id = "run_" + current_date
        payload = {
            "success": True,
            "run_id": run_id,
            "run_type": run_type,
            "started_at": started_at,
            "input_ref": input_ref,
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
                "name": "StartAutomationRun",
                "description": "Start a deterministic automation run; returns run_id derived from the plan date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_type": {"type": "string"},
                        "started_at": {
                            "type": "string",
                            "description": "ISO datetime. Defaults to current_date + current_time.",
                        },
                        "input_ref": {
                            "type": "object",
                            "description": "Reference blob (plan_id, date, etc.)",
                        },
                    },
                    "required": ["run_type"],
                    "additionalProperties": False,
                },
            },
        }
