import json
from itertools import islice
from typing import Dict, Any, List, Optional, Union
from domains.dto import Tool

# ---- Helpers ---------------------------------

def _now_iso_fixed() -> str:
    return "2025-08-20T00:00:00Z"


def _next_auto_id(rows: List[Dict[str, Any]], key: str) -> int:
    return max((int(r.get(key, 0)) for r in rows), default=0) + 1


def _by_key(items: List[Dict[str, Any]], key: str) -> Dict[Any, Dict[str, Any]]:
    return {i.get(key): i for i in (items or [])}


# ---- Tools ------------------------------------

class ValidateDriveTimeHops(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        stops = kwargs.get("property_ids") or []
        max_minutes = kwargs.get("max_minutes", 30)
        hops = [{"from": stops[i], "to": stops[i + 1], "minutes": 20} for i in range(max(0, len(stops) - 1))]
        ok = all(h["minutes"] <= max_minutes for h in hops)
        return json.dumps({"ok": ok, "hops": hops, "max_minutes": max_minutes}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_drive_time_hops",
                "description": "Compute if sequential hops fit within max drive minutes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_ids": {"type": "array", "items": {"type": "string"}},
                        "max_minutes": {"type": "integer"},
                    },
                    "required": ["property_ids", "max_minutes"],
                },
            },
        }


class FetchClientPrefs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get("client_id")
        if client_id is None:
            return json.dumps({"error": "client_id is required"}, indent=2)
        prefs = next((p for p in data.get("client_preferences", []) if p.get("client_id") == client_id), None)
        if not prefs:
            return json.dumps({"error": f"No preferences found for client_id={client_id}"}, indent=2)
        return json.dumps(prefs, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_client_prefs",
                "description": "Get preferences for a specific client.",
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }


class RetrieveMortgageProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get("client_id")
        profiles = data.get("mortgage_profiles") or data.get("mortage_profiles") or []  # typo tolerance
        prof = next((m for m in profiles if m.get("client_id") == client_id), None)
        if not prof:
            return json.dumps({"error": f"No mortgage profile for client_id={client_id}"}, indent=2)
        return json.dumps(prof, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "retrieve_mortgage_profile",
                "description": "Fetch the mortgage profile for a client.",
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }


class LookupPropertyWithLatestListing(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_id = kwargs.get("property_id")
        if not property_id:
            return json.dumps({"error": "property_id is required"}, indent=2)
        prop = next((p for p in data.get("properties", []) if p.get("property_id") == property_id), None)
        if not prop:
            return json.dumps({"error": f"Property '{property_id}' not found"}, indent=2)
        listings = [l for l in data.get("listings", []) if l.get("property_id") == property_id]
        listing = None
        if listings:
            listing = max(listings, key=lambda x: ((x.get("updated_at") or ""), x.get("listing_id", 0)))
        return json.dumps({"property": prop, "listing": listing}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "lookup_property_with_latest_listing",
                "description": "Get a property's details and its most recent listing (if available).",
                "parameters": {
                    "type": "object",
                    "properties": {"property_id": {"type": "string"}},
                    "required": ["property_id"],
                },
            },
        }


