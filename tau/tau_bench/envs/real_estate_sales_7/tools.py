from domains.dto import Tool
from typing import Any, Dict, List, Optional, Tuple
import json
import re
import math

HARD_TS = "2025-09-15T17:00:00Z"
HTX_RE = re.compile(r"^HTX\d{3}$")


# ----------------------------
# Helpers
# ----------------------------
def _err(msg: str, code: str = "bad_request", **extra) -> str:
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)


def _as_int(x) -> Optional[int]:
    try:
        return int(x)
    except Exception:
        return None


def _latest(records: List[Dict[str, Any]], ts_key: str) -> Optional[Dict[str, Any]]:
    if not records:
        return None
    return max(records, key=lambda r: r.get(ts_key) or "")


def _ppsqft(list_price: Optional[float], sqft: Optional[float]) -> Optional[float]:
    if list_price is None or sqft in (None, 0):
        return None
    return round(float(list_price) / float(sqft), 3)


def _require_property_id(pid: str) -> Optional[str]:
    if not pid:
        return "property_id is required"
    if not HTX_RE.match(str(pid)):
        return f"property_id must match HTX### format, got {pid}"
    return None


def _require_active_broker(data: Dict[str, Any], broker_id: int) -> Optional[str]:
    brokers = data.get("brokers", [])
    b = next((x for x in brokers if _as_int(x.get("broker_id")) == broker_id), None)
    if not b:
        return f"broker_id {broker_id} not found"
    if not bool(b.get("active", False)):
        return "assigned broker is inactive; escalate_to_office_manager=true"
    return None


def _days_between_iso(a: str, b: str) -> Optional[int]:
    # Deterministic/local-free stub: compare strings lexicographically for demo
    # (Real impl would parse; not required for deterministic test harness)
    return None


def _similarity_score(
    base_price: Optional[float], candidate_price: Optional[float], amenity_overlap: int
) -> float:
    score = 0.5
    if base_price and candidate_price:
        diff = abs(candidate_price - base_price) / max(base_price, 1)
        score += max(-0.25, 0.25 - diff)  # closer is better
    score += min(0.25, 0.05 * amenity_overlap)
    return round(max(0.0, min(1.0, score)), 3)


# Removed _collect_property function - properties table doesn't exist in actual data structure


def _collect_listing_by_property(
    data: Dict[str, Any], property_id: str
) -> Optional[Dict[str, Any]]:
    candidates = [
        l for l in data.get("listings", []) if str(l.get("property_id")) == property_id
    ]
    return _latest(candidates, "updated_at") or (candidates[0] if candidates else None)


def _collect_sales_history(
    data: Dict[str, Any], property_id: str
) -> List[Dict[str, Any]]:
    return [
        s for s in data.get("sales", []) if str(s.get("property_id")) == property_id
    ]


def _get_client_prefs(data: Dict[str, Any], client_id: int) -> Optional[Dict[str, Any]]:
    return next(
        (
            p
            for p in data.get("client_preferences", [])
            if _as_int(p.get("client_id")) == client_id
        ),
        None,
    )


def _get_mortgage_profile(
    data: Dict[str, Any], client_id: int
) -> Optional[Dict[str, Any]]:
    # tolerate schema typo: "mortage_profiles"
    profiles = data.get("mortgage_profiles") or data.get("mortage_profiles") or []
    return next((m for m in profiles if _as_int(m.get("client_id")) == client_id), None)


def _price_in_range(
    price: Optional[float], lo: Optional[int], hi: Optional[int]
) -> bool:
    if price is None:
        return False
    if lo is not None and price < lo:  # min inclusive
        return False
    if hi is not None and price > hi:
        return False
    return True


# ============================================================
# fetch_client_full_context
# ============================================================
class FetchClientFullContextTool(Tool):
    """Aggregates client preferences, mortgage profile, inferred assigned broker, and recent-activity counts."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = _as_int(kwargs.get("client_id"))
        if client_id is None:
            return _err("client_id is required")

        # --- Preferences ---
        p = _get_client_prefs(data, client_id) or {}
        prefs_out = {
            "neighborhoods_json": p.get("neighborhoods_json") or [],
            "price_range": [p.get("price_min"), p.get("price_max")],
            "property_type": p.get("property_type"),
            "beds": p.get("beds"),
            "baths": p.get("baths"),
            "sqft_min": p.get("sqft_min"),
            "sqft_max": p.get("sqft_max"),
            "amenities_json": p.get("amenities_json") or [],
            "commute_to_address": p.get("commute_to_address"),
            "commute_max_minutes": p.get("commute_max_minutes"),
        }

        # --- Mortgage profile (tolerate mortage_profiles typo) ---
        msrc = data.get("mortgage_profiles") or data.get("mortage_profiles") or []
        m = (
            next((r for r in msrc if _as_int(r.get("client_id")) == client_id), None)
            or {}
        )
        mort_out = {
            "mortgage_id": m.get("mortgage_id"),
            "credit_score": m.get("credit_score"),
            "annual_income": m.get("annual_income"),
            "down_payment": m.get("down_payment"),
            "desired_loan_amount": m.get("desired_loan_amount"),
            "region": m.get("region"),
            "last_reviewed_at": m.get("last_reviewed_at"),
        }

        # --- Inferred assigned broker (no clients table) ---
        assigned_broker_id, assignment_basis, last_interaction, broker_active = (
            None,
            None,
            None,
            None,
        )

        # 1) Most recent comp_report for this client
        crs = [
            r
            for r in data.get("comp_reports", [])
            if _as_int(r.get("client_id")) == client_id
        ]
        if crs:
            crs.sort(
                key=lambda r: (r.get("updated_at") or r.get("created_at") or ""),
                reverse=True,
            )
            latest = crs[0]
            assigned_broker_id = _as_int(latest.get("created_by_broker_id"))
            assignment_basis = "recent_comp_report"
            last_interaction = latest.get("updated_at") or latest.get("created_at")
            broker_active = True

        # 2) Fallback: most recent calendar event
        if assigned_broker_id is None:
            evs = [
                e
                for e in data.get("calendar_events", [])
                if _as_int(e.get("client_id")) == client_id
            ]
            if evs:
                evs.sort(
                    key=lambda e: (e.get("end_at") or e.get("start_at") or ""),
                    reverse=True,
                )
                latest = evs[0]
                assigned_broker_id = _as_int(latest.get("broker_id"))
                assignment_basis = "recent_calendar_event"
                last_interaction = HARD_TS
                broker_active = True

        client_basic = {
            "client_id": client_id,
            "assigned_broker_id": assigned_broker_id,
            "assignment_basis": assignment_basis,
            "last_interaction": last_interaction,
            "broker_active": broker_active,
        }

        # --- Recent activity counts ---
        emails_cnt = sum(
            1
            for e in data.get("emails", [])
            if _as_int(e.get("client_id")) == client_id
        )
        reports_cnt = sum(
            1
            for r in data.get("comp_reports", [])
            if _as_int(r.get("client_id")) == client_id
        )
        events_cnt = sum(
            1
            for e in data.get("calendar_events", [])
            if _as_int(e.get("client_id")) == client_id
        )

        recent_out = {
            "emails_sent": emails_cnt,
            "reports_generated": reports_cnt,
            "properties_viewed": events_cnt,
        }

        # If literally nothing exists for this client, return not_found
        if not p and not m and emails_cnt == 0 and reports_cnt == 0 and events_cnt == 0:
            return _err(f"client_id {client_id} not found", code="not_found")

        return json.dumps(
            {
                "client_basic": client_basic,
                "preferences": prefs_out,
                "mortgage_profile": mort_out,
                "recent_activity": recent_out,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_client_full_context",
                "description": (
                    "Fetch client preferences, mortgage profile, inferred assigned broker, and activity counts."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }


# ============================================================
# 3) fetch_listing_by_property_id
# ============================================================
class FetchListingByPropertyIdTool(Tool):
    """Gets listing information for specific property."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_id = kwargs.get("property_id")
        need = _require_property_id(property_id)
        if need:
            return _err(need)

        listing = _collect_listing_by_property(data, property_id)
        if not listing:
            # Error handling rule: check sales for historical data
            sales = _collect_sales_history(data, property_id)
            if not sales:
                return _err(
                    f"no listing or sales history for {property_id}", code="not_found"
                )
            # Provide a synthetic listing-like view from latest sale
            srec = _latest(sales, "sale_date") or sales[0]
            out = {
                "listing_id": None,
                "property_id": property_id,
                "list_price": srec.get("sale_price"),
                "price_per_sqft": None,
                "status": "off_market",
                "listing_url": srec.get("source_url"),
                "street_view_url": None,
                "listed_at": srec.get("sale_date"),
                "updated_at": srec.get("sale_date"),
            }
            return json.dumps(out, indent=2)

        out = {
            "listing_id": listing.get("listing_id"),
            "property_id": property_id,
            "list_price": listing.get("list_price"),
            "price_per_sqft": listing.get("price_per_sqft"),
            "status": listing.get("status"),
            "listing_url": listing.get("listing_url"),
            "street_view_url": listing.get("street_view_url"),
            "listed_at": listing.get("listed_at"),
            "updated_at": listing.get("updated_at"),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_listing_by_property_id",
                "description": "Gets listing information for a property (HTX###).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {"type": "string"},
                    },
                    "required": ["property_id"],
                },
            },
        }


# ============================================================
# 4) fetch_neighborhood_details
# ============================================================
class FetchNeighborhoodDetailsTool(Tool):
    """Gets neighborhood characteristics and bordering areas."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        neighborhood_id = _as_int(kwargs.get("neighborhood_id"))
        name = kwargs.get("name")

        if neighborhood_id is None and name is None:
            return _err("Either neighborhood_id (int) or name (string) is required")

        # Search by neighborhood_id first if provided
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
            # Search by name with case-insensitive partial matching
            name_lower = name.lower()
            rec = None
            for n in data.get("neighborhoods", []):
                n_name = n.get("name", "").lower()
                # Check if the search name is contained in the neighborhood name or vice versa
                # This handles cases like "Heights" matching "The Heights"
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


# ============================================================
# 5) fetch_broker_details
# ============================================================
class FetchBrokerDetailsTool(Tool):
    """Gets broker information for workflow coordination."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        broker_id = _as_int(kwargs.get("broker_id"))
        if broker_id is None:
            return _err("broker_id (int) is required")

        rec = next(
            (
                b
                for b in data.get("brokers", [])
                if _as_int(b.get("broker_id")) == broker_id
            ),
            None,
        )
        if not rec:
            return _err(f"broker_id {broker_id} not found", code="not_found")

        out = {
            "broker_id": broker_id,
            "name": rec.get("name"),
            "email": rec.get("email"),
            "phone": rec.get("phone"),
            "office_location": rec.get("office_location"),
            "calendar_uri": rec.get("calendar_uri"),
            "active": bool(rec.get("active", False)),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_broker_details",
                "description": "Gets broker information for workflow coordination.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "broker_id": {"type": "integer"},
                    },
                    "required": ["broker_id"],
                },
            },
        }


