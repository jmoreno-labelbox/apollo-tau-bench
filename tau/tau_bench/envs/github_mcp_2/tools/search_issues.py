# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchIssues(Tool):
    """Searches issues by title, label, or body keyword."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        query = kwargs.get("query", "").lower()
        results = []

        for issue in _issues(data):
            # print("ISWEU::", issue)
            title = issue.get("title", "").lower()
            body = issue.get("body", "").lower()
            raw_labels = issue.get("labels", [])
            flat_labels = [l for sub in raw_labels for l in (sub if isinstance(sub, list) else [sub])]
            labels = [l.lower() for l in flat_labels]


            if query in title or query in body or query in labels:
                results.append(issue.get("number"))

        return json.dumps({"results": results}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "search_issues",
                "description": "Search issues by keyword in title, body, or labels.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"}
                    },
                    "required": ["query"]
                }
            }
        }
