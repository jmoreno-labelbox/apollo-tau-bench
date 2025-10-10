# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class StartAutomationRun(Tool):
    """Start a deterministic automation run; the caller provides all timestamps/refs, with plan-date defaults."""
    @staticmethod
    def invoke(data: Dict[str, Any], run_type, started_at, input_ref = {}) -> str:
        run_type: str = run_type
        started_at: str = started_at or _iso_at(current_date, current_time)
        input_ref: Dict[str, Any] = input_ref
        run_id = "run_" + current_date
        return json.dumps({
            "success": True,
            "run_id": run_id,
            "run_type": run_type,
            "started_at": started_at,
            "input_ref": input_ref
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "start_automation_run",
                "description": "Start a deterministic automation run; returns run_id derived from the plan date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_type": {"type": "string"},
                        "started_at": {
                            "type": "string",
                            "description": "ISO datetime. Defaults to current_date + current_time."
                        },
                        "input_ref": {"type": "object", "description": "Reference blob (plan_id, date, etc.)"}
                    },
                    "required": ["run_type"],
                    "additionalProperties": False
                }
            }
        }
