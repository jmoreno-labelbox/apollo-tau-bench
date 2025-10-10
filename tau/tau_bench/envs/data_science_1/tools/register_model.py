# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class RegisterModel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], feature_names, model_name, model_path, model_type, target_name, train_metrics_json_path_nullable, training_ts) -> str:
        err = _require(kwargs, ["model_name", "model_path"])
        if err: return err
        row = {"model_name": model_name, "model_type": model_type,
               "training_ts": training_ts,
               "model_path": model_path, "feature_names": feature_names,
               "target_name": target_name,
               "train_metrics_json_path_nullable": train_metrics_json_path_nullable}
        return json.dumps(_append(data.setdefault("models", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "register_model",
            "description": "Registers a trained model artifact with metadata.",
            "parameters": {"type": "object", "properties": {
                "model_name": {"type": "string"}, "model_type": {"type": "string"},
                "training_ts": {"type": "string"}, "model_path": {"type": "string"},
                "feature_names": {"type": "array", "items": {"type": "string"}},
                "target_name": {"type": "string"},
                "train_metrics_json_path_nullable": {"type": "string"}},
                "required": ["model_name", "model_path"]}}}
