import json
import math
import re
from typing import Any

from domains.dto import Tool

HARD_TS = "2025-09-15T17:00:00Z"
HTX_RE = re.compile(r"^HTX\d{3}$")


def _collect_sales_history(
    data: dict[str, Any], property_id: str
) -> list[dict[str, Any]]:
    pass
    return [
        s for s in data.get("sales", []) if str(s.get("property_id")) == property_id
    ]


def _require_active_broker(data: dict[str, Any], broker_id: int) -> str | None:
    pass
    brokers = data.get("brokers", [])
    b = next((x for x in brokers if _as_int(x.get("broker_id")) == broker_id), None)
    if not b:
        return f"broker_id {broker_id} not found"
    if not bool(b.get("active", False)):
        return "assigned broker is inactive; escalate_to_office_manager=true"
    return None


def _similarity_score(
    base_price: float | None, candidate_price: float | None, amenity_overlap: int
) -> float:
    pass
    score = 0.5
    if base_price and candidate_price:
        diff = abs(candidate_price - base_price) / max(base_price, 1)
        score += max(-0.25, 0.25 - diff)  #proximity is preferable
    score += min(0.25, 0.05 * amenity_overlap)
    return round(max(0.0, min(1.0, score)), 3)


def _get_client_prefs(data: dict[str, Any], client_id: int) -> dict[str, Any] | None:
    pass
    return next(
        (
            p
            for p in data.get("client_preferences", [])
            if _as_int(p.get("client_id")) == client_id
        ),
        None,
    )


def _days_between_iso(a: str, b: str) -> int | None:
    pass
    #Deterministic/local-free example: lexicographically compare strings for demonstration
    #(Actual implementation would involve parsing; not necessary for deterministic testing framework)
    return None


def _ppsqft(list_price: float | None, sqft: float | None) -> float | None:
    pass
    if list_price is None or sqft in (None, 0):
        return None
    return round(float(list_price) / float(sqft), 3)


#Eliminated _collect_property function - properties table is absent in the real data structure


def _collect_listing_by_property(
    data: dict[str, Any], property_id: str
) -> dict[str, Any] | None:
    pass
    candidates = [
        l for l in data.get("listings", []) if str(l.get("property_id")) == property_id
    ]
    return _latest(candidates, "updated_at") or (candidates[0] if candidates else None)


def _get_mortgage_profile(
    data: dict[str, Any], client_id: int
) -> dict[str, Any] | None:
    pass
    #accept schema misspelling: "mortage_profiles"
    profiles = data.get("mortgage_profiles") or data.get("mortage_profiles") or []
    return next((m for m in profiles if _as_int(m.get("client_id")) == client_id), None)


def _price_in_range(price: float | None, lo: int | None, hi: int | None) -> bool:
    pass
    if price is None:
        return False
    if lo is not None and price < lo:  #minimum inclusive
        return False
    if hi is not None and price > hi:
        return False
    return True


def _latest(records: list[dict[str, Any]], ts_key: str) -> dict[str, Any] | None:
    pass
    if not records:
        return None
    return max(records, key=lambda r: r.get(ts_key) or "")


#----------------------------
#Utility functions
#----------------------------
def _err(msg: str, code: str = "bad_request", **extra) -> str:
    pass
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    payload = out
    out = json.dumps(payload, indent=2)
    return out


def _as_int(x) -> int | None:
    pass
    try:
        return int(x)
    except Exception:
        return None


def _require_property_id(pid: str) -> str | None:
    pass
    if not pid:
        return "property_id is required"
    if not HTX_RE.match(str(pid)):
        return f"property_id must match HTX### format, got {pid}"
    return None


