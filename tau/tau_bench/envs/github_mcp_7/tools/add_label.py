# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddLabel(Tool):
    """Add a label to an issue or PR."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        kind = kwargs.get("kind")
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        number = kwargs.get("number")
        label = kwargs.get("label")
        target_list = _issues(data) if kind == "issue" else _prs(data)
        for obj in target_list:
            if obj.get("owner") == owner and obj.get("repo") == repo and obj.get("number") == number:
                labels = obj.setdefault("labels", [])
                if label and label not in labels:
                    labels.append(label)
                return json.dumps(obj)
        raise RuntimeError("Target not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_label",
                "description": "Add a label to an issue or PR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kind": {"type": "string", "enum": ["issue", "pr"]},
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "label": {"type": "string"}
                    },
                    "required": ["kind", "repo", "number", "label"]
                }
            },
        }