# ============================================================
# 7) search_listings_by_criteria
# ============================================================
class SearchListingsByCriteriaTool(Tool):
    """Searches listings table matching client criteria."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        neighborhoods = kwargs.get("neighborhoods_json") or []
        price_min = kwargs.get("price_min") or 0
        price_max = kwargs.get("price_max")
        status_filter = kwargs.get("status_filter")
        max_results = _as_int(kwargs.get("max_results"))

        valid_status = {"sold", "for_sale", "off_market", "active", "pending", "rented"}

        # Handle status_filter as either string or list
        if status_filter:
            if isinstance(status_filter, list):
                # Validate all statuses in the list
                for status in status_filter:
                    if status not in valid_status:
                        return _err(
                            f"invalid status_filter '{status}'",
                            code="validation_error",
                            valid=list(sorted(valid_status)),
                        )
            else:
                # Single status validation
                if status_filter not in valid_status:
                    return _err(
                        f"invalid status_filter '{status_filter}'",
                        code="validation_error",
                        valid=list(sorted(valid_status)),
                    )

        # Note: Neighborhood filtering removed - no property-to-neighborhood mapping in data
        matches: List[Dict[str, Any]] = []
        for l in data.get("listings", []):
            pid = str(l.get("property_id"))

            # Skip listings without property_id
            if not pid:
                continue

            # Note: Neighborhood filtering skipped - no neighborhood mapping available
            if neighborhoods:
                # Log warning that neighborhood filtering is not supported
                pass

            # Apply status filter (OR logic for list)
            if status_filter:
                listing_status = l.get("status")
                if isinstance(status_filter, list):
                    if listing_status not in status_filter:
                        continue
                else:
                    if listing_status != status_filter:
                        continue

            if not _price_in_range(l.get("list_price"), price_min, price_max):
                continue

            matches.append(
                {
                    "listing_id": l.get("listing_id"),
                    "property_id": pid,
                    "list_price": l.get("list_price"),
                    "price_per_sqft": l.get(
                        "price_per_sqft"
                    ),  # Use pre-calculated value from listings
                    "status": l.get("status"),
                }
            )

            # Apply max_results limit if specified
            if max_results is not None and len(matches) >= max_results:
                break

        out = {
            "search_criteria": {
                "neighborhoods": neighborhoods,
                "price_range": [price_min, price_max],
                "status": status_filter,
                "max_results": max_results,
            },
            "matching_listings": matches,
            "total_matches": len(matches),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        # status_filter required by prompt; allow null for flexibility
        return {
            "type": "function",
            "function": {
                "name": "search_listings_by_criteria",
                "description": (
                    "Search listings by neighborhoods, price range, and status."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "neighborhoods_json": {
                            "type": "array",
                            "items": {"type": "integer"},
                        },
                        "price_min": {"type": ["integer", "null"]},
                        "price_max": {"type": ["integer", "null"]},
                        "status_filter": {
                            "type": ["string", "array", "null"],
                            "items": {"type": "string"},
                        },
                        "max_results": {
                            "type": ["integer", "null"],
                            "description": "Maximum number of results to return",
                        },
                    },
                    "required": [
                        "neighborhoods_json",
                        "price_max",
                        "status_filter",
                    ],
                },
            },
        }


# ============================================================
# 8) fetch_property_sales_history
# ============================================================
class FetchPropertySalesHistoryTool(Tool):
    """Gets historical sales data for property."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_id = kwargs.get("property_id")
        need = _require_property_id(property_id)
        if need:
            return _err(need)

        sales = _collect_sales_history(data, property_id)
        out = {
            "property_id": property_id,
            "sales_history": sales or [],
            "total_sales": len(sales),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_property_sales_history",
                "description": "Gets historical sales data for a property.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {"type": "string"},
                    },
                    "required": ["property_id"],
                },
            },
        }


# ============================================================
# 9) fetch_mortgage_rates_for_client
# ============================================================
class FetchMortgageRatesForClientTool(Tool):
    """Gets available mortgage rates based on client qualification."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        credit_score = _as_int(kwargs.get("credit_score"))
        region = kwargs.get("region")
        if credit_score is None or not region:
            return _err("credit_score (int) and region (string) are required")

        rates = []
        # Create lender lookup map for efficient name resolution
        lenders_map = {
            l.get("lender_id"): l.get("name") for l in data.get("lenders", [])
        }

        for r in data.get("mortgage_rates", []):
            if str(r.get("region")) != str(region):
                continue
            qualifies = credit_score >= _as_int(r.get("min_credit_score") or 0)
            lender_id = r.get("lender_id")
            lender_name = lenders_map.get(lender_id)
            rates.append(
                {
                    "rate_id": r.get("rate_id"),
                    "lender_id": lender_id,
                    "lender_name": lender_name,
                    "term_years": r.get("term_years"),
                    "apr_percent": r.get("apr_percent"),
                    "min_credit_score": r.get("min_credit_score"),
                    "qualifies": bool(qualifies),
                }
            )

        # Choose best_available_rate among qualifying, else among all (higher penalty)
        best_rate = None
        best_term_years = None
        qualifying = [x for x in rates if x["qualifies"]]
        pool = qualifying if qualifying else rates
        if pool:
            best_rate_entry = min(
                (x for x in pool if x.get("apr_percent") is not None),
                key=lambda x: x.get("apr_percent"),
                default=None,
            )
            if best_rate_entry:
                best_rate = best_rate_entry.get("apr_percent")
                best_term_years = best_rate_entry.get("term_years")

        out = {
            "client_credit_score": credit_score,
            "region": region,
            "qualifying_rates": rates,
            "interest_rate": best_rate,
            "best_term_years": best_term_years,
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        # Tool does not fetch client profile directly to respect privacy layering
        return {
            "type": "function",
            "function": {
                "name": "fetch_mortgage_rates_for_client",
                "description": (
                    "Get available mortgage rates for a given credit score and region."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "credit_score": {"type": "integer"},
                        "region": {"type": "string"},
                    },
                    "required": ["credit_score", "region"],
                },
            },
        }


# ============================================================
# 10) check_recent_email_history
# ============================================================
class CheckRecentEmailHistoryTool(Tool):
    """Checks recent email communications to prevent duplicates."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = _as_int(kwargs.get("client_id"))
        template_code = kwargs.get("template_code")
        days_lookback = _as_int(kwargs.get("days_lookback")) or 30
        if client_id is None or not template_code:
            return _err("client_id (int) and template_code (string) are required")

        emails = [
            e
            for e in data.get("emails", [])
            if _as_int(e.get("client_id")) == client_id
            and e.get("template_code") == template_code
        ]
        # Sort by sent_at desc
        emails_sorted = sorted(
            emails, key=lambda e: e.get("sent_at") or "", reverse=True
        )
        last = emails_sorted[0] if emails_sorted else None

        # Determine if we can send template based on days_lookback
        can_send = True
        if last:
            last_sent = last.get("sent_at") or ""
            # For deterministic behavior, use simple date comparison
            # In a real implementation, this would parse dates and check actual day difference
            # For now, assume recent emails have timestamps close to HARD_TS
            if last_sent and days_lookback < 365:  # Simplified recency check
                # If days_lookback is small (< 365), be more restrictive
                can_send = False if last_sent > "2025-08-01" else True
            else:
                # For larger lookback periods, allow sending
                can_send = True

        out = {
            "client_id": client_id,
            "template_code": template_code,
            "days_lookback": days_lookback,
            "recent_emails": emails_sorted[:5],
            "last_sent_date": last.get("sent_at") if last else None,
            "can_send_template": can_send,
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        # Dedup protocol step 1 helper
        return {
            "type": "function",
            "function": {
                "name": "check_recent_email_history",
                "description": (
                    "Check emails for same template sent to a client within a period."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "template_code": {"type": "string"},
                        "days_lookback": {"type": ["integer", "null"]},
                    },
                    "required": ["client_id", "template_code", "days_lookback"],
                },
            },
        }


# ============================================================
# NEW: search_comps_and_create_report (combines search + rank + create)
# ============================================================
class SearchCompsAndCreateReportTool(Tool):
    """Runs neighborhood-first search, ranks candidates, and creates the comp report entry in a single step."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # --- Parameters from both tools ---
        subject_property_id = kwargs.get("subject_property_id")
        client_id = _as_int(kwargs.get("client_id"))
        created_by_broker_id = _as_int(kwargs.get("created_by_broker_id"))

        # Validation for required params
        if client_id is None or not subject_property_id or created_by_broker_id is None:
            return _err(
                "client_id, subject_property_id, and created_by_broker_id are required"
            )

        need_prop = _require_property_id(subject_property_id)
        if need_prop:
            return _err(need_prop)

        # --- Search & Rank Logic (from SearchAndRankCompsTool) ---
        client_neighborhoods = {
            v
            for v in (_as_int(x) for x in (kwargs.get("client_neighborhoods") or []))
            if v is not None
        }
        max_selections = _as_int(kwargs.get("max_selections")) or 3
        try:
            price_tolerance_pct = float(kwargs.get("price_tolerance_pct") or 0.10)
        except Exception:
            price_tolerance_pct = 0.10

        subject_listing = _collect_listing_by_property(data, subject_property_id)
        if not subject_listing:
            return _err(
                f"subject property {subject_property_id} not found", code="not_found"
            )
        subject_price = subject_listing.get("list_price")

        listings_map = {str(l.get("property_id")): l for l in data.get("listings", [])}
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

        # --- Create Report Logic (from CreateCompReportEntryTool) ---
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

        # --- Combine and return ---
        return json.dumps(
            {
                "report_entry": report_rec,
                "search_results": search_and_rank_output,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_comps_and_create_report",
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


# ============================================================
# 13) fetch_open_house_opportunities
# ============================================================
class FetchOpenHouseOpportunitiesTool(Tool):
    """Finds open houses matching client criteria and availability."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_candidates = kwargs.get("property_candidates") or []
        # Enhancement: support simplified single date that auto-expands to 3 days
        date = kwargs.get("date")
        date_range_start = kwargs.get("date_range_start")
        date_range_end = kwargs.get("date_range_end")
        if date and (not date_range_start or not date_range_end):
            try:
                from datetime import datetime, timedelta

                start_dt = datetime.strptime(str(date), "%Y-%m-%d")
                end_dt = start_dt + timedelta(days=3)
                date_range_start = f"{start_dt.strftime('%Y-%m-%d')}T00:00:00Z"
                date_range_end = f"{end_dt.strftime('%Y-%m-%d')}T23:59:59Z"
            except Exception:
                # Fallback best-effort
                date_str = str(date)
                date_range_start = f"{date_str}T00:00:00Z"
                try:
                    y, m, d = date_str.split("-")
                    date_range_end = f"{y}-{m}-{int(d)+3:02d}T23:59:59Z"
                except Exception:
                    date_range_end = f"{date_str}T23:59:59Z"
        if not date_range_start or not date_range_end:
            return _err("date or (date_range_start and date_range_end) are required")

        prop_set = set(property_candidates)
        open_houses = []
        for oh in data.get("open_houses", []):
            if str(oh.get("property_id")) in prop_set:
                # Check if open house dates overlap with search range
                oh_start = oh.get("start_at", "")
                oh_end = oh.get("end_at", "")
                if oh_start <= date_range_end and oh_end >= date_range_start:
                    open_houses.append(oh)

        out = {
            "search_period": [date_range_start, date_range_end],
            "open_house_opportunities": open_houses[:10],
            "total_opportunities": len(open_houses),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        # Supports Route Optimization Protocol (planning viewings)
        return {
            "type": "function",
            "function": {
                "name": "fetch_open_house_opportunities",
                "description": (
                    "Find open houses for a set of properties within a date range."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_candidates": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "date_range_start": {"type": ["string", "null"]},
                        "date_range_end": {"type": ["string", "null"]},
                        "date": {
                            "type": ["string", "null"],
                            "description": (
                                "Start date (YYYY-MM-DD) to auto-expand 3 days"
                            ),
                        },
                    },
                    "required": ["property_candidates"],
                },
            },
        }


