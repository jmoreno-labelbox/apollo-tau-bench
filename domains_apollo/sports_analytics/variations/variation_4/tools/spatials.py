from tau_bench.envs.tool import Tool
import json
from typing import Any

class Spatials(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], game_pk: Any = None, artifact_name: str = None, qc_status: str = "passed") -> str:
        artifacts = data.setdefault("spatial_artifacts", [])
        artifacts.append(
            {
                "game_pk": game_pk,
                "artifact_name": artifact_name,
                "qc_status": qc_status,
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "spatArt",
                "description": "Stores a normalized spatial artifact record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "string"},
                        "artifact_name": {"type": "string"},
                        "qc_status": {"type": "string"},
                    },
                    "required": ["game_pk", "artifact_name"],
                },
            },
        }
