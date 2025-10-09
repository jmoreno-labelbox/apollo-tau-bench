from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class record_automation_run(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        ended_at: str = None,
        request_id: str = None,
        started_at: str = None,
        status: str = None,
        task_name: str = None,
        timestamp: str = None
    ) -> str:
        p = _params(data, {
            "task_name": task_name,
            "status": status,
            "request_id": request_id,
            "started_at": started_at,
            "ended_at": ended_at,
            "timestamp": timestamp
        })
        miss = _require(p, ["task_name", "status", "request_id"])
        if miss:
            return miss
        run_id = f"run_{p['request_id']}"
        _ensure(data, "automation_runs", []).append(
            {
                "run_id": run_id,
                "task_name": p["task_name"],
                "status": p["status"],
                "started_at": p.get("started_at"),
                "ended_at": p.get("ended_at"),
                "timestamp": p.get("timestamp"),
            }
        )
        return _ok({"run_id": run_id, "status": p["status"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordAutomationRun",
                "description": "Record a deterministic automation run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_name": {"type": "string"},
                        "status": {"type": "string"},
                        "started_at": {"type": "string"},
                        "ended_at": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["task_name", "status", "request_id"],
                },
            },
        }
