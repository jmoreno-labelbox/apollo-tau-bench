# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeFeatureCoverage(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], available_features, required_features) -> str:
        required = required_features or []
        available = available_features or []
        req = sorted([str(x) for x in required])
        ava = sorted([str(x) for x in available])
        present = [x for x in req if x in ava]
        missing = [x for x in req if x not in ava]
        present_count = len(present)
        required_count = len(req)
        missing_count = len(missing)
        coverage = 0.0 if required_count == 0 else present_count / float(required_count)
        return json.dumps({"present_features": present, "missing_features": missing, "present_count": present_count, "required_count": required_count, "missing_count": missing_count, "coverage": coverage})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"compute_feature_coverage","description":"Computes present/missing features and coverage ratio given required and available feature lists.","parameters":{"type":"object","properties":{"required_features":{"type":"array","items":{"type":"string"}},"available_features":{"type":"array","items":{"type":"string"}}},"required":["required_features","available_features"]}}}
