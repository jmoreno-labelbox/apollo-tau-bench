from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class LogETLRun(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        run_name: str = None,
        task: str = None,
        status: str = None,
        rows_processed: int = None
    ) -> str:
        runs = data.get("etl_runs", {}).values()
        max_id = 0
        for r in runs:
            try:
                rid = int(r.get("run_id", 0))
                if rid > max_id:
                    max_id = rid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "run_id": new_id,
            "run_name": run_name,
            "task": task,
            "status": status,
            "rows_processed": rows_processed,
            "started_at": _fixed_now_iso(),
            "finished_at": _fixed_now_iso(),
        }
        data["etl_runs"][row["etl_run_id"]] = row
        payload = {"run_id": new_id, "run_name": row["run_name"]}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterEtlRun",
                "description": "Insert a new ETL run record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_name": {"type": "string"},
                        "task": {"type": "string"},
                        "status": {"type": "string"},
                        "rows_processed": {"type": ["integer", "null"]},
                    },
                    "required": ["run_name", "task", "status"],
                },
            },
        }
