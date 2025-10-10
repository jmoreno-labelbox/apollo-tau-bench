# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class StoreFeatures(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["csv_path", "feature_names"])
        if err: return err
        row = {"csv_path": kwargs["csv_path"], "feature_names": kwargs["feature_names"],
               "definitions_nullable": kwargs.get("definitions_nullable"), "generated_ts": kwargs.get("generated_ts")}
        return json.dumps(_append(data.setdefault("features", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_features",
            "description": "Stores feature list metadata for a generated CSV.",
            "parameters": {"type": "object", "properties": {
                "csv_path": {"type": "string"}, "feature_names": {"type": "array", "items": {"type": "string"}},
                "definitions_nullable": {"type": "array", "items": {"type": "string"}},
                "generated_ts": {"type": "string"}}, "required": ["csv_path", "feature_names"]}}}
