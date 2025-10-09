from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreatePurchaseOrder(Tool):
    """Generates a new purchase order along with a corresponding 'Planned' inbound shipment."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, line_items: list = None, priority: str = None) -> str:
        if not all([supplier_id, line_items, priority]):
            payload = {"error": "supplier_id, line_items, and priority are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        supplier = next(
            (
                s
                for s in data.get("supplier_master", [])
                if s.get("supplier_id") == supplier_id
            ),
            None,
        )
        if not supplier:
            payload = {"error": f"Supplier '{supplier_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        inbound_shipments = data.get("inbound_shipments", [])

        current_year_str = str(get_current_year())

        #Select POs exclusively for the current year
        pos_this_year = [
            s
            for s in inbound_shipments
            if s.get("purchase_order_number", "").startswith(f"PO-{current_year_str}")
        ]

        #Identify the highest sequence number for the current year
        max_seq_num_this_year = 0
        if pos_this_year:
            max_seq_num_this_year = max(
                (
                    int(po.get("purchase_order_number").split("-")[2])
                    for po in pos_this_year
                ),
                default=0,
            )

        new_seq_num = max_seq_num_this_year + 1
        new_po_number = f"PO-{current_year_str}-{new_seq_num:04d}"
        #--- FINALIZED LOGIC END ---

        max_ship_id = max(
            (
                int(s.get("shipment_id", "SHIP-0").split("-")[1])
                for s in inbound_shipments
            ),
            default=0,
        )
        new_shipment_id = f"SHIP-{max_ship_id + 1:04d}"

        first_sku = line_items[0]["sku"]
        dest_warehouse = next(
            (i for i in data.get("inventory", []) if i.get("sku") == first_sku), {}
        )

        new_shipment = {
            "shipment_id": new_shipment_id,
            "purchase_order_number": new_po_number,
            "supplier_id": supplier_id,
            "supplier_name": supplier.get("supplier_name"),
            "origin_address": supplier.get("contact_information", {})
            .get("address", {})
            .get("street"),
            "origin_city": supplier.get("contact_information", {})
            .get("address", {})
            .get("city"),
            "origin_country": supplier.get("contact_information", {})
            .get("address", {})
            .get("country"),
            "destination_warehouse_id": dest_warehouse.get("warehouse_id"),
            "destination_warehouse_name": dest_warehouse.get("warehouse_name"),
            "status": "Planned",
            "priority_level": priority,
        }

        inbound_shipments.append(new_shipment)
        payload = {"status": "success", "purchase_order_number": new_po_number}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePurchaseOrder",
                "description": "Creates a new purchase order for a supplier, which also generates a new 'Planned' inbound shipment record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier for the order.",
                        },
                        "line_items": {
                            "type": "array",
                            "description": "A list of products to order.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                        "priority": {
                            "type": "string",
                            "description": "The priority level for this order (e.g., 'High').",
                        },
                    },
                    "required": ["supplier_id", "line_items", "priority"],
                },
            },
        }
