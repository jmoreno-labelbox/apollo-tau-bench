from tau_bench.envs.tool import Tool
import json
from typing import Any

class WriteSpatialArtifact(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        artifacts = data.setdefault("spatial_artifacts", [])
        artifacts.append(
            {
                "game_pk": kwargs.get("game_pk"),
                "artifact_name": kwargs.get("artifact_name"),
                "qc_status": kwargs.get("qc_status", "passed"),
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteSpatialArtifact",
                "description": "Persists a normalized spatial artifact record.",
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
