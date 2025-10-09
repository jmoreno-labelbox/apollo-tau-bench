import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


def _index_by(items: list[dict[str, Any]], key: str) -> dict[Any, dict[str, Any]]:
    pass
    return {i.get(key): i for i in items or []}


def _fixed_now_iso() -> str:
    pass
    return "2025-08-20T00:00:00Z"


def _next_int_id(rows: list[dict[str, Any]], key: str) -> int:
    pass
    return max((int(r.get(key, 0)) for r in rows), default=0) + 1


class GetClientPreferences(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None) -> str:
        if client_id is None:
            payload = {"error": "client_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        prefs = next(
            (
                p
                for p in data.get("client_preferences", [])
                if p.get("client_id") == client_id
            ),
            None,
        )
        if not prefs:
            payload = {"error": f"No preferences found for client_id={client_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = prefs
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetClientPreferences",
                "description": "Get preferences for a specific client.",
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }


class GetMortgageProfile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None) -> str:
        profiles = data.get("mortgage_profiles") or data.get("mortage_profiles") or []
        prof = next((m for m in profiles if m.get("client_id") == client_id), None)
        if not prof:
            payload = {"error": f"No mortgage profile for client_id={client_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = prof
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMortgageProfile",
                "description": "Fetch the mortgage profile for a client.",
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }


class GetPropertyAndListing(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], property_id: str = None) -> str:
        if not property_id:
            payload = {"error": "property_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        prop = next(
            (
                p
                for p in data.get("properties", [])
                if p.get("property_id") == property_id
            ),
            None,
        )
        if not prop:
            payload = {"error": f"Property '{property_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        listings = [
            l for l in data.get("listings", []) if l.get("property_id") == property_id
        ]
        listing = None
        if listings:
            listing = max(
                listings,
                key=lambda x: (x.get("updated_at") or "", x.get("listing_id", 0)),
            )
        payload = {"property": prop, "listing": listing}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPropertyAndListing",
                "description": "Get a property's details and its most recent listing (if available).",
                "parameters": {
                    "type": "object",
                    "properties": {"property_id": {"type": "string"}},
                    "required": ["property_id"],
                },
            },
        }


class SearchListings(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        neighborhood_ids: list[int] = None,
        price_min: float = None,
        price_max: float = None,
        beds: int = None,
        baths: int = None,
        sqft_min: int = None,
        sqft_max: int = None,
        property_type: str = None,
        limit: int = 15
    ) -> str:
        props = _index_by(data.get("properties", []), "property_id")
        results: list[dict[str, Any]] = []
        for lst in data.get("listings", []) or []:
            if lst.get("status") != "active":
                continue
            pr = props.get(lst.get("property_id"))
            if not pr:
                continue
            if neighborhood_ids and pr.get("neighborhood_id") not in set(
                neighborhood_ids
            ):
                continue
            if property_type and pr.get("property_type") != property_type:
                continue
            if beds is not None and pr.get("beds") != beds:
                continue
            if baths is not None and pr.get("baths") != baths:
                continue
            if price_min is not None and lst.get("list_price", 0) < price_min:
                continue
            if price_max is not None and lst.get("list_price", 0) > price_max:
                continue
            if sqft_min is not None and pr.get("sqft", 0) < sqft_min:
                continue
            if sqft_max is not None and pr.get("sqft", 0) > sqft_max:
                continue
            results.append(
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
            )
            if len(results) >= limit:
                break
        payload = {"results": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchListings",
                "description": "Search active listings by neighborhood(s) and criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "neighborhood_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                        },
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


class SearchListingsInNeighborhoods(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], neighborhood_ids: list = None,
    price_min: Any = None,
    beds: Any = None,
    property_type: Any = None,
    baths: Any = None,
    price_max: Any = None,
    limit: Any = None
    ) -> str:
        neighborhood_ids = neighborhood_ids or []
        return SearchListings.invoke(data, neighborhood_ids=neighborhood_ids)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchListingsInNeighborhoods",
                "description": "Search listings within the provided neighborhoods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "neighborhood_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                        },
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


class GetNeighborhoodDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], neighborhood_id: str = None, beds: Any = None, property_type: Any = None, price_min: Any = None) -> str:
        n = next(
            (
                n
                for n in data.get("neighborhoods", [])
                if n.get("neighborhood_id") == neighborhood_id
            ),
            None,
        )
        if not n:
            payload = {"error": f"Neighborhood {neighborhood_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = n
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNeighborhoodDetails",
                "description": "Return a neighborhood row including bordering_ids_json.",
                "parameters": {
                    "type": "object",
                    "properties": {"neighborhood_id": {"type": "integer"}},
                    "required": ["neighborhood_id"],
                },
            },
        }


class GetBorderingNeighborhoods(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], neighborhood_id: str = None) -> str:
        nid = neighborhood_id
        n = next(
            (
                n
                for n in data.get("neighborhoods", [])
                if n.get("neighborhood_id") == nid
            ),
            None,
        )
        if not n:
            payload = {"error": f"Neighborhood {nid} not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"neighborhood_id": nid, "bordering": n.get("bordering_ids_json") or []}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBorderingNeighborhoods",
                "description": "List bordering neighborhood IDs for a given neighborhood.",
                "parameters": {
                    "type": "object",
                    "properties": {"neighborhood_id": {"type": "integer"}},
                    "required": ["neighborhood_id"],
                },
            },
        }


class GetBrokerDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], broker_id: str = None) -> str:
        br = next(
            (b for b in data.get("brokers", []) if b.get("broker_id") == broker_id),
            None,
        )
        if not br:
            payload = {"error": f"Broker {broker_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = br
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getBrokerDetails",
                "description": "Fetch a broker profile.",
                "parameters": {
                    "type": "object",
                    "properties": {"broker_id": {"type": "integer"}},
                    "required": ["broker_id"],
                },
            },
        }


class ComputeMortgageEstimate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None, list_price: float = None, term_years: int = 30, region_override: str = None,
    region: Any = None,
    ) -> str:
        profiles = data.get("mortgage_profiles") or data.get("mortage_profiles") or []
        profile = next((m for m in profiles if m.get("client_id") == client_id), {})
        credit_score = profile.get("credit_score", 720)
        down_payment = profile.get("down_payment", int(0.2 * (list_price or 0)))
        loan_amount = profile.get(
            "desired_loan_amount", (list_price or 0) - down_payment
        )
        region = region_override or profile.get("region")

        best = None
        for r in data.get("mortgage_rates", []) or []:
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
            monthly_payment = (
                loan_amount
                * (monthly_rate * (1 + monthly_rate) ** n)
                / ((1 + monthly_rate) ** n - 1)
            )
        payload = {
                "client_id": client_id,
                "loan_amount": round(loan_amount, 2),
                "apr_percent": round(apr * 100, 3),
                "term_years": term_years,
                "estimated_monthly_payment": round(monthly_payment, 2),
                "lender_rate_used": best,
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
                "name": "ComputeMortgageEstimate",
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


class FetchRecentSalesByProperty(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], property_id: str, limit: int = 3) -> str:
        sales = [
            s for s in data.get("sales", []) if s.get("property_id") == property_id
        ]
        sales = sorted(sales, key=lambda s: s.get("sale_date") or "", reverse=True)[
            :limit
        ]
        payload = {"property_id": property_id, "sales": sales}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchRecentSalesByProperty",
                "description": "Return up to N recent sales rows for a property.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {"type": "string"},
                        "limit": {"type": "integer"},
                    },
                    "required": ["property_id"],
                },
            },
        }


