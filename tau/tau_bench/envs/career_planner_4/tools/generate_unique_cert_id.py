# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class generate_unique_cert_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], prefix: str) -> str:
        unique_id = f"{prefix}001"
        return json.dumps({"generated_cert_id": unique_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "generate_unique_cert_id",
                "description": "Generate a unique certification ID",
                "parameters": {
                    "type": "object",
                    "properties": {"prefix": {"type": "string"}},
                    "required": ["prefix"],
                },
            },
        }
