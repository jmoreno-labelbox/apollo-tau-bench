# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadFeatureBundle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        feats = data.get("features", []) or []
        fid = kwargs.get("feature_set_id")
        fname = kwargs.get("feature_set_name")
        row = None
        if fid is not None:
            row = next((f for f in feats if str(f.get("feature_set_id")) == str(fid)), None)
        elif fname:
            row = next((f for f in feats if f.get("feature_set_name") == fname), None)
        return json.dumps(row or {"error": "Feature set not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_feature_bundle",
            "description": "Fetch a feature-set by id or by name.",
            "parameters": {"type": "object", "properties": {
                "feature_set_id": {"type": "string"},
                "feature_set_name": {"type": "string"}
            }, "required": []}
        }}
