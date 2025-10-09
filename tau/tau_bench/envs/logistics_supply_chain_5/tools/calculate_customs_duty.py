from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict

class CalculateCustomsDuty(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str = None, total_value: float = None, country_of_origin: str = None) -> str:
        # Basic duty calculation - a real system would utilize tariff schedules
        duty_rates = {
            "Middle Kingdom": 0.05,  # Duty rate of 5%
            "Nippon": 0.02,  # Duty rate of 2%
            "Deutschland": 0.025,  # Duty rate of 2.5%
            "Mexico": 0.0,  # Preferential rate under USMCA
            "default": 0.035  # Standard rate of 3.5%
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
                "name": "CalculateCustomsDuty",
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
