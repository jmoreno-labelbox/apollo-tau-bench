# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
