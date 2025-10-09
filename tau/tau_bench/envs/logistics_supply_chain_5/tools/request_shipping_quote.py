from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RequestShippingQuote(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], carrier_scac: str = None, weight_kg: float = None, destination: str = None) -> str:
        carriers = data.get("carriers", [])

        carrier = next((c for c in carriers if c.get("scac") == carrier_scac), None)
        if not carrier:
            return json.dumps({"error": f"Carrier {carrier_scac} not found"})

        # Basic rate calculation
        base_rate_per_kg = {
            "NSTS": 2.50,  # Maritime shipping
            "DLOG": 1.80,  # Rail and truck transport
            "SWDL": 4.50,  # Expedited shipping
            "GPLS": 3.20,  # Land and air transport
            "NRMC": 2.30   # Maritime freight
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
                "name": "RequestShippingQuote",
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
