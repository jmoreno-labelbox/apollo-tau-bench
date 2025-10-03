from tau_bench.envs.tool import Tool
import json
from typing import Any

class Pithcmapping(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], source_table: str = None) -> str:
        payload = {"canonical_table": "pitches_canonical"}
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
                "name": "mappings",
                "description": "Transforms raw pitch types to canonical labels.",
                "parameters": {
                    "type": "object",
                    "properties": {"source_table": {"type": "string"}},
                },
                "required": [],
            },
        }
