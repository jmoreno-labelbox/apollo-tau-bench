import json
from datetime import datetime, timedelta
from typing import Any

from tau_bench.envs.tool import Tool

#--- READ-ONLY TOOLS ---




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


class FindProductByName(Tool):
    """Locates a product's SKU and additional details using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], product_name: str = None) -> str:
        products = data.get("product_master", {}).values()
        for product in products.values():
            if product.get("product_name") == product_name:
                payload = {
                    "sku": product.get("sku"),
                    "unit_price": product.get("unit_price"),
                    "weight_kg": product.get("weight_kg"),
                    "hazmat_information": product.get("hazmat_information"),
                    "country_of_origin": product.get("country_of_origin"),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Product not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindProductByName",
                "description": "Finds a product's SKU, price, weight, and hazmat information by its full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_name": {
                            "type": "string",
                            "description": "The full name of the product.",
                        }
                    },
                    "required": ["product_name"],
                },
            },
        }


class GetProductDetails(Tool):
    """Locates a product's information using its SKU."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None) -> str:
        products = data.get("product_master", {}).values()
        for product in products.values():
            if product.get("sku") == sku:
                payload = product
                out = json.dumps(payload)
                return out
        payload = {"error": "Product not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductDetails",
                "description": "Finds all product details from product_master by its sku",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The sku of the product.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }


class FindWarehouseByName(Tool):
    """Locates a warehouse's ID using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_name: str = None) -> str:
        warehouses = data.get("warehouses", {}).values()
        for warehouse in warehouses.values():
            if warehouse.get("warehouse_name") == warehouse_name:
                payload = {"warehouse_id": warehouse.get("warehouse_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": "Warehouse not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindWarehouseByName",
                "description": "Finds a warehouse's ID by its full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_name": {
                            "type": "string",
                            "description": "The full name of the warehouse.",
                        }
                    },
                    "required": ["warehouse_name"],
                },
            },
        }


class GetWarehouseDetails(Tool):
    """Obtains complete details for a warehouse using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str = None) -> str:
        warehouses = data.get("warehouses", {}).values()
        for warehouse in warehouses.values():
            if warehouse.get("warehouse_id") == warehouse_id:
                payload = warehouse
                out = json.dumps(payload)
                return out
        payload = {"error": "Warehouse not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWarehouseDetails",
                "description": "Retrieves the full record for a warehouse by its exact ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse (e.g., 'WH-01').",
                        }
                    },
                    "required": ["warehouse_id"],
                },
            },
        }


class GetAllWarehouses(Tool):
    """Fetches all warehouse records from the dataset, allowing for filtering."""

    @staticmethod
    def invoke(data: dict[str, Any], filters: dict[str, Any] = None) -> str:
        warehouses = data.get("warehouses", {}).values()

        if not warehouses:
            payload = {"message": "No warehouses found."}
            out = json.dumps(payload)
            return out

        if not filters:
            payload = warehouses
            out = json.dumps(payload)
            return out

        filtered_warehouses = []
        for warehouse in warehouses.values():
            match = True
            for key, value in filters.items():
                warehouse_value = warehouse.get(key)

                if isinstance(warehouse_value, list):
                    if value not in warehouse_value:
                        match = False
                        break
                elif isinstance(warehouse_value, str) and isinstance(value, str):
                    if warehouse_value.lower() != value.lower():
                        match = False
                        break
                elif warehouse_value != value:
                    match = False
                    break
            if match:
                filtered_data["warehouses"][warehouse_id] = warehouse

        if filtered_warehouses:
            payload = filtered_warehouses
            out = json.dumps(payload)
            return out
        else:
            payload = {"message": "No warehouses found matching the specified filters."}
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllWarehouses",
                "description": "Retrieves a list of all warehouses, with an option to filter by specific criteria like warehouse_type or certifications.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filters": {
                            "type": "object",
                            "description": "Optional. A dictionary of key-value pairs to filter warehouses. Example: {'warehouse_type': 'Cold Storage', 'certifications': 'FDA Registered'}",
                        }
                    },
                    "required": [],
                },
            },
        }


