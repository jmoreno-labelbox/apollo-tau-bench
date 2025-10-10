# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLabels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str) -> str:
        """Get all available labels for a repository."""
        issues_data = list(data.get("issues", {}).values())

        # Locate the repository within the issues dataset.
        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                # Gather all distinct labels from every issue in this repository.
                all_labels = set()
                for labels_list in issue_entry["labels"]:
                    if isinstance(labels_list, list):
                        all_labels.update(labels_list)
                    elif isinstance(labels_list, str):
                        all_labels.add(labels_list)

                # Transform into a sorted list to ensure uniform results.
                available_labels = sorted(list(all_labels))

                return json.dumps({
                    "success": True,
                    "data": {
                        "repository": f"{owner}/{repo}",
                        "available_labels": available_labels,
                        "total_labels": len(available_labels)
                    },
                    "metadata": {
                        "owner": owner,
                        "repo": repo,
                        "labels_discovered": len(available_labels)
                    }
                }, indent=2)

        # Return an empty list of labels if the repository is missing.
        return json.dumps({
            "success": True,
            "data": {
                "repository": f"{owner}/{repo}",
                "available_labels": [],
                "total_labels": 0
            },
            "metadata": {
                "owner": owner,
                "repo": repo,
                "labels_discovered": 0
            }
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_labels",
                "description": "Get all available labels for a repository to understand the labeling system and available options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"}
                    },
                    "required": ["owner", "repo"]
                }
            }
        }
