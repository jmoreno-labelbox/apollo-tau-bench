from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddRunStep(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddRunStep",
                "description": "Adds a step entry to a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "step_id": {"type": "string", "description": "Unique step id"},
                        "name": {
                            "type": "string",
                            "description": "Human readable step name",
                        },
                        "status": {
                            "type": "string",
                            "description": "pending|running|completed|failed",
                            "enum": ["pending", "running", "completed", "failed"],
                        },
                        "started_at": {
                            "type": "string",
                            "description": "ISO8601 start time",
                        },
                        "ended_at": {
                            "type": "string",
                            "description": "ISO8601 end time",
                        },
                    },
                    "required": ["run_id", "step_id", "name", "status"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, step_id=None, name=None, status=None, started_at=None, ended_at=None):
        step = {
            "id": step_id,
            "name": name,
            "status": status,
            "started_at": started_at,
            "ended_at": ended_at,
        }
        runs = data.get("build_runs", {}).values()
        run = next((r for r in runs.values() if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        steps = run.get("steps") or []
        steps.append(step)
        run["steps"] = steps
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
