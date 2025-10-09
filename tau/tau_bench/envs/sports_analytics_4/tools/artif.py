from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class Artif(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], game_pk: str = None, artifact_name: str = None) -> str:
        artifacts = data.get("spatial_artifacts", {}).values()
        rec = next(
            (
                a
                for a in artifacts.values() if str(a.get("game_pk")) == str(game_pk)
                and a.get("artifact_name") == artifact_name
            ),
            None,
        )
        payload = rec or {}
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
                "name": "findArt",
                "description": "Retrieves record for a persisted spatial artifact by game and name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "string"},
                        "artifact_name": {"type": "string"},
                    },
                    "required": ["game_pk", "artifact_name"],
                },
            },
        }
