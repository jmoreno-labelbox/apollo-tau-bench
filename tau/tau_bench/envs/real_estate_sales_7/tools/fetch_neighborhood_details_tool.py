# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _err(msg: str, code: str = "bad_request", ) -> str:
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

def _as_int(x) -> Optional[int]:
    try:
        return int(x)
    except Exception:
        return None

class FetchNeighborhoodDetailsTool(Tool):
    """Gets neighborhood characteristics and bordering areas."""

    @staticmethod
    def invoke(data: Dict[str, Any], name, neighborhood_id) -> str:
        neighborhood_id = _as_int(neighborhood_id)

        if neighborhood_id is None and name is None:
            return _err("Either neighborhood_id (int) or name (string) is required")

        # Prioritize searching by neighborhood_id if it is available.
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
            # Perform a case-insensitive search for name matches using partial input.
            name_lower = name.lower()
            rec = None
            for n in data.get("neighborhoods", []):
                n_name = n.get("name", "").lower()
                # Verify if the search term is present in the neighborhood name or if the neighborhood name is included in the search term.
                # This manages scenarios such as "Heights" aligning with "The Heights."
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
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_neighborhood_details",
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