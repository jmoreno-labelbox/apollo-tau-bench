from typing import Dict, Any, List, Optional
from domains.dto import Tool
import json
from datetime import datetime

# Helpers
def _now_iso() -> str:
    return "2025-08-20T00:00:00Z"

def _by_key(items: List[Dict[str, Any]], key: str) -> Dict[Any, Dict[str, Any]]:
    return {i.get(key): i for i in (items or [])}

# ─────────────────
# Projects & Rates
# ─────────────────

class ListProjectsCatalog(Tool):
    """List all projects."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"projects": data.get("projects", [])}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "list_projects_catalog",
            "description": "List projects.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }}

class FetchProjectCard(Tool):
    """Fetch project by project_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pid = kwargs.get("project_id")
        row = next((p for p in data.get("projects", []) if p.get("project_id") == pid), None)
        if not row:
            return json.dumps({"error": f"project_id '{pid}' not found"}, indent=2)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "fetch_project_card",
            "description": "Fetch a project by id.",
            "parameters": {"type": "object", "properties": {"project_id": {"type": "string"}}, "required": ["project_id"]}
        }}

class AddProjectCard(Tool):
    """Create a new project row."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        projects = data.get("projects", [])
        row = {
            "project_id": kwargs.get("project_id"),
            "publisher_id": kwargs.get("publisher_id"),
            "isbn": kwargs.get("isbn"),
            "project_title": kwargs.get("project_title"),
            "default_hourly_rate": kwargs.get("default_hourly_rate"),
            "override_hourly_rate": kwargs.get("override_hourly_rate"),
            "account_code": kwargs.get("account_code"),
            "is_active": kwargs.get("is_active", True),
            "created_at": _now_iso(),
            "updated_at": _now_iso()
        }
        projects.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "add_project_card",
            "description": "Create a project.",
            "parameters": {"type": "object", "properties": {
                "project_id": {"type": "string"},
                "publisher_id": {"type": "string"},
                "isbn": {"type": "string"},
                "project_title": {"type": "string"},
                "default_hourly_rate": {"type": "number"},
                "override_hourly_rate": {"type": ["number", "null"]},
                "account_code": {"type": ["string", "null"]},
                "is_active": {"type": "boolean"}
            }, "required": ["project_id", "publisher_id", "isbn", "project_title", "default_hourly_rate"]}
        }}

class MapHourlyRates(Tool):
    """Resolve hourly rate per project (override → default)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_ids = kwargs.get("project_id_list") or []
        projects = _by_key(data.get("projects", []), "project_id")
        rate_map = {pid: (projects.get(pid, {}).get("override_hourly_rate")
                          or projects.get(pid, {}).get("default_hourly_rate") or 0)
                    for pid in project_ids}
        return json.dumps({"rate_map": rate_map}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "map_hourly_rates",
            "description": "Resolve hourly rate for each project.",
            "parameters": {"type": "object", "properties": {
                "project_id_list": {"type": "array", "items": {"type": "string"}}
            }, "required": ["project_id_list"]}
        }}

# ───────────────
# Time & Invoicing
# ───────────────

class ReadTimeEntries(Tool):
    """Fetch time entries for projects within a date window."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        prj_ids = set(kwargs.get("project_id_list") or [])
        start = kwargs.get("period_start")
        end = kwargs.get("period_end")
        out = []
        for t in data.get("time_entries", []) or []:
            if prj_ids and t.get("project_id") not in prj_ids:
                continue
            if start and t.get("entry_date", "") < start:
                continue
            if end and t.get("entry_date", "") > end:
                continue
            out.append(t)
        return json.dumps({"rows": out}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_time_entries",
            "description": "Fetch time entries by project and period.",
            "parameters": {"type": "object", "properties": {
                "project_id_list": {"type": "array", "items": {"type": "string"}},
                "period_start": {"type": "string"},
                "period_end": {"type": "string"}
            }, "required": ["project_id_list", "period_start", "period_end"]}
        }}

class AuditTimeEntries(Tool):
    """Validate the presence of ISBN and account_code for billable entries."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = kwargs.get("rows") or []
        missing = [r for r in rows
                   if not r.get("description") or not r.get("isbn") or not r.get("account_code")]
        return json.dumps({"valid": len(missing) == 0, "missing_count": len(missing)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "audit_time_entries",
            "description": "Ensure time entries have ISBN and account_code.",
            "parameters": {"type": "object", "properties": {
                "rows": {"type": "array", "items": {"type": "object"}}
            }, "required": ["rows"]}
        }}

