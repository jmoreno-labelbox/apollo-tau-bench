from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetMemberTargets(Tool):
    """Retrieve target_calories/target_protein and flags for a member."""

    @staticmethod
    def invoke(data: dict[str, Any], member_id: str = None) -> str:
        if member_id is None:
            return _json_dump({"error": "member_id is required"})
        row = _require(data, "members", "member_id", member_id)
        if not row:
            return _json_dump({"error": f"member_id {member_id} not found"})
        out = {
            "member_id": member_id,
            "target_calories": row.get("target_calories"),
            "target_protein": row.get("target_protein"),
            "is_child": row.get("is_child"),
            "activity_level": row.get("activity_level"),
            "allergies_json": row.get("allergies_json"),
        }
        return _json_dump(out)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMemberTargets",
                "description": "Return member nutrition targets and key flags.",
                "parameters": {
                    "type": "object",
                    "properties": {"member_id": {"type": "integer"}},
                    "required": ["member_id"],
                },
            },
        }
