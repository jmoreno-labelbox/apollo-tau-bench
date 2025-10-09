from tau_bench.envs.tool import Tool
import json
from typing import Any

class WriteModelConfig(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        classification_threshold_m_nullable: float = None,
        precip_24h_threshold_mm_nullable: float = None,
        test_split_fraction_nullable: float = None,
        random_seed_nullable: int = None,
        saved_json_path: str = None,
        created_ts: str = None
    ) -> str:
        err = _require({"saved_json_path": saved_json_path}, ["saved_json_path"])
        if err:
            return err
        row = {
            "classification_threshold_m_nullable": classification_threshold_m_nullable,
            "precip_24h_threshold_mm_nullable": precip_24h_threshold_mm_nullable,
            "test_split_fraction_nullable": test_split_fraction_nullable,
            "random_seed_nullable": random_seed_nullable,
            "saved_json_path": saved_json_path,
            "created_ts": created_ts,
        }
        payload = _append(data.setdefault("model_config", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteModelConfig",
                "description": "Stores modeling configuration (thresholds/split/seed).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "classification_threshold_m_nullable": {"type": "number"},
                        "precip_24h_threshold_mm_nullable": {"type": "number"},
                        "test_split_fraction_nullable": {"type": "number"},
                        "random_seed_nullable": {"type": "integer"},
                        "saved_json_path": {"type": "string"},
                        "created_ts": {"type": "string"},
                    },
                    "required": ["saved_json_path"],
                },
            },
        }
