from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPredictionsByModelName(Tool):
    """Fetches predictions record using model_name."""

    @staticmethod
    def invoke(data: dict[str, Any], model_name: str) -> str:
        rows = data.get("predictions", [])
        for row in rows:
            if row.get("model_name") == model_name:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {"error": "predictions not found", "model_name": model_name}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPredictionsByModelName",
                "description": "Retrieves predictions record by model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {"model_name": {"type": "string"}},
                    "required": ["model_name"],
                },
            },
        }