class AggregateHoursByISBN(Tool):
    """Aggregate hours by ISBN within a set of time entries."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = kwargs.get("rows") or []
        grouped: Dict[str, float] = {}
        for r in rows:
            isbn = r.get("isbn")
            if not isbn:
                continue
            grouped[isbn] = grouped.get(isbn, 0.0) + float(r.get("hours_worked", 0.0))
        return json.dumps({"grouped_hours": grouped}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "aggregate_hours_by_isbn",
            "description": "Sum hours per ISBN.",
            "parameters": {"type": "object", "properties": {
                "rows": {"type": "array", "items": {"type": "object"}}
            }, "required": ["rows"]}
        }}

class ComputeInvoiceTotals(Tool):
    """Compute subtotal, HST, and total for invoice lines."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        lines = kwargs.get("lines") or []
        hst = float(kwargs.get("hst_rate", 0.13))
        subtotal = sum(float(l.get("hours", 0)) * float(l.get("rate", 0)) for l in lines)
        hst_amount = round(subtotal * hst, 2)
        total_due = round(subtotal + hst_amount, 2)
        return json.dumps({"subtotal": round(subtotal, 2),
                           "hst_amount": hst_amount,
                           "total_due": total_due}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "compute_invoice_totals",
            "description": "Compute invoice totals.",
            "parameters": {"type": "object", "properties": {
                "lines": {"type": "array", "items": {"type": "object"}},
                "hst_rate": {"type": "number"}
            }, "required": ["lines"]}
        }}

class CreateInvoiceRecord(Tool):
    """Insert a new invoice row and return its id and number."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoices = data.get("invoices", [])
        # Generate sequential invoice_id like INV001, INV002 ...
        prefix, max_num = "INV", 0
        for inv in invoices:
            s = str(inv.get("invoice_id", ""))
            if s.startswith(prefix):
                try:
                    max_num = max(max_num, int(s[len(prefix):]))
                except ValueError:
                    pass
        new_id = f"{prefix}{max_num + 1:03d}"

        row = {
            "invoice_id": new_id,
            "invoice_number": kwargs.get("invoice_number"),
            "publisher_id": kwargs.get("publisher_id"),
            "invoice_date": kwargs.get("invoice_date"),
            "period_start": kwargs.get("period_start"),
            "period_end": kwargs.get("period_end"),
            "subtotal": kwargs.get("subtotal"),
            "hst_amount": kwargs.get("hst_amount"),
            "total_due": kwargs.get("total_due"),
            "pdf_path": kwargs.get("pdf_path"),
            "sent_at": None,
            "paid_at": None,
            "created_at": _now_iso()
        }
        invoices.append(row)
        return json.dumps({"invoice_id": new_id, "invoice_number": row["invoice_number"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "create_invoice_record",
            "description": "Insert a new invoice row.",
            "parameters": {"type": "object", "properties": {
                "invoice_number": {"type": "string"},
                "publisher_id": {"type": "string"},
                "invoice_date": {"type": "string"},
                "period_start": {"type": "string"},
                "period_end": {"type": "string"},
                "subtotal": {"type": "number"},
                "hst_amount": {"type": "number"},
                "total_due": {"type": "number"},
                "pdf_path": {"type": "string"}
            }, "required": ["invoice_number", "publisher_id", "invoice_date",
                            "period_start", "period_end", "subtotal", "hst_amount", "total_due", "pdf_path"]}
        }}

class FetchInvoiceRecord(Tool):
    """Read an invoice by invoice_id or invoice_number."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invs = data.get("invoices", [])
        invoice_id = kwargs.get("invoice_id")
        invoice_number = kwargs.get("invoice_number")
        row = None
        if invoice_id is not None:
            row = next((i for i in invs if str(i.get("invoice_id")) == str(invoice_id)), None)
        elif invoice_number:
            row = next((i for i in invs if i.get("invoice_number") == invoice_number), None)
        if not row:
            return json.dumps({"error": "invoice not found"}, indent=2)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "fetch_invoice_record",
            "description": "Fetch invoice by id or number.",
            "parameters": {"type": "object", "properties": {
                "invoice_id": {"type": "string"},
                "invoice_number": {"type": "string"}
            }, "required": []}
        }}

