import json
import uuid
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from domains.dto import Tool

def get_current_timestamp() -> str:
    return "2025-07-31T12:00:00.000000"

def get_current_timestamp_object() -> datetime:
    return datetime.strptime(get_current_timestamp(), "%Y-%m-%dT%H:%M:%S.%f")

def get_current_year_month_day() -> str:
    return "2025-07-31"

def generate_unique_id() -> str:
    return 'fd520c73'


class GetInventoryBySkuWarehouse(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str, warehouse_id: str) -> str:
        inventory = data.get("inventory", [])

        inventory_item = next(
            (item for item in inventory
             if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id),
            None
        )

        if not inventory_item:
            return json.dumps({
                "error": f"Inventory not found for SKU {sku} in warehouse {warehouse_id}"
            })

        return json.dumps(inventory_item)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_by_sku_warehouse",
                "description": "Retrieve inventory details for specific SKU in a warehouse",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Product SKU identifier"
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "Warehouse identifier"
                        }
                    },
                    "required": ["sku", "warehouse_id"]
                }
            }
        }

class CreatePurchaseOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get("supplier_id")
        sku = kwargs.get("sku")
        quantity = kwargs.get("quantity")
        destination_warehouse = kwargs.get("destination_warehouse")
        priority = kwargs.get("priority", "Medium")
        notes = kwargs.get("notes", "")
        unit_price_specific = kwargs.get("unit_price", "")

        if not all([supplier_id, sku, quantity, destination_warehouse]):
            return json.dumps({
                "error": "supplier_id, sku, quantity, and destination_warehouse are required"
            })

        suppliers = data.get("supplier_master", [])
        products = data.get("product_master", [])
        warehouses = data.get("warehouses", [])

        supplier = next((s for s in suppliers if s.get("supplier_id") == supplier_id), None)
        if not supplier:
            return json.dumps({"error": f"Supplier {supplier_id} not found"})

        product = next((p for p in products if p.get("sku") == sku), None)
        if not product:
            return json.dumps({"error": f"Product {sku} not found"})

        warehouse = next((w for w in warehouses if w.get("warehouse_id") == destination_warehouse), None)
        if not warehouse:
            return json.dumps({"error": f"Warehouse {destination_warehouse} not found"})

        existing_pos = data.get("purchase_orders", [])
        po_counter = len(existing_pos) + 1
        po_id = f"PO-{supplier_id}-{sku}-{po_counter:03d}"

        total_cost = product.get("unit_price", 0) * quantity
        if unit_price_specific:
            total_cost = unit_price_specific * quantity

        fixed_creation_date = "2024-07-20T18:06:05.000000"
        fixed_delivery_date = "2024-08-19T18:06:05.000000"

        purchase_order = {
            "po_id": po_id,
            "supplier_id": supplier_id,
            "supplier_name": supplier.get("supplier_name"),
            "sku": sku,
            "product_name": product.get("product_name"),
            "quantity": quantity,
            "unit_price": product.get("unit_price"),
            "total_cost": total_cost,
            "destination_warehouse": destination_warehouse,
            "priority": priority,
            "notes": notes,
            "status": "Created",
            "created_date": fixed_creation_date,
            "expected_delivery": fixed_delivery_date
        }

        if "purchase_orders" not in data:
            data["purchase_orders"] = []
        data["purchase_orders"].append(purchase_order)

        return json.dumps({
            "status": "Created",
            "total_cost": total_cost,
            "priority": priority,
            "po_id": po_id,
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_purchase_order",
                "description": "Create a new purchase order for inventory replenishment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "Supplier identifier"},
                        "sku": {"type": "string", "description": "Product SKU"},
                        "quantity": {"type": "integer", "description": "Order quantity"},
                        "destination_warehouse": {"type": "string", "description": "Destination warehouse ID"},
                        "priority": {"type": "string", "description": "Order priority (Low/Medium/High/Critical)"},
                        "notes": {"type": "string", "description": "Additional order notes"},
                        "unit_price": {"type": "number", "description": "Unit price of the product (optional, defaults to product master)"},
                    },
                    "required": ["supplier_id", "sku", "quantity", "destination_warehouse"]
                }
            }
        }

class SearchInboundShipments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        destination_warehouse_id = kwargs.get("destination_warehouse_id")
        status = kwargs.get("status")

        inbound_shipments = data.get("inbound_shipments", [])
        inventory = data.get("inventory", [])

        # Find current inventory for the SKU/warehouse
        current_inventory = next(
            (item for item in inventory
             if item.get("sku") == sku and item.get("warehouse_id") == destination_warehouse_id),
            None
        )

        current_available = current_inventory.get("quantity_available", 0) if current_inventory else 0
        current_inbound = current_inventory.get("quantity_inbound", 0) if current_inventory else 0

        # Filter matching shipments
        results = []
        for shipment in inbound_shipments:
            match = True
            # Check if shipment contains the SKU by looking for it in the data structure
            if sku and not any(sku in str(value) for value in shipment.values()):
                match = False
            if destination_warehouse_id and shipment.get("destination_warehouse_id") != destination_warehouse_id:
                match = False
            if status and shipment.get("status") != status:
                match = False
            if match:
                results.append(shipment)

        # Calculate total expected stock based on actual inventory + inbound
        total_expected_stock = current_available + current_inbound

        return json.dumps({
            "shipments": results,
            "current_available": current_available,
            "current_inbound": current_inbound,
            "total_expected_stock": total_expected_stock
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_inbound_shipments",
                "description": "Search for inbound shipments based on criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "Product SKU to filter by"},
                        "destination_warehouse_id": {"type": "string", "description": "Destination warehouse"},
                        "status": {"type": "string", "description": "Shipment status to filter by"}
                    },
                    "required": []
                }
            }
        }

class GetOrderDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        orders = data.get("outbound_orders", [])

        order = next((o for o in orders if o.get("order_id") == order_id), None)

        if not order:
            return json.dumps({"error": f"Order {order_id} not found"})

        return json.dumps(order)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Retrieve detailed information about a specific order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Order identifier"}
                    },
                    "required": ["order_id"]
                }
            }
        }

class VerifyInventoryAllocation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        orders = data.get("outbound_orders", [])
        inventory = data.get("inventory", [])

        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"Order {order_id} not found"})

        warehouse_id = order.get("warehouse_id")
        total_units = order.get("total_units", 0)

        # Simplified allocation check - in real system would check line items
        warehouse_inventory = [item for item in inventory if item.get("warehouse_id") == warehouse_id]
        total_available = sum(item.get("quantity_available", 0) for item in warehouse_inventory)

        allocation_status = "fully_allocated" if total_available >= total_units else "insufficient_inventory"

        return json.dumps({
            "order_id": order_id,
            "allocation_status": allocation_status,
            "required_units": total_units,
            "available_units": total_available
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_inventory_allocation",
                "description": "Verify that inventory is allocated for all items in an order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Order identifier"}
                    },
                    "required": ["order_id"]
                }
            }
        }