class GetInventoryDetails(Tool):
    """Obtains essential inventory information for a particular product at a specific warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, warehouse_id: str = None) -> str:
        inventory_items = data.get("inventory", {}).values()
        for item in inventory_items.values():
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                payload = {
                    "inventory_id": item.get("inventory_id"),
                    "reorder_point": item.get("reorder_point"),
                    "quantity_on_hand": item.get("quantity_on_hand"),
                    "quantity_available": item.get("quantity_available"),
                    "quantity_allocated": item.get("quantity_allocated"),
                    "quantity_inbound": item.get("quantity_inbound"),
                    "unit_cost": item.get("unit_cost"),
                    "unit_weight_kg": item.get("unit_weight_kg"),
                    "lot_number": item.get("lot_number"),
                    "unit_dimensions_cm": item.get("unit_dimensions_cm"),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Inventory record not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryDetails",
                "description": "Retrieves key inventory details for a specific product at a specific warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse.",
                        },
                    },
                    "required": ["sku", "warehouse_id"],
                },
            },
        }


class FindCarrierByMethodOfTransport(Tool):
    """Identifies the highest-rated, active carrier for a given transport method."""

    @staticmethod
    def invoke(data: dict[str, Any], method_of_transport: str = None) -> str:
        carriers = data.get("carriers", {}).values()
        if not method_of_transport:
            payload = {"error": "Method of transport is required"}
            out = json.dumps(payload)
            return out
        best_carrier = None
        max_rating = -1.0

        for carrier in carriers.values():
            is_active = carrier.get("active_status", False)
            supported_modes = [
                mode.lower() for mode in carrier.get("supported_modes", [])
            ]

            if is_active and method_of_transport.lower() in supported_modes:
                current_rating = carrier.get("performance_metrics", {}).values().get(
                    "average_rating", 0.0
                )
                if current_rating > max_rating:
                    max_rating = current_rating
                    best_carrier = carrier

        if best_carrier:
            payload = {
                "carrier_id": best_carrier.get("carrier_id"),
                "carrier_name": best_carrier.get("carrier_name"),
                "carrier_scac": best_carrier.get("scac"),
            }
            out = json.dumps(payload)
            return out
        else:
            payload = {
                "error": f"No active carrier found for transport method: {method_of_transport}"
            }
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCarrierByMethodOfTransport",
                "description": "Finds the active carrier with the highest average rating for a given method of transport (e.g., 'sea', 'air', 'truck').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "method_of_transport": {
                            "type": "string",
                            "description": "The method of transport to search for (e.g., 'sea', 'air', 'truck').",
                        }
                    },
                    "required": ["method_of_transport"],
                },
            },
        }


class FindCarrierByService(Tool):
    """Identifies the top-rated, active carrier for a specific transport mode and service level."""

    @staticmethod
    def invoke(data: dict[str, Any], mode_of_transport: str = None, service_level: str = None) -> str:
        carriers = data.get("carriers", {}).values()

        if not mode_of_transport or not service_level:
            payload = {"error": "Mode of transport and service level are required"}
            out = json.dumps(payload)
            return out

        best_carrier = None
        max_rating = -1.0

        for carrier in carriers.values():
            is_active = carrier.get("active_status", False)
            supported_modes = [
                mode.lower() for mode in carrier.get("supported_modes", [])
            ]
            supported_services = [
                service.lower() for service in carrier.get("service_levels", [])
            ]

            if (
                is_active
                and mode_of_transport.lower() in supported_modes
                and service_level.lower() in supported_services
            ):
                current_rating = carrier.get("performance_metrics", {}).values().get(
                    "average_rating", 0.0
                )
                if current_rating > max_rating:
                    max_rating = current_rating
                    best_carrier = carrier

        if best_carrier:
            payload = {
                "carrier_id": best_carrier.get("carrier_id"),
                "carrier_name": best_carrier.get("carrier_name"),
                "carrier_scac": best_carrier.get("scac"),
            }
            out = json.dumps(payload)
            return out
        else:
            payload = {
                "error": f"No active carrier found for mode '{mode_of_transport}' and service '{service_level}'"
            }
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCarrierByService",
                "description": "Finds the active carrier with the highest rating for a given transport mode AND a specific service level (e.g., 'Pharma', 'Perishables', 'Express').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mode_of_transport": {
                            "type": "string",
                            "description": "The required mode of transport (e.g., 'Air', 'Sea', 'Truck').",
                        },
                        "service_level": {
                            "type": "string",
                            "description": "The specific service level required (e.g., 'Pharma', 'Reefer', 'Express').",
                        },
                    },
                    "required": ["mode_of_transport", "service_level"],
                },
            },
        }


class CalculateExpectedArrivalDate(Tool):
    """Determines an expected arrival date based on the supplier's typical lead time."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, current_date: str = None) -> str:
        suppliers = data.get("supplier_master", {}).values()

        supplier_details = next(
            (s for s in suppliers.values() if s.get("supplier_id") == supplier_id), {}
        )
        if not supplier_details:
            payload = {"error": f"Supplier with ID '{supplier_id}' not found."}
            out = json.dumps(payload)
            return out

        lead_time = supplier_details.get("standard_lead_time_days")
        if lead_time is None:
            payload = {
                "error": f"Standard lead time is not available for supplier '{supplier_id}'."
            }
            out = json.dumps(payload)
            return out

        try:
            start_date = datetime.strptime(current_date, "%Y-%m-%d")
            delivery_date = start_date + timedelta(days=lead_time)
            formatted_date = delivery_date.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            payload = {
                "error": "Invalid date format for current_date. Please use YYYY-MM-DD."
            }
            out = json.dumps(payload)
            return out
        payload = {"expected_arrival_date": formatted_date}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateExpectedArrivalDate",
                "description": "Calculates the expected arrival date from a given start date using the specified supplier's standard lead time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier to get the lead time from.",
                        },
                        "current_date": {
                            "type": "string",
                            "description": "The starting date for the calculation, in YYYY-MM-DD format.",
                        },
                    },
                    "required": [
                        "supplier_id",
                        "current_date",
                    ],
                },
            },
        }


