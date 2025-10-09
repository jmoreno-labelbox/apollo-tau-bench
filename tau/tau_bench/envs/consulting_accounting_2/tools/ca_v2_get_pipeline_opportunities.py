from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CaV2GetPipelineOpportunities(Tool):
    """Retrieve pipeline opportunities, optionally filtered by stage or likelihood."""

    @staticmethod
    def invoke(data: dict[str, Any], stage: str = None, min_probability: float = None) -> str:
        opportunities = data.get("pipeline_opportunities", [])

        if stage:
            opportunities = [opp for opp in opportunities if opp.get("stage") == stage]

        if min_probability is not None:
            opportunities = [
                opp
                for opp in opportunities
                if opp.get("probability", 0) >= min_probability
            ]
        payload = opportunities
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetPipelineOpportunities",
                "description": "Get pipeline opportunities, optionally filtered by stage or minimum probability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "stage": {"type": "string"},
                        "min_probability": {
                            "type": "number",
                            "minimum": 0,
                            "maximum": 1,
                        },
                    },
                    "required": [],
                },
            },
        }
