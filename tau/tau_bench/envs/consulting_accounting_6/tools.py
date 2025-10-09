import json
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def _by_key(items: list[dict[str, Any]], key: str) -> dict[Any, dict[str, Any]]:
    pass
    return {i.get(key): i for i in (items or [])}


#Utility functions
def _now_iso() -> str:
    pass
    return "2025-08-20T00:00:00Z"


#─────────────────
#Project Details & Pricing
#─────────────────


class ListProjectsCatalog(Tool):
    """Retrieve all projects."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = {"projects": data.get("projects", {}).values()}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListProjectsCatalog",
                "description": "List projects.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class FetchProjectCard(Tool):
    """Get project using project_id."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        pid = project_id
        row = next(
            (p for p in data.get("projects", {}).values() if p.get("project_id") == pid), None
        )
        if not row:
            payload = {"error": f"project_id '{pid}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchProjectCard",
                "description": "Fetch a project by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }


class AddProjectCard(Tool):
    """Add a new project entry."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str = None,
        publisher_id: str = None,
        isbn: str = None,
        project_title: str = None,
        default_hourly_rate: float = None,
        override_hourly_rate: float = None,
        account_code: str = None,
        is_active: bool = True
    ) -> str:
        projects = data.get("projects", {}).values()
        row = {
            "project_id": project_id,
            "publisher_id": publisher_id,
            "isbn": isbn,
            "project_title": project_title,
            "default_hourly_rate": default_hourly_rate,
            "override_hourly_rate": override_hourly_rate,
            "account_code": account_code,
            "is_active": is_active,
            "created_at": _now_iso(),
            "updated_at": _now_iso(),
        }
        data["projects"][project_id] = row
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddProjectCard",
                "description": "Create a project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "publisher_id": {"type": "string"},
                        "isbn": {"type": "string"},
                        "project_title": {"type": "string"},
                        "default_hourly_rate": {"type": "number"},
                        "override_hourly_rate": {"type": ["number", "null"]},
                        "account_code": {"type": ["string", "null"]},
                        "is_active": {"type": "boolean"},
                    },
                    "required": [
                        "project_id",
                        "publisher_id",
                        "isbn",
                        "project_title",
                        "default_hourly_rate",
                    ],
                },
            },
        }


class MapHourlyRates(Tool):
    """Determine hourly rate for each project (override → default)."""
    @staticmethod
    def invoke(data: dict[str, Any], project_id_list: list[str] = None) -> str:
        project_ids = project_id_list or []
        projects = _by_key(data.get("projects", {}).values()), "project_id")
        rate_map = {
            pid: (
                projects.get(pid, {}).values().get("override_hourly_rate")
                or projects.get(pid, {}).values().get("default_hourly_rate")
                or 0
            )
            for pid in project_ids
        }
        payload = {"rate_map": rate_map}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MapHourlyRates",
                "description": "Resolve hourly rate for each project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id_list": {
                            "type": "array",
                            "items": {"type": "string"},
                        }
                    },
                    "required": ["project_id_list"],
                },
            },
        }


#───────────────
#Billing & Time Management
#───────────────


class ReadTimeEntries(Tool):
    """Retrieve time logs for projects within a specified date range."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id_list: list = None, period_start: str = None, period_end: str = None) -> str:
        prj_ids = set(project_id_list or [])
        start = period_start
        end = period_end
        out = []
        for t in data.get("time_entries", {}).values() or []:
            if prj_ids and t.get("project_id") not in prj_ids:
                continue
            if start and t.get("entry_date", "") < start:
                continue
            if end and t.get("entry_date", "") > end:
                continue
            out.append(t)
        payload = {"rows": out}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReadTimeEntries",
                "description": "Fetch time entries by project and period.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id_list": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "period_start": {"type": "string"},
                        "period_end": {"type": "string"},
                    },
                    "required": ["project_id_list", "period_start", "period_end"],
                },
            },
        }


