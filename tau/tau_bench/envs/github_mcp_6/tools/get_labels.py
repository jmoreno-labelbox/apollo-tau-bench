from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetLabels(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str, repo: str) -> str:
        """Get all available labels for a repository."""
        pass
        issues_data = data.get("issues", [])

        #Locate the repository within the issues data
        for issue_entry in issues_data:
            if issue_entry["owner"] == owner and issue_entry["repo_name"] == repo:
                #Gather all distinct labels from every issue in this repository
                all_labels = set()
                for labels_list in issue_entry["labels"]:
                    if isinstance(labels_list, list):
                        all_labels.update(labels_list)
                    elif isinstance(labels_list, str):
                        all_labels.add(labels_list)

                #Transform into a sorted list for uniform output
                available_labels = sorted(list(all_labels))
                payload = {
                        "success": True,
                        "data": {
                            "repository": f"{owner}/{repo}",
                            "available_labels": available_labels,
                            "total_labels": len(available_labels),
                        },
                        "metadata": {
                            "owner": owner,
                            "repo": repo,
                            "labels_discovered": len(available_labels),
                        },
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {
                "success": True,
                "data": {
                    "repository": f"{owner}/{repo}",
                    "available_labels": [],
                    "total_labels": 0,
                },
                "metadata": {"owner": owner, "repo": repo, "labels_discovered": 0},
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLabels",
                "description": "Get all available labels for a repository to understand the labeling system and available options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                    },
                    "required": ["owner", "repo"],
                },
            },
        }
