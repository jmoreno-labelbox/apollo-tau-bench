import json
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def _index_by(items: list[dict[str, Any]], key: str) -> dict[Any, dict[str, Any]]:
    pass
    
    if isinstance(items, dict): items = list(items)
return {i.get(key): i for i in items or []}


def _fixed_now_iso() -> str:
    pass
    return "2025-08-20T00:00:00Z"


class GetConsultantProfile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], consultant_id: str = None) -> str:
        row = next(
            (c for c in data.get("consultants", {}).values() if c.get("consultant_id") == consultant_id),
            None,
        )
        if not row:
            payload = {"error": f"Consultant '{consultant_id}' not found"}
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
                "name": "GetConsultantProfile",
                "description": "Fetch the consultant profile row.",
                "parameters": {
                    "type": "object",
                    "properties": {"consultant_id": {"type": "string"}},
                    "required": ["consultant_id"],
                },
            },
        }


class UpdateConsultantContact(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], consultant_id: str, address: str = None, phone: str = None, email: str = None, gst_number: str = None) -> str:
        cid = consultant_id
        fields = {
            "address": address,
            "phone": phone,
            "email": email,
            "gst_number": gst_number
        }
        fields = {k: v for k, v in fields.items() if v is not None}
        row = next(
            (c for c in data.get("consultants", {}).values() if c.get("consultant_id") == cid),
            None,
        )
        if not row:
            payload = {"error": f"Consultant '{cid}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        row.update(fields)
        row["updated_at"] = _fixed_now_iso()
        payload = {"consultant_id": cid, "updated": fields}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateConsultantContact",
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


class GetPublisherInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], publisher_id: str = None) -> str:
        pid = publisher_id
        row = next(
            (p for p in data.get("publishers", {}).values() if p.get("publisher_id") == pid),
            None,
        )
        if not row:
            payload = {"error": f"Publisher '{pid}' not found"}
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
                "name": "GetPublisherInfo",
                "description": "Fetch a publisher record.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_id": {"type": "string"}},
                    "required": ["publisher_id"],
                },
            },
        }


class CreatePublisher(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], publisher_id: str = None, name: str = None, address: str = None, contact_email: str = None, gst_number: str = None) -> str:
        publishers = data.get("publishers", {}).values()
        row = {
            "publisher_id": publisher_id,
            "name": name,
            "address": address,
            "contact_email": contact_email,
            "gst_number": gst_number,
            "created_at": _fixed_now_iso(),
            "updated_at": _fixed_now_iso(),
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
                "name": "CreatePublisher",
                "description": "Create a publisher row.",
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


class UpdatePublisherContact(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        publisher_id: str,
        address: str = None,
        contact_email: str = None,
        gst_number: str = None
    ) -> str:
        row = next(
            (p for p in data.get("publishers", {}).values() if p.get("publisher_id") == publisher_id),
            None,
        )
        if not row:
            payload = {"error": f"Publisher '{publisher_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        updates = {
            "address": address,
            "contact_email": contact_email,
            "gst_number": gst_number
        }
        updates = {k: v for k, v in updates.items() if v is not None}
        row.update(updates)
        row["updated_at"] = _fixed_now_iso()
        payload = {"publisher_id": publisher_id, "updated": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdatePublisherContact",
                "description": "Update a publisher’s contact fields.",
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


class FetchProjects(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], unexpected: Any = None) -> str:
        payload = {"projects": data.get("projects", {}).values()}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchProjects",
                "description": "List all projects.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class GetProjectDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        pid = project_id
        row = next(
            (p for p in data.get("projects", {}).values() if p.get("project_id") == pid), None
        )
        if not row:
            payload = {"error": f"Project '{pid}' not found"}
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
                "name": "GetProjectDetails",
                "description": "Fetch a project by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }


class CreateProject(Tool):
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
            "created_at": _fixed_now_iso(),
            "updated_at": _fixed_now_iso(),
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
                "name": "CreateProject",
                "description": "Create a new project row.",
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


class FetchTimeEntries(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id_list: list = None, period_start: str = None, period_end: str = None) -> str:
        prj_ids = set(project_id_list or [])
        start = period_start
        end = period_end
        rows = []
        for t in data.get("time_entries", {}).values() or []:
            if prj_ids and t.get("project_id") not in prj_ids:
                continue
            if start and t.get("entry_date", "") < start:
                continue
            if end and t.get("entry_date", "") > end:
                continue
            data["invoices"][invoice_id] = t
        payload = {"rows": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchTimeEntries",
                "description": "Fetch time entries by project(s) and period.",
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


class ValidateTimeEntries(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], rows: list[dict[str, Any]] = None) -> str:
        rows = rows or []
        missing = [
            r
            for r in rows.values() if not r.get("description")
            or r.get("isbn") in (None, "")
            or r.get("account_code") in (None, "")
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
                "name": "ValidateTimeEntries",
                "description": "Validate that time entries have ISBN and account_code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rows": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["rows"],
                },
            },
        }


