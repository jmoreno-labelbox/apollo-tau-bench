# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateInboundShipment(Tool):
    """Creates a new inbound shipment record, which also serves as a Purchase Order."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # --- Retrieve necessary parameters from kwargs ---
        supplier_id = kwargs.get("supplier_id")
        # supplier_name = kwargs.get("supplier_name")
        destination_warehouse_id = kwargs.get("destination_warehouse_id")
        # destination_warehouse_name = kwargs.get("destination_warehouse_name")
        order_quantity = kwargs.get("order_quantity")
        unit_cost = kwargs.get("unit_cost")
        unit_weight = kwargs.get("unit_weight")
        expected_arrival_date = kwargs.get("expected_arrival_date")

        # --- Manage possible absence of mandatory parameters ---
        if not all(
            [
                supplier_id,
                # vendor_name,
                destination_warehouse_id,
                # target_warehouse_name,
                order_quantity,
                unit_cost,
                unit_weight,
                expected_arrival_date,
            ]
        ):
            return json.dumps({"error": "One or more required arguments are missing."})

        inbound_shipments = list(data.get("inbound_shipments", {}).values())

        # --- Automatically generate unique identifiers ---
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

        # --- Retrieve associated data for defaults ---
        warehouses = list(data.get("warehouses", {}).values())
        destination_warehouse_details = next(
            (
                wh
                for wh in warehouses
                if wh.get("warehouse_id") == destination_warehouse_id
            ),
            {},
        )

        suppliers = list(data.get("supplier_master", {}).values())
        supplier_details = next(
            (sup for sup in suppliers if sup.get("supplier_id") == supplier_id), {}
        )
        supplier_contact_info = supplier_details.get("contact_information", {})
        supplier_address = supplier_contact_info.get("address", {})

        # --- Create the complete shipment record using default values ---
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
                        # --- Necessary Parameters ---
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier.",
                        },
                        # "vendor_identifier": {
                        # "format": "string",
                        # "Supplier's name."
                        # },
                        "destination_warehouse_id": {
                            "type": "string",
                            "description": "The ID of the destination warehouse.",
                        },
                        # "target_warehouse_name": {
                        # "dataType": "string",
                        # "name": "The identifier for the target warehouse.",
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
                        # --- Parameters that are not mandatory ---
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
                        # "vendor_name",
                        "destination_warehouse_id",
                        # "target_warehouse_name",
                        "order_quantity",
                        "unit_price",
                        "unit_weight",
                        "expected_arrival_date",
                    ],
                },
            },
        }
