from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetMemberTargets(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], member_id: int) -> str:
        members = _get_table(data, "members")
        m = next((x for x in members if x.get("member_id") == member_id), None)
        if not m:
            return _error("member not found")
        payload = {"calories": m.get("target_calories"), "protein": m.get("target_protein")}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getMemberTargets",
                "description": "Returns stored calorie and protein targets for a member.",
                "parameters": {
                    "type": "object",
                    "properties": {"member_id": {"type": "integer"}},
                    "required": ["member_id"],
                },
            },
        }
