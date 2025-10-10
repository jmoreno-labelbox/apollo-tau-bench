# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class VerifyColdChainIntegrity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str, carrier_scac: str) -> str:
        return json.dumps({
            "shipment_id": shipment_id,
            "carrier_scac": carrier_scac,
            "cold_chain_integrity": "maintained",
            "temperature_maintained": True,
            "verification_date": get_current_timestamp()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_cold_chain_integrity",
                "description": "Verify cold chain integrity for temperature-sensitive shipments",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "Shipment identifier"},
                        "carrier_scac": {"type": "string", "description": "Carrier SCAC code"}
                    },
                    "required": ["shipment_id", "carrier_scac"]
                }
            }
        }
