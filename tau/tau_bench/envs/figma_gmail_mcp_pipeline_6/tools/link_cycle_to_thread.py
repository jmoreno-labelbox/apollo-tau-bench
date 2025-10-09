from tau_bench.envs.tool import Tool
import json
from typing import Any

class link_cycle_to_thread(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str, thread_id: str) -> str:
        cycles = data.setdefault("review_cycles", [])
        threads = data.setdefault("gmail_threads", [])
        if not any(
            isinstance(t, dict) and t.get("thread_id") == thread_id for t in threads
        ):
            payload = {"error": f"thread_id '{thread_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        cyc = next(
            (
                c
                for c in cycles
                if isinstance(c, dict) and c.get("cycle_id") == cycle_id
            ),
            None,
        )
        if not cyc:
            payload = {"error": f"cycle_id '{cycle_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        cyc["thread_id_nullable"] = thread_id
        payload = {"cycle_id": cyc["cycle_id"], "thread_id": thread_id}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkCycleToThread",
                "description": "Link an existing Gmail thread to a review cycle (writes thread_id_nullable).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "thread_id": {"type": "string"},
                    },
                    "required": ["cycle_id", "thread_id"],
                },
            },
        }
