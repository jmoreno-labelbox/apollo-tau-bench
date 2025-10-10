# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTransferCompliance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], status, transfer_id) -> str:
        entry = {
            "transfer_id": transfer_id,
            "status": status
        }
        data.setdefault("transfer_compliance", []).append(entry)
        return json.dumps({"message": "Transfer compliance updated.", "entry": entry}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "update_transfer_compliance",
                "description": "Tool function: update_transfer_compliance",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
