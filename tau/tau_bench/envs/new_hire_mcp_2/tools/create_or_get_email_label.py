from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateOrGetEmailLabel(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str) -> str:
        rows = _ensure_list(data, "email_labels")
        for r in rows:
            if r.get("name") == name:
                payload = {"label_id": r.get("label_id"), "created": False}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        new_id = f"lbl_{_slug(name)}"
        rows.append({"label_id": new_id, "name": name})
        payload = {"label_id": new_id, "created": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOrGetEmailLabel",
                "description": "Return existing label_id by name or create deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