class SaveCompReport(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        client_id: str,
        subject_property_id: str,
        created_by_broker_id: str,
        final_status: str = "draft"
    ) -> str:
        reports = data.get("comp_reports", [])
        new_report_id = _next_int_id(reports, "report_id")
        doc_uri = f"https://storage.example.com/reports/comp_{new_report_id:03d}.pdf"
        rpt = {
            "report_id": new_report_id,
            "client_id": client_id,
            "subject_property_id": subject_property_id,
            "created_by_broker_id": created_by_broker_id,
            "created_at": _fixed_now_iso(),
            "doc_uri": doc_uri,
            "status": final_status,
        }
        reports.append(rpt)

        comps_table = data.get("comparables", [])
        props = _index_by(data.get("properties", []), "property_id")
        _index_by(data.get("listings", []), "property_id")
        candidates = []
        for lst in data.get("listings", []) or []:
            if lst.get("status") != "active":
                continue
            pid = lst.get("property_id")
            if pid == subject_property_id:
                continue
            props.get(pid, {})
            candidates.append(
                {
                    "comp_property_id": pid,
                    "similarity_score": 0.8,
                    "selection_reason": "Neighborhood/size proximity",
                    "tie_breaker_notes": "Deterministic placeholder",
                }
            )
        for comp in candidates[:3]:
            comp_id = _next_int_id(comps_table, "comp_id")
            comps_table.append({"comp_id": comp_id, "report_id": new_report_id, **comp})

        documents = data.get("documents", [])
        new_doc_id = _next_int_id(documents, "document_id")
        documents.append(
            {
                "document_id": new_doc_id,
                "entity_type": "comp_report",
                "entity_id": new_report_id,
                "doc_type": "comp_report",
                "file_uri": doc_uri,
                "created_by": created_by_broker_id,
                "created_at": _fixed_now_iso(),
            }
        )

        audits = data.get("audit_events", [])
        new_audit_id = _next_int_id(audits, "event_id")
        audits.append(
            {
                "event_id": new_audit_id,
                "actor_id": created_by_broker_id,
                "action": (
                    "comp_report_saved"
                    if final_status != "sent_to_client"
                    else "comp_report_sent"
                ),
                "entity_type": "comp_reports",
                "entity_id": new_report_id,
                "occurred_at": _fixed_now_iso(),
                "metadata_json": {
                    "comps_count": min(3, len(candidates)),
                    "search_tiers": "neighborhood_first_with_borders",
                },
            }
        )
        payload = {"report_id": new_report_id, "doc_uri": doc_uri, "status": final_status}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SaveCompReport",
                "description": "Create/update a comp report; writes comp_reports, comparables, documents, audit_events.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "subject_property_id": {"type": "string"},
                        "created_by_broker_id": {"type": "integer"},
                        "final_status": {"type": "string"},
                    },
                    "required": [
                        "client_id",
                        "subject_property_id",
                        "created_by_broker_id",
                    ],
                },
            },
        }


class GetCompReportDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], report_id: int) -> str:
        rpt = next(
            (
                r
                for r in data.get("comp_reports", [])
                if r.get("report_id") == int(report_id)
            ),
            None,
        )
        if not rpt:
            payload = {"error": f"Report {report_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        comps = [
            c
            for c in data.get("comparables", [])
            if c.get("report_id") == int(report_id)
        ]
        docs = [
            d
            for d in data.get("documents", [])
            if d.get("entity_type") == "comp_report"
            and d.get("entity_id") == int(report_id)
        ]
        payload = {"report": rpt, "comparables": comps, "documents": docs}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCompReportDetails",
                "description": "Fetch a comp report with its comparables and attached document(s).",
                "parameters": {
                    "type": "object",
                    "properties": {"report_id": {"type": "integer"}},
                    "required": ["report_id"],
                },
            },
        }


class UpdateCompReportStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], report_id: int, status: str) -> str:
        rpt = next(
            (
                r
                for r in data.get("comp_reports", [])
                if r.get("report_id") == int(report_id)
            ),
            None,
        )
        if not rpt:
            payload = {"error": f"Report {report_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        rpt["status"] = status
        payload = {"report_id": report_id, "status": status}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCompReportStatus",
                "description": "Update the status of a comp report.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
                        "status": {"type": "string"},
                    },
                    "required": ["report_id", "status"],
                },
            },
        }


class CreateCampaign(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, ctype: str = None, created_by: str = None,
    type: Any = None,
    ) -> str:
        c = data.get("campaigns", [])
        new_id = _next_int_id(c, "campaign_id")
        row = {
            "campaign_id": new_id,
            "name": name,
            "type": ctype,
            "created_by": created_by,
            "created_at": _fixed_now_iso(),
        }
        c.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCampaign",
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


class GetCampaignDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str, type: Any = None) -> str:
        c = next(
            (x for x in data.get("campaigns", []) if x.get("campaign_id") == campaign_id), None
        )
        if not c:
            payload = {"error": f"campaign_id {campaign_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = c
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCampaignDetails",
                "description": "Fetch a campaign row by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "integer"}},
                    "required": ["campaign_id"],
                },
            },
        }


class RenderClientEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], template_code: str, client_id: str, subject: str = None, slug: str = None) -> str:
        subject = subject or template_code
        slug = slug or f"{template_code}_{client_id}".lower().replace(" ", "_")
        body_uri = f"https://storage.example.com/emails/{slug}.html"
        payload = {
            "client_id": client_id,
            "subject": subject,
            "body_uri": body_uri,
            "template_code": template_code,
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
                "name": "RenderClientEmail",
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


class SendEmail(Tool):
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
        emails = data.get("emails", [])
        new_email_id = _next_int_id(emails, "email_id")
        row = {
            "email_id": new_email_id,
            "client_id": client_id,
            "broker_id": broker_id,
            "subject": subject,
            "body_uri": body_uri,
            "template_code": template_code,
            "sent_at": _fixed_now_iso(),
            "campaign_id": campaign_id,
        }
        emails.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
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
                    "required": [
                        "client_id",
                        "broker_id",
                        "subject",
                        "body_uri",
                        "template_code",
                    ],
                },
            },
        }


class GetEmailsForClient(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None) -> str:
        rows = [e for e in (data.get("emails") or []) if e.get("client_id") == client_id]
        payload = {"client_id": client_id, "emails": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmailsForClient",
                "description": "List all emails for a client.",
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }


class CreateCalendarEvent(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], broker_id: str = None, client_id: str = None, title: str = None, start_at: str = None, end_at: str = None, location: str = None, notes: str = None, source: str = None) -> str:
        events = data.get("calendar_events", [])
        new_id = _next_int_id(events, "event_id")
        row = {
            "event_id": new_id,
            "broker_id": broker_id,
            "client_id": client_id,
            "title": title,
            "start_at": start_at,
            "end_at": end_at,
            "location": location,
            "notes": notes,
            "source": source,
        }
        events.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCalendarEvent",
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
                    "required": [
                        "broker_id",
                        "client_id",
                        "title",
                        "start_at",
                        "end_at",
                        "location",
                        "source",
                    ],
                },
            },
        }


class GetCalendarEventsForClient(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None) -> str:
        rows = [e for e in data.get("calendar_events", []) if e.get("client_id") == client_id]
        payload = {"client_id": client_id, "events": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCalendarEventsForClient",
                "description": "List calendar events for a client.",
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }


class FetchOpenHousesByProperties(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], property_ids: list = None, date_from: str = None, date_to: str = None) -> str:
        pids = set(property_ids or [])
        rows = []
        for oh in data.get("open_houses", []) or []:
            if pids and oh.get("property_id") not in pids:
                continue
            dt = oh.get("start_at", "")
            if date_from and dt < f"{date_from}T00:00:00Z":
                continue
            if date_to and dt > f"{date_to}T23:59:59Z":
                continue
            rows.append(oh)
        payload = {"matches": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchOpenHousesByProperties",
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


class BuildRoute(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        client_id: str = None,
        date: str = None,
        stops_ordered_json: str = None,
        map_url: str = None,
        created_by_broker_id: str = None
    ) -> str:
        routes = data.get("routes", [])
        new_id = _next_int_id(routes, "route_id")
        row = {
            "route_id": new_id,
            "client_id": client_id,
            "date": date,
            "stops_ordered_json": stops_ordered_json,
            "map_url": map_url or f"https://maps.google.com/route/route_{new_id:03d}",
            "created_by_broker_id": created_by_broker_id,
            "created_at": _fixed_now_iso(),
        }
        routes.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildRoute",
                "description": "Persist a route with ordered stops and a map link.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "date": {"type": "string"},
                        "stops_ordered_json": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "map_url": {"type": "string"},
                        "created_by_broker_id": {"type": "integer"},
                    },
                    "required": [
                        "client_id",
                        "date",
                        "stops_ordered_json",
                        "created_by_broker_id",
                    ],
                },
            },
        }


class GetRouteDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], route_id: str = None) -> str:
        rid = route_id
        r = next((x for x in data.get("routes", []) if x.get("route_id") == rid), None)
        if not r:
            payload = {"error": f"route_id {rid} not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = r
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRouteDetails",
                "description": "Fetch a route by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"route_id": {"type": "integer"}},
                    "required": ["route_id"],
                },
            },
        }


class DraftSellerBrokerEmails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None, property_ids: list = None) -> str:
        props = property_ids or []
        drafts_uri = f"https://storage.example.com/drafts/client_{client_id}_props_{len(props)}.pdf"
        payload = {"client_id": client_id, "property_ids": props, "drafts_uri": drafts_uri}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DraftSellerBrokerEmails",
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


