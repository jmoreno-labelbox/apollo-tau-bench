from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetAutomationRun(Tool):
    """Retrieve an automation run using id."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        rows = _table(data, "automation_runs")
        row = next((r for r in rows if r.get("id") == id), None)
        return _ok({"automation_run": row}) if row else _err("automation_run not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAutomationRun",
                "description": "Fetch an automation run by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
