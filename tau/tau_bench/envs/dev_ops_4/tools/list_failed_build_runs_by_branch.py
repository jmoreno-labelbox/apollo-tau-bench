# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListFailedBuildRunsByBranch(Tool):
    """List failed build runs for a given branch."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        branch = kwargs.get("branch")
        runs = data.get("build_runs", [])
        failed = [r for r in runs if r.get("branch") == branch and r.get("status") == "failed"]
        return json.dumps({"count": len(failed), "runs": failed}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_failed_build_runs_by_branch",
                "description": "List failed build runs for a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "branch": {"type": "string"}
                    },
                    "required": ["branch"]
                }
            }
        }