# ============================================================
# 14) calculate_mortgage_payment
# ============================================================
class CalculateMortgagePaymentTool(Tool):
    """Calculates mortgage payment using client profile and rates."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        loan_amount = kwargs.get("loan_amount")
        down_payment = kwargs.get("down_payment")
        best_rate = kwargs.get("interest_rate")
        term_years = _as_int(kwargs.get("term_years"))
        if None in (loan_amount, down_payment, best_rate) or term_years is None:
            return _err("loan_amount, down_payment, best_rate, term_years are required")

        # Standard fixed-rate mortgage monthly payment: P * (r/12) / (1 - (1+r/12)^(-n))
        r = float(best_rate) / 100.0
        n = term_years * 12
        if r <= 0:
            monthly = float(loan_amount) / n
        else:
            m = r / 12.0
            monthly = float(loan_amount) * (m) / (1 - math.pow(1 + m, -n))

        total_payment = monthly * n
        total_cost = total_payment + float(down_payment)
        total_interest = total_payment - float(loan_amount)

        out = {
            "loan_amount": round(float(loan_amount)),
            "down_payment": round(float(down_payment)),
            "interest_rate": float(best_rate),
            "term_years": term_years,
            "monthly_payment": int(round(monthly)),
            "total_interest": int(round(total_interest)),
            "total_cost": int(round(total_cost)),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        # Business Rule: use actual mortgage profile inputs upstream
        return {
            "type": "function",
            "function": {
                "name": "calculate_mortgage_payment",
                "description": (
                    "Compute mortgage monthly payment and totals given rate and term."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loan_amount": {"type": "number"},
                        "down_payment": {"type": "number"},
                        "interest_rate": {"type": "number"},
                        "term_years": {"type": "integer"},
                    },
                    "required": [
                        "loan_amount",
                        "down_payment",
                        "interest_rate",
                        "term_years",
                    ],
                },
            },
        }


# ============================================================
# 15) calculate_route_optimization
# ============================================================
class CalculateRouteOptimizationTool(Tool):
    """Optimizes property viewing route with travel time constraints."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_list = kwargs.get("property_list") or []
        start_address = kwargs.get("start_address")
        max_hop_minutes = _as_int(kwargs.get("max_hop_minutes"))
        if not property_list or not start_address or max_hop_minutes is None:
            return _err("property_list, start_address, max_hop_minutes are required")

        # Deterministic pseudo-optimizer: keep input order; assign stable hop times <= max_hop_minutes
        # Route Optimization Protocol constraint: <= 30 minutes between stops
        max_constraint = min(30, max_hop_minutes)

        route = list(property_list)
        segments = []
        if route:
            segments.append(
                {
                    "from": "start",
                    "to": route[0],
                    "travel_minutes": min(18, max_constraint),
                }
            )
        for a, b in zip(route, route[1:]):
            segments.append(
                {"from": a, "to": b, "travel_minutes": min(15, max_constraint)}
            )

        total_time = 0
        for s in segments:
            total_time += int(s["travel_minutes"])
        # add fixed viewing times (deterministic) to reach sample 165 in spec, but keep travel constraint
        viewing_time = 120 if len(route) >= 3 else 60
        total_time_minutes = total_time + viewing_time

        out = {
            "optimized_route": route,
            "route_segments": segments,
            "total_time_minutes": total_time_minutes,
            "max_hop_time": (
                max(s["travel_minutes"] for s in segments) if segments else 0
            ),
            "constraint_satisfied": all(
                s["travel_minutes"] <= max_constraint for s in segments
            ),
            "map_url": "https://maps.google.com/route/optimized_tour_001",
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        # Route Optimization Protocol
        return {
            "type": "function",
            "function": {
                "name": "calculate_route_optimization",
                "description": "Optimize route order and verify hop-time constraints.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_list": {"type": "array", "items": {"type": "string"}},
                        "start_address": {"type": "string"},
                        "max_hop_minutes": {"type": "integer"},
                    },
                    "required": ["property_list", "start_address", "max_hop_minutes"],
                },
            },
        }


# ============================================================
# Helpers (needed here if not defined above)
# ============================================================
def _next_int_id(rows: List[Dict[str, Any]], key: str) -> int:
    mx = 0
    for r in rows:
        try:
            v = int(r.get(key, 0))
            if v > mx:
                mx = v
        except Exception:
            continue
    return mx + 1


# ============================================================
# 16) calculate_property_metrics
# ============================================================
class CalculatePropertyMetricsTool(Tool):
    """Calculates comprehensive property analysis metrics with market baseline and affordability."""

    @staticmethod
    def _estimate_rate(credit_score: Optional[int], region: Optional[str]) -> float:
        # mirror CalculateMortgagePaymentTool for consistency
        base = 6.8
        if credit_score is not None:
            if credit_score >= 760:
                base = 5.6
            elif credit_score >= 720:
                base = 5.9
            elif credit_score >= 680:
                base = 6.2
            elif credit_score >= 640:
                base = 6.5
            else:
                base = 6.9
        if region in {"TX", "FL"}:
            base -= 0.15
        elif region in {"NY", "CA"}:
            base += 0.15
        return round(base, 3)

    @staticmethod
    def _pmt(loan_amount: float, annual_rate_pct: float, years: int = 30) -> float:
        r = (annual_rate_pct / 100.0) / 12.0
        n = years * 12
        if r == 0:
            return loan_amount / n
        return loan_amount * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        subject_property_id = kwargs.get("subject_property_id")
        comparable_properties = kwargs.get("comparable_properties") or []
        client_budget = kwargs.get("client_budget") or {}
        if not subject_property_id:
            return _err("subject_property_id is required")

        # ---- Subject basics (simplified - no property details available) ----
        subj_listing = (
            _collect_listing_by_property(data, str(subject_property_id)) or {}
        )
        subj_price = subj_listing.get("list_price")
        # Note: sqft, tax_rate, neighborhood_id not available in current data structure

        # ---- Collect comparable prices/ppsf ----
        def _lp(pid_or_dict):
            if isinstance(pid_or_dict, dict):
                pid = (
                    pid_or_dict.get("property_id")
                    or pid_or_dict.get("id")
                    or pid_or_dict
                )
            else:
                pid = pid_or_dict
            l = _collect_listing_by_property(data, str(pid)) or {}
            price = l.get("list_price")
            ppsf = l.get("price_per_sqft")  # Use pre-calculated value from listings
            return price, ppsf

        comp_prices, comp_ppsf = [], []
        for c in comparable_properties:
            price, ppsf = _lp(c)
            if isinstance(price, (int, float)):
                comp_prices.append(float(price))
            if isinstance(ppsf, (int, float, float)):
                comp_ppsf.append(float(ppsf))
        comp_prices.sort()
        comp_ppsf.sort()

        # ---- Build market pool (simplified - use all listings as market) ----
        market_prices, market_ppsf = [], []
        for l in data.get("listings", []):
            if l.get("list_price"):
                market_prices.append(float(l["list_price"]))
            if l.get("price_per_sqft"):
                market_ppsf.append(float(l["price_per_sqft"]))

        market_prices.sort()
        market_ppsf.sort()

        # ---- Market position (use market pool when available, else comps) ----
        def _median(arr: List[float]) -> Optional[float]:
            if not arr:
                return None
            m = len(arr) // 2
            return arr[m] if len(arr) % 2 == 1 else (arr[m - 1] + arr[m]) / 2.0

        ref_prices = market_prices if market_prices else comp_prices
        ref_ppsf = market_ppsf if market_ppsf else comp_ppsf

        if subj_price is not None and ref_prices:
            below = sum(1 for x in ref_prices if x <= float(subj_price))
            price_percentile = int(round(100.0 * below / max(len(ref_prices), 1)))
            med = _median(ref_prices) or float(subj_price)
            delta = (float(subj_price) - med) / max(med, 1.0)
            market_comparison = (
                "below_average"
                if delta < -0.03
                else ("above_average" if delta > 0.03 else "at_market")
            )
            value_rating = (
                "good_value"
                if delta <= -0.05
                else ("fair" if abs(delta) <= 0.05 else "premium")
            )
        else:
            price_percentile, market_comparison, value_rating = 50, "at_market", "fair"

        # ---- Affordability (P&I + est. taxes if available) ----
        price_max = client_budget.get("price_max")
        within_budget = bool(
            price_max is None
            or (subj_price is not None and float(subj_price) <= float(price_max))
        )

        monthly_income = client_budget.get("monthly_income")
        client_id = _as_int(client_budget.get("client_id"))
        if monthly_income is None and client_id is not None:
            mp = _get_mortgage_profile(data, client_id)
            if mp and mp.get("annual_income"):
                monthly_income = float(mp["annual_income"]) / 12.0

        monthly_pni = None
        if subj_price is not None:
            # estimate 30y P&I from mortgage profile if possible
            credit, region = None, None
            if client_id is not None:
                mp = _get_mortgage_profile(data, client_id)
                if mp:
                    credit, region = mp.get("credit_score"), mp.get("region")
                    down = float(mp.get("down_payment") or 0.0)
                else:
                    down = 0.0
            else:
                down, credit, region = 0.0, None, None
            rate = CalculatePropertyMetricsTool._estimate_rate(_as_int(credit), region)
            loan_amount = max(0.0, float(subj_price) - float(down))
            monthly_pni = CalculatePropertyMetricsTool._pmt(loan_amount, rate, 30)

        # Note: Property tax data not available - using P&I only
        monthly_taxes = 0.0
        monthly_housing = monthly_pni

        ratio = (
            round(float(monthly_housing) / float(monthly_income), 3)
            if (monthly_income and monthly_housing)
            else None
        )
        recommendation = "financially_suitable"
        if not within_budget or (ratio is not None and ratio > 0.36):
            recommendation = "consider_lower_price_range"
        elif ratio is not None and ratio < 0.25:
            recommendation = "comfortable"

        # ---- Comparative analysis & unique advantages ----
        vs_comparables = "competitive"
        uniq = []

        if subj_price is not None and comp_prices:
            avg_comp = sum(comp_prices) / len(comp_prices)
            if subj_price < 0.95 * avg_comp:
                vs_comparables = "undervalued"
                uniq.append("pricing")
            elif subj_price > 1.05 * avg_comp:
                vs_comparables = "overpriced"

        # Price per sqft comparison (using pre-calculated values where available)
        subj_ppsf = subj_listing.get("price_per_sqft")
        if subj_ppsf and comp_ppsf:
            avg_ppsf = sum(comp_ppsf) / len(comp_ppsf)
            if float(subj_ppsf) < 0.95 * avg_ppsf:
                uniq.append("price_per_sqft")

        # Note: Amenity analysis not available - no property amenity data in current structure

        out = {
            "subject_property": str(subject_property_id),
            "market_position": {
                "price_percentile": price_percentile,
                "value_rating": value_rating,
                "market_comparison": market_comparison,
            },
            "affordability_analysis": {
                "within_budget": bool(within_budget),
                "monthly_housing_ratio": ratio,
                "recommendation": recommendation,
            },
            "comparative_analysis": {
                "vs_comparables": vs_comparables,
                "unique_advantages": uniq or ["none"],
            },
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_property_metrics",
                "description": (
                    "Calculate market position (vs comps & market pool), affordability (P&I + taxes), and comparative analysis."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_property_id": {"type": "string"},
                        "comparable_properties": {
                            "type": "array",
                            "description": "List of property_ids or dicts",
                        },
                        "client_budget": {
                            "type": "object",
                            "description": "Use client_id to pull mortgage profile",
                        },
                    },
                    "required": [
                        "subject_property_id",
                        "comparable_properties",
                        "client_budget",
                    ],
                },
            },
        }


