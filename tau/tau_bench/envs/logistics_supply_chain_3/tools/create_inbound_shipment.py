from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

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

        inbound_shipments = data.get("inbound_shipments", [])

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
        inbound_shipments.append(new_shipment)
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
