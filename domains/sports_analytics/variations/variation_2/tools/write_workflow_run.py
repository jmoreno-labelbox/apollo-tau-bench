from tau_bench.envs.tool import Tool
import json
from typing import Any

class WriteWorkflowRun(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        runs = _load_table(data, "workflow_runs")
        run = {
            "dag_name": kwargs.get("dag_name"),
            "status": kwargs.get("status"),
            "report_id": kwargs.get("report_id"),
        }
        runs.append(run)
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteWorkflowRun",
                "description": "Writes a workflow run row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dag_name": {"type": "string"},
                        "status": {"type": "string"},
                        "report_id": {"type": "string"},
                    },
                    "required": ["dag_name", "status"],
                },
            },
        }
