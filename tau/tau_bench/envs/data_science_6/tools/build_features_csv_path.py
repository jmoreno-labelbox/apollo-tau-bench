# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildFeaturesCsvPath(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], city_slug) -> str:
        if not city_slug:
            return json.dumps({"error":"Missing city_slug"})
        return json.dumps({"city_slug": city_slug, "features_csv_path": "/processed_data/features.csv"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_features_csv_path","description":"Returns canonical features CSV path for a city_slug.","parameters":{"type":"object","properties":{"city_slug":{"type":"string"}},"required":["city_slug"]}}}
