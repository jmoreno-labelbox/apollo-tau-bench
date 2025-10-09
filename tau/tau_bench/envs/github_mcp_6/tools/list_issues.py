from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListIssues(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str,
        repo: str,
        state: str,
        labels: list[str] = None,
    ) -> str:
        """List issues filtered by label/state. When no labels are provided, returns all issues."""
        pass
        issues_data = data.get("issues", [])

        #Treat None or empty labels as "retrieve all"
        if labels is None:
            labels = []

        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                issues = []
                for i, issue_number in enumerate(issue_entry["issue_numbers"]):
                    issue_state = issue_entry["issue_states"][i]
                    issue_labels = issue_entry["labels"][i]

                    #Apply filter based on state
                    if state != "all" and issue_state != state:
                        continue

                    #Apply filter based on labels (if provided and not empty)
                    if labels and not any(label in issue_labels for label in labels):
                        continue

                    issues.append(
                        {
                            "number": issue_number,
                            "title": issue_entry["issue_titles"][i],
                            "state": issue_state,
                        }
                    )
                payload = {"issues": issues}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"issues": []}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listIssues",
                "description": "List issues filtered by label/state. When no labels are provided, returns all issues.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "state": {"type": "string", "description": "State filter"},
                        "labels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Label filter (optional - if not provided, returns all issues)",
                        },
                    },
                    "required": ["owner", "repo", "state"],
                },
            },
        }