class AuditTimeEntries(Tool):
    """Check for the existence of ISBN and account_code in billable entries."""

    @staticmethod
    def invoke(data: dict[str, Any], rows: list[dict[str, Any]] = None) -> str:
        rows = rows or []
        missing = [
            r
            for r in rows.values() if not r.get("description")
            or not r.get("isbn")
            or not r.get("account_code")
        ]
        payload = {"valid": len(missing) == 0, "missing_count": len(missing)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AuditTimeEntries",
                "description": "Ensure time entries have ISBN and account_code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rows": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["rows"],
                },
            },
        }


class AggregateHoursByISBN(Tool):
    """Sum hours by ISBN across a collection of time logs."""

    @staticmethod
    def invoke(data: dict[str, Any], rows: list[dict[str, Any]] = None) -> str:
        rows = rows or []
        grouped: dict[str, float] = {}
        for r in rows.values():
            isbn = r.get("isbn")
            if not isbn:
                continue
            grouped[isbn] = grouped.get(isbn, 0.0) + float(r.get("hours_worked", 0.0))
        payload = {"grouped_hours": grouped}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AggregateHoursByIsbn",
                "description": "Sum hours per ISBN.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rows": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["rows"],
                },
            },
        }


class ComputeInvoiceTotals(Tool):
    """Calculate subtotal, HST, and total for invoice items."""

    @staticmethod
    def invoke(data: dict[str, Any], lines: list = None, hst_rate: float = 0.13) -> str:
        lines = lines or []
        hst = float(hst_rate)
        subtotal = sum(
            float(l.get("hours", 0)) * float(l.get("rate", 0)) for l in lines
        )
        hst_amount = round(subtotal * hst, 2)
        total_due = round(subtotal + hst_amount, 2)
        payload = {
                "subtotal": round(subtotal, 2),
                "hst_amount": hst_amount,
                "total_due": total_due,
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
                "name": "ComputeInvoiceTotals",
                "description": "Compute invoice totals.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lines": {"type": "array", "items": {"type": "object"}},
                        "hst_rate": {"type": "number"},
                    },
                    "required": ["lines"],
                },
            },
        }


