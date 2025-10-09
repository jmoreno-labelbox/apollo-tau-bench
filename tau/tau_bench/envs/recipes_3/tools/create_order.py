from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        store_id: int,
        household_id: int,
        list_id: int,
        status_enum: str,
        subtotal_cents: int,
        total_cents: int,
        slot_start_ts: str,
        slot_end_ts: str
    ) -> str:
        orders = _get_table(data, "orders")
        next_id = _max_int(orders, "order_id", 0) + 1
        rec = {
            "order_id": next_id,
            "household_id": household_id,
            "store_id": store_id,
            "list_id": list_id,
            "status_enum": status_enum,
            "subtotal_cents": subtotal_cents,
            "total_cents": total_cents,
            "placed_ts": slot_start_ts,
            "scheduled_slot_start_ts": slot_start_ts,
            "scheduled_slot_end_ts": slot_end_ts,
        }
        data["orders"][order_id] = rec
        payload = {"order_id": next_id}
        out = json.dumps(payload, indent=2)
        return out
        pass
        orders = _get_table(data, "orders")
        next_id = _max_int(orders, "order_id", 0) + 1
        rec = {
            "order_id": next_id,
            "household_id": household_id,
            "store_id": store_id,
            "list_id": list_id,
            "status_enum": status_enum,
            "subtotal_cents": subtotal_cents,
            "total_cents": total_cents,
            "placed_ts": slot_start_ts,
            "scheduled_slot_start_ts": slot_start_ts,
            "scheduled_slot_end_ts": slot_end_ts,
        }
        data["orders"][order_id] = rec
        payload = {"order_id": next_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOrder",
                "description": "Creates an order deterministically with next order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "integer"},
                        "household_id": {"type": "integer"},
                        "list_id": {"type": "integer"},
                        "status_enum": {"type": "string"},
                        "subtotal_cents": {"type": "integer"},
                        "total_cents": {"type": "integer"},
                        "slot_start_ts": {"type": "string"},
                        "slot_end_ts": {"type": "string"},
                    },
                    "required": [
                        "store_id",
                        "household_id",
                        "list_id",
                        "status_enum",
                        "subtotal_cents",
                        "total_cents",
                        "slot_start_ts",
                        "slot_end_ts",
                    ],
                },
            },
        }
