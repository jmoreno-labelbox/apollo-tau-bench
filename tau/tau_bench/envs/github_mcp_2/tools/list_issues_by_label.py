# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListIssuesByLabel(Tool):
    """Returns all issues that have a given label (e.g., 'bug')"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        label = kwargs.get("label")
        if not label:
            return json.dumps({"error": "label is required."}, indent=2)

        issues = _issues(data)
        result = []

        for issue in issues:
            numbers = issue["issue_numbers"]
            labels_list = issue.get("labels", [])

            for idx, lbls in enumerate(labels_list):
                if label in lbls:
                    result.append(numbers[idx])

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_issues_by_label",
                "description": "Returns all issues containing the given label.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "label": {"type": "string"}
                    },
                    "required": ["label"]
                }
            }
        }