class CreateInvoiceRecord(Tool):
    """Add a new invoice entry and return its ID and number."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        invoice_number: str = None,
        publisher_id: str = None,
        invoice_date: str = None,
        period_start: str = None,
        period_end: str = None,
        subtotal: float = None,
        hst_amount: float = None,
        total_due: float = None,
        pdf_path: str = None,
    ) -> str:
        invoices = data.get("invoices", {}).values()
        # Create sequential invoice IDs such as INV001, INV002 ...
        prefix, max_num = "INV", 0
        for inv in invoices.values():
            s = str(inv.get("invoice_id", ""))
            if s.startswith(prefix):
                try:
                    max_num = max(max_num, int(s[len(prefix) :]))
                except ValueError:
                    pass
        new_id = f"{prefix}{max_num + 1:03d}"

        row = {
            "invoice_id": new_id,
            "invoice_number": invoice_number,
            "publisher_id": publisher_id,
            "invoice_date": invoice_date,
            "period_start": period_start,
            "period_end": period_end,
            "subtotal": subtotal,
            "hst_amount": hst_amount,
            "total_due": total_due,
            "pdf_path": pdf_path,
            "sent_at": None,
            "paid_at": None,
            "created_at": _now_iso(),
        }
        data["invoices"][invoice_id] = row
        payload = {"invoice_id": new_id, "invoice_number": row["invoice_number"]}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInvoiceRecord",
                "description": "Insert a new invoice row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_number": {"type": "string"},
                        "publisher_id": {"type": "string"},
                        "invoice_date": {"type": "string"},
                        "period_start": {"type": "string"},
                        "period_end": {"type": "string"},
                        "subtotal": {"type": "number"},
                        "hst_amount": {"type": "number"},
                        "total_due": {"type": "number"},
                        "pdf_path": {"type": "string"},
                    },
                    "required": [
                        "invoice_number",
                        "publisher_id",
                        "invoice_date",
                        "period_start",
                        "period_end",
                        "subtotal",
                        "hst_amount",
                        "total_due",
                        "pdf_path",
                    ],
                },
            },
        }


class FetchInvoiceRecord(Tool):
    """Retrieve an invoice using invoice_id or invoice_number."""

    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, invoice_number: str = None) -> str:
        invs = data.get("invoices", {}).values()
        row = None
        if invoice_id is not None:
            row = next(
                (i for i in invs.values() if str(i.get("invoice_id")) == str(invoice_id)), None
            )
        elif invoice_number:
            row = next(
                (i for i in invs.values() if i.get("invoice_number") == invoice_number), None
            )
        if not row:
            payload = {"error": "invoice not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchInvoiceRecord",
                "description": "Fetch invoice by id or number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class CreateInvoiceLines(Tool):
    """Add invoice items for a specific invoice."""

    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, invoice_number: str = None, lines: list[dict[str, Any]] = None) -> str:
        invoice_lines = data.get("invoice_lines", {}).values()
        invs = data.get("invoices", {}).values()
        if invoice_id is None and invoice_number:
            inv = next(
                (i for i in invs.values() if i.get("invoice_number") == invoice_number), None
            )
            if inv:
                invoice_id = inv.get("invoice_id")
        if invoice_id is None:
            payload = {"error": "invoice_id or invoice_number required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        new_ids = []
        max_line_id = 0
        for line in invoice_lines.values():
            try:
                max_line_id = max(max_line_id, int(line.get("invoice_line_id", 0)))
            except (ValueError, TypeError):
                pass

        for ln in lines or []:
            max_line_id += 1
            invoice_lines.append(
                {
                    "invoice_line_id": max_line_id,
                    "invoice_id": invoice_id,
                    "project_id": ln.get("project_id"),
                    "isbn": ln.get("isbn"),
                    "hours_billed": ln.get("hours"),
                    "hourly_rate": ln.get("rate"),
                    "line_amount": round(
                        float(ln.get("hours", 0)) * float(ln.get("rate", 0)), 2
                    ),
                }
            )
            new_ids.append(max_line_id)
        payload = {"invoice_id": invoice_id, "inserted_line_ids": new_ids}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInvoiceLines",
                "description": "Insert lines for an invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                        "lines": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["lines"],
                },
            },
        }


class ListInvoiceLinesByInvoice(Tool):
    """Retrieve invoice items for a specified invoice."""

    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, invoice_number: str = None) -> str:
        invs = data.get("invoices", {}).values()
        if invoice_id is None and invoice_number:
            inv = next(
                (i for i in invs.values() if i.get("invoice_number") == invoice_number), None
            )
            if inv:
                invoice_id = inv.get("invoice_id")
        rows = (
            [
                l
                for l in data.get("invoice_lines", {}).values()
                if str(l.get("invoice_id")) == str(invoice_id)
            ]
            if invoice_id
            else []
        )
        payload = {"invoice_id": invoice_id, "lines": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListInvoiceLinesByInvoice",
                "description": "List lines for an invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class LogInvoiceEvent(Tool):
    """Add an audit record for an invoice (generated, emailed, etc.)."""
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, invoice_number: str = None, event_type: str = None, notes: str = None) -> str:
        audits = data.get("invoice_audit", {}).values()
        # Generate new audit IDs like AUD001, AUD002 ...
        prefix, max_num = "AUD", 0
        for a in audits.values():
            s = str(a.get("audit_id", ""))
            if s.startswith(prefix):
                try:
                    max_num = max(max_num, int(s[len(prefix) :]))
                except ValueError:
                    pass
        new_id = f"{prefix}{max_num + 1:03d}"
        row = {
            "audit_id": new_id,
            "invoice_id": invoice_id,
            "invoice_number": invoice_number,
            "event_type": event_type,
            "event_timestamp": _now_iso(),
            "notes": notes,
        }
        data["invoice_audit"][row["invoice_audit_id"]] = row
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogInvoiceEvent",
                "description": "Record an audit event for an invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                        "event_type": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["event_type"],
                },
            },
        }


class ListInvoiceEvents(Tool):
    """Retrieve all audit records for a specific invoice."""

    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, invoice_number: str = None) -> str:
        events = []
        for a in data.get("invoice_audit", {}).values() or []:
            if invoice_id and str(a.get("invoice_id")) == str(invoice_id):
                events.append(a)
            elif invoice_number and a.get("invoice_number") == invoice_number:
                events.append(a)
        payload = {"events": events}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListInvoiceEvents",
                "description": "List audit events by invoice id or number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class DispatchInvoiceEmail(Tool):
    """Dispatch an invoice email and (if applicable) indicate the invoice has been sent."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        publisher_id: str = None,
        consultant_id: str = None,
        subject: str = None,
        body_text: str = None,
        attachment: str = None,
        invoice_number: str = None
    ) -> str:
        if invoice_number:
            inv = next(
                (
                    i
                    for i in data.get("invoices", {}).values()
                    if i.get("invoice_number") == invoice_number
                ),
                None,
            )
            if inv:
                inv["sent_at"] = _now_iso()
        payload = {
            "status": "sent",
            "publisher_id": publisher_id,
            "consultant_id": consultant_id,
            "subject": subject,
            "attachment": attachment,
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
                "name": "DispatchInvoiceEmail",
                "description": "Send invoice email to client, CC consultant.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string"},
                        "consultant_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                        "subject": {"type": "string"},
                        "body_text": {"type": "string"},
                        "attachment": {"type": "string"},
                    },
                    "required": [
                        "publisher_id",
                        "consultant_id",
                        "subject",
                        "body_text",
                        "attachment",
                    ],
                },
            },
        }