class SelectOptimalCarrier(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        destination_city = kwargs.get("destination_city")
        destination_country = kwargs.get("destination_country")
        priority_level = kwargs.get("priority_level")
        total_weight_kg = kwargs.get("total_weight_kg")
        preferred_carrier = kwargs.get("preferred_carrier")
        carriers_list = kwargs.get("carriers_list", None)

        carriers = data.get("carriers", [])

        # Filter active carriers
        active_carriers = [c for c in carriers if c.get("active_status", False)]

        # Apply business rules for carrier selection
        suitable_carriers = []
        for carrier in active_carriers:
            # Rule: Carriers with <95% on-time delivery cannot handle Critical priority
            if priority_level == "Critical" and carrier.get("performance_metrics", {}).get("on_time_delivery_percentage", 0) < 95:
                continue

            if carriers_list:
                if carrier.get('scac') not in carriers_list:
                    continue

            # Rule: Check regional coverage and city service capability
            coverage = carrier.get("regional_coverage", "")
            carrier_address = carrier.get("contact_information", {}).get("address", {})
            carrier_country = carrier_address.get("country", "")
            carrier_city = carrier_address.get("city", "")

            # Since service_cities doesn't exist in DB, use logical service area determination
            # based on carrier operational presence and coverage
            coverage_match = False

            # Global carriers serve all destinations
            if coverage == "Global":
                coverage_match = True
            # Regional coverage matching
            elif coverage == "North America" and destination_country in ["USA", "Canada", "Mexico"]:
                coverage_match = True
            # Country-level matching
            elif destination_country == carrier_country:
                coverage_match = True
            # Special case: carriers in major hub cities can serve broader regions
            elif carrier_city in ["Los Angeles", "New York", "Chicago", "Miami", "Seattle", "Houston"] and destination_country == "USA":
                coverage_match = True
            # Carriers can serve their home city and surrounding region
            elif destination_city == carrier_city:
                coverage_match = True
            elif preferred_carrier and carrier.get("scac") == preferred_carrier:
                # If a preferred carrier is specified, ensure it matches the criteria
                if carrier.get("scac") == preferred_carrier:
                    coverage_match = True
            elif carriers_list:
                # If a list of carriers is provided, check if this carrier is in the list
                if carrier.get("scac") in carriers_list:
                    coverage_match = True

            if coverage_match:
                suitable_carriers.append(carrier)

        if not suitable_carriers:
            return json.dumps({"error": "No suitable carriers found for the specified criteria"})

        # Select best carrier based on performance rating and priority rules
        if preferred_carrier:
            best_carrier = next((c for c in suitable_carriers if c.get("scac") == preferred_carrier), None)
        else:
            if priority_level == "Critical":
                # For critical shipments, prioritize performance
                best_carrier = max(suitable_carriers,
                                key=lambda c: (
                                    c.get("performance_metrics", {}).get("on_time_delivery_percentage", 0),
                                    c.get("performance_metrics", {}).get("average_rating", 0)
                                ))
            else:
                # For standard shipments, balance performance and cost
                best_carrier = max(suitable_carriers,
                                key=lambda c: c.get("performance_metrics", {}).get("average_rating", 0))



        return json.dumps({
            "selected_carrier": best_carrier.get("scac"),
            "carrier_name": best_carrier.get("carrier_name"),
            "performance_rating": best_carrier.get("performance_metrics", {}).get("average_rating"),
            "on_time_delivery": best_carrier.get("performance_metrics", {}).get("on_time_delivery_percentage"),
            "coverage": best_carrier.get("regional_coverage")
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "select_optimal_carrier",
                "description": "Select the best carrier based on destination, priority, and performance metrics",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_city": {"type": "string", "description": "Destination city"},
                        "destination_country": {"type": "string", "description": "Destination country"},
                        "priority_level": {"type": "string", "description": "Shipment priority level"},
                        "total_weight_kg": {"type": "number", "description": "Total shipment weight in kg"},
                        "preferred_carrier": {
                            "type": "string",
                            "description": "Preferred carrier SCAC (optional)"
                        },
                        "carriers_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "scac": {"type": "string", "description": "Carrier SCAC code"},
                                }
                            }
                        }
                    },
                    "required": ["destination_city", "destination_country", "priority_level"]
                }
            }
        }

class GenerateShippingLabels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, carrier_scac: str) -> str:
        orders = data.get("outbound_orders", [])
        carriers = data.get("carriers", [])

        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"Order {order_id} not found"})

        carrier = next((c for c in carriers if c.get("scac") == carrier_scac), None)

        # UPDATED: Handle carriers referenced in orders but not in carriers.json
        tracking = ""
        if not carrier:
            # Check if carrier exists in order data (fallback for data inconsistencies)
            order_carrier = order.get("carrier_scac")
            if order_carrier == carrier_scac:
                carrier_name = order.get("carrier_name", f"Carrier {carrier_scac}")
                tracking = order.get("tracking_number", "")
            else:
                return json.dumps({"error": f"Carrier {carrier_scac} not found"})
        else:
            carrier_name = carrier.get("carrier_name")

        tracking_number = f"{carrier_scac}-{order_id}"
        if tracking:
            tracking_number = tracking

        shipping_label = {
            "label_id": f"LBL-{carrier_scac}",
            "order_id": order_id,
            "tracking_number": tracking_number,
            "carrier_scac": carrier_scac,
            "carrier_name": carrier_name,
            "generated_date": get_current_timestamp(),
            "destination_address": order.get("destination_address"),
            "weight_kg": order.get("total_weight_kg"),
            "service_level": order.get("shipping_service_level", "Standard"),
            "estimated_delivery_date": order.get("expected_delivery_date")
        }

        if "shipping_labels" not in data:
            data["shipping_labels"] = []
        data["shipping_labels"].append(shipping_label)

        return json.dumps({
            "tracking_number": tracking_number,
            "label_id": shipping_label["label_id"],
            "carrier_name": carrier_name,
            "estimated_delivery_date": shipping_label["estimated_delivery_date"]
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_shipping_labels",
                "description": "Generate shipping labels and tracking numbers for an order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Order identifier"},
                        "carrier_scac": {"type": "string", "description": "Carrier SCAC code"}
                    },
                    "required": ["order_id", "carrier_scac"]
                }
            }
        }

class UpdateOrderStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, new_status: str) -> str:
        orders = data.get("outbound_orders", [])

        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"Order {order_id} not found"})

        old_status = order.get("status")
        order["status"] = new_status
        order["last_updated"] = get_current_year_month_day()

        if new_status == "Shipped":
            order["actual_ship_date"] = get_current_year_month_day()

        return json.dumps({
            "order_id": order_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_timestamp": order["last_updated"]
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_order_status",
                "description": "Update the status of an order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Order identifier"},
                        "new_status": {"type": "string", "description": "New order status"},
                        "status": {"type": "string", "description": "Alternative status parameter"}
                    },
                    "required": ["order_id", "new_status"]
                }
            }
        }

class GetShipmentDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str) -> str:
        inbound_shipments = data.get("inbound_shipments", [])

        shipment = next((s for s in inbound_shipments if s.get("shipment_id") == shipment_id), None)

        if not shipment:
            return json.dumps({"error": f"Shipment {shipment_id} not found"})

        return json.dumps(shipment)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_shipment_details",
                "description": "Retrieve detailed information about a specific shipment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "Shipment identifier"}
                    },
                    "required": ["shipment_id"]
                }
            }
        }

class VerifyCustomsDocumentation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str) -> str:
        inbound_shipments = data.get("inbound_shipments", [])

        shipment = next((s for s in inbound_shipments if s.get("shipment_id") == shipment_id), None)
        if not shipment:
            return json.dumps({"error": f"Shipment {shipment_id} not found"})

        documentation_complete = True
        missing_docs = []

        # Check required documentation
        if not shipment.get("bill_of_lading"):
            documentation_complete = False
            missing_docs.append("bill_of_lading")

        if shipment.get("origin_country") != shipment.get("destination_country"):
            if not shipment.get("customs_entry_number"):
                documentation_complete = False
                missing_docs.append("customs_entry_number")

        return json.dumps({
            "shipment_id": shipment_id,
            "documentation_complete": documentation_complete,
            "missing_documents": missing_docs,
            "customs_status": shipment.get("customs_clearance_status"),
            "duty_paid": shipment.get("duty_paid", False)
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_customs_documentation",
                "description": "Verify completeness of customs documentation for a shipment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "Shipment identifier"}
                    },
                    "required": ["shipment_id"]
                }
            }
        }

class CalculateCustomsDuty(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        shipment_id = kwargs.get("shipment_id")
        total_value = kwargs.get("total_value")
        country_of_origin = kwargs.get("country_of_origin")

        # Simplified duty calculation - in real system would use tariff schedules
        duty_rates = {
            "China": 0.05,  # 5% duty rate
            "Japan": 0.02,  # 2% duty rate
            "Germany": 0.025, # 2.5% duty rate
            "Mexico": 0.0,  # USMCA preferential rate
            "default": 0.035 # 3.5% standard rate
        }

        duty_rate = duty_rates.get(country_of_origin, duty_rates["default"])
        duty_amount = total_value * duty_rate

        return json.dumps({
            "shipment_id": shipment_id,
            "duty_rate": duty_rate,
            "duty_amount": duty_amount,
            "total_value": total_value,
            "country_of_origin": country_of_origin
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_customs_duty",
                "description": "Calculate customs duty amount for a shipment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "Shipment identifier"},
                        "total_value": {"type": "number", "description": "Total shipment value"},
                        "country_of_origin": {"type": "string", "description": "Country of origin"}
                    },
                    "required": ["shipment_id", "total_value", "country_of_origin"]
                }
            }
        }

class ProcessDutyPayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str, duty_amount: float) -> str:
        inbound_shipments = data.get("inbound_shipments", [])

        shipment = next((s for s in inbound_shipments if s.get("shipment_id") == shipment_id), None)
        if not shipment:
            return json.dumps({"error": f"Shipment {shipment_id} not found"})

        # Process payment
        payment_id = f"PAY-{shipment_id}-{duty_amount:.1f}"

        duty_payment = {
            "payment_id": payment_id,
            "shipment_id": shipment_id,
            "duty_amount": duty_amount,
            "payment_date": get_current_timestamp(),
            "payment_status": "Completed",
            "payment_method": "Electronic"
        }

        # Update shipment
        shipment["duty_paid"] = True
        shipment["duty_amount"] = duty_amount

        if "duty_payments" not in data:
            data["duty_payments"] = []
        data["duty_payments"].append(duty_payment)

        return json.dumps({
            "payment_id": payment_id,
            "duty_amount": duty_amount,
            "payment_status": "Completed"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_duty_payment",
                "description": "Process customs duty payment for a shipment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "Shipment identifier"},
                        "duty_amount": {"type": "number", "description": "Duty amount to pay"}
                    },
                    "required": ["shipment_id", "duty_amount"]
                }
            }
        }

class UpdateCustomsStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str, status: str) -> str:
        inbound_shipments = data.get("inbound_shipments", [])

        shipment = next((s for s in inbound_shipments if s.get("shipment_id") == shipment_id), None)
        if not shipment:
            return json.dumps({"error": f"Shipment {shipment_id} not found"})

        old_status = shipment.get("customs_clearance_status")
        shipment["customs_clearance_status"] = status

        if status == "Cleared":
            shipment["customs_clearance_date"] = get_current_timestamp()
            shipment["customs_entry_number"] = f"US-{shipment_id}"

        return json.dumps({
            "shipment_id": shipment_id,
            "old_customs_status": old_status,
            "new_customs_status": status,
            "customs_entry_number": shipment.get("customs_entry_number")
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_customs_status",
                "description": "Update customs clearance status for a shipment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "Shipment identifier"},
                        "status": {"type": "string", "description": "New customs status"}
                    },
                    "required": ["shipment_id", "status"]
                }
            }
        }

class UpdateShipmentStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str, status: str) -> str:
        inbound_shipments = data.get("inbound_shipments", [])

        shipment = next((s for s in inbound_shipments if s.get("shipment_id") == shipment_id), None)
        if not shipment:
            return json.dumps({"error": f"Shipment {shipment_id} not found"})

        old_status = shipment.get("status")
        shipment["status"] = status
        shipment["last_updated"] = get_current_timestamp()

        if status == "Received":
            shipment["actual_arrival_date"] = get_current_year_month_day()

        return json.dumps({
            "shipment_id": shipment_id,
            "old_status": old_status,
            "new_status": status,
            "updated_timestamp": shipment["last_updated"]
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_shipment_status",
                "description": "Update the status of an inbound shipment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "Shipment identifier"},
                        "status": {"type": "string", "description": "New shipment status"}
                    },
                    "required": ["shipment_id", "status"]
                }
            }
        }

