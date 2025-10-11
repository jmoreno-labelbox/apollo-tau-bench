# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_or_create_label_id(db: Dict[str, Any], name: str) -> str:
    """Return label_id for `name`; create next sequential id (label_1, label_2, ...) if missing."""
    labels = db.setdefault("email_labels", [])
    for lab in labels:
        if lab.get("name") == name:
            return lab["label_id"]
    max_n = 0
    for lab in labels:
        lid = lab.get("label_id") or ""
        m = re.match(r"^label_(\d+)$", lid)
        if m:
            n = int(m.group(1))
            if n > max_n: max_n = n
    new_id = f"label_{max_n + 1}"
    labels.append({"label_id": new_id, "name": name})
    return new_id

class GetOrCreateEmailLabel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name) -> str:
        label_id = _get_or_create_label_id(data, name)
        return json.dumps({"label_id": label_id, "name": name}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_or_create_email_label",
                "description": "Get or create label by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"]
                }
            }
        }