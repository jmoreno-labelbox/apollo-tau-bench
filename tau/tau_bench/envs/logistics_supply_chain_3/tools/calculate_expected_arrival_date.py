# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateExpectedArrivalDate(Tool):
    """Calculates an expected arrival date based on a supplier's standard lead time."""

    @staticmethod
    def invoke(data: Dict[str, Any], current_date, supplier_id) -> str:
        suppliers = list(data.get("supplier_master", {}).values())

        supplier_details = next(
            (s for s in suppliers if s.get("supplier_id") == supplier_id), {}
        )
        if not supplier_details:
            return json.dumps({"error": f"Supplier with ID '{supplier_id}' not found."})

        lead_time = supplier_details.get("standard_lead_time_days")
        if lead_time is None:
            return json.dumps(
                {
                    "error": f"Standard lead time is not available for supplier '{supplier_id}'."
                }
            )

        try:
            start_date = datetime.strptime(current_date, "%Y-%m-%d")  # type: ignore
            delivery_date = start_date + timedelta(days=lead_time)
            formatted_date = delivery_date.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            return json.dumps(
                {
                    "error": "Invalid date format for current_date. Please use YYYY-MM-DD."
                }
            )

        return json.dumps({"expected_arrival_date": formatted_date})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_expected_arrival_date",
                "description": "Calculates the expected arrival date from a given start date using the specified supplier's standard lead time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier to get the lead time from.",
                        },
                        "current_date": {
                            "type": "string",
                            "description": "The starting date for the calculation, in YYYY-MM-DD format.",
                        },
                    },
                    "required": [
                        "supplier_id",
                        "current_date",
                    ],
                },
            },
        }
