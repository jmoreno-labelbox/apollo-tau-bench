from tau_bench.envs.tool import Tool
import json
from typing import Any

class SavePredictionsRecord(Tool):
    """Adds a predictions record."""

    @staticmethod
    def invoke(data: dict[str, Any], model_name: str, predictions_csv_path: str, row_count: int, columns: list, generated_ts: str) -> str:
        req = {
            "model_name",
            "predictions_csv_path",
            "row_count",
            "columns",
            "generated_ts",
        }
        record = {
            "model_name": model_name,
            "predictions_csv_path": predictions_csv_path,
            "row_count": row_count,
            "columns": columns,
            "generated_ts": generated_ts,
        }
        if not req.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        data.setdefault("predictions", []).append(record)
        payload = {
            "status": "inserted",
            "model_name": model_name,
            "predictions_csv_path": predictions_csv_path,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "savePredictionsRecord",
                "description": "Appends a predictions record.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }
