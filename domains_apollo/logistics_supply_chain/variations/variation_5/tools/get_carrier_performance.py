from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict

class GetCarrierPerformance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], carrier_scac: str = None, route: str = None) -> str:
        carriers = data.get("carriers", [])

        carrier = next((c for c in carriers if c.get("scac") == carrier_scac), None)
        if not carrier:
            return json.dumps({"error": f"Carrier {carrier_scac} not found"})

        performance_data = {
            "carrier_scac": carrier_scac,
            "carrier_name": carrier.get("carrier_name"),
            "performance_metrics": carrier.get("performance_metrics", {}),
            "supported_modes": carrier.get("supported_modes", []),
            "service_levels": carrier.get("service_levels", []),
            "regional_coverage": carrier.get("regional_coverage"),
            "active_status": carrier.get("active_status", False),
            "route_specific_data": f"Performance data for {route}" if route else None
        }

        return json.dumps(performance_data)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCarrierPerformance",
                "description": "Retrieve carrier performance metrics and capabilities",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_scac": {"type": "string", "description": "Carrier SCAC code"},
                        "route": {"type": "string", "description": "Specific route or region"}
                    },
                    "required": ["carrier_scac"]
                }
            }
        }
