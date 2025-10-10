# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _load_table


class WriteWorkflowRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        runs = _load_table(data, "workflow_runs")
        run = {
            "dag_name": kwargs.get("dag_name"),
            "status": kwargs.get("status"),
            "report_id": kwargs.get("report_id"),
        }
        runs.append(run)
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "write_workflow_run", "description": "Writes a workflow run row.", "parameters": {"type": "object", "properties": {"dag_name": {"type": "string"}, "status": {"type": "string"}, "report_id": {"type": "string"}}, "required": ["dag_name", "status"]}}}
