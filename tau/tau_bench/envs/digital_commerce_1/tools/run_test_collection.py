# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table








def _stable_id(prefix: str, *parts: str) -> str:
    base = "-".join(_slugify(p) for p in parts if p is not None and str(p) != "")
    return f"{prefix}-{base}" if base else prefix

def _json(x: Any) -> str:
    return json.dumps(x, separators=(",", ":"))

def _ensure_table(db: Dict[str, Any], name: str):
    if name not in db:
        db[name] = []
    return db[name]

class RunTestCollection(Tool):
    @staticmethod
    def invoke(data, environment: str, collection_name: str = "SMOKE") -> str:
        tests = _ensure_table(data, "test_runs")
        run_id = _stable_id("run", collection_name, environment, FIXED_NOW)
        tests.append(
            {
                "run_id": run_id,
                "collection_name": collection_name,
                "environment": environment,
                "status": "Running",
                "created_at": FIXED_NOW,
            }
        )
        return _json({"run_id": run_id})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "run_test_collection",
                "description": "Execute a named API test collection. Defaults to 'SMOKE'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {"type": "string", "enum": ["DEV", "UAT", "PROD"]},
                        "collection_name": {"type": "string", "default": "SMOKE"},
                    },
                    "required": ["environment"],
                },
            },
        }