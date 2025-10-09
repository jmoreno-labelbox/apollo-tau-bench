from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CaV2FindPublisherByName(Tool):
    """Locate publisher using name."""

    @staticmethod
    def invoke(data: dict[str, Any], publisher_name: str = None) -> str:
        if not publisher_name:
            return _error("publisher_name is required.")
        publishers = data.get("publishers", [])
        publisher = _find_one(publishers, "name", publisher_name)
        return (
            json.dumps(publisher)
            if publisher
            else _error(f"Publisher '{publisher_name}' not found.")
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2FindPublisherByName",
                "description": "Find a publisher by their name.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_name": {"type": "string"}},
                    "required": ["publisher_name"],
                },
            },
        }
