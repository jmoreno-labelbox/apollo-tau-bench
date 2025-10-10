from typing import Dict, Any, List, Optional
from domains.dto import Tool
import json
from datetime import datetime
import re

def _fixed_now_iso() -> str:
    return "2025-08-20T00:00:00Z"

def _index_by(items: List[Dict[str, Any]], key: str) -> Dict[Any, Dict[str, Any]]:
    return {i.get(key): i for i in items or []}

class GetConsultantProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("consultant_id")
        row = next((c for c in data.get("consultants", []) if c.get("consultant_id") == cid), None)
        if not row:
            return json.dumps({"error": f"Consultant '{cid}' not found"}, indent=2)
        return json.dumps(row, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_consultant_profile",
            "description":"Fetch the consultant profile row.",
            "parameters":{"type":"object","properties":{"consultant_id":{"type":"string"}},"required":["consultant_id"]}
        }}

class UpdateConsultantContact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("consultant_id")
        fields = {k:v for k,v in kwargs.items() if k in {"address","phone","email","gst_number"}}
        row = next((c for c in data.get("consultants", []) if c.get("consultant_id") == cid), None)
        if not row:
            return json.dumps({"error": f"Consultant '{cid}' not found"}, indent=2)
        row.update(fields)
        row["updated_at"] = _fixed_now_iso()
        return json.dumps({"consultant_id": cid, "updated": fields}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_consultant_contact",
            "description":"Update contact fields for a consultant.",
            "parameters":{"type":"object","properties":{
                "consultant_id":{"type":"string"},
                "address":{"type":"string"},"phone":{"type":"string"},"email":{"type":"string"},"gst_number":{"type":"string"}
            },"required":["consultant_id"]}
        }}

class GetPublisherInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pid = kwargs.get("publisher_id")
        row = next((p for p in data.get("publishers", []) if p.get("publisher_id") == pid), None)
        if not row:
            return json.dumps({"error": f"Publisher '{pid}' not found"}, indent=2)
        return json.dumps(row, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_publisher_info",
            "description":"Fetch a publisher record.",
            "parameters":{"type":"object","properties":{"publisher_id":{"type":"string"}},"required":["publisher_id"]}
        }}

class CreatePublisher(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        publishers = data.get("publishers", [])
        row = {
            "publisher_id": kwargs.get("publisher_id"),
            "name": kwargs.get("name"),
            "address": kwargs.get("address"),
            "contact_email": kwargs.get("contact_email"),
            "gst_number": kwargs.get("gst_number"),
            "created_at": _fixed_now_iso(),
            "updated_at": _fixed_now_iso()
        }
        publishers.append(row)
        return json.dumps(row, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_publisher",
            "description":"Create a publisher row.",
            "parameters":{"type":"object","properties":{
                "publisher_id":{"type":"string"},
                "name":{"type":"string"},"address":{"type":"string"},"contact_email":{"type":"string"},"gst_number":{"type":"string"}
            },"required":["publisher_id","name"]}
        }}

class UpdatePublisherContact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pid = kwargs.get("publisher_id")
        row = next((p for p in data.get("publishers", []) if p.get("publisher_id") == pid), None)
        if not row:
            return json.dumps({"error": f"Publisher '{pid}' not found"}, indent=2)
        updates = {k:v for k,v in kwargs.items() if k in {"address","contact_email","gst_number"}}
        row.update(updates)
        row["updated_at"] = _fixed_now_iso()
        return json.dumps({"publisher_id": pid, "updated": updates}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_publisher_contact",
            "description":"Update a publisher’s contact fields.",
            "parameters":{"type":"object","properties":{
                "publisher_id":{"type":"string"},
                "address":{"type":"string"},"contact_email":{"type":"string"},"gst_number":{"type":"string"}
            },"required":["publisher_id"]}
        }}

class FetchProjects(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"projects": data.get("projects", [])}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"fetch_projects",
            "description":"List all projects.",
            "parameters":{"type":"object","properties":{},"required":[]}
        }}

class GetProjectDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pid = kwargs.get("project_id")
        row = next((p for p in data.get("projects", []) if p.get("project_id") == pid), None)
        if not row:
            return json.dumps({"error": f"Project '{pid}' not found"}, indent=2)
        return json.dumps(row, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_project_details",
            "description":"Fetch a project by ID.",
            "parameters":{"type":"object","properties":{"project_id":{"type":"string"}},"required":["project_id"]}
        }}

