from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class BuildOutputPaths(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], feature_validation_json_path: str = None) -> str:
        if not feature_validation_json_path:
            payload = {"error": "Missing feature_validation_json_path"}
            out = json.dumps(payload)
            return out
        payload = {"output_paths": [feature_validation_json_path]}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "buildOutputPaths",
                "description": "Wraps the feature_validation_json_path into the output_paths array.",
                "parameters": {
                    "type": "object",
                    "properties": {"feature_validation_json_path": {"type": "string"}},
                    "required": ["feature_validation_json_path"],
                },
            },
        }
