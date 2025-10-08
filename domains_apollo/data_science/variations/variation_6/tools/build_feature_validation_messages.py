from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class BuildFeatureValidationMessages(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        model_name: str = None,
        feature_validation_json_path: str = None,
        present_count: int = None,
        required_count: int = None,
        missing_features: list = None
    ) -> str:
        if missing_features is None:
            missing_features = []
        if (
            model_name is None
            or feature_validation_json_path is None
            or present_count is None
            or required_count is None
        ):
            payload = {"error": "Missing required fields"}
            out = json.dumps(payload)
            return out
        miss = sorted([str(x) for x in missing_features])
        miss_str = "none" if len(miss) == 0 else ", ".join(miss)
        messages = [
            f"Feature validation for {model_name}: {present_count}/{required_count} required features present.",
            f"Missing features: {miss_str}.",
            f"Validated file: {feature_validation_json_path}.",
        ]
        payload = {"messages": messages}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "buildFeatureValidationMessages",
                "description": "Builds deterministic FVP messages with sorted missing features and the validation artifact path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "feature_validation_json_path": {"type": "string"},
                        "present_count": {"type": "integer"},
                        "required_count": {"type": "integer"},
                        "missing_features": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": [
                        "model_name",
                        "feature_validation_json_path",
                        "present_count",
                        "required_count",
                    ],
                },
            },
        }