class CreateProject(Tool):
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
            "created_at": _fixed_now_iso(),
            "updated_at": _fixed_now_iso()
        }
        projects.append(row)
        return json.dumps(row, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_project",
            "description":"Create a new project row.",
            "parameters":{"type":"object","properties":{
                "project_id":{"type":"string"},
                "publisher_id":{"type":"string"},
                "isbn":{"type":"string"},
                "project_title":{"type":"string"},
                "default_hourly_rate":{"type":"number"},
                "override_hourly_rate":{"type":["number","null"]},
                "account_code":{"type":["string","null"]},
                "is_active":{"type":"boolean"}
            },"required":["project_id","publisher_id","isbn","project_title","default_hourly_rate"]}
        }}

class FetchTimeEntries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        prj_ids = set(kwargs.get("project_id_list") or [])
        start = kwargs.get("period_start")
        end = kwargs.get("period_end")
        rows = []
        for t in data.get("time_entries", []) or []:
            if prj_ids and t.get("project_id") not in prj_ids:
                continue
            if start and t.get("entry_date","") < start:
                continue
            if end and t.get("entry_date","") > end:
                continue
            rows.append(t)
        return json.dumps({"rows": rows}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"fetch_time_entries",
            "description":"Fetch time entries by project(s) and period.",
            "parameters":{"type":"object","properties":{
                "project_id_list":{"type":"array","items":{"type":"string"}},
                "period_start":{"type":"string"},
                "period_end":{"type":"string"}
            },"required":["project_id_list","period_start","period_end"]}
        }}

class ValidateTimeEntries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = kwargs.get("rows") or []
        missing = [r for r in rows if not r.get("description") or r.get("isbn") in (None,"") or r.get("account_code") in (None,"")]
        return json.dumps({"valid": len(missing)==0, "missing_count": len(missing)}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"validate_time_entries",
            "description":"Validate that time entries have ISBN and account_code.",
            "parameters":{"type":"object","properties":{"rows":{"type":"array","items":{"type":"object"}}},"required":["rows"]}
        }}

class GroupHoursByISBN(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = kwargs.get("rows") or []
        grouped = {}
        for r in rows:
            isbn = r.get("isbn")
            if not isbn: 
                continue
            grouped.setdefault(isbn, 0.0)
            grouped[isbn] += float(r.get("hours_worked", 0.0))
        return json.dumps({"grouped_hours": grouped}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"group_hours_by_isbn",
            "description":"Sum hours per ISBN within a set of time entries.",
            "parameters":{"type":"object","properties":{"rows":{"type":"array","items":{"type":"object"}}},"required":["rows"]}
        }}

class ResolveHourlyRates(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id_list = kwargs.get("project_id_list") or []
        projects = _index_by(data.get("projects", []), "project_id")
        rate_map = {}
        for pid in project_id_list:
            pr = projects.get(pid) or {}
            rate_map[pid] = pr.get("override_hourly_rate") or pr.get("default_hourly_rate") or 0
        return json.dumps({"rate_map": rate_map}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"resolve_hourly_rates",
            "description":"Resolve hourly rate per project (override else default).",
            "parameters":{"type":"object","properties":{"project_id_list":{"type":"array","items":{"type":"string"}}},"required":["project_id_list"]}
        }}

class CalculateInvoiceTotals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        lines = kwargs.get("lines") or []
        hst = float(kwargs.get("hst_rate", 0.13))
        subtotal = sum(float(l.get("hours",0))*float(l.get("rate",0)) for l in lines)
        hst_amount = round(subtotal*hst, 2)
        total_due = round(subtotal+hst_amount, 2)
        return json.dumps({"subtotal": round(subtotal,2), "hst_amount": hst_amount, "total_due": total_due}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"calculate_invoice_totals",
            "description":"Compute subtotal, HST, and total_due for invoice lines.",
            "parameters":{"type":"object","properties":{
                "lines":{"type":"array","items":{"type":"object"}},
                "hst_rate":{"type":"number"}
            },"required":["lines"]}
        }}