class FindSupplierByName(Tool):
    """Locates a supplier's ID and lead time using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_name: str = None) -> str:
        suppliers = data.get("supplier_master", {}).values()
        for supplier in suppliers.values():
            if supplier.get("supplier_name") == supplier_name:
                payload = {
                    "supplier_id": supplier.get("supplier_id"),
                    "standard_lead_time_days": supplier.get("standard_lead_time_days"),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Supplier not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindSupplierByName",
                "description": "Finds a supplier's ID and standard lead time by its full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_name": {
                            "type": "string",
                            "description": "The full name of the supplier.",
                        }
                    },
                    "required": ["supplier_name"],
                },
            },
        }


class FindInventoryBySku(Tool):
    """Identifies all inventory records for a specified SKU across all warehouses."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None) -> str:
        inventory_items = data.get("inventory", {}).values()
        found_records = []
        for item in inventory_items.values():
            if item.get("sku") == sku:
                found_records.append(
                    {
                        "inventory_id": item["inventory_id"],
                        "warehouse_id": item["warehouse_id"],
                        "warehouse_name": item["warehouse_name"],
                        "quantity_on_hand": item["quantity_on_hand"],
                        "quantity_available": item["quantity_available"],
                        "quantity_allocated": item["quantity_allocated"],
                        "quantity_inbound": item["quantity_inbound"],
                        "unit_cost": item["unit_cost"],
                        "lot_number": item["lot_number"],
                        "expiration_date": item["expiration_date"],
                        "unit_dimensions_cm": item["unit_dimensions_cm"],
                    }
                )
        if found_records:
            payload = found_records
            out = json.dumps(payload)
            return out
        payload = {"error": "No inventory records found for that SKU"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindInventoryBySku",
                "description": "Finds all inventory records for a given SKU, returning a list of locations and quantities.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to search for.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }


class FindInboundShipmentsByWarehouse(Tool):
    """Locates all inbound shipments intended for a particular warehouse ID."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str = None) -> str:
        inbound_shipments = data.get("inbound_shipments", {}).values()
        found_shipments = []
        for shipment in inbound_shipments.values():
            dest_id = shipment.get("destination_warehouse_id") or shipment.get(
                "destination_warehouse_id"
            )
            if dest_id == warehouse_id:
                found_data["shipments"][shipment_id] = shipment
        if found_shipments:
            payload = found_shipments
            out = json.dumps(payload)
            return out
        payload = {"message": "No inbound shipments found for that warehouse"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindInboundShipmentsByWarehouse",
                "description": "Finds all inbound shipments, including their status and expected arrival date, destined for a specific warehouse ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the destination warehouse (e.g., 'WH-01').",
                        }
                    },
                    "required": ["warehouse_id"],
                },
            },
        }


class GetSupplierDetails(Tool):
    """Obtains complete details for a supplier using their ID."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None) -> str:
        suppliers = data.get("supplier_master", {}).values()
        for supplier in suppliers.values():
            if supplier.get("supplier_id") == supplier_id:
                payload = supplier
                out = json.dumps(payload)
                return out
        payload = {"error": "Supplier not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupplierDetails",
                "description": "Retrieves the full record for a supplier by their id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The id of the supplier.",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }


class FindInboundShipmentsBySupplier(Tool):
    """Identifies all inbound shipments associated with a particular supplier ID."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None) -> str:
        inbound_shipments = data.get("inbound_shipments", {}).values()
        found_shipments = []
        for shipment in inbound_shipments.values():
            if shipment.get("supplier_id") == supplier_id:
                found_data["shipments"][shipment_id] = shipment
        if found_shipments:
            payload = found_shipments
            out = json.dumps(payload)
            return out
        payload = {"message": "No inbound shipments found for that supplier"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindInboundShipmentsBySupplier",
                "description": "Finds all inbound shipments associated with a specific supplier ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier (e.g., 'SUP-1001').",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }


class FindCheapestCarrierByService(Tool):
    """Identifies the lowest-cost, active carrier for a specific transport mode and service level."""

    @staticmethod
    def invoke(data: dict[str, Any], mode_of_transport: str = None, service_level: str = None) -> str:
        carriers = data.get("carriers", {}).values()

        if not mode_of_transport or not service_level:
            payload = {"error": "Mode of transport and service level are required"}
            out = json.dumps(payload)
            return out

        cheapest_carrier = None
        min_cost = float("inf")

        for carrier in carriers.values():
            is_active = carrier.get("active_status", False)
            supported_modes = [
                mode.lower() for mode in carrier.get("supported_modes", [])
            ]
            supported_services = [
                service.lower() for service in carrier.get("service_levels", [])
            ]

            if (
                is_active
                and mode_of_transport.lower() in supported_modes
                and service_level.lower() in supported_services
            ):
                current_cost = len(carrier.get("carrier_name", ""))
                if current_cost < min_cost:
                    min_cost = current_cost
                    cheapest_carrier = carrier

        if cheapest_carrier:
            payload = {
                "carrier_id": cheapest_carrier.get("carrier_id"),
                "carrier_name": cheapest_carrier.get("carrier_name"),
                "carrier_scac": cheapest_carrier.get("scac"),
            }
            out = json.dumps(payload)
            return out
        else:
            payload = {
                "error": f"No active carrier found for mode '{mode_of_transport}' and service '{service_level}'"
            }
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCheapestCarrierByService",
                "description": "Finds the active carrier with the lowest cost for a given transport mode and a specific service level (e.g., 'LTL', 'FTL').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mode_of_transport": {
                            "type": "string",
                            "description": "The required mode of transport (e.g., 'Truck', 'Rail').",
                        },
                        "service_level": {
                            "type": "string",
                            "description": "The specific service level required (e.g., 'LTL', 'Economy').",
                        },
                    },
                    "required": ["mode_of_transport", "service_level"],
                },
            },
        }


class FindOutboundOrderBySO(Tool):
    """Locates a single outbound order record using its Sales Order (SO) number."""

    @staticmethod
    def invoke(data: dict[str, Any], sales_order_number: str = None, outbound_orders: list = None) -> str:
        outbound_orders = outbound_orders if outbound_orders is not None else data.get("outbound_orders", {}).values()
        for order in outbound_orders.values()):
            if order.get("sales_order_number") == sales_order_number:
                payload = order
                out = json.dumps(payload)
                return out
        payload = {"error": "Outbound order not found for that Sales Order number"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindOutboundOrderBySo",
                "description": "Finds the full details of an outbound order using its Sales Order (SO) number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sales_order_number": {
                            "type": "string",
                            "description": "The Sales Order number of the order to find (e.g., 'SO-2024-0002').",
                        }
                    },
                    "required": ["sales_order_number"],
                },
            },
        }


class GetAllOutboundOrders(Tool):
    """Fetches all outbound order records from the dataset, with filtering options."""

    @staticmethod
    def invoke(data: dict[str, Any], filters: dict[str, Any] = None) -> str:
        outbound_orders = data.get("outbound_orders", {}).values()

        if not outbound_orders:
            payload = {"message": "No outbound orders found."}
            out = json.dumps(payload)
            return out

        if not filters:
            payload = outbound_orders
            out = json.dumps(payload)
            return out

        filtered_orders = []
        for order in outbound_orders.values():
            match = True
            for key, value in filters.items():
                order_value = order.get(key)
                if isinstance(order_value, str) and isinstance(value, str):
                    if order_value.lower() != value.lower():
                        match = False
                        break
                elif isinstance(order_value, bool) and isinstance(value, str):
                    if str(order_value).lower() != value.lower():
                        match = False
                        break
                elif order_value != value:
                    match = False
                    break
            if match:
                filtered_data["orders"][order_id] = order

        if filtered_orders:
            payload = filtered_orders
            out = json.dumps(payload)
            return out
        else:
            payload = {"message": "No outbound orders found matching the specified filters."}
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllOutboundOrders",
                "description": "Retrieves a list of all outbound orders, with an option to filter by specific criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filters": {
                            "type": "object",
                            "description": "Optional. A dictionary of key-value pairs to filter the orders. Keys must be valid fields from the order record. Example: {'status': 'In Transit', 'fragile': true}",
                        }
                    },
                    "required": [],
                },
            },
        }


class GetCarrierDetailsByName(Tool):
    """Obtains complete details for a carrier using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], carrier_name: str = None) -> str:
        carriers = data.get("carriers", {}).values()
        for carrier in carriers.values():
            if carrier.get("carrier_name") == carrier_name:
                payload = carrier
                out = json.dumps(payload)
                return out
        payload = {"error": "Carrier not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCarrierDetailsByName",
                "description": "Retrieves the full record for a carrier by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_name": {
                            "type": "string",
                            "description": "The full name of the carrier.",
                        }
                    },
                    "required": ["carrier_name"],
                },
            },
        }


