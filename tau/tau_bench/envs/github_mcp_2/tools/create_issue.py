from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class CreateIssue(Tool):
    """Generates a new issue within a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, title: str, body: str = "", labels: list = []) -> str:
        if not all([repo_name, title]):
            payload = {"error": "repo_name and title are required."}
            out = json.dumps(payload, indent=2)
            return out

        number = get_next_issue_number()
        me = _auth(data)["username"]

        issue = {
            "repo_name": repo_name,
            "number": number,
            "title": title,
            "body": body,
            "labels": labels,
            "state": "open",
            "creator": me,
            "comments": [],
        }
        #print("issue:", issue)

        _issues(data).append(issue)
        payload = {"message": "Issue created", "number": number}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateIssue",
                "description": "Creates a new issue in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                        "labels": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["repo_name", "title"],
                },
            },
        }