class GetSupplierPerformance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str) -> str:
        suppliers = data.get("supplier_master", [])

        supplier = next((s for s in suppliers if s.get("supplier_id") == supplier_id), None)

        if not supplier:
            return json.dumps({"error": f"Supplier {supplier_id} not found"})

        performance_data = {
            "supplier_id": supplier_id,
            "supplier_name": supplier.get("supplier_name"),
            "performance_rating": supplier.get("performance_rating"),
            "on_time_delivery_percentage": supplier.get("on_time_delivery_percentage"),
            "relationship_status": supplier.get("relationship_status"),
            "certifications": supplier.get("certifications", []),
            "standard_lead_time_days": supplier.get("standard_lead_time_days"),
            "payment_terms": supplier.get("payment_terms")
        }

        return json.dumps(performance_data)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_supplier_performance",
                "description": "Retrieve supplier performance metrics and details",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "Supplier identifier"}
                    },
                    "required": ["supplier_id"]
                }
            }
        }

class CreateSupplierImprovementPlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get("supplier_id")
        review_cycle_days = kwargs.get("review_cycle_days", 90)
        recommendation = kwargs.get("recommendation", "maintain_active")

        suppliers = data.get("supplier_master", [])
        supplier = next((s for s in suppliers if s.get("supplier_id") == supplier_id), None)

        if not supplier:
            return json.dumps({"error": f"Supplier {supplier_id} not found"})

        plan_id = f"SIP-{supplier_id}"

        improvement_plan = {
            "plan_id": plan_id,
            "supplier_id": supplier_id,
            "supplier_name": supplier.get("supplier_name"),
            "review_cycle_days": review_cycle_days,
            "created_date": get_current_timestamp(),
            "next_review_date": (get_current_timestamp_object() + timedelta(days=review_cycle_days)).isoformat(),
            "status": "Active",
            "current_performance_rating": supplier.get("performance_rating"),
            "target_improvements": [
                "Improve on-time delivery performance",
                "Enhance quality control processes",
                "Strengthen communication protocols",
                "Proper forecast and path planning"
            ]
        }

        if "supplier_improvement_plans" not in data:
            data["supplier_improvement_plans"] = []
        data["supplier_improvement_plans"].append(improvement_plan)

        recommended_value = "maintain_active"
        if recommendation:
            recommended_value = recommendation

        return json.dumps({
            "plan_id": plan_id,
            "status": "Created",
            "next_review_date": improvement_plan["next_review_date"],
            "supplier_status_recommendation": recommended_value
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_supplier_improvement_plan",
                "description": "Create a performance improvement plan for a supplier",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "Supplier identifier"},
                        "review_cycle_days": {"type": "integer", "description": "Review cycle in days"},
                        "recommendation": {"type": "string", "description": "Supplier status recommendation"}
                    },
                    "required": ["supplier_id"]
                }
            }
        }

class SearchPurchaseOrders(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get("supplier_id")
        status = kwargs.get("status")

        # Since we don't have purchase_orders data, we'll search inbound_shipments
        # which represent orders that have been placed and are being fulfilled
        inbound_shipments = data.get("inbound_shipments", [])
        results = []

        for shipment in inbound_shipments:
            match = True

            if supplier_id and shipment.get("supplier_id") != supplier_id:
                match = False
            if status:
                # Map shipment status to purchase order equivalent status
                po_status = "Delivered" if shipment.get("status") == "Received" else shipment.get("status")
                if po_status != status:
                    match = False
            if match:
                # Convert shipment data to purchase order format

                po_data = {
                    "po_id": shipment.get("purchase_order_number"),
                    "supplier_id": shipment.get("supplier_id"),
                    "supplier_name": shipment.get("supplier_name"),
                    "status": "Delivered" if shipment.get("status") == "Received" else shipment.get("status"),
                    "total_value": shipment.get("total_value"),
                    "value_currency": shipment.get("value_currency"),
                    "expected_delivery": shipment.get("expected_arrival_date"),
                    "actual_delivery": shipment.get("actual_arrival_date"),
                    "destination_warehouse": shipment.get("destination_warehouse_id"),
                    "tracking_number": shipment.get("tracking_number"),
                    "shipment_id": shipment.get("shipment_id")
                }
                results.append(po_data)

        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_purchase_orders",
                "description": "Search for purchase orders based on criteria (uses inbound shipment data)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "Supplier identifier"},
                        "status": {"type": "string", "description": "Purchase order status"}
                    },
                    "required": []
                }
            }
        }

class GetInventoryDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str, warehouse_id: str) -> str:
        inventory = data.get("inventory", [])

        inventory_item = next(
            (item for item in inventory
             if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id),
            None
        )

        if not inventory_item:
            return json.dumps({
                "error": f"Inventory not found for SKU {sku} in warehouse {warehouse_id}"
            })

        return json.dumps(inventory_item)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_details",
                "description": "Get detailed inventory information for a specific SKU and warehouse",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "Product SKU"},
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"}
                    },
                    "required": ["sku", "warehouse_id"]
                }
            }
        }

class PerformPhysicalCount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str, warehouse_id: str, **kwargs) -> str:
        inventory = data.get("inventory", [])
        instruction_amount = kwargs.get("instruction_amount", 0)
        quantity_available_flag = kwargs.get("quantity_available_flag", False)

        inventory_item = next(
            (item for item in inventory
             if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id),
            None
        )

        if not inventory_item:
            return json.dumps({"error": f"Inventory not found for SKU {sku} in warehouse {warehouse_id}"})

        # Simulate physical count with slight variance
        system_count = inventory_item.get("quantity_on_hand", 0)
        if quantity_available_flag:
            system_count = inventory_item.get("quantity_available", 0)
        physical_count = system_count - int(system_count * 0.0075)  # 0.75% variance
        if instruction_amount:
            physical_count = instruction_amount

        count_record = {
            "count_id": f"CNT-{sku}-{warehouse_id}",
            "sku": sku,
            "warehouse_id": warehouse_id,
            "system_count": system_count,
            "physical_count": physical_count,
            "count_date": get_current_timestamp(),
            "counter_id": "EMP-CYCLE-001",
            "variance": physical_count - system_count
        }

        if "cycle_counts" not in data:
            data["cycle_counts"] = []
        data["cycle_counts"].append(count_record)

        return json.dumps({
            "count_id": count_record["count_id"],
            "system_count": system_count,
            "physical_count": physical_count,
            "variance": count_record["variance"]
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "perform_physical_count",
                "description": "Perform physical inventory count for a specific SKU",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "Product SKU"},
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"},
                        "instruction_amount": {"type": "integer", "description": "Amount to adjust"},
                        "quantity_available_flag": {"type": "boolean", "description": "Use quantity available instead of quantity on hand"}
                    },
                    "required": ["sku", "warehouse_id"]
                }
            }
        }

