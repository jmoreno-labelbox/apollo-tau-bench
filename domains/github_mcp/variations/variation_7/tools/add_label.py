from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddLabel(Tool):
    """Attach a label to an issue or pull request."""

    @staticmethod
    def invoke(data: dict[str, Any], kind: str = None, owner: str = None, repo: str = None, number: int = None, label: str = None) -> str:
        owner = owner or _actor_name(data)
        target_list = _issues(data) if kind == "issue" else _prs(data)
        for obj in target_list:
            if (
                obj.get("owner") == owner
                and obj.get("repo") == repo
                and obj.get("number") == number
            ):
                labels = obj.setdefault("labels", [])
                if label and label not in labels:
                    labels.append(label)
                payload = obj
                out = json.dumps(payload)
                return out
        raise RuntimeError("Target not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddLabel",
                "description": "Add a label to an issue or PR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kind": {"type": "string", "enum": ["issue", "pr"]},
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "label": {"type": "string"},
                    },
                    "required": ["kind", "repo", "number", "label"],
                },
            },
        }
