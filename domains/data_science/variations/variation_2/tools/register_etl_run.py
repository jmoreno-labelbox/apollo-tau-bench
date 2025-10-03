from tau_bench.envs.tool import Tool
import json
from typing import Any

class RegisterEtlRun(Tool):
    """Adds an etl_runs record."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str, input_paths: Any, output_paths: Any, status: str, started_ts: Any) -> str:
        req = {"run_id", "input_paths", "output_paths", "status", "started_ts"}
        record = {
            "run_id": run_id,
            "input_paths": input_paths,
            "output_paths": output_paths,
            "status": status,
            "started_ts": started_ts
        }
        if not req.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        data.setdefault("etl_runs", []).append(record)
        payload = {"status": "inserted", "run_id": record.get("run_id")}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "registerEtlRun",
                "description": "Appends an etl_runs record.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }
