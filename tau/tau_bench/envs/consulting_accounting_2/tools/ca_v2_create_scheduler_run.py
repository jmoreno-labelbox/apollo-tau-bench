# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2CreateSchedulerRun(Tool):
    """Create a scheduler run log entry."""

    @staticmethod
    def invoke(data: Dict[str, Any], executed_at, log_path, run_id, scheduled_for, status, task_name) -> str:

        if not all([task_name, status]):
            return _error("Required fields: task_name, status")

        scheduler_run = {
            "run_id": run_id or f"RUN{len(data.get('scheduler_runs', [])) + 1:03d}",
            "task_name": task_name,
            "scheduled_for": scheduled_for,
            "executed_at": executed_at,
            "status": status,
            "log_path": log_path
        }

        # Ensure scheduler_runs is a list before appending
        if "scheduler_runs" not in data:
            data["scheduler_runs"] = []
        elif not isinstance(data["scheduler_runs"], list):
            data["scheduler_runs"] = list(data["scheduler_runs"].values()) if isinstance(data["scheduler_runs"], dict) else []
        data["scheduler_runs"].append(scheduler_run)

        return _ok(run_id=run_id, task_name=task_name, status=status)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_scheduler_run",
                "description": "Create a scheduler run log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "task_name": {"type": "string"},
                        "scheduled_for": {"type": "string"},
                        "executed_at": {"type": "string"},
                        "status": {"type": "string"},
                        "log_path": {"type": "string"}
                    },
                    "required": ["task_name", "status"],
                },
            },
        }
