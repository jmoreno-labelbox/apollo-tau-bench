from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateWarehouseNotes(Tool):
    """Inserts or replaces notes for a particular warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str = None, notes: str = None) -> str:
        if not all([warehouse_id, notes]):
            payload = {"error": "warehouse_id and notes are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        warehouse = next(
            (
                w
                for w in data.get("warehouses", {}).values()
                if w.get("warehouse_id") == warehouse_id
            ),
            None,
        )
        if not warehouse:
            payload = {"error": f"Warehouse '{warehouse_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        new_note = f"{notes}"
        if "notes" in warehouse and warehouse["notes"]:
            warehouse["notes"] += f"\n{new_note}"
        else:
            warehouse["notes"] = new_note
        payload = warehouse
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateWarehouseNotes",
                "description": "Adds a new note to a specific warehouse's record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["warehouse_id", "notes"],
                },
            },
        }
