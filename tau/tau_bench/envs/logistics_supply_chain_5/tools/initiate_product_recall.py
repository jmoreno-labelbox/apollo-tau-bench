# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InitiateProductRecall(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], lot_number: str, recall_type: str) -> str:
        recall_id = f"RCL-{lot_number}-{recall_type}"

        return json.dumps({
            "recall_id": recall_id,
            "lot_number": lot_number,
            "recall_type": recall_type,
            "status": "Initiated",
            "recall_date": get_current_timestamp(),
            "recall_scope": f"all_lot_{lot_number}"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "initiate_product_recall",
                "description": "Initiate product recall for specific lot number",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lot_number": {"type": "string", "description": "Lot number to recall"},
                        "recall_type": {"type": "string", "description": "Type of recall (voluntary/mandatory/precautionary)"}
                    },
                    "required": ["lot_number", "recall_type"]
                }
            }
        }
