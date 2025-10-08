from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListTimeEntries(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None, month: str = None) -> str:
        pid = project_id
        entries = [
            t for t in data.get("time_entries", []) if t.get("project_id") == pid
        ]
        if month:
            entries = [
                t for t in entries if str(t.get("entry_date", "")).startswith(month)
            ]
        payload = {"project_id": pid, "month": month, "time_entries": entries}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListTimeEntries",
                "description": "List time entries filtered by project and optional month.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "month": {"type": "string"},
                    },
                    "required": ["project_id"],
                },
            },
        }