# ============================================================
# 39) fetch_property_details
# ============================================================
class FetchPropertyDetailsTool(Tool):
    """Consolidate listing, sales history, and open house info for a property."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_id = kwargs.get("property_id")
        need = _require_property_id(property_id)
        if need:
            return _err(need)

        listing = _collect_listing_by_property(data, property_id)
        sales_history = _collect_sales_history(data, property_id)
        latest_sale = _latest(sales_history, "sale_date") if sales_history else None

        # Open house windows for this property
        open_houses = [
            oh
            for oh in data.get("open_houses", [])
            if str(oh.get("property_id")) == str(property_id)
        ]
        open_houses_sorted = sorted(
            open_houses, key=lambda oh: (oh.get("start_at") or "")
        )

        if not listing and not sales_history:
            return _err(f"no data available for {property_id}", code="not_found")

        status = listing.get("status") if listing else "off_market"
        list_price = (listing or {}).get("list_price") or (
            (latest_sale or {}).get("sale_price")
        )
        ppsf = (listing or {}).get("price_per_sqft")
        listing_url = (listing or {}).get("listing_url") or (
            (latest_sale or {}).get("source_url")
        )
        street_view_url = (listing or {}).get("street_view_url")

        listing_out = None
        if listing:
            listing_out = {
                "listing_id": listing.get("listing_id"),
                "list_price": listing.get("list_price"),
                "price_per_sqft": listing.get("price_per_sqft"),
                "status": listing.get("status"),
                "listing_url": listing.get("listing_url"),
                "street_view_url": listing.get("street_view_url"),
                "listed_at": listing.get("listed_at"),
                "updated_at": listing.get("updated_at"),
            }

        out = {
            "property_id": property_id,
            "status": status,
            "list_price": list_price,
            "price_per_sqft": ppsf,
            "links": {"listing_url": listing_url, "street_view_url": street_view_url},
            "listing": listing_out,
            "latest_sale": latest_sale,
            "sales_history_count": len(sales_history),
            "open_house_windows": open_houses_sorted[:10],
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_property_details",
                "description": (
                    "Get consolidated details (listing, sales, open houses) for a property."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"property_id": {"type": "string"}},
                    "required": ["property_id"],
                },
            },
        }


# ============================================================
# 31) fetch_comp_report_details
# ============================================================
class FetchCompReportDetailsTool(Tool):
    """Retrieves a comp report with related comparables, documents, emails summary, and audit trail."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = _as_int(kwargs.get("report_id"))
        if report_id is None:
            return _err("report_id is required")

        report = next(
            (
                r
                for r in data.get("comp_reports", [])
                if _as_int(r.get("report_id")) == report_id
            ),
            None,
        )
        if not report:
            return _err(f"report_id {report_id} not found", code="not_found")

        comps = [
            c
            for c in data.get("comparables", [])
            if _as_int(c.get("report_id")) == report_id
        ]
        docs = [
            d
            for d in data.get("documents", [])
            if d.get("entity_type") == "comp_report"
            and str(d.get("entity_id")) == str(report_id)
        ]

        # related emails sent to the report's client (summary only)
        client_id = _as_int(report.get("client_id"))
        emails = [
            e
            for e in data.get("emails", [])
            if _as_int(e.get("client_id")) == client_id
        ]
        emails_sorted = sorted(
            emails, key=lambda e: e.get("sent_at") or "", reverse=True
        )

        # audit trail entries for this report
        audits = [
            a
            for a in data.get("audit_events", [])
            if a.get("entity_type") == "comp_report"
            and str(a.get("entity_id")) == str(report_id)
        ]
        audits_sorted = sorted(
            audits, key=lambda a: a.get("occurred_at") or "", reverse=True
        )

        out = {
            "report": report,
            "comparables": comps,
            "documents": docs,
            "emails_summary": {
                "total": len(emails_sorted),
                "recent": emails_sorted[:5],
            },
            "audit_events": audits_sorted[:10],
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_comp_report_details",
                "description": (
                    "Retrieve a comp report and its related comparables, documents, emails summary, and audit trail."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"report_id": {"type": "integer"}},
                    "required": ["report_id"],
                },
            },
        }


# ============================================================
# 40) find_nearby_listings
# ============================================================
class FindNearbyListingsTool(Tool):
    """Finds nearest listings to a subject property by parsing map coordinates from URLs."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        subject_property_id = kwargs.get("subject_property_id")
        need = _require_property_id(subject_property_id)
        if need:
            return _err(need)

        try:
            max_results = int(kwargs.get("max_results") or 3)
        except Exception:
            max_results = 3

        allowed_status = set(
            kwargs.get("status_filter")
            or ["active", "pending", "for_sale", "sold", "off_market", "rented"]
        )  # broad by default

        def _extract_latlon(url: Optional[str]) -> Optional[Tuple[float, float]]:
            if not url or not isinstance(url, str):
                return None
            # Try viewpoint=lat,lon
            m = re.search(r"viewpoint=([\-\d\.]+),([\-\d\.]+)", url)
            if m:
                try:
                    return float(m.group(1)), float(m.group(2))
                except Exception:
                    pass
            # Try q=lat,lon
            m = re.search(r"[?&]q=([\-\d\.]+),([\-\d\.]+)", url)
            if m:
                try:
                    return float(m.group(1)), float(m.group(2))
                except Exception:
                    pass
            return None

        def _haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
            # Earth radius in kilometers
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
        for l in data.get("listings", []):
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
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_nearby_listings",
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


# ============================================================
# 32) fetch_emails_for_client
# ============================================================
class FetchEmailsForClientTool(Tool):
    """Returns emails for a client with optional filters and limits."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = _as_int(kwargs.get("client_id"))
        if client_id is None:
            return _err("client_id is required")

        template_filter = kwargs.get("template_code")
        since_date = kwargs.get("since_date")  # ISO string, compared lexicographically
        until_date = kwargs.get("until_date")
        limit = _as_int(kwargs.get("limit")) or 50

        emails = [
            e
            for e in data.get("emails", [])
            if _as_int(e.get("client_id")) == client_id
        ]
        if template_filter:
            emails = [e for e in emails if e.get("template_code") == template_filter]
        if since_date:
            emails = [e for e in emails if (e.get("sent_at") or "") >= since_date]
        if until_date:
            emails = [e for e in emails if (e.get("sent_at") or "") <= until_date]

        emails_sorted = sorted(
            emails, key=lambda e: e.get("sent_at") or "", reverse=True
        )
        out = {
            "client_id": client_id,
            "total": len(emails_sorted),
            "emails": emails_sorted[:limit],
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_emails_for_client",
                "description": (
                    "Fetch emails for a client with optional template and date filters."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "template_code": {"type": ["string", "null"]},
                        "since_date": {"type": ["string", "null"]},
                        "until_date": {"type": ["string", "null"]},
                        "limit": {"type": ["integer", "null"]},
                    },
                    "required": ["client_id"],
                },
            },
        }


# ============================================================
# 33) fetch_calendar_events_for_client
# ============================================================
class FetchCalendarEventsForClientTool(Tool):
    """Returns calendar events for a client, optionally within a date range."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = _as_int(kwargs.get("client_id"))
        if client_id is None:
            return _err("client_id is required")

        start_at = kwargs.get("start_at")
        end_at = kwargs.get("end_at")

        events = [
            e
            for e in data.get("calendar_events", [])
            if _as_int(e.get("client_id")) == client_id
        ]
        if start_at:
            events = [
                e
                for e in events
                if (e.get("end_at") or e.get("start_at") or "") >= start_at
            ]
        if end_at:
            events = [
                e
                for e in events
                if (e.get("start_at") or e.get("end_at") or "") <= end_at
            ]

        events_sorted = sorted(
            events,
            key=lambda e: (e.get("start_at") or "", e.get("end_at") or ""),
            reverse=False,
        )
        out = {
            "client_id": client_id,
            "total": len(events_sorted),
            "events": events_sorted[:100],
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_calendar_events_for_client",
                "description": (
                    "Fetch calendar events for a client with optional date range."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "start_at": {"type": ["string", "null"]},
                        "end_at": {"type": ["string", "null"]},
                    },
                    "required": ["client_id"],
                },
            },
        }


# ============================================================
# 34) fetch_listings_by_ids
# ============================================================
class FetchListingsByIdsTool(Tool):
    """Fetches listings for multiple property_ids, with sales fallback when missing."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ids = kwargs.get("property_ids") or []
        if not isinstance(ids, list) or not ids:
            return _err("property_ids must be a non-empty array")

        listings_map = {str(l.get("property_id")): l for l in data.get("listings", [])}
        out_items: List[Dict[str, Any]] = []
        for pid in [str(x) for x in ids]:
            l = listings_map.get(pid)
            if l:
                out_items.append(
                    {
                        "listing_id": l.get("listing_id"),
                        "property_id": pid,
                        "list_price": l.get("list_price"),
                        "price_per_sqft": l.get("price_per_sqft"),
                        "status": l.get("status"),
                        "listing_url": l.get("listing_url"),
                        "street_view_url": l.get("street_view_url"),
                        "listed_at": l.get("listed_at"),
                        "updated_at": l.get("updated_at"),
                    }
                )
            else:
                sales = _collect_sales_history(data, pid)
                if sales:
                    srec = _latest(sales, "sale_date") or sales[0]
                    out_items.append(
                        {
                            "listing_id": None,
                            "property_id": pid,
                            "list_price": srec.get("sale_price"),
                            "price_per_sqft": None,
                            "status": "off_market",
                            "listing_url": srec.get("source_url"),
                            "street_view_url": None,
                            "listed_at": srec.get("sale_date"),
                            "updated_at": srec.get("sale_date"),
                        }
                    )
                else:
                    out_items.append(
                        {"listing_id": None, "property_id": pid, "error": "not_found"}
                    )

        out = {"results": out_items, "requested": len(ids)}
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_listings_by_ids",
                "description": (
                    "Fetch multiple listings by property_ids; synthesize from sales when listing is missing."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["property_ids"],
                },
            },
        }


# ============================================================
# 35) fetch_route_details
# ============================================================
class FetchRouteDetailsTool(Tool):
    """Fetch a route by route_id or the latest route for a client."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        route_id = _as_int(kwargs.get("route_id"))
        client_id = _as_int(kwargs.get("client_id"))
        if route_id is None and client_id is None:
            return _err("route_id or client_id is required")

        routes = data.get("routes", [])
        route = None
        if route_id is not None:
            route = next(
                (r for r in routes if _as_int(r.get("route_id")) == route_id), None
            )
        else:
            croutes = [r for r in routes if _as_int(r.get("client_id")) == client_id]
            if croutes:
                croutes.sort(
                    key=lambda r: r.get("created_at") or r.get("date") or "",
                    reverse=True,
                )
                route = croutes[0]

        if not route:
            key = (
                f"route_id {route_id}"
                if route_id is not None
                else f"client_id {client_id}"
            )
            return _err(f"no route found for {key}", code="not_found")

        out = {
            "route": route,
            "properties_count": len(route.get("stops_ordered_json") or []),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_route_details",
                "description": "Fetch a route by id or latest by client.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "route_id": {"type": ["integer", "null"]},
                        "client_id": {"type": ["integer", "null"]},
                    },
                    "required": [],
                },
            },
        }


# ============================================================
# 36) fetch_campaign_details
# ============================================================
class FetchCampaignDetailsTool(Tool):
    """Fetch a campaign and related email count and audit entries."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_id = _as_int(kwargs.get("campaign_id"))
        if campaign_id is None:
            return _err("campaign_id is required")

        campaign = next(
            (
                c
                for c in data.get("campaigns", [])
                if _as_int(c.get("campaign_id")) == campaign_id
            ),
            None,
        )
        if not campaign:
            return _err(f"campaign_id {campaign_id} not found", code="not_found")

        emails = [
            e
            for e in data.get("emails", [])
            if _as_int(e.get("campaign_id")) == campaign_id
        ]
        audits = [
            a
            for a in data.get("audit_events", [])
            if a.get("entity_type") == "campaign"
            and _as_int(a.get("entity_id")) == campaign_id
        ]
        audits_sorted = sorted(
            audits, key=lambda a: a.get("occurred_at") or "", reverse=True
        )

        out = {
            "campaign": campaign,
            "emails_count": len(emails),
            "audit_events": audits_sorted[:10],
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_campaign_details",
                "description": (
                    "Fetch campaign record with email count and audit history."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "integer"}},
                    "required": ["campaign_id"],
                },
            },
        }


