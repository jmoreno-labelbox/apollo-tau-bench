from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class GetAutomationRunHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_type: str = None) -> str:
        pass
        #optional filters based on type
        runs = _assert_table(data, "automation_runs")
        out = [r for r in runs.values() if (run_type is None or r.get("run_type") == run_type)]
        payload = out
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAutomationRunHistory",
                "description": "Read automation_runs (optionally filter by run_type).",
                "parameters": {
                    "type": "object",
                    "properties": {"run_type": {"type": "string"}},
                },
            },
        }
