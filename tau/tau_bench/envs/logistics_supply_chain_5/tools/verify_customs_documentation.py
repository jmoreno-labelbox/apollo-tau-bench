from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class VerifyCustomsDocumentation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str, customs_clearance_status: str = None, duty_paid: bool = False) -> str:
        inbound_shipments = data.get("inbound_shipments", [])

        shipment = next((s for s in inbound_shipments if s.get("shipment_id") == shipment_id), None)
        if not shipment:
            return json.dumps({"error": f"Shipment {shipment_id} not found"})

        documentation_complete = True
        missing_docs = []

        # Verify the necessary documentation
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
            "customs_status": customs_clearance_status,
            "duty_paid": duty_paid
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifyCustomsDocumentation",
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