class CalculateInventoryVariance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        system_count = kwargs.get("system_count")
        physical_count = kwargs.get("physical_count")
        instruction_count = kwargs.get("instruction_count")
        instruction_system_count = kwargs.get("instruction_system_count", 0)

        if instruction_count:
            physical_count = instruction_count

        if instruction_system_count:
            system_count = instruction_system_count

        if system_count == 0:
            variance_percentage = 0
        else:
            variance_percentage = abs((physical_count - system_count) / system_count) * 100

        variance = physical_count - system_count

        variance_analysis = {
            "sku": sku,
            "system_count": system_count,
            "physical_count": physical_count,
            "variance": variance,
            "variance_percentage": round(variance_percentage, 2),
            "variance_threshold_exceeded": variance_percentage > 2.0,
            "analysis_date": get_current_timestamp()
        }

        return json.dumps(variance_analysis)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_inventory_variance",
                "description": "Calculate variance between system and physical inventory counts",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "Product SKU"},
                        "system_count": {"type": "integer", "description": "System inventory count"},
                        "physical_count": {"type": "integer", "description": "Physical inventory count"},
                        "instruction_count": {"type": "integer", "description": "Instruction count"},
                        "instruction_system_count": {"type": "integer", "description": "Instruction system count"}
                    },
                    "required": ["sku"]
                }
            }
        }

class CreateInventoryAdjustment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        warehouse_id = kwargs.get("warehouse_id")
        adjustment_quantity = kwargs.get("adjustment_quantity")
        reason = kwargs.get("reason")

        inventory = data.get("inventory", [])

        inventory_item = next(
            (item for item in inventory
             if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id),
            None
        )

        if not inventory_item:
            return json.dumps({"error": f"Inventory not found for SKU {sku} in warehouse {warehouse_id}"})

        adjustment_id = f"ADJ-{warehouse_id}"

        # Update inventory quantities
        old_quantity = inventory_item.get("quantity_on_hand", 0)
        new_quantity = old_quantity + adjustment_quantity
        inventory_item["quantity_on_hand"] = new_quantity
        inventory_item["quantity_available"] = inventory_item.get("quantity_available", 0) + adjustment_quantity
        inventory_item["last_counted_date"] = get_current_year_month_day()

        # Create adjustment record
        adjustment_record = {
            "adjustment_id": adjustment_id,
            "sku": sku,
            "warehouse_id": warehouse_id,
            "adjustment_quantity": adjustment_quantity,
            "old_quantity": old_quantity,
            "new_quantity": new_quantity,
            "reason": reason,
            "adjustment_date": get_current_timestamp(),
            "adjusted_by": "SYSTEM"
        }

        if "inventory_adjustments" not in data:
            data["inventory_adjustments"] = []
        data["inventory_adjustments"].append(adjustment_record)

        # Calculate total adjustment value
        product_master = data.get("inventory", [])
        product = next((p for p in product_master if p.get("sku") == sku), None)
        unit_price = product.get("unit_cost", 0) if product else 0

        total_adjustment_value = abs(adjustment_quantity) * unit_price

        return json.dumps({
            "adjustment_id": adjustment_id,
            "old_quantity": old_quantity,
            "new_quantity": new_quantity,
            "adjustment_amount": adjustment_quantity,
            "total_adjustment_value": total_adjustment_value
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_inventory_adjustment",
                "description": "Create inventory adjustment record and update quantities",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "Product SKU"},
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"},
                        "adjustment_quantity": {"type": "integer", "description": "Quantity adjustment (positive or negative)"},
                        "reason": {"type": "string", "description": "Reason for adjustment"}
                    },
                    "required": ["sku", "warehouse_id", "adjustment_quantity", "reason"]
                }
            }
        }

class UpdateAccuracyMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str) -> str:
        warehouses = data.get("warehouses", [])
        inventory = data.get("inventory", [])
        cycle_counts = data.get("cycle_counts", [])

        warehouse = next((w for w in warehouses if w.get("warehouse_id") == warehouse_id), None)
        if not warehouse:
            return json.dumps({"error": f"Warehouse {warehouse_id} not found"})

        # Calculate accuracy metrics
        warehouse_inventory = [item for item in inventory if item.get("warehouse_id") == warehouse_id]
        warehouse_counts = [count for count in cycle_counts if count.get("warehouse_id") == warehouse_id]

        total_items = len(warehouse_inventory)
        accurate_counts = len([count for count in warehouse_counts if abs(count.get("variance", 0)) <= count.get("system_count", 1) * 0.02])

        accuracy_percentage = (accurate_counts / max(len(warehouse_counts), 1)) * 100 if warehouse_counts else 99.5

        metrics = {
            "warehouse_id": warehouse_id,
            "inventory_accuracy_percentage": round(accuracy_percentage, 2),
            "total_items_counted": len(warehouse_counts),
            "accurate_counts": accurate_counts,
            "last_updated": get_current_timestamp()
        }

        return json.dumps(metrics)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_accuracy_metrics",
                "description": "Update inventory accuracy metrics for a warehouse",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"}
                    },
                    "required": ["warehouse_id"]
                }
            }
        }

class GetCarrierPerformance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carrier_scac = kwargs.get("carrier_scac")
        route = kwargs.get("route")

        carriers = data.get("carriers", [])

        carrier = next((c for c in carriers if c.get("scac") == carrier_scac), None)
        if not carrier:
            return json.dumps({"error": f"Carrier {carrier_scac} not found"})

        performance_data = {
            "carrier_scac": carrier_scac,
            "carrier_name": carrier.get("carrier_name"),
            "performance_metrics": carrier.get("performance_metrics", {}),
            "supported_modes": carrier.get("supported_modes", []),
            "service_levels": carrier.get("service_levels", []),
            "regional_coverage": carrier.get("regional_coverage"),
            "active_status": carrier.get("active_status", False),
            "route_specific_data": f"Performance data for {route}" if route else None
        }

        return json.dumps(performance_data)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_carrier_performance",
                "description": "Retrieve carrier performance metrics and capabilities",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_scac": {"type": "string", "description": "Carrier SCAC code"},
                        "route": {"type": "string", "description": "Specific route or region"}
                    },
                    "required": ["carrier_scac"]
                }
            }
        }

