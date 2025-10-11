# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildFeatureValidationRunId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], city_slug, created_ts, model_name) -> str:
        if not city_slug or not model_name or not created_ts:
            return json.dumps({"error":"Missing city_slug, model_name or created_ts"})
        ymd = created_ts[:10].replace("-", "")
        run_id = f"fv_{city_slug}_{model_name}_{ymd}_v1"
        return json.dumps({"run_id": run_id, "ymd": ymd})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_feature_validation_run_id","description":"Builds canonical run_id for feature validation from city_slug, model_name, and created_ts.","parameters":{"type":"object","properties":{"city_slug":{"type":"string"},"model_name":{"type":"string"},"created_ts":{"type":"string"}},"required":["city_slug","model_name","created_ts"]}}}
