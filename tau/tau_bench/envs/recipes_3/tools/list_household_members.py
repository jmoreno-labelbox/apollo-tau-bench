# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListHouseholdMembers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int) -> str:
        rows = [
            m for m in list(list(list(data.get("members", {}).values())) if isinstance(data.get("members"), dict) else data.get("members", [])) if int(m.get("household_id")) == int(household_id)
        ]
        return json.dumps({"members": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_household_members",
                "description": "List members of a household.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }
