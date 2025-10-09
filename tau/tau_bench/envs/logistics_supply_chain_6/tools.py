import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


#Tools for Product and Inventory
class GetProductBySku(Tool):
    """Utility for retrieving product information using SKU."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str) -> str:
        """Run the tool using the specified parameters."""
        products = data.get("product_master", [])
        for product in products:
            if product.get("sku") == sku:
                payload = product
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Product with SKU {sku} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetProductBySku",
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
    """Utility for locating products according to specified criteria."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        category: str | None = None,
        subcategory: str | None = None,
        brand: str | None = None
    ) -> str:
        """Run the tool with the provided parameters."""
        products = data.get("product_master", [])
        results = []
        for product in products:
            if (
                (not category or product.get("category") == category)
                and (not subcategory or product.get("subcategory") == subcategory)
                and (not brand or product.get("brand") == brand)
            ):
                results.append(product)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
        """Run the tool with the provided parameters."""
        pass
        products = data.get("product_master", [])
        results = []
        for product in products:
            if (
                (not category or product.get("category") == category)
                and (not subcategory or product.get("subcategory") == subcategory)
                and (not brand or product.get("brand") == brand)
            ):
                results.append(product)
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "findProducts",
                "description": "Finds products based on category, subcategory, or brand.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The product category.",
                        },
                        "subcategory": {
                            "type": "string",
                            "description": "The product subcategory.",
                        },
                        "brand": {
                            "type": "string",
                            "description": "The product brand.",
                        },
                    },
                },
            },
        }


class GetInventoryBySku(Tool):
    """Utility for obtaining inventory quantities for a SKU in all warehouses."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str) -> str:
        """Run the tool using the specified parameters."""
        inventory = data.get("inventory", [])
        results = [item for item in inventory if item.get("sku") == sku]
        if not results:
            payload = {"error": f"No inventory found for SKU {sku}"}
            out = json.dumps(payload, indent=2)
            return out
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the tool's specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryBySku",
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
    """Utility for retrieving inventory from a particular warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str, sku: str | None = None) -> str:
        """Run the tool with the provided parameters."""
        inventory = data.get("inventory", [])
        results = []
        for item in inventory:
            if item.get("warehouse_id") == warehouse_id:
                if not sku or item.get("sku") == sku:
                    results.append(item)
        if not results:
            payload = {"error": f"No inventory found for warehouse {warehouse_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryInWarehouse",
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
    """Utility for modifying the amount of a product within a warehouse."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        warehouse_id: str,
        sku: str,
        quantity_change: int,
        reason: str
    ) -> str:
        """Run the tool using the specified parameters."""
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
                payload = {
                    "inventory_id": item["inventory_id"],
                    "sku": sku,
                    "warehouse_id": warehouse_id,
                    "original_quantity": original_qty,
                    "new_quantity": item["quantity_on_hand"],
                    "reason": reason,
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {
            "error": f"Inventory item not found for SKU {sku} in warehouse {warehouse_id}"
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        """Run the tool using the specified parameters."""
        pass
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
                payload = {
                        "inventory_id": item["inventory_id"],
                        "sku": sku,
                        "warehouse_id": warehouse_id,
                        "original_quantity": original_qty,
                        "new_quantity": item["quantity_on_hand"],
                        "reason": reason,
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {
                "error": f"Inventory item not found for SKU {sku} in warehouse {warehouse_id}"
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "AdjustInventory",
                "description": "Manually adjusts the inventory quantity for a product in a specific warehouse (e.g., for cycle counts, damage).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse.",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to adjust.",
                        },
                        "quantity_change": {
                            "type": "integer",
                            "description": "The amount to change the quantity by (can be positive or negative).",
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the adjustment (e.g., 'Damaged Goods', 'Cycle Count Adjustment').",
                        },
                    },
                    "required": ["warehouse_id", "sku", "quantity_change", "reason"],
                },
            },
        }


#Tools for Managing Orders
class CreateOutboundOrder(Tool):
    """Utility for generating a new outbound order for customers."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        customer_name: str,
        warehouse_id: str,
        items: list[dict[str, Any]],
        shipping_address: str,
        total_value: int | None = None
    ) -> str:
        """Run the tool with the provided parameters."""
        pass
        outbound_orders = data.get("outbound_orders", [])
        inventory = data.get("inventory", [])

        # Verify stock for all items initially
        for order_item in items:
            sku = order_item["sku"]
            quantity = order_item["quantity"]
            for inv_item in inventory:
                if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                    if inv_item["quantity_available"] < quantity:
                        payload = {
                            "error": f"Insufficient stock for SKU {sku}. Available: {inv_item['quantity_available']}, Requested: {quantity}"
                        }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                    break
            # if stock_found is not present:
            # return json.dumps({"error": f"SKU {sku} is missing in warehouse {warehouse_id}"}, indent=2)

        # Distribute stock and generate order
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
            # "order_date": "2024-07-19", # Mimicking today's date
            "status": "Pending",
            "warehouse_id": warehouse_id,
            "items": items,
            "total_value": round(total_cost, 2),
            "currency": "USD",
            "shipping_address": shipping_address,
            "carrier_id": None,
            "tracking_number": None,
        }
        outbound_orders.append(new_order)
        payload = new_order
        out = json.dumps(payload, indent=2)
        return out
        """Run the tool with the provided parameters."""
        pass
        outbound_orders = data.get("outbound_orders", [])
        inventory = data.get("inventory", [])

        #Verify stock for all items initially
        for order_item in items:
            sku = order_item["sku"]
            quantity = order_item["quantity"]
            for inv_item in inventory:
                if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                    if inv_item["quantity_available"] < quantity:
                        payload = {
                                "error": f"Insufficient stock for SKU {sku}. Available: {inv_item['quantity_available']}, Requested: {quantity}"
                            }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                    break
            #if stock_found is not present:
            #return json.dumps({"error": f"SKU {sku} is missing in warehouse {warehouse_id}"}, indent=2)

        #Distribute stock and generate order
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
            #"order_date": "2024-07-19", # Mimicking today's date
            "status": "Pending",
            "warehouse_id": warehouse_id,
            "items": items,
            "total_value": round(total_cost, 2),
            "currency": "USD",
            "shipping_address": shipping_address,
            "carrier_id": None,
            "tracking_number": None,
        }
        outbound_orders.append(new_order)
        payload = new_order
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the tool's specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateOutboundOrder",
                "description": "Creates a new outbound order for a customer, allocating stock from a specified warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_name": {
                            "type": "string",
                            "description": "The name of the customer.",
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse to fulfill the order from.",
                        },
                        "items": {
                            "type": "array",
                            "description": "A list of items to order.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {
                                        "type": "string",
                                        "description": "Product SKU.",
                                    },
                                    "quantity": {
                                        "type": "integer",
                                        "description": "Number of units to order.",
                                    },
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                        "shipping_address": {
                            "type": "string",
                            "description": "The customer's full shipping address.",
                        },
                        "total_value": {
                            "type": "integer",
                            "description": "The total value of the order",
                        },
                    },
                    "required": [
                        "customer_name",
                        "warehouse_id",
                        "items",
                        "shipping_address",
                    ],
                },
            },
        }


class GetOutboundOrderStatus(Tool):
    """Utility for checking the status of an outbound order."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        """Run the tool using the specified parameters."""
        orders = data.get("outbound_orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                payload = order
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Order with ID {order_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetOutboundOrderStatus",
                "description": "Retrieves the current status and details of a specific outbound customer order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to look up.",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }


class UpdateOutboundOrderStatus(Tool):
    """Utility for modifying the status of an outbound order."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        new_status: str,
        tracking_number: str | None = None,
        carrier_id: str | None = None
    ) -> str:
        """Run the tool with the provided parameters."""
        _new_statusL = new_status or ''.lower()
        pass
        orders = data.get("outbound_orders", [])
        inventory = data.get("inventory", [])
        for order in orders:
            if order.get("order_id") == order_id:
                order["status"] = new_status
                if tracking_number:
                    order["tracking_number"] = tracking_number
                if carrier_id:
                    order["carrier_id"] = carrier_id

                # If dispatched, reduce on_hand and allocated amounts
                if new_status.lower() == "shipped" and "items" in order:
                    warehouse_id = order["warehouse_id"]
                    for item in order["items"]:
                        sku = item["sku"]
                        quantity = item["quantity"]
                        for inv_item in inventory:
                            if (
                                inv_item["warehouse_id"] == warehouse_id
                                and inv_item["sku"] == sku
                            ):
                                inv_item["quantity_on_hand"] -= quantity
                                inv_item["quantity_allocated"] -= quantity
                                break
                payload = {"order_id": order_id, "new_status": new_status}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Order with ID {order_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
        """Run the tool with the provided parameters."""
        _new_statusL = new_status or ''.lower()
        pass
        orders = data.get("outbound_orders", [])
        inventory = data.get("inventory", [])
        for order in orders:
            if order.get("order_id") == order_id:
                order["status"] = new_status
                if tracking_number:
                    order["tracking_number"] = tracking_number
                if carrier_id:
                    order["carrier_id"] = carrier_id

                #If dispatched, reduce on_hand and allocated amounts
                if new_status.lower() == "shipped" and "items" in order:
                    warehouse_id = order["warehouse_id"]
                    for item in order["items"]:
                        sku = item["sku"]
                        quantity = item["quantity"]
                        for inv_item in inventory:
                            if (
                                inv_item["warehouse_id"] == warehouse_id
                                and inv_item["sku"] == sku
                            ):
                                inv_item["quantity_on_hand"] -= quantity
                                inv_item["quantity_allocated"] -= quantity
                                break
                payload = {"order_id": order_id, "new_status": new_status}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Order with ID {order_id} not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateOutboundOrderStatus",
                "description": "Updates the status of an outbound order (e.g., to 'Shipped'). If shipping, adjusts inventory and adds tracking info.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status (e.g., 'Processing', 'Shipped', 'Delivered', 'Cancelled').",
                        },
                        "tracking_number": {
                            "type": "string",
                            "description": "The tracking number, if the order is being shipped.",
                        },
                        "carrier_id": {
                            "type": "string",
                            "description": "The ID of the carrier, if the order is being shipped.",
                        },
                    },
                    "required": ["order_id", "new_status"],
                },
            },
        }


