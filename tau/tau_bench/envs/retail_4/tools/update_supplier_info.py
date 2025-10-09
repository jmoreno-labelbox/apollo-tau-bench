from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateSupplierInfo(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_id: str,
        contact_updates: dict[str, str] = None,
        performance_rating: float = None,
        notes: str = None,
    ) -> str:
        """
        Update supplier contact information and performance metrics

        Writes to: suppliers.json (updates existing supplier contact_info and adds performance data)
        Data Sources: suppliers.json (supplier_id, name, contact_info)
        """
        suppliers = data.get("suppliers", [])
        supplier_to_update = None
        supplier_index = None

        # Find the supplier
        for i, supplier in enumerate(suppliers):
            if supplier.get("supplier_id") == supplier_id:
                supplier_to_update = supplier
                supplier_index = i
                break

        if not supplier_to_update:
            payload = {"error": f"Supplier {supplier_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # WRITE OPERATION: Update supplier information
        updates_applied = []

        if contact_updates:
            current_contact = supplier_to_update.get("contact_info", {})

            if "phone" in contact_updates:
                current_contact["phone"] = contact_updates["phone"]
                updates_applied.append("phone")

            if "email" in contact_updates:
                current_contact["email"] = contact_updates["email"]
                updates_applied.append("email")

            supplier_to_update["contact_info"] = current_contact

        # Add performance tracking
        if performance_rating is not None:
            if not (0.0 <= performance_rating <= 5.0):
                payload = {
                    "error": "Performance rating must be between 0.0 and 5.0",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

            if "performance_metrics" not in supplier_to_update:
                supplier_to_update["performance_metrics"] = {}

            supplier_to_update["performance_metrics"]["rating"] = performance_rating
            supplier_to_update["performance_metrics"][
                "last_updated"
            ] = datetime.now().isoformat()
            updates_applied.append("performance_rating")

        if notes:
            supplier_to_update["notes"] = notes
            updates_applied.append("notes")

        supplier_to_update["last_updated"] = datetime.now().isoformat()

        # Update the supplier in the data structure
        data["suppliers"][supplier_index] = supplier_to_update

        result = {
            "status": "success",
            "supplier_id": supplier_id,
            "supplier_name": supplier_to_update.get("name"),
            "updates_applied": updates_applied,
            "updated_contact_info": supplier_to_update.get("contact_info", {}),
            "performance_rating": supplier_to_update.get("performance_metrics", {}).get(
                "rating"
            ),
            "last_updated": supplier_to_update["last_updated"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSupplierInfo",
                "description": "Update supplier contact information and performance metrics",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier identifier (e.g., '#SUP0001')",
                        },
                        "contact_updates": {
                            "type": "object",
                            "properties": {
                                "phone": {"type": "string"},
                                "email": {"type": "string"},
                            },
                            "description": "Contact information updates",
                        },
                        "performance_rating": {
                            "type": "number",
                            "description": "Performance rating between 0.0 and 5.0",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Additional notes about supplier",
                        },
                    },
                    "required": ["supplier_id"],
                },
            },
        }
