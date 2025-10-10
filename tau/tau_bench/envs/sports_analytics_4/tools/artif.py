# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Artif(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")
        artifact_name = kwargs.get("artifact_name")
        artifacts = data.get("spatial_artifacts", [])
        rec = next((a for a in artifacts if str(a.get("game_pk")) == str(game_pk) and a.get("artifact_name") == artifact_name), None)
        # return result
        return json.dumps(rec or {}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {
            "type": "function",
            "function": {
                "name": "findArt",
                "description": "Retrieves record for a persisted spatial artifact by game and name.",
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
