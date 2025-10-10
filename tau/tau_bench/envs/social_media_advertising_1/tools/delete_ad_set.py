# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteAdSet(Tool):
    """Deletes an ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], adset_id) -> str:
        if not adset_id:
            return json.dumps({"error": "adset_id is a required parameter."})

        adsets = list(data.get("adsets", {}).values())
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                data['adsets'] = [d for d in data['adsets'] if d['adset_id'] != adset_id]
                return json.dumps(
                    {
                        "status": "success",
                        "message": f"Ad set with id {adset_id} deleted successfully",
                    }
                )

        return json.dumps({"error": f"Ad set with ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_adset",
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
