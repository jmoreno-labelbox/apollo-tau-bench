from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FetchEtlExecution(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None, run_name: str = None) -> str:
        runs = data.get("etl_runs", {}).values() or []
        row = None
        if run_id is not None:
            row = next((r for r in runs.values() if str(r.get("run_id")) == str(run_id)), None)
        elif run_name:
            row = next((r for r in runs.values() if r.get("run_name") == run_name), None)
        payload = row or {"error": "ETL run not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchEtlExecution",
                "description": "Read an ETL execution by id or run_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "run_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
