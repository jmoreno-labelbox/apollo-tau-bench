from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class CreateRelease(Tool):
    """Generates a release for a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, tag: str, body: str = "", title: str = "",
    name: Any = None,
    ) -> str:
        if not all([repo_name, tag]):
            payload = {"error": "repo_name and tag are required."}
            out = json.dumps(payload, indent=2)
            return out

        repo = _find_repo_record(data, repo_name)
        repo.setdefault("releases", []).append(
            {
                "tag_name": tag,
                "body": body,
                "created_by": _auth(data)["username"],
                "created_at": get_current_timestamp(),
            }
        )
        payload = {
                "message": "Release created.",
                "repo_name": repo_name,
                "tag_name": tag,
                "title": title,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateRelease",
                "description": "Creates a new release (tag + body).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "tag": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                    },
                    "required": ["repo_name", "tag"],
                },
            },
        }
