# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateOutboundOrderStatus(Tool):
    """Updates the status of an existing outbound order."""
    @staticmethod
    def invoke(data: Dict[str, Any], new_status, order_id) -> str:

        if not all([order_id, new_status]):
            return json.dumps({"error": "order_id and new_status are required."}, indent=2)

        order = next((o for o in data.get('outbound_orders', []) if o.get('order_id') == order_id), None)
        if not order:
            return json.dumps({"error": f"Order '{order_id}' not found."}, indent=2)

        if new_status == "Cancelled":
            for item in order.get("line_items", []):
                for inv_record in list(data.get('inventory', {}).values()):
                    if inv_record.get('sku') == item.get('sku') and inv_record.get('warehouse_id') == order.get('warehouse_id'):
                        inv_record['quantity_available'] += item.get('quantity', 0)
                        inv_record['quantity_allocated'] -= item.get('quantity', 0)
                        break

        order['status'] = new_status
        return_related_statuses = [
            "Returned",
            "Partially Returned",
            "Cancelled - Damaged Stock", # Ou outros estados que envolvam reembolso/cancelamento afetando o retorno.
            "Processing Return",
            "Incorrect Item Returned",
            "Cancelled - Force Majeure",
            "On Hold - Fraud Investigation", # Conforme a política de fraude/reembolso.
            "Cancelled - Expired Stock",
            "Cancelled" # Um cancelamento genérico também resulta em um retorno.
        ]
        if new_status in return_related_statuses:
            order['return_status'] = new_status
        else:
            order['return_status'] = "None"
        return json.dumps(order, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_outbound_order_status",
                "description": "Updates the status of an existing outbound order (e.g., to 'Partially Returned').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to update."},
                        "new_status": {"type": "string", "description": "The new status to set for the order."}
                    },
                    "required": ["order_id", "new_status"]
                }
            }
        }
