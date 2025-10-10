# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class CreateTimeBasedSplit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["split_summary_json_path"])
        if err: return err
        row = {"method": kwargs.get("method"), "test_fraction": kwargs.get("test_fraction"),
               "train_index_count": kwargs.get("train_index_count"),
               "test_index_count": kwargs.get("test_index_count"),
               "split_summary_json_path": kwargs["split_summary_json_path"],
               "split_ts": kwargs.get("split_ts")}
        return json.dumps(_append(data.setdefault("dataset_split", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "create_time_based_split",
            "description": "Registers a time-based dataset split summary.",
            "parameters": {"type": "object", "properties": {
                "method": {"type": "string"}, "test_fraction": {"type": "number"},
                "train_index_count": {"type": "integer"}, "test_index_count": {"type": "integer"},
                "split_summary_json_path": {"type": "string"}, "split_ts": {"type": "string"}},
                "required": ["split_summary_json_path"]}}}
