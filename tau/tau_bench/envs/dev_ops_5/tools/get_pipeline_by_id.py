# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPipelineById(Tool):
    """Retrieves a pipeline by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pipeline_id = kwargs.get("id")
        pipelines = list(data.get("pipelines", {}).values())
        for p in pipelines:
            if p.get("id") == pipeline_id:
                return json.dumps(p)
        return json.dumps({"error": f"Pipeline with ID '{pipeline_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pipeline_by_id",
                "description": "Retrieves a pipeline by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "The unique ID of the pipeline."}
                    },
                    "required": ["id"],
                },
            },
        }
