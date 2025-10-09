from tau_bench.envs.tool import Tool
import json
from typing import Any

class ComputeAndStoreMergedTimeseries(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        columns: list[str] = None,
        created_ts: str = None,
        csv_path: str = None,
        file_hash_sha256: str = None,
        max_timestamp: str = None,
        min_timestamp: str = None,
        row_count: int = None
    ) -> str:
        err = _require({"csv_path": csv_path}, ["csv_path"])
        if err:
            return err
        allowed = [
            "csv_path",
            "columns",
            "row_count",
            "min_timestamp",
            "max_timestamp",
            "file_hash_sha256",
            "created_ts",
        ]
        row = {k: v for k, v in locals().items() if k in allowed and v is not None}
        payload = _append(data.setdefault("processed_timeseries", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeAndStoreMergedTimeseries",
                "description": "Registers a merged timeseries CSV artifact and its metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "csv_path": {"type": "string"},
                        "columns": {"type": "array", "items": {"type": "string"}},
                        "row_count": {"type": "integer"},
                        "min_timestamp": {"type": "string"},
                        "max_timestamp": {"type": "string"},
                        "file_hash_sha256": {"type": "string"},
                        "created_ts": {"type": "string"},
                    },
                    "required": ["csv_path"],
                },
            },
        }
