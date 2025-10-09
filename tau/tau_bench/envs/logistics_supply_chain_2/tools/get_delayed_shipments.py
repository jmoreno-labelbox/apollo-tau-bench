from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetDelayedShipments(Tool):
    """Utility for obtaining shipments where the expected arrival date has passed but the actual arrival date is not recorded."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_ids: list = None, today: str = None) -> str:
        from datetime import datetime

        shipments = data.get("inbound_shipments", [])
        today_date = datetime.strptime(today, "%Y-%m-%d").date()
        delayed = []
        for s in shipments:
            expected_arrival = s.get("expected_arrival_date")
            actual_arrival = s.get("actual_arrival_date")
            if expected_arrival and actual_arrival is None:
                try:
                    expected_date = datetime.strptime(
                        expected_arrival, "%Y-%m-%d"
                    ).date()
                    if expected_date < today_date:
                        delayed.append(s["shipment_id"])
                except Exception:
                    pass
        if list_of_ids:
            delayed = [d for d in delayed if d in list_of_ids]
        payload = delayed
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDelayedShipments",
                "description": "Retrieve shipments past expected arrival date but not yet arrived.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "today": {"type": "string", "description": "Reference date"},
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of shipments to choose from.",
                        },
                    },
                    "required": ["today"],
                },
            },
        }
