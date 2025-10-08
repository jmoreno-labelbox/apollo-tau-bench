from tau_bench.envs.tool import Tool
import json
from typing import Any

class StorePredictions(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        columns: list = None,
        generated_ts: str = None,
        model_name: str = None,
        predictions_csv_path: str = None,
        row_count: int = None
    ) -> str:
        err = _require({"model_name": model_name, "predictions_csv_path": predictions_csv_path}, ["model_name", "predictions_csv_path"])
        if err:
            return err
        row = {
            "model_name": model_name,
            "predictions_csv_path": predictions_csv_path,
            "row_count": row_count,
            "columns": columns,
            "generated_ts": generated_ts,
        }
        payload = _append(data.setdefault("predictions", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StorePredictions",
                "description": "Stores a predictions CSV artifact for a model.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "predictions_csv_path": {"type": "string"},
                        "row_count": {"type": "integer"},
                        "columns": {"type": "array", "items": {"type": "string"}},
                        "generated_ts": {"type": "string"},
                    },
                    "required": ["model_name", "predictions_csv_path"],
                },
            },
        }
