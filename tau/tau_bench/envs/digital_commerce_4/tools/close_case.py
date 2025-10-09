from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CloseCase(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], case_id: str, resolution: str) -> str:
        case_id = _sid(case_id)
        cases = data.get("cases", {}).values()
        c = next((x for x in cases.values() if x.get("case_id") == case_id), None)
        if not c:
            payload = {"error": f"case {case_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        c["status"] = "Resolved"
        c["resolution"] = resolution
        _append_audit(data, "CLOSE_CASE", case_id, {"resolution": resolution})
        _ws_append(data, case_id, "CLOSE_CASE", {"resolution": resolution})
        payload = c
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "closeCase",
                "description": "Close a case with a resolution.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_id": {"type": "string"},
                        "resolution": {"type": "string"},
                    },
                    "required": ["case_id", "resolution"],
                },
            },
        }
