# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAutomationRunHistory(Tool):
    """Retrieves automation run history for analysis and monitoring."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_type = kwargs.get("run_type")
        status_filter = kwargs.get("status", None)
        limit = kwargs.get("limit", 10)

        runs = data.get('automation_runs', [])

        # Apply filter based on the specified run type.
        if run_type:
            runs = [r for r in runs if r.get('run_type') == run_type]

        # Apply status filter if provided.
        if status_filter:
            runs = [r for r in runs if r.get('status') == status_filter]

        # Order by started_at in descending order and restrict the number of results.
        runs.sort(key=lambda x: x.get('started_at', ''), reverse=True)
        runs = runs[:limit]

        # Compute descriptive statistics.
        total_runs = len(runs)
        success_count = len([r for r in runs if r.get('status') == 'completed'])
        failure_count = len([r for r in runs if r.get('status') == 'failed'])
        success_rate = round((success_count / total_runs * 100), 2) if total_runs > 0 else 0

        result = {
            "summary": {
                "total_runs": total_runs,
                "success_count": success_count,
                "failure_count": failure_count,
                "success_rate_percent": success_rate
            },
            "runs": runs
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_automation_run_history", "description": "Retrieves automation run history with filtering and summary statistics for monitoring and analysis.", "parameters": {"type": "object", "properties": {"run_type": {"type": "string", "description": "Filter by specific automation type (e.g., 'plan_freeze', 'budget_apply')."}, "status": {"type": "string", "description": "Filter by run status (e.g., 'completed', 'failed', 'started')."}, "limit": {"type": "number", "description": "Maximum number of runs to return (default: 10)."}}, "required": []}}}
