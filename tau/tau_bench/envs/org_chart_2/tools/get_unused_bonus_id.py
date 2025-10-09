from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetUnusedBonusId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        bonuses = data.get("bonuses", [])
        prefix = "BON"
        start_num = 10000

        if not bonuses:
            payload = f"{prefix}{start_num}"
            out = json.dumps(payload, indent=2)
            return out

        max_id_num = 0
        for bonus in bonuses:
            bonus_id = bonus.get("bonus_id", "")
            if bonus_id.startswith(prefix):
                try:
                    num = int(bonus_id[len(prefix) :])
                    if num > max_id_num:
                        max_id_num = num
                except (ValueError, TypeError):
                    continue

        next_id_num = max(start_num, max_id_num) + 1
        payload = f"{prefix}{next_id_num}"
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUnusedBonusId",
                "description": "Return a bonus payment ID that is not currently in use.",
                "parameters": {},
            },
        }
