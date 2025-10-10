import json
from typing import Any, Dict, List, Optional

from domains.dto import Tool


# Product & Inventory Tools
class GetProductBySku(Tool):
    """Tool to get product details by SKU."""

    @staticmethod
    def invoke(data: Dict[str, Any], sku: str) -> str:
        """Execute the tool with given parameters."""
        products = data.get("product_master", [])
        for product in products:
            if product.get("sku") == sku:
                return json.dumps(product, indent=2)
        return json.dumps({"error": f"Product with SKU {sku} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_product_by_sku",
                "description": "Retrieves detailed information about a specific product using its SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The Stock Keeping Unit (SKU) of the product to find.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }


class FindProducts(Tool):
    """Tool to find products based on criteria."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        category: Optional[str] = None,
        subcategory: Optional[str] = None,
        brand: Optional[str] = None,
    ) -> str:
        """Execute the tool with given parameters."""
        products = data.get("product_master", [])
        results = []
        for product in products:
            if (not category or product.get("category") == category) and \
               (not subcategory or product.get("subcategory") == subcategory) and \
               (not brand or product.get("brand") == brand):
                results.append(product)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "find_products",
                "description": "Finds products based on category, subcategory, or brand.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {"type": "string", "description": "The product category."},
                        "subcategory": {"type": "string", "description": "The product subcategory."},
                        "brand": {"type": "string", "description": "The product brand."},
                    },
                },
            },
        }


class GetInventoryBySku(Tool):
    """Tool to get inventory levels for a SKU across all warehouses."""

    @staticmethod
    def invoke(data: Dict[str, Any], sku: str) -> str:
        """Execute the tool with given parameters."""
        inventory = data.get("inventory", [])
        results = [item for item in inventory if item.get("sku") == sku]
        if not results:
            return json.dumps({"error": f"No inventory found for SKU {sku}"}, indent=2)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_by_sku",
                "description": "Retrieves inventory levels for a specific product SKU across all warehouses.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to check inventory for.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }


class GetInventoryInWarehouse(Tool):
    """Tool to get inventory for a specific warehouse."""

    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str, sku: Optional[str] = None) -> str:
        """Execute the tool with given parameters."""
        inventory = data.get("inventory", [])
        results = []
        for item in inventory:
            if item.get("warehouse_id") == warehouse_id:
                if not sku or item.get("sku") == sku:
                    results.append(item)
        if not results:
            return json.dumps({"error": f"No inventory found for warehouse {warehouse_id}"}, indent=2)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_in_warehouse",
                "description": "Retrieves all inventory items or a specific SKU's inventory from a single warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse to check.",
                        },
                        "sku": {
                            "type": "string",
                            "description": "Optional: The SKU of a specific product to check.",
                        },
                    },
                    "required": ["warehouse_id"],
                },
            },
        }


class AdjustInventory(Tool):
    """Tool to adjust the quantity of a product in a warehouse."""

    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str, sku: str, quantity_change: int, reason: str) -> str:
        """Execute the tool with given parameters."""
        inventory = data.get("inventory", [])
        for item in inventory:
            if item.get("warehouse_id") == warehouse_id and item.get("sku") == sku:
                original_qty = item["quantity_on_hand"]
                item["quantity_on_hand"] += quantity_change
                item["quantity_available"] += quantity_change

                if item["quantity_on_hand"] < 0:
                    item["quantity_on_hand"] = 0
                if item["quantity_available"] < 0:
                    item["quantity_available"] = 0

                return json.dumps({
                    "inventory_id": item["inventory_id"],
                    "sku": sku,
                    "warehouse_id": warehouse_id,
                    "original_quantity": original_qty,
                    "new_quantity": item["quantity_on_hand"],
                    "reason": reason
                }, indent=2)
        return json.dumps({"error": f"Inventory item not found for SKU {sku} in warehouse {warehouse_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "adjust_inventory",
                "description": "Manually adjusts the inventory quantity for a product in a specific warehouse (e.g., for cycle counts, damage).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "The ID of the warehouse."},
                        "sku": {"type": "string", "description": "The SKU of the product to adjust."},
                        "quantity_change": {"type": "integer", "description": "The amount to change the quantity by (can be positive or negative)."},
                        "reason": {"type": "string", "description": "The reason for the adjustment (e.g., 'Damaged Goods', 'Cycle Count Adjustment')."}
                    },
                    "required": ["warehouse_id", "sku", "quantity_change", "reason"],
                },
            },
        }


# Order Management Tools
class CreateOutboundOrder(Tool):
    """Tool to create a new outbound customer order."""

    @staticmethod
    def invoke(data: Dict[str, Any], customer_name: str, warehouse_id: str, items: List[Dict[str, Any]], shipping_address: str, total_value: Optional[int] = None) -> str:
        """Execute the tool with given parameters."""
        outbound_orders = data.get("outbound_orders", [])
        inventory = data.get("inventory", [])

        # Check stock for all items first
        for order_item in items:
            sku = order_item["sku"]
            quantity = order_item["quantity"]
            stock_found = False
            for inv_item in inventory:
                if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                    if inv_item["quantity_available"] < quantity:
                        return json.dumps({"error": f"Insufficient stock for SKU {sku}. Available: {inv_item['quantity_available']}, Requested: {quantity}"}, indent=2)
                    stock_found = True
                    break
            # if not stock_found:
            #     return json.dumps({"error": f"SKU {sku} not found in warehouse {warehouse_id}"}, indent=2)

        # Allocate stock and create order
        total_cost = 0
        for order_item in items:
            sku = order_item["sku"]
            quantity = order_item["quantity"]
            for inv_item in inventory:
                if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                    inv_item["quantity_allocated"] += quantity
                    inv_item["quantity_available"] -= quantity
                    total_cost += inv_item.get("unit_cost", 0) * quantity
                    break

        if total_value is not None:
            total_cost = total_value

        new_order_id = f"ORD-{len(outbound_orders) + 1:04d}"
        new_order = {
            "order_id": new_order_id,
            "customer_name": customer_name,
            # "order_date": "2024-07-19", # Simulating current date
            "status": "Pending",
            "warehouse_id": warehouse_id,
            "items": items,
            "total_value": round(total_cost, 2),
            "currency": "USD",
            "shipping_address": shipping_address,
            "carrier_id": None,
            "tracking_number": None
        }
        outbound_orders.append(new_order)
        return json.dumps(new_order, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "create_outbound_order",
                "description": "Creates a new outbound order for a customer, allocating stock from a specified warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_name": {"type": "string", "description": "The name of the customer."},
                        "warehouse_id": {"type": "string", "description": "The ID of the warehouse to fulfill the order from."},
                        "items": {
                            "type": "array",
                            "description": "A list of items to order.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string", "description": "Product SKU."},
                                    "quantity": {"type": "integer", "description": "Number of units to order."}
                                },
                                "required": ["sku", "quantity"]
                            }
                        },
                        "shipping_address": {"type": "string", "description": "The customer's full shipping address."},
                        "total_value": {"type": "integer", "description": "The total value of the order"}
                    },
                    "required": ["customer_name", "warehouse_id", "items", "shipping_address"],
                },
            },
        }


class GetOutboundOrderStatus(Tool):
    """Tool to get the status of an outbound order."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        """Execute the tool with given parameters."""
        orders = data.get("outbound_orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                return json.dumps(order, indent=2)
        return json.dumps({"error": f"Order with ID {order_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_outbound_order_status",
                "description": "Retrieves the current status and details of a specific outbound customer order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to look up."}
                    },
                    "required": ["order_id"],
                },
            },
        }


class UpdateOutboundOrderStatus(Tool):
    """Tool to update the status of an outbound order."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, new_status: str, tracking_number: Optional[str] = None, carrier_id: Optional[str] = None) -> str:
        """Execute the tool with given parameters."""
        orders = data.get("outbound_orders", [])
        inventory = data.get("inventory", [])
        for order in orders:
            if order.get("order_id") == order_id:
                order["status"] = new_status
                if tracking_number:
                    order["tracking_number"] = tracking_number
                if carrier_id:
                    order["carrier_id"] = carrier_id

                # If shipped, deduct from on_hand and allocated quantities
                if new_status.lower() == "shipped" and "items" in order:
                    warehouse_id = order["warehouse_id"]
                    for item in order["items"]:
                        sku = item["sku"]
                        quantity = item["quantity"]
                        for inv_item in inventory:
                            if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                                inv_item["quantity_on_hand"] -= quantity
                                inv_item["quantity_allocated"] -= quantity
                                break

                return json.dumps({"order_id": order_id, "new_status": new_status}, indent=2)
        return json.dumps({"error": f"Order with ID {order_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "update_outbound_order_status",
                "description": "Updates the status of an outbound order (e.g., to 'Shipped'). If shipping, adjusts inventory and adds tracking info.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to update."},
                        "new_status": {"type": "string", "description": "The new status (e.g., 'Processing', 'Shipped', 'Delivered', 'Cancelled')."},
                        "tracking_number": {"type": "string", "description": "The tracking number, if the order is being shipped."},
                        "carrier_id": {"type": "string", "description": "The ID of the carrier, if the order is being shipped."}
                    },
                    "required": ["order_id", "new_status"],
                },
            },
        }


