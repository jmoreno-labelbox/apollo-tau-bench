# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDelayedShipments(Tool):
    """Tool to retrieve shipments whose expected arrival date is past but actual arrival date is missing."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        from datetime import datetime
        shipments = list(data.get("inbound_shipments", {}).values())
        list_of_shipments = kwargs.get("list_of_ids", None)
        today = datetime.strptime(kwargs.get('today'), "%Y-%m-%d").date()
        delayed = []
        for s in shipments:
            expected_arrival = s.get("expected_arrival_date")
            actual_arrival = s.get("actual_arrival_date")
            if expected_arrival and actual_arrival is None:
                try:
                    expected_date = datetime.strptime(expected_arrival, "%Y-%m-%d").date()
                    if expected_date < today:
                        delayed.append(s['shipment_id'])
                except Exception:
                    pass
        if list_of_shipments:
            delayed = [d for d in delayed if d in list_of_shipments]
        return json.dumps(delayed, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_delayed_shipments",
                "description": "Retrieve shipments past expected arrival date but not yet arrived.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "today": {"type": "string", "description": "Reference date"},
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of shipments to choose from."
                        }
                    },
                    "required": ["today"]
                }
            }
        }
