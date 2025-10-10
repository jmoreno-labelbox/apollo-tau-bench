# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class VerifyCustomsDocumentation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str) -> str:
        inbound_shipments = list(data.get("inbound_shipments", {}).values())

        shipment = next((s for s in inbound_shipments if s.get("shipment_id") == shipment_id), None)
        if not shipment:
            return json.dumps({"error": f"Shipment {shipment_id} not found"})

        documentation_complete = True
        missing_docs = []

        # Verify necessary documentation
        if not shipment.get("bill_of_lading"):
            documentation_complete = False
            missing_docs.append("bill_of_lading")

        if shipment.get("origin_country") != shipment.get("destination_country"):
            if not shipment.get("customs_entry_number"):
                documentation_complete = False
                missing_docs.append("customs_entry_number")

        return json.dumps({
            "shipment_id": shipment_id,
            "documentation_complete": documentation_complete,
            "missing_documents": missing_docs,
            "customs_status": shipment.get("customs_clearance_status"),
            "duty_paid": shipment.get("duty_paid", False)
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_customs_documentation",
                "description": "Verify completeness of customs documentation for a shipment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "Shipment identifier"}
                    },
                    "required": ["shipment_id"]
                }
            }
        }
