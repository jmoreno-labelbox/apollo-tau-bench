from tau_bench.envs.tool import Tool
import json
from typing import Any

class FetchFeatureSetDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], feature_set_id: str = None, feature_set_name: str = None) -> str:
        feats = data.get("features", []) or []
        row = None
        if feature_set_id is not None:
            row = next(
                (f for f in feats if str(f.get("feature_set_id")) == str(feature_set_id)), None
            )
        elif feature_set_name:
            row = next((f for f in feats if f.get("feature_set_name") == feature_set_name), None)
        payload = row or {"error": "Feature set not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFeatureSetDetails",
                "description": "Read a feature set by id or by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "feature_set_id": {"type": "string"},
                        "feature_set_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
