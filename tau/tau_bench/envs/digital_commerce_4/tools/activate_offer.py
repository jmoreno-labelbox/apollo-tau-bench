from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ActivateOffer(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], offer_id: str, is_active: bool) -> str:
        offer_id = _sid(offer_id)
        offers = data.get("offers", {}).values()
        off = next((o for o in offers.values() if o.get("offer_id") == offer_id), None)
        if not off:
            payload = {"error": f"offer {offer_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        off["is_active"] = bool(is_active)
        _append_audit(data, "ACTIVATE_OFFER", offer_id, {"is_active": bool(is_active)})
        _ws_append(data, offer_id, "ACTIVATE_OFFER", {"is_active": bool(is_active)})
        payload = off
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "activateOffer",
                "description": "Activate or deactivate an offer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "offer_id": {"type": "string"},
                        "is_active": {"type": "boolean"},
                    },
                    "required": ["offer_id", "is_active"],
                },
            },
        }
