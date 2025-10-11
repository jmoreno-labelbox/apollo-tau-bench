# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _load_table




def _load_table(data: Dict[str, Any], table: str) -> List[Dict[str, Any]]:
    return data.get(table, [])

class WriteWorkflowRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], dag_name, report_id, status) -> str:
        runs = _load_table(data, "workflow_runs")
        run = {
            "dag_name": dag_name,
            "status": status,
            "report_id": report_id,
        }
        runs.append(run)
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "write_workflow_run", "description": "Writes a workflow run row.", "parameters": {"type": "object", "properties": {"dag_name": {"type": "string"}, "status": {"type": "string"}, "report_id": {"type": "string"}}, "required": ["dag_name", "status"]}}}