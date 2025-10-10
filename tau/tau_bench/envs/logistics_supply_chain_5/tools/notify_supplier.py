# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class NotifySupplier(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str, notification_type: str) -> str:
        suppliers = data.get("supplier_master", [])

        supplier = next((s for s in suppliers if s.get("supplier_id") == supplier_id), None)
        if not supplier:
            return json.dumps({"error": f"Supplier {supplier_id} not found"})

        notification_id = f"NOT-{supplier.get('supplier_id')}"

        notification = {
            "notification_id": notification_id,
            "supplier_id": supplier_id,
            "supplier_name": supplier.get("supplier_name"),
            "notification_type": notification_type,
            "contact_email": supplier.get("contact_information", {}).get("email"),
            "contact_phone": supplier.get("contact_information", {}).get("phone"),
            "notification_date": get_current_timestamp(),
            "delivery_status": "Sent",
            "urgency": "High" if notification_type == "quality_incident" else "Medium"
        }

        if "supplier_notifications" not in data:
            data["supplier_notifications"] = []
        data["supplier_notifications"].append(notification)

        return json.dumps({
            "notification_id": notification_id,
            "delivery_status": "Sent",
            "contact_method": notification["contact_email"]
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "notify_supplier",
                "description": "Send notification to supplier about issues or updates",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "Supplier identifier"},
                        "notification_type": {"type": "string", "description": "Type of notification (quality_incident/delivery_delay/general)"}
                    },
                    "required": ["supplier_id", "notification_type"]
                }
            }
        }