class CancelOutboundOrder(Tool):
    """Tool to cancel an outbound order."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        """Execute the tool with given parameters."""
        orders = data.get("outbound_orders", [])
        inventory = data.get("inventory", [])
        for order in orders:
            if order.get("order_id") == order_id:
                # if order["status"] in ["Shipped", "Delivered"]:
                #     return json.dumps({"error": f"Cannot cancel order {order_id} with status '{order['status']}'"}, indent=2)

                # De-allocate stock
                # warehouse_id = order["warehouse_id"]
                # for item in order["items"]:
                #     sku = item["sku"]
                #     quantity = item["quantity"]
                #     for inv_item in inventory:
                #         if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                #             inv_item["quantity_allocated"] -= quantity
                #             inv_item["quantity_available"] += quantity
                #             break

                order["status"] = "Cancelled"
                return json.dumps({"order_id": order_id, "status": "Cancelled"}, indent=2)
        return json.dumps({"error": f"Order with ID {order_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "cancel_outbound_order",
                "description": "Cancels a pending or processing outbound order and returns the allocated stock to available inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to cancel."}
                    },
                    "required": ["order_id"],
                },
            },
        }


# Shipment & Carrier Tools
class GetInboundShipmentDetails(Tool):
    """Tool to get details of an inbound shipment."""

    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str) -> str:
        """Execute the tool with given parameters."""
        shipments = data.get("inbound_shipments", [])
        for shipment in shipments:
            if shipment.get("shipment_id") == shipment_id:
                return json.dumps(shipment, indent=2)
        return json.dumps({"error": f"Shipment with ID {shipment_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_inbound_shipment_details",
                "description": "Retrieves full details for a specific inbound shipment from a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "The ID of the inbound shipment."}
                    },
                    "required": ["shipment_id"],
                },
            },
        }


class FindInboundShipments(Tool):
    """Tool to find inbound shipments based on criteria."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        status: Optional[str] = None,
        supplier_id: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> str:
        """Execute the tool with given parameters."""
        shipments = data.get("inbound_shipments", [])
        results = []
        for shipment in shipments:
            if (not status or shipment.get("status") == status) and \
               (not supplier_id or shipment.get("supplier_id") == supplier_id) and \
               (not warehouse_id or shipment.get("destination_warehouse_id") == warehouse_id):
                results.append(shipment)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "find_inbound_shipments",
                "description": "Finds inbound shipments based on status, supplier, or destination warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string", "description": "Filter by shipment status (e.g., 'In Transit', 'Received', 'Delayed')."},
                        "supplier_id": {"type": "string", "description": "Filter by the supplier's ID."},
                        "warehouse_id": {"type": "string", "description": "Filter by the destination warehouse ID."},
                    },
                },
            },
        }


