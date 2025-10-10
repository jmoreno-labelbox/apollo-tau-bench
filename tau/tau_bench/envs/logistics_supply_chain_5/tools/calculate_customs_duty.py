# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateCustomsDuty(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], country_of_origin, shipment_id, total_value) -> str:

        # Streamlined duty assessment - actual implementation would involve tariff schedules.
        duty_rates = {
            "China": 0.05,  # 5% tax rate
            "Japan": 0.02,  # 2% tariff rate
            "Germany": 0.025, # 2.5% tariff rate
            "Mexico": 0.0,  # USMCA favored tariff rate
            "default": 0.035 # 3.5% base rate
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
