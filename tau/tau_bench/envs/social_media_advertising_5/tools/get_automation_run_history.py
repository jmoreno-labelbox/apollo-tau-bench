from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAutomationRunHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_type: str = None, status: str = None, limit: int = 10) -> str:
        runs = data.get("automation_runs", [])
        if run_type:
            runs = [r for r in runs if r.get("run_type") == run_type]
        if status:
            runs = [r for r in runs if r.get("status") == status]
        runs.sort(key=lambda x: x.get("started_at", ""), reverse=True)
        runs = runs[:limit]
        total = len(runs)
        succ = len([r for r in runs if r.get("status") == "completed"])
        fail = len([r for r in runs if r.get("status") == "failed"])
        rate = round((succ / total * 100), 2) if total > 0 else 0
        payload = {
                "summary": {
                    "total_runs": total,
                    "success_count": succ,
                    "failure_count": fail,
                    "success_rate_percent": rate,
                },
                "runs": runs,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAutomationRunHistory",
                "description": "Gets automation runs with summary.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_type": {"type": "string"},
                        "status": {"type": "string"},
                        "limit": {"type": "number"},
                    },
                    "required": [],
                },
            },
        }
