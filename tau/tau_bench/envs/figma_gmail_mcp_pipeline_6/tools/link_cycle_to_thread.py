# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class link_cycle_to_thread(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cycle_id: str, thread_id: str) -> str:
        cycles = data.setdefault("review_cycles", [])
        threads = data.setdefault("gmail_threads", [])
        if not any(isinstance(t, dict) and t.get("thread_id") == thread_id for t in threads):
            return json.dumps({"error": f"thread_id '{thread_id}' not found"}, indent=2)
        cyc = next((c for c in cycles if isinstance(c, dict) and c.get("cycle_id") == cycle_id), None)
        if not cyc:
            return json.dumps({"error": f"cycle_id '{cycle_id}' not found"}, indent=2)
        cyc["thread_id_nullable"] = thread_id
        return json.dumps({"cycle_id": cyc["cycle_id"], "thread_id": thread_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"link_cycle_to_thread",
            "description":"Link an existing Gmail thread to a review cycle (writes thread_id_nullable).",
            "parameters":{"type":"object","properties":{
                "cycle_id":{"type":"string"},
                "thread_id":{"type":"string"}
            },"required":["cycle_id","thread_id"]}
        }}
