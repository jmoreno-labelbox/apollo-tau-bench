from tau_bench.envs.tool import Tool
import json
from typing import Any

class StartAutomationRun(Tool):
    """Initiate an automated run (build triage, asset_qa, testing)."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        automation_type: str = None, 
        input_ref: str = None, 
        automation_run_id: str = None
    ) -> str:
        pass
        # build_triage, asset_qa, testing
        run = {
            "id": automation_run_id,
            "automation_type": automation_type,
            "input_ref": input_ref,
            "status": "running",
            "started_at": FIXED_NOW,
            "ended_at": None,
            "duration_ms": 0,
            "outputs_json": {},
            "errors_json": None,
        }
        data.setdefault("automation_runs", []).append(run)
        payload = {"automation_run": run}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StartAutomationRun",
                "description": "Create a deterministic 'running' automation run record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "automation_type": {
                            "type": "string",
                            "enum": ["build_triage", "asset_qa", "testing"],
                        },
                        "input_ref": {"type": "string"},
                        "automation_run_id": {"type": "string"},
                    },
                    "required": ["automation_type", "input_ref", "automation_run_id"],
                },
            },
        }
