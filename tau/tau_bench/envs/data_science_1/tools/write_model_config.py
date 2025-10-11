# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require






def _require(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return json.dumps({"error": f"Missing required arguments: {', '.join(missing)}"}, indent=2)
    return None

def _append(table: List[Dict[str, Any]], row: Dict[str, Any]) -> Dict[str, Any]:
    table.append(row)
    return row

class WriteModelConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], classification_threshold_m_nullable, created_ts, precip_24h_threshold_mm_nullable, random_seed_nullable, saved_json_path, test_split_fraction_nullable) -> str:
        err = _require(kwargs, ["saved_json_path"])
        if err: return err
        row = {
            "classification_threshold_m_nullable": classification_threshold_m_nullable,
            "precip_24h_threshold_mm_nullable": precip_24h_threshold_mm_nullable,
            "test_split_fraction_nullable": test_split_fraction_nullable,
            "random_seed_nullable": random_seed_nullable,
            "saved_json_path": saved_json_path, "created_ts": created_ts
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