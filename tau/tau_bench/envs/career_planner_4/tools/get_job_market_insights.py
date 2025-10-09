from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetJobMarketInsights(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role: str) -> str:
        _roleL = role or ''.lower()
        insights = data.get("job_market_insights", {}).values()
        insight = next(
            (i for i in insights.values() if i.get("role", "").lower() == role.lower()), None
        )
        if insight:
            payload = insight
            out = json.dumps(payload, indent=2)
            return out
        else:
            payload = {"role": role, "insights": "Market data not available"}
            out = json.dumps(
                payload, indent=2
            )
            return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getJobMarketInsights",
                "description": "Get job market insights for a role",
                "parameters": {
                    "type": "object",
                    "properties": {"role": {"type": "string"}},
                    "required": ["role"],
                },
            },
        }
