from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddPredictionBatch(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], batch_name: str = None, model_name: str = None, items: list = None) -> str:
        preds = data.get("predictions", {}).values()
        max_id = 0
        for p in preds:
            try:
                pid = int(p.get("prediction_id", 0))
                if pid > max_id:
                    max_id = pid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "prediction_id": new_id,
            "batch_name": batch_name,
            "model_name": model_name,
            "items": items or [],
            "created_at": _fixed_now_iso(),
        }
        data["predictions"][row["prediction_id"]] = row
        payload = {"prediction_id": new_id, "batch_name": row["batch_name"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertPredictionBatch",
                "description": "Insert a batch of predictions for a model.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "batch_name": {"type": "string"},
                        "model_name": {"type": "string"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["batch_name", "model_name", "items"],
                },
            },
        }
