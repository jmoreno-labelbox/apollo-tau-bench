# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogEtlExecution(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        runs = data.get("etl_runs", [])
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
            "run_name": kwargs.get("run_name"),
            "task": kwargs.get("task"),
            "status": kwargs.get("status"),
            "rows_processed": kwargs.get("rows_processed"),
            "started_at": _now_iso_fixed(),
            "finished_at": _now_iso_fixed(),
        }
        runs.append(row)
        return json.dumps({"run_id": new_id, "run_name": row["run_name"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "log_etl_execution",
            "description": "Record an ETL execution row.",
            "parameters": {"type": "object", "properties": {
                "run_name": {"type": "string"},
                "task": {"type": "string"},
                "status": {"type": "string"},
                "rows_processed": {"type": ["integer", "null"]}
            }, "required": ["run_name", "task", "status"]}
        }}
