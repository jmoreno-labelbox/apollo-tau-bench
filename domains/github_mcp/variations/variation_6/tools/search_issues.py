from tau_bench.envs.tool import Tool
import json
from typing import Any

class SearchIssues(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], query: str) -> str:
        """Search issues by query."""
        _queryL = query or ''.lower()
        pass
        issues_data = data.get("issues", [])
        matching_issues = []

        for issue_entry in issues_data:
            for i, title in enumerate(issue_entry["issue_titles"]):
                if (
                    query.lower() in title.lower()
                    or query.lower() in issue_entry["issue_bodies"][i].lower()
                ):
                    matching_issues.append(
                        {
                            "number": issue_entry["issue_numbers"][i],
                            "title": title,
                            "state": issue_entry["issue_states"][i],
                        }
                    )
        payload = {"issues": matching_issues}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchIssues",
                "description": "Search issues by query.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Issue search query"}
                    },
                    "required": ["query"],
                },
            },
        }
