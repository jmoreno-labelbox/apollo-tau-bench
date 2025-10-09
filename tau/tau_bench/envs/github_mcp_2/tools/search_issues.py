from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class SearchIssues(Tool):
    """Looks for issues based on title, label, or body keyword."""

    @staticmethod
    def invoke(data: dict[str, Any], query: str = "") -> str:
        query = query.lower()
        results = []

        for issue in _issues(data):
            #print("ISWEU::", issue)
            title = issue.get("title", "").lower()
            body = issue.get("body", "").lower()
            raw_labels = issue.get("labels", [])
            flat_labels = [
                l
                for sub in raw_labels
                for l in (sub if isinstance(sub, list) else [sub])
            ]
            labels = [l.lower() for l in flat_labels]

            if query in title or query in body or query in labels:
                results.append(issue.get("number"))
        payload = {"results": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchIssues",
                "description": "Search issues by keyword in title, body, or labels.",
                "parameters": {
                    "type": "object",
                    "properties": {"query": {"type": "string"}},
                    "required": ["query"],
                },
            },
        }