class CreateInvoiceLines(Tool):
    """Insert invoice lines for an invoice."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoice_lines = data.get("invoice_lines", [])
        invs = data.get("invoices", [])
        invoice_id = kwargs.get("invoice_id")
        invoice_number = kwargs.get("invoice_number")
        if invoice_id is None and invoice_number:
            inv = next((i for i in invs if i.get("invoice_number") == invoice_number), None)
            if inv:
                invoice_id = inv.get("invoice_id")
        if invoice_id is None:
            return json.dumps({"error": "invoice_id or invoice_number required"}, indent=2)

        new_ids = []
        max_line_id = 0
        for line in invoice_lines:
            try:
                max_line_id = max(max_line_id, int(line.get("invoice_line_id", 0)))
            except (ValueError, TypeError):
                pass

        for ln in (kwargs.get("lines") or []):
            max_line_id += 1
            invoice_lines.append({
                "invoice_line_id": max_line_id,
                "invoice_id": invoice_id,
                "project_id": ln.get("project_id"),
                "isbn": ln.get("isbn"),
                "hours_billed": ln.get("hours"),
                "hourly_rate": ln.get("rate"),
                "line_amount": round(float(ln.get("hours", 0)) * float(ln.get("rate", 0)), 2)
            })
            new_ids.append(max_line_id)
        return json.dumps({"invoice_id": invoice_id, "inserted_line_ids": new_ids}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "create_invoice_lines",
            "description": "Insert lines for an invoice.",
            "parameters": {"type": "object", "properties": {
                "invoice_id": {"type": "string"},
                "invoice_number": {"type": "string"},
                "lines": {"type": "array", "items": {"type": "object"}}
            }, "required": ["lines"]}
        }}

class ListInvoiceLinesByInvoice(Tool):
    """List invoice lines for a given invoice."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoice_id = kwargs.get("invoice_id")
        invoice_number = kwargs.get("invoice_number")
        invs = data.get("invoices", [])
        if invoice_id is None and invoice_number:
            inv = next((i for i in invs if i.get("invoice_number") == invoice_number), None)
            if inv:
                invoice_id = inv.get("invoice_id")
        rows = [l for l in data.get("invoice_lines", []) if str(l.get("invoice_id")) == str(invoice_id)] if invoice_id else []
        return json.dumps({"invoice_id": invoice_id, "lines": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "list_invoice_lines_by_invoice",
            "description": "List lines for an invoice.",
            "parameters": {"type": "object", "properties": {
                "invoice_id": {"type": "string"},
                "invoice_number": {"type": "string"}
            }, "required": []}
        }}

class LogInvoiceEvent(Tool):
    """Append an audit event for an invoice (generated, emailed…)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        audits = data.get("invoice_audit", [])
        # New audit_id like AUD001, AUD002 ...
        prefix, max_num = "AUD", 0
        for a in audits:
            s = str(a.get("audit_id", ""))
            if s.startswith(prefix):
                try:
                    max_num = max(max_num, int(s[len(prefix):]))
                except ValueError:
                    pass
        new_id = f"{prefix}{max_num + 1:03d}"
        row = {
            "audit_id": new_id,
            "invoice_id": kwargs.get("invoice_id"),
            "invoice_number": kwargs.get("invoice_number"),
            "event_type": kwargs.get("event_type"),
            "event_timestamp": _now_iso(),
            "notes": kwargs.get("notes")
        }
        audits.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "log_invoice_event",
            "description": "Record an audit event for an invoice.",
            "parameters": {"type": "object", "properties": {
                "invoice_id": {"type": "string"},
                "invoice_number": {"type": "string"},
                "event_type": {"type": "string"},
                "notes": {"type": "string"}
            }, "required": ["event_type"]}
        }}

class ListInvoiceEvents(Tool):
    """List all audit events for an invoice."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inv_id = kwargs.get("invoice_id")
        inv_no = kwargs.get("invoice_number")
        events = []
        for a in data.get("invoice_audit", []) or []:
            if inv_id and str(a.get("invoice_id")) == str(inv_id):
                events.append(a)
            elif inv_no and a.get("invoice_number") == inv_no:
                events.append(a)
        return json.dumps({"events": events}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "list_invoice_events",
            "description": "List audit events by invoice id or number.",
            "parameters": {"type": "object", "properties": {
                "invoice_id": {"type": "string"},
                "invoice_number": {"type": "string"}
            }, "required": []}
        }}

