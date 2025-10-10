# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildFeatureValidationPath(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city_slug = kwargs.get("city_slug")
        model_name = kwargs.get("model_name")
        created_ts = kwargs.get("created_ts")
        if not city_slug or not model_name or not created_ts:
            return json.dumps({"error":"Missing city_slug, model_name or created_ts"})
        ymd = created_ts[:10].replace("-", "")
        path = f"/processed_data/feature_validation_{city_slug}_{model_name}_{ymd}.json"
        return json.dumps({"city_slug": city_slug, "model_name": model_name, "ymd": ymd, "feature_validation_json_path": path})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_feature_validation_path","description":"Builds canonical feature validation JSON path from city_slug, model_name, and created_ts.","parameters":{"type":"object","properties":{"city_slug":{"type":"string"},"model_name":{"type":"string"},"created_ts":{"type":"string"}},"required":["city_slug","model_name","created_ts"]}}}
