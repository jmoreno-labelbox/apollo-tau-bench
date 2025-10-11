# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_unused_bonus_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        bonuses = data.get("bonuses", [])
        prefix = "BON"
        start_num = 10000

        if not bonuses:
            return json.dumps(f"{prefix}{start_num}", indent=2)

        max_id_num = 0
        for bonus in bonuses:
            bonus_id = bonus.get("bonus_id", "")
            if bonus_id.startswith(prefix):
                try:
                    num = int(bonus_id[len(prefix):])
                    if num > max_id_num:
                        max_id_num = num
                except (ValueError, TypeError):
                    continue

        next_id_num = max(start_num, max_id_num) + 1
        return json.dumps(f"{prefix}{next_id_num}", indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_unused_bonus_id",
                "description": "Return a bonus payment ID that is not currently in use.",
                "parameters": {},
            },
        }
