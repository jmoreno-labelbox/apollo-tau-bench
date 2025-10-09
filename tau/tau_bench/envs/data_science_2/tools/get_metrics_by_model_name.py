from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetMetricsByModelName(Tool):
    """Fetches metrics record based on model_name."""

    @staticmethod
    def invoke(data: dict[str, Any], model_name: str) -> str:
        rows = data.get("metrics", {}).values()
        for row in rows:
            if row.get("model_name") == model_name:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {"error": "metrics not found", "model_name": model_name}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMetricsByModelName",
                "description": "Retrieves metrics record by model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {"model_name": {"type": "string"}},
                    "required": ["model_name"],
                },
            },
        }
