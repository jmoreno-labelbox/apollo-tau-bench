from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPipelineById(Tool):
    """Fetches a pipeline using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        pipeline_id = id
        pipelines = data.get("pipelines", {}).values()
        for p in pipelines.values():
            if p.get("id") == pipeline_id:
                payload = p
                out = json.dumps(payload)
                return out
        payload = {"error": f"Pipeline with ID '{pipeline_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPipelineById",
                "description": "Retrieves a pipeline by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "The unique ID of the pipeline.",
                        }
                    },
                    "required": ["id"],
                },
            },
        }
