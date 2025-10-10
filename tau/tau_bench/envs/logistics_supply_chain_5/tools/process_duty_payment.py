# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ProcessDutyPayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str, duty_amount: float) -> str:
        inbound_shipments = list(data.get("inbound_shipments", {}).values())

        shipment = next((s for s in inbound_shipments if s.get("shipment_id") == shipment_id), None)
        if not shipment:
            return json.dumps({"error": f"Shipment {shipment_id} not found"})

        # Execute payment transaction
        payment_id = f"PAY-{shipment_id}-{duty_amount:.1f}"

        duty_payment = {
            "payment_id": payment_id,
            "shipment_id": shipment_id,
            "duty_amount": duty_amount,
            "payment_date": get_current_timestamp(),
            "payment_status": "Completed",
            "payment_method": "Electronic"
        }

        # Revise shipment details
        shipment["duty_paid"] = True
        shipment["duty_amount"] = duty_amount

        if "duty_payments" not in data:
            data["duty_payments"] = []
        data["duty_payments"].append(duty_payment)

        return json.dumps({
            "payment_id": payment_id,
            "duty_amount": duty_amount,
            "payment_status": "Completed"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_duty_payment",
                "description": "Process customs duty payment for a shipment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "Shipment identifier"},
                        "duty_amount": {"type": "number", "description": "Duty amount to pay"}
                    },
                    "required": ["shipment_id", "duty_amount"]
                }
            }
        }
