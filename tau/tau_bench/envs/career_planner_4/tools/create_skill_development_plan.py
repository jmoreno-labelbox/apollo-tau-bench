# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class create_skill_development_plan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, focus_areas: list) -> str:
        plan = {
            "plan_id": f"SDP{int(datetime.now().timestamp() * 1000) % 10000}",
            "user_id": user_id,
            "focus_areas": focus_areas,
            "created_date": "2025-07-04",
            "status": "Active",
        }

        data.setdefault("skill_development_plans", []).append(plan)

        return json.dumps(
            {
                "success": f"Skill development plan created for user {user_id}",
                "plan": plan,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "create_skill_development_plan",
                "description": "Create a skill development plan for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "focus_areas": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["user_id", "focus_areas"],
                },
            },
        }
