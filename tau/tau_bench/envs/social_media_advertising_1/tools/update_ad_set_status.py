from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateAdSetStatus(Tool):
    """Modifies the status of a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, new_status: str = None) -> str:
        adsets = data.get("adsets", {}).values()
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                old_status = adset["status"]
                adset["status"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Ad set status updated from '{old_status}' to '{new_status}'",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set {adset_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdsetStatus",
                "description": "Updates the status for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["adset_id", "new_status"],
                },
            },
        }