class CreateInboundShipment(Tool):
    """Tool to create a new inbound shipment record."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str, destination_warehouse_id: str, carrier_id: str, items: List[Dict[str, Any]], estimated_arrival_date: str) -> str:
        """Execute the tool with given parameters."""
        inbound_shipments = data.get("inbound_shipments", [])

        new_shipment_id = f"SHIP-{len(inbound_shipments) + 1:04d}"

        new_shipment = {
            "shipment_id": new_shipment_id,
            "supplier_id": supplier_id,
            "destination_warehouse_id": destination_warehouse_id,
            "carrier_id": carrier_id,
            "status": "In Transit",
            "items": items,
            "estimated_arrival_date": estimated_arrival_date,
            "actual_arrival_date": None,
            "customs_status": "Cleared",
            "hazmat": any(item.get("hazmat", False) for item in items)
        }

        inbound_shipments.append(new_shipment)

        return json.dumps(new_shipment, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "create_inbound_shipment",
                "description": "Creates a new inbound shipment record from a supplier to a warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "The ID of the supplier sending the shipment."},
                        "destination_warehouse_id": {"type": "string", "description": "The ID of the destination warehouse."},
                        "carrier_id": {"type": "string", "description": "The ID of the carrier transporting the shipment."},
                        "items": {
                            "type": "array",
                            "description": "A list of items in the shipment.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string", "description": "Product SKU."},
                                    "quantity": {"type": "integer", "description": "Number of units."}
                                },
                                "required": ["sku", "quantity"]
                            }
                        },
                        "estimated_arrival_date": {"type": "string", "description": "The estimated arrival date in YYYY-MM-DD format."}
                    },
                    "required": ["supplier_id", "destination_warehouse_id", "carrier_id", "items", "estimated_arrival_date"],
                },
            },
        }


class ReceiveInboundShipment(Tool):
    """Tool to process the receipt of an inbound shipment."""

    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str, items_received: List[Dict[str, Any]]) -> str:
        """Execute the tool with given parameters."""

        shipments = data.get("inbound_shipments", [])
        inventory = data.get("inventory", [])
        shipment_found = False
        for shipment in shipments:
            if shipment.get("shipment_id") == shipment_id:
                shipment_found = True
                if shipment["status"] == "Received":
                    return json.dumps({"error": f"Shipment {shipment_id} has already been received."}, indent=2)

                shipment["status"] = "Received"
                shipment["actual_arrival_date"] = "2024-07-19" # Simulating current date

                # Update inventory
                warehouse_id = shipment["destination_warehouse_id"]
                for received_item in items_received:
                    sku = received_item["sku"]
                    quantity = received_item["quantity"]
                    inv_item_found = False
                    for inv_item in inventory:
                        if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                            inv_item["quantity_on_hand"] += quantity
                            inv_item["quantity_available"] += quantity
                            inv_item_found = True
                            break
                    if not inv_item_found:
                        # This case should be handled by creating a new inventory record, but is simplified here.
                        return json.dumps({"error": f"SKU {sku} not found in inventory for warehouse {warehouse_id}. Cannot receive."}, indent=2)

                return json.dumps({"shipment_id": shipment_id, "status": "Received"}, indent=2)

        if not shipment_found:
            return json.dumps({"error": f"Shipment with ID {shipment_id} not found"}, indent=2)
        return ""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "receive_inbound_shipment",
                "description": "Processes the receipt of an inbound shipment, updating its status and adding the received items to inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "The ID of the inbound shipment being received."},
                        "items_received": {
                            "type": "array",
                            "description": "A list of SKUs and quantities that were received.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string", "description": "Product SKU."},
                                    "quantity": {"type": "integer", "description": "Number of units received."}
                                },
                                "required": ["sku", "quantity"]
                            }
                        }
                    },
                    "required": ["shipment_id", "items_received"],
                },
            },
        }


class GetCarrierDetails(Tool):
    """Tool to get details for a specific shipping carrier."""

    @staticmethod
    def invoke(data: Dict[str, Any], carrier_id: str) -> str:
        """Execute the tool with given parameters."""
        carriers = data.get("carriers", [])
        for carrier in carriers:
            if carrier.get("carrier_id") == carrier_id:
                return json.dumps(carrier, indent=2)
            if carrier.get("scac") == carrier_id:
                return json.dumps(carrier, indent=2)
        return json.dumps({"error": f"Carrier with ID/SCAC {carrier_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_carrier_details",
                "description": "Retrieves detailed information about a specific shipping carrier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_id": {"type": "string", "description": "The ID/SCAC of the carrier."}
                    },
                    "required": ["carrier_id"],
                },
            },
        }


class FindCarriers(Tool):
    """Tool to find carriers based on supported transport modes."""

    @staticmethod
    def invoke(data: Dict[str, Any], transport_mode: str) -> str:
        """Execute the tool with given parameters."""
        carriers = data.get("carriers", [])
        results = [
            carrier for carrier in carriers
            if transport_mode in carrier.get("supported_modes", []) and carrier.get("active_status")
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "find_carriers",
                "description": "Finds active shipping carriers that support a specific mode of transport.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transport_mode": {"type": "string", "description": "The mode of transport (e.g., 'Air', 'Sea', 'Truck', 'Rail')."}
                    },
                    "required": ["transport_mode"],
                },
            },
        }


# Supplier & Warehouse Tools
class GetSupplierInfo(Tool):
    """Tool to get information about a supplier."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str) -> str:
        """Execute the tool with given parameters."""
        suppliers = data.get("supplier_master", [])
        for supplier in suppliers:
            if supplier.get("supplier_id") == supplier_id:
                return json.dumps(supplier, indent=2)
        return json.dumps({"error": f"Supplier with ID {supplier_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_supplier_info",
                "description": "Retrieves detailed information about a specific supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "The ID of the supplier."}
                    },
                    "required": ["supplier_id"],
                },
            },
        }


