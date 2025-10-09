from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateTimeBasedSplit(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        method: str = None,
        test_fraction: float = None,
        train_index_count: int = None,
        test_index_count: int = None,
        split_summary_json_path: str = None,
        split_ts: str = None
    ) -> str:
        err = _require({"split_summary_json_path": split_summary_json_path}, ["split_summary_json_path"])
        if err:
            return err
        row = {
            "method": method,
            "test_fraction": test_fraction,
            "train_index_count": train_index_count,
            "test_index_count": test_index_count,
            "split_summary_json_path": split_summary_json_path,
            "split_ts": split_ts,
        }
        payload = _append(data.setdefault("dataset_split", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTimeBasedSplit",
                "description": "Registers a time-based dataset split summary.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "method": {"type": "string"},
                        "test_fraction": {"type": "number"},
                        "train_index_count": {"type": "integer"},
                        "test_index_count": {"type": "integer"},
                        "split_summary_json_path": {"type": "string"},
                        "split_ts": {"type": "string"},
                    },
                    "required": ["split_summary_json_path"],
                },
            },
        }
