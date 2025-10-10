# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogTransfer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], from_store, quantity, sku, to_store) -> str:
        entry = {
            "from_store": from_store,
            "to_store": to_store,
            "sku": sku,
            "quantity": quantity
        }
        data.setdefault("transfer_logs", []).append(entry)
        return json.dumps({"message": "Transfer logged.", "entry": entry}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "log_transfer",
                "description": "Tool function: log_transfer",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
