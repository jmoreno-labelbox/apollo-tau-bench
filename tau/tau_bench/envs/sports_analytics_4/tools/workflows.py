# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Workflows(Tool):
    @staticmethod
        # primary execution method
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        runs = _load_table(data, "workflow_runs")
        run = {
            "dag_name": kwargs.get("dag_name"),
            "status": kwargs.get("status"),
            "report_id": kwargs.get("report_id"),
        }
        runs.append(run)
        # return output
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return output
        return {"type": "function", "function": {"name": "wrokingRun", "description": "Persists a workflow run row.", "parameters": {"type": "object", "properties": {"dag_name": {"type": "string"}, "status": {"type": "string"}, "report_id": {"type": "string"}}, "required": ["dag_name", "status"]}}}