class InsertInvoice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoices = data.get("invoices", [])
        
        prefix = "INV"
        max_num = 0
        for inv in invoices:
            inv_id_str = str(inv.get("invoice_id", ""))
            if inv_id_str.startswith(prefix):
                numeric_part = inv_id_str[len(prefix):]
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
            "created_at": _fixed_now_iso()
        }
        invoices.append(row)
        return json.dumps({"invoice_id": new_id, "invoice_number": row["invoice_number"]}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"insert_invoice",
            "description":"Insert a new invoice row.",
            "parameters":{"type":"object","properties":{
                "invoice_number":{"type":"string"},"publisher_id":{"type":"string"},
                "invoice_date":{"type":"string"},"period_start":{"type":"string"},"period_end":{"type":"string"},
                "subtotal":{"type":"number"},"hst_amount":{"type":"number"},"total_due":{"type":"number"},
                "pdf_path":{"type":"string"}
            },"required":["invoice_number","publisher_id","invoice_date","period_start","period_end","subtotal","hst_amount","total_due","pdf_path"]}
        }}

class GetInvoiceDetails(Tool):
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
            return json.dumps({"error":"Invoice not found"}, indent=2)
        return json.dumps(row, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_invoice_details",
            "description":"Read an invoice by id or invoice_number.",
            "parameters":{"type":"object","properties":{
                "invoice_id":{"type":"string"},"invoice_number":{"type":"string"}
            },"required":[]}
        }}

class InsertInvoiceLines(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoice_lines = data.get("invoice_lines", [])
        invs = data.get("invoices", [])
        invoice_id = kwargs.get("invoice_id")
        invoice_number = kwargs.get("invoice_number")
        if invoice_id is None and invoice_number:
            inv = next((i for i in invs if i.get("invoice_number")==invoice_number), None)
            if inv:
                invoice_id = inv.get("invoice_id")
        if invoice_id is None:
            return json.dumps({"error":"invoice_id or invoice_number required"}, indent=2)
        lines = kwargs.get("lines") or []
        new_ids = []
        
        max_line_id = 0
        for line in invoice_lines:
            try:
                line_id_val = int(line.get("invoice_line_id", 0))
                if line_id_val > max_line_id:
                    max_line_id = line_id_val
            except (ValueError, TypeError):
                continue
        
        for ln in lines:
            max_line_id += 1
            lid = max_line_id
            invoice_lines.append({
                "invoice_line_id": lid,
                "invoice_id": invoice_id,
                "project_id": ln.get("project_id"),
                "isbn": ln.get("isbn"),
                "hours_billed": ln.get("hours"),
                "hourly_rate": ln.get("rate"),
                "line_amount": round(float(ln.get("hours",0))*float(ln.get("rate",0)), 2)
            })
            new_ids.append(lid)
        return json.dumps({"invoice_id": invoice_id, "inserted_line_ids": new_ids}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"insert_invoice_lines",
            "description":"Insert invoice lines for an invoice.",
            "parameters":{"type":"object","properties":{
                "invoice_id":{"type":"string"},
                "invoice_number":{"type":"string"},
                "lines":{"type":"array","items":{"type":"object"}}
            },"required":["lines"]}
        }}

class ListInvoiceLines(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoice_id = kwargs.get("invoice_id")
        invoice_number = kwargs.get("invoice_number")
        invs = data.get("invoices", [])
        if invoice_id is None and invoice_number:
            inv = next((i for i in invs if i.get("invoice_number")==invoice_number), None)
            if inv: invoice_id = inv.get("invoice_id")
        rows = [l for l in data.get("invoice_lines", []) if str(l.get("invoice_id")) == str(invoice_id)] if invoice_id else []
        return json.dumps({"invoice_id": invoice_id, "lines": rows}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_invoice_lines",
            "description":"List lines for an invoice by id or number.",
            "parameters":{"type":"object","properties":{"invoice_id":{"type":"string"},"invoice_number":{"type":"string"}},"required":[]}
        }}

class RecordInvoiceAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        audits = data.get("invoice_audit", [])
        prefix = "AUD"
        max_num = 0
        for audit in audits:
            audit_id_str = str(audit.get("audit_id", ""))
            if audit_id_str.startswith(prefix):
                numeric_part = audit_id_str[len(prefix):]
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
            "invoice_id": kwargs.get("invoice_id"),
            "invoice_number": kwargs.get("invoice_number"),
            "event_type": kwargs.get("event_type"),
            "event_timestamp": _fixed_now_iso(),
            "notes": kwargs.get("notes")
        }
        audits.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"record_invoice_audit",
            "description":"Append an InvoiceAudit event (generated, emailed, etc.).",
            "parameters":{"type":"object","properties":{
                "invoice_id":{"type":"string"},"invoice_number":{"type":"string"},
                "event_type":{"type":"string"},"notes":{"type":"string"}
            },"required":["event_type"]}
        }}

class ListInvoiceAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inv_id = kwargs.get("invoice_id")
        inv_num = kwargs.get("invoice_number")
        rows = []
        for a in data.get("invoice_audit", []) or []:
            if inv_id and str(a.get("invoice_id")) == str(inv_id):
                rows.append(a)
            elif inv_num and a.get("invoice_number")==inv_num:
                rows.append(a)
        return json.dumps({"events": rows}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_invoice_audit",
            "description":"List audit events for an invoice by id or number.",
            "parameters":{"type":"object","properties":{"invoice_id":{"type":"string"},"invoice_number":{"type":"string"}},"required":[]}
        }}

class SendInvoiceEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        publisher_id = kwargs.get("publisher_id")
        consultant_id = kwargs.get("consultant_id")
        subject = kwargs.get("subject")
        body_text = kwargs.get("body_text")
        attachment = kwargs.get("attachment")
        inv_no = kwargs.get("invoice_number")
        if inv_no:
            inv = next((i for i in data.get("invoices", []) if i.get("invoice_number")==inv_no), None)
            if inv:
                inv["sent_at"] = _fixed_now_iso()
        return json.dumps({"status":"sent", "publisher_id": publisher_id, "consultant_id": consultant_id, "subject": subject, "attachment": attachment}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"send_invoice_email",
            "description":"Send invoice email to publisher, CC consultant (external).",
            "parameters":{"type":"object","properties":{
                "publisher_id":{"type":"string"},"consultant_id":{"type":"string"},
                "invoice_number":{"type":"string"},
                "subject":{"type":"string"},"body_text":{"type":"string"},"attachment":{"type":"string"}
            },"required":["publisher_id","consultant_id","subject","body_text","attachment"]}
        }}

class FetchInvoices(Tool):
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
            if start and r.get("invoice_date","") < start:
                continue
            if end and r.get("invoice_date","") > end:
                continue
            out.append(r)
        return json.dumps({"invoices": out}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"fetch_invoices",
            "description":"Fetch invoices with optional filters (status/open, publisher, date range).",
            "parameters":{"type":"object","properties":{
                "status":{"type":"string"},
                "publisher_id":{"type":"string"},
                "date_from":{"type":"string"},"date_to":{"type":"string"}
            },"required":[]}
        }}

class ComputeDaysOutstanding(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        today = kwargs.get("today") or "2025-08-20"
        invs = kwargs.get("invoices") or []
        out = []
        for r in invs:
            due = r.get("period_end") or r.get("invoice_date")
            ds = (datetime.fromisoformat(today) - datetime.fromisoformat((due[:10] if len(due)>10 else due))).days
            out.append({"invoice_number": r.get("invoice_number"), "days_outstanding": ds})
        return json.dumps({"aging": out}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"compute_days_outstanding",
            "description":"Compute days outstanding per invoice for a given as-of date.",
            "parameters":{"type":"object","properties":{
                "invoices":{"type":"array","items":{"type":"object"}},
                "today":{"type":"string"}
            },"required":["invoices"]}
        }}

class CategorizeAging(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aging = kwargs.get("aging") or []
        buckets = []
        for a in aging:
            days = int(a.get("days_outstanding",0))
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
        return {"type":"function","function":{
            "name":"categorize_aging",
            "description":"Map days outstanding to aging buckets including 'upcoming_due'.",
            "parameters":{"type":"object","properties":{"aging":{"type":"array","items":{"type":"object"}}},"required":["aging"]}
        }}

class SummarizeARByClient(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoices = kwargs.get("invoices") or []
        summary: Dict[str, Dict[str, float]] = {}
        for inv in invoices:
            pid = inv.get("publisher_id")
            bucket = inv.get("aging_bucket","0-30")
            amt = float(inv.get("total_due", 0))
            summary.setdefault(pid, {})
            summary[pid][bucket] = summary[pid].get(bucket, 0.0) + amt
        return json.dumps({"summary_by_publisher": summary}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"summarize_ar_by_client",
            "description":"Summarize A/R by publisher and aging bucket.",
            "parameters":{"type":"object","properties":{"invoices":{"type":"array","items":{"type":"object"}}},"required":["invoices"]}
        }}

class ComputeCollectionKPIs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        window_months = int(kwargs.get("window_months",12))
        invs = data.get("invoices", []) or []
        total_ar = sum(float(i.get("total_due",0)) for i in invs if i.get("paid_at") is None)
        avg_daily_sales = round((sum(float(i.get("subtotal",0)) for i in invs)/max(1, window_months*30)),2)
        dso = round((total_ar/max(0.01, avg_daily_sales)),2)
        return json.dumps({"window_months": window_months, "total_ar": round(total_ar,2), "avg_daily_sales": avg_daily_sales, "dso": dso}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"compute_collection_kpis",
            "description":"Compute A/R collection KPIs (total A/R, avg daily sales, DSO) over a window.",
            "parameters":{"type":"object","properties":{"window_months":{"type":"integer"}},"required":[]}
        }}

class ExportARAgingReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        period_label = kwargs.get("period_label")
        pdf_path = f"https://storage.example.com/reports/AR_Aging_{period_label}.pdf"
        return json.dumps({"report_pdf_path": pdf_path}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"export_ar_aging_report",
            "description":"Export an A/R Aging report and return pdf path.",
            "parameters":{"type":"object","properties":{"period_label":{"type":"string"}},"required":["period_label"]}
        }}

class InsertDashboardSnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        snaps = data.get("dashboard_snapshots", [])
        
        max_id = 0
        for s in snaps:
            try:
                snap_id = int(s.get("snapshot_id", 0))
                if snap_id > max_id:
                    max_id = snap_id
            except (ValueError, TypeError):
                continue
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
        return {"type":"function","function":{
            "name":"insert_dashboard_snapshot",
            "description":"Create a dashboard snapshot row.",
            "parameters":{"type":"object","properties":{
                "snapshot_date":{"type":"string"},
                "ytd_revenue":{"type":"number"},
                "ytd_tax_reserve":{"type":"number"},
                "pdf_path":{"type":"string"}
            },"required":["snapshot_date"]}
        }}

class GetDashboardSnapshotDetails(Tool):
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
            return json.dumps({"error":"Snapshot not found"}, indent=2)
        return json.dumps(row, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_dashboard_snapshot_details",
            "description":"Fetch a snapshot by id or by snapshot_date.",
            "parameters":{"type":"object","properties":{"snapshot_id":{"type":"string"},"snapshot_date":{"type":"string"}},"required":[]}
        }}

class InsertProjectRevenueRows(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows_tbl = data.get("project_revenue", [])
        snapshot_id = kwargs.get("snapshot_id")
        items = kwargs.get("items") or []
        inserted = []
        
        max_id = 0
        for r in rows_tbl:
            try:
                row_id = int(r.get("row_id", 0))
                if row_id > max_id:
                    max_id = row_id
            except (ValueError, TypeError):
                continue

        for it in items:
            max_id += 1
            rid = max_id
            rows_tbl.append({"row_id": rid, "snapshot_id": snapshot_id, "project_id": it.get("project_id"), "ytd_revenue": it.get("ytd_revenue")})
            inserted.append(rid)
        return json.dumps({"snapshot_id": snapshot_id, "inserted_row_ids": inserted}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"insert_project_revenue_rows",
            "description":"Insert project revenue rows for a snapshot.",
            "parameters":{"type":"object","properties":{
                "snapshot_id":{"type":"string"},
                "items":{"type":"array","items":{"type":"object"}}
            },"required":["snapshot_id","items"]}
        }}

class InsertMonthlyRevenueRows(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows_tbl = data.get("monthly_revenue", [])
        snapshot_id = kwargs.get("snapshot_id")
        items = kwargs.get("items") or []
        inserted = []
        
        max_id = 0
        for r in rows_tbl:
            try:
                row_id = int(r.get("row_id", 0))
                if row_id > max_id:
                    max_id = row_id
            except (ValueError, TypeError):
                continue
        
        for it in items:
            max_id += 1
            rid = max_id
            rows_tbl.append({"row_id": rid, "snapshot_id": snapshot_id, "month_year": it.get("month_year"),
                                "revenue": it.get("revenue"), "tax_reserve": it.get("tax_reserve"),
                                "profit_flag": it.get("profit_flag")})
            inserted.append(rid)
        return json.dumps({"snapshot_id": snapshot_id, "inserted_row_ids": inserted}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"insert_monthly_revenue_rows",
            "description":"Insert monthly revenue rows for a snapshot.",
            "parameters":{"type":"object","properties":{
                "snapshot_id":{"type":"string"},
                "items":{"type":"array","items":{"type":"object"}}
            },"required":["snapshot_id","items"]}
        }}

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
    InsertMonthlyRevenueRows()
]