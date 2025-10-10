# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CompleteAutomationRun(Tool):
    """Complete a previously started automation run with deterministic duration."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        automation_run_id = kwargs.get("automation_run_id")
        status = kwargs.get("status")
        outputs_json = kwargs.get("outputs_json", {})

        runs = data.get("automation_runs", [])
        idx = _idx_by_id(runs, automation_run_id)
        if idx is None:
            runs.append({
                "id": automation_run_id,
                "automation_type": "build_triage",
                "input_ref": "",
                "status": "running",
                "started_at": FIXED_NOW,
                "ended_at": None,
                "duration_ms": 0,
                "outputs_json": {},
                "errors_json": None
            })
            idx = len(runs) - 1

        run = runs[idx]
        if run["started_at"] == "2025-01-27T12:30:00Z":
            ended_at = "2025-01-27T12:35:00Z"
            duration_ms = DEFAULT_AUTOMATION_DURATION_MS
        else:
            ended_at = "2025-01-27T12:35:00Z"
            duration_ms = DEFAULT_AUTOMATION_DURATION_MS

        run.update({
            "status": status,
            "ended_at": ended_at,
            "duration_ms": duration_ms,
            "outputs_json": outputs_json
        })
        runs[idx] = run
        return json.dumps({"automation_run": run}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "complete_automation_run",
                "description": "Mark automation run as completed/failed and compute deterministic duration.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "automation_run_id": {"type": "string"},
                        "status": {"type": "string", "enum": ["completed", "failed", "cancelled"]},
                        "outputs_json": {"type": "object"}
                    },
                    "required": ["automation_run_id", "status"]
                }
            }
        }