#--- WRITE/UPDATE TOOLS ---


class CreateInboundShipment(Tool):
    """Generates a new inbound shipment record that also functions as a Purchase Order."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_id: str,
        destination_warehouse_id: str,
        order_quantity: float,
        unit_cost: float,
        unit_weight: float,
        expected_arrival_date: str,
        origin_address: str = None,
        origin_city: str = None,
        origin_country: str = None,
        destination_address: str = None,
        destination_city: str = None,
        destination_country: str = None,
        carrier_name: str = None,
        carrier_scac: str = None,
        mode_of_transport: str = "Sea",
        incoterms: str = "FOB",
        container_number: str = None,
        bill_of_lading: str = None,
        tracking_number: str = None,
        expected_departure_date: str = None,
        actual_departure_date: str = None,
        actual_arrival_date: str = None,
        number_of_packages: int = None,
        total_volume_cbm: float = None,
        customs_entry_number: str = None,
        destination_warehouse_name: str = None,
        duty_paid: bool = False,
        temperature_control_required: bool = False,
        temperature_celsius: float = None,
        hazmat: bool = False,
        hazmat_class: str = None,
        value_currency: str = "USD",
        insurance_policy_number: str = None,
        insurance_provider: str = None,
        priority_level: str = "Medium",
        notes: str = None,
        supplier_name: Any = None,
    ) -> str:
        if not all(
            [
                supplier_id,
                destination_warehouse_id,
                order_quantity,
                unit_cost,
                unit_weight,
                expected_arrival_date,
            ]
        ):
            payload = {"error": "One or more required arguments are missing."}
            out = json.dumps(payload)
            return out

        inbound_shipments = data.get("inbound_shipments", {}).values()

        max_ship_num = 0
        for shipment in inbound_shipments.values():
            ship_id = shipment.get("shipment_id", "SHIP-0000")
            ship_num_str = ship_id.split("-")[-1]
            if ship_num_str.isdigit():
                max_ship_num = max(max_ship_num, int(ship_num_str))
        new_shipment_id = f"SHIP-{max_ship_num + 1:04d}"

        max_po_num = 0
        for shipment in inbound_shipments.values():
            po_num_str = shipment.get("purchase_order_number", "PO-2024-0000").split(
                "-"
            )[-1]
            if po_num_str.isdigit():
                max_po_num = max(max_po_num, int(po_num_str))
        new_po_number = f"PO-2024-{max_po_num + 1:04d}"

        warehouses = data.get("warehouses", {}).values()
        destination_warehouse_details = next(
            (
                wh
                for wh in warehouses.values() if wh.get("warehouse_id") == destination_warehouse_id
            ),
            {},
        )

        suppliers = data.get("supplier_master", {}).values()
        supplier_details = next(
            (sup for sup in suppliers.values() if sup.get("supplier_id") == supplier_id), {}
        )
        supplier_contact_info = supplier_details.get("contact_information", {}).values()
        supplier_address = supplier_contact_info.get("address", {}).values()

        new_shipment = {
            "shipment_id": new_shipment_id,
            "purchase_order_number": new_po_number,
            "supplier_id": supplier_id,
            "supplier_name": supplier_details.get("supplier_name"),
            "origin_address": origin_address or supplier_address.get("street"),
            "origin_city": origin_city or supplier_address.get("city"),
            "origin_country": origin_country or supplier_address.get("country"),
            "destination_warehouse_id": destination_warehouse_id,
            "destination_warehouse_name": destination_warehouse_details.get(
                "warehouse_name"
            ),
            "destination_address": destination_address or destination_warehouse_details.get("address"),
            "destination_city": destination_city or destination_warehouse_details.get("city"),
            "destination_country": destination_country or destination_warehouse_details.get("country"),
            "carrier_name": carrier_name,
            "carrier_scac": carrier_scac,
            "mode_of_transport": mode_of_transport,
            "incoterms": incoterms,
            "container_number": container_number,
            "bill_of_lading": bill_of_lading,
            "tracking_number": tracking_number,
            "expected_departure_date": expected_departure_date,
            "expected_arrival_date": expected_arrival_date,
            "actual_departure_date": actual_departure_date,
            "actual_arrival_date": actual_arrival_date,
            "status": "Planned",
            "number_of_packages": number_of_packages or max(1, round(order_quantity / 100)),
            "total_weight_kg": round(order_quantity * unit_weight, 2),
            "total_volume_cbm": total_volume_cbm,
            "unit_of_measure_weight": "kg",
            "unit_of_measure_volume": "cbm",
            "customs_clearance_status": "Scheduled",
            "customs_entry_number": customs_entry_number,
            "duty_paid": duty_paid,
            "temperature_control_required": temperature_control_required,
            "temperature_celsius": temperature_celsius,
            "hazmat": hazmat,
            "hazmat_class": hazmat_class,
            "value_currency": value_currency,
            "total_value": round(order_quantity * unit_cost, 2),
            "insurance_policy_number": insurance_policy_number,
            "insurance_provider": insurance_provider,
            "priority_level": priority_level,
            "notes": notes,
        }
        inbound_data["shipments"][shipment_id] = new_shipment
        payload = {
            "status": "success",
            "shipment_id": new_shipment_id,
            "purchase_order_number": new_po_number,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInboundShipment",
                "description": "Creates a new planned inbound shipment, generating a new PO number. Fills in default values for any non-required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier.",
                        },
                        "destination_warehouse_id": {
                            "type": "string",
                            "description": "The ID of the destination warehouse.",
                        },
                        "order_quantity": {
                            "type": "integer",
                            "description": "The total quantity of the product being ordered.",
                        },
                        "unit_cost": {
                            "type": "number",
                            "description": "The cost per unit for calculating total value.",
                        },
                        "unit_weight": {
                            "type": "number",
                            "description": "The weight per unit in kg for calculating total weight.",
                        },
                        "expected_arrival_date": {
                            "type": "string",
                            "description": "The calculated expected arrival date (YYYY-MM-DD).",
                        },
                        "origin_address": {
                            "type": "string",
                            "description": "Optional. The supplier's origin street address. Defaults to supplier's master data if not provided.",
                        },
                        "origin_city": {
                            "type": "string",
                            "description": "Optional. The supplier's origin city. Defaults to supplier's master data if not provided.",
                        },
                        "origin_country": {
                            "type": "string",
                            "description": "Optional. The supplier's origin country. Defaults to supplier's master data if not provided.",
                        },
                        "destination_address": {
                            "type": "string",
                            "description": "Optional. The warehouse's destination street address. Defaults to warehouse's master data if not provided.",
                        },
                        "destination_city": {
                            "type": "string",
                            "description": "Optional. The warehouse's destination city. Defaults to warehouse's master data if not provided.",
                        },
                        "destination_country": {
                            "type": "string",
                            "description": "Optional. The warehouse's destination country. Defaults to warehouse's master data if not provided.",
                        },
                        "carrier_name": {
                            "type": "string",
                            "description": "Optional. The name of the assigned carrier.",
                        },
                        "carrier_scac": {
                            "type": "string",
                            "description": "Optional. The SCAC code for the carrier.",
                        },
                        "mode_of_transport": {
                            "type": "string",
                            "description": "Optional. The mode of transport (e.g., 'Sea', 'Air'). Defaults to 'Sea'.",
                        },
                        "incoterms": {
                            "type": "string",
                            "description": "Optional. The Incoterms for the shipment (e.g., 'FOB', 'CIF'). Defaults to 'FOB'.",
                        },
                        "container_number": {
                            "type": "string",
                            "description": "Optional. The shipping container number, if applicable.",
                        },
                        "bill_of_lading": {
                            "type": "string",
                            "description": "Optional. The Bill of Lading (BOL) or Air Waybill (AWB) number.",
                        },
                        "tracking_number": {
                            "type": "string",
                            "description": "Optional. The carrier's tracking number for the shipment.",
                        },
                        "expected_departure_date": {
                            "type": "string",
                            "description": "Optional. The expected departure date (YYYY-MM-DD).",
                        },
                        "actual_departure_date": {
                            "type": "string",
                            "description": "Optional. The actual departure date (YYYY-MM-DD).",
                        },
                        "actual_arrival_date": {
                            "type": "string",
                            "description": "Optional. The actual arrival date (YYYY-MM-DD).",
                        },
                        "number_of_packages": {
                            "type": "integer",
                            "description": "Optional. Estimated number of packages. Defaults to a calculation based on order quantity.",
                        },
                        "total_volume_cbm": {
                            "type": "number",
                            "description": "Optional. The total volume of the shipment in cubic meters (cbm).",
                        },
                        "customs_entry_number": {
                            "type": "string",
                            "description": "Optional. The customs entry number once cleared.",
                        },
                        "duty_paid": {
                            "type": "boolean",
                            "description": "Optional. Set to true if customs duties have been paid. Defaults to false.",
                        },
                        "temperature_control_required": {
                            "type": "boolean",
                            "description": "Optional. Set to true if the shipment requires temperature control. Defaults to false.",
                        },
                        "temperature_celsius": {
                            "type": "number",
                            "description": "Optional. The required temperature in Celsius, if applicable.",
                        },
                        "hazmat": {
                            "type": "boolean",
                            "description": "Optional. Set to true if the shipment contains hazardous materials. Defaults to false.",
                        },
                        "hazmat_class": {
                            "type": "string",
                            "description": "Optional. The hazmat class, if applicable.",
                        },
                        "value_currency": {
                            "type": "string",
                            "description": "Optional. The currency for the total value (e.g., 'USD', 'EUR'). Defaults to 'USD'.",
                        },
                        "insurance_policy_number": {
                            "type": "string",
                            "description": "Optional. The insurance policy number covering the shipment.",
                        },
                        "insurance_provider": {
                            "type": "string",
                            "description": "Optional. The name of the insurance provider.",
                        },
                        "priority_level": {
                            "type": "string",
                            "description": "Optional. The priority of the shipment (e.g., 'Medium', 'High'). Defaults to 'Medium'.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional. Any notes to add to the shipment record.",
                        },
                    },
                    "required": [
                        "supplier_id",
                        "destination_warehouse_id",
                        "order_quantity",
                        "unit_cost",
                        "unit_weight",
                        "expected_arrival_date",
                    ],
                },
            },
        }


class UpdateInventoryInboundQuantity(Tool):
    """Revises the inbound quantity for a particular product within a warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, warehouse_id: str = None, quantity_to_add: int = None) -> str:
        inventory_items = data.get("inventory", {}).values()
        for item in inventory_items.values():
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                original_inbound = item.get("quantity_inbound", 0)
                item["quantity_inbound"] = original_inbound + quantity_to_add
                payload = {
                    "status": "success",
                    "inventory_id": item.get("inventory_id"),
                    "new_inbound_quantity": item["quantity_inbound"],
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Inventory record not found to update"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryInboundQuantity",
                "description": "Updates the inbound quantity for a specific product in a warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse.",
                        },
                        "quantity_to_add": {
                            "type": "integer",
                            "description": "The quantity to add to the inbound total.",
                        },
                    },
                    "required": ["sku", "warehouse_id", "quantity_to_add"],
                },
            },
        }


