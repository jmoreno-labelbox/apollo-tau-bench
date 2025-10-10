# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchAutomationRunsByType(Tool):
    """Searches for automation runs with a specific run type."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_type = kwargs.get("run_type")
        runs = data.get("automation_runs", [])
        matching_runs = []
        
        for run in runs:
            if run.get("run_type") == run_type:
                matching_runs.append(run.get("run_id"))
        
        return json.dumps({"automation_run_ids": matching_runs})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_automation_runs_by_type",
                "description": "Searches for automation runs with a specific run type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_type": {
                            "type": "string",
                            "description": "The run type to search for (e.g., plan_freeze, budget_apply, creative_rotation).",
                        }
                    },
                    "required": ["run_type"],
                },
            },
        }
