from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FetchNeighborhoodDetailsTool(Tool):
    """Retrieves characteristics of the neighborhood and adjacent areas."""

    @staticmethod
    def invoke(data: dict[str, Any], neighborhood_id: int = None, name: str = None) -> str:
        if neighborhood_id is None and name is None:
            return _err("Either neighborhood_id (int) WA name (string) is required")

        # Prioritize searching by neighborhood_id if available
        if neighborhood_id is not None:
            rec = next(
                (
                    n
                    for n in data.get("neighborhoods", [])
                    if _as_int(n.get("neighborhood_id")) == neighborhood_id
                ),
                None,
            )
        else:
            # Conduct a case-insensitive partial name search
            name_lower = name.lower()
            rec = None
            for n in data.get("neighborhoods", []):
                n_name = n.get("name", "").lower()
                # Verify if the search name exists within the neighborhood name or the other way around
                # This accommodates scenarios such as "Heights" corresponding to "The Hills"
                if name_lower in n_name or n_name in name_lower:
                    rec = n
                    break

        if not rec:
            search_term = (
                f"neighborhood_id {neighborhood_id}"
                if neighborhood_id is not None
                else f"name '{name}'"
            )
            return _err(f"{search_term} not found", code="not_found")

        out = {
            "neighborhood_id": rec.get("neighborhood_id"),
            "name": rec.get("name"),
            "city": rec.get("city"),
            "region": rec.get("region"),
            "walk_score": rec.get("walk_score"),
            "transit_score": rec.get("transit_score"),
            "bordering_ids_json": rec.get("bordering_ids_json") or [],
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchNeighborhoodDetails",
                "description": "Gets neighborhood characteristics and bordering areas.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "neighborhood_id": {"type": "integer"},
                        "name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
