from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ComputeFeatureCoverage(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], required_features: list = None, available_features: list = None) -> str:
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
        payload = {
                "present_features": present,
                "missing_features": missing,
                "present_count": present_count,
                "required_count": required_count,
                "missing_count": missing_count,
                "coverage": coverage,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeFeatureCoverage",
                "description": "Computes present/missing features and coverage ratio given required and available feature lists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "required_features": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "available_features": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["required_features", "available_features"],
                },
            },
        }