class DispatchInvoiceEmail(Tool):
    """Send an invoice email and (if provided) mark the invoice as sent."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        publisher_id = kwargs.get("publisher_id")
        consultant_id = kwargs.get("consultant_id")
        subject = kwargs.get("subject")
        body_text = kwargs.get("body_text")
        attachment = kwargs.get("attachment")
        inv_no = kwargs.get("invoice_number")

        if inv_no:
            inv = next((i for i in data.get("invoices", []) if i.get("invoice_number") == inv_no), None)
            if inv:
                inv["sent_at"] = _now_iso()

        return json.dumps({"status": "sent",
                           "publisher_id": publisher_id,
                           "consultant_id": consultant_id,
                           "subject": subject,
                           "attachment": attachment}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "dispatch_invoice_email",
            "description": "Send invoice email to client, CC consultant.",
            "parameters": {"type": "object", "properties": {
                "publisher_id": {"type": "string"},
                "consultant_id": {"type": "string"},
                "invoice_number": {"type": "string"},
                "subject": {"type": "string"},
                "body_text": {"type": "string"},
                "attachment": {"type": "string"}
            }, "required": ["publisher_id", "consultant_id", "subject", "body_text", "attachment"]}
        }}

class QueryInvoices(Tool):
    """Filter invoices by status/publisher/date range."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = data.get("invoices", []) or []
        status = kwargs.get("status")
        pid = kwargs.get("publisher_id")
        start = kwargs.get("date_from")
        end = kwargs.get("date_to")
        out = []
        for r in rows:
            if status == "open" and r.get("paid_at") is not None:
                continue
            if pid and r.get("publisher_id") != pid:
                continue
            if start and r.get("invoice_date", "") < start:
                continue
            if end and r.get("invoice_date", "") > end:
                continue
            out.append(r)
        return json.dumps({"invoices": out}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "query_invoices",
            "description": "Fetch invoices with filters.",
            "parameters": {"type": "object", "properties": {
                "status": {"type": "string"},
                "publisher_id": {"type": "string"},
                "date_from": {"type": "string"},
                "date_to": {"type": "string"}
            }, "required": []}
        }}

# ───────────────────────────────
# Consultant & Client (Publisher)
# ───────────────────────────────

class FetchConsultantProfile(Tool):
    """Return the consultant profile row by consultant_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("consultant_id")
        row = next((c for c in data.get("consultants", []) if c.get("consultant_id") == cid), None)
        if not row:
            return json.dumps({"error": f"consultant_id '{cid}' not found"}, indent=2)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "fetch_consultant_profile",
            "description": "Fetch a consultant profile.",
            "parameters": {"type": "object", "properties": {"consultant_id": {"type": "string"}}, "required": ["consultant_id"]}
        }}

class MutateConsultantContact(Tool):
    """Update consultant contact fields."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("consultant_id")
        updates = {k: v for k, v in kwargs.items() if k in {"address", "phone", "email", "gst_number"}}
        row = next((c for c in data.get("consultants", []) if c.get("consultant_id") == cid), None)
        if not row:
            return json.dumps({"error": f"consultant_id '{cid}' not found"}, indent=2)
        row.update(updates)
        row["updated_at"] = _now_iso()
        return json.dumps({"consultant_id": cid, "updated": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "mutate_consultant_contact",
            "description": "Update contact fields for a consultant.",
            "parameters": {"type": "object", "properties": {
                "consultant_id": {"type": "string"},
                "address": {"type": "string"},
                "phone": {"type": "string"},
                "email": {"type": "string"},
                "gst_number": {"type": "string"}
            }, "required": ["consultant_id"]}
        }}

