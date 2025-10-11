# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _issues(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("issues", [])

def _auth(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Return acting identity as {"username": "...", "email": "..."}.
    Requires get_me(username=...) to have set data["_me"].
    """
    me = data.get("_me")
    if isinstance(me, dict) and "username" in me:
        return me
    raise Exception("No acting identity set. Call get_me(username=...) first.")

class CreateIssue(Tool):
    """Creates a new issue in a repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], repo_name, title, body = "", labels = []) -> str:

        if not all([repo_name, title]):
            return json.dumps({"error": "repo_name and title are required."}, indent=2)

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
        # print("problem:", issue)

        _issues(data).append(issue)
        # print("final output:", _issues(data))
        return json.dumps({"message": "Issue created", "number": number}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_issue",
                "description": "Creates a new issue in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                        "labels": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["repo_name", "title"]
                }
            }
        }