class QueryActiveListings(Tool):
    """Filter and return active listings by given constraints."""

    @staticmethod
    def _by_key(rows: List[Dict[str, Any]], key: str) -> Dict[Any, Dict[str, Any]]:
        return {r.get(key): r for r in rows or []}

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        neighborhood_ids = kwargs.get("neighborhood_ids")
        price_min: Optional[float] = kwargs.get("price_min")
        price_max: Optional[float] = kwargs.get("price_max")
        beds: Optional[int] = kwargs.get("beds")
        baths: Optional[int] = kwargs.get("baths")
        sqft_min: Optional[int] = kwargs.get("sqft_min")
        sqft_max: Optional[int] = kwargs.get("sqft_max")
        property_type: Optional[str] = kwargs.get("property_type")
        limit: int = kwargs.get("limit", 15)

        neighborhoods = set(neighborhood_ids or [])
        props = QueryActiveListings._by_key(data.get("properties", []), "property_id")
        listings = (data.get("listings") or [])

        def within(val: Optional[float], lo: Optional[float], hi: Optional[float]) -> bool:
            v = 0 if val is None else val
            if lo is not None and v < lo:
                return False
            if hi is not None and v > hi:
                return False
            return True

        def matches(pr: Dict[str, Any], lst: Dict[str, Any]) -> bool:
            return (
                lst.get("status") == "active"
                and (not neighborhoods or pr.get("neighborhood_id") in neighborhoods)
                and (property_type is None or pr.get("property_type") == property_type)
                and (beds is None or pr.get("beds") == beds)
                and (baths is None or pr.get("baths") == baths)
                and within(lst.get("list_price", 0), price_min, price_max)
                and within(pr.get("sqft", 0), sqft_min, sqft_max)
            )

        result_iter = (
            {
                "listing_id": lst.get("listing_id"),
                "property_id": pr.get("property_id"),
                "neighborhood_id": pr.get("neighborhood_id"),
                "list_price": lst.get("list_price"),
                "property_type": pr.get("property_type"),
                "beds": pr.get("beds"),
                "baths": pr.get("baths"),
                "sqft": pr.get("sqft"),
                "listing_url": lst.get("listing_url"),
                "street_view_url": lst.get("street_view_url"),
            }
            for lst in listings
            if (pr := props.get(lst.get("property_id"))) is not None and matches(pr, lst)
        )

        results = list(islice(result_iter, limit))
        return json.dumps({"results": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "query_active_listings",
                "description": "Search active listings by neighborhood(s) and criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "neighborhood_ids": {"type": "array", "items": {"type": "integer"}},
                        "price_min": {"type": "integer"},
                        "price_max": {"type": "integer"},
                        "beds": {"type": "integer"},
                        "baths": {"type": "integer"},
                        "sqft_min": {"type": "integer"},
                        "sqft_max": {"type": "integer"},
                        "property_type": {"type": "string"},
                        "limit": {"type": "integer"},
                    },
                    "required": [],
                },
            },
        }


class QueryListingsByNeighborhoods(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        kwargs["neighborhood_ids"] = kwargs.get("neighborhood_ids") or []
        return QueryActiveListings.invoke(data, **kwargs)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "query_listings_by_neighborhoods",
                "description": "Search listings within the provided neighborhoods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "neighborhood_ids": {"type": "array", "items": {"type": "integer"}},
                        "price_min": {"type": "integer"},
                        "price_max": {"type": "integer"},
                        "beds": {"type": "integer"},
                        "baths": {"type": "integer"},
                        "limit": {"type": "integer"},
                    },
                    "required": ["neighborhood_ids"],
                },
            },
        }


class FetchNeighborhood(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        neighborhood_id = kwargs.get("neighborhood_id")
        n = next((n for n in data.get("neighborhoods", []) if n.get("neighborhood_id") == neighborhood_id), None)
        if not n:
            return json.dumps({"error": f"Neighborhood {neighborhood_id} not found"}, indent=2)
        return json.dumps(n, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_neighborhood",
                "description": "Return a neighborhood row including bordering_ids_json.",
                "parameters": {
                    "type": "object",
                    "properties": {"neighborhood_id": {"type": "integer"}},
                    "required": ["neighborhood_id"],
                },
            },
        }


class ListAdjacentNeighborhoods(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        nid = kwargs.get("neighborhood_id")
        n = next((n for n in data.get("neighborhoods", []) if n.get("neighborhood_id") == nid), None)
        if not n:
            return json.dumps({"error": f"Neighborhood {nid} not found"}, indent=2)
        return json.dumps({"neighborhood_id": nid, "bordering": n.get("bordering_ids_json") or []}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_adjacent_neighborhoods",
                "description": "List bordering neighborhood IDs for a given neighborhood.",
                "parameters": {
                    "type": "object",
                    "properties": {"neighborhood_id": {"type": "integer"}},
                    "required": ["neighborhood_id"],
                },
            },
        }


class FetchBrokerProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        broker_id = kwargs.get("broker_id")
        br = next((b for b in data.get("brokers", []) if b.get("broker_id") == broker_id), None)
        if not br:
            return json.dumps({"error": f"Broker {broker_id} not found"}, indent=2)
        return json.dumps(br, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_broker_profile",
                "description": "Fetch a broker profile.",
                "parameters": {
                    "type": "object",
                    "properties": {"broker_id": {"type": "integer"}},
                    "required": ["broker_id"],
                },
            },
        }


class EstimateMortgagePayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get("client_id")
        list_price = kwargs.get("list_price")
        term_years = kwargs.get("term_years", 30)
        region_override = kwargs.get("region")

        profiles = data.get("mortgage_profiles") or data.get("mortage_profiles") or []
        profile = next((m for m in profiles if m.get("client_id") == client_id), {})
        credit_score = profile.get("credit_score", 720)
        down_payment = profile.get("down_payment", int(0.2 * (list_price or 0)))
        loan_amount = profile.get("desired_loan_amount", (list_price or 0) - down_payment)
        region = region_override or profile.get("region")

        best = None
        for r in (data.get("mortgage_rates", []) or []):
            if region and r.get("region") != region:
                continue
            if r.get("term_years") != term_years:
                continue
            if r.get("min_credit_score", 0) > credit_score:
                continue
            if not best or r.get("apr_percent", 99) < best.get("apr_percent", 99):
                best = r
        apr = (best or {}).get("apr_percent", 6.0) / 100.0
        monthly_rate = apr / 12.0
        n = term_years * 12
        if monthly_rate == 0 or n == 0:
            monthly_payment = loan_amount / max(1, n)
        else:
            monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** n) / ((1 + monthly_rate) ** n - 1)

        return json.dumps(
            {
                "client_id": client_id,
                "loan_amount": round(loan_amount, 2),
                "apr_percent": round(apr * 100, 3),
                "term_years": term_years,
                "estimated_monthly_payment": round(monthly_payment, 2),
                "lender_rate_used": best,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "estimate_mortgage_payment",
                "description": "Estimate monthly payment for a client given list_price (prefers client profile + lender rates).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "list_price": {"type": "number"},
                        "term_years": {"type": "integer"},
                        "region": {"type": "string"},
                    },
                    "required": ["client_id", "list_price"],
                },
            },
        }


class RecentSalesForProperty(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_id = kwargs.get("property_id")
        limit = int(kwargs.get("limit", 3))
        sales = [s for s in data.get("sales", []) if s.get("property_id") == property_id]
        sales = sorted(sales, key=lambda s: s.get("sale_date") or "", reverse=True)[:limit]
        return json.dumps({"property_id": property_id, "sales": sales}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "recent_sales_for_property",
                "description": "Return up to N recent sales rows for a property.",
                "parameters": {
                    "type": "object",
                    "properties": {"property_id": {"type": "string"}, "limit": {"type": "integer"}},
                    "required": ["property_id"],
                },
            },
        }


class CreateOrUpdateCompReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get("client_id")
        subject_property_id = kwargs.get("subject_property_id")
        created_by_broker_id = kwargs.get("created_by_broker_id")
        final_status = kwargs.get("final_status", "draft")

        reports = data.get("comp_reports", [])
        new_report_id = _next_auto_id(reports, "report_id")
        doc_uri = f"https://test.storage.com/reports/comp_{new_report_id:03d}.pdf"
        rpt = {
            "report_id": new_report_id,
            "client_id": client_id,
            "subject_property_id": subject_property_id,
            "created_by_broker_id": created_by_broker_id,
            "created_at": _now_iso_fixed(),
            "doc_uri": doc_uri,
            "status": final_status,
        }
        reports.append(rpt)

        comps_table = data.get("comparables", [])
        props = _by_key(data.get("properties", []), "property_id")
        candidates = []
        for lst in (data.get("listings", []) or []):
            if lst.get("status") != "active":
                continue
            pid = lst.get("property_id")
            if pid == subject_property_id:
                continue
            pr = props.get(pid, {})
            candidates.append(
                {
                    "comp_property_id": pid,
                    "similarity_score": 0.8,
                    "selection_reason": "Neighborhood/size proximity",
                    "tie_breaker_notes": "Deterministic placeholder",
                }
            )
        for comp in candidates[:3]:
            comp_id = _next_auto_id(comps_table, "comp_id")
            comps_table.append({"comp_id": comp_id, "report_id": new_report_id, **comp})

        documents = data.get("documents", [])
        new_doc_id = _next_auto_id(documents, "document_id")
        documents.append(
            {
                "document_id": new_doc_id,
                "entity_type": "comp_report",
                "entity_id": new_report_id,
                "doc_type": "comp_report",
                "file_uri": doc_uri,
                "created_by": created_by_broker_id,
                "created_at": _now_iso_fixed(),
            }
        )

        audits = data.get("audit_events", [])
        new_audit_id = _next_auto_id(audits, "event_id")
        audits.append(
            {
                "event_id": new_audit_id,
                "actor_id": created_by_broker_id,
                "action": "comp_report_saved" if final_status != "sent_to_client" else "comp_report_sent",
                "entity_type": "comp_reports",
                "entity_id": new_report_id,
                "occurred_at": _now_iso_fixed(),
                "metadata_json": {"comps_count": min(3, len(candidates)), "search_tiers": "neighborhood_first_with_borders"},
            }
        )

        return json.dumps({"report_id": new_report_id, "doc_uri": doc_uri, "status": final_status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_or_update_comp_report",
                "description": "Create/update a comp report; writes comp_reports, comparables, documents, audit_events.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "subject_property_id": {"type": "string"},
                        "created_by_broker_id": {"type": "integer"},
                        "final_status": {"type": "string"},
                    },
                    "required": ["client_id", "subject_property_id", "created_by_broker_id"],
                },
            },
        }


class ReadCompReportBundle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = kwargs.get("report_id")
        rpt = next((r for r in data.get("comp_reports", []) if r.get("report_id") == int(report_id)), None)
        if not rpt:
            return json.dumps({"error": f"Report {report_id} not found"}, indent=2)
        comps = [c for c in data.get("comparables", []) if c.get("report_id") == int(report_id)]
        docs = [d for d in data.get("documents", []) if d.get("entity_type") == "comp_report" and d.get("entity_id") == int(report_id)]
        return json.dumps({"report": rpt, "comparables": comps, "documents": docs}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "read_comp_report_bundle",
                "description": "Fetch a comp report with its comparables and attached document(s).",
                "parameters": {
                    "type": "object",
                    "properties": {"report_id": {"type": "integer"}},
                    "required": ["report_id"],
                },
            },
        }


class SetCompReportStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_id = kwargs.get("report_id")
        new_status = kwargs.get("status")
        rpt = next((r for r in data.get("comp_reports", []) if r.get("report_id") == int(report_id)), None)
        if not rpt:
            return json.dumps({"error": f"Report {report_id} not found"}, indent=2)
        rpt["status"] = new_status
        return json.dumps({"report_id": report_id, "status": new_status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_comp_report_status",
                "description": "Update the status of a comp report.",
                "parameters": {
                    "type": "object",
                    "properties": {"report_id": {"type": "integer"}, "status": {"type": "string"}},
                    "required": ["report_id", "status"],
                },
            },
        }


class NewCampaignCreator(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name, ctype, created_by = kwargs.get("name"), kwargs.get("type"), kwargs.get("created_by")
        c = data.get("campaigns", [])
        new_id = _next_auto_id(c, "campaign_id")
        row = {"campaign_id": new_id, "name": name, "type": ctype, "created_by": created_by, "created_at": _now_iso_fixed()}
        c.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "new_campaign_creator",
                "description": "Create a new campaign row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string"},
                        "created_by": {"type": "integer"},
                    },
                    "required": ["name", "type", "created_by"],
                },
            },
        }


