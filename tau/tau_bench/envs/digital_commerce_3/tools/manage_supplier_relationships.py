from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ManageSupplierRelationships(Tool):
    """Oversee relationships with suppliers and procurement processes."""

    @staticmethod
    def invoke(
        data: dict[str, Any], supplier_name: Any, action: Any, contact_email: str = None, supplier_data: Any = {}
    ) -> str:
        pass
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
                "contact_email": contact_email,
                "rating": 4.0,
                "status": "active",
                "added_at": FIXED_NOW,
            }
            data["suppliers"][supplier_id] = supplier

        result = {
            "supplier_name": supplier_name,
            "action": action,
            "status": "completed",
        }

        _append_audit(data, "supplier_managed", supplier_name, {"action": action})
        payload = result
        out = json.dumps(payload, indent=2)
        return out
        pass
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
            data["suppliers"][supplier_id] = supplier

        result = {
            "supplier_name": supplier_name,
            "action": action,
            "status": "completed",
        }

        _append_audit(data, "supplier_managed", supplier_name, {"action": action})
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageSupplierRelationships",
                "description": "Manage supplier relationships and procurement workflows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_name": {"type": "string"},
                        "action": {"type": "string"},
                        "supplier_data": {"type": "object"},
                    },
                    "required": ["supplier_name", "action"],
                },
            },
        }