class UpdateInventoryAllocatedQuantity(Tool):
    """Modifies the allocated and available quantities for a product in a warehouse when an order is created."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, warehouse_id: str = None, quantity_to_allocate: int = None) -> str:
        inventory_items = data.get("inventory", {}).values()

        if not all([sku, warehouse_id, quantity_to_allocate]):
            payload = {"error": "SKU, warehouse ID, and quantity to allocate are required."}
            out = json.dumps(payload)
            return out

        for item in inventory_items.values():
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                available = item.get("quantity_available", 0)
                if available < quantity_to_allocate:
                    payload = {
                        "error": f"Insufficient quantity available. Available: {available}, Required: {quantity_to_allocate}"
                    }
                    out = json.dumps(payload)
                    return out

                original_allocated = item.get("quantity_allocated", 0)
                item["quantity_available"] = available - quantity_to_allocate
                item["quantity_allocated"] = original_allocated + quantity_to_allocate
                payload = {
                    "status": "success",
                    "inventory_id": item.get("inventory_id"),
                    "new_available_quantity": item["quantity_available"],
                    "new_allocated_quantity": item["quantity_allocated"],
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Inventory record not found to update"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryAllocatedQuantity",
                "description": "Allocates stock for an outbound order, decreasing available quantity and increasing allocated quantity.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to allocate.",
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse from which to allocate.",
                        },
                        "quantity_to_allocate": {
                            "type": "integer",
                            "description": "The quantity of the product to allocate.",
                        },
                    },
                    "required": ["sku", "warehouse_id", "quantity_to_allocate"],
                },
            },
        }


class CreateOutboundOrder(Tool):
    """Generates a new outbound order record."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        warehouse_id: str = None,
        carrier_scac: str = None,
        sales_order_number: str = None,
        customer_id: str = None,
        customer_name: str = None,
        customer_address: str = None,
        customer_city: str = None,
        customer_country: str = None,
        destination_address: str = None,
        destination_city: str = None,
        destination_country: str = None,
        order_date: str = None,
        promised_ship_date: str = None,
        expected_delivery_date: str = None,
        number_of_line_items: int = 1,
        total_units: int = 1,
        number_of_packages: int = None,
        packaging_type: str = "Insulated Box",
        total_weight_kg: float = 1.0,
        total_volume_cbm: float = None,
        value_currency: str = "USD",
        total_value: float = None,
        carrier_name: str = None,
        mode_of_transport: str = None,
        shipping_service_level: str = None,
        shipping_cost: float = None,
        payment_terms: str = "Net 30",
        temperature_control_required: bool = False,
        temperature_celsius: float = None,
        hazmat: bool = False,
        hazmat_class: str = None,
        fragile: bool = True,
        priority_level: str = "Medium",
        notes: str = None
    ) -> str:
        outbound_orders = data.get("outbound_orders", {}).values()
        warehouses = data.get("warehouses", {}).values()

        max_order_num = 0
        for order in outbound_orders.values():
            order_id = order.get("order_id", "ORD-0000")
            order_num_str = order_id.split("-")[-1]
            if order_num_str.isdigit():
                max_order_num = max(max_order_num, int(order_num_str))
        new_order_id = f"ORD-{max_order_num + 1:04d}"

        warehouse_details = next(
            (wh for wh in warehouses.values() if wh.get("warehouse_id") == warehouse_id), {}
        )
        warehouse_name = warehouse_details.get("warehouse_name", "")
        warehouse_address = warehouse_details.get("address", "")
        origin_city = warehouse_details.get("city", "")
        origin_country = warehouse_details.get("country", "")

        new_order = {
            "order_id": new_order_id,
            "sales_order_number": sales_order_number,
            "customer_id": customer_id,
            "customer_name": customer_name,
            "customer_address": customer_address,
            "customer_city": customer_city,
            "customer_country": customer_country,
            "destination_address": destination_address,
            "destination_city": destination_city,
            "destination_country": destination_country,
            "warehouse_id": warehouse_id,
            "warehouse_name": warehouse_name,
            "warehouse_address": warehouse_address,
            "origin_city": origin_city,
            "origin_country": origin_country,
            "order_date": order_date,
            "promised_ship_date": promised_ship_date,
            "actual_ship_date": None,
            "expected_delivery_date": expected_delivery_date,
            "actual_delivery_date": None,
            "status": "Pending",
            "number_of_line_items": number_of_line_items,
            "total_units": total_units,
            "number_of_packages": number_of_packages,
            "packaging_type": packaging_type,
            "total_weight_kg": total_weight_kg,
            "total_volume_cbm": total_volume_cbm,
            "unit_of_measure_weight": "kg",
            "unit_of_measure_volume": "cbm",
            "value_currency": value_currency,
            "total_value": total_value,
            "carrier_name": carrier_name,
            "carrier_scac": carrier_scac,
            "mode_of_transport": mode_of_transport,
            "shipping_service_level": shipping_service_level,
            "tracking_number": None,
            "shipping_cost": shipping_cost,
            "payment_terms": payment_terms,
            "temperature_control_required": temperature_control_required,
            "temperature_celsius": temperature_celsius,
            "hazmat": hazmat,
            "hazmat_class": hazmat_class,
            "fragile": fragile,
            "priority_level": priority_level,
            "return_status": "None",
            "notes": notes,
        }
        outbound_data["orders"][order_id] = new_order
        payload = {
            "status": "success",
            "order_id": new_order_id,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOutboundOrder",
                "description": "Creates a new outbound order record in a 'Pending' state.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sales_order_number": {"type": "string"},
                        "customer_name": {"type": "string"},
                        "destination_city": {"type": "string"},
                        "destination_country": {"type": "string"},
                        "warehouse_id": {"type": "string"},
                        "carrier_name": {"type": "string"},
                        "carrier_scac": {"type": "string"},
                        "mode_of_transport": {"type": "string"},
                        "shipping_service_level": {"type": "string"},
                        "total_units": {"type": "integer"},
                        "total_weight_kg": {"type": "number"},
                        "temperature_control_required": {"type": "boolean"},
                        "temperature_celsius": {"type": "number"},
                        "hazmat": {"type": "boolean"},
                        "hazmat_class": {"type": "string"},
                        "priority_level": {"type": "string"},
                        "order_date": {
                            "type": "string",
                            "description": "Date of the order in YYYY-MM-DD format.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes for the order.",
                        },
                    },
                    "required": [
                        "sales_order_number",
                        "customer_name",
                        "warehouse_id",
                        "carrier_scac",
                        "order_date",
                    ],
                },
            },
        }