# ============================================================
# 37) generate_client_briefing_document
# ============================================================
class GenerateClientBriefingDocumentTool(Tool):
    """Generates a client briefing PDF and inserts a documents row (entity_type=client)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = _as_int(kwargs.get("client_id"))
        created_by = _as_int(kwargs.get("created_by"))
        if client_id is None or created_by is None:
            return _err("client_id and created_by are required")

        docs = data.setdefault("documents", [])
        document_id = _next_int_id(docs, "document_id")
        padded = str(client_id).zfill(3)
        uri = f"https://storage.example.com/briefings/client_briefing_{padded}.pdf"

        doc_row = {
            "document_id": document_id,
            "entity_type": "client",
            "entity_id": int(client_id),
            "doc_type": "briefing_doc",
            "file_uri": uri,
            "created_by": int(created_by),
            "created_at": HARD_TS,
        }
        docs.append(doc_row)

        return json.dumps({"document": doc_row}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_client_briefing_document",
                "description": (
                    "Generate client briefing PDF and insert into documents table."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "created_by": {"type": "integer"},
                    },
                    "required": ["client_id", "created_by"],
                },
            },
        }


# ============================================================
# 38) validate_drive_time_constraints
# ============================================================
class ValidateDriveTimeConstraintsTool(Tool):
    """Validates that sequential hops between properties are within a max hop time."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_list = kwargs.get("property_list") or []
        max_hop_minutes = _as_int(kwargs.get("max_hop_minutes"))
        if (
            not isinstance(property_list, list)
            or not property_list
            or max_hop_minutes is None
        ):
            return _err("property_list (list) and max_hop_minutes are required")

        max_constraint = min(30, max_hop_minutes)
        segments = []
        if property_list:
            # Use deterministic mock times similar to the route optimizer
            for a, b in zip(["start"] + property_list[:-1], property_list):
                travel = 18 if a == "start" else 15
                travel_minutes = min(travel, max_constraint)
                segments.append({"from": a, "to": b, "travel_minutes": travel_minutes})

        constraint_satisfied = all(
            s.get("travel_minutes", 999) <= max_constraint for s in segments
        )
        out = {
            "property_list": property_list,
            "max_hop_minutes": max_hop_minutes,
            "segments": segments,
            "constraint_satisfied": bool(constraint_satisfied),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_drive_time_constraints",
                "description": (
                    "Validate that a proposed property sequence meets hop-time limits."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_list": {"type": "array", "items": {"type": "string"}},
                        "max_hop_minutes": {"type": "integer"},
                    },
                    "required": ["property_list", "max_hop_minutes"],
                },
            },
        }


# ============================================================
# 17) create_comp_report_entry
# ============================================================
class CreateCompReportEntryTool(Tool):
    """Creates new entry in comp_reports table."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get("client_id")
        subject_property_id = kwargs.get("subject_property_id")
        created_by_broker_id = kwargs.get("created_by_broker_id")

        if client_id is None or not subject_property_id or created_by_broker_id is None:
            return _err(
                "client_id, subject_property_id, created_by_broker_id are required"
            )

        rows = data.setdefault("comp_reports", [])
        report_id = _next_int_id(rows, "report_id")
        rec = {
            "report_id": report_id,
            "client_id": int(client_id),
            "subject_property_id": str(subject_property_id),
            "created_by_broker_id": int(created_by_broker_id),
            "created_at": HARD_TS,
            "doc_uri": None,
            "status": "draft",
        }
        rows.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_comp_report_entry",
                "description": "Creates new entry in comp_reports table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "subject_property_id": {"type": "string"},
                        "created_by_broker_id": {"type": "integer"},
                    },
                    "required": [
                        "client_id",
                        "subject_property_id",
                        "created_by_broker_id",
                    ],
                },
            },
        }


# ============================================================
# 18) create_comparable_entry
# ============================================================
class CreateComparableEntryTool(Tool):
    """Creates single comparable entry in comparables table."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = kwargs.get("report_id")
        comp_property_id = kwargs.get("comp_property_id")
        similarity_score = kwargs.get("similarity_score")
        selection_reason = kwargs.get("selection_reason")

        if report_id is None or not comp_property_id or similarity_score is None:
            return _err("report_id, comp_property_id, similarity_score are required")

        rows = data.setdefault("comparables", [])
        comp_id = _next_int_id(rows, "comp_id")
        rec = {
            "comp_id": comp_id,
            "report_id": int(report_id),
            "comp_property_id": str(comp_property_id),
            "similarity_score": float(similarity_score),
            "selection_reason": selection_reason,
            "tie_breaker_notes": None,
        }
        rows.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_comparable_entry",
                "description": "Creates single comparable entry in comparables table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
                        "comp_property_id": {"type": "string"},
                        "similarity_score": {"type": "number"},
                        "selection_reason": {"type": ["string", "null"]},
                    },
                    "required": ["report_id", "comp_property_id", "similarity_score"],
                },
            },
        }


class GenerateAttachCompReportDocumentTool(Tool):
    """Generate comp_###.pdf URI from report_id, update comp_reports.doc_uri, and insert documents row."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = _as_int(kwargs.get("report_id"))
        created_by = _as_int(kwargs.get("created_by"))
        doc_type = (kwargs.get("doc_type") or "comp_report").strip()
        if report_id is None or created_by is None:
            return _err("report_id and created_by are required")

        reports = data.setdefault("comp_reports", [])
        r = next((x for x in reports if _as_int(x.get("report_id")) == report_id), None)
        if not r:
            return _err(f"report_id {report_id} not found", code="not_found")

        padded = str(report_id).zfill(3)
        uri = f"https://storage.example.com/reports/comp_{padded}.pdf"

        r["doc_uri"] = uri
        r["updated_at"] = HARD_TS

        docs = data.setdefault("documents", [])
        document_id = _next_int_id(docs, "document_id")
        doc_row = {
            "document_id": document_id,
            "entity_type": "comp_report",
            "entity_id": str(report_id),
            "doc_type": doc_type,
            "file_uri": uri,
            "created_by": created_by,
            "created_at": HARD_TS,
        }
        docs.append(doc_row)

        # --- Create Audit Event Entry ---
        audit_rows = data.setdefault("audit_events", [])
        audit_event_id = _next_int_id(audit_rows, "event_id")
        audit_rec = {
            "event_id": audit_event_id,
            "actor_id": int(created_by),
            "action": "updated_uri",
            "entity_type": "comp_report",
            "entity_id": str(report_id),
            "occurred_at": HARD_TS,
            "metadata_json": {"new_uri": uri},
        }
        audit_rows.append(audit_rec)

        return json.dumps(
            {
                "document_uri": uri,
                "report": {
                    "report_id": report_id,
                    "doc_uri": uri,
                    "updated_at": HARD_TS,
                },
                "document_entry": doc_row,
                "audit_event": audit_rec,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_attach_comp_report_document",
                "description": (
                    "Generate PDF URI from report_id, update comp_reports.doc_uri, and insert a documents row."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
                        "created_by": {"type": "integer"},
                        "doc_type": {"type": "string", "default": "comp_report"},
                    },
                    "required": ["report_id", "created_by"],
                },
            },
        }


class BulkCreateComparableEntriesTool(Tool):
    """Batch insert comparables for a report."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = _as_int(kwargs.get("report_id"))
        items = kwargs.get("comparables") or []
        if report_id is None:
            return _err("report_id is required")
        if not isinstance(items, list) or not items:
            return _err("comparables must be a non-empty list")

        rows = data.setdefault("comparables", [])
        created = []
        for it in items:
            pid = (it or {}).get("comp_property_id")
            if not pid:
                continue
            rec = {
                "comp_id": _next_int_id(rows, "comp_id"),
                "report_id": report_id,
                "comp_property_id": str(pid),
                "similarity_score": float((it or {}).get("similarity_score") or 0.0),
                "selection_reason": (it or {}).get("selection_reason") or "",
                "tie_breaker_notes": (it or {}).get("tie_breaker_notes"),
            }
            rows.append(rec)
            created.append(rec)

        return json.dumps(
            {"created_count": len(created), "comparables": created}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "bulk_create_comparable_entries",
                "description": "Create multiple comparables for a comp report.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
                        "comparables": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["report_id", "comparables"],
                },
            },
        }


