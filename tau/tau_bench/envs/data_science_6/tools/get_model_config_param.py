# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetModelConfigParam(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], saved_json_path) -> str:
        if not saved_json_path:
            return json.dumps({"error": "Missing saved_json_path"})
        for rec in data.get("model_config", []):
            if rec.get("saved_json_path") == saved_json_path:
                return json.dumps({
                    "saved_json_path": saved_json_path,
                    "test_split_fraction": rec.get("test_split_fraction_nullable"),
                    "classification_threshold_m": rec.get("classification_threshold_m_nullable"),
                    "precip_24h_threshold_mm": rec.get("precip_24h_threshold_mm_nullable"),
                    "random_seed": rec.get("random_seed_nullable"),
                    "created_ts": rec.get("created_ts")
                })
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"get_model_config_param",
                "description":"Returns parameters from a model_config record identified by saved_json_path.",
                "parameters":{"type":"object","properties":{"saved_json_path":{"type":"string"}},"required":["saved_json_path"]}
            }
        }
