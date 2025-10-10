# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Artif(Tool):
    @staticmethod
        # primary execution method
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")
        artifact_name = kwargs.get("artifact_name")
        artifacts = data.get("spatial_artifacts", [])
        rec = next((a for a in artifacts if str(a.get("game_pk")) == str(game_pk) and a.get("artifact_name") == artifact_name), None)
        # return outcome
        return json.dumps(rec or {}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return output
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