class FindSuppliers(Tool):
    """Tool to find suppliers by the category of products they supply."""

    @staticmethod
    def invoke(data: Dict[str, Any], product_categories: List) -> str:
        """Execute the tool with given parameters."""
        suppliers = data.get("supplier_master", [])
        results = [
            supplier for supplier in suppliers
            if set(product_categories).issubset(supplier.get("product_categories", []))
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "find_suppliers",
                "description": "Finds suppliers that provide products in a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_categories": {"type": "list", "description": "The product categories to search for (e.g., 'Electronics', 'Apparel')."}
                    },
                    "required": ["product_categories"],
                },
            },
        }


class GetWarehouseInfo(Tool):
    """Tool to get information about a warehouse."""

    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str) -> str:
        """Execute the tool with given parameters."""
        warehouses = data.get("warehouses", [])
        for warehouse in warehouses:
            if warehouse.get("warehouse_id") == warehouse_id:
                return json.dumps(warehouse, indent=2)
        return json.dumps({"error": f"Warehouse with ID {warehouse_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_warehouse_info",
                "description": "Retrieves detailed information about a specific warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "The ID of the warehouse."}
                    },
                    "required": ["warehouse_id"],
                },
            },
        }


class FindWarehouses(Tool):
    """Tool to find warehouses based on location or capabilities."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        city: Optional[str] = None,
        country: Optional[str] = None,
        special_capability: Optional[str] = None,
        special_capabilities: Optional[List] = None,
    ) -> str:
        """Execute the tool with given parameters."""
        warehouses = data.get("warehouses", [])
        results = []
        for warehouse in warehouses:
            has_capability = False
            if special_capability:
                if special_capability in warehouse.get("special_capabilities", []) or warehouse.get("warehouse_type") == special_capability:
                    has_capability = True

            if special_capabilities:
                if bool(set(special_capabilities)) and set(special_capabilities).issubset(warehouse.get("special_capabilities", [])):
                    has_capability = True

            if (not city or warehouse.get("city") == city) and \
               (not country or warehouse.get("country") == country) and \
               (not special_capability or has_capability) and \
               (not special_capabilities or has_capability):
                results.append(warehouse)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "find_warehouses",
                "description": "Finds warehouses based on location or special capabilities.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "Filter by city."},
                        "country": {"type": "string", "description": "Filter by country."},
                        "special_capability": {"type": "string", "description": "Filter by a special capability (e.g., 'Cold Storage', 'Hazmat Certified')."},
                        "special_capabilities": {"type": "list", "description": "Filter by multiple special capabilities (e.g., 'Cold Storage', 'Hazmat Certified')."},
                    },
                },
            },
        }

class UpdateOutboundOrderItems(Tool):
    """Tool to add or remove items from a pending outbound order."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, items_to_add: Optional[List[Dict[str, Any]]] = None, items_to_remove: Optional[List[Dict[str, Any]]] = None) -> str:
        """Execute the tool with given parameters."""
        orders = data.get("outbound_orders", [])
        inventory = data.get("inventory", [])
        order_found = False
        for order in orders:
            if order.get("order_id") == order_id:
                order_found = True
                if order["status"] != "Pending":
                    return json.dumps({"error": f"Order {order_id} cannot be modified as its status is '{order['status']}'"}, indent=2)

                warehouse_id = order["warehouse_id"]

                # Process additions
                if items_to_add:
                    for item_to_add in items_to_add:
                        sku = item_to_add["sku"]
                        quantity = item_to_add["quantity"]
                        # Check stock
                        stock_found = False
                        for inv_item in inventory:
                            if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                                if inv_item["quantity_available"] < quantity:
                                    return json.dumps({"error": f"Insufficient stock for SKU {sku}. Available: {inv_item['quantity_available']}, Requested: {quantity}"}, indent=2)
                                stock_found = True
                                break
                        if not stock_found:
                            return json.dumps({"error": f"SKU {sku} not found in warehouse {warehouse_id}"}, indent=2)

                        # Allocate stock and add item
                        for inv_item in inventory:
                            if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                                inv_item["quantity_allocated"] += quantity
                                inv_item["quantity_available"] -= quantity
                                order["items"].append(item_to_add)
                                order["total_cost"] += inv_item.get("unit_cost", 0) * quantity
                                break

                # Process removals
                if items_to_remove:
                    for item_to_remove in items_to_remove:
                        sku_to_remove = item_to_remove["sku"]
                        quantity_to_remove = item_to_remove["quantity"]
                        item_in_order = False
                        for i, order_item in enumerate(order["items"]):
                            if order_item["sku"] == sku_to_remove:
                                item_in_order = True
                                if order_item["quantity"] < quantity_to_remove:
                                    return json.dumps({"error": f"Cannot remove {quantity_to_remove} of SKU {sku_to_remove}, only {order_item['quantity']} in order."}, indent=2)

                                # De-allocate stock
                                for inv_item in inventory:
                                    if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku_to_remove:
                                        inv_item["quantity_allocated"] -= quantity_to_remove
                                        inv_item["quantity_available"] += quantity_to_remove
                                        order["total_cost"] -= inv_item.get("unit_cost", 0) * quantity_to_remove
                                        break

                                order_item["quantity"] -= quantity_to_remove
                                if order_item["quantity"] == 0:
                                    order["items"].pop(i)
                                break
                        if not item_in_order:
                            return json.dumps({"error": f"SKU {sku_to_remove} not found in order {order_id}"}, indent=2)

                order["total_cost"] = round(order["total_cost"], 2)
                order["status"] = "Updated"
                return json.dumps({"order_id": order_id, "new_total_cost": order["total_cost"], "status": "Updated"}, indent=2)

        if not order_found:
            return json.dumps({"error": f"Order with ID {order_id} not found"}, indent=2)
        return ""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "update_outbound_order_items",
                "description": "Adds or removes items from a pending outbound customer order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to modify."},
                        "items_to_add": {
                            "type": "array",
                            "description": "A list of items to add to the order.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string", "description": "Product SKU."},
                                    "quantity": {"type": "integer", "description": "Number of units to add."}
                                },
                                "required": ["sku", "quantity"]
                            }
                        },
                        "items_to_remove": {
                            "type": "array",
                            "description": "A list of items to remove from the order.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string", "description": "Product SKU."},
                                    "quantity": {"type": "integer", "description": "Number of units to remove."}
                                },
                                "required": ["sku", "quantity"]
                            }
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }

