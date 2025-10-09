from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListCarriersByMode(Tool):
    """A utility to identify all active carriers that facilitate a specific transport mode."""

    @staticmethod
    def invoke(data: dict[str, Any], mode: str = None) -> str:
        if not mode:
            payload = {"error": "mode is a required argument."}
            out = json.dumps(payload, indent=2)
            return out
        carriers = data.get("carriers", {}).values()
        matching_carriers = [
            c
            for c in carriers.values() if c.get("active_status") is True
            and mode.title() in c.get("supported_modes", [])
        ]
        payload = matching_carriers
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListCarriersByMode",
                "description": "Finds all active carriers for a given transportation mode.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mode": {
                            "type": "string",
                            "description": "The mode of transport to filter by (e.g., 'Air', 'Sea').",
                        }
                    },
                    "required": ["mode"],
                },
            },
        }
