# Copyright Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOutboundOrder(Tool):
    """Creates a new outbound order record."""

    @staticmethod
    def invoke(data: Dict[str, Any], carrier_name, customer_address, customer_city, customer_country, customer_id, customer_name, destination_address, destination_city, destination_country, expected_delivery_date, mode_of_transport, notes, number_of_packages, order_date, promised_ship_date, sales_order_number, shipping_cost, shipping_service_level, total_value, total_volume_cbm, warehouse_id, carrier_scac = None, fragile = True, hazmat = False, hazmat_class = None, number_of_line_items = 1, packaging_type = "Insulated Box", payment_terms = "Net 30", priority_level = "Medium", temperature_celsius = None, temperature_control_required = False, total_units = 1, total_weight_kg = 1.0, value_currency = "USD") -> str:
        outbound_orders = list(data.get("outbound_orders", {}).values())
        warehouses = list(data.get("warehouses", {}).values())

        # --- Automatically generate a unique identifier ---
        max_order_num = 0
        for order in outbound_orders:
            order_id = order.get("order_id", "ORD-0000")
            order_num_str = order_id.split("-")[-1]
            if order_num_str.isdigit():
                max_order_num = max(max_order_num, int(order_num_str))
        new_order_id = f"ORD-{max_order_num + 1:04d}"
        warehouse_details = next(
            (wh for wh in warehouses if wh.get("warehouse_id") == warehouse_id), {}
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
