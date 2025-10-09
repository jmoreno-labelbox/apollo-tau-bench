from tau_bench.envs.tool import Tool
import json
from typing import Any

class ReadFeatureBundle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], feature_set_id: str = None, feature_set_name: str = None) -> str:
        feats = data.get("features", []) or []
        fid = feature_set_id
        fname = feature_set_name
        row = None
        if fid is not None:
            row = next(
                (f for f in feats if str(f.get("feature_set_id")) == str(fid)), None
            )
        elif fname:
            row = next((f for f in feats if f.get("feature_set_name") == fname), None)
        payload = row or {"error": "Feature set not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReadFeatureBundle",
                "description": "Fetch a feature-set by id or by name.",
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
