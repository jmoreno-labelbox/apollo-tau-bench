from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ComputeSplitCounts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], row_count: int = None, test_fraction: float = None) -> str:
        try:
            row_count = int(row_count)
            test_fraction = float(test_fraction)
        except Exception:
            payload = {"error": "row_count must be int and test_fraction must be float"}
            out = json.dumps(payload)
            return out
        if row_count < 0 or not (0 < test_fraction < 1):
            payload = {"error": "Invalid values for row_count or test_fraction"}
            out = json.dumps(payload)
            return out
        train_index_count = int(row_count * (1 - test_fraction))
        test_index_count = row_count - train_index_count
        payload = {
            "row_count": row_count,
            "test_fraction": test_fraction,
            "train_index_count": train_index_count,
            "test_index_count": test_index_count,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeSplitCounts",
                "description": "Computes train/test counts given row_count and test_fraction (floor rule).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_count": {"type": "integer"},
                        "test_fraction": {"type": "number"},
                    },
                    "required": ["row_count", "test_fraction"],
                },
            },
        }
