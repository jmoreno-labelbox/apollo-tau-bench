# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RegisterEtlRun(Tool):
    """
    Appends an etl_runs record.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        req = {"run_id", "input_paths", "output_paths", "status", "started_ts"}
        if not req.issubset(set(record.keys())):
            return json.dumps({"error": "missing required fields"})
        data.setdefault("etl_runs", []).append(record)
        return json.dumps({"status": "inserted", "run_id": record.get("run_id")})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "register_etl_run",
                "description": "Appends an etl_runs record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object"}
                    },
                    "required": ["record"]
                }
            }
        }
