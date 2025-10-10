# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchAutomationRunsByStatus(Tool):
    """Searches for automation runs with a specific status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        runs = data.get("automation_runs", [])
        matching_runs = []
        
        for run in runs:
            if run.get("status") == status:
                matching_runs.append(run.get("run_id"))
        
        return json.dumps({"automation_run_ids": matching_runs})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_automation_runs_by_status",
                "description": "Searches for automation runs with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status to search for (e.g., completed, failed).",
                        }
                    },
                    "required": ["status"],
                },
            },
        }