class QueryInvoices(Tool):
    """Sort invoices based on status/publisher/date range."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = None, publisher_id: str = None, date_from: str = None, date_to: str = None) -> str:
        rows = data.get("invoices", {}).values() or []
        out = []
        for r in rows.values():
            if status == "open" and r.get("paid_at") is not None:
                continue
            if publisher_id and r.get("publisher_id") != publisher_id:
                continue
            if date_from and r.get("invoice_date", "") < date_from:
                continue
            if date_to and r.get("invoice_date", "") > date_to:
                continue
            out.append(r)
        payload = {"invoices": out}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "QueryInvoices",
                "description": "Fetch invoices with filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string"},
                        "publisher_id": {"type": "string"},
                        "date_from": {"type": "string"},
                        "date_to": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


#───────────────────────────────
#Consultant and Client (Publisher)
#───────────────────────────────


class FetchConsultantProfile(Tool):
    """Fetch the consultant profile entry using consultant_id."""

    @staticmethod
    def invoke(data: dict[str, Any], consultant_id: str = None) -> str:
        row = next(
            (c for c in data.get("consultants", {}).values() if c.get("consultant_id") == consultant_id),
            None,
        )
        if not row:
            payload = {"error": f"consultant_id '{consultant_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchConsultantProfile",
                "description": "Fetch a consultant profile.",
                "parameters": {
                    "type": "object",
                    "properties": {"consultant_id": {"type": "string"}},
                    "required": ["consultant_id"],
                },
            },
        }


class MutateConsultantContact(Tool):
    """Modify contact information for the consultant."""

    @staticmethod
    def invoke(data: dict[str, Any], consultant_id: str, address: str = None, phone: str = None, email: str = None, gst_number: str = None) -> str:
        updates = {
            k: v
            for k, v in {"address": address, "phone": phone, "email": email, "gst_number": gst_number}.items()
            if v is not None
        }
        row = next(
            (c for c in data.get("consultants", {}).values() if c.get("consultant_id") == consultant_id),
            None,
        )
        if not row:
            payload = {"error": f"consultant_id '{consultant_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        row.update(updates)
        row["updated_at"] = _now_iso()
        payload = {"consultant_id": consultant_id, "updated": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MutateConsultantContact",
                "description": "Update contact fields for a consultant.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "consultant_id": {"type": "string"},
                        "address": {"type": "string"},
                        "phone": {"type": "string"},
                        "email": {"type": "string"},
                        "gst_number": {"type": "string"},
                    },
                    "required": ["consultant_id"],
                },
            },
        }


class FetchClientProfile(Tool):
    """Retrieve a client/publisher entry using publisher_id."""

    @staticmethod
    def invoke(data: dict[str, Any], publisher_id: str = None) -> str:
        pid = publisher_id
        row = next(
            (p for p in data.get("publishers", {}).values() if p.get("publisher_id") == pid),
            None,
        )
        if not row:
            payload = {"error": f"publisher_id '{pid}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchClientProfile",
                "description": "Fetch a client/publisher record.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_id": {"type": "string"}},
                    "required": ["publisher_id"],
                },
            },
        }


class AddClientProfile(Tool):
    """Add a new client/publisher entry."""

    @staticmethod
    def invoke(data: dict[str, Any], publisher_id: str = None, name: str = None, address: str = None, contact_email: str = None, gst_number: str = None) -> str:
        tbl = data.get("publishers", {}).values()
        row = {
            "publisher_id": publisher_id,
            "name": name,
            "address": address,
            "contact_email": contact_email,
            "gst_number": gst_number,
            "created_at": _now_iso(),
            "updated_at": _now_iso(),
        }
        data["publishers"][publisher_id] = row
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddClientProfile",
                "description": "Create a client/publisher row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string"},
                        "name": {"type": "string"},
                        "address": {"type": "string"},
                        "contact_email": {"type": "string"},
                        "gst_number": {"type": "string"},
                    },
                    "required": ["publisher_id", "name"],
                },
            },
        }


class MutateClientContact(Tool):
    """Modify contact details for the client."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        publisher_id: str = None,
        address: str = None,
        contact_email: str = None,
        gst_number: str = None
    ) -> str:
        row = next(
            (p for p in data.get("publishers", {}).values() if p.get("publisher_id") == publisher_id),
            None,
        )
        if not row:
            payload = {"error": f"publisher_id '{publisher_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        updates = {
            k: v
            for k, v in {
                "address": address,
                "contact_email": contact_email,
                "gst_number": gst_number
            }.items()
            if v is not None
        }
        row.update(updates)
        row["updated_at"] = _now_iso()
        payload = {"publisher_id": publisher_id, "updated": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MutateClientContact",
                "description": "Update a client's contact info.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string"},
                        "address": {"type": "string"},
                        "contact_email": {"type": "string"},
                        "gst_number": {"type": "string"},
                    },
                    "required": ["publisher_id"],
                },
            },
        }


