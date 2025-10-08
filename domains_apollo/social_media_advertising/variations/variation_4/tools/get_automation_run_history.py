from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetAutomationRunHistory(Tool):
    """Fetches the history of automation runs for review and monitoring."""

    @staticmethod
    def invoke(data: dict[str, Any], run_type: str = None, status: str = None, limit: int = 10) -> str:
        runs = data.get("automation_runs", [])

        # Apply filter based on run type if provided
        if run_type:
            runs = [r for r in runs if r.get("run_type") == run_type]

        # Apply filter based on status if provided
        if status:
            runs = [r for r in runs if r.get("status") == status]

        # Order by started_at (latest first) and restrict results
        runs.sort(key=lambda x: x.get("started_at", ""), reverse=True)
        runs = runs[:limit]

        # Compute summary statistics
        total_runs = len(runs)
        success_count = len([r for r in runs if r.get("status") == "completed"])
        failure_count = len([r for r in runs if r.get("status") == "failed"])
        success_rate = (
            round((success_count / total_runs * 100), 2) if total_runs > 0 else 0
        )

        result = {
            "summary": {
                "total_runs": total_runs,
                "success_count": success_count,
                "failure_count": failure_count,
                "success_rate_percent": success_rate,
            },
            "runs": runs,
        }
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAutomationRunHistory",
                "description": "Retrieves automation run history with filtering and summary statistics for monitoring and analysis.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_type": {
                            "type": "string",
                            "description": "Filter by specific automation type (e.g., 'plan_freeze', 'budget_apply').",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by run status (e.g., 'completed', 'failed', 'started').",
                        },
                        "limit": {
                            "type": "number",
                            "description": "Maximum number of runs to return (default: 10).",
                        },
                    },
                    "required": [],
                },
            },
        }