class RequestShippingQuote(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carrier_scac = kwargs.get("carrier_scac")
        weight_kg = kwargs.get("weight_kg")
        destination = kwargs.get("destination")

        carriers = data.get("carriers", [])

        carrier = next((c for c in carriers if c.get("scac") == carrier_scac), None)
        if not carrier:
            return json.dumps({"error": f"Carrier {carrier_scac} not found"})

        # Simplified rate calculation
        base_rate_per_kg = {
            "MAEU": 2.50,  # Sea freight
            "DBSG": 1.80,  # Rail/Truck
            "FDEG": 4.50,  # Express
            "UPSN": 3.20,  # Ground/Air
            "HLCU": 2.30   # Sea freight
        }.get(carrier_scac, 3.00)

        estimated_cost = weight_kg * base_rate_per_kg
        quote_id = f"QTE-{carrier_scac}-{carrier.get('carrier_name')}"

        quote = {
            "quote_id": quote_id,
            "carrier_scac": carrier_scac,
            "carrier_name": carrier.get("carrier_name"),
            "weight_kg": weight_kg,
            "destination": destination,
            "estimated_cost": estimated_cost,
            "base_rate_per_kg": base_rate_per_kg,
            "quote_date": get_current_timestamp(),
            "validity_days": 30,
            "service_level": "Standard"
        }

        if "shipping_quotes" not in data:
            data["shipping_quotes"] = []
        data["shipping_quotes"].append(quote)

        return json.dumps({
            "quote_id": quote_id,
            "estimated_cost": estimated_cost,
            "carrier_name": carrier.get("carrier_name"),
            "validity_days": 30
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "request_shipping_quote",
                "description": "Request shipping quote from a carrier",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_scac": {"type": "string", "description": "Carrier SCAC code"},
                        "weight_kg": {"type": "number", "description": "Shipment weight in kg"},
                        "destination": {"type": "string", "description": "Destination location"}
                    },
                    "required": ["carrier_scac", "weight_kg", "destination"]
                }
            }
        }

# Additional required functions for complex tasks

class GetWarehouseCapacity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str) -> str:
        warehouses = data.get("warehouses", [])
        warehouse = next((w for w in warehouses if w.get("warehouse_id") == warehouse_id), None)

        if not warehouse:
            return json.dumps({"error": f"Warehouse {warehouse_id} not found"})

        total_capacity = warehouse.get("total_storage_capacity_cbm", 0)
        utilization = warehouse.get("current_utilization_percentage", 0)

        return json.dumps({
            "warehouse_id": warehouse_id,
            "total_capacity_cbm": total_capacity,
            "current_utilization_percentage": utilization,
            "used_capacity_cbm": total_capacity * (utilization / 100),
            "remaining_capacity_cbm": total_capacity * ((100 - utilization) / 100)
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_warehouse_capacity",
                "description": "Get warehouse capacity and utilization information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"}
                    },
                    "required": ["warehouse_id"]
                }
            }
        }

class CalculateUtilizationPercentage(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str) -> str:
        warehouses = data.get("warehouses", [])
        warehouse = next((w for w in warehouses if w.get("warehouse_id") == warehouse_id), None)

        if not warehouse:
            return json.dumps({"error": f"Warehouse {warehouse_id} not found"})

        utilization = warehouse.get("current_utilization_percentage", 85.0)

        return json.dumps({
            "warehouse_id": warehouse_id,
            "utilization_percentage": utilization,
            "status": "under_capacity" if utilization < 90 else "approaching_capacity"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_utilization_percentage",
                "description": "Calculate current warehouse utilization percentage",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"}
                    },
                    "required": ["warehouse_id"]
                }
            }
        }

class AnalyzeInventoryByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str) -> str:
        inventory = data.get("inventory", [])
        product_master = data.get("product_master", [])

        warehouse_inventory = [item for item in inventory if item.get("warehouse_id") == warehouse_id]

        category_analysis = {}
        for item in warehouse_inventory:
            sku = item.get("sku")
            product = next((p for p in product_master if p.get("sku") == sku), None)
            if product:
                category = product.get("category", "Unknown")
                if category not in category_analysis:
                    category_analysis[category] = {"items": 0, "total_value": 0}
                category_analysis[category]["items"] += 1
                category_analysis[category]["total_value"] += item.get("total_value", 0)

        return json.dumps({
            "warehouse_id": warehouse_id,
            "category_breakdown": category_analysis,
            "analysis_date": get_current_timestamp()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyze_inventory_by_category",
                "description": "Analyze inventory breakdown by product category",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"}
                    },
                    "required": ["warehouse_id"]
                }
            }
        }

class IdentifyOverflowOptions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str, required_capacity: int) -> str:
        warehouses = data.get("warehouses", [])
        current_warehouse = next((w for w in warehouses if w.get("warehouse_id") == warehouse_id), None)

        if not current_warehouse:
            return json.dumps({"error": f"Warehouse {warehouse_id} not found"})

        # Find nearby warehouses with available capacity
        overflow_options = []
        for warehouse in warehouses:
            if warehouse.get("warehouse_id") != warehouse_id:
                total_capacity = warehouse.get("total_storage_capacity_cbm", 0)
                utilization = warehouse.get("current_utilization_percentage", 0)
                available = total_capacity * ((100 - utilization) / 100)

                if available >= required_capacity:
                    overflow_options.append({
                        "warehouse_id": warehouse.get("warehouse_id"),
                        "warehouse_name": warehouse.get("warehouse_name"),
                        "available_capacity": available,
                        "city": warehouse.get("city")
                    })

        return json.dumps({
            "overflow_options": overflow_options[:3],  # Top 3 options
            "required_capacity": required_capacity
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "identify_overflow_options",
                "description": "Identify warehouse overflow options for excess capacity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "Current warehouse identifier"},
                        "required_capacity": {"type": "integer", "description": "Required overflow capacity"}
                    },
                    "required": ["warehouse_id", "required_capacity"]
                }
            }
        }

class CreateCapacityPlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str, optimization_strategy: str) -> str:
        plan_id = f"CAP-{warehouse_id}"

        capacity_plan = {
            "plan_id": plan_id,
            "warehouse_id": warehouse_id,
            "optimization_strategy": optimization_strategy,
            "created_date": get_current_timestamp(),
            "recommendations": [
                "Redistribute slow-moving inventory",
                "Optimize storage layout",
                "Consider seasonal adjustments"
            ],
            "expected_efficiency_gain": "15%",
            "implementation_timeline": "30_days"
        }

        if "capacity_plans" not in data:
            data["capacity_plans"] = []
        data["capacity_plans"].append(capacity_plan)

        return json.dumps({
            "plan_id": plan_id,
            "status": "Created",
            "optimization_strategy": optimization_strategy
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_capacity_plan",
                "description": "Create warehouse capacity optimization plan",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"},
                        "optimization_strategy": {"type": "string", "description": "Optimization strategy to apply"}
                    },
                    "required": ["warehouse_id", "optimization_strategy"]
                }
            }
        }