class FetchClientProfile(Tool):
    """Read a client/publisher row by publisher_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pid = kwargs.get("publisher_id")
        row = next((p for p in data.get("publishers", []) if p.get("publisher_id") == pid), None)
        if not row:
            return json.dumps({"error": f"publisher_id '{pid}' not found"}, indent=2)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "fetch_client_profile",
            "description": "Fetch a client/publisher record.",
            "parameters": {"type": "object", "properties": {"publisher_id": {"type": "string"}}, "required": ["publisher_id"]}
        }}

class AddClientProfile(Tool):
    """Create a new client/publisher row."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tbl = data.get("publishers", [])
        row = {
            "publisher_id": kwargs.get("publisher_id"),
            "name": kwargs.get("name"),
            "address": kwargs.get("address"),
            "contact_email": kwargs.get("contact_email"),
            "gst_number": kwargs.get("gst_number"),
            "created_at": _now_iso(),
            "updated_at": _now_iso()
        }
        tbl.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "add_client_profile",
            "description": "Create a client/publisher row.",
            "parameters": {"type": "object", "properties": {
                "publisher_id": {"type": "string"},
                "name": {"type": "string"},
                "address": {"type": "string"},
                "contact_email": {"type": "string"},
                "gst_number": {"type": "string"}
            }, "required": ["publisher_id", "name"]}
        }}

class MutateClientContact(Tool):
    """Update client contact fields."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pid = kwargs.get("publisher_id")
        row = next((p for p in data.get("publishers", []) if p.get("publisher_id") == pid), None)
        if not row:
            return json.dumps({"error": f"publisher_id '{pid}' not found"}, indent=2)
        updates = {k: v for k, v in kwargs.items() if k in {"address", "contact_email", "gst_number"}}
        row.update(updates)
        row["updated_at"] = _now_iso()
        return json.dumps({"publisher_id": pid, "updated": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "mutate_client_contact",
            "description": "Update a client's contact info.",
            "parameters": {"type": "object", "properties": {
                "publisher_id": {"type": "string"},
                "address": {"type": "string"},
                "contact_email": {"type": "string"},
                "gst_number": {"type": "string"}
            }, "required": ["publisher_id"]}
        }}

# ───────────
# KPIs
# ───────────

class DeriveDaysOutstanding(Tool):
    """Compute days outstanding for each invoice given an as-of date."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        today = kwargs.get("today") or "2025-08-20"
        invs = kwargs.get("invoices") or []
        out = []
        for r in invs:
            due = r.get("period_end") or r.get("invoice_date")
            due_iso = (due[:10] if isinstance(due, str) and len(due) > 10 else due)
            ds = (datetime.fromisoformat(today) - datetime.fromisoformat(due_iso)).days
            out.append({"invoice_number": r.get("invoice_number"), "days_outstanding": ds})
        return json.dumps({"aging": out}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "derive_days_outstanding",
            "description": "Compute days outstanding as of a given date.",
            "parameters": {"type": "object", "properties": {
                "invoices": {"type": "array", "items": {"type": "object"}},
                "today": {"type": "string"}
            }, "required": ["invoices"]}
        }}