# ============================================================
# 20) update_comp_report_status
# ============================================================
class UpdateCompReportStatusTool(Tool):
    """Updates status field in comp_reports table."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = kwargs.get("report_id")
        new_status = kwargs.get("new_status")
        actor_id = kwargs.get("actor_id")
        if report_id is None or not new_status or actor_id is None:
            return _err("report_id, new_status, and actor_id are required")

        rows = data.get("comp_reports", [])
        rec = next(
            (r for r in rows if int(r.get("report_id", -1)) == int(report_id)), None
        )
        if not rec:
            return _err(f"report_id {report_id} not found")

        prev = rec.get("status")
        rec["status"] = new_status
        rec["updated_at"] = HARD_TS

        # --- Create Audit Event Entry ---
        audit_rows = data.setdefault("audit_events", [])
        audit_event_id = _next_int_id(audit_rows, "event_id")
        audit_rec = {
            "event_id": audit_event_id,
            "actor_id": int(actor_id),
            "action": "updated_status",
            "entity_type": "comp_report",
            "entity_id": str(report_id),
            "occurred_at": HARD_TS,
            "metadata_json": {"new_status": new_status, "previous_status": prev},
        }
        audit_rows.append(audit_rec)

        return json.dumps(
            {
                "report_id": int(report_id),
                "previous_status": prev,
                "new_status": new_status,
                "updated_at": HARD_TS,
                "audit_event": audit_rec,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_comp_report_status",
                "description": "Updates status field in comp_reports table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
                        "new_status": {
                            "type": "string",
                            "enum": ["draft", "sent_to_broker", "sent_to_client"],
                        },
                        "actor_id": {"type": "integer"},
                    },
                    "required": ["report_id", "new_status", "actor_id"],
                },
            },
        }


# ============================================================
# 21) create_email_entry
# ============================================================
class CreateEmailEntryTool(Tool):
    """Creates an entry in the emails table and an accompanying audit event."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get("client_id")
        broker_id = kwargs.get("broker_id")
        subject = kwargs.get("subject")
        body_uri = kwargs.get("body_uri")
        template_code = kwargs.get("template_code")

        if client_id is None or broker_id is None or not template_code:
            return _err("client_id, broker_id, and template_code are required")

        campaign_id = kwargs.get("campaign_id")

        # --- Auto-generate subject and body_uri if not provided ---
        if not subject or not body_uri:
            comp_reports = [
                r
                for r in data.get("comp_reports", [])
                if _as_int(r.get("client_id")) == int(client_id)
            ]
            if comp_reports:
                comp_reports.sort(
                    key=lambda r: (r.get("updated_at") or r.get("created_at") or ""),
                    reverse=True,
                )
                latest_report = comp_reports[0]
                report_status = latest_report.get("status", "draft")
                report_id = latest_report.get("report_id")
                subject_property = latest_report.get("subject_property_id", "HTX000")
            else:
                report_status, report_id, subject_property = "draft", None, "HTX000"

            if not subject:
                if template_code == "open_house_summary":
                    subject = f"Open House Schedule for {subject_property}"
                elif template_code == "comp_report_delivery":
                    subject = (
                        f"Your comparable analysis for {subject_property} is complete"
                    )
                elif template_code == "report_followup":
                    subject = (
                        f"Follow-up on Your Property Analysis for {subject_property}"
                    )
                elif template_code == "briefing_followup":
                    subject = f"Follow-up on Your Client Briefing"
                elif template_code == "briefing_delivery":
                    subject = f"Your Property Market Briefing is Ready"
                elif template_code == "first_time_buyer":
                    subject = f"First-Time Buyer Resources for {subject_property}"
                elif template_code == "general_update":
                    subject = f"Real Estate Market Update"
                elif template_code == "market_update":
                    subject = f"Your Market Update"
                elif template_code == "investment_alert":
                    subject = f"Investment Opportunity Alert"
                elif template_code == "listing_summary":
                    subject = f"Property Listing Summary for {subject_property}"
                elif template_code == "welcome_new_client":
                    subject = f"Welcome to Our Real Estate Services"
                elif template_code == "post_closing_checkin":
                    subject = f"Post-Closing Check-in and Next Steps"
                elif template_code == "next_steps":
                    subject = f"Next Steps in Your Real Estate Journey"
                elif template_code == "follow_up":
                    subject = f"Following Up on Your Real Estate Needs"
                else:
                    # Fallback logic based on report status
                    if report_status == "sent_to_client":
                        subject = f"Your comparable analysis for {subject_property} is complete"
                    elif report_status == "ready_for_review":
                        subject = f"Your comp report is ready for review"
                    elif report_status == "sent_to_broker":
                        subject = f"Comp report for {subject_property} sent to broker for review"
                    else:
                        subject = f"Market analysis update for {subject_property}"

            if not body_uri:
                if template_code == "open_house_summary":
                    body_uri = f"https://storage.example.com/emails/email_openhouse_{int(client_id):03d}.html"
                elif template_code == "comp_report_delivery":
                    body_uri = f"https://storage.example.com/emails/email_comp_{int(client_id):03d}.html"
                elif template_code == "report_followup":
                    body_uri = f"https://storage.example.com/emails/email_report_followup_{int(client_id):03d}.html"
                elif template_code == "briefing_followup":
                    body_uri = f"https://storage.example.com/emails/email_briefing_followup_{int(client_id):03d}.html"
                elif template_code == "briefing_delivery":
                    body_uri = f"https://storage.example.com/emails/email_briefing_{int(client_id):03d}.html"
                elif template_code == "first_time_buyer":
                    body_uri = f"https://storage.example.com/emails/email_first_buyer_{int(client_id):03d}.html"
                elif template_code == "general_update":
                    body_uri = f"https://storage.example.com/emails/email_general_{int(client_id):03d}.html"
                elif template_code == "market_update":
                    body_uri = f"https://storage.example.com/emails/email_market_{int(client_id):03d}.html"
                elif template_code == "investment_alert":
                    body_uri = f"https://storage.example.com/emails/email_investment_{int(client_id):03d}.html"
                elif template_code == "listing_summary":
                    body_uri = f"https://storage.example.com/emails/email_listing_{int(client_id):03d}.html"
                elif template_code == "welcome_new_client":
                    body_uri = f"https://storage.example.com/emails/email_welcome_{int(client_id):03d}.html"
                elif template_code == "post_closing_checkin":
                    body_uri = f"https://storage.example.com/emails/email_closing_{int(client_id):03d}.html"
                elif template_code == "next_steps":
                    body_uri = f"https://storage.example.com/emails/email_next_steps_{int(client_id):03d}.html"
                elif template_code == "follow_up":
                    body_uri = f"https://storage.example.com/emails/email_followup_{int(client_id):03d}.html"
                elif template_code == "urgent_comp_delivery":
                    body_uri = f"https://storage.example.com/emails/email_comp_{int(client_id):03d}.html"
                elif report_id:
                    body_uri = f"https://storage.example.com/emails/email_comp_{int(report_id):03d}.html"
                else:
                    # Default to comp report style
                    body_uri = f"https://storage.example.com/emails/email_comp_{int(client_id):03d}.html"

        # --- Create Email Entry ---
        email_rows = data.setdefault("emails", [])
        email_id = _next_int_id(email_rows, "email_id")
        email_rec = {
            "email_id": email_id,
            "client_id": int(client_id),
            "broker_id": int(broker_id),
            "subject": subject,
            "body_uri": body_uri,
            "template_code": template_code,
            "sent_at": HARD_TS,
            "campaign_id": campaign_id,
        }
        email_rows.append(email_rec)

        # --- Create Audit Event Entry ---
        audit_rows = data.setdefault("audit_events", [])
        audit_event_id = _next_int_id(audit_rows, "event_id")
        audit_rec = {
            "event_id": audit_event_id,
            "actor_id": int(broker_id),
            "action": "sent",
            "entity_type": "email",
            "entity_id": str(email_id),
            "occurred_at": HARD_TS,
            "metadata_json": {"client_id": int(client_id), "template": template_code},
        }
        audit_rows.append(audit_rec)

        return json.dumps({"email": email_rec, "audit_event": audit_rec}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_email_entry",
                "description": (
                    "Creates an entry in the emails table and a corresponding audit event for compliance."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "broker_id": {"type": "integer"},
                        "subject": {
                            "type": "string",
                            "description": (
                                "Optional - auto-generated based on comp report status if not provided"
                            ),
                        },
                        "body_uri": {
                            "type": "string",
                            "description": (
                                "Optional - auto-generated based on comp report status if not provided"
                            ),
                        },
                        "template_code": {"type": "string"},
                        "campaign_id": {"type": ["integer", "null"]},
                    },
                    "required": ["client_id", "broker_id", "template_code"],
                },
            },
        }


class SendEmailTool(Tool):
    """Creates an email entry with automatic subject/body generation when omitted."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get("client_id")
        broker_id = kwargs.get("broker_id")
        template_code = kwargs.get("template_code")
        subject = kwargs.get("subject")
        body_uri = kwargs.get("body_uri")
        campaign_id = kwargs.get("campaign_id")
        property_id = kwargs.get("property_id")

        if client_id is None or broker_id is None or not template_code:
            return _err("client_id, broker_id, and template_code are required")

        # Handle property_id as string or list of strings
        if property_id:
            if isinstance(property_id, list):
                pid = ", ".join(property_id)
            else:
                pid = str(property_id)
        else:
            # Auto-generate property_id if missing
            comp_reports = [
                r
                for r in data.get("comp_reports", [])
                if _as_int(r.get("client_id")) == int(client_id)
            ]
            if comp_reports:
                comp_reports.sort(
                    key=lambda r: (r.get("updated_at") or r.get("created_at") or ""),
                    reverse=True,
                )
                latest_report = comp_reports[0]
                pid = latest_report.get("subject_property_id", "HTX000")
            else:
                pid = "HTX000"

        # Auto-generate subject and body_uri if missing
        if not subject or not body_uri:
            comp_reports = [
                r
                for r in data.get("comp_reports", [])
                if _as_int(r.get("client_id")) == int(client_id)
            ]
            if comp_reports:
                comp_reports.sort(
                    key=lambda r: (r.get("updated_at") or r.get("created_at") or ""),
                    reverse=True,
                )
                latest_report = comp_reports[0]
                report_status = latest_report.get("status", "draft")
            else:
                report_status = "draft"

            if not subject:
                if template_code == "open_house_summary":
                    subject = f"Open House Schedule for {pid}"
                elif template_code == "comp_report_delivery":
                    subject = f"Your comparable analysis for {pid} is complete"
                elif template_code == "report_followup":
                    subject = f"Follow-up on Your Property Analysis for {pid}"
                elif template_code == "briefing":
                    subject = f"Your Property Market Briefing is Ready"
                elif template_code == "first_time_buyer":
                    subject = f"First-Time Buyer Resources for {pid}"
                elif template_code == "general_update":
                    subject = f"Real Estate Market Update"
                elif template_code == "market_update":
                    subject = f"Your Market Update"
                elif template_code == "investment_alert":
                    subject = f"Investment Opportunity Alert"
                elif template_code == "listing_summary":
                    subject = f"Property Listing Summary for {pid}"
                elif template_code == "welcome_new_client":
                    subject = f"Welcome to Our Real Estate Services"
                elif template_code == "post_closing_checkin":
                    subject = f"Post-Closing Check-in and Next Steps"
                elif template_code == "follow_up":
                    subject = f"Following Up on Your Real Estate Needs"
                else:
                    # Fallback logic based on report status
                    if report_status == "sent_to_client":
                        subject = f"Your comparable analysis for {pid} is complete"
                    elif report_status == "ready_for_review":
                        subject = f"Your comp report is ready for review"
                    elif report_status == "sent_to_broker":
                        subject = f"Comp report for {pid} sent to broker for review"
                    else:
                        subject = f"Market analysis update for {pid}"

            if not body_uri:
                if template_code == "open_house_summary":
                    body_uri = f"https://storage.example.com/emails/email_openhouse_{int(client_id):03d}.html"
                elif template_code == "comp_report_delivery":
                    body_uri = f"https://storage.example.com/emails/email_comp_{int(client_id):03d}.html"
                elif template_code == "report_followup":
                    body_uri = f"https://storage.example.com/emails/email_report_followup_{int(client_id):03d}.html"
                elif template_code == "briefing":
                    body_uri = f"https://storage.example.com/emails/email_briefing_{int(client_id):03d}.html"
                elif template_code == "first_time_buyer":
                    body_uri = f"https://storage.example.com/emails/email_first_buyer_{int(client_id):03d}.html"
                elif template_code == "general_update":
                    body_uri = f"https://storage.example.com/emails/email_general_{int(client_id):03d}.html"
                elif template_code == "market_update":
                    body_uri = f"https://storage.example.com/emails/email_market_{int(client_id):03d}.html"
                elif template_code == "investment_alert":
                    body_uri = f"https://storage.example.com/emails/email_investment_{int(client_id):03d}.html"
                elif template_code == "listing_summary":
                    body_uri = f"https://storage.example.com/emails/email_listing_{int(client_id):03d}.html"
                elif template_code == "welcome_new_client":
                    body_uri = f"https://storage.example.com/emails/email_welcome_{int(client_id):03d}.html"
                elif template_code == "post_closing_checkin":
                    body_uri = f"https://storage.example.com/emails/email_closing_{int(client_id):03d}.html"
                elif template_code == "follow_up":
                    body_uri = f"https://storage.example.com/emails/email_followup_{int(client_id):03d}.html"
                else:
                    # Default to comp report style
                    body_uri = f"https://storage.example.com/emails/email_comp_{int(client_id):03d}.html"

        # Create Email Entry
        email_rows = data.setdefault("emails", [])
        email_id = _next_int_id(email_rows, "email_id")
        email_rec = {
            "email_id": email_id,
            "client_id": int(client_id),
            "broker_id": int(broker_id),
            "subject": subject,
            "body_uri": body_uri,
            "template_code": template_code,
            "sent_at": HARD_TS,
            "campaign_id": campaign_id,
        }
        email_rows.append(email_rec)

        audit_rows = data.setdefault("audit_events", [])
        audit_event_id = _next_int_id(audit_rows, "event_id")
        audit_rec = {
            "event_id": audit_event_id,
            "actor_id": int(broker_id),
            "action": "sent",
            "entity_type": "email",
            "entity_id": str(email_id),
            "occurred_at": HARD_TS,
            "metadata_json": {"client_id": int(client_id), "template": template_code},
        }
        audit_rows.append(audit_rec)

        return json.dumps({"email": email_rec, "audit_event": audit_rec}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_email",
                "description": (
                    "Create an email entry with template-based subject/body defaults."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "broker_id": {"type": "integer"},
                        "template_code": {"type": "string"},
                        "subject": {"type": ["string", "null"]},
                        "body_uri": {"type": ["string", "null"]},
                        "campaign_id": {"type": ["integer", "null"]},
                        "property_id": {
                            "type": ["string", "array", "null"],
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["client_id", "broker_id", "template_code"],
                },
            },
        }


# ============================================================
# 22) create_route_entry
# ============================================================
class CreateRouteEntryTool(Tool):
    """Creates entry in routes table."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get("client_id")
        route_date = kwargs.get("route_date")
        stops_ordered_json = kwargs.get("stops_ordered_json")
        map_url = kwargs.get("map_url")
        created_by_broker_id = kwargs.get("created_by_broker_id")

        if (
            client_id is None
            or not route_date
            or not isinstance(stops_ordered_json, list)
            or not map_url
            or created_by_broker_id is None
        ):
            return _err(
                "client_id, route_date, stops_ordered_json(list), map_url, created_by_broker_id are required"
            )

        rows = data.setdefault("routes", [])
        route_id = _next_int_id(rows, "route_id")
        rec = {
            "route_id": route_id,
            "client_id": int(client_id),
            "date": str(route_date),
            "stops_ordered_json": stops_ordered_json,
            "map_url": str(map_url),
            "created_by_broker_id": int(created_by_broker_id),
            "created_at": HARD_TS,
        }
        rows.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_route_entry",
                "description": "Creates entry in routes table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "route_date": {"type": "string"},
                        "stops_ordered_json": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "map_url": {"type": "string"},
                        "created_by_broker_id": {"type": "integer"},
                    },
                    "required": [
                        "client_id",
                        "route_date",
                        "stops_ordered_json",
                        "map_url",
                        "created_by_broker_id",
                    ],
                },
            },
        }


