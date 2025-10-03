from tau_bench.envs.tool import Tool
import json
from typing import Any

class Workflows(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], dag_name: str = None, status: str = None, report_id: str = None,
    game_pk: Any = None,
    final_output: str = None,
    ) -> str:
        runs = _load_table(data, "workflow_runs")
        run = {
            "dag_name": dag_name,
            "status": status,
            "report_id": report_id,
        }
        runs.append(run)
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "wrokingRun",
                "description": "Persists a workflow run row.",
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
