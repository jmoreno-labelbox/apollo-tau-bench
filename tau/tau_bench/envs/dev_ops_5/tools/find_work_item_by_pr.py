# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindWorkItemByPr(Tool):
    """Finds a work item associated with a pull request number."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # This is a mock implementation as there's no direct link in the schema.
        # It will find a work item that matches the PR title approximately.
        pr_number = kwargs.get("pr_number")
        repo_id = kwargs.get("repository_id")
        prs = list(data.get("pull_requests", {}).values())
        work_items = data.get("work_items", [])
        
        pr_title = ""
        for pr in prs:
            if pr.get("repository_id") == repo_id and pr.get("number") == pr_number:
                pr_title = pr.get("title", "").lower()
                break

        if not pr_title:
            return json.dumps({"error": "PR not found."})
            
        for item in work_items:
            if item.get("title", "").lower() in pr_title:
                return json.dumps(item)
                
        return json.dumps({"info": "No matching work item found for PR."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_work_item_by_pr",
                "description": "Finds a work item associated with a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pr_number": {"type": "integer"},
                        "repository_id": {"type": "string"}
                    },
                    "required": ["pr_number", "repository_id"],
                },
            },
        }