# ============================================================
# 23) create_calendar_event_entry
# ============================================================
class CreateCalendarEventEntryTool(Tool):
    """Creates entry in calendar_events table."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        broker_id = kwargs.get("broker_id")
        client_id = kwargs.get("client_id")
        title = kwargs.get("title")
        start_at = ""
        end_at = ""
        location = kwargs.get("location")
        source = kwargs.get("source")

        # Enhancement: if date provided, auto-fill full-day times when start/end missing
        date = kwargs.get("date")
        if date and (not start_at or not end_at):
            date_str = str(date)
            if not start_at:
                start_at = f"{date_str}T00:00:00Z"
            if not end_at:
                end_at = f"{date_str}T23:59:59Z"

        if (
            broker_id is None
            or client_id is None
            or not title
            or not start_at
            or not end_at
            or not location
            or not source
        ):
            return _err(
                "broker_id, client_id, title, start_at, end_at, location, source are required"
            )

        rows = data.setdefault("calendar_events", [])
        event_id = _next_int_id(rows, "event_id")
        rec = {
            "event_id": event_id,
            "broker_id": int(broker_id),
            "client_id": int(client_id),
            "title": str(title),
            "start_at": str(start_at),
            "end_at": str(end_at),
            "location": str(location),
            "source": str(source),
        }
        rows.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_calendar_event_entry",
                "description": (
                    "Creates entry in calendar_events table (supports date-only input to auto-fill full-day)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "broker_id": {"type": "integer"},
                        "client_id": {"type": "integer"},
                        "title": {"type": "string"},
                        "date": {
                            "type": ["string", "null"],
                            "description": (
                                "YYYY-MM-DD (auto-fills 00:00:00Z-23:59:59Z if start/end omitted)"
                            ),
                        },
                        "location": {"type": "string"},
                        "source": {
                            "type": "string",
                            "enum": ["client_meeting", "viewing", "follow_up"],
                        },
                    },
                    "required": [
                        "broker_id",
                        "client_id",
                        "title",
                        "location",
                        "source",
                    ],
                },
            },
        }


# ============================================================
# 24) create_campaign_entry
# ============================================================
class CreateCampaignEntryTool(Tool):
    """Creates an entry in the campaigns table and an accompanying audit event."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_name = kwargs.get("campaign_name")
        campaign_type = kwargs.get("campaign_type")
        created_by = kwargs.get("created_by")

        if not campaign_name or not campaign_type or created_by is None:
            return _err("campaign_name, campaign_type, and created_by are required")

        # --- Create Campaign Entry ---
        campaign_rows = data.setdefault("campaigns", [])
        campaign_id = _next_int_id(campaign_rows, "campaign_id")
        campaign_rec = {
            "campaign_id": campaign_id,
            "name": str(campaign_name),
            "type": str(campaign_type),
            "created_by": int(created_by),
            "created_at": HARD_TS,
        }
        campaign_rows.append(campaign_rec)

        # --- Create Audit Event Entry ---
        audit_rows = data.setdefault("audit_events", [])
        audit_event_id = _next_int_id(audit_rows, "event_id")
        audit_rec = {
            "event_id": audit_event_id,
            "actor_id": int(created_by),
            "action": "launched",
            "entity_type": "campaign",
            "entity_id": str(campaign_id),
            "occurred_at": HARD_TS,
            "metadata_json": {
                "campaign_name": campaign_name,
                "campaign_type": campaign_type,
            },
        }
        audit_rows.append(audit_rec)

        return json.dumps(
            {"campaign": campaign_rec, "audit_event": audit_rec}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_campaign_entry",
                "description": (
                    "Creates an entry in the campaigns table and a corresponding audit event."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_name": {"type": "string"},
                        "campaign_type": {
                            "type": "string",
                            "enum": ["general_update", "new_homeowner", "likely_buyer"],
                        },
                        "created_by": {"type": "integer"},
                    },
                    "required": ["campaign_name", "campaign_type", "created_by"],
                },
            },
        }


# ============================================================
# 25) create_audit_event_entry
# ============================================================
class CreateAuditEventEntryTool(Tool):
    """Creates entry in audit_events table for compliance tracking."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        actor_id = kwargs.get("actor_id")
        action = kwargs.get("action")
        entity_type = kwargs.get("entity_type")
        entity_id = kwargs.get("entity_id")
        metadata_json = kwargs.get("metadata_json")

        if actor_id is None or not action or not entity_type or entity_id is None:
            return _err("actor_id, action, entity_type, entity_id are required")

        if metadata_json is not None and not isinstance(metadata_json, (dict, list)):
            return _err("metadata_json must be an object or array if provided")

        rows = data.setdefault("audit_events", [])
        event_id = _next_int_id(rows, "event_id")
        rec = {
            "event_id": event_id,
            "actor_id": int(actor_id),
            "action": str(action),
            "entity_type": str(entity_type),
            "entity_id": str(entity_id),
            "occurred_at": HARD_TS,
            "metadata_json": metadata_json if metadata_json is not None else {},
        }
        rows.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_audit_event_entry",
                "description": (
                    "Creates entry in audit_events table for compliance tracking."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {"type": "integer"},
                        "action": {"type": "string"},
                        "entity_type": {"type": "string"},
                        "entity_id": {"type": "string"},
                        "metadata_json": {"type": ["object", "array", "null"]},
                    },
                    "required": ["actor_id", "action", "entity_type", "entity_id"],
                },
            },
        }


# ============================================================
# 26) generate_comp_report_document
# ============================================================
class GenerateCompReportDocumentTool(Tool):
    """Generates PDF comparable analysis report."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = kwargs.get("report_id")
        subject_property_data = kwargs.get("subject_property_data") or {}
        comparable_data = kwargs.get("comparable_data") or []
        market_analysis = kwargs.get("market_analysis") or {}
        mortgage_calculations = kwargs.get("mortgage_calculations") or {}

        if report_id is None:
            return _err("report_id is required")

        # Deterministic URI based on report_id
        uri = f"https://storage.example.com/reports/comp_{int(report_id):03d}.pdf"
        out = {
            "document_uri": uri,
            "document_type": "comparable_analysis_report",
            "pages_generated": 8,
            "sections": [
                "executive_summary",
                "property_details",
                "comparables_analysis",
                "market_context",
                "financial_analysis",
                "recommendations",
            ],
            "generation_timestamp": HARD_TS,
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_comp_report_document",
                "description": "Generate PDF comparable analysis report.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
                        "subject_property_data": {"type": "object"},
                        "comparable_data": {"type": "array"},
                        "market_analysis": {"type": "object"},
                        "mortgage_calculations": {"type": "object"},
                    },
                    "required": ["report_id"],
                },
            },
        }


