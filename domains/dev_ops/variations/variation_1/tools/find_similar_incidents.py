from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindSimilarIncidents(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], signature: str, top_k: int = 5) -> str:
        crashes = _get_table(data, "crash_events")
        neighbors = [c for c in crashes if c.get("fingerprint") == signature][:top_k]
        payload = {"neighbors": neighbors}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindSimilarIncidents",
                "description": "Returns prior crash/incidents with identical deterministic fingerprint (simulated semantic match).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "signature": {"type": "string"},
                        "top_k": {"type": "integer"},
                    },
                    "required": ["signature"],
                },
            },
        }
