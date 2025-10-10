# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRunTypeForAutomationRun(Tool):
    """Retrieves the run type for a specific automation run."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("run_id")
        runs = list(data.get("automation_runs", {}).values())
        
        for run in runs:
            if run.get("run_id") == run_id:
                return json.dumps({"run_type": run.get('run_type')})
        
        return json.dumps({"error": f"Automation run with ID '{run_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_run_type_for_automation_run",
                "description": "Retrieves the run type for a specific automation run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {
                            "type": "string",
                            "description": "The unique ID of the automation run.",
                        }
                    },
                    "required": ["run_id"],
                },
            },
        }
