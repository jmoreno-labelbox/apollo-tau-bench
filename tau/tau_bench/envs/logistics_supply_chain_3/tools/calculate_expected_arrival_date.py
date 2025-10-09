from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CalculateExpectedArrivalDate(Tool):
    """Determines an expected arrival date based on the supplier's typical lead time."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, current_date: str = None) -> str:
        suppliers = data.get("supplier_master", {}).values()

        supplier_details = next(
            (s for s in suppliers.values() if s.get("supplier_id") == supplier_id), {}
        )
        if not supplier_details:
            payload = {"error": f"Supplier with ID '{supplier_id}' not found."}
            out = json.dumps(payload)
            return out

        lead_time = supplier_details.get("standard_lead_time_days")
        if lead_time is None:
            payload = {
                "error": f"Standard lead time is not available for supplier '{supplier_id}'."
            }
            out = json.dumps(payload)
            return out

        try:
            start_date = datetime.strptime(current_date, "%Y-%m-%d")
            delivery_date = start_date + timedelta(days=lead_time)
            formatted_date = delivery_date.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            payload = {
                "error": "Invalid date format for current_date. Please use YYYY-MM-DD."
            }
            out = json.dumps(payload)
            return out
        payload = {"expected_arrival_date": formatted_date}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateExpectedArrivalDate",
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