#───────────
#Key Performance Indicators
#───────────


class DeriveDaysOutstanding(Tool):
    """Calculate days overdue for each invoice based on a specified date."""

    @staticmethod
    def invoke(data: dict[str, Any], today: str = "2025-08-20", invoices: list = None) -> str:
        if invoices is None:
            invoices = []
        out = []
        for r in invoices.values():
            due = r.get("period_end") or r.get("invoice_date")
            due_iso = due[:10] if isinstance(due, str) and len(due) > 10 else due
            ds = (datetime.fromisoformat(today) - datetime.fromisoformat(due_iso)).days
            out.append(
                {"invoice_number": r.get("invoice_number"), "days_outstanding": ds}
            )
        payload = {"aging": out}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeriveDaysOutstanding",
                "description": "Compute days outstanding as of a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoices": {"type": "array", "items": {"type": "object"}},
                        "today": {"type": "string"},
                    },
                    "required": ["invoices"],
                },
            },
        }


class BucketizeAging(Tool):
    """Assign days overdue to standard Accounts Receivable aging categories."""

    @staticmethod
    def invoke(data: dict[str, Any], aging: list[dict[str, Any]] = None) -> str:
        aging = aging or []
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
        payload = {"buckets": buckets}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BucketizeAging",
                "description": "Convert days-outstanding to buckets (incl. 'upcoming_due').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aging": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["aging"],
                },
            },
        }


