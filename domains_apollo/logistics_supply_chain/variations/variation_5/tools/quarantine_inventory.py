from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict

class QuarantineInventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], lot_number: str = None, warehouse_id: str = None, reason: str = None) -> str:
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
                "name": "QuarantineInventory",
                "description": "Quarantine inventory items by EAC number",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lot_number": {"type": "string", "description": "EAC number to quarantine"},
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"},
                        "reason": {"type": "string", "description": "Reason for quarantine"}
                    },
                    "required": ["lot_number", "warehouse_id", "reason"]
                }
            }
        }
