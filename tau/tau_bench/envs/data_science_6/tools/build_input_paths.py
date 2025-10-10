# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildInputPaths(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        features_csv_path = kwargs.get("features_csv_path")
        model_path = kwargs.get("model_path")
        if not features_csv_path or not model_path:
            return json.dumps({"error":"Missing features_csv_path or model_path"})
        return json.dumps({"input_paths": [features_csv_path, model_path]})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_input_paths","description":"Builds input_paths array for feature validation from features_csv_path and model_path.","parameters":{"type":"object","properties":{"features_csv_path":{"type":"string"},"model_path":{"type":"string"}},"required":["features_csv_path","model_path"]}}}