class ReadCampaign(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("campaign_id")
        c = next((x for x in data.get("campaigns", []) if x.get("campaign_id") == cid), None)
        if not c:
            return json.dumps({"error": f"campaign_id {cid} not found"}, indent=2)
        return json.dumps(c, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "read_campaign",
                "description": "Fetch a campaign row by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "integer"}},
                    "required": ["campaign_id"],
                },
            },
        }


class ComposeClientEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        template_code = kwargs.get("template_code")
        client_id = kwargs.get("client_id")
        subject = (kwargs.get("subject") or template_code)
        slug = (kwargs.get("slug") or f"{template_code}_{client_id}").lower().replace(" ", "_")
        body_uri = f"https://test.storage.com/emails/{slug}.html"
        return json.dumps({"client_id": client_id, "subject": subject, "body_uri": body_uri, "template_code": template_code}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compose_client_email",
                "description": "Render email body and return body_uri for a template + client.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "template_code": {"type": "string"},
                        "client_id": {"type": "integer"},
                        "subject": {"type": "string"},
                        "slug": {"type": "string"},
                        "payload": {"type": "object"},
                    },
                    "required": ["template_code", "client_id"],
                },
            },
        }


class PersistOutboundEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get("client_id")
        broker_id = kwargs.get("broker_id")
        subject = kwargs.get("subject")
        body_uri = kwargs.get("body_uri")
        template_code = kwargs.get("template_code")
        campaign_id = kwargs.get("campaign_id")
        emails = data.get("emails", [])
        new_email_id = _next_auto_id(emails, "email_id")
        row = {
            "email_id": new_email_id,
            "client_id": client_id,
            "broker_id": broker_id,
            "subject": subject,
            "body_uri": body_uri,
            "template_code": template_code,
            "sent_at": _now_iso_fixed(),
            "campaign_id": campaign_id,
        }
        emails.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "persist_outbound_email",
                "description": "Persist an outbound email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "broker_id": {"type": "integer"},
                        "subject": {"type": "string"},
                        "body_uri": {"type": "string"},
                        "template_code": {"type": "string"},
                        "campaign_id": {"type": ["integer", "null"]},
                    },
                    "required": ["client_id", "broker_id", "subject", "body_uri", "template_code"],
                },
            },
        }


class ListClientEmails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("client_id")
        rows = [e for e in (data.get("emails") or []) if e.get("client_id") == cid]
        return json.dumps({"client_id": cid, "emails": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_client_emails",
                "description": "List all emails for a client.",
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }


class InsertCalendarEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        events = data.get("calendar_events", [])
        new_id = _next_auto_id(events, "event_id")
        row = {
            "event_id": new_id,
            "broker_id": kwargs.get("broker_id"),
            "client_id": kwargs.get("client_id"),
            "title": kwargs.get("title"),
            "start_at": kwargs.get("start_at"),
            "end_at": kwargs.get("end_at"),
            "location": kwargs.get("location"),
            "notes": kwargs.get("notes"),
            "source": kwargs.get("source"),
        }
        events.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "insert_calendar_event",
                "description": "Create a calendar event.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "broker_id": {"type": "integer"},
                        "client_id": {"type": "integer"},
                        "title": {"type": "string"},
                        "start_at": {"type": "string"},
                        "end_at": {"type": "string"},
                        "location": {"type": "string"},
                        "notes": {"type": "string"},
                        "source": {"type": "string"},
                    },
                    "required": ["broker_id", "client_id", "title", "start_at", "end_at", "location", "source"],
                },
            },
        }