class UpdateInboundShipment(Tool):
    """Tool to update details of an inbound shipment."""

    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str, destination_warehouse_id: Optional[str] = None, destination_warehouse_name: Optional[str] = None, destination_address: Optional[str] = None, destination_city: Optional[str] = None, estimated_arrival_date: Optional[str] = None, status: Optional[str] = None, carrier_id: Optional[str] = None, carrier_name: Optional[str] = None, carrier_scac:
               Optional[str] = None) -> str:
        """Execute the tool with given parameters."""
        shipments = data.get("inbound_shipments", [])
        for shipment in shipments:
            if shipment.get("shipment_id") == shipment_id:
                # if shipment["status"] not in ["In Transit", "Delayed"]:
                #      return json.dumps({"error": f"Shipment {shipment_id} cannot be updated with status '{shipment['status']}'"}, indent=2)
                if destination_warehouse_id:
                    shipment["destination_warehouse_id"] = destination_warehouse_id
                if destination_warehouse_name:
                    shipment["destination_warehouse_name"] = destination_warehouse_name
                if destination_address:
                    shipment["destination_address"] = destination_address
                if destination_city:
                    shipment["destination_city"] = destination_city
                if estimated_arrival_date:
                    shipment["estimated_arrival_date"] = estimated_arrival_date
                if status:
                    shipment["status"] = status
                if carrier_id:
                    shipment["carrier_id"] = carrier_id
                if carrier_name:
                    shipment["carrier_name"] = carrier_name
                if carrier_scac:
                    shipment["carrier_scac"] = carrier_scac
                return json.dumps({"shipment_id": shipment_id, "updated_details": shipment}, indent=2)
        return json.dumps({"error": f"Shipment with ID {shipment_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "update_inbound_shipment",
                "description": "Updates the details of an in-transit or delayed inbound shipment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "The ID of the shipment to update."},
                        "destination_warehouse_id": {"type": "string", "description": "The new destination warehouse ID."},
                        "destination_warehouse_name": {"type": "string", "description": "The new destination warehouse name."},
                        "destination_address": {"type": "string", "description": "The new destination address."},
                        "destination_city": {"type": "string", "description": "The new destination city."},
                        "estimated_arrival_date": {"type": "string", "description": "The new estimated arrival date in YYYY-MM-DD format."},
                        "status": {"type": "string", "description": "The new status of the shipment (e.g., 'Delayed')."},
                        "carrier_id": {"type": "string", "description": "The new carrier ID of the shipment."},
                        "carrier_name": {"type": "string", "description": "The new carrier name of the shipment."},
                        "carrier_scac": {"type": "string", "description": "The new carrier SCAC of the shipment."},
                    },
                    "required": ["shipment_id"],
                },
            },
        }

# Export tools as instances
TOOLS = [
    GetProductBySku(),
    FindProducts(),
    GetInventoryBySku(),
    GetInventoryInWarehouse(),
    AdjustInventory(),
    CreateOutboundOrder(),
    GetOutboundOrderStatus(),
    UpdateOutboundOrderStatus(),
    CancelOutboundOrder(),
    GetInboundShipmentDetails(),
    FindInboundShipments(),
    CreateInboundShipment(),
    ReceiveInboundShipment(),
    GetCarrierDetails(),
    FindCarriers(),
    GetSupplierInfo(),
    FindSuppliers(),
    GetWarehouseInfo(),
    FindWarehouses(),
    UpdateOutboundOrderItems(),
    UpdateInboundShipment(),
]
