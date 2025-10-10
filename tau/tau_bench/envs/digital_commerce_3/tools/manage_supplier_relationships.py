# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import FIXED_NOW


class ManageSupplierRelationships(Tool):
    """Manage supplier relationships and procurement workflows."""

    @staticmethod
    def invoke(
        data: Dict[str, Any], supplier_name: Any, action: Any, supplier_data: Any = {}
    ) -> str:
        supplier_name = supplier_name
        action = action
        supplier_data = supplier_data

        if not supplier_name or not action:
            return _error("supplier_name and action are required.")

        suppliers = data.setdefault("suppliers", [])

        if action == "add":
            supplier = {
                "supplier_id": f"SUP_{len(suppliers) + 1:03d}",
                "supplier_name": supplier_name,
                "contact_email": supplier_data.get("contact_email"),
                "rating": 4.0,
                "status": "active",
                "added_at": FIXED_NOW,
            }
            suppliers.append(supplier)

        result = {"supplier_name": supplier_name, "action": action, "status": "completed"}

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_supplier_relationships",
                "description": "Manage supplier relationships and procurement workflows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_name": {"type": "string"},
                        "action": {"type": "string", "enum": ["add"]},
                        "supplier_data": {"type": "object"},
                    },
                    "required": ["supplier_name", "action"],
                },
            },
        }
