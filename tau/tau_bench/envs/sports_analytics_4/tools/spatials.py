# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Spatials(Tool):
    @staticmethod
        # primary execution method
    def invoke(data: Dict[str, Any], artifact_name, game_pk, qc_status = "passed") -> str:
        artifacts = data.setdefault("spatial_artifacts", [])
        artifacts.append({
            "game_pk": game_pk,
            "artifact_name": artifact_name,
            "qc_status": qc_status
        })
        # return output
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return outcome
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
                        "qc_status": {"type": "string"}
                    },
                    "required": ["game_pk", "artifact_name"]
                }
            }
        }
