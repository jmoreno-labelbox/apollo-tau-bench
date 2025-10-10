# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateWarehouseNotes(Tool):
    """Adds or overwrites notes for a specific warehouse."""
    @staticmethod
    def invoke(data: Dict[str, Any], notes, warehouse_id) -> str:
        if not all([warehouse_id, notes]):
            return json.dumps({"error": "warehouse_id and notes are required."}, indent=2)
        warehouse = next((w for w in data.get('warehouses', []) if w.get('warehouse_id') == warehouse_id), None)
        if not warehouse:
            return json.dumps({"error": f"Warehouse '{warehouse_id}' not found."}, indent=2)
        new_note = f"{notes}"
        if 'notes' in warehouse and warehouse['notes']:
            warehouse['notes'] += f"\n{new_note}"
        else:
            warehouse['notes'] = new_note
        return json.dumps(warehouse, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_warehouse_notes", "description": "Adds a new note to a specific warehouse's record.", "parameters": {"type": "object", "properties": {"warehouse_id": {"type": "string"}, "notes": {"type": "string"}}, "required": ["warehouse_id", "notes"]}}}
