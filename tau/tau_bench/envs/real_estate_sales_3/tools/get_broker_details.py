from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetBrokerDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], broker_id: str = None) -> str:
        br = next(
            (b for b in data.get("brokers", []) if b.get("broker_id") == broker_id),
            None,
        )
        if not br:
            payload = {"error": f"Broker {broker_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = br
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getBrokerDetails",
                "description": "Fetch a broker profile.",
                "parameters": {
                    "type": "object",
                    "properties": {"broker_id": {"type": "integer"}},
                    "required": ["broker_id"],
                },
            },
        }
