# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchBrokerProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        broker_id = kwargs.get("broker_id")
        br = next((b for b in data.get("brokers", []) if b.get("broker_id") == broker_id), None)
        if not br:
            return json.dumps({"error": f"Broker {broker_id} not found"}, indent=2)
        return json.dumps(br, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_broker_profile",
                "description": "Fetch a broker profile.",
                "parameters": {
                    "type": "object",
                    "properties": {"broker_id": {"type": "integer"}},
                    "required": ["broker_id"],
                },
            },
        }
