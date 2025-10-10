# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOutboundOrder(Tool):
    """Creates a new outbound order record."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        outbound_orders = list(data.get("outbound_orders", {}).values())
        warehouses = list(data.get("warehouses", {}).values())

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