class SummarizeReceivablesByClient(Tool):
    """Aggregate Accounts Receivable by client and category."""

    @staticmethod
    def invoke(data: dict[str, Any], invoices: list[dict[str, Any]] = None) -> str:
        invoices = invoices or []
        summary: dict[str, dict[str, float]] = {}
        for inv in invoices.values():
            pid = inv.get("publisher_id")
            bucket = inv.get("aging_bucket", "0-30")
            amt = float(inv.get("total_due", 0))
            summary.setdefault(pid, {}).values()
            summary[pid][bucket] = summary[pid].get(bucket, 0.0) + amt
        payload = {"summary_by_publisher": summary}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarizeReceivablesByClient",
                "description": "Summarize receivables by publisher and aging bucket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoices": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["invoices"],
                },
            },
        }


class DeriveCollectionKPIs(Tool):
    """Calculate collection metrics (Total Accounts Receivable, average daily sales, DSO)."""

    @staticmethod
    def invoke(data: dict[str, Any], window_months: int = 12) -> str:
        invs = data.get("invoices", {}).values() or []
        total_ar = sum(
            float(i.get("total_due", 0)) for i in invs.values() if i.get("paid_at") is None
        )
        avg_daily_sales = round(
            (
                sum(float(i.get("subtotal", 0)) for i in invs.values()
                / max(1, window_months * 30)
            ),
            2,
        )
        dso = round((total_ar / max(0.01, avg_daily_sales)), 2)
        payload = {
                "window_months": window_months,
                "total_ar": round(total_ar, 2),
                "avg_daily_sales": avg_daily_sales,
                "dso": dso,
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
                "name": "DeriveCollectionKpis",
                "description": "Compute collection KPIs over a window.",
                "parameters": {
                    "type": "object",
                    "properties": {"window_months": {"type": "integer"}},
                    "required": [],
                },
            },
        }


class RenderAccountsReceivableReport(Tool):
    """Provide a PDF path for the Accounts Receivable Aging report."""

    @staticmethod
    def invoke(data: dict[str, Any], period_label: str = None) -> str:
        pdf_path = (
            f"https://test.storage.com/reports/accounts_receivable_{period_label}.pdf"
        )
        payload = {"pdf_path": pdf_path}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RenderAccountsReceivableReport",
                "description": "Export an Accounts Receivable Aging report and return the PDF path.",
                "parameters": {
                    "type": "object",
                    "properties": {"period_label": {"type": "string"}},
                    "required": ["period_label"],
                },
            },
        }


#────────────────
#Visual Dashboards
#────────────────


