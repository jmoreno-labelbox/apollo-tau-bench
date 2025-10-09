from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCarrierDetails(Tool):
    """Fetches complete details for a single carrier using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], carrier_name: str = None) -> str:
        if not carrier_name:
            payload = {"error": "carrier_name is required."}
            out = json.dumps(payload, indent=2)
            return out
        carrier = next(
            (
                c
                for c in data.get("carriers", {}).values()
                if carrier_name.lower() in c.get("carrier_name", "").lower()
            ),
            None,
        )
        if not carrier:
            payload = {"error": f"Carrier '{carrier_name}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = carrier
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCarrierDetails",
                "description": "Retrieves the full details for a single carrier by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"carrier_name": {"type": "string"}},
                    "required": ["carrier_name"],
                },
            },
        }
