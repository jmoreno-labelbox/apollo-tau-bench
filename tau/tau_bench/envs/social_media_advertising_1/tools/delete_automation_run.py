# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteAutomationRun(Tool):
    """Deletes an automation run record."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("run_id")
        if not run_id:
            return json.dumps({"error": "run_id is a required parameter."})

        runs = list(data.get("automation_runs", {}).values())
        original_count = len(runs)
        data['automation_runs'] = [r for r in runs if r.get("run_id") != run_id]

        if len(data['automation_runs']) < original_count:
            return json.dumps({
                "status": "success",
                "message": f"Automation run with id {run_id} deleted successfully."
            })
        else:
            return json.dumps({"error": f"Automation run with ID '{run_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_automation_run",
                "description": "Deletes an automation run record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {
                            "type": "string",
                            "description": "The unique ID of the automation run to delete.",
                        },
                    },
                    "required": ["run_id"],
                },
            },
        }
