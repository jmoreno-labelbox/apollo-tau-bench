# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOrGetEmailLabel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name) -> str:
        rows = _ensure_list(data, "email_labels")
        for r in rows:
            if r.get("name") == name:
                return json.dumps({"label_id": r.get("label_id"), "created": False}, indent=2)
        new_id = f"lbl_{_slug(name)}"
        rows.append({"label_id": new_id, "name": name})
        return json.dumps({"label_id": new_id, "created": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_or_get_email_label",
                                                 "description": "Return existing label_id by name or create deterministically.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"name": {"type": "string"}},
                                                                "required": ["name"]}}}
