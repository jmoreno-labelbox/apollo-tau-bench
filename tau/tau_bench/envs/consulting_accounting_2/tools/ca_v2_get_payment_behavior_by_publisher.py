from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CaV2GetPaymentBehaviorByPublisher(Tool):
    """Retrieve payment behavior information for a specific publisher."""

    @staticmethod
    def invoke(data: dict[str, Any], publisher_id: str = None) -> str:
        if not publisher_id:
            return _error("publisher_id is required.")

        payment_behaviors = data.get("payment_behavior", {}).values()
        behavior = _find_one(list(payment_behaviors.values()), "publisher_id", publisher_id)
        return (
            json.dumps(behavior)
            if behavior
            else _error(f"Payment behavior for publisher '{publisher_id}' not found.")
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetPaymentBehaviorByPublisher",
                "description": "Get payment behavior patterns for a specific publisher.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_id": {"type": "string"}},
                    "required": ["publisher_id"],
                },
            },
        }
