from tau_bench.envs.tool import Tool
import json
from typing import Any

class SimilarIncidentLookupV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], signature: str, top_k: int = 5) -> str:
        pass
        crashes = _get_table(data, "crash_events")
        neighbors = [
            c
            for c in crashes
            if c.get("crash_fingerprint") == signature
            or c.get("fingerprint") == signature
        ][:top_k]
        payload = {"neighbors": neighbors}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SimilarIncidentLookupV2",
                "description": "Returns incidents matching the exact signature/fingerprint (deterministic).",
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
