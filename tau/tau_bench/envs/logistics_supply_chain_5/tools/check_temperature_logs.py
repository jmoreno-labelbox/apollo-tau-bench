# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckTemperatureLogs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        shipment_id = kwargs.get("shipment_id")
        shipments = list(data.get("inbound_shipments", {}).values())
        required_temp_range = kwargs.get("required_temp_range")
        shipment = next((s for s in shipments if s.get("shipment_id") == shipment_id), None)
        excursions_flag = kwargs.get("excursions_flag", False)

        excursions_detected = False
        temperature_compliance = "compliant"

        if required_temp_range:
            temp_range = required_temp_range.split("-")
            if '-' in required_temp_range and 'below' in required_temp_range:
                min_temp = float(-30.0)
                max_temp = float(temp_range[1].replace('C', '').strip())
            elif 'to' in required_temp_range:
                to_range = required_temp_range.replace('C', '').split('to')
                # Handle negative values in the temperature range
                min_temp = float(to_range[0].strip())
                max_temp = float(to_range[1].strip())
            elif 'Cool, Dry' in required_temp_range:
                min_temp  = float(15)
                max_temp = float(25)
            else:
                min_temp = float(temp_range[0].replace('C', '').strip())
                max_temp = float(temp_range[1].replace('C', '').strip())

            if shipment['temperature_celsius'] is None:
                excursions_detected = False
                temperature_compliance = "compliant"
            else:
                if shipment['temperature_celsius'] < min_temp or shipment['temperature_celsius'] > max_temp:
                    excursions_detected = True
                    temperature_compliance = "non-compliant"


        else:
            if shipment['temperature_celsius'] is None:
                excursions_detected = False
                temperature_compliance = "compliant"

        if excursions_flag:
                excursions_detected = True
                temperature_compliance = "non-compliant"

        return json.dumps({
            "shipment_id": shipment_id,
            "temperature_compliance": temperature_compliance,
            "required_range": required_temp_range,
            "actual_temperature": shipment['temperature_celsius'],
            "excursions_detected": excursions_detected
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_temperature_logs",
                "description": "Check temperature monitoring logs for a shipment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "Shipment identifier"},
                        "required_temp_range": {"type": "string", "description": "Required temperature range"},
                        "excursions_flag": {"type": "boolean", "description": "Flag to check for temperature excursions"}
                    },
                    "required": ["shipment_id"]
                }
            }
        }