# Placeholder functions for complex logistics operations
class QuarantineInventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        lot_number = kwargs.get("lot_number")
        warehouse_id = kwargs.get("warehouse_id")
        reason = kwargs.get("reason")

        quarantine_id = f"QTN-{lot_number}-{warehouse_id}"

        return json.dumps({
            "quarantine_id": quarantine_id,
            "lot_number": lot_number,
            "warehouse_id": warehouse_id,
            "reason": reason,
            "status": "Quarantined",
            "quarantine_date": get_current_timestamp()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "quarantine_inventory",
                "description": "Quarantine inventory items by lot number",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lot_number": {"type": "string", "description": "Lot number to quarantine"},
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"},
                        "reason": {"type": "string", "description": "Reason for quarantine"}
                    },
                    "required": ["lot_number", "warehouse_id", "reason"]
                }
            }
        }

class CheckTemperatureLogs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        shipment_id = kwargs.get("shipment_id")
        shipments = data.get("inbound_shipments", [])
        required_temp_range = kwargs.get("required_temp_range")
        shipment = next((s for s in shipments if s.get("shipment_id") == shipment_id), None)
        excursions_flag = kwargs.get("excursions_flag", False)

        excursions_detected = False
        temperature_compliance = "compliant"

        if required_temp_range:
            temp_range = required_temp_range.split("-")
            if '-' in required_temp_range and 'below' in required_temp_range:
                min_temp = float(-30.0)
                max_temp = float(temp_range[1].replace('C', '').strip())
            elif 'to' in required_temp_range:
                to_range = required_temp_range.replace('C', '').split('to')
                # Handle negative values in the temperature range
                min_temp = float(to_range[0].strip())
                max_temp = float(to_range[1].strip())
            elif 'Cool, Dry' in required_temp_range:
                min_temp  = float(15)
                max_temp = float(25)
            else:
                min_temp = float(temp_range[0].replace('C', '').strip())
                max_temp = float(temp_range[1].replace('C', '').strip())

            if shipment['temperature_celsius'] is None:
                excursions_detected = False
                temperature_compliance = "compliant"
            else:
                if shipment['temperature_celsius'] < min_temp or shipment['temperature_celsius'] > max_temp:
                    excursions_detected = True
                    temperature_compliance = "non-compliant"


        else:
            if shipment['temperature_celsius'] is None:
                excursions_detected = False
                temperature_compliance = "compliant"

        if excursions_flag:
                excursions_detected = True
                temperature_compliance = "non-compliant"

        return json.dumps({
            "shipment_id": shipment_id,
            "temperature_compliance": temperature_compliance,
            "required_range": required_temp_range,
            "actual_temperature": shipment['temperature_celsius'],
            "excursions_detected": excursions_detected
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_temperature_logs",
                "description": "Check temperature monitoring logs for a shipment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "Shipment identifier"},
                        "required_temp_range": {"type": "string", "description": "Required temperature range"},
                        "excursions_flag": {"type": "boolean", "description": "Flag to check for temperature excursions"}
                    },
                    "required": ["shipment_id"]
                }
            }
        }

class VerifyColdChainIntegrity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str, carrier_scac: str) -> str:
        return json.dumps({
            "shipment_id": shipment_id,
            "carrier_scac": carrier_scac,
            "cold_chain_integrity": "maintained",
            "temperature_maintained": True,
            "verification_date": get_current_timestamp()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_cold_chain_integrity",
                "description": "Verify cold chain integrity for temperature-sensitive shipments",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "Shipment identifier"},
                        "carrier_scac": {"type": "string", "description": "Carrier SCAC code"}
                    },
                    "required": ["shipment_id", "carrier_scac"]
                }
            }
        }

class InitiateProductRecall(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], lot_number: str, recall_type: str) -> str:
        recall_id = f"RCL-{lot_number}-{recall_type}"

        return json.dumps({
            "recall_id": recall_id,
            "lot_number": lot_number,
            "recall_type": recall_type,
            "status": "Initiated",
            "recall_date": get_current_timestamp(),
            "recall_scope": f"all_lot_{lot_number}"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "initiate_product_recall",
                "description": "Initiate product recall for specific lot number",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lot_number": {"type": "string", "description": "Lot number to recall"},
                        "recall_type": {"type": "string", "description": "Type of recall (voluntary/mandatory/precautionary)"}
                    },
                    "required": ["lot_number", "recall_type"]
                }
            }
        }

class CreateIncidentReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        id = kwargs.get("id")
        incident_type = kwargs.get("incident_type")
        severity = kwargs.get("severity", "medium")

        incident_id = f"INC-{id}-{severity}"

        incident_report = {
            "incident_id": incident_id,
            "id": id,
            "incident_type": incident_type,
            "severity": severity,
            "reported_date": get_current_timestamp(),
            "reported_by": "SYSTEM",
            "status": "Open",
            "investigation_required": True,
            "regulatory_notification": severity in ["high", "critical"],
            "customer_notification": True,
            "estimated_impact": "TBD"
        }

        if "incident_reports" not in data:
            data["incident_reports"] = []
        data["incident_reports"].append(incident_report)

        return json.dumps({
            "incident_id": incident_id,
            "status": "Created",
            "investigation_required": True,
            "regulatory_notification_required": incident_report["regulatory_notification"]
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_incident_report",
                "description": "Create incident report for supply chain issues",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "Related identifier"},
                        "incident_type": {"type": "string", "description": "Type of incident"},
                        "severity": {"type": "string", "description": "Incident severity (low/medium/high/critical)"}
                    },
                    "required": ["id", "incident_type"]
                }
            }
        }

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

