# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindPreviousSuccessfulDeployment(Tool):
    """Finds the last successful deployment for a given pipeline before a specific time."""
    @staticmethod
    def invoke(data: Dict[str, Any], before_timestamp, pipeline_id) -> str:
        deployments = sorted([d for d in list(data.get("deployments", {}).values()) if d.get("pipeline_id") == pipeline_id and d.get("deployed_at") < before_timestamp], key=lambda x: x['deployed_at'], reverse=True)
        
        for d in deployments:
            if d.get("status") == "successful":
                return json.dumps(d)
        return json.dumps({"error": f"No successful deployment found for pipeline '{pipeline_id}' before '{before_timestamp}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_previous_successful_deployment",
                "description": "Finds the last successful deployment for a pipeline before a specific time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pipeline_id": {"type": "string"},
                        "before_timestamp": {"type": "string"}
                    },
                    "required": ["pipeline_id", "before_timestamp"],
                },
            },
        }
