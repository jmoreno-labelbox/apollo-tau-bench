from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListListingsByIds(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], listing_ids: list = None) -> str:
        ids = set(listing_ids or [])
        props = _index_by(list(data.get("properties", {}).values()), "property_id")
        out = []
        for lst in data.get("listings", {}).values() or []:
            if ids and lst.get("listing_id") not in ids:
                continue
            pr = props.get(lst.get("property_id")) or {}
            out.append({"listing": lst, "property": pr})
        payload = {"items": out}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListListingsByIds",
                "description": "Return listing + property for listing_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "listing_ids": {"type": "array", "items": {"type": "integer"}}
                    },
                    "required": ["listing_ids"],
                },
            },
        }