class UpdateShipmentNotes(Tool):
    """Revises the notes for a particular inbound shipment."""

    @staticmethod
    def invoke(data: dict[str, Any], shipment_id: str = None, new_note: str = None) -> str:
        inbound_shipments = data.get("inbound_shipments", {}).values()

        for shipment in inbound_shipments.values():
            if shipment.get("shipment_id") == shipment_id:
                original_note = shipment.get("notes")
                if original_note:
                    shipment["notes"] = f"{original_note} | {new_note}"
                else:
                    shipment["notes"] = new_note
                payload = {
                    "status": "success",
                    "shipment_id": shipment_id,
                    "updated_notes": shipment["notes"],
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Shipment ID not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateShipmentNotes",
                "description": "Updates the notes field for a specific inbound shipment record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {
                            "type": "string",
                            "description": "The ID of the shipment to update (e.g., 'SHIP-0001').",
                        },
                        "new_note": {
                            "type": "string",
                            "description": "The new note to add to the shipment record.",
                        },
                    },
                    "required": ["shipment_id", "new_note"],
                },
            },
        }


class UpdateInventoryStatus(Tool):
    """Modifies the stock status for a particular inventory ID."""

    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None, new_status: str = None) -> str:
        inventory_items = data.get("inventory", {}).values()

        if not inventory_id or not new_status:
            payload = {"error": "Inventory ID and new status are required."}
            out = json.dumps(payload)
            return out

        for item in inventory_items.values():
            if item.get("inventory_id") == inventory_id:
                item["stock_status"] = new_status
                if new_status.lower() == "quarantined":
                    item["quantity_available"] = 0
                payload = {
                    "status": "success",
                    "inventory_id": inventory_id,
                    "new_stock_status": item["stock_status"],
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Inventory ID not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryStatus",
                "description": "Updates the stock status of a specific inventory item (e.g., to 'In Stock', 'Quarantined'). If status is set to 'Quarantined', it also sets the available quantity to 0.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "The unique ID of the inventory record to update (e.g., 'INV-0001').",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new stock status to set.",
                        },
                    },
                    "required": ["inventory_id", "new_status"],
                },
            },
        }


