# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSpatialArtifact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], artifact_name, game_pk) -> str:
        artifacts = data.get("spatial_artifacts", [])
        rec = next((a for a in artifacts if str(a.get("game_pk")) == str(game_pk) and a.get("artifact_name") == artifact_name), None)
        return json.dumps(rec or {}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_spatial_artifact",
                "description": "Reads a persisted spatial artifact by game and name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "string"},
                        "artifact_name": {"type": "string"}
                    },
                    "required": ["game_pk", "artifact_name"]
                }
            }
        }
