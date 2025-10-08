from tau_bench.envs.tool import Tool
import json
from typing import Any

class find_similar_incidents(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], issue_signature: str) -> str:
        pass
        incidents = data.get("incident_history", [])
        hits = [i for i in incidents if i.get("issue_signature") == issue_signature]
        payload = {"count": len(hits), "results": hits}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindSimilarIncidents",
                "description": "Finds past incidents with a similar issue signature.",
                "parameters": {
                    "type": "object",
                    "properties": {"issue_signature": {"type": "string"}},
                    "required": ["issue_signature"],
                },
            },
        }
