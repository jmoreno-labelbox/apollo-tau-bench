# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class StartAutomationRun(Tool):
    """Start an automation run (build triage, asset_qa, testing)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        automation_type = kwargs.get("automation_type")  # build_triage, asset_qa, testing
        input_ref = kwargs.get("input_ref")
        automation_run_id = kwargs.get("automation_run_id")
        run = {
            "id": automation_run_id,
            "automation_type": automation_type,
            "input_ref": input_ref,
            "status": "running",
            "started_at": FIXED_NOW,
            "ended_at": None,
            "duration_ms": 0,
            "outputs_json": {},
            "errors_json": None
        }
        data.setdefault("automation_runs", []).append(run)
        return json.dumps({"automation_run": run}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "start_automation_run",
                "description": "Create a deterministic 'running' automation run record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "automation_type": {"type": "string", "enum": ["build_triage", "asset_qa", "testing"]},
                        "input_ref": {"type": "string"},
                        "automation_run_id": {"type": "string"}
                    },
                    "required": ["automation_type", "input_ref", "automation_run_id"]
                }
            }
        }
