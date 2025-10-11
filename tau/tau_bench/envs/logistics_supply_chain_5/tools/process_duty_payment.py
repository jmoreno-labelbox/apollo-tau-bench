# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from datetime import datetime


def get_current_timestamp() -> str:
    return "2025-07-31T12:00:00.000000"

def get_current_timestamp_object() -> datetime:
    return datetime.strptime(get_current_timestamp(), "%Y-%m-%dT%H:%M:%S.%f")

def get_current_year_month_day() -> str:
    return "2025-07-31"

def generate_unique_id() -> str:
    return 'fd520c73'

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