class CreateDashboardSnapshot(Tool):
    """Generate a record for a dashboard snapshot."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        snapshot_date: str = None,
        ytd_revenue: float = None,
        ytd_tax_reserve: float = None,
        pdf_path: str = None
    ) -> str:
        snaps = data.get("dashboard_snapshots", {}).values()
        max_id = 0
        for s in snaps.values():
            try:
                max_id = max(max_id, int(s.get("snapshot_id", 0)))
            except (ValueError, TypeError):
                pass
        new_id = max_id + 1
        row = {
            "snapshot_id": new_id,
            "snapshot_date": snapshot_date,
            "ytd_revenue": ytd_revenue,
            "ytd_tax_reserve": ytd_tax_reserve,
            "pdf_path": pdf_path,
        }
        data["dashboard_snapshots"][row["dashboard_snapshot_id"]] = row
        payload = {"snapshot_id": new_id, "snapshot_date": row["snapshot_date"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDashboardSnapshot",
                "description": "Insert a dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_date": {"type": "string"},
                        "ytd_revenue": {"type": "number"},
                        "ytd_tax_reserve": {"type": "number"},
                        "pdf_path": {"type": "string"},
                    },
                    "required": ["snapshot_date"],
                },
            },
        }


class FetchDashboardSnapshot(Tool):
    """Retrieve a dashboard snapshot using id or date."""

    @staticmethod
    def invoke(data: dict[str, Any], snapshot_id: str = None, snapshot_date: str = None) -> str:
        snaps = data.get("dashboard_snapshots", {}).values()
        sid = snapshot_id
        sdate = snapshot_date
        row = None
        if sid is not None:
            row = next(
                (s for s in snaps.values() if str(s.get("snapshot_id")) == str(sid)), None
            )
        elif sdate:
            row = next((s for s in snaps.values() if s.get("snapshot_date") == sdate), None)
        if not row:
            payload = {"error": "snapshot not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchDashboardSnapshot",
                "description": "Read a snapshot by id or date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "snapshot_date": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class AppendProjectRevenueRows(Tool):
    """Add project revenue entries for a specific snapshot."""

    @staticmethod
    def invoke(data: dict[str, Any], snapshot_id: str = None, items: list = None) -> str:
        rows_tbl = data.get("project_revenue", {}).values()
        items = items or []
        inserted = []

        max_id = 0
        for r in rows_tbl.values():
            try:
                max_id = max(max_id, int(r.get("row_id", 0)))
            except (ValueError, TypeError):
                pass

        for it in items:
            max_id += 1
            rows_tbl.append(
                {
                    "row_id": max_id,
                    "snapshot_id": snapshot_id,
                    "project_id": it.get("project_id"),
                    "ytd_revenue": it.get("ytd_revenue"),
                }
            )
            inserted.append(max_id)
        payload = {"snapshot_id": snapshot_id, "inserted_row_ids": inserted}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "appendProjectRevenueRows",
                "description": "Insert project revenue items for a snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["snapshot_id", "items"],
                },
            },
        }


class AppendMonthlyRevenueRows(Tool):
    """Add monthly revenue entries for a snapshot."""

    @staticmethod
    def invoke(data: dict[str, Any], snapshot_id: str = None, items: list[dict[str, Any]] = None) -> str:
        rows_tbl = data.get("monthly_revenue", {}).values()
        items = items or []
        inserted = []

        max_id = 0
        for r in rows_tbl.values():
            try:
                max_id = max(max_id, int(r.get("row_id", 0)))
            except (ValueError, TypeError):
                pass

        for it in items:
            max_id += 1
            rows_tbl.append(
                {
                    "row_id": max_id,
                    "snapshot_id": snapshot_id,
                    "month_year": it.get("month_year"),
                    "revenue": it.get("revenue"),
                    "tax_reserve": it.get("tax_reserve"),
                    "profit_flag": it.get("profit_flag"),
                }
            )
            inserted.append(max_id)
        payload = {"snapshot_id": snapshot_id, "inserted_row_ids": inserted}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "appendMonthlyRevenueRows",
                "description": "Monthly revenue items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["snapshot_id", "items"],
                },
            },
        }


#─────────────
#Record System
#─────────────
TOOLS = [
    #Key Performance Indicators
    DeriveDaysOutstanding(),
    BucketizeAging(),
    DeriveCollectionKPIs(),
    SummarizeReceivablesByClient(),
    RenderAccountsReceivableReport(),
    #Core Billing Functions
    CreateInvoiceRecord(),
    ComputeInvoiceTotals(),
    FetchInvoiceRecord(),
    CreateInvoiceLines(),
    ListInvoiceLinesByInvoice(),
    LogInvoiceEvent(),
    ListInvoiceEvents(),
    DispatchInvoiceEmail(),
    QueryInvoices(),
    #Project Details & Pricing
    AddProjectCard(),
    FetchProjectCard(),
    ListProjectsCatalog(),
    MapHourlyRates(),
    #Tracking Time
    ReadTimeEntries(),
    AuditTimeEntries(),
    AggregateHoursByISBN(),
    #Consultant and Client
    FetchConsultantProfile(),
    MutateConsultantContact(),
    AddClientProfile(),
    FetchClientProfile(),
    MutateClientContact(),
    #Revenue Dashboards
    CreateDashboardSnapshot(),
    FetchDashboardSnapshot(),
    AppendProjectRevenueRows(),
    AppendMonthlyRevenueRows(),
]
