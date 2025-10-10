# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddFeatureSet(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        feats = data.get("features", [])
        max_id = 0
        for f in feats:
            try:
                fid = int(f.get("feature_set_id", 0))
                if fid > max_id: max_id = fid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "feature_set_id": new_id,
            "feature_set_name": kwargs.get("feature_set_name"),
            "version": kwargs.get("version"),
            "columns": kwargs.get("columns"),
            "created_at": _fixed_now_iso()
        }
        feats.append(row)
        return json.dumps({"feature_set_id": new_id, "feature_set_name": row["feature_set_name"]}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"insert_feature_set",
            "description":"Insert a new feature set descriptor.",
            "parameters":{"type":"object","properties":{
                "feature_set_name":{"type":"string"},
                "version":{"type":"string"},
                "columns":{"type":"array","items":{"type":"string"}}
            },"required":["feature_set_name","version","columns"]}
        }}
