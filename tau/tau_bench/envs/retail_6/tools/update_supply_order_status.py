from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateSupplyOrderStatus(Tool):
    """Update the status of a supply order."""

    @staticmethod
    def invoke(data, supply_order_id=None, status=None) -> str:
        if not supply_order_id or not status:
            payload = {"error": "supply_order_id and status are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        so = next(
            (
                s
                for s in data.get("supply_orders", {}).values()
                if s.get("supply_order_id") == supply_order_id
            ),
            None,
        )
        if not so:
            payload = {"error": f"supply_order_id {supply_order_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        so["status"] = status
        payload = {"success": True, "supply_order_id": supply_order_id, "status": status}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateSupplyOrderStatus",
                "description": "Update a supply order's status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["supply_order_id", "status"],
                },
            },
        }
