# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WriteSpatialArtifact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        artifacts = data.setdefault("spatial_artifacts", [])
        artifacts.append({
            "game_pk": kwargs.get("game_pk"),
            "artifact_name": kwargs.get("artifact_name"),
            "qc_status": kwargs.get("qc_status", "passed")
        })
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "write_spatial_artifact",
                "description": "Persists a normalized spatial artifact record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "string"},
                        "artifact_name": {"type": "string"},
                        "qc_status": {"type": "string"}
                    },
                    "required": ["game_pk", "artifact_name"]
                }
            }
        }
