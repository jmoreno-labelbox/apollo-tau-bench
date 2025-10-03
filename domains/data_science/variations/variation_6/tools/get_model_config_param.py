from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetModelConfigParam(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], saved_json_path: str = None) -> str:
        if not saved_json_path:
            payload = {"error": "Missing saved_json_path"}
            out = json.dumps(payload)
            return out
        for rec in data.get("model_config", []):
            if rec.get("saved_json_path") == saved_json_path:
                payload = {
                    "saved_json_path": saved_json_path,
                    "test_split_fraction": rec.get("test_split_fraction_nullable"),
                    "classification_threshold_m": rec.get(
                        "classification_threshold_m_nullable"
                    ),
                    "precip_24h_threshold_mm": rec.get(
                        "precip_24h_threshold_mm_nullable"
                    ),
                    "random_seed": rec.get("random_seed_nullable"),
                    "created_ts": rec.get("created_ts"),
                }
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetModelConfigParam",
                "description": "Returns parameters from a model_config record identified by saved_json_path.",
                "parameters": {
                    "type": "object",
                    "properties": {"saved_json_path": {"type": "string"}},
                    "required": ["saved_json_path"],
                },
            },
        }