class GroupHoursByISBN(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], rows: list[dict[str, Any]] = None) -> str:
        rows = rows or []
        grouped = {}
        for r in rows.values():
            isbn = r.get("isbn")
            if not isbn:
                continue
            grouped.setdefault(isbn, 0.0)
            grouped[isbn] += float(r.get("hours_worked", 0.0))
        payload = {"grouped_hours": grouped}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GroupHoursByIsbn",
                "description": "Sum hours per ISBN within a set of time entries.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rows": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["rows"],
                },
            },
        }


class ResolveHourlyRates(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id_list: list[str] = None) -> str:
        project_id_list = project_id_list or []
        projects = _index_by(list(data.get("projects", {}).values()), "project_id")
        rate_map = {}
        for pid in project_id_list:
            pr = projects.get(pid) or {}
            rate_map[pid] = (
                pr.get("override_hourly_rate") or pr.get("default_hourly_rate") or 0
            )
        payload = {"rate_map": rate_map}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ResolveHourlyRates",
                "description": "Resolve hourly rate per project (override else default).",
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


class CalculateInvoiceTotals(Tool):
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
                "name": "CalculateInvoiceTotals",
                "description": "Compute subtotal, HST, and total_due for invoice lines.",
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


class InsertInvoice(Tool):
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
        pdf_path: str = None
    ) -> str:
        invoices = data.get("invoices", {}).values()

        prefix = "INV"
        max_num = 0
        for inv in invoices.values():
            inv_id_str = str(inv.get("invoice_id", ""))
            if inv_id_str.startswith(prefix):
                numeric_part = inv_id_str[len(prefix) :]
                try:
                    num = int(numeric_part)
                    if num > max_num:
                        max_num = num
                except ValueError:
                    continue
        new_number = max_num + 1
        new_id = f"{prefix}{new_number:03d}"

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
            "created_at": _fixed_now_iso(),
        }
        data["invoices"][invoice_id] = row
        payload = {"invoice_id": new_id, "invoice_number": row["invoice_number"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertInvoice",
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


class GetInvoiceDetails(Tool):
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
            payload = {"error": "Invoice not found"}
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
                "name": "GetInvoiceDetails",
                "description": "Read an invoice by id or invoice_number.",
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


class InsertInvoiceLines(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: int = None, invoice_number: str = None, lines: list = None) -> str:
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
        lines = lines or []
        new_ids = []

        max_line_id = 0
        for line in invoice_lines.values():
            try:
                line_id_val = int(line.get("invoice_line_id", 0))
                if line_id_val > max_line_id:
                    max_line_id = line_id_val
            except (ValueError, TypeError):
                continue

        for ln in lines:
            max_line_id += 1
            lid = max_line_id
            invoice_lines.append(
                {
                    "invoice_line_id": lid,
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
            new_ids.append(lid)
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
                "name": "InsertInvoiceLines",
                "description": "Insert invoice lines for an invoice.",
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


class ListInvoiceLines(Tool):
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
                "name": "ListInvoiceLines",
                "description": "List lines for an invoice by id or number.",
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


class RecordInvoiceAudit(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        invoice_id: str = None,
        invoice_number: str = None,
        event_type: str = None,
        notes: str = None
    ) -> str:
        audits = data.get("invoice_audit", {}).values()
        prefix = "AUD"
        max_num = 0
        for audit in audits.values():
            audit_id_str = str(audit.get("audit_id", ""))
            if audit_id_str.startswith(prefix):
                numeric_part = audit_id_str[len(prefix) :]
                try:
                    num = int(numeric_part)
                    if num > max_num:
                        max_num = num
                except ValueError:
                    continue

        new_number = max_num + 1
        new_id = f"{prefix}{new_number:03d}"

        row = {
            "audit_id": new_id,
            "invoice_id": invoice_id,
            "invoice_number": invoice_number,
            "event_type": event_type,
            "event_timestamp": _fixed_now_iso(),
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
                "name": "RecordInvoiceAudit",
                "description": "Append an InvoiceAudit event (generated, emailed, etc.).",
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


class ListInvoiceAudit(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, invoice_number: str = None) -> str:
        rows = []
        for a in data.get("invoice_audit", {}).values() or []:
            if invoice_id and str(a.get("invoice_id")) == str(invoice_id):
                data["invoices"][invoice_id] = a
            elif invoice_number and a.get("invoice_number") == invoice_number:
                data["invoices"][invoice_id] = a
        payload = {"events": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListInvoiceAudit",
                "description": "List audit events for an invoice by id or number.",
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


class SendInvoiceEmail(Tool):
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
        inv_no = invoice_number
        if inv_no:
            inv = next(
                (
                    i
                    for i in data.get("invoices", {}).values()
                    if i.get("invoice_number") == inv_no
                ),
                None,
            )
            if inv:
                inv["sent_at"] = _fixed_now_iso()
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
                "name": "SendInvoiceEmail",
                "description": "Send invoice email to publisher, CC consultant (external).",
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


class FetchInvoices(Tool):
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
                "name": "FetchInvoices",
                "description": "Fetch invoices with optional filters (status/open, publisher, date range).",
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


class ComputeDaysOutstanding(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], today: str = "2025-08-20", invoices: list = None) -> str:
        if invoices is None:
            invoices = []
        out = []
        for r in invoices.values():
            due = r.get("period_end") or r.get("invoice_date")
            ds = (
                datetime.fromisoformat(today)
                - datetime.fromisoformat(due[:10] if len(due) > 10 else due)
            ).days
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
                "name": "ComputeDaysOutstanding",
                "description": "Compute days outstanding per invoice for a given as-of date.",
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


class CategorizeAging(Tool):
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
                "name": "CategorizeAging",
                "description": "Map days outstanding to aging buckets including 'upcoming_due'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aging": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["aging"],
                },
            },
        }


class SummarizeARByClient(Tool):
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
                "name": "summarizeArByClient",
                "description": "Summarize A/R by publisher and aging bucket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoices": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["invoices"],
                },
            },
        }


