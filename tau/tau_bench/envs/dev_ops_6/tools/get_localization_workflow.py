from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetLocalizationWorkflow(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        wid = id
        rows = _table(data, "localization_workflow")
        row = next((r for r in rows if r.get("id") == wid), None)
        return (
            _ok({"localization_workflow": row})
            if row
            else _err("localization_workflow not found")
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLocalizationWorkflow",
                "description": "Fetch localization_workflow by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
