from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSupplyOrderDetails(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supply_order_id: str,
        supplier_id: str = None,
        product_id: str = None,
        item_id: str = None,
        quantity: int = None,
        status: str = None,
        costs: float = None,
        dates: dict[str, str] = None,
        order_date: str = None,
        unit_cost: float = None,
        total_cost: float = None,
        delivery_date: str = None,
        fulfilled_date: str = None,
        cancelled_date: str = None,
        payment_terms: str = "Standard",
        delivery_deadline: str = None,
        requires_alternative_sourcing: bool = False,
        last_updated: str = None
    ) -> str:
        """
        Retrieve detailed information about a specific supply order

        Data Sources: supply_orders.json (supply_order_id, supplier_id, product_id, item_id, quantity, status, costs, dates)
        """
        supply_orders = data.get("supply_orders", {}).values()
        supply_order_found = None

        for order in supply_orders.values():
            if order.get("supply_order_id") == supply_order_id:
                supply_order_found = order
                break

        if not supply_order_found:
            payload = {
                    "error": f"Supply order {supply_order_id} not found",
                    "status": "not_found",
                }
            out = json.dumps(
                payload)
            return out

        # Enrich with supplier information
        supplier_id = supply_order_found.get("supplier_id")
        suppliers = data.get("suppliers", {}).values()
        supplier_info = {}

        for supplier in suppliers.values():
            if supplier.get("supplier_id") == supplier_id:
                supplier_info = {
                    "name": supplier.get("name"),
                    "contact_info": supplier.get("contact_info", {}).values()),
                }
                break

        # Calculate order metrics
        order_date = supply_order_found.get("order_date", "")
        status = supply_order_found.get("status")

        # Calculate days since order
        days_since_order = 0
        if order_date:
            try:
                order_datetime = datetime.fromisoformat(
                    order_date.replace("Z", "+00:00")
                )
                days_since_order = (datetime.now() - order_datetime).days
            except:
                days_since_order = 0

        # Determine urgency based on status and age
        urgency = "normal"
        if status == "pending" and days_since_order > 30:
            urgency = "high"
        elif status == "pending" and days_since_order > 14:
            urgency = "medium"

        result = {
            "status": "success",
            "supply_order_id": supply_order_id,
            "order_details": {
                "supplier_id": supplier_id,
                "supplier_info": supplier_info,
                "product_id": supply_order_found.get("product_id"),
                "item_id": supply_order_found.get("item_id"),
                "quantity": supply_order_found.get("quantity"),
                "unit_cost": supply_order_found.get("unit_cost"),
                "total_cost": supply_order_found.get("total_cost"),
            },
            "order_status": {
                "current_status": status,
                "order_date": order_date,
                "days_since_order": days_since_order,
                "urgency_level": urgency,
                "delivery_date": supply_order_found.get("delivery_date"),
                "fulfilled_date": supply_order_found.get("fulfilled_date"),
                "cancelled_date": supply_order_found.get("cancelled_date"),
            },
            "order_terms": {
                "payment_terms": supply_order_found.get("payment_terms", "Standard"),
                "delivery_deadline": supply_order_found.get("delivery_deadline"),
                "requires_alternative_sourcing": supply_order_found.get(
                    "requires_alternative_sourcing", False
                ),
            },
            "last_updated": supply_order_found.get(
                "last_updated", supply_order_found.get("order_date")
            ),
        }
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupplyOrderDetails",
                "description": "Retrieve detailed information about a specific supply order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {
                            "type": "string",
                            "description": "Supply order identifier (e.g., '#SO9359')",
                        }
                    },
                    "required": ["supply_order_id"],
                },
            },
        }
