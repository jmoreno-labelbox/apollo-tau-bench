from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DeleteAdSet(Tool):
    """Removes an ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        if not adset_id:
            payload = {"error": "adset_id is a required parameter."}
            out = json.dumps(payload)
            return out

        adsets = data.get("adsets", {}).values()
        for adset in adsets.values():
            if adset.get("adset_id") == adset_id:
                data["adsets"] = [
                    d for d in data["adsets"].values() if d["adset_id"] != adset_id
                ]
                payload = {
                        "status": "success",
                        "message": f"Ad set with id {adset_id} deleted successfully",
                    }
                out = json.dumps(
                    payload)
                return out
        payload = {"error": f"Ad set with ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteAdset",
                "description": "Deletes an ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set to delete.",
                        },
                    },
                    "required": ["adset_id"],
                },
            },
        }
