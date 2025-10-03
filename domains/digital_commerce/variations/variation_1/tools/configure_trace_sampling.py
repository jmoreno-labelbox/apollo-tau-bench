from tau_bench.envs.tool import Tool
import json
from typing import Any

class ConfigureTraceSampling(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sample_rate: float) -> str:
        flags = _ensure_table(data, "trace_flags")
        policy_id = _stable_id("trace", f"{sample_rate:.2f}")
        row = _find_one(flags, policy_id=policy_id)
        if row:
            row["sample_rate"] = float(sample_rate)
            row["created_at"] = FIXED_NOW
        else:
            flags.append(
                {
                    "policy_id": policy_id,
                    "sample_rate": float(sample_rate),
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"policy_id": policy_id, "effective_rate": float(sample_rate)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConfigureTraceSampling",
                "description": "Configure API trace sampling rate globally.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sample_rate": {
                            "type": "number",
                            "minimum": 0.0,
                            "maximum": 1.0,
                        }
                    },
                    "required": ["sample_rate"],
                },
            },
        }
