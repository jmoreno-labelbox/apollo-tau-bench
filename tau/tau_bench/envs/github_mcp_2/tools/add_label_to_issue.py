# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddLabelToIssue(Tool):
    """Adds a label to the specified issue. Supports both aggregated and flat issue shapes."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        issue_number = kwargs.get("issue_number")
        label = kwargs.get("label")

        if not all([repo_name, issue_number, label]):
            return json.dumps({"error": "repo_name, issue_number, and label are required."}, indent=2)

        target = int(issue_number)

        # 1) Support aggregated blocks (original dataset shape)
        for block in _issues(data):
            if block.get("repo_name") != repo_name:
                continue
            if "issue_numbers" in block and "labels" in block:
                issue_numbers = block["issue_numbers"]
                if target in issue_numbers:
                    idx = issue_numbers.index(target)
                    labels_at_idx = list(set(block["labels"][idx] + [label]))
                    block["labels"][idx] = labels_at_idx
                    return json.dumps({"message": f"Label '{label}' added."}, indent=2)

        # 2) Support flat rows (created by CreateIssue)
        for row in _issues(data):
            if row.get("repo_name") == repo_name and row.get("number") == target:
                cur = set(row.get("labels", []))
                cur.add(label)
                row["labels"] = list(cur)
                return json.dumps({"message": f"Label '{label}' added."}, indent=2)

        return json.dumps({"error": "Issue not found."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "add_label_to_issue",
                "description": "Adds a label to an issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"},
                        "label": {"type": "string"},
                    },
                    "required": ["repo_name", "issue_number", "label"]
                }
            }
        }
