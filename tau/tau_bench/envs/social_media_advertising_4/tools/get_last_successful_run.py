# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLastSuccessfulRun(Tool):
    """Finds when a job type last completed successfully."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_type = kwargs.get("run_type")
        successful_runs = [r for r in data.get('automation_runs', []) if r.get('run_type') == run_type and r.get('status') == 'completed']
        if not successful_runs:
            return json.dumps({"error": f"No successful run found for type '{run_type}'."})
        last_run = max(successful_runs, key=lambda x: x['ended_at'])
        return json.dumps(last_run)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_last_successful_run", "description": "Reads the automation log to find when a specific job type last completed successfully.", "parameters": {"type": "object", "properties": {"run_type": {"type": "string"}}, "required": ["run_type"]}}}