class PostAuditEvent(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        actor_id: str = None,
        action: str = None,
        entity_type: str = None,
        entity_id: str = None,
        metadata_json: dict = None
    ) -> str:
        audits = data.get("audit_events", [])
        new_id = _next_int_id(audits, "event_id")
        row = {
            "event_id": new_id,
            "actor_id": actor_id,
            "action": action,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "occurred_at": _fixed_now_iso(),
            "metadata_json": metadata_json or {},
        }
        audits.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PostAuditEvent",
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


class ListListingsByIds(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], listing_ids: list = None) -> str:
        ids = set(listing_ids or [])
        props = _index_by(data.get("properties", []), "property_id")
        out = []
        for lst in data.get("listings", []) or []:
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


class GetOpenHouseWindowsForNeighborhoods(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], neighborhood_ids: list[int] = None) -> str:
        nids = set(neighborhood_ids or [])
        props = [
            p for p in data.get("properties", []) if p.get("neighborhood_id") in nids
        ]
        prop_ids = {p.get("property_id") for p in props}
        rows = [
            oh
            for oh in data.get("open_houses", [])
            if oh.get("property_id") in prop_ids
        ]
        payload = {"neighborhood_ids": list(nids), "open_houses": rows}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOpenHouseWindowsForNeighborhoods",
                "description": "Fetch open house windows for neighborhoods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "neighborhood_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                        }
                    },
                    "required": ["neighborhood_ids"],
                },
            },
        }


class CheckDriveTimeConstraints(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], property_ids: list = None, max_minutes: int = 30) -> str:
        stops = property_ids or []
        hops = [
            {"from": stops[i], "to": stops[i + 1], "minutes": 20}
            for i in range(max(0, len(stops) - 1))
        ]
        ok = all(h["minutes"] <= max_minutes for h in hops)
        payload = {"ok": ok, "hops": hops, "max_minutes": max_minutes}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckDriveTimeConstraints",
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


class GenerateBriefingDoc(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: int, broker_id: int, version_tag: str = "v1",
    property_id: Any = None,
    doc_type: Any = None
    ) -> str:
        documents = data.get("documents", [])
        new_id = _next_int_id(documents, "document_id")
        file_uri = f"https://storage.example.com/briefings/client_briefing_{client_id:03d}_{version_tag}.pdf"
        row = {
            "document_id": new_id,
            "entity_type": "client",
            "entity_id": client_id,
            "doc_type": "briefing_doc",
            "file_uri": file_uri,
            "created_by": broker_id,
            "created_at": _fixed_now_iso(),
        }
        documents.append(row)
        payload = {"document_id": new_id, "file_uri": file_uri}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateBriefingDoc",
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


class AttachDocumentToClient(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str, doc_type: str = "briefing_doc", file_uri: str = None, created_by: str = None, property_id: Any = None,
    document_id: Any = None,
    ) -> str:
        documents = data.get("documents", [])
        new_id = _next_int_id(documents, "document_id")
        row = {
            "document_id": new_id,
            "entity_type": "client",
            "entity_id": client_id,
            "doc_type": doc_type,
            "file_uri": file_uri,
            "created_by": created_by,
            "created_at": _fixed_now_iso(),
        }
        documents.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AttachDocumentToClient",
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


TOOLS = [
    GetClientPreferences(),
    GetMortgageProfile(),
    GetPropertyAndListing(),
    SearchListings(),
    SearchListingsInNeighborhoods(),
    GetNeighborhoodDetails(),
    GetBorderingNeighborhoods(),
    GetBrokerDetails(),
    ComputeMortgageEstimate(),
    FetchRecentSalesByProperty(),
    SaveCompReport(),
    GetCompReportDetails(),
    UpdateCompReportStatus(),
    CreateCampaign(),
    GetCampaignDetails(),
    RenderClientEmail(),
    SendEmail(),
    GetEmailsForClient(),
    CreateCalendarEvent(),
    GetCalendarEventsForClient(),
    FetchOpenHousesByProperties(),
    BuildRoute(),
    GetRouteDetails(),
    DraftSellerBrokerEmails(),
    PostAuditEvent(),
    ListListingsByIds(),
    GetOpenHouseWindowsForNeighborhoods(),
    CheckDriveTimeConstraints(),
    GenerateBriefingDoc(),
    AttachDocumentToClient(),
]
