# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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

        # Streamlined rate computation
        base_rate_per_kg = {
            "MAEU": 2.50,  # Maritime shipping
            "DBSG": 1.80,  # Railroad/Truck
            "FDEG": 4.50,  # Articulate
            "UPSN": 3.20,  # Terrain/Aerial
            "HLCU": 2.30   # Maritime shipping
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
