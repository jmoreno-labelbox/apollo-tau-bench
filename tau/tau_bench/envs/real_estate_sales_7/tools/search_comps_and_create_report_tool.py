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

class SearchCompsAndCreateReportTool(Tool):
    """Performs a neighborhood-first search, ranks candidates, and generates the comp report entry in one step."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        subject_property_id: str,
        client_id: int,
        created_by_broker_id: int,
        client_neighborhoods: list[int] = None,
        max_selections: int = 3,
        price_tolerance_pct: float = 0.10
    ) -> str:
        #--- Parameters sourced from both tools ---
        client_id = _as_int(client_id)
        created_by_broker_id = _as_int(created_by_broker_id)

        # Verification for mandatory parameters
        if client_id is None or not subject_property_id or created_by_broker_id is None:
            return _err(
                "client_id, subject_property_id, and created_by_broker_id are required"
            )

        need_prop = _require_property_id(subject_property_id)
        if need_prop:
            return _err(need_prop)

        #--- Logic for Search & Rank (from SearchAndRankCompsTool) ---
        client_neighborhoods = {
            v
            for v in (_as_int(x) for x in (client_neighborhoods or []))
            if v is not None
        }
        max_selections = _as_int(max_selections) or 3
        try:
            price_tolerance_pct = float(price_tolerance_pct or 0.10)
        except Exception:
            price_tolerance_pct = 0.10

        subject_listing = _collect_listing_by_property(data, subject_property_id)
        if not subject_listing:
            return _err(
                f"subject property {subject_property_id} not found", code="not_found"
            )
        subject_price = subject_listing.get("list_price")

        listings_map = {str(l.get("property_id")): l for l in data.get("listings", {}).values()}
        candidate_ids = set(listings_map.keys())

        candidates = []
        for pid in candidate_ids:
            if pid == subject_property_id:
                continue
            l = listings_map.get(pid)
            if not l or l.get("status") not in {
                "active",
                "for_sale",
                "pending",
                "sold",
            }:
                continue

            if subject_price is not None and l.get("list_price") is not None:
                lo = subject_price * (1 - price_tolerance_pct)
                hi = subject_price * (1 + price_tolerance_pct)
                if not (lo <= float(l["list_price"]) <= hi):
                    continue

            score = _similarity_score(subject_price, l.get("list_price"), 0)
            rec = {"property_id": pid, "tier": 0, "similarity_score": score}
            candidates.append(rec)

        candidates.sort(key=lambda r: (-r["similarity_score"], r["property_id"]))
        top_candidates = candidates[:10]

        ranked = []
        for c in top_candidates:
            pid = c["property_id"]
            l = _collect_listing_by_property(data, pid) or {}
            price = l.get("list_price")

            if price is not None and subject_price is not None:
                pdiff = abs(float(price) - float(subject_price)) / max(
                    float(subject_price), 1.0
                )
                price_sc = max(0.0, 1.0 - min(pdiff, 0.60))
            else:
                price_sc = 0.6

            upstream = float(c.get("similarity_score") or 0.6)
            final = round(min(1.0, max(0.0, 0.7 * price_sc + 0.3 * upstream)), 3)

            if final >= 0.85:
                reason = "Strong price fit"
            elif final >= 0.70:
                reason = "Good price fit"
            elif final >= 0.50:
                reason = "Fair price fit"
            else:
                reason = "Weak price fit"

            ranked.append(
                {
                    "property_id": pid,
                    "final_score": final,
                    "selection_reason": reason,
                    "score_breakdown": {"price": round(price_sc, 3)},
                    "tier": c["tier"],
                }
            )

        ranked.sort(key=lambda r: (-r["final_score"], r["property_id"]))
        for i, r in enumerate(ranked, 1):
            r["rank"] = i

        selected = [r["property_id"] for r in ranked[:max_selections]]

        search_and_rank_output = {
            "subject_property_id": subject_property_id,
            "candidates_found": len(candidates),
            "ranked_properties": ranked,
            "selected_comparables": selected,
        }

        #--- Logic for Report Creation (from CreateCompReportEntryTool) ---
        rows = data.setdefault("comp_reports", [])
        report_id = _next_int_id(rows, "report_id")
        report_rec = {
            "report_id": report_id,
            "client_id": client_id,
            "subject_property_id": str(subject_property_id),
            "created_by_broker_id": created_by_broker_id,
            "created_at": HARD_TS,
            "doc_uri": None,
            "status": "draft",
        }
        rows.append(report_rec)
        payload = {
                "report_entry": report_rec,
                "search_results": search_and_rank_output,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchCompsAndCreateReport",
                "description": (
                    "Searches for comparable properties, ranks them, and creates a new comp report entry."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_property_id": {"type": "string"},
                        "client_id": {"type": "integer"},
                        "created_by_broker_id": {"type": "integer"},
                        "client_neighborhoods": {
                            "type": "array",
                            "items": {"type": "integer"},
                        },
                        "client_amenities": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "max_selections": {"type": ["integer", "null"]},
                        "price_tolerance_pct": {"type": ["number", "null"]},
                    },
                    "required": [
                        "subject_property_id",
                        "client_id",
                        "created_by_broker_id",
                        "client_neighborhoods",
                    ],
                },
            },
        }
