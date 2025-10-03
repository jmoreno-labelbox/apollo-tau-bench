from tau_bench.envs.tool import Tool
import json
from typing import Any

class ComputeDeltaNumbers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], before: float, after: float, label: str) -> str:
        delta = float(after) - float(before)
        payload = {
            "label": label,
            "before": float(before),
            "after": float(after),
            "delta": round(delta, 6),
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "computeDeltaNumbers",
                "description": "Compute numeric delta between before/after.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "before": {"type": "number"},
                        "after": {"type": "number"},
                        "label": {"type": "string"},
                    },
                    "required": ["before", "after", "label"],
                },
            },
        }
