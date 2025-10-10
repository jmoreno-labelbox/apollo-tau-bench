# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListIssues(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str, state: str, labels: List[str] = None) -> str:
        """List issues filtered by label/state. When no labels are provided, returns all issues."""
        issues_data = list(data.get("issues", {}).values())

        # Handle None or empty labels as "retrieve all"
        if labels is None:
            labels = []

        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                issues = []
                for i, issue_number in enumerate(issue_entry["issue_numbers"]):
                    issue_state = issue_entry["issue_states"][i]
                    issue_labels = issue_entry["labels"][i]

                    # Filter by state
                    if state != "all" and issue_state != state:
                        continue

                    # Filter by labels (if labels filter is provided and not empty)
                    if labels and not any(label in issue_labels for label in labels):
                        continue

                    issues.append({
                        "number": issue_number,
                        "title": issue_entry["issue_titles"][i],
                        "state": issue_state
                    })

                return json.dumps({"issues": issues}, indent=2)

        return json.dumps({"issues": []}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_issues",
                "description": "List issues filtered by label/state. When no labels are provided, returns all issues.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "state": {"type": "string", "description": "State filter"},
                        "labels": {"type": "array", "items": {"type": "string"}, "description": "Label filter (optional - if not provided, returns all issues)"}
                    },
                    "required": ["owner", "repo", "state"]
                }
            }
        }
