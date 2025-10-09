from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class find_work_item_by_crash_fingerprint(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], fingerprint: str) -> str:
        pass
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("metadata") and fingerprint in item["metadata"].get(
                "crash_fingerprint", ""
            ):
                payload = item
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Work item with crash fingerprint '{fingerprint}' not found"}
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindWorkItemByCrashFingerprint",
                "description": "Finds a work item by its associated crash fingerprint.",
                "parameters": {
                    "type": "object",
                    "properties": {"fingerprint": {"type": "string"}},
                    "required": ["fingerprint"],
                },
            },
        }
