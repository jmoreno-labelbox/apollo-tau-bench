# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildFeatureValidationMessages(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], feature_validation_json_path, missing_features, model_name, present_count, required_count) -> str:
        missing_features = missing_features or []
        if model_name is None or feature_validation_json_path is None or present_count is None or required_count is None:
            return json.dumps({"error":"Missing required fields"})
        miss = sorted([str(x) for x in missing_features])
        miss_str = "none" if len(miss) == 0 else ", ".join(miss)
        messages = [
            f"Feature validation for {model_name}: {present_count}/{required_count} required features present.",
            f"Missing features: {miss_str}.",
            f"Validated file: {feature_validation_json_path}."
        ]
        return json.dumps({"messages": messages})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"build_feature_validation_messages",
                "description":"Builds deterministic FVP messages with sorted missing features and the validation artifact path.",
                "parameters":{
                    "type":"object",
                    "properties":{
                        "model_name":{"type":"string"},
                        "feature_validation_json_path":{"type":"string"},
                        "present_count":{"type":"integer"},
                        "required_count":{"type":"integer"},
                        "missing_features":{"type":"array","items":{"type":"string"}}
                    },
                    "required":["model_name","feature_validation_json_path","present_count","required_count"]
                }
            }
        }