class GetApprovedSuppliers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str, **kwargs) -> str:
        suppliers = data.get("supplier_master", [])
        product_master = data.get("product_master", [])
        preferred_supplier = kwargs.get("preferred_supplier", None)

        # Find the product to get its category
        product = next((p for p in product_master if p.get("sku") == sku), None)
        if not product:
            return json.dumps({"error": f"Product {sku} not found"})

        product_category = product.get("category", "")

        # Find suppliers that provide products in this category
        approved_suppliers = []
        for supplier in suppliers:
            supplier_categories = supplier.get("product_categories", [])

            if preferred_supplier and supplier.get("supplier_id") == preferred_supplier:
                # If a preferred supplier is specified, prioritize it
                approved_suppliers.insert(0, {
                    "supplier_id": supplier.get("supplier_id"),
                    "supplier_name": supplier.get("supplier_name"),
                    "performance_rating": supplier.get("performance_rating"),
                    "on_time_delivery_percentage": supplier.get("on_time_delivery_percentage"),
                    "standard_lead_time_days": supplier.get("standard_lead_time_days"),
                    "relationship_status": supplier.get("relationship_status"),
                    "product_categories": supplier_categories
                })
                break
            else:
                # Check if supplier serves this product category and is active
                if (any(cat in product_category for cat in supplier_categories) and
                    supplier.get("relationship_status") == "Active" and
                    supplier.get("performance_rating", 0) >= 4.0):

                    approved_suppliers.append({
                        "supplier_id": supplier.get("supplier_id"),
                        "supplier_name": supplier.get("supplier_name"),
                        "performance_rating": supplier.get("performance_rating"),
                        "on_time_delivery_percentage": supplier.get("on_time_delivery_percentage"),
                        "standard_lead_time_days": supplier.get("standard_lead_time_days"),
                        "relationship_status": supplier.get("relationship_status"),
                        "product_categories": supplier.get("product_categories", [])
                    })

        return json.dumps({
            "sku": sku,
            "product_category": product_category,
            "approved_suppliers": approved_suppliers,
            "supplier_count": len(approved_suppliers)
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_approved_suppliers",
                "description": "Get list of approved suppliers for a specific SKU based on product category and performance criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Product SKU to find approved suppliers for",
                            "preferred_supplier": {
                                "type": "string",
                                "description": "Optional preferred supplier ID to prioritize in results"
                            }
                        }
                    },
                    "required": ["sku"]
                }
            }
        }

class CalculateFinancialImpact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_value = kwargs.get("product_value", 0)
        liability_estimate = kwargs.get("liability_estimate", 0)

        financial_impact = {
            "product_value_at_risk": product_value,
            "estimated_liability": liability_estimate,
            "total_financial_impact": product_value + liability_estimate,
            "insurance_coverage": min(product_value * 0.8, 100000),  # Simplified coverage calc
            "net_exposure": max(0, (product_value + liability_estimate) - min(product_value * 0.8, 100000)),
            "calculation_date": get_current_timestamp()
        }

        return json.dumps(financial_impact)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_financial_impact",
                "description": "Calculate financial impact of supply chain incidents",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_value": {"type": "number", "description": "Value of affected products"},
                        "liability_estimate": {"type": "number", "description": "Estimated liability amount"}
                    },
                    "required": ["product_value"]
                }
            }
        }

class EscalateToQualityTeam(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], incident_id: str, priority: str) -> str:
        escalation_id = f"ESC-{incident_id}"

        escalation = {
            "escalation_id": escalation_id,
            "incident_id": incident_id,
            "escalated_to": "Quality Assurance Team",
            "priority": priority,
            "escalation_date": get_current_timestamp(),
            "escalated_by": "SYSTEM",
            "expected_response_hours": 4 if priority == "critical" else 24,
            "status": "Pending",
            "assigned_to": "QA-MANAGER-001"
        }

        if "escalations" not in data:
            data["escalations"] = []
        data["escalations"].append(escalation)

        return json.dumps({
            "escalation_id": escalation_id,
            "assigned_to": "Quality Assurance Team",
            "expected_response_hours": escalation["expected_response_hours"]
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "escalate_to_quality_team",
                "description": "Escalate incident to quality assurance team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "incident_id": {"type": "string", "description": "Incident identifier"},
                        "priority": {"type": "string", "description": "Escalation priority"}
                    },
                    "required": ["incident_id", "priority"]
                }
            }
        }


class VerifyStorageCompliance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str, storage_type: str, **kwargs) -> str:
        warehouses = data.get("warehouses", [])
        warehouse = next((w for w in warehouses if w.get("warehouse_id") == warehouse_id), None)
        compliant_flag = kwargs.get("compliant_flag", True)

        if not warehouse:
            return json.dumps({"error": f"Warehouse {warehouse_id} not found"})

        warehouse_capabilities = warehouse.get("special_capabilities", [])
        certifications = warehouse.get("certifications", [])
        warehouse_type = warehouse.get("warehouse_type", "")

        compliance_status = "compliant"
        compliance_issues = []

        if certifications:
            if len(certifications) < 0:
                compliance_issues.append("Insufficient certifications")
                compliance_status = "non_compliant"
            else:
                compliance_status = "compliant"

        if not compliant_flag:
            compliance_status = "non_compliant"
            compliance_issues.append("Compliance required but not met")


        return json.dumps({
            "warehouse_id": warehouse_id,
            "storage_type": storage_type,
            "compliance_status": compliance_status,
            "warehouse_capabilities": warehouse_capabilities,
            "warehouse_certifications": certifications,
            "warehouse_type": warehouse_type,
            "compliance_issues": compliance_issues,
            "verification_date": get_current_timestamp()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_storage_compliance",
                "description": "Verify warehouse compliance for specific storage requirements",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"},
                        "storage_type": {"type": "string", "description": "Storage type to verify (hazmat, chemical, high_security, electronics, frozen, pharmaceutical)"},
                        "compliant_flag": {"type": "boolean", "description": "Whether compliance is required for the storage type"},
                    },
                    "required": ["warehouse_id", "storage_type"]
                }
            }
        }

TOOLS = [
    GetInventoryBySkuWarehouse(),
    CreatePurchaseOrder(),
    SearchInboundShipments(),
    GetOrderDetails(),
    VerifyInventoryAllocation(),
    SelectOptimalCarrier(),
    GenerateShippingLabels(),
    UpdateOrderStatus(),
    GetShipmentDetails(),
    VerifyCustomsDocumentation(),
    CalculateCustomsDuty(),
    ProcessDutyPayment(),
    UpdateCustomsStatus(),
    UpdateShipmentStatus(),
    GetSupplierPerformance(),
    CreateSupplierImprovementPlan(),
    SearchPurchaseOrders(),
    GetInventoryDetails(),
    PerformPhysicalCount(),
    CalculateInventoryVariance(),
    CreateInventoryAdjustment(),
    UpdateAccuracyMetrics(),
    GetCarrierPerformance(),
    RequestShippingQuote(),
    GetWarehouseCapacity(),
    CalculateUtilizationPercentage(),
    AnalyzeInventoryByCategory(),
    IdentifyOverflowOptions(),
    CreateCapacityPlan(),
    QuarantineInventory(),
    CheckTemperatureLogs(),
    VerifyColdChainIntegrity(),
    InitiateProductRecall(),
    CreateIncidentReport(),
    NotifySupplier(),
    CalculateFinancialImpact(),
    EscalateToQualityTeam(),
    GetApprovedSuppliers(),
    VerifyStorageCompliance(),
]
