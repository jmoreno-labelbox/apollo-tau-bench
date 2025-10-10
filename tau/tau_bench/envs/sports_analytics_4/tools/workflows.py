# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Workflows(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        runs = _load_table(data, "workflow_runs")
        run = {
            "dag_name": kwargs.get("dag_name"),
            "status": kwargs.get("status"),
            "report_id": kwargs.get("report_id"),
        }
        runs.append(run)
        # return result
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {"type": "function", "function": {"name": "wrokingRun", "description": "Persists a workflow run row.", "parameters": {"type": "object", "properties": {"dag_name": {"type": "string"}, "status": {"type": "string"}, "report_id": {"type": "string"}}, "required": ["dag_name", "status"]}}}