class ListClientCalendarEvents(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("client_id")
        rows = [e for e in data.get("calendar_events", []) if e.get("client_id") == cid]
        return json.dumps({"client_id": cid, "events": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_client_calendar_events",
                "description": "List calendar events for a client.",
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }


class OpenHousesForProperties(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pids = set(kwargs.get("property_ids") or [])
        date_from = kwargs.get("date_from")
        date_to = kwargs.get("date_to")
        rows = []
        for oh in (data.get("open_houses", []) or []):
            if pids and oh.get("property_id") not in pids:
                continue
            dt = oh.get("start_at", "")
            if date_from and dt < f"{date_from}T00:00:00Z":
                continue
            if date_to and dt > f"{date_to}T23:59:59Z":
                continue
            rows.append(oh)
        return json.dumps({"matches": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "open_houses_for_properties",
                "description": "Fetch open house windows for specific properties within a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_ids": {"type": "array", "items": {"type": "string"}},
                        "date_from": {"type": "string"},
                        "date_to": {"type": "string"},
                    },
                    "required": ["property_ids", "date_from", "date_to"],
                },
            },
        }


class PersistViewingRoute(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        routes = data.get("routes", [])
        new_id = _next_auto_id(routes, "route_id")
        row = {
            "route_id": new_id,
            "client_id": kwargs.get("client_id"),
            "date": kwargs.get("date"),
            "stops_ordered_json": kwargs.get("stops_ordered_json"),
            "map_url": kwargs.get("map_url") or f"https://maps.google.com/route/route_{new_id:03d}",
            "created_by_broker_id": kwargs.get("created_by_broker_id"),
            "created_at": _now_iso_fixed(),
        }
        routes.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "persist_viewing_route",
                "description": "Persist a route with ordered stops and a map link.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "date": {"type": "string"},
                        "stops_ordered_json": {"type": "array", "items": {"type": "string"}},
                        "map_url": {"type": "string"},
                        "created_by_broker_id": {"type": "integer"},
                    },
                    "required": ["client_id", "date", "stops_ordered_json", "created_by_broker_id"],
                },
            },
        }


class ReadRoute(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rid = kwargs.get("route_id")
        r = next((x for x in data.get("routes", []) if x.get("route_id") == rid), None)
        if not r:
            return json.dumps({"error": f"route_id {rid} not found"}, indent=2)
        return json.dumps(r, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "read_route",
                "description": "Fetch a route by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"route_id": {"type": "integer"}},
                    "required": ["route_id"],
                },
            },
        }


class DraftSellerBrokerBatch(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        props = kwargs.get("property_ids") or []
        client_id = kwargs.get("client_id")
        drafts_uri = f"https://test.storage.com/drafts/client_{client_id}_props_{len(props)}.pdf"
        return json.dumps({"client_id": client_id, "property_ids": props, "drafts_uri": drafts_uri}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "draft_seller_broker_batch",
                "description": "Generate a drafts bundle for seller broker emails.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "property_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["client_id", "property_ids"],
                },
            },
        }

class AppendAuditEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        audits = data.get("audit_events", [])
        new_id = _next_auto_id(audits, "event_id")
        row = {
            "event_id": new_id,
            "actor_id": kwargs.get("actor_id"),
            "action": kwargs.get("action"),
            "entity_type": kwargs.get("entity_type"),
            "entity_id": kwargs.get("entity_id"),
            "occurred_at": _now_iso_fixed(),
            "metadata_json": kwargs.get("metadata_json") or {},
        }
        audits.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_audit_event",
                "description": "Append an audit_events row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {"type": "integer"},
                        "action": {"type": "string"},
                        "entity_type": {"type": "string"},
                        "entity_id": {"type": ["integer", "string"]},
                        "metadata_json": {"type": "object"},
                    },
                    "required": ["actor_id", "action", "entity_type", "entity_id"],
                },
            },
        }