class ComputeCollectionKPIs(Tool):
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
                "name": "ComputeCollectionKpis",
                "description": "Compute A/R collection KPIs (total A/R, avg daily sales, DSO) over a window.",
                "parameters": {
                    "type": "object",
                    "properties": {"window_months": {"type": "integer"}},
                    "required": [],
                },
            },
        }


class ExportARAgingReport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], period_label: str = None) -> str:
        pdf_path = f"https://storage.example.com/reports/AR_Aging_{period_label}.pdf"
        payload = {"report_pdf_path": pdf_path}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportArAgingReport",
                "description": "Export an A/R Aging report and return pdf path.",
                "parameters": {
                    "type": "object",
                    "properties": {"period_label": {"type": "string"}},
                    "required": ["period_label"],
                },
            },
        }


class InsertDashboardSnapshot(Tool):
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
                snap_id = int(s.get("snapshot_id", 0))
                if snap_id > max_id:
                    max_id = snap_id
            except (ValueError, TypeError):
                continue
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
                "name": "InsertDashboardSnapshot",
                "description": "Create a dashboard snapshot row.",
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


class GetDashboardSnapshotDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], snapshot_id: str = None, snapshot_date: str = None) -> str:
        snaps = data.get("dashboard_snapshots", {}).values()
        row = None
        if snapshot_id is not None:
            row = next(
                (s for s in snaps.values() if str(s.get("snapshot_id")) == str(snapshot_id)), None
            )
        elif snapshot_date:
            row = next((s for s in snaps.values() if s.get("snapshot_date") == snapshot_date), None)
        if not row:
            payload = {"error": "Snapshot not found"}
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
                "name": "GetDashboardSnapshotDetails",
                "description": "Fetch a snapshot by id or by snapshot_date.",
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


