from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class UpdateSupplierContact(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, phone: str = None, email: str = None, contact_info: dict = None) -> str:
        if not supplier_id:
            payload = {"error": "supplier_id is required"}
            out = json.dumps(payload)
            return out

        suppliers = data["suppliers"]
        supplier = next((s for s in suppliers if s["supplier_id"] == supplier_id), None)

        if not supplier:
            payload = {"error": f"Supplier {supplier_id} not found"}
            out = json.dumps(payload)
            return out

        if contact_info:
            old_contact = supplier["contact_info"].copy()
            supplier["contact_info"] = contact_info
        else:
            if not phone and not email:
                payload = {"error": "At least one of phone or email is required"}
                out = json.dumps(payload)
                return out
            old_contact = supplier["contact_info"].copy()

            if phone:
                supplier["contact_info"]["phone"] = phone
            if email:
                supplier["contact_info"]["email"] = email
        payload = {
                "success": True,
                "supplier_id": supplier_id,
                "old_contact": old_contact,
                "new_contact": supplier["contact_info"],
                "updated_at": get_current_timestamp(),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateSupplierContact",
                "description": "Update contact information for a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID to update",
                        },
                        "phone": {"type": "string", "description": "New phone number"},
                        "email": {"type": "string", "description": "New email address"},
                        "contact_info": {
                            "type": "object",
                            "description": "Complete contact information object",
                            "properties": {
                                "phone": {
                                    "type": "string",
                                    "description": "Phone number",
                                },
                                "email": {
                                    "type": "string",
                                    "description": "Email address",
                                },
                            },
                        },
                    },
                    "required": ["supplier_id"],
                },
            },
        }
