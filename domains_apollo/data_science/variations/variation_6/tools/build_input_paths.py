from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class BuildInputPaths(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], features_csv_path: str = None, model_path: str = None) -> str:
        if not features_csv_path or not model_path:
            payload = {"error": "Missing features_csv_path or model_path"}
            out = json.dumps(payload)
            return out
        payload = {"input_paths": [features_csv_path, model_path]}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "buildInputPaths",
                "description": "Builds input_paths array for feature validation from features_csv_path and model_path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "features_csv_path": {"type": "string"},
                        "model_path": {"type": "string"},
                    },
                    "required": ["features_csv_path", "model_path"],
                },
            },
        }