class PerformInventoryAdjustment(Tool):
    """
    Conducts a complete inventory adjustment for a product at a designated warehouse.
    It revises the quantity on hand, available quantity, last counted date, and appends an audit note.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        sku: str,
        warehouse_id: str,
        new_physical_count: int,
        current_date: str,
        reason_note: str = ""
,
    current_allocated_quantity: Any = None,
    ) -> str:
        inventory_items = data.get("inventory", {}).values()

        if not all(
            [
                sku,
                warehouse_id,
                new_physical_count is not None,
                current_date,
            ]
        ):
            payload = {"error": "One or more required arguments are missing."}
            out = json.dumps(payload)
            return out

        for item in inventory_items.values():
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                original_on_hand = item.get("quantity_on_hand", 0)
                discrepancy = new_physical_count - original_on_hand

                item["quantity_on_hand"] = new_physical_count
                item["quantity_available"] = max(
                    0, new_physical_count - item.get("quantity_allocated", 0)
                )
                item["last_counted_date"] = current_date

                if reason_note:
                    adjustment_log = f"Adjustment on {current_date}: Count changed from {original_on_hand} to {new_physical_count} (Discrepancy: {discrepancy}). Reason: {reason_note}."
                    if item.get("notes"):
                        item["notes"] = f"{item['notes']} | {adjustment_log}"
                    else:
                        item["notes"] = adjustment_log
                payload = {
                    "status": "success",
                    "inventory_id": item.get("inventory_id"),
                    "new_on_hand_quantity": item["quantity_on_hand"],
                    "new_available_quantity": item["quantity_available"],
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Inventory record not found to adjust"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PerformInventoryAdjustment",
                "description": "Updates inventory quantities based on a physical count, adjusts available stock, updates the count date, and logs the reason.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to adjust.",
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse where the adjustment is occurring.",
                        },
                        "new_physical_count": {
                            "type": "integer",
                            "description": "The new, correct physical quantity on hand.",
                        },
                        "current_date": {
                            "type": "string",
                            "description": "The date of the adjustment in YYYY-MM-DD format.",
                        },
                        "reason_note": {
                            "type": "string",
                            "description": "Optional. A reason for the adjustment, which will be logged in the inventory record.",
                        },
                    },
                    "required": [
                        "sku",
                        "warehouse_id",
                        "new_physical_count",
                        "current_date",
                    ],
                },
            },
        }


class UpdateOutboundOrderDetails(Tool):
    """Modifies one or more fields for a particular outbound order."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, notes: str = None,
    destination_address: Any = None,
    return_status: Any = None,
    status: Any = None,
    destination_city: str = None,
    destination_country: str = None,
    carrier_name: str = None,
    carrier_scac: str = None,
    ) -> str:
        if not order_id:
            payload = {"error": "order_id is a required argument."}
            out = json.dumps(payload)
            return out

        outbound_orders = data.get("outbound_orders", {}).values()
        order_to_update = next(
            (o for o in outbound_orders.values() if o.get("order_id") == order_id), None
        )

        if not order_to_update:
            payload = {"error": f"Order with ID '{order_id}' not found."}
            out = json.dumps(payload)
            return out

        updated_fields = []

        if notes is not None:
            original_note = order_to_update.get("notes", "")
            if original_note:
                order_to_update["notes"] = f"{original_note} | {notes}"
            else:
                order_to_update["notes"] = notes
            updated_fields.append("notes")

        if not updated_fields:
            payload = {"message": "No valid fields provided to update."}
            out = json.dumps(payload)
            return out
        payload = {
            "status": "success",
            "order_id": order_id,
            "updated_fields": updated_fields,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOutboundOrderDetails",
                "description": "Updates details of an existing outbound order. Use this to change status, destination, or add notes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The unique ID of the order to update (e.g., 'ORD-0002').",
                        },
                        "destination_address": {
                            "type": "string",
                            "description": "The new destination street address.",
                        },
                        "destination_city": {
                            "type": "string",
                            "description": "The new destination city.",
                        },
                        "destination_country": {
                            "type": "string",
                            "description": "The new destination country.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status of the order (e.g., 'Diverted', 'Cancelled').",
                        },
                        "notes": {
                            "type": "string",
                            "description": "A new note to append to the order's existing notes.",
                        },
                    },
                    "required": ["order_id"],
                },
            },
        }