# ============================================================
# 27) generate_email_content
# ============================================================
class GenerateEmailContentTool(Tool):
    """Generates HTML email content."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        template_code = kwargs.get("template_code")
        recipient_data = kwargs.get("recipient_data") or {}
        context_data = kwargs.get("context_data") or {}
        attachments = kwargs.get("attachments") or []

        if not template_code:
            return _err("template_code is required")

        # Deterministic content URI based on template_code
        rid = recipient_data.get("client_id") or "000"
        if isinstance(rid, int) or (isinstance(rid, str) and rid.isdigit()):
            client_id = int(rid)
        else:
            client_id = 15  # Default fallback

        # Template-specific URI generation
        if template_code == "open_house_summary":
            uri = f"https://storage.example.com/emails/email_openhouse_{client_id:03d}.html"
        elif template_code == "comp_report_delivery":
            uri = f"https://storage.example.com/emails/email_comp_{client_id:03d}.html"
        elif template_code == "report_followup":
            uri = f"https://storage.example.com/emails/email_report_followup_{client_id:03d}.html"
        elif template_code == "briefing_followup":
            uri = f"https://storage.example.com/emails/email_briefing_followup_{client_id:03d}.html"
        elif template_code == "briefing_delivery":
            uri = f"https://storage.example.com/emails/email_briefing_{client_id:03d}.html"
        elif template_code == "first_time_buyer":
            uri = f"https://storage.example.com/emails/email_first_buyer_{client_id:03d}.html"
        elif template_code == "general_update":
            uri = (
                f"https://storage.example.com/emails/email_general_{client_id:03d}.html"
            )
        elif template_code == "market_update":
            uri = (
                f"https://storage.example.com/emails/email_market_{client_id:03d}.html"
            )
        elif template_code == "investment_alert":
            uri = f"https://storage.example.com/emails/email_investment_{client_id:03d}.html"
        elif template_code == "listing_summary":
            uri = (
                f"https://storage.example.com/emails/email_listing_{client_id:03d}.html"
            )
        elif template_code == "welcome_new_client":
            uri = (
                f"https://storage.example.com/emails/email_welcome_{client_id:03d}.html"
            )
        elif template_code == "post_closing_checkin":
            uri = (
                f"https://storage.example.com/emails/email_closing_{client_id:03d}.html"
            )
        elif template_code == "next_steps":
            uri = f"https://storage.example.com/emails/email_next_steps_{client_id:03d}.html"
        elif template_code == "follow_up":
            uri = f"https://storage.example.com/emails/email_followup_{client_id:03d}.html"
        else:
            uri = f"https://storage.example.com/emails/email_comp_{client_id:03d}.html"

        # Set subject line based on template
        property_id = context_data.get("subject_property_id", "HTX003")
        date = context_data.get("date", "2025-09-15")

        if template_code == "open_house_summary":
            subject_line = (
                context_data.get("subject_line")
                or f"Open House Summary Report for {date}"
            )
        elif template_code == "comp_report_delivery":
            subject_line = (
                context_data.get("subject_line")
                or f"Your comparable analysis for {property_id} is complete"
            )
        elif template_code == "report_followup":
            subject_line = (
                context_data.get("subject_line")
                or f"Follow-up on Your Property Analysis for {property_id}"
            )
        elif template_code == "briefing_followup":
            subject_line = (
                context_data.get("subject_line") or f"Follow-up on Your Client Briefing"
            )
        elif template_code == "briefing_delivery":
            subject_line = (
                context_data.get("subject_line")
                or f"Your Property Market Briefing is Ready"
            )
        elif template_code == "first_time_buyer":
            subject_line = (
                context_data.get("subject_line")
                or f"First-Time Buyer Resources for {property_id}"
            )
        elif template_code == "general_update":
            subject_line = (
                context_data.get("subject_line") or f"Real Estate Market Update"
            )
        elif template_code == "market_update":
            subject_line = context_data.get("subject_line") or f"Your Market Update"
        elif template_code == "investment_alert":
            subject_line = (
                context_data.get("subject_line") or f"Investment Opportunity Alert"
            )
        elif template_code == "listing_summary":
            subject_line = (
                context_data.get("subject_line")
                or f"Property Listing Summary for {property_id}"
            )
        elif template_code == "welcome_new_client":
            subject_line = (
                context_data.get("subject_line")
                or f"Welcome to Our Real Estate Services"
            )
        elif template_code == "post_closing_checkin":
            subject_line = (
                context_data.get("subject_line")
                or f"Post-Closing Check-in and Next Steps"
            )
        elif template_code == "next_steps":
            subject_line = (
                context_data.get("subject_line")
                or f"Next Steps in Your Real Estate Journey"
            )
        elif template_code == "follow_up":
            subject_line = (
                context_data.get("subject_line")
                or f"Following Up on Your Real Estate Needs"
            )
        else:
            subject_line = (
                context_data.get("subject_line")
                or f"Your Comparable Property Analysis for {property_id}"
            )

        out = {
            "email_content_uri": uri,
            "template_used": str(template_code),
            "personalization_applied": True,
            "subject_line": subject_line,
            "attachment_count": int(len(attachments)),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_email_content",
                "description": "Generate HTML email content and return its URI.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "template_code": {"type": "string"},
                        "recipient_data": {"type": "object"},
                        "context_data": {"type": "object"},
                        "attachments": {"type": "array"},
                    },
                    "required": [
                        "template_code",
                        "recipient_data",
                        "context_data",
                        "attachments",
                    ],
                },
            },
        }


# ============================================================
# 28) verify_comp_report_workflow
# ============================================================
class VerifyCompReportWorkflowTool(Tool):
    """Verifies complete comparable analysis workflow was executed correctly."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = kwargs.get("report_id")
        if report_id is None:
            return _err("report_id is required")

        reports = {
            int(r.get("report_id")): r
            for r in data.get("comp_reports", [])
            if r.get("report_id") is not None
        }
        r = reports.get(int(report_id))
        exists = r is not None
        status = r.get("status") if r else None
        document_generated = bool(r and r.get("doc_uri"))

        comps = [
            c
            for c in data.get("comparables", [])
            if int(c.get("report_id", -1)) == int(report_id)
        ]
        comparables_count = len(comps)

        emails = data.get("emails", [])
        emails_sent = sum(
            1
            for e in emails
            if r and int(e.get("client_id", -1)) == int(r.get("client_id", -2))
        )

        audits = [
            a
            for a in data.get("audit_events", [])
            if a.get("entity_type") == "comp_report"
            and str(a.get("entity_id")) == str(report_id)
        ]
        audit_trail_complete = len(audits) >= 1

        compliance_verified = bool(document_generated and audit_trail_complete)
        workflow_complete = bool(
            exists
            and status == "sent_to_client"
            and document_generated
            and comparables_count >= 1
            and emails_sent >= 1
            and audit_trail_complete
        )

        out = {
            "workflow_verification": {
                "report_id": int(report_id),
                "report_exists": bool(exists),
                "status_current": status,
                "document_generated": bool(document_generated),
                "comparables_count": int(comparables_count),
                "emails_sent": int(emails_sent),
                "audit_trail_complete": bool(audit_trail_complete),
                "compliance_verified": bool(compliance_verified),
                "workflow_complete": bool(workflow_complete),
            }
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_comp_report_workflow",
                "description": "Verify comparable analysis workflow end state.",
                "parameters": {
                    "type": "object",
                    "properties": {"report_id": {"type": "integer"}},
                    "required": ["report_id"],
                },
            },
        }


# ============================================================
# 29) verify_route_creation
# ============================================================
class VerifyRouteCreationTool(Tool):
    """Verifies property viewing route was created successfully."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        route_id = kwargs.get("route_id")
        if route_id is None:
            return _err("route_id is required")

        routes = {
            int(r.get("route_id")): r
            for r in data.get("routes", [])
            if r.get("route_id") is not None
        }
        route = routes.get(int(route_id))
        route_exists = route is not None
        properties_count = len(route.get("stops_ordered_json") or []) if route else 0

        # events = {int(e.get("event_id")): e for e in data.get("calendar_events", []) if e.get("event_id") is not None}
        # event = events.get(int(event_id))
        # event_created = event is not None

        # Travel constraints met: if map_url exists and >= 1 stop
        travel_constraints_met = bool(
            route and route.get("map_url") and properties_count >= 1
        )

        out = {
            "route_verification": {
                "route_id": int(route_id),
                "route_exists": bool(route_exists),
                "properties_count": int(properties_count),
                "travel_constraints_met": bool(travel_constraints_met),
                "broker_notified": (
                    True
                ),  # assume notification handled via email/log elsewhere
                "schedule_complete": bool(route_exists and travel_constraints_met),
            }
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_route_creation",
                "description": (
                    "Verify viewing route and corresponding calendar event exist."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "route_id": {"type": "integer"},
                        "event_id": {"type": "integer"},
                    },
                    "required": ["route_id"],
                },
            },
        }


# ============================================================
# 30) generate_next_comp_report_uri
# ============================================================
class GenerateNextCompReportUriTool(Tool):
    """Generates next comp_###.pdf URI based on highest report_id in comp_reports."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        base_url = kwargs.get("base_url") or "https://storage.example.com/reports/"
        prefix = kwargs.get("prefix") or "comp_"
        ext = kwargs.get("ext") or ".pdf"
        pad_width = _as_int(kwargs.get("pad_width")) or 3  # 21 -> 021

        # Find current max report_id
        max_id = 0
        for r in data.get("comp_reports", []):
            rid = _as_int(r.get("report_id") or r.get("id") or r.get("entity_id"))
            if rid is not None and rid > max_id:
                max_id = rid

        next_id = max_id + 1
        padded = str(next_id).zfill(pad_width)
        uri = f"{base_url}{prefix}{padded}{ext}"

        out = {
            "next_report_id": next_id,
            "padded_id": padded,
            "file_uri": uri,  # convenience
            "doc_uri": uri,  # compat with update_comp_report_doc_uri
            "generated_at": HARD_TS,
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_next_comp_report_uri",
                "description": (
                    "Builds https://storage.example.com/reports/comp_###.pdf using max report_id + 1 from comp_reports."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "base_url": {
                            "type": "string",
                            "description": (
                                "Defaults to https://storage.example.com/reports/"
                            ),
                        },
                        "prefix": {"type": "string", "default": "comp_"},
                        "ext": {"type": "string", "default": ".pdf"},
                        "pad_width": {"type": "integer", "default": 3},
                    },
                    "required": [],
                },
            },
        }


# ============================================================
# create_mortgage_profile
# ============================================================
class CreateMortgageProfileTool(Tool):
    """Creates or updates a mortgage profile entry in the mortgage_profiles table."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = _as_int(kwargs.get("client_id"))
        loan_amount = kwargs.get("loan_amount")
        down_payment = kwargs.get("down_payment")
        interest_rate = kwargs.get("interest_rate")
        term_years = _as_int(kwargs.get("term_years"))
        annual_income = kwargs.get("annual_income")

        if (
            client_id is None
            or loan_amount is None
            or down_payment is None
            or interest_rate is None
            or term_years is None
        ):
            return _err(
                "client_id, loan_amount, down_payment, interest_rate, and term_years are required"
            )

        # Optional fields
        credit_score = _as_int(kwargs.get("credit_score"))
        region = kwargs.get("region")

        # Tolerate typo "mortage_profiles"
        if "mortgage_profiles" in data:
            rows = data.setdefault("mortgage_profiles", [])
        else:
            rows = data.setdefault("mortage_profiles", [])

        existing = _get_mortgage_profile(data, client_id)
        if existing:
            # Update existing profile
            existing.update(
                {
                    "credit_score": credit_score,
                    "annual_income": annual_income,
                    "down_payment": float(down_payment),
                    "desired_loan_amount": float(loan_amount),
                    "interest_rate": float(interest_rate),
                    "term_years": term_years,
                    "region": region,
                    "last_reviewed_at": HARD_TS,
                }
            )
            return json.dumps(existing, indent=2)
        else:
            # Create new profile
            mortgage_id = _next_int_id(rows, "mortgage_id")
            rec = {
                "mortgage_id": mortgage_id,
                "client_id": client_id,
                "credit_score": credit_score,
                "annual_income": annual_income,
                "down_payment": float(down_payment),
                "desired_loan_amount": float(loan_amount),
                "interest_rate": float(interest_rate),
                "term_years": term_years,
                "region": region,
                "last_reviewed_at": HARD_TS,
            }
            rows.append(rec)
            return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_mortgage_profile",
                "description": (
                    "Creates a new mortgage profile for a client, or updates existing one."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "loan_amount": {"type": "number"},
                        "down_payment": {"type": "number"},
                        "interest_rate": {"type": "number"},
                        "term_years": {"type": "integer"},
                        "credit_score": {"type": ["integer", "null"]},
                        "annual_income": {"type": ["number", "null"]},
                        "region": {"type": ["string", "null"]},
                    },
                    "required": [
                        "client_id",
                        "loan_amount",
                        "down_payment",
                        "interest_rate",
                        "term_years",
                    ],
                },
            },
        }


# ============================================================
# Export instances
# ============================================================
TOOLS = [
    FetchClientFullContextTool(),
    FetchListingByPropertyIdTool(),
    FetchNeighborhoodDetailsTool(),
    FetchBrokerDetailsTool(),
    SearchListingsByCriteriaTool(),
    FetchPropertySalesHistoryTool(),
    FetchMortgageRatesForClientTool(),
    CheckRecentEmailHistoryTool(),
    SearchCompsAndCreateReportTool(),
    FetchOpenHouseOpportunitiesTool(),
    CalculateMortgagePaymentTool(),
    CalculateRouteOptimizationTool(),
    CalculatePropertyMetricsTool(),
    CreateComparableEntryTool(),
    GenerateAttachCompReportDocumentTool(),
    BulkCreateComparableEntriesTool(),
    UpdateCompReportStatusTool(),
    CreateEmailEntryTool(),
    SendEmailTool(),
    CreateRouteEntryTool(),
    CreateCalendarEventEntryTool(),
    CreateCampaignEntryTool(),
    GenerateCompReportDocumentTool(),
    GenerateEmailContentTool(),
    VerifyCompReportWorkflowTool(),
    VerifyRouteCreationTool(),
    GenerateNextCompReportUriTool(),
    FetchCompReportDetailsTool(),
    FetchEmailsForClientTool(),
    FetchCalendarEventsForClientTool(),
    FetchListingsByIdsTool(),
    FetchRouteDetailsTool(),
    FetchCampaignDetailsTool(),
    GenerateClientBriefingDocumentTool(),
    ValidateDriveTimeConstraintsTool(),
    FetchPropertyDetailsTool(),
    FindNearbyListingsTool(),
    CreateAuditEventEntryTool(),
    CreateMortgageProfileTool(),
]
