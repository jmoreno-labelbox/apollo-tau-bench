from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CheckTemperatureLogs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str = None, required_temp_range: str = None, excursions_flag: bool = False,
    required_range: Any = None,
    ) -> str:
        shipments = data.get("inbound_shipments", {}).values()
        shipment = next((s for s in shipments.values() if s.get("shipment_id") == shipment_id), None)

        excursions_detected = False
        temperature_compliance = "compliant"

        if required_temp_range:
            temp_range = required_temp_range.split("-")
            if '-' in required_temp_range and 'below' in required_temp_range:
                min_temp = float(-30.0)
                max_temp = float(temp_range[1].replace('C', '').strip())
            elif 'to' in required_temp_range:
                to_range = required_temp_range.replace('C', '').split('to')
                # Manage negative values within the temperature range
                min_temp = float(to_range[0].strip())
                max_temp = float(to_range[1].strip())
            elif 'Cool, Dry' in required_temp_range:
                min_temp = float(15)
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
                "name": "CheckTemperatureLogs",
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