class CreateInventoryRecord(Tool):
    """Generates a new, blank inventory record for a product in a designated warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, warehouse_id: str = None) -> str:
        if not sku or not warehouse_id:
            payload = {"error": "SKU and warehouse_id are required."}
            out = json.dumps(payload)
            return out

        inventory_items = data.get("inventory", {}).values()
        for item in inventory_items.values():
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                payload = {
                    "error": f"Inventory record for SKU {sku} at warehouse {warehouse_id} already exists."
                }
                out = json.dumps(payload)
                return out

        product_details = {}
        products = data.get("product_master", {}).values()
        for p in products.values():
            if p.get("sku") == sku:
                product_details = p
                break

        warehouse_details = {}
        warehouses = data.get("warehouses", {}).values()
        warehouse_details = next(
            (wh for wh in warehouses.values() if wh.get("warehouse_id") == warehouse_id), {}
        )

        if not product_details or not warehouse_details:
            payload = {
                "error": "Could not find product or warehouse details to create the record."
            }
            out = json.dumps(payload)
            return out

        max_inv_num = 0
        for item in inventory_items.values():
            inv_id = item.get("inventory_id", "INV-0000")
            inv_num_str = inv_id.split("-")[-1]
            if inv_num_str.isdigit():
                max_inv_num = max(max_inv_num, int(inv_num_str))
        new_inventory_id = f"INV-{max_inv_num + 1:04d}"

        new_record = {
            "inventory_id": new_inventory_id,
            "sku": sku,
            "product_name": product_details.get("product_name"),
            "product_description": product_details.get("product_description"),
            "warehouse_id": warehouse_id,
            "warehouse_name": warehouse_details.get("warehouse_name"),
            "location_in_warehouse": None,
            "quantity_on_hand": 0,
            "quantity_available": 0,
            "quantity_allocated": 0,
            "quantity_inbound": 0,
            "quantity_damaged": 0,
            "unit_cost": product_details.get("unit_price"),
            "total_value": 0.00,
            "currency": product_details.get("currency"),
            "unit_weight_kg": product_details.get("weight_kg"),
            "unit_dimensions_cm": product_details.get("dimensions_cm"),
            "lot_number": None,
            "expiration_date": None,
            "received_date": None,
            "last_counted_date": None,
            "reorder_point": 0,
            "stock_status": "Out of Stock",
            "storage_requirements": product_details.get("storage_requirements"),
        }

        data["inventory"][inventory_id] = new_record
        payload = {
            "status": "success",
            "inventory_id": new_inventory_id,
            "message": "New inventory record created.",
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInventoryRecord",
                "description": "Creates a new, empty inventory record for a given SKU at a specific warehouse. Fails if a record already exists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse to create the record in.",
                        },
                    },
                    "required": ["sku", "warehouse_id"],
                },
            },
        }


TOOLS = [
    FindProductByName(),
    GetProductDetails(),
    FindWarehouseByName(),
    GetWarehouseDetails(),
    GetAllWarehouses(),
    GetInventoryDetails(),
    FindCarrierByMethodOfTransport(),
    FindCarrierByService(),
    CalculateExpectedArrivalDate(),
    FindSupplierByName(),
    FindInventoryBySku(),
    FindInboundShipmentsByWarehouse(),
    GetSupplierDetails(),
    FindInboundShipmentsBySupplier(),
    FindCheapestCarrierByService(),
    FindOutboundOrderBySO(),
    GetAllOutboundOrders(),
    GetCarrierDetailsByName(),
    CreateInboundShipment(),
    UpdateInventoryInboundQuantity(),
    UpdateInventoryAllocatedQuantity(),
    CreateOutboundOrder(),
    UpdateShipmentNotes(),
    UpdateInventoryStatus(),
    PerformInventoryAdjustment(),
    UpdateOutboundOrderDetails(),
    CreateInventoryRecord(),
]