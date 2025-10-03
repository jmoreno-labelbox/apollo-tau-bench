from tau_bench.envs.tool import Tool
import json
from typing import Any

class ComputeNutritionTargets(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], member_ids: list[int]) -> str:
        members = _get_table(data, "members")
        out = {}
        for mid in member_ids or []:
            m = next((x for x in members if x.get("member_id") == mid), None)
            if m:
                out[str(mid)] = {
                    "calories": m.get("target_calories"),
                    "protein": m.get("target_protein"),
                }
        payload = {"targets": out}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeNutritionTargets",
                "description": "Collects stored targets for the provided member_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member_ids": {"type": "array", "items": {"type": "integer"}}
                    },
                    "required": ["member_ids"],
                },
            },
        }