class CancelOutboundOrder(Tool):
    """Utility for voiding an outbound order."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str, outbound_orders: list = None, inventory: list = None) -> str:
        """Run the tool using the specified parameters."""
        orders = outbound_orders if outbound_orders is not None else data.get("outbound_orders", [])
        inventory = inventory if inventory is not None else data.get("inventory", [])
        for order in orders:
            if order.get("order_id") == order_id:
                # if order["status"] is in ["Shipped", "Delivered"]:
                # return json.dumps({"error": f"Order {order_id} cannot be canceled due to status '{order['status']}'"}, indent=2)

                # Release allocated stock
                # warehouse_id is set to order["warehouse_id"]
                # for item in order["items"]:
                # sku is assigned from item["sku"]
                # quantity is taken from item["quantity"]
                # for inv_item in inventory:
                # if inv_item["warehouse_id"] matches warehouse_id and inv_item["sku"] matches sku:
                # inv_item["quantity_allocated"] is decreased by quantity
                # inv_item["quantity_available"] is increased by quantity
                # exit the loop

                order["status"] = "Cancelled"
                payload = {"order_id": order_id, "status": "Cancelled"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Order with ID {order_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "CancelOutboundOrder",
                "description": "Cancels a pending or processing outbound order and returns the allocated stock to available inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to cancel.",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }


#Tools for Shipments and Carriers
class GetInboundShipmentDetails(Tool):
    """Utility for retrieving information about an inbound shipment."""

    @staticmethod
    def invoke(data: dict[str, Any], shipment_id: str) -> str:
        """Run the tool with the provided parameters."""
        shipments = data.get("inbound_shipments", [])
        for shipment in shipments:
            if shipment.get("shipment_id") == shipment_id:
                payload = shipment
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Shipment with ID {shipment_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetInboundShipmentDetails",
                "description": "Retrieves full details for a specific inbound shipment from a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {
                            "type": "string",
                            "description": "The ID of the inbound shipment.",
                        }
                    },
                    "required": ["shipment_id"],
                },
            },
        }


class FindInboundShipments(Tool):
    """Utility for locating inbound shipments according to specified criteria."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        status: str | None = None,
        supplier_id: str | None = None,
        warehouse_id: str | None = None
    ) -> str:
        """Run the tool using the specified parameters."""
        shipments = data.get("inbound_shipments", [])
        results = []
        for shipment in shipments:
            if (
                (not status or shipment.get("status") == status)
                and (not supplier_id or shipment.get("supplier_id") == supplier_id)
                and (
                    not warehouse_id
                    or shipment.get("destination_warehouse_id") == warehouse_id
                )
            ):
                results.append(shipment)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
        """Run the tool using the specified parameters."""
        pass
        shipments = data.get("inbound_shipments", [])
        results = []
        for shipment in shipments:
            if (
                (not status or shipment.get("status") == status)
                and (not supplier_id or shipment.get("supplier_id") == supplier_id)
                and (
                    not warehouse_id
                    or shipment.get("destination_warehouse_id") == warehouse_id
                )
            ):
                results.append(shipment)
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindInboundShipments",
                "description": "Finds inbound shipments based on status, supplier, or destination warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Filter by shipment status (e.g., 'In Transit', 'Received', 'Delayed').",
                        },
                        "supplier_id": {
                            "type": "string",
                            "description": "Filter by the supplier's ID.",
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "Filter by the destination warehouse ID.",
                        },
                    },
                },
            },
        }


