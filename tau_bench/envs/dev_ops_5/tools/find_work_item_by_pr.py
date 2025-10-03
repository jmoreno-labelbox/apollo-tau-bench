from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindWorkItemByPr(Tool):
    """Locates a work item linked to a pull request number."""

    @staticmethod
    def invoke(data: dict[str, Any], pr_number: int = None, repository_id: int = None) -> str:
        pass
        # This is a simulated implementation since there is no direct connection in the schema.
        # It will locate a work item that closely corresponds to the PR title.
        prs = data.get("pull_requests", [])
        work_items = data.get("work_items", [])

        pr_title = ""
        for pr in prs:
            if pr.get("repository_id") == repository_id and pr.get("number") == pr_number:
                pr_title = pr.get("title", "").lower()
                break

        if not pr_title:
            payload = {"error": "PR not found."}
            out = json.dumps(payload)
            return out

        for item in work_items:
            if item.get("title", "").lower() in pr_title:
                payload = item
                out = json.dumps(payload)
                return out
        payload = {"info": "No matching work item found for PR."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findWorkItemByPr",
                "description": "Finds a work item associated with a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pr_number": {"type": "integer"},
                        "repository_id": {"type": "string"},
                    },
                    "required": ["pr_number", "repository_id"],
                },
            },
        }