class InsertProjectRevenueRows(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], snapshot_id: int = None, items: list = None) -> str:
        rows_tbl = data.get("project_revenue", {}).values()
        items = items or []
        inserted = []

        max_id = 0
        for r in rows_tbl.values():
            try:
                row_id = int(r.get("row_id", 0))
                if row_id > max_id:
                    max_id = row_id
            except (ValueError, TypeError):
                continue

        for it in items:
            max_id += 1
            rid = max_id
            rows_tbl.append(
                {
                    "row_id": rid,
                    "snapshot_id": snapshot_id,
                    "project_id": it.get("project_id"),
                    "ytd_revenue": it.get("ytd_revenue"),
                }
            )
            inserted.append(rid)
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
                "name": "insertProjectRevenueRows",
                "description": "Insert project revenue rows for a snapshot.",
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


class InsertMonthlyRevenueRows(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], snapshot_id: str = None, items: list[dict[str, Any]] = None) -> str:
        rows_tbl = data.get("monthly_revenue", {}).values()
        items = items or []
        inserted = []

        max_id = 0
        for r in rows_tbl.values():
            try:
                row_id = int(r.get("row_id", 0))
                if row_id > max_id:
                    max_id = row_id
            except (ValueError, TypeError):
                continue

        for it in items:
            max_id += 1
            rid = max_id
            rows_tbl.append(
                {
                    "row_id": rid,
                    "snapshot_id": snapshot_id,
                    "month_year": it.get("month_year"),
                    "revenue": it.get("revenue"),
                    "tax_reserve": it.get("tax_reserve"),
                    "profit_flag": it.get("profit_flag"),
                }
            )
            inserted.append(rid)
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
                "name": "insertMonthlyRevenueRows",
                "description": "Insert monthly revenue rows for a snapshot.",
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


TOOLS = [
    GetConsultantProfile(),
    UpdateConsultantContact(),
    GetPublisherInfo(),
    CreatePublisher(),
    UpdatePublisherContact(),
    FetchProjects(),
    GetProjectDetails(),
    CreateProject(),
    FetchTimeEntries(),
    ValidateTimeEntries(),
    GroupHoursByISBN(),
    ResolveHourlyRates(),
    CalculateInvoiceTotals(),
    InsertInvoice(),
    GetInvoiceDetails(),
    InsertInvoiceLines(),
    ListInvoiceLines(),
    RecordInvoiceAudit(),
    ListInvoiceAudit(),
    SendInvoiceEmail(),
    FetchInvoices(),
    ComputeDaysOutstanding(),
    CategorizeAging(),
    SummarizeARByClient(),
    ComputeCollectionKPIs(),
    ExportARAgingReport(),
    InsertDashboardSnapshot(),
    GetDashboardSnapshotDetails(),
    InsertProjectRevenueRows(),
    InsertMonthlyRevenueRows(),
]
