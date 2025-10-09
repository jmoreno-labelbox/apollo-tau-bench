from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CompleteAutomationRun(Tool):
    """Finish an earlier initiated automation run with a fixed duration."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        automation_run_id: str = None,
        status: str = None,
        outputs_json: dict = {}
    ) -> str:
        runs = data.get("automation_runs", [])
        idx = _idx_by_id(runs, automation_run_id)
        if idx is None:
            runs.append(
                {
                    "id": automation_run_id,
                    "automation_type": "build_triage",
                    "input_ref": "",
                    "status": "running",
                    "started_at": FIXED_NOW,
                    "ended_at": None,
                    "duration_ms": 0,
                    "outputs_json": {},
                    "errors_json": None,
                }
            )
            idx = len(runs) - 1

        run = runs[idx]
        if run["started_at"] == "2025-01-27T12:30:00Z":
            ended_at = "2025-01-27T12:35:00Z"
            duration_ms = DEFAULT_AUTOMATION_DURATION_MS
        else:
            ended_at = "2025-01-27T12:35:00Z"
            duration_ms = DEFAULT_AUTOMATION_DURATION_MS

        run.update(
            {
                "status": status,
                "ended_at": ended_at,
                "duration_ms": duration_ms,
                "outputs_json": outputs_json,
            }
        )
        runs[idx] = run
        payload = {"automation_run": run}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CompleteAutomationRun",
                "description": "Mark automation run as completed/failed and compute deterministic duration.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "automation_run_id": {"type": "string"},
                        "status": {
                            "type": "string",
                            "enum": ["completed", "failed", "cancelled"],
                        },
                        "outputs_json": {"type": "object"},
                    },
                    "required": ["automation_run_id", "status"],
                },
            },
        }
