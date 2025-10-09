from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GenerateUniqueAnalysisId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], prefix: str) -> str:
        unique_id = f"{prefix}001"
        payload = {"generated_analysis_id": unique_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "generateUniqueAnalysisId",
                "description": "Generate a unique analysis ID",
                "parameters": {
                    "type": "object",
                    "properties": {"prefix": {"type": "string"}},
                    "required": ["prefix"],
                },
            },
        }