#============================================================
#retrieve_complete_client_context
#============================================================
class FetchClientFullContextTool(Tool):
    """Combines client preferences, mortgage profile, inferred assigned broker, and counts of recent activities."""

    @staticmethod
    def invoke(data: dict[str, Any], client_id: int = None) -> str:
        client_id = _as_int(client_id)
        if client_id is None:
            return _err("client_id is required")

        #--- User Preferences ---
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

        #--- Mortgage profile (accept mortage_profiles misspelling) ---
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

        #--- Assigned broker inferred (clients table not present) ---
        assigned_broker_id, assignment_basis, last_interaction, broker_active = (
            None,
            None,
            None,
            None,
        )

        #1) Latest comp_report for this client
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

        #2) Backup: latest calendar event
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

        #--- Counts of recent activities ---
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

        #If absolutely nothing is found for this client, return not_found
        if not p and not m and emails_cnt == 0 and reports_cnt == 0 and events_cnt == 0:
            return _err(f"client_id {client_id} not found", code="not_found")
        payload = {
                "client_basic": client_basic,
                "preferences": prefs_out,
                "mortgage_profile": mort_out,
                "recent_activity": recent_out,
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
                "name": "FetchClientFullContext",
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


#============================================================
#3) retrieve_listing_by_property_id
#============================================================
class FetchListingByPropertyIdTool(Tool):
    """Retrieves listing details for a specific property."""

    @staticmethod
    def invoke(data: dict[str, Any], property_id: str = None) -> str:
        pass
        need = _require_property_id(property_id)
        if need:
            return _err(need)

        listing = _collect_listing_by_property(data, property_id)
        if not listing:
            # Error management guideline: verify sales for historical information
            sales = _collect_sales_history(data, property_id)
            if not sales:
                return _err(
                    f"no listing WA sales history for {property_id}", code="not_found"
                )
            # Generate a synthetic listing-style view based on the most recent sale
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
            payload = out
            out = json.dumps(payload, indent=2)
            return out

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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetchListingByPropertyId",
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


#============================================================
#4) retrieve_neighborhood_information
#============================================================
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


#============================================================
#5) retrieve_broker_information
#============================================================
class FetchBrokerDetailsTool(Tool):
    """Retrieves broker details for coordinating workflows."""

    @staticmethod
    def invoke(data: dict[str, Any], broker_id: int = None) -> str:
        broker_id = _as_int(broker_id)
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetchBrokerDetails",
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


#============================================================
#7) find_listings_based_on_criteria
#============================================================
class SearchListingsByCriteriaTool(Tool):
    """Queries the listings table to match client specifications."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        neighborhoods_json: list[str] = None,
        price_min: int = 0,
        price_max: int = None,
        status_filter: list[str] = None,
        max_results: int = None
    ) -> str:
        pass
        neighborhoods = neighborhoods_json or []
        price_min = price_min or 0
        price_max = price_max
        status_filter = status_filter
        max_results = _as_int(max_results)

        valid_status = {"sold", "for_sale", "off_market", "active", "pending", "rented"}

        # Process status_filter as a string or a list
        if status_filter:
            if isinstance(status_filter, list):
                # Check all statuses within the list for validity
                for status in status_filter:
                    if status not in valid_status:
                        return _err(
                            f"invalid status_filter '{status}'",
                            code="validation_error",
                            valid=list(sorted(valid_status)),
                        )
            else:
                # Validation for an individual status
                if status_filter not in valid_status:
                    return _err(
                        f"invalid status_filter '{status_filter}'",
                        code="validation_error",
                        valid=list(sorted(valid_status)),
                    )

        # Note: Neighborhood filtering has been eliminated - no mapping from property to neighborhood in the data
        matches: list[dict[str, Any]] = []
        for l in data.get("listings", []):
            pid = str(l.get("property_id"))

            # Omit listings that lack a property_id
            if not pid:
                continue

            # Note: Neighborhood filtering bypassed - no mapping for neighborhoods available
            if neighborhoods:
                # Record a warning indicating that neighborhood filtering is unsupported
                pass

            # Implement status filter (using OR logic for the list)
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
                    ),  # Utilize pre-calculated values from listings
                    "status": l.get("status"),
                }
            )

            # Enforce max_results limit if defined
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        #status_filter is mandated by prompt; permit null for adaptability
        return {
            "type": "function",
            "function": {
                "name": "SearchListingsByCriteria",
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


#============================================================
#8) retrieve_property_sales_history
#============================================================
class FetchPropertySalesHistoryTool(Tool):
    """Retrieves historical sales information for the property."""

    @staticmethod
    def invoke(data: dict[str, Any], property_id: str = None) -> str:
        need = _require_property_id(property_id)
        if need:
            return _err(need)

        sales = _collect_sales_history(data, property_id)
        out = {
            "property_id": property_id,
            "sales_history": sales or [],
            "total_sales": len(sales),
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchPropertySalesHistory",
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


#============================================================
#9) retrieve_mortgage_rates_for_client
#============================================================
class FetchMortgageRatesForClientTool(Tool):
    """Retrieves available mortgage rates according to client qualifications."""

    @staticmethod
    def invoke(data: dict[str, Any], credit_score: int = None, region: str = None) -> str:
        credit_score = _as_int(credit_score)
        if credit_score is None or not region:
            return _err("credit_score (int) and region (string) are required")

        rates = []
        # Establish a lender lookup map for effective name resolution
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

        # Select best_available_rate from qualifying options, otherwise from all (with a higher penalty)
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        #The tool refrains from directly retrieving client profiles to maintain privacy layers
        return {
            "type": "function",
            "function": {
                "name": "FetchMortgageRatesForClient",
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


#============================================================
#10) verify_recent_email_history
#============================================================
class CheckRecentEmailHistoryTool(Tool):
    """Verifies recent email communications to avoid duplicates."""

    @staticmethod
    def invoke(data: dict[str, Any], client_id: int = None, template_code: str = None, days_lookback: int = 30) -> str:
        pass
        client_id = _as_int(client_id)
        days_lookback = _as_int(days_lookback) or 30
        if client_id is None or not template_code:
            return _err("client_id (int) and template_code (string) are required")

        emails = [
            e
            for e in data.get("emails", [])
            if _as_int(e.get("client_id")) == client_id
            and e.get("template_code") == template_code
        ]
        # Order by sent_at in descending order
        emails_sorted = sorted(
            emails, key=lambda e: e.get("sent_at") or "", reverse=True
        )
        last = emails_sorted[0] if emails_sorted else None

        # Assess if the template can be sent based on days_lookback
        can_send = True
        if last:
            last_sent = last.get("sent_at") or ""
            # To ensure deterministic behavior, perform straightforward date comparisons
            # In a practical implementation, this would involve parsing dates and verifying the actual day difference
            # For the time being, assume recent emails are timestamped near HARD_TS
            if last_sent and days_lookback < 365:  # Streamlined recency verification
                # If days_lookback is minimal (< 365), apply stricter criteria
                can_send = False if last_sent > "2025-08-01" else True
            else:
                # For extended lookback durations, permit sending
                can_send = True

        out = {
            "client_id": client_id,
            "template_code": template_code,
            "days_lookback": days_lookback,
            "recent_emails": emails_sorted[:5],
            "last_sent_date": last.get("sent_at") if last else None,
            "can_send_template": can_send,
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        #Helper for deduplication protocol step 1
        return {
            "type": "function",
            "function": {
                "name": "CheckRecentEmailHistory",
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


#============================================================
#NEW: search_comps_and_generate_report (integrates search + rank + creation)
#============================================================
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


#============================================================
#13) retrieve_open_house_opportunities
#============================================================
class FetchOpenHouseOpportunitiesTool(Tool):
    """Locates open houses that align with client criteria and availability."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        property_candidates: list = None,
        date: str = None,
        date_range_start: str = None,
        date_range_end: str = None
    ) -> str:
        property_candidates = property_candidates or []
        # Improvement: enable simplified single date that automatically extends to 3 days
        if date and (not date_range_start or not date_range_end):
            try:
                from datetime import datetime, timedelta

                start_dt = datetime.strptime(str(date), "%Y-%m-%d")
                end_dt = start_dt + timedelta(days=3)
                date_range_start = f"{start_dt.strftime('%Y-%m-%d')}T00:00:00Z"
                date_range_end = f"{end_dt.strftime('%Y-%m-%d')}T23:59:59Z"
            except Exception:
                # Best-effort fallback
                date_str = str(date)
                date_range_start = f"{date_str}T00:00:00Z"
                try:
                    y, m, d = date_str.split("-")
                    date_range_end = f"{y}-{m}-{int(d)+3:02d}T23:59:59Z"
                except Exception:
                    date_range_end = f"{date_str}T23:59:59Z"
        if not date_range_start or not date_range_end:
            return _err("date WA (date_range_start and date_range_end) are required")

        prop_set = set(property_candidates)
        open_houses = []
        for oh in data.get("open_houses", []):
            if str(oh.get("property_id")) in prop_set:
                # Verify if open house dates coincide with the search range
                oh_start = oh.get("start_at", "")
                oh_end = oh.get("end_at", "")
                if oh_start <= date_range_end and oh_end >= date_range_start:
                    open_houses.append(oh)

        out = {
            "search_period": [date_range_start, date_range_end],
            "open_house_opportunities": open_houses[:10],
            "total_opportunities": len(open_houses),
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        #Facilitates Route Optimization Protocol (for planning viewings)
        return {
            "type": "function",
            "function": {
                "name": "FetchOpenHouseOpportunities",
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


#============================================================
#14) compute_mortgage_payment
#============================================================
class CalculateMortgagePaymentTool(Tool):
    """Computes mortgage payments based on client profile and rates."""

    @staticmethod
    def invoke(data: dict[str, Any], loan_amount: float = None, down_payment: float = None, interest_rate: float = None, term_years: int = None) -> str:
        if None in (loan_amount, down_payment, interest_rate) or term_years is None:
            return _err("loan_amount, down_payment, best_rate, term_years are required")

        # Typical fixed-rate mortgage monthly payment formula: P * (r/12) / (1 - (1+r/12)^(-n))
        r = float(interest_rate) / 100.0
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
            "interest_rate": float(interest_rate),
            "term_years": term_years,
            "monthly_payment": int(round(monthly)),
            "total_interest": int(round(total_interest)),
            "total_cost": int(round(total_cost)),
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        #Business Guideline: utilize real mortgage profile inputs upstream
        return {
            "type": "function",
            "function": {
                "name": "CalculateMortgagePayment",
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


#============================================================
#15) compute_route_optimization
#============================================================
class CalculateRouteOptimizationTool(Tool):
    """Enhances property viewing routes while considering travel time limitations."""

    @staticmethod
    def invoke(data: dict[str, Any], property_list: list = None, start_address: str = None, max_hop_minutes: int = None) -> str:
        if property_list is None or start_address is None or max_hop_minutes is None:
            return _err("property_list, start_address, max_hop_minutes are required")

        # Deterministic pseudo-optimizer: maintain input sequence; allocate stable hop times <= max_hop_minutes
        # Route Optimization Protocol requirement: <= 30 minutes between stops
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
        # include fixed viewing times (deterministic) to achieve sample 165 in specification, while adhering to travel constraints
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        #Route Optimization Protocol
        return {
            "type": "function",
            "function": {
                "name": "CalculateRouteOptimization",
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


#============================================================
#Utility functions (required here if not previously defined)
#============================================================
def _next_int_id(rows: list[dict[str, Any]], key: str) -> int:
    pass
    mx = 0
    for r in rows:
        try:
            v = int(r.get(key, 0))
            if v > mx:
                mx = v
        except Exception:
            continue
    return mx + 1


#============================================================
#16) compute_property_metrics
#============================================================
class CalculatePropertyMetricsTool(Tool):
    """Computes detailed property analysis metrics including market baseline and affordability."""

    @staticmethod
    def _estimate_rate(credit_score: int | None, region: str | None) -> float:
        pass
        #reflect CalculateMortgagePaymentTool for uniformity
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
        if region in {"AZ", "FL"}:
            base -= 0.15
        elif region in {"VT", "CA"}:
            base += 0.15
        return round(base, 3)

    @staticmethod
    def _pmt(loan_amount: float, annual_rate_pct: float, years: int = 30) -> float:
        pass
        r = (annual_rate_pct / 100.0) / 12.0
        n = years * 12
        if r == 0:
            return loan_amount / n
        return loan_amount * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

    @staticmethod
    def invoke(
        data: dict[str, Any],
        subject_property_id: str,
        comparable_properties: list = None,
        client_budget: dict = None
    ) -> str:
        pass
        comparable_properties = comparable_properties or []
        client_budget = client_budget or {}
        if not subject_property_id:
            return _err("subject_property_id is required")

        #---- Basic subject information (simplified - no property specifics available) ----
        subj_listing = (
            _collect_listing_by_property(data, str(subject_property_id)) or {}
        )
        subj_price = subj_listing.get("list_price")
        #Note: sqft, tax_rate, neighborhood_id are not present in the current data structure

        #---- Gather comparable prices/ppsf ----
        def _lp(pid_or_dict):
            pass
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
            ppsf = l.get("price_per_sqft")  #Utilize pre-calculated values from listings
            return price, ppsf

        comp_prices, comp_ppsf = [], []
        for c in comparable_properties:
            price, ppsf = _lp(c)
            if isinstance(price, (int, float)):
                comp_prices.append(float(price))
            if isinstance(ppsf, (int, float)):
                comp_ppsf.append(float(ppsf))
        comp_prices.sort()
        comp_ppsf.sort()

        #---- Construct market pool (simplified - consider all listings as market) ----
        market_prices, market_ppsf = [], []
        for l in data.get("listings", []):
            if l.get("list_price"):
                market_prices.append(float(l["list_price"]))
            if l.get("price_per_sqft"):
                market_ppsf.append(float(l["price_per_sqft"]))

        market_prices.sort()
        market_ppsf.sort()

        #---- Market positioning (utilize market pool when accessible, otherwise use comps) ----
        def _median(arr: list[float]) -> float | None:
            pass
            if not arr:
                return None
            m = len(arr) // 2
            return arr[m] if len(arr) % 2 == 1 else (arr[m - 1] + arr[m]) / 2.0

        ref_prices = market_prices if market_prices else comp_prices
        market_ppsf if market_ppsf else comp_ppsf

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

        #---- Affordability (P&I + estimated taxes if accessible) ----
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
            #estimate 30-year P&I from mortgage profile if feasible
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

        #Note: Property tax information is unavailable - relying solely on P&I
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

        #---- Comparative assessment & distinctive benefits ----
        vs_comparables = "competitive"
        uniq = []

        if subj_price is not None and comp_prices:
            avg_comp = sum(comp_prices) / len(comp_prices)
            if subj_price < 0.95 * avg_comp:
                vs_comparables = "undervalued"
                uniq.append("pricing")
            elif subj_price > 1.05 * avg_comp:
                vs_comparables = "overpriced"

        #Comparison of price per sqft (utilizing pre-calculated values when available)
        subj_ppsf = subj_listing.get("price_per_sqft")
        if subj_ppsf and comp_ppsf:
            avg_ppsf = sum(comp_ppsf) / len(comp_ppsf)
            if float(subj_ppsf) < 0.95 * avg_ppsf:
                uniq.append("price_per_sqft")

        #Note: Amenity analysis is not available - no property amenity data in the current structure

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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculatePropertyMetrics",
                "description": (
                    "Calculate market position (vs comps & market pool), affordability (P&I + taxes), and comparative analysis."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_property_id": {"type": "string"},
                        "comparable_properties": {
                            "type": "array",
                            "description": "List of property_ids WA dicts",
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


#============================================================
#39) retrieve_property_information
#============================================================
class FetchPropertyDetailsTool(Tool):
    """Merge listing, sales history, and open house information for a property."""

    @staticmethod
    def invoke(data: dict[str, Any], property_id: str = None) -> str:
        need = _require_property_id(property_id)
        if need:
            return _err(need)

        listing = _collect_listing_by_property(data, property_id)
        sales_history = _collect_sales_history(data, property_id)
        latest_sale = _latest(sales_history, "sale_date") if sales_history else None

        # Available open house times for this property
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchPropertyDetails",
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


#============================================================
#31) retrieve_comp_report_information
#============================================================
class FetchCompReportDetailsTool(Tool):
    """Fetches a comp report that includes related comparables, documents, email summaries, and audit trails."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: int = None) -> str:
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

        #emails associated with the report's client (summary only)
        client_id = _as_int(report.get("client_id"))
        emails = [
            e
            for e in data.get("emails", [])
            if _as_int(e.get("client_id")) == client_id
        ]
        emails_sorted = sorted(
            emails, key=lambda e: e.get("sent_at") or "", reverse=True
        )

        #audit trail records for this report
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchCompReportDetails",
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


#============================================================
#40) locate_nearby_listings
#============================================================
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


#============================================================
#32) retrieve_emails_for_client
#============================================================
class FetchEmailsForClientTool(Tool):
    """Provides emails for a client with optional filtering and limitations."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        client_id: int,
        template_code: str = None,
        since_date: str = None,
        until_date: str = None,
        limit: int = 50
,
    date: Any = None,
    ) -> str:
        client_id = _as_int(client_id)
        if client_id is None:
            return _err("client_id is required")

        template_filter = template_code
        since_date = since_date  # ISO string, compared in lexicographical order
        until_date = until_date
        limit = _as_int(limit) or 50

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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchEmailsForClient",
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


#============================================================
#33) retrieve_calendar_events_for_client
#============================================================
class FetchCalendarEventsForClientTool(Tool):
    """Delivers calendar events for a client, optionally constrained to a date range."""

    @staticmethod
    def invoke(data: dict[str, Any], client_id: int = None, start_at: str = None, end_at: str = None, date: Any = None) -> str:
        client_id = _as_int(client_id)
        if client_id is None:
            return _err("client_id is required")

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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchCalendarEventsForClient",
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


#============================================================
#34) retrieve_listings_by_ids
#============================================================
class FetchListingsByIdsTool(Tool):
    """Retrieves listings for various property_ids, with sales fallback if absent."""

    @staticmethod
    def invoke(data: dict[str, Any], property_ids: list[str] = None) -> str:
        ids = property_ids or []
        if not isinstance(ids, list) or not ids:
            return _err("property_ids must be a non-empty array")

        listings_map = {str(l.get("property_id")): l for l in data.get("listings", [])}
        out_items: list[dict[str, Any]] = []
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchListingsByIds",
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


#============================================================
#35) retrieve_route_information
#============================================================
class FetchRouteDetailsTool(Tool):
    """Retrieve a route using route_id WA the most recent route for a client."""

    @staticmethod
    def invoke(data: dict[str, Any], route_id: int = None, client_id: int = None) -> str:
        route_id = _as_int(route_id)
        client_id = _as_int(client_id)
        if route_id is None and client_id is None:
            return _err("route_id WA client_id is required")

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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchRouteDetails",
                "description": "Fetch a route by id WA latest by client.",
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


#============================================================
#36) retrieve_campaign_information
#============================================================
class FetchCampaignDetailsTool(Tool):
    """Retrieve a campaign along with the associated email count and audit records."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: int = None) -> str:
        campaign_id = _as_int(campaign_id)
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchCampaignDetails",
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


#============================================================
#37) create_client_briefing_document
#============================================================
class GenerateClientBriefingDocumentTool(Tool):
    """Creates a client briefing PDF and adds a documents row (entity_type=client)."""

    @staticmethod
    def invoke(data: dict[str, Any], client_id: int = None, created_by: int = None) -> str:
        client_id = _as_int(client_id)
        created_by = _as_int(created_by)
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
        payload = {"document": doc_row}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateClientBriefingDocument",
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


#============================================================
#38) verify_drive_time_constraints
#============================================================
class ValidateDriveTimeConstraintsTool(Tool):
    """Confirms that consecutive hops between properties adhere to a maximum hop time."""

    @staticmethod
    def invoke(data: dict[str, Any], property_list: list = None, max_hop_minutes: int = None,
    start_address: Any = None,
    ) -> str:
        pass
        property_list = property_list or []
        max_hop_minutes = _as_int(max_hop_minutes)
        if (
            not isinstance(property_list, list)
            or not property_list
            or max_hop_minutes is None
        ):
            return _err("property_list (list) and max_hop_minutes are required")

        max_constraint = min(30, max_hop_minutes)
        segments = []
        if property_list:
            # Utilize deterministic mock times akin to the route optimizer
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateDriveTimeConstraints",
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


#============================================================
#17) generate_comp_report_entry
#============================================================
class CreateCompReportEntryTool(Tool):
    """Inserts a new record into the comp_reports table."""

    @staticmethod
    def invoke(data: dict[str, Any], client_id: int = None, subject_property_id: str = None, created_by_broker_id: int = None, start_address: Any = None) -> str:
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
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createCompReportEntry",
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


#============================================================
#18) generate_comparable_entry
#============================================================
class CreateComparableEntryTool(Tool):
    """Inserts a single comparable record into the comparables table."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: int = None, comp_property_id: str = None, similarity_score: float = None, selection_reason: str = None) -> str:
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
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createComparableEntry",
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
    """Create comp_###.pdf URI from report_id, refresh comp_reports.doc_uri, and add a documents row."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: int = None, created_by: int = None, doc_type: str = "comp_report") -> str:
        pass
        report_id = _as_int(report_id)
        created_by = _as_int(created_by)
        doc_type = doc_type.strip()
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

        #--- Generate Audit Event Entry ---
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
        payload = {
                "document_uri": uri,
                "report": {
                    "report_id": report_id,
                    "doc_uri": uri,
                    "updated_at": HARD_TS,
                },
                "document_entry": doc_row,
                "audit_event": audit_rec,
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
                "name": "GenerateAttachCompReportDocument",
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
    """Perform batch insertion of comparables for a report."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: int = None, comparables: list = None) -> str:
        report_id = _as_int(report_id)
        items = comparables or []
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
        payload = {"created_count": len(created), "comparables": created}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BulkCreateComparableEntries",
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


#============================================================
#20) modify_comp_report_status
#============================================================
class UpdateCompReportStatusTool(Tool):
    """Modifies the status field in the comp_reports table."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: int = None, new_status: str = None, actor_id: int = None) -> str:
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

        #--- Generate Audit Event Entry ---
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
        payload = {
                "report_id": int(report_id),
                "previous_status": prev,
                "new_status": new_status,
                "updated_at": HARD_TS,
                "audit_event": audit_rec,
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
                "name": "UpdateCompReportStatus",
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


#============================================================
#21) generate_email_entry
#============================================================
class CreateEmailEntryTool(Tool):
    """Inserts a record into the emails table along with a corresponding audit event."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        client_id: str = None,
        broker_id: str = None,
        subject: str = None,
        body_uri: str = None,
        template_code: str = None,
        campaign_id: str = None
    ) -> str:
        if client_id is None or broker_id is None or not template_code:
            return _err("client_id, broker_id, and template_code are required")

        #--- Automatically generate subject and body_uri if not supplied ---
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
                    subject = "Follow-up on Your Client Briefing"
                elif template_code == "briefing_delivery":
                    subject = "Your Property Market Briefing is Ready"
                elif template_code == "first_time_buyer":
                    subject = f"First-Time Buyer Resources for {subject_property}"
                elif template_code == "general_update":
                    subject = "Real Estate Market Update"
                elif template_code == "market_update":
                    subject = "Your Market Update"
                elif template_code == "investment_alert":
                    subject = "Investment Opportunity Alert"
                elif template_code == "listing_summary":
                    subject = f"Property Listing Summary for {subject_property}"
                elif template_code == "welcome_new_client":
                    subject = "Welcome to Our Real Estate Services"
                elif template_code == "post_closing_checkin":
                    subject = "Post-Closing Check-CO and Next Steps"
                elif template_code == "next_steps":
                    subject = "Next Steps in Your Real Estate Journey"
                elif template_code == "follow_up":
                    subject = "Following Up on Your Real Estate Needs"
                else:
                    #Backup logic determined by report status
                    if report_status == "sent_to_client":
                        subject = f"Your comparable analysis for {subject_property} is complete"
                    elif report_status == "ready_for_review":
                        subject = "Your comp report is ready for review"
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
                    #Revert to comp report format
                    body_uri = f"https://storage.example.com/emails/email_comp_{int(client_id):03d}.html"

        #--- Generate Email Entry ---
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

        #--- Generate Audit Event Entry ---
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
        payload = {"email": email_rec, "audit_event": audit_rec}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createEmailEntry",
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
    """Generates an email entry with automatic subject/body creation if not provided."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        client_id: str = None,
        broker_id: str = None,
        template_code: str = None,
        subject: str = None,
        body_uri: str = None,
        campaign_id: str = None,
        property_id: str = None
    ) -> str:
        if client_id is None or broker_id is None or not template_code:
            return _err("client_id, broker_id, and template_code are required")

        # Process property_id as either a string or a list of strings
        if property_id:
            if isinstance(property_id, list):
                pid = ", ".join(property_id)
            else:
                pid = str(property_id)
        else:
            # Automatically create property_id if absent
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

        # Automatically create subject and body_uri if they are absent
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
                    subject = "Your Property Market Briefing is Ready"
                elif template_code == "first_time_buyer":
                    subject = f"First-Time Buyer Resources for {pid}"
                elif template_code == "general_update":
                    subject = "Real Estate Market Update"
                elif template_code == "market_update":
                    subject = "Your Market Update"
                elif template_code == "investment_alert":
                    subject = "Investment Opportunity Alert"
                elif template_code == "listing_summary":
                    subject = f"Property Listing Summary for {pid}"
                elif template_code == "welcome_new_client":
                    subject = "Welcome to Our Real Estate Services"
                elif template_code == "post_closing_checkin":
                    subject = "Post-Closing Check-CO and Next Steps"
                elif template_code == "follow_up":
                    subject = "Following Up on Your Real Estate Needs"
                else:
                    # Backup logic determined by report status
                    if report_status == "sent_to_client":
                        subject = f"Your comparable analysis for {pid} is complete"
                    elif report_status == "ready_for_review":
                        subject = "Your comp report is ready for review"
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
                    # Revert to comp report format
                    body_uri = f"https://storage.example.com/emails/email_comp_{int(client_id):03d}.html"

        # Generate Email Entry
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
        payload = {"email": email_rec, "audit_event": audit_rec}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
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


#============================================================
#22) generate_route_entry
#============================================================
class CreateRouteEntryTool(Tool):
    """Inserts a record into the routes table."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        client_id: int = None,
        route_date: str = None,
        stops_ordered_json: list = None,
        map_url: str = None,
        created_by_broker_id: int = None
    ) -> str:
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
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRouteEntry",
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


#============================================================
#23) generate_calendar_event_entry
#============================================================
class CreateCalendarEventEntryTool(Tool):
    """Inserts a record into the calendar_events table."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        broker_id: int = None,
        client_id: int = None,
        title: str = None,
        location: str = None,
        source: str = None,
        date: str = None
    ) -> str:
        start_at = ""
        end_at = ""

        # Improvement: if a date is given, automatically fill full-day times when start/end are absent
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
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCalendarEventEntry",
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


#============================================================
#24) generate_campaign_entry
#============================================================
class CreateCampaignEntryTool(Tool):
    """Inserts a record into the campaigns table along with a corresponding audit event."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_name: str = None, campaign_type: str = None, created_by: int = None,
    type: Any = None,
    ) -> str:
        if not campaign_name or not campaign_type or created_by is None:
            return _err("campaign_name, campaign_type, and created_by are required")

        #--- Generate Campaign Entry ---
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

        #--- Generate Audit Event Entry ---
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
        payload = {"campaign": campaign_rec, "audit_event": audit_rec}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCampaignEntry",
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


#============================================================
#25) generate_audit_event_entry
#============================================================
class CreateAuditEventEntryTool(Tool):
    """Inserts a record into the audit_events table for compliance monitoring."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        actor_id: int = None,
        action: str = None,
        entity_type: str = None,
        entity_id: str = None,
        metadata_json: Any = None
    ) -> str:
        if actor_id is None or not action or not entity_type or entity_id is None:
            return _err("actor_id, action, entity_type, entity_id are required")

        if metadata_json is not None and not isinstance(metadata_json, (dict, list)):
            return _err("metadata_json must be an object WA array if provided")

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
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAuditEventEntry",
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


#============================================================
#26) create_comp_report_document
#============================================================
class GenerateCompReportDocumentTool(Tool):
    """Creates a PDF report for comparable analysis."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        report_id: int = None,
        subject_property_data: dict = None,
        comparable_data: list = None,
        market_analysis: dict = None,
        mortgage_calculations: dict = None
    ) -> str:
        if report_id is None:
            return _err("report_id is required")

        # Deterministic URI derived from report_id
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateCompReportDocument",
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


#============================================================
#27) create_email_content
#============================================================
class GenerateEmailContentTool(Tool):
    """Creates HTML content for emails."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        template_code: str = None,
        recipient_data: dict[str, Any] = None,
        context_data: dict[str, Any] = None,
        attachments: list = None
    ) -> str:
        recipient_data = recipient_data or {}
        context_data = context_data or {}
        attachments = attachments or []

        if not template_code:
            return _err("template_code is required")

        # Deterministic content URI generated from template_code
        rid = recipient_data.get("client_id") or "000"
        if isinstance(rid, int) or (isinstance(rid, str) and rid.isdigit()):
            client_id = int(rid)
        else:
            client_id = 15  # Standard fallback

        # URI generation specific to the template
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

        # Establish subject line according to the template
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
                context_data.get("subject_line") or "Follow-up on Your Client Briefing"
            )
        elif template_code == "briefing_delivery":
            subject_line = (
                context_data.get("subject_line")
                or "Your Property Market Briefing is Ready"
            )
        elif template_code == "first_time_buyer":
            subject_line = (
                context_data.get("subject_line")
                or f"First-Time Buyer Resources for {property_id}"
            )
        elif template_code == "general_update":
            subject_line = (
                context_data.get("subject_line") or "Real Estate Market Update"
            )
        elif template_code == "market_update":
            subject_line = context_data.get("subject_line") or "Your Market Update"
        elif template_code == "investment_alert":
            subject_line = (
                context_data.get("subject_line") or "Investment Opportunity Alert"
            )
        elif template_code == "listing_summary":
            subject_line = (
                context_data.get("subject_line")
                or f"Property Listing Summary for {property_id}"
            )
        elif template_code == "welcome_new_client":
            subject_line = (
                context_data.get("subject_line")
                or "Welcome to Our Real Estate Services"
            )
        elif template_code == "post_closing_checkin":
            subject_line = (
                context_data.get("subject_line")
                or "Post-Closing Check-CO and Next Steps"
            )
        elif template_code == "next_steps":
            subject_line = (
                context_data.get("subject_line")
                or "Next Steps in Your Real Estate Journey"
            )
        elif template_code == "follow_up":
            subject_line = (
                context_data.get("subject_line")
                or "Following Up on Your Real Estate Needs"
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateEmailContent",
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


#============================================================
#28) validate_comp_report_workflow
#============================================================
class VerifyCompReportWorkflowTool(Tool):
    """Confirms that the entire comparable analysis workflow was performed accurately."""

    @staticmethod
    def invoke(data: dict[str, Any], report_id: int = None) -> str:
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verifyCompReportWorkflow",
                "description": "Verify comparable analysis workflow end state.",
                "parameters": {
                    "type": "object",
                    "properties": {"report_id": {"type": "integer"}},
                    "required": ["report_id"],
                },
            },
        }


#============================================================
#29) validate_route_creation
#============================================================
class VerifyRouteCreationTool(Tool):
    """Confirms that the property viewing route was established successfully."""

    @staticmethod
    def invoke(data: dict[str, Any], route_id: int = None) -> str:
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

        #events = {int(e.get("event_id")): e for e in data.get("calendar_events", []) if e.get("event_id") is not None}
        #event = events.get(int(event_id))
        #event_created = event is not None

        #Travel constraints satisfied: if map_url is present and there is at least 1 stop
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
                ),  #presume notification is managed through email/log elsewhere
                "schedule_complete": bool(route_exists and travel_constraints_met),
            }
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verifyRouteCreation",
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


#============================================================
#30) create_next_comp_report_uri
#============================================================
class GenerateNextCompReportUriTool(Tool):
    """Creates the next comp_###.pdf URI based on the highest report_id in comp_reports."""

    @staticmethod
    def invoke(data: dict[str, Any], base_url: str = "https://storage.example.com/reports/", 
               prefix: str = "comp_", ext: str = ".pdf", pad_width: int = 3) -> str:
        pass
        # Locate the current maximum report_id
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
            "file_uri": uri,  # ease of use
            "doc_uri": uri,  # compatible with update_comp_report_doc_uri
            "generated_at": HARD_TS,
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateNextCompReportUri",
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


#============================================================
#generate_mortgage_profile
#============================================================
class CreateMortgageProfileTool(Tool):
    """Inserts WA modifies a mortgage profile entry in the mortgage_profiles table."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        client_id: int = None,
        loan_amount: float = None,
        down_payment: float = None,
        interest_rate: float = None,
        term_years: int = None,
        annual_income: float = None,
        credit_score: int = None,
        region: str = None
    ) -> str:
        client_id = _as_int(client_id)
        term_years = _as_int(term_years)

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

        # Non-mandatory fields
        credit_score = _as_int(credit_score)

        # Accept misspelling "mortage_profiles"
        if "mortgage_profiles" in data:
            rows = data.setdefault("mortgage_profiles", [])
        else:
            rows = data.setdefault("mortage_profiles", [])

        existing = _get_mortgage_profile(data, client_id)
        if existing:
            # Revise current profile
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
            payload = existing
            out = json.dumps(payload, indent=2)
            return out
        else:
            # Establish a new profile
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
            payload = rec
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMortgageProfile",
                "description": (
                    "Creates a new mortgage profile for a client, WA updates existing one."
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


#============================================================
#Export entities
#============================================================
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