class GatherListingsWithProperties(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ids = set(kwargs.get("listing_ids") or [])
        props = _by_key(data.get("properties", []), "property_id")
        out: List[Dict[str, Any]] = []
        for lst in (data.get("listings", []) or []):
            if ids and lst.get("listing_id") not in ids:
                continue
            pr = props.get(lst.get("property_id")) or {}
            out.append({"listing": lst, "property": pr})
        return json.dumps({"items": out}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "gather_listings_with_properties",
                "description": "Return listing + property for listing_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {"listing_ids": {"type": "array", "items": {"type": "integer"}}},
                    "required": ["listing_ids"],
                },
            },
        }


class OpenHouseWindowsByNeighborhoods(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        nids = set(kwargs.get("neighborhood_ids") or [])
        props = [p for p in data.get("properties", []) if p.get("neighborhood_id") in nids]
        prop_ids = {p.get("property_id") for p in props}
        rows = [oh for oh in data.get("open_houses", []) if oh.get("property_id") in prop_ids]
        return json.dumps({"neighborhood_ids": list(nids), "open_houses": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "open_house_windows_by_neighborhoods",
                "description": "Fetch open house windows for neighborhoods.",
                "parameters": {
                    "type": "object",
                    "properties": {"neighborhood_ids": {"type": "array", "items": {"type": "integer"}}},
                    "required": ["neighborhood_ids"],
                },
            },
        }


class CreateBriefingDoc(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get("client_id")
        broker_id = kwargs.get("broker_id")
        version_tag = kwargs.get("version_tag", "v1")
        documents = data.get("documents", [])
        new_id = _next_auto_id(documents, "document_id")
        file_uri = f"https://test.storage.com/details/client_briefing_{client_id:03d}_{version_tag}.pdf"
        row = {
            "document_id": new_id,
            "entity_type": "client",
            "entity_id": client_id,
            "doc_type": "briefing_doc",
            "file_uri": file_uri,
            "created_by": broker_id,
            "created_at": _now_iso_fixed(),
        }
        documents.append(row)
        return json.dumps({"document_id": new_id, "file_uri": file_uri}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_briefing_doc",
                "description": "Create a client briefing document and persist it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "broker_id": {"type": "integer"},
                        "version_tag": {"type": "string"},
                    },
                    "required": ["client_id", "broker_id"],
                },
            },
        }


class LinkDocumentToClient(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        documents = data.get("documents", [])
        new_id = _next_auto_id(documents, "document_id")
        row = {
            "document_id": new_id,
            "entity_type": "client",
            "entity_id": kwargs.get("client_id"),
            "doc_type": kwargs.get("doc_type") or "briefing_doc",
            "file_uri": kwargs.get("file_uri"),
            "created_by": kwargs.get("created_by"),
            "created_at": _now_iso_fixed(),
        }
        documents.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_document_to_client",
                "description": "Attach a provided file_uri to a client as a document.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "file_uri": {"type": "string"},
                        "doc_type": {"type": "string"},
                        "created_by": {"type": "integer"},
                    },
                    "required": ["client_id", "file_uri"],
                },
            },
        }





# ---- Tools List ------------------------------------------------
TOOLS = [
    ValidateDriveTimeHops(),
    FetchClientPrefs(),
    RetrieveMortgageProfile(),
    LookupPropertyWithLatestListing(),
    QueryActiveListings(),
    QueryListingsByNeighborhoods(),
    FetchNeighborhood(),
    ListAdjacentNeighborhoods(),
    FetchBrokerProfile(),
    EstimateMortgagePayment(),
    RecentSalesForProperty(),
    CreateOrUpdateCompReport(),
    ReadCompReportBundle(),
    SetCompReportStatus(),
    NewCampaignCreator(),
    ReadCampaign(),
    ComposeClientEmail(),
    PersistOutboundEmail(),
    ListClientEmails(),
    InsertCalendarEvent(),
    ListClientCalendarEvents(),
    OpenHousesForProperties(),
    PersistViewingRoute(),
    ReadRoute(),
    DraftSellerBrokerBatch(),
    AppendAuditEvent(),
    GatherListingsWithProperties(),
    OpenHouseWindowsByNeighborhoods(),
    CreateBriefingDoc(),
    LinkDocumentToClient(),
]
