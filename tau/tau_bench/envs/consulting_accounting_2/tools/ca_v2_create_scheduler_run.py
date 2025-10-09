from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2CreateSchedulerRun(Tool):
    """Generate an entry for the scheduler run log."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None, task_name: str = None, scheduled_for: str = None, executed_at: str = None, status: str = None, log_path: str = None) -> str:
        if not all([task_name, status]):
            return _error("Required fields: task_name, status")

        scheduler_run = {
            "run_id": run_id or f"RUN{len(data.get('scheduler_runs', [])) + 1:03d}",
            "task_name": task_name,
            "scheduled_for": scheduled_for,
            "executed_at": executed_at,
            "status": status,
            "log_path": log_path,
        }

        data.setdefault("scheduler_runs", []).append(scheduler_run)

        return _ok(run_id=run_id, task_name=task_name, status=status)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateSchedulerRun",
                "description": "Create a scheduler run log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "task_name": {"type": "string"},
                        "scheduled_for": {"type": "string"},
                        "executed_at": {"type": "string"},
                        "status": {"type": "string"},
                        "log_path": {"type": "string"},
                    },
                    "required": ["task_name", "status"],
                },
            },
        }
