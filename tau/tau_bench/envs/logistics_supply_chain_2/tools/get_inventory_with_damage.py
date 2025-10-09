from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetInventoryWithDamage(Tool):
    """Utility for obtaining inventory items that have a quantity damaged greater than zero."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        threshold: int = None,
        less_than_threshold: str = "False",
        list_of_ids: list = None
    ) -> str:
        inventories = data.get("inventory", [])
        if threshold:
            if less_than_threshold == "True":
                damaged = [
                    [item["inventory_id"], item["quantity_damaged"]]
                    for item in inventories
                    if item["quantity_damaged"] < threshold
                ]
            else:
                damaged = [
                    [item["inventory_id"], item["quantity_damaged"]]
                    for item in inventories
                    if item["quantity_damaged"] > threshold
                ]
        else:
            if less_than_threshold == "True":
                damaged = [
                    [item["inventory_id"], item["quantity_damaged"]]
                    for item in inventories
                    if item["quantity_damaged"] < 0
                ]
            else:
                damaged = [
                    [item["inventory_id"], item["quantity_damaged"]]
                    for item in inventories
                    if item["quantity_damaged"] > 0
                ]
        if list_of_ids:
            damaged = [d for d in damaged if d[0] in list_of_ids]
        payload = damaged
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryWithDamage",
                "description": "Retrieve inventory items that have damaged stock.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of inventories to choose from.",
                        },
                        "threshold": {
                            "type": "number",
                            "description": "Threshold value of quantity damaged.",
                        },
                        "less_than_threshold": {
                            "type": "string",
                            "description": "'True' means value compared less than threshold.",
                        },
                    },
                },
            },
        }
