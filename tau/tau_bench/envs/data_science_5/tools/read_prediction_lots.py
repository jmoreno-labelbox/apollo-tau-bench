from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ReadPredictionLots(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], batch_name: str = None, model_name: str = None) -> str:
        preds = data.get("predictions", []) or []
        rows = [
            p
            for p in preds
            if (not batch_name or p.get("batch_name") == batch_name)
            and (not model_name or p.get("model_name") == model_name)
        ]
        payload = {"predictions": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReadPredictionLots",
                "description": "Read prediction batches (filter by batch or model).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "batch_name": {"type": "string"},
                        "model_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