class BucketizeAging(Tool):
    """Map days outstanding to standard Accounts Receivable aging buckets."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aging = kwargs.get("aging") or []
        buckets = []
        for a in aging:
            days = int(a.get("days_outstanding", 0))
            if days < 0 and days >= -7:
                b = "upcoming_due"
            elif 0 <= days <= 30:
                b = "0-30"
            elif 31 <= days <= 60:
                b = "31-60"
            elif 61 <= days <= 90:
                b = "61-90"
            elif days > 90:
                b = "90+"
            else:
                b = "not_due"
            buckets.append({"invoice_number": a.get("invoice_number"), "bucket": b})
        return json.dumps({"buckets": buckets}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "bucketize_aging",
            "description": "Convert days-outstanding to buckets (incl. 'upcoming_due').",
            "parameters": {"type": "object", "properties": {
                "aging": {"type": "array", "items": {"type": "object"}}
            }, "required": ["aging"]}
        }}

class SummarizeReceivablesByClient(Tool):
    """Summarize Accounts Receivable by client and bucket."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoices = kwargs.get("invoices") or []
        summary: Dict[str, Dict[str, float]] = {}
        for inv in invoices:
            pid = inv.get("publisher_id")
            bucket = inv.get("aging_bucket", "0-30")
            amt = float(inv.get("total_due", 0))
            summary.setdefault(pid, {})
            summary[pid][bucket] = summary[pid].get(bucket, 0.0) + amt
        return json.dumps({"summary_by_publisher": summary}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "summarize_receivables_by_client",
            "description": "Summarize receivables by publisher and aging bucket.",
            "parameters": {"type": "object", "properties": {
                "invoices": {"type": "array", "items": {"type": "object"}}
            }, "required": ["invoices"]}
        }}

class DeriveCollectionKPIs(Tool):
    """Compute collection KPIs (Total Accounts Receivable, avg daily sales, DSO)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        window_months = int(kwargs.get("window_months", 12))
        invs = data.get("invoices", []) or []
        total_ar = sum(float(i.get("total_due", 0)) for i in invs if i.get("paid_at") is None)
        avg_daily_sales = round((sum(float(i.get("subtotal", 0)) for i in invs) / max(1, window_months * 30)), 2)
        dso = round((total_ar / max(0.01, avg_daily_sales)), 2)
        return json.dumps({"window_months": window_months,
                           "total_ar": round(total_ar, 2),
                           "avg_daily_sales": avg_daily_sales,
                           "dso": dso}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "derive_collection_kpis",
            "description": "Compute collection KPIs over a window.",
            "parameters": {"type": "object", "properties": {
                "window_months": {"type": "integer"}
            }, "required": []}
        }}

class RenderAccountsReceivableReport(Tool):
    """Return a PDF path for the Accounts Receivable Aging report."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        period_label = kwargs.get("period_label")
        pdf_path = f"https://test.storage.com/reports/accounts_receivable_{period_label}.pdf"
        return json.dumps({"pdf_path": pdf_path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "render_accounts_receivable_report",
            "description": "Export an Accounts Receivable Aging report and return the PDF path.",
            "parameters": {"type": "object", "properties": {
                "period_label": {"type": "string"}
            }, "required": ["period_label"]}
        }}

# ────────────────
# Dashboards
# ────────────────

class CreateDashboardSnapshot(Tool):
    """Create a dashboard snapshot record."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        snaps = data.get("dashboard_snapshots", [])
        max_id = 0
        for s in snaps:
            try:
                max_id = max(max_id, int(s.get("snapshot_id", 0)))
            except (ValueError, TypeError):
                pass
        new_id = max_id + 1
        row = {
            "snapshot_id": new_id,
            "snapshot_date": kwargs.get("snapshot_date"),
            "ytd_revenue": kwargs.get("ytd_revenue"),
            "ytd_tax_reserve": kwargs.get("ytd_tax_reserve"),
            "pdf_path": kwargs.get("pdf_path")
        }
        snaps.append(row)
        return json.dumps({"snapshot_id": new_id, "snapshot_date": row["snapshot_date"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "create_dashboard_snapshot",
            "description": "Insert a dashboard snapshot.",
            "parameters": {"type": "object", "properties": {
                "snapshot_date": {"type": "string"},
                "ytd_revenue": {"type": "number"},
                "ytd_tax_reserve": {"type": "number"},
                "pdf_path": {"type": "string"}
            }, "required": ["snapshot_date"]}
        }}

class FetchDashboardSnapshot(Tool):
    """Fetch a dashboard snapshot by id or date."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        snaps = data.get("dashboard_snapshots", [])
        sid = kwargs.get("snapshot_id")
        sdate = kwargs.get("snapshot_date")
        row = None
        if sid is not None:
            row = next((s for s in snaps if str(s.get("snapshot_id")) == str(sid)), None)
        elif sdate:
            row = next((s for s in snaps if s.get("snapshot_date") == sdate), None)
        if not row:
            return json.dumps({"error": "snapshot not found"}, indent=2)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "fetch_dashboard_snapshot",
            "description": "Read a snapshot by id or date.",
            "parameters": {"type": "object", "properties": {
                "snapshot_id": {"type": "string"},
                "snapshot_date": {"type": "string"}
            }, "required": []}
        }}

