# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RegisterFeatureBundle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], columns, feature_set_name, version) -> str:
        feats = list(data.get("features", {}).values())
        max_id = 0
        for f in feats:
            try:
                fid = int(f.get("feature_set_id", 0))
                if fid > max_id:
                    max_id = fid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "feature_set_id": new_id,
            "feature_set_name": feature_set_name,
            "version": version,
            "columns": columns,
            "created_at": _fixed_now_iso(),
        }
        feats.append(row)
        return json.dumps({"feature_set_id": new_id, "feature_set_name": row["feature_set_name"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "register_feature_bundle",
            "description": "Create a feature-set descriptor record.",
            "parameters": {"type": "object", "properties": {
                "feature_set_name": {"type": "string"},
                "version": {"type": "string"},
                "columns": {"type": "array", "items": {"type": "string"}}
            }, "required": ["feature_set_name", "version", "columns"]}
        }}
