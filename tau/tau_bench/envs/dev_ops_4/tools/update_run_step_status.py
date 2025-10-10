# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateRunStepStatus(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "update_run_step_status",
                "description": "Updates the status or fields of an existing run step.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "step_id": {"type": "string", "description": "Step id to update"},
                        "status": {"type": "string", "description": "New status"},
                        "exit_code": {"type": "integer", "description": "Optional exit code"},
                        "duration_ms": {"type": "integer", "description": "Optional duration"},
                        "log_uri": {"type": "string", "description": "Optional log location"}
                    },
                    "required": ["run_id", "step_id"]
                }
            }
        }

    @staticmethod
    def invoke(data, run_id, step_id):
        runs = list(data.get("build_runs", {}).values())
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        steps = run.get("steps") or []
        step = next((s for s in steps if s.get("id") == step_id), None)
        if not step:
            return json.dumps({"error": "step_not_found", "run_id": run_id, "step_id": step_id})
        for k in ["status", "exit_code", "duration_ms", "log_uri"]:
            if k in kwargs and kwargs.get(k) is not None:
                step[k] = kwargs.get(k)
        run["steps"] = steps
        return json.dumps({"run": run}, indent=2)