class AppendProjectRevenueRows(Tool):
    """Insert project revenue rows for a given snapshot."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows_tbl = data.get("project_revenue", [])
        snapshot_id = kwargs.get("snapshot_id")
        items = kwargs.get("items") or []
        inserted = []

        max_id = 0
        for r in rows_tbl:
            try:
                max_id = max(max_id, int(r.get("row_id", 0)))
            except (ValueError, TypeError):
                pass

        for it in items:
            max_id += 1
            rows_tbl.append({
                "row_id": max_id,
                "snapshot_id": snapshot_id,
                "project_id": it.get("project_id"),
                "ytd_revenue": it.get("ytd_revenue")
            })
            inserted.append(max_id)
        return json.dumps({"snapshot_id": snapshot_id, "inserted_row_ids": inserted}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "append_project_revenue_rows",
            "description": "Insert project revenue items for a snapshot.",
            "parameters": {"type": "object", "properties": {
                "snapshot_id": {"type": "string"},
                "items": {"type": "array", "items": {"type": "object"}}
            }, "required": ["snapshot_id", "items"]}
        }}

class AppendMonthlyRevenueRows(Tool):
    """Insert monthly revenue rows for a snapshot."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows_tbl = data.get("monthly_revenue", [])
        snapshot_id = kwargs.get("snapshot_id")
        items = kwargs.get("items") or []
        inserted = []

        max_id = 0
        for r in rows_tbl:
            try:
                max_id = max(max_id, int(r.get("row_id", 0)))
            except (ValueError, TypeError):
                pass

        for it in items:
            max_id += 1
            rows_tbl.append({
                "row_id": max_id,
                "snapshot_id": snapshot_id,
                "month_year": it.get("month_year"),
                "revenue": it.get("revenue"),
                "tax_reserve": it.get("tax_reserve"),
                "profit_flag": it.get("profit_flag")
            })
            inserted.append(max_id)
        return json.dumps({"snapshot_id": snapshot_id, "inserted_row_ids": inserted}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "append_monthly_revenue_rows",
            "description": "Monthly revenue items.",
            "parameters": {"type": "object", "properties": {
                "snapshot_id": {"type": "string"},
                "items": {"type": "array", "items": {"type": "object"}}
            }, "required": ["snapshot_id", "items"]}
        }}

# ─────────────
# Registry
# ─────────────
TOOLS = [
    #KPIs
    DeriveDaysOutstanding(),
    BucketizeAging(),
    DeriveCollectionKPIs(),
    SummarizeReceivablesByClient(),
    RenderAccountsReceivableReport(),

    # Invoicing core
    CreateInvoiceRecord(),
    ComputeInvoiceTotals(),
    FetchInvoiceRecord(),
    CreateInvoiceLines(),
    ListInvoiceLinesByInvoice(),
    LogInvoiceEvent(),
    ListInvoiceEvents(),
    DispatchInvoiceEmail(),
    QueryInvoices(),

    # Projects & rates
    AddProjectCard(),
    FetchProjectCard(),
    ListProjectsCatalog(),
    MapHourlyRates(),

    # Time tracking
    ReadTimeEntries(),
    AuditTimeEntries(),
    AggregateHoursByISBN(),

    # Consultant & client
    FetchConsultantProfile(),
    MutateConsultantContact(),
    AddClientProfile(),
    FetchClientProfile(),
    MutateClientContact(),

    # Dashboards & revenue
    CreateDashboardSnapshot(),
    FetchDashboardSnapshot(),
    AppendProjectRevenueRows(),
    AppendMonthlyRevenueRows(),
]
