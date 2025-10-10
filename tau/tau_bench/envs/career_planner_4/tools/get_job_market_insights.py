# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_job_market_insights(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], role: str) -> str:
        insights = data.get("job_market_insights", [])
        insight = next(
            (i for i in insights if i.get("role", "").lower() == role.lower()), None
        )
        if insight:
            return json.dumps(insight, indent=2)
        else:
            return json.dumps(
                {"role": role, "insights": "Market data not available"}, indent=2
            )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_job_market_insights",
                "description": "Get job market insights for a role",
                "parameters": {
                    "type": "object",
                    "properties": {"role": {"type": "string"}},
                    "required": ["role"],
                },
            },
        }
