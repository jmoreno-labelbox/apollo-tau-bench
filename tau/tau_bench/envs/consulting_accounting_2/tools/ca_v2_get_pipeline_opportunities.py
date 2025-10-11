# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2GetPipelineOpportunities(Tool):
    """Get pipeline opportunities, optionally filtered by stage or probability."""

    @staticmethod
    def invoke(data: Dict[str, Any], min_probability, stage) -> str:

        opportunities = data.get("pipeline_opportunities", [])

        if stage:
            opportunities = [opp for opp in opportunities if opp.get("stage") == stage]

        if min_probability is not None:
            opportunities = [opp for opp in opportunities if opp.get("probability", 0) >= min_probability]

        return json.dumps(opportunities)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_pipeline_opportunities",
                "description": "Get pipeline opportunities, optionally filtered by stage or minimum probability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "stage": {"type": "string"},
                        "min_probability": {"type": "number", "minimum": 0, "maximum": 1}
                    },
                    "required": [],
                },
            },
        }
