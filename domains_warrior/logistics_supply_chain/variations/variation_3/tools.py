from domains.dto import Tool
import json
from typing import Dict, Any
from datetime import datetime, timedelta

# --- READ-ONLY TOOLS ---


class FindProductByName(Tool):
    """Finds a product's SKU and other details by its name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_name = kwargs.get("product_name")
        products = data.get("product_master", [])
        for product in products:
            if product.get("product_name") == product_name:
                return json.dumps(
                    {
                        "sku": product.get("sku"),
                        "unit_price": product.get("unit_price"),
                        "weight_kg": product.get("weight_kg"),
                        "hazmat_information": product.get("hazmat_information"),
                        "country_of_origin": product.get("country_of_origin"),
                    }
                )
        return json.dumps({"error": "Product not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_product_by_name",
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
    """Finds a product's details by its sku."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        products = data.get("product_master", [])
        for product in products:
            if product.get("sku") == sku:
                return json.dumps(product)
        return json.dumps({"error": "Product not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_details",
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
    """Finds a warehouse's ID by its name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        warehouse_name = kwargs.get("warehouse_name")
        warehouses = data.get("warehouses", [])
        for warehouse in warehouses:
            if warehouse.get("warehouse_name") == warehouse_name:
                return json.dumps({"warehouse_id": warehouse.get("warehouse_id")})
        return json.dumps({"error": "Warehouse not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_warehouse_by_name",
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
    """Retrieves the full details for a warehouse by its ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        warehouse_id = kwargs.get("warehouse_id")
        warehouses = data.get("warehouses", [])
        for warehouse in warehouses:
            if warehouse.get("warehouse_id") == warehouse_id:
                return json.dumps(warehouse)
        return json.dumps({"error": "Warehouse not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_warehouse_details",
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
    """Retrieves all warehouse records from the dataset, with an option to filter."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        warehouses = data.get("warehouses", [])
        filters = kwargs.get("filters")

        if not warehouses:
            return json.dumps({"message": "No warehouses found."})

        if not filters:
            return json.dumps(warehouses)

        filtered_warehouses = []
        for warehouse in warehouses:
            match = True
            for key, value in filters.items():
                warehouse_value = warehouse.get(key)

                # If the warehouse field is a list (e.g., certifications, special_capabilities)
                # This checks if the required value is present in the list.
                if isinstance(warehouse_value, list):
                    if value not in warehouse_value:
                        match = False
                        break
                # Handle case-insensitivity for string comparisons
                elif isinstance(warehouse_value, str) and isinstance(value, str):
                    if warehouse_value.lower() != value.lower():
                        match = False
                        break
                # Direct comparison for other types
                elif warehouse_value != value:
                    match = False
                    break
            if match:
                filtered_warehouses.append(warehouse)

        if filtered_warehouses:
            return json.dumps(filtered_warehouses)
        else:
            return json.dumps(
                {"message": "No warehouses found matching the specified filters."}
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_warehouses",
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
    """Retrieves key inventory details for a specific product at a specific warehouse."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        warehouse_id = kwargs.get("warehouse_id")
        inventory_items = data.get("inventory", [])
        for item in inventory_items:
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                return json.dumps(
                    {
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
                )
        return json.dumps({"error": "Inventory record not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_details",
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
    """Finds the best-rated, active carrier for a specific transport method."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carriers = data.get("carriers", [])
        method_of_transport = kwargs.get("method_of_transport")
        if not method_of_transport:
            return json.dumps({"error": "Method of transport is required"})
        best_carrier = None
        max_rating = -1.0  # Initialize with a value lower than any possible rating

        for carrier in carriers:
            is_active = carrier.get("active_status", False)
            # Ensure supported_modes is a list and handle case-insensitivity
            supported_modes = [
                mode.lower() for mode in carrier.get("supported_modes", [])
            ]

            if is_active and method_of_transport.lower() in supported_modes:
                current_rating = carrier.get("performance_metrics", {}).get(
                    "average_rating", 0.0
                )
                if current_rating > max_rating:
                    max_rating = current_rating
                    best_carrier = carrier

        if best_carrier:
            return json.dumps(
                {
                    "carrier_id": best_carrier.get("carrier_id"),
                    "carrier_name": best_carrier.get("carrier_name"),
                    "carrier_scac": best_carrier.get("scac"),
                }
            )
        else:
            return json.dumps(
                {
                    "error": f"No active carrier found for transport method: {method_of_transport}"
                }
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_carrier_by_method_of_transport",
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
    """Finds the best-rated, active carrier for a specific transport mode AND service level."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carriers = data.get("carriers", [])
        mode_of_transport = kwargs.get("mode_of_transport")
        service_level = kwargs.get("service_level")

        if not mode_of_transport or not service_level:
            return json.dumps(
                {"error": "Mode of transport and service level are required"}
            )

        best_carrier = None
        max_rating = -1.0

        for carrier in carriers:
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
                current_rating = carrier.get("performance_metrics", {}).get(
                    "average_rating", 0.0
                )
                if current_rating > max_rating:
                    max_rating = current_rating
                    best_carrier = carrier

        if best_carrier:
            return json.dumps(
                {
                    "carrier_id": best_carrier.get("carrier_id"),
                    "carrier_name": best_carrier.get("carrier_name"),
                    "carrier_scac": best_carrier.get("scac"),
                }
            )
        else:
            return json.dumps(
                {
                    "error": f"No active carrier found for mode '{mode_of_transport}' and service '{service_level}'"
                }
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_carrier_by_service",
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
    """Calculates an expected arrival date based on a supplier's standard lead time."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        suppliers = data.get("supplier_master", [])
        supplier_id = kwargs.get("supplier_id")
        current_date = kwargs.get("current_date")

        supplier_details = next(
            (s for s in suppliers if s.get("supplier_id") == supplier_id), {}
        )
        if not supplier_details:
            return json.dumps({"error": f"Supplier with ID '{supplier_id}' not found."})

        lead_time = supplier_details.get("standard_lead_time_days")
        if lead_time is None:
            return json.dumps(
                {
                    "error": f"Standard lead time is not available for supplier '{supplier_id}'."
                }
            )

        try:
            start_date = datetime.strptime(current_date, "%Y-%m-%d")  # type: ignore
            delivery_date = start_date + timedelta(days=lead_time)
            formatted_date = delivery_date.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            return json.dumps(
                {
                    "error": "Invalid date format for current_date. Please use YYYY-MM-DD."
                }
            )

        return json.dumps({"expected_arrival_date": formatted_date})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_expected_arrival_date",
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
    """Finds a supplier's ID and lead time by its name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_name = kwargs.get("supplier_name")
        suppliers = data.get("supplier_master", [])
        for supplier in suppliers:
            if supplier.get("supplier_name") == supplier_name:
                return json.dumps(
                    {
                        "supplier_id": supplier.get("supplier_id"),
                        "standard_lead_time_days": supplier.get(
                            "standard_lead_time_days"
                        ),
                    }
                )
        return json.dumps({"error": "Supplier not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_supplier_by_name",
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
    """Finds all inventory records for a given SKU across all warehouses."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        inventory_items = data.get("inventory", [])
        found_records = []
        for item in inventory_items:
            if item.get("sku") == sku:
                found_records.append(
                    {
                        "inventory_id": item.get("inventory_id"),
                        "warehouse_id": item.get("warehouse_id"),
                        "warehouse_name": item.get("warehouse_name"),
                        "quantity_on_hand": item.get("quantity_on_hand"),
                        "quantity_available": item.get("quantity_available"),
                        "quantity_allocated": item.get("quantity_allocated"),
                        "quantity_inbound": item.get("quantity_inbound"),
                        "unit_cost": item.get("unit_cost"),
                        "lot_number": item.get("lot_number"),
                        "expiration_date": item.get("expiration_date"),
                        "unit_dimensions_cm": item.get("unit_dimensions_cm"),
                    }
                )
        if found_records:
            return json.dumps(found_records)
        return json.dumps({"error": "No inventory records found for that SKU"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_inventory_by_sku",
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
    """Finds all inbound shipments destined for a specific warehouse ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        warehouse_id = kwargs.get("warehouse_id")
        inbound_shipments = data.get("inbound_shipments", [])
        found_shipments = []
        for shipment in inbound_shipments:
            # Handle potential key errors for destination_warehouse_id
            dest_id = shipment.get("destination_warehouse_id") or shipment.get(
                "destination_warehouse_id"
            )
            if dest_id == warehouse_id:
                found_shipments.append(shipment)
        if found_shipments:
            return json.dumps(found_shipments)
        return json.dumps({"message": "No inbound shipments found for that warehouse"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_inbound_shipments_by_warehouse",
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
    """Retrieves the full details for a supplier by their id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get("supplier_id")
        suppliers = data.get("supplier_master", [])
        for supplier in suppliers:
            if supplier.get("supplier_id") == supplier_id:
                return json.dumps(supplier)
        return json.dumps({"error": "Supplier not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_supplier_details",
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
    """Finds all inbound shipments from a specific supplier ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get("supplier_id")
        inbound_shipments = data.get("inbound_shipments", [])
        found_shipments = []
        for shipment in inbound_shipments:
            if shipment.get("supplier_id") == supplier_id:
                found_shipments.append(shipment)
        if found_shipments:
            return json.dumps(found_shipments)
        return json.dumps({"message": "No inbound shipments found for that supplier"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_inbound_shipments_by_supplier",
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
    """Finds the cheapest, active carrier for a specific transport mode and service level."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carriers = data.get("carriers", [])
        mode_of_transport = kwargs.get("mode_of_transport")
        service_level = kwargs.get("service_level")

        if not mode_of_transport or not service_level:
            return json.dumps(
                {"error": "Mode of transport and service level are required"}
            )

        cheapest_carrier = None
        # Initialize with a very high cost
        min_cost = float("inf")

        for carrier in carriers:
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
                # This is a mock cost; in a real scenario, this would be a complex calculation or API call
                # For this simulation, we'll use the length of the carrier name as a proxy for cost.
                current_cost = len(carrier.get("carrier_name", ""))
                if current_cost < min_cost:
                    min_cost = current_cost
                    cheapest_carrier = carrier

        if cheapest_carrier:
            return json.dumps(
                {
                    "carrier_id": cheapest_carrier.get("carrier_id"),
                    "carrier_name": cheapest_carrier.get("carrier_name"),
                    "carrier_scac": cheapest_carrier.get("scac"),
                }
            )
        else:
            return json.dumps(
                {
                    "error": f"No active carrier found for mode '{mode_of_transport}' and service '{service_level}'"
                }
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_cheapest_carrier_by_service",
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
    """Finds a single outbound order record by its Sales Order (SO) number."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        so_number = kwargs.get("sales_order_number")
        outbound_orders = data.get("outbound_orders", [])
        for order in outbound_orders:
            if order.get("sales_order_number") == so_number:
                return json.dumps(order)
        return json.dumps(
            {"error": "Outbound order not found for that Sales Order number"}
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_outbound_order_by_so",
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
    """Retrieves all outbound order records from the dataset, with an option to filter."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        outbound_orders = data.get("outbound_orders", [])
        filters = kwargs.get("filters")

        if not outbound_orders:
            return json.dumps({"message": "No outbound orders found."})

        if not filters:
            return json.dumps(outbound_orders)

        filtered_orders = []
        for order in outbound_orders:
            match = True
            for key, value in filters.items():
                order_value = order.get(key)
                # Handle case-insensitivity for string comparisons
                if isinstance(order_value, str) and isinstance(value, str):
                    if order_value.lower() != value.lower():
                        match = False
                        break
                # Handle boolean comparison where value might be a string 'true'/'false'
                elif isinstance(order_value, bool) and isinstance(value, str):
                    if str(order_value).lower() != value.lower():
                        match = False
                        break
                elif order_value != value:
                    match = False
                    break
            if match:
                filtered_orders.append(order)

        if filtered_orders:
            return json.dumps(filtered_orders)
        else:
            return json.dumps(
                {"message": "No outbound orders found matching the specified filters."}
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_outbound_orders",
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
    """Retrieves the full details for a carrier by its name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carrier_name = kwargs.get("carrier_name")
        carriers = data.get("carriers", [])
        for carrier in carriers:
            if carrier.get("carrier_name") == carrier_name:
                return json.dumps(carrier)
        return json.dumps({"error": "Carrier not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_carrier_details_by_name",
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


# --- WRITE/UPDATE TOOLS ---


class CreateInboundShipment(Tool):
    """Creates a new inbound shipment record, which also serves as a Purchase Order."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # --- Extract required arguments from kwargs ---
        supplier_id = kwargs.get("supplier_id")
        # supplier_name = kwargs.get("supplier_name")
        destination_warehouse_id = kwargs.get("destination_warehouse_id")
        # destination_warehouse_name = kwargs.get("destination_warehouse_name")
        order_quantity = kwargs.get("order_quantity")
        unit_cost = kwargs.get("unit_cost")
        unit_weight = kwargs.get("unit_weight")
        expected_arrival_date = kwargs.get("expected_arrival_date")

        # --- Handle potential missing required arguments ---
        if not all(
            [
                supplier_id,
                # supplier_name,
                destination_warehouse_id,
                # destination_warehouse_name,
                order_quantity,
                unit_cost,
                unit_weight,
                expected_arrival_date,
            ]
        ):
            return json.dumps({"error": "One or more required arguments are missing."})

        inbound_shipments = data.get("inbound_shipments", [])

        # --- Auto-increment unique IDs ---
        max_ship_num = 0
        for shipment in inbound_shipments:
            ship_id = shipment.get("shipment_id", "SHIP-0000")
            ship_num_str = ship_id.split("-")[-1]
            if ship_num_str.isdigit():
                max_ship_num = max(max_ship_num, int(ship_num_str))
        new_shipment_id = f"SHIP-{max_ship_num + 1:04d}"

        max_po_num = 0
        for shipment in inbound_shipments:
            po_num_str = shipment.get("purchase_order_number", "PO-2024-0000").split(
                "-"
            )[-1]
            if po_num_str.isdigit():
                max_po_num = max(max_po_num, int(po_num_str))
        new_po_number = f"PO-2024-{max_po_num + 1:04d}"

        # --- Look up related data for defaults ---
        warehouses = data.get("warehouses", [])
        destination_warehouse_details = next(
            (
                wh
                for wh in warehouses
                if wh.get("warehouse_id") == destination_warehouse_id
            ),
            {},
        )

        suppliers = data.get("supplier_master", [])
        supplier_details = next(
            (sup for sup in suppliers if sup.get("supplier_id") == supplier_id), {}
        )
        supplier_contact_info = supplier_details.get("contact_information", {})
        supplier_address = supplier_contact_info.get("address", {})

        # --- Construct the full shipment record with defaults ---
        new_shipment = {
            "shipment_id": new_shipment_id,
            "purchase_order_number": new_po_number,
            "supplier_id": supplier_id,
            "supplier_name": supplier_details.get("supplier_name"),
            "origin_address": kwargs.get(
                "origin_address", supplier_address.get("street")
            ),
            "origin_city": kwargs.get("origin_city", supplier_address.get("city")),
            "origin_country": kwargs.get(
                "origin_country", supplier_address.get("country")
            ),
            "destination_warehouse_id": destination_warehouse_id,
            "destination_warehouse_name": destination_warehouse_details.get(
                "warehouse_name"
            ),
            "destination_address": kwargs.get(
                "destination_address", destination_warehouse_details.get("address")
            ),
            "destination_city": kwargs.get(
                "destination_city", destination_warehouse_details.get("city")
            ),
            "destination_country": kwargs.get(
                "destination_country", destination_warehouse_details.get("country")
            ),
            "carrier_name": kwargs.get("carrier_name", None),
            "carrier_scac": kwargs.get("carrier_scac", None),
            "mode_of_transport": kwargs.get("mode_of_transport", "Sea"),
            "incoterms": kwargs.get("incoterms", "FOB"),
            "container_number": kwargs.get("container_number", None),
            "bill_of_lading": kwargs.get("bill_of_lading", None),
            "tracking_number": kwargs.get("tracking_number", None),
            "expected_departure_date": kwargs.get("expected_departure_date", None),
            "expected_arrival_date": expected_arrival_date,
            "actual_departure_date": kwargs.get("actual_departure_date", None),
            "actual_arrival_date": kwargs.get("actual_arrival_date", None),
            "status": "Planned",
            "number_of_packages": kwargs.get(
                "number_of_packages",
                max(1, round(order_quantity / 100)),  # type: ignore
            ),
            "total_weight_kg": round(order_quantity * unit_weight, 2),  # type: ignore
            "total_volume_cbm": kwargs.get("total_volume_cbm", None),
            "unit_of_measure_weight": "kg",
            "unit_of_measure_volume": "cbm",
            "customs_clearance_status": "Scheduled",
            "customs_entry_number": kwargs.get("customs_entry_number", None),
            "duty_paid": kwargs.get("duty_paid", False),
            "temperature_control_required": kwargs.get(
                "temperature_control_required", False
            ),
            "temperature_celsius": kwargs.get("temperature_celsius", None),
            "hazmat": kwargs.get("hazmat", False),
            "hazmat_class": kwargs.get("hazmat_class", None),
            "value_currency": kwargs.get("value_currency", "USD"),
            "total_value": round(order_quantity * unit_cost, 2),  # type: ignore
            "insurance_policy_number": kwargs.get("insurance_policy_number", None),
            "insurance_provider": kwargs.get("insurance_provider", None),
            "priority_level": kwargs.get("priority_level", "Medium"),
            "notes": kwargs.get("notes", None),
        }
        inbound_shipments.append(new_shipment)

        return json.dumps(
            {
                "status": "success",
                "shipment_id": new_shipment_id,
                "purchase_order_number": new_po_number,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_inbound_shipment",
                "description": "Creates a new planned inbound shipment, generating a new PO number. Fills in default values for any non-required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        # --- Required Parameters ---
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier.",
                        },
                        # "supplier_name": {
                        #     "type": "string",
                        #     "description": "The name of the supplier.",
                        # },
                        "destination_warehouse_id": {
                            "type": "string",
                            "description": "The ID of the destination warehouse.",
                        },
                        # "destination_warehouse_name": {
                        #     "type": "string",
                        #     "description": "The name of the destination warehouse.",
                        # },
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
                        # --- Optional Parameters ---
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
                        # "supplier_name",
                        "destination_warehouse_id",
                        # "destination_warehouse_name",
                        "order_quantity",
                        "unit_price",
                        "unit_weight",
                        "expected_arrival_date",
                    ],
                },
            },
        }


class UpdateInventoryInboundQuantity(Tool):
    """Updates the inbound quantity for a specific product in a warehouse."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_items = data.get("inventory", [])
        sku = kwargs.get("sku")
        warehouse_id = kwargs.get("warehouse_id")
        quantity_to_add = kwargs.get("quantity_to_add")
        for item in inventory_items:
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                original_inbound = item.get("quantity_inbound", 0)
                item["quantity_inbound"] = original_inbound + quantity_to_add
                return json.dumps(
                    {
                        "status": "success",
                        "inventory_id": item.get("inventory_id"),
                        "new_inbound_quantity": item["quantity_inbound"],
                    }
                )
        return json.dumps({"error": "Inventory record not found to update"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_inbound_quantity",
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
    """Updates the allocated and available quantities for a product in a warehouse upon order creation."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_items = data.get("inventory", [])
        sku = kwargs.get("sku")
        warehouse_id = kwargs.get("warehouse_id")
        quantity_to_allocate = kwargs.get("quantity_to_allocate")

        if not all([sku, warehouse_id, quantity_to_allocate]):
            return json.dumps(
                {"error": "SKU, warehouse ID, and quantity to allocate are required."}
            )

        for item in inventory_items:
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                available = item.get("quantity_available", 0)
                if available < quantity_to_allocate:
                    return json.dumps(
                        {
                            "error": f"Insufficient quantity available. Available: {available}, Required: {quantity_to_allocate}"
                        }
                    )

                original_allocated = item.get("quantity_allocated", 0)
                item["quantity_available"] = available - quantity_to_allocate
                item["quantity_allocated"] = original_allocated + quantity_to_allocate

                return json.dumps(
                    {
                        "status": "success",
                        "inventory_id": item.get("inventory_id"),
                        "new_available_quantity": item["quantity_available"],
                        "new_allocated_quantity": item["quantity_allocated"],
                    }
                )
        return json.dumps({"error": "Inventory record not found to update"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_allocated_quantity",
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
    """Creates a new outbound order record."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        outbound_orders = data.get("outbound_orders", [])
        warehouses = data.get("warehouses", [])

        # --- Auto-increment unique ID ---
        max_order_num = 0
        for order in outbound_orders:
            order_id = order.get("order_id", "ORD-0000")
            order_num_str = order_id.split("-")[-1]
            if order_num_str.isdigit():
                max_order_num = max(max_order_num, int(order_num_str))
        new_order_id = f"ORD-{max_order_num + 1:04d}"

        # --- Look up warehouse details for defaults ---
        warehouse_id = kwargs.get("warehouse_id")
        warehouse_details = next(
            (wh for wh in warehouses if wh.get("warehouse_id") == warehouse_id), {}
        )
        warehouse_name = warehouse_details.get("warehouse_name", "")
        warehouse_address = warehouse_details.get("address", "")
        origin_city = warehouse_details.get("city", "")
        origin_country = warehouse_details.get("country", "")
        carrier_scac = kwargs.get("carrier_scac", None)

        new_order = {
            "order_id": new_order_id,
            "sales_order_number": kwargs.get("sales_order_number"),
            "customer_id": kwargs.get("customer_id"),
            "customer_name": kwargs.get("customer_name"),
            "customer_address": kwargs.get("customer_address"),
            "customer_city": kwargs.get("customer_city"),
            "customer_country": kwargs.get("customer_country"),
            "destination_address": kwargs.get("destination_address"),
            "destination_city": kwargs.get("destination_city"),
            "destination_country": kwargs.get("destination_country"),
            "warehouse_id": warehouse_id,
            "warehouse_name": warehouse_name,
            "warehouse_address": warehouse_address,
            "origin_city": origin_city,
            "origin_country": origin_country,
            "order_date": kwargs.get("order_date"),
            "promised_ship_date": kwargs.get("promised_ship_date"),
            "actual_ship_date": None,
            "expected_delivery_date": kwargs.get("expected_delivery_date"),
            "actual_delivery_date": None,
            "status": "Pending",
            "number_of_line_items": kwargs.get("number_of_line_items", 1),
            "total_units": kwargs.get("total_units", 1),
            "number_of_packages": kwargs.get("number_of_packages"),
            "packaging_type": kwargs.get("packaging_type", "Insulated Box"),
            "total_weight_kg": kwargs.get("total_weight_kg", 1.0),
            "total_volume_cbm": kwargs.get("total_volume_cbm"),
            "unit_of_measure_weight": "kg",
            "unit_of_measure_volume": "cbm",
            "value_currency": kwargs.get("value_currency", "USD"),
            "total_value": kwargs.get("total_value"),
            "carrier_name": kwargs.get("carrier_name"),
            "carrier_scac": carrier_scac,
            "mode_of_transport": kwargs.get("mode_of_transport"),
            "shipping_service_level": kwargs.get("shipping_service_level"),
            "tracking_number": None,
            "shipping_cost": kwargs.get("shipping_cost"),
            "payment_terms": kwargs.get("payment_terms", "Net 30"),
            "temperature_control_required": kwargs.get(
                "temperature_control_required", False
            ),
            "temperature_celsius": kwargs.get("temperature_celsius", None),
            "hazmat": kwargs.get("hazmat", False),
            "hazmat_class": kwargs.get("hazmat_class", None),
            "fragile": kwargs.get("fragile", True),
            "priority_level": kwargs.get("priority_level", "Medium"),
            "return_status": "None",
            "notes": kwargs.get("notes"),
        }
        outbound_orders.append(new_order)

        return json.dumps(
            {
                "status": "success",
                "order_id": new_order_id,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_outbound_order",
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
    """Updates the notes for a specific inbound shipment."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        shipment_id = kwargs.get("shipment_id")
        new_note = kwargs.get("new_note")
        inbound_shipments = data.get("inbound_shipments", [])

        for shipment in inbound_shipments:
            if shipment.get("shipment_id") == shipment_id:
                original_note = shipment.get("notes")
                # Append new note to existing notes if they exist, separated by a pipe
                if original_note:
                    shipment["notes"] = f"{original_note} | {new_note}"
                else:
                    shipment["notes"] = new_note

                return json.dumps(
                    {
                        "status": "success",
                        "shipment_id": shipment_id,
                        "updated_notes": shipment["notes"],
                    }
                )
        return json.dumps({"error": "Shipment ID not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_shipment_notes",
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
    """Updates the stock status for a specific inventory ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_id = kwargs.get("inventory_id")
        new_status = kwargs.get("new_status")
        inventory_items = data.get("inventory", [])

        if not inventory_id or not new_status:
            return json.dumps({"error": "Inventory ID and new status are required."})

        for item in inventory_items:
            if item.get("inventory_id") == inventory_id:
                item["stock_status"] = new_status
                # When quarantining, make quantity unavailable
                if new_status.lower() == "quarantined":
                    item["quantity_available"] = 0
                return json.dumps(
                    {
                        "status": "success",
                        "inventory_id": inventory_id,
                        "new_stock_status": item["stock_status"],
                    }
                )
        return json.dumps({"error": "Inventory ID not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_status",
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
    Performs a full inventory adjustment for a product at a specific warehouse.
    It updates quantity on hand, available quantity, last counted date, and adds an audit note.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_items = data.get("inventory", [])
        sku = kwargs.get("sku")
        warehouse_id = kwargs.get("warehouse_id")
        new_physical_count = kwargs.get("new_physical_count")
        current_date = kwargs.get("current_date")
        reason_note = kwargs.get("reason_note", "")

        if not all(
            [
                sku,
                warehouse_id,
                new_physical_count is not None,
                current_date,
            ]
        ):
            return json.dumps({"error": "One or more required arguments are missing."})

        for item in inventory_items:
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                original_on_hand = item.get("quantity_on_hand", 0)
                discrepancy = new_physical_count - original_on_hand

                # Update core quantities
                item["quantity_on_hand"] = new_physical_count
                item["quantity_available"] = max(
                    0, new_physical_count - item.get("quantity_allocated", 0)
                )
                item["last_counted_date"] = current_date

                # Append a detailed note for audit trail
                if reason_note:
                    adjustment_log = f"Adjustment on {current_date}: Count changed from {original_on_hand} to {new_physical_count} (Discrepancy: {discrepancy}). Reason: {reason_note}."
                    if item.get("notes"):
                        item["notes"] = f"{item['notes']} | {adjustment_log}"
                    else:
                        item["notes"] = adjustment_log

                return json.dumps(
                    {
                        "status": "success",
                        "inventory_id": item.get("inventory_id"),
                        "new_on_hand_quantity": item["quantity_on_hand"],
                        "new_available_quantity": item["quantity_available"],
                    }
                )
        return json.dumps({"error": "Inventory record not found to adjust"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "perform_inventory_adjustment",
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
    """Updates one or more fields for a specific outbound order."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        if not order_id:
            return json.dumps({"error": "order_id is a required argument."})

        outbound_orders = data.get("outbound_orders", [])
        order_to_update = next(
            (o for o in outbound_orders if o.get("order_id") == order_id), None
        )

        if not order_to_update:
            return json.dumps({"error": f"Order with ID '{order_id}' not found."})

        updated_fields = []

        # Iterate over possible fields to update
        for key, value in kwargs.items():
            if key == "order_id":
                continue

            if key == "notes":
                # Append new note to existing notes
                original_note = order_to_update.get("notes", "")
                if original_note:
                    order_to_update["notes"] = f"{original_note} | {value}"
                else:
                    order_to_update["notes"] = value
                updated_fields.append(key)
            elif key in order_to_update:
                order_to_update[key] = value
                updated_fields.append(key)

        if not updated_fields:
            return json.dumps({"message": "No valid fields provided to update."})

        return json.dumps(
            {
                "status": "success",
                "order_id": order_id,
                "updated_fields": updated_fields,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_outbound_order_details",
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
    """Creates a new, empty inventory record for a product in a specific warehouse."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        warehouse_id = kwargs.get("warehouse_id")

        if not sku or not warehouse_id:
            return json.dumps({"error": "SKU and warehouse_id are required."})

        # Check if the record already exists
        inventory_items = data.get("inventory", [])
        for item in inventory_items:
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                return json.dumps(
                    {
                        "error": f"Inventory record for SKU {sku} at warehouse {warehouse_id} already exists."
                    }
                )

        # Get product and warehouse details to populate the new record
        product_details = {}
        products = data.get("product_master", [])
        for p in products:
            if p.get("sku") == sku:
                product_details = p
                break

        warehouse_details = {}
        warehouses = data.get("warehouses", [])
        warehouse_details = next(
            (wh for wh in warehouses if wh.get("warehouse_id") == warehouse_id), {}
        )

        if not product_details or not warehouse_details:
            return json.dumps(
                {
                    "error": "Could not find product or warehouse details to create the record."
                }
            )

        # Auto-increment inventory ID
        max_inv_num = 0
        for item in inventory_items:
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
            "unit_cost": product_details.get(
                "unit_price"
            ),  # Using unit_price as a proxy for cost
            "total_value": 0.00,
            "currency": product_details.get("currency"),
            "unit_weight_kg": product_details.get("weight_kg"),
            "unit_dimensions_cm": product_details.get("dimensions_cm"),
            "lot_number": None,
            "expiration_date": None,
            "received_date": None,
            "last_counted_date": None,
            "reorder_point": 0,  # Default reorder point
            "stock_status": "Out of Stock",
            "storage_requirements": product_details.get("storage_requirements"),
        }

        inventory_items.append(new_record)

        return json.dumps(
            {
                "status": "success",
                "inventory_id": new_inventory_id,
                "message": "New inventory record created.",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_inventory_record",
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
