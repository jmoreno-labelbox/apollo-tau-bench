from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateRunStepStatus(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateRunStepStatus",
                "description": "Updates the status or fields of an existing run step.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "step_id": {
                            "type": "string",
                            "description": "Step id to update",
                        },
                        "status": {"type": "string", "description": "New status"},
                        "exit_code": {
                            "type": "integer",
                            "description": "Optional exit code",
                        },
                        "duration_ms": {
                            "type": "integer",
                            "description": "Optional duration",
                        },
                        "log_uri": {
                            "type": "string",
                            "description": "Optional log location",
                        },
                    },
                    "required": ["run_id", "step_id"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, step_id=None, status=None, exit_code=None, duration_ms=None, log_uri=None):
        run_id = run_id
        step_id = step_id
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        steps = run.get("steps") or []
        step = next((s for s in steps if s.get("id") == step_id), None)
        if not step:
            payload = {"error": "step_not_found", "run_id": run_id, "step_id": step_id}
            out = json.dumps(payload)
            return out
        for k, v in [("status", status), ("exit_code", exit_code), ("duration_ms", duration_ms), ("log_uri", log_uri)]:
            if v is not None:
                step[k] = v
        run["steps"] = steps
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
