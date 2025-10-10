# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class WriteModelConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["saved_json_path"])
        if err: return err
        row = {
            "classification_threshold_m_nullable": kwargs.get("classification_threshold_m_nullable"),
            "precip_24h_threshold_mm_nullable": kwargs.get("precip_24h_threshold_mm_nullable"),
            "test_split_fraction_nullable": kwargs.get("test_split_fraction_nullable"),
            "random_seed_nullable": kwargs.get("random_seed_nullable"),
            "saved_json_path": kwargs["saved_json_path"], "created_ts": kwargs.get("created_ts")
        }
        return json.dumps(_append(data.setdefault("model_config", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "write_model_config",
            "description": "Stores modeling configuration (thresholds/split/seed).",
            "parameters": {"type": "object", "properties": {
                "classification_threshold_m_nullable": {"type": "number"},
                "precip_24h_threshold_mm_nullable": {"type": "number"},
                "test_split_fraction_nullable": {"type": "number"},
                "random_seed_nullable": {"type": "integer"},
                "saved_json_path": {"type": "string"},
                "created_ts": {"type": "string"}}, "required": ["saved_json_path"]}}}
