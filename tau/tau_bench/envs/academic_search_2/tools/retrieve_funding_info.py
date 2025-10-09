from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class RetrieveFundingInfo(Tool):
    """Looks for funding sources using source_name or funding_source_id."""

    @staticmethod
    def invoke(data: dict[str, Any], source_name: Any = None, funding_source_id: Any = None) -> str:
        if not source_name and not funding_source_id:
            payload = data.get("funding_sources", [])
            out = json.dumps(payload, indent=2)
            return out

        funding_sources = data.get("funding_sources", [])
        results = [
            fs
            for fs in funding_sources
            if (
                not source_name
                or source_name.lower() in fs.get("source_name", "").lower()
            )
            and (
                not funding_source_id
                or fs.get("funding_source_id") == funding_source_id
            )
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RetrieveFundingInfo",
                "description": "Searches for funding sources by name or ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_name": {"type": "string"},
                        "funding_source_id": {"type": "string"},
                    },
                },
            },
        }
