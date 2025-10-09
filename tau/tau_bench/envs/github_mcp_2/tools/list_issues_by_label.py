from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListIssuesByLabel(Tool):
    """Delivers all issues that possess a specific label (e.g., 'bug')"""

    @staticmethod
    def invoke(data: dict[str, Any], label: str = None,
    repo_name: Any = None,
    ) -> str:
        if not label:
            payload = {"error": "label is required."}
            out = json.dumps(payload, indent=2)
            return out

        issues = _issues(data)
        result = []

        for issue in issues:
            numbers = issue["issue_numbers"]
            labels_list = issue.get("labels", [])

            for idx, lbls in enumerate(labels_list):
                if label in lbls:
                    result.append(numbers[idx])
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListIssuesByLabel",
                "description": "Returns all issues containing the given label.",
                "parameters": {
                    "type": "object",
                    "properties": {"label": {"type": "string"}},
                    "required": ["label"],
                },
            },
        }
