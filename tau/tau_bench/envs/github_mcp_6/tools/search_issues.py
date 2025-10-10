# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchIssues(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], query: str) -> str:
        """Search issues by query."""
        issues_data = list(data.get("issues", {}).values())
        matching_issues = []

        for issue_entry in issues_data:
            for i, title in enumerate(issue_entry["issue_titles"]):
                if query.lower() in title.lower() or query.lower() in issue_entry["issue_bodies"][i].lower():
                    matching_issues.append({
                        "number": issue_entry["issue_numbers"][i],
                        "title": title,
                        "state": issue_entry["issue_states"][i]
                    })

        return json.dumps({"issues": matching_issues}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_issues",
                "description": "Search issues by query.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Issue search query"}
                    },
                    "required": ["query"]
                }
            }
        }