class CreateInboundShipment(Tool):
    """Utility for generating a new record for an inbound shipment."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_id: str,
        destination_warehouse_id: str,
        carrier_id: str,
        items: list[dict[str, Any]],
        estimated_arrival_date: str
,
    supplier_name: Any = None,
    ) -> str:
        """Run the tool with the provided parameters."""
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
            "hazmat": any(item.get("hazmat", False) for item in items),
        }

        inbound_shipments.append(new_shipment)
        payload = new_shipment
        out = json.dumps(payload, indent=2)
        return out
        """Run the tool with the provided parameters."""
        pass
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
            "hazmat": any(item.get("hazmat", False) for item in items),
        }

        inbound_shipments.append(new_shipment)
        payload = new_shipment
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateInboundShipment",
                "description": "Creates a new inbound shipment record from a supplier to a warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier sending the shipment.",
                        },
                        "destination_warehouse_id": {
                            "type": "string",
                            "description": "The ID of the destination warehouse.",
                        },
                        "carrier_id": {
                            "type": "string",
                            "description": "The ID of the carrier transporting the shipment.",
                        },
                        "items": {
                            "type": "array",
                            "description": "A list of items in the shipment.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {
                                        "type": "string",
                                        "description": "Product SKU.",
                                    },
                                    "quantity": {
                                        "type": "integer",
                                        "description": "Number of units.",
                                    },
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                        "estimated_arrival_date": {
                            "type": "string",
                            "description": "The estimated arrival date in YYYY-MM-DD format.",
                        },
                    },
                    "required": [
                        "supplier_id",
                        "destination_warehouse_id",
                        "carrier_id",
                        "items",
                        "estimated_arrival_date",
                    ],
                },
            },
        }


class ReceiveInboundShipment(Tool):
    """Utility for handling the receipt of an inbound shipment."""

    @staticmethod
    def invoke(
        data: dict[str, Any], shipment_id: str, items_received: list[dict[str, Any]]
    ) -> str:
        """Run the tool using the specified parameters."""
        shipments = data.get("inbound_shipments", [])
        inventory = data.get("inventory", [])
        shipment_found = False
        for shipment in shipments:
            if shipment.get("shipment_id") == shipment_id:
                shipment_found = True
                if shipment["status"] == "Received":
                    payload = {"error": f"Shipment {shipment_id} has already been received."}
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out

                shipment["status"] = "Received"
                shipment["actual_arrival_date"] = (
                    "2024-07-19"  # Mimicking the current date
                )

                # Revise inventory
                warehouse_id = shipment["destination_warehouse_id"]
                for received_item in items_received:
                    sku = received_item["sku"]
                    quantity = received_item["quantity"]
                    inv_item_found = False
                    for inv_item in inventory:
                        if (
                            inv_item["warehouse_id"] == warehouse_id
                            and inv_item["sku"] == sku
                        ):
                            inv_item["quantity_on_hand"] += quantity
                            inv_item["quantity_available"] += quantity
                            inv_item_found = True
                            break
                    if not inv_item_found:
                        payload = {
                            "error": f"SKU {sku} not found in inventory for warehouse {warehouse_id}. Cannot receive."
                        }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                payload = {"shipment_id": shipment_id, "status": "Received"}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        if not shipment_found:
            payload = {"error": f"Shipment with ID {shipment_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        return ""
        """Run the tool using the specified parameters."""
        pass

        shipments = data.get("inbound_shipments", [])
        inventory = data.get("inventory", [])
        shipment_found = False
        for shipment in shipments:
            if shipment.get("shipment_id") == shipment_id:
                shipment_found = True
                if shipment["status"] == "Received":
                    payload = {"error": f"Shipment {shipment_id} has already been received."}
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out

                shipment["status"] = "Received"
                shipment["actual_arrival_date"] = (
                    "2024-07-19"  #Mimicking the current date
                )

                #Revise inventory
                warehouse_id = shipment["destination_warehouse_id"]
                for received_item in items_received:
                    sku = received_item["sku"]
                    quantity = received_item["quantity"]
                    inv_item_found = False
                    for inv_item in inventory:
                        if (
                            inv_item["warehouse_id"] == warehouse_id
                            and inv_item["sku"] == sku
                        ):
                            inv_item["quantity_on_hand"] += quantity
                            inv_item["quantity_available"] += quantity
                            inv_item_found = True
                            break
                    if not inv_item_found:
                        payload = {
                                "error": f"SKU {sku} not found in inventory for warehouse {warehouse_id}. Cannot receive."
                            }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                payload = {"shipment_id": shipment_id, "status": "Received"}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        if not shipment_found:
            payload = {"error": f"Shipment with ID {shipment_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        return ""

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "ReceiveInboundShipment",
                "description": "Processes the receipt of an inbound shipment, updating its status and adding the received items to inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {
                            "type": "string",
                            "description": "The ID of the inbound shipment being received.",
                        },
                        "items_received": {
                            "type": "array",
                            "description": "A list of SKUs and quantities that were received.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {
                                        "type": "string",
                                        "description": "Product SKU.",
                                    },
                                    "quantity": {
                                        "type": "integer",
                                        "description": "Number of units received.",
                                    },
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                    },
                    "required": ["shipment_id", "items_received"],
                },
            },
        }


class GetCarrierDetails(Tool):
    """Utility for retrieving information about a particular shipping carrier."""

    @staticmethod
    def invoke(data: dict[str, Any], carrier_id: str) -> str:
        """Run the tool with the provided parameters."""
        carriers = data.get("carriers", [])
        for carrier in carriers:
            if carrier.get("carrier_id") == carrier_id:
                payload = carrier
                out = json.dumps(payload, indent=2)
                return out
            if carrier.get("scac") == carrier_id:
                payload = carrier
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Carrier with ID/SCAC {carrier_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetCarrierDetails",
                "description": "Retrieves detailed information about a specific shipping carrier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_id": {
                            "type": "string",
                            "description": "The ID/SCAC of the carrier.",
                        }
                    },
                    "required": ["carrier_id"],
                },
            },
        }


class FindCarriers(Tool):
    """Utility for locating carriers according to their supported transport methods."""

    @staticmethod
    def invoke(data: dict[str, Any], transport_mode: str, carriers: list = None) -> str:
        """Run the tool using the specified parameters."""
        carriers = carriers if carriers is not None else data.get("carriers", [])
        results = [
            carrier
            for carrier in carriers
            if transport_mode in carrier.get("supported_modes", [])
            and carrier.get("active_status")
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindCarriers",
                "description": "Finds active shipping carriers that support a specific mode of transport.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transport_mode": {
                            "type": "string",
                            "description": "The mode of transport (e.g., 'Air', 'Sea', 'Truck', 'Rail').",
                        }
                    },
                    "required": ["transport_mode"],
                },
            },
        }


#Tools for Suppliers and Warehouses
class GetSupplierInfo(Tool):
    """Utility for retrieving details regarding a supplier."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str) -> str:
        """Run the tool with the provided parameters."""
        suppliers = data.get("supplier_master", [])
        for supplier in suppliers:
            if supplier.get("supplier_id") == supplier_id:
                payload = supplier
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Supplier with ID {supplier_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetSupplierInfo",
                "description": "Retrieves detailed information about a specific supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier.",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }


class FindSuppliers(Tool):
    """Utility for locating suppliers based on the types of products they provide."""

    @staticmethod
    def invoke(data: dict[str, Any], product_categories: list, supplier_master: list = None) -> str:
        """Run the tool using the specified parameters."""
        suppliers = supplier_master if supplier_master is not None else []
        results = [
            supplier
            for supplier in suppliers
            if set(product_categories).issubset(supplier.get("product_categories", []))
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindSuppliers",
                "description": "Finds suppliers that provide products in a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_categories": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "The product categories to search for (e.g., 'Electronics', 'Apparel').",
                        }
                    },
                    "required": ["product_categories"],
                },
            },
        }


class GetWarehouseInfo(Tool):
    """Utility for retrieving details about a warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str) -> str:
        """Run the tool with the provided parameters."""
        warehouses = data.get("warehouses", [])
        for warehouse in warehouses:
            if warehouse.get("warehouse_id") == warehouse_id:
                payload = warehouse
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Warehouse with ID {warehouse_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetWarehouseInfo",
                "description": "Retrieves detailed information about a specific warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse.",
                        }
                    },
                    "required": ["warehouse_id"],
                },
            },
        }


class FindWarehouses(Tool):
    """Utility for locating warehouses according to their location or features."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        city: str | None = None,
        country: str | None = None,
        special_capability: str | None = None,
        special_capabilities: list | None = None
    ) -> str:
        """Run the tool using the specified parameters."""
        warehouses = data.get("warehouses", [])
        results = []
        for warehouse in warehouses:
            has_capability = False
            if special_capability:
                if (
                    special_capability in warehouse.get("special_capabilities", [])
                    or warehouse.get("warehouse_type") == special_capability
                ):
                    has_capability = True

            if special_capabilities:
                if bool(set(special_capabilities)) and set(
                    special_capabilities
                ).issubset(warehouse.get("special_capabilities", [])):
                    has_capability = True

            if (
                (not city or warehouse.get("city") == city)
                and (not country or warehouse.get("country") == country)
                and (not special_capability or has_capability)
                and (not special_capabilities or has_capability)
            ):
                results.append(warehouse)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
        """Run the tool using the specified parameters."""
        pass
        warehouses = data.get("warehouses", [])
        results = []
        for warehouse in warehouses:
            has_capability = False
            if special_capability:
                if (
                    special_capability in warehouse.get("special_capabilities", [])
                    or warehouse.get("warehouse_type") == special_capability
                ):
                    has_capability = True

            if special_capabilities:
                if bool(set(special_capabilities)) and set(
                    special_capabilities
                ).issubset(warehouse.get("special_capabilities", [])):
                    has_capability = True

            if (
                (not city or warehouse.get("city") == city)
                and (not country or warehouse.get("country") == country)
                and (not special_capability or has_capability)
                and (not special_capabilities or has_capability)
            ):
                results.append(warehouse)
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindWarehouses",
                "description": "Finds warehouses based on location or special capabilities.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "Filter by city."},
                        "country": {
                            "type": "string",
                            "description": "Filter by country.",
                        },
                        "special_capability": {
                            "type": "string",
                            "description": "Filter by a special capability (e.g., 'Cold Storage', 'Hazmat Certified').",
                        },
                        "special_capabilities": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter by multiple special capabilities (e.g., 'Cold Storage', 'Hazmat Certified').",
                        },
                    },
                },
            },
        }


