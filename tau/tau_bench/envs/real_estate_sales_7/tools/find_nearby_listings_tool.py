from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindNearbyListingsTool(Tool):
    """Identifies the closest listings to a subject property by extracting map coordinates from URLs."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        subject_property_id: str,
        max_results: int = 3,
        status_filter: list[str] = None
    ) -> str:
        pass
        need = _require_property_id(subject_property_id)
        if need:
            return _err(need)

        try:
            max_results = int(max_results or 3)
        except Exception:
            max_results = 3

        allowed_status = set(
            status_filter
            or ["active", "pending", "for_sale", "sold", "off_market", "rented"]
        )  # default to broad

        def _extract_latlon(url: str | None) -> tuple[float, float] | None:
            pass
            if not url or not isinstance(url, str):
                return None
            # Attempt viewpoint=lat,lon
            m = re.search(r"viewpoint=([\-\d\.]+),([\-\d\.]+)", url)
            if m:
                try:
                    return float(m.group(1)), float(m.group(2))
                except Exception:
                    pass
            # Attempt q=lat,lon
            m = re.search(r"[?&]q=([\-\d\.]+),([\-\d\.]+)", url)
            if m:
                try:
                    return float(m.group(1)), float(m.group(2))
                except Exception:
                    pass
            return None

        def _haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
            pass
            # Radius of the Earth in kilometers
            R = 6371.0
            dlat = math.radians(lat2 - lat1)
            dlon = math.radians(lon2 - lon1)
            a = (
                math.sin(dlat / 2) ** 2
                + math.cos(math.radians(lat1))
                * math.cos(math.radians(lat2))
                * math.sin(dlon / 2) ** 2
            )
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            return R * c

        subj = _collect_listing_by_property(data, subject_property_id)
        if not subj:
            return _err(
                f"subject property {subject_property_id} not found", code="not_found"
            )
        subj_ll = _extract_latlon(subj.get("street_view_url"))
        if not subj_ll:
            return _err("coordinates_unavailable for subject property")

        lat1, lon1 = subj_ll
        candidates = []
        for l in data.get("listings", {}).values():
            pid = str(l.get("property_id"))
            if not pid or pid == subject_property_id:
                continue
            if l.get("status") not in allowed_status:
                continue
            ll = _extract_latlon(l.get("street_view_url"))
            if not ll:
                continue
            lat2, lon2 = ll
            dist = _haversine_km(lat1, lon1, lat2, lon2)
            candidates.append(
                {
                    "property_id": pid,
                    "distance_km": round(dist, 3),
                    "status": l.get("status"),
                }
            )

        candidates.sort(key=lambda x: (x["distance_km"], x["property_id"]))
        top = candidates[:max_results]

        out = {
            "subject_property_id": subject_property_id,
            "nearby_property_ids": [c["property_id"] for c in top],
            "neighbors": top,
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindNearbyListings",
                "description": (
                    "Find nearest property_ids to a subject using parsed map coordinates."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_property_id": {"type": "string"},
                        "max_results": {"type": ["integer", "null"]},
                        "status_filter": {
                            "type": ["array", "null"],
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["subject_property_id"],
                },
            },
        }
