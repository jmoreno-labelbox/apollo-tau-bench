# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildOutputPaths(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], feature_validation_json_path) -> str:
        if not feature_validation_json_path:
            return json.dumps({"error":"Missing feature_validation_json_path"})
        return json.dumps({"output_paths": [feature_validation_json_path]})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_output_paths","description":"Wraps the feature_validation_json_path into the output_paths array.","parameters":{"type":"object","properties":{"feature_validation_json_path":{"type":"string"}},"required":["feature_validation_json_path"]}}}