class UpdateOutboundOrderItems(Tool):
    """Utility for including or excluding items from a pending outbound order."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        items_to_add: list[dict[str, Any]] | None = None,
        items_to_remove: list[dict[str, Any]] | None = None
    ) -> str:
        """Run the tool with the provided parameters."""
        orders = data.get("outbound_orders", [])
        inventory = data.get("inventory", [])
        order_found = False
        for order in orders:
            if order.get("order_id") == order_id:
                order_found = True
                if order["status"] != "Pending":
                    payload = {
                        "error": f"Order {order_id} cannot be modified as its status is '{order['status']}'"
                    }
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out

                warehouse_id = order["warehouse_id"]

                # Handle additions
                if items_to_add:
                    for item_to_add in items_to_add:
                        sku = item_to_add["sku"]
                        quantity = item_to_add["quantity"]
                        # Verify stock
                        stock_found = False
                        for inv_item in inventory:
                            if (
                                inv_item["warehouse_id"] == warehouse_id
                                and inv_item["sku"] == sku
                            ):
                                if inv_item["quantity_available"] < quantity:
                                    payload = {
                                        "error": f"Insufficient stock for SKU {sku}. Available: {inv_item['quantity_available']}, Requested: {quantity}"
                                    }
                                    out = json.dumps(
                                        payload, indent=2,
                                    )
                                    return out
                                stock_found = True
                                break
                        if not stock_found:
                            payload = {
                                "error": f"SKU {sku} not found in warehouse {warehouse_id}"
                            }
                            out = json.dumps(
                                payload, indent=2,
                            )
                            return out

                        # Distribute stock and include item
                        for inv_item in inventory:
                            if (
                                inv_item["warehouse_id"] == warehouse_id
                                and inv_item["sku"] == sku
                            ):
                                inv_item["quantity_allocated"] += quantity
                                inv_item["quantity_available"] -= quantity
                                order["items"].append(item_to_add)
                                order["total_cost"] += (
                                    inv_item.get("unit_cost", 0) * quantity
                                )
                                break

                # Handle removals
                if items_to_remove:
                    for item_to_remove in items_to_remove:
                        sku_to_remove = item_to_remove["sku"]
                        quantity_to_remove = item_to_remove["quantity"]
                        item_in_order = False
                        for i, order_item in enumerate(order["items"]):
                            if order_item["sku"] == sku_to_remove:
                                item_in_order = True
                                if order_item["quantity"] < quantity_to_remove:
                                    payload = {
                                        "error": f"Cannot remove {quantity_to_remove} of SKU {sku_to_remove}, only {order_item['quantity']} in order."
                                    }
                                    out = json.dumps(
                                        payload, indent=2,
                                    )
                                    return out

                                # Release stock allocation
                                for inv_item in inventory:
                                    if (
                                        inv_item["warehouse_id"] == warehouse_id
                                        and inv_item["sku"] == sku_to_remove
                                    ):
                                        inv_item[
                                            "quantity_allocated"
                                        ] -= quantity_to_remove
                                        inv_item[
                                            "quantity_available"
                                        ] += quantity_to_remove
                                        order["total_cost"] -= (
                                            inv_item.get("unit_cost", 0)
                                            * quantity_to_remove
                                        )
                                        break

                                order_item["quantity"] -= quantity_to_remove
                                if order_item["quantity"] == 0:
                                    order["items"].pop(i)
                                break
                        if not item_in_order:
                            payload = {
                                "error": f"SKU {sku_to_remove} not found in order {order_id}"
                            }
                            out = json.dumps(
                                payload, indent=2,
                            )
                            return out

                order["total_cost"] = round(order["total_cost"], 2)
                order["status"] = "Updated"
                payload = {
                    "order_id": order_id,
                    "new_total_cost": order["total_cost"],
                    "status": "Updated",
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

        if not order_found:
            payload = {"error": f"Order with ID {order_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        return ""
        """Run the tool with the provided parameters."""
        pass
        orders = data.get("outbound_orders", [])
        inventory = data.get("inventory", [])
        order_found = False
        for order in orders:
            if order.get("order_id") == order_id:
                order_found = True
                if order["status"] != "Pending":
                    payload = {
                            "error": f"Order {order_id} cannot be modified as its status is '{order['status']}'"
                        }
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out

                warehouse_id = order["warehouse_id"]

                #Handle additions
                if items_to_add:
                    for item_to_add in items_to_add:
                        sku = item_to_add["sku"]
                        quantity = item_to_add["quantity"]
                        #Verify stock
                        stock_found = False
                        for inv_item in inventory:
                            if (
                                inv_item["warehouse_id"] == warehouse_id
                                and inv_item["sku"] == sku
                            ):
                                if inv_item["quantity_available"] < quantity:
                                    payload = {
                                            "error": f"Insufficient stock for SKU {sku}. Available: {inv_item['quantity_available']}, Requested: {quantity}"
                                        }
                                    out = json.dumps(
                                        payload, indent=2,
                                    )
                                    return out
                                stock_found = True
                                break
                        if not stock_found:
                            payload = {
                                    "error": f"SKU {sku} not found in warehouse {warehouse_id}"
                                }
                            out = json.dumps(
                                payload, indent=2,
                            )
                            return out

                        #Distribute stock and include item
                        for inv_item in inventory:
                            if (
                                inv_item["warehouse_id"] == warehouse_id
                                and inv_item["sku"] == sku
                            ):
                                inv_item["quantity_allocated"] += quantity
                                inv_item["quantity_available"] -= quantity
                                order["items"].append(item_to_add)
                                order["total_cost"] += (
                                    inv_item.get("unit_cost", 0) * quantity
                                )
                                break

                #Handle removals
                if items_to_remove:
                    for item_to_remove in items_to_remove:
                        sku_to_remove = item_to_remove["sku"]
                        quantity_to_remove = item_to_remove["quantity"]
                        item_in_order = False
                        for i, order_item in enumerate(order["items"]):
                            if order_item["sku"] == sku_to_remove:
                                item_in_order = True
                                if order_item["quantity"] < quantity_to_remove:
                                    payload = {
                                            "error": f"Cannot remove {quantity_to_remove} of SKU {sku_to_remove}, only {order_item['quantity']} in order."
                                        }
                                    out = json.dumps(
                                        payload, indent=2,
                                    )
                                    return out

                                #Release stock allocation
                                for inv_item in inventory:
                                    if (
                                        inv_item["warehouse_id"] == warehouse_id
                                        and inv_item["sku"] == sku_to_remove
                                    ):
                                        inv_item[
                                            "quantity_allocated"
                                        ] -= quantity_to_remove
                                        inv_item[
                                            "quantity_available"
                                        ] += quantity_to_remove
                                        order["total_cost"] -= (
                                            inv_item.get("unit_cost", 0)
                                            * quantity_to_remove
                                        )
                                        break

                                order_item["quantity"] -= quantity_to_remove
                                if order_item["quantity"] == 0:
                                    order["items"].pop(i)
                                break
                        if not item_in_order:
                            payload = {
                                    "error": f"SKU {sku_to_remove} not found in order {order_id}"
                                }
                            out = json.dumps(
                                payload, indent=2,
                            )
                            return out

                order["total_cost"] = round(order["total_cost"], 2)
                order["status"] = "Updated"
                payload = {
                        "order_id": order_id,
                        "new_total_cost": order["total_cost"],
                        "status": "Updated",
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

        if not order_found:
            payload = {"error": f"Order with ID {order_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        return ""

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateOutboundOrderItems",
                "description": "Adds or removes items from a pending outbound customer order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to modify.",
                        },
                        "items_to_add": {
                            "type": "array",
                            "description": "A list of items to add to the order.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {
                                        "type": "string",
                                        "description": "Product SKU.",
                                    },
                                    "quantity": {
                                        "type": "integer",
                                        "description": "Number of units to add.",
                                    },
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                        "items_to_remove": {
                            "type": "array",
                            "description": "A list of items to remove from the order.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {
                                        "type": "string",
                                        "description": "Product SKU.",
                                    },
                                    "quantity": {
                                        "type": "integer",
                                        "description": "Number of units to remove.",
                                    },
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                    },
                    "required": ["order_id"],
                },
            },
        }


class UpdateInboundShipment(Tool):
    """Utility for modifying information related to an inbound shipment."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        shipment_id: str,
        destination_warehouse_id: str | None = None,
        destination_warehouse_name: str | None = None,
        destination_address: str | None = None,
        destination_city: str | None = None,
        estimated_arrival_date: str | None = None,
        status: str | None = None,
        carrier_id: str | None = None,
        carrier_name: str | None = None,
        carrier_scac: str | None = None
    ) -> str:
        """Run the tool using the specified parameters."""
        shipments = data.get("inbound_shipments", [])
        for shipment in shipments:
            if shipment.get("shipment_id") == shipment_id:
                # if shipment["status"] is not among ["In Transit", "Delayed"]:
                # return json.dumps({"error": f"Shipment {shipment_id} cannot be modified due to status '{shipment['status']}'"}, indent=2)
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
                payload = {"shipment_id": shipment_id, "updated_details": shipment}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Shipment with ID {shipment_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
        """Run the tool using the specified parameters."""
        pass
        shipments = data.get("inbound_shipments", [])
        for shipment in shipments:
            if shipment.get("shipment_id") == shipment_id:
                #if shipment["status"] is not among ["In Transit", "Delayed"]:
                #return json.dumps({"error": f"Shipment {shipment_id} cannot be modified due to status '{shipment['status']}'"}, indent=2)
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
                payload = {"shipment_id": shipment_id, "updated_details": shipment}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Shipment with ID {shipment_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateInboundShipment",
                "description": "Updates the details of an in-transit or delayed inbound shipment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {
                            "type": "string",
                            "description": "The ID of the shipment to update.",
                        },
                        "destination_warehouse_id": {
                            "type": "string",
                            "description": "The new destination warehouse ID.",
                        },
                        "destination_warehouse_name": {
                            "type": "string",
                            "description": "The new destination warehouse name.",
                        },
                        "destination_address": {
                            "type": "string",
                            "description": "The new destination address.",
                        },
                        "destination_city": {
                            "type": "string",
                            "description": "The new destination city.",
                        },
                        "estimated_arrival_date": {
                            "type": "string",
                            "description": "The new estimated arrival date in YYYY-MM-DD format.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status of the shipment (e.g., 'Delayed').",
                        },
                        "carrier_id": {
                            "type": "string",
                            "description": "The new carrier ID of the shipment.",
                        },
                        "carrier_name": {
                            "type": "string",
                            "description": "The new carrier name of the shipment.",
                        },
                        "carrier_scac": {
                            "type": "string",
                            "description": "The new carrier SCAC of the shipment.",
                        },
                    },
                    "required": ["shipment_id"],
                },
            },
        }


#Export tools as object instances
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
