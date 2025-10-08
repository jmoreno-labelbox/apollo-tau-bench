from tau_bench.envs.tool import Tool
import json
from typing import Any

class RegisterModel(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        feature_names: list[str] = None,
        model_name: str = None,
        model_path: str = None,
        model_type: str = None,
        target_name: str = None,
        train_metrics_json_path_nullable: str = None,
        training_ts: str = None
    ) -> str:
        err = _require({"model_name": model_name, "model_path": model_path}, ["model_name", "model_path"])
        if err:
            return err
        row = {
            "model_name": model_name,
            "model_type": model_type,
            "training_ts": training_ts,
            "model_path": model_path,
            "feature_names": feature_names,
            "target_name": target_name,
            "train_metrics_json_path_nullable": train_metrics_json_path_nullable,
        }
        payload = _append(data.setdefault("models", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterModel",
                "description": "Registers a trained model artifact with metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "model_type": {"type": "string"},
                        "training_ts": {"type": "string"},
                        "model_path": {"type": "string"},
                        "feature_names": {"type": "array", "items": {"type": "string"}},
                        "target_name": {"type": "string"},
                        "train_metrics_json_path_nullable": {"type": "string"},
                    },
                    "required": ["model_name", "model_path"],
                },
            },
        }
