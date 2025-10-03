from tau_bench.envs.tool import Tool
import json
from typing import Any

class RunCanonicalPitchMap(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        payload = {"canonical_table": "pitches_canonical"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RunCanonicalPitchMap",
                "description": "Maps raw pitch types to canonical labels.",
                "parameters": {
                    "type": "object",
                    "properties": {"source_table": {"type": "string"}},
                },
                "required": [],
            },
        }
