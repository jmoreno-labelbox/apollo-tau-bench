# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class StorePredictions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], columns, generated_ts, model_name, predictions_csv_path, row_count) -> str:
        err = _require(kwargs, ["model_name", "predictions_csv_path"])
        if err: return err
        row = {"model_name": model_name, "predictions_csv_path": predictions_csv_path,
               "row_count": row_count, "columns": columns,
               "generated_ts": generated_ts}
        return json.dumps(_append(data.setdefault("predictions", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_predictions",
            "description": "Stores a predictions CSV artifact for a model.",
            "parameters": {"type": "object", "properties": {
                "model_name": {"type": "string"}, "predictions_csv_path": {"type": "string"},
                "row_count": {"type": "integer"}, "columns": {"type": "array", "items": {"type": "string"}},
                "generated_ts": {"type": "string"}}, "required": ["model_name", "predictions_csv_path"]}}}
