# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class QuarantineInventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], lot_number, reason, warehouse_id) -> str:

        quarantine_id = f"QTN-{lot_number}-{warehouse_id}"

        return json.dumps({
            "quarantine_id": quarantine_id,
            "lot_number": lot_number,
            "warehouse_id": warehouse_id,
            "reason": reason,
            "status": "Quarantined",
            "quarantine_date": get_current_timestamp()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "quarantine_inventory",
                "description": "Quarantine inventory items by lot number",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lot_number": {"type": "string", "description": "Lot number to quarantine"},
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"},
                        "reason": {"type": "string", "description": "Reason for quarantine"}
                    },
                    "required": ["lot_number", "warehouse_id", "reason"]
                }
            }
        }
