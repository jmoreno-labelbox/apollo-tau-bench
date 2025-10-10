import json
import math
from datetime import datetime
from typing import Dict, Any, List

from domains.dto import Tool


# ---------------- READ TOOLS ----------------

class GetPublisherByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns publisher_id for a given publisher name.
        """
        name = kwargs["publisher_name"]
        pub = next((p for p in data["publishers"] if p["name"] == name), None)
        return json.dumps(pub["publisher_id"] if pub else None)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPublisherByName",
                "description": "Retrieve publisher_id for a given publisher name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_name": {"type": "string", "description": "Exact publisher name to look up"}
                    },
                    "required": ["publisher_name"],
                },
            },
        }


class GetPublisherInvoices(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns all invoice_ids for a given publisher_id.
        """
        publisher_id = kwargs["publisher_id"]
        invoices = [inv for inv in data["invoices"] if inv["publisher_id"] == publisher_id]
        return json.dumps([inv["invoice_id"] for inv in invoices])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPublisherInvoices",
                "description": "Retrieve all invoice_ids for a given publisher_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string", "description": "Publisher ID to filter invoices by"}
                    },
                    "required": ["publisher_id"],
                },
            },
        }

class CreateInvoiceLine(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Insert a new invoice line linked to an existing invoice_id.
        Deterministic: uses provided invoice_id, project_id, isbn, hours, rate, hst_rate.
        Returns created line_id.
        """
        invoice_id = kwargs["invoice_id"]
        project_id = kwargs["project_id"]
        hours = kwargs.get("hours", 1)
        rate = kwargs.get("rate", 1)
        hst_rate = kwargs.get("hst_rate", 0.13)

        line_id = f"LINE-{len(data['invoice_lines'])+1:04d}"
        line_total = round(hours * rate, 2)
        hst_amount = round(line_total * hst_rate, 2)

        new_line = {
            "line_id": line_id,
            "invoice_id": invoice_id,
            "project_id": project_id,
            "hours": hours,
            "rate": rate,
            "line_total": line_total,
            "hst_amount": hst_amount
        }
        data["invoice_lines"].append(new_line)
        return json.dumps(new_line)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInvoiceLine",
                "description": "Create a line item for an invoice using project time entry details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string", "description": "Publisher ID to filter invoices by"}
                    },
                    "required": ["invoice_id",'project_id'],
                },
            },
        }

class GetInvoiceLines(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns invoice_line_ids for a given invoice_id.
        """
        invoice_id = kwargs["invoice_id"]
        lines = [ln for ln in data["invoice_lines"] if ln["invoice_id"] == invoice_id]
        return json.dumps([ln["line_id"] for ln in lines])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInvoiceLines",
                "description": "Retrieve all invoice_line_ids for a given invoice_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string", "description": "Invoice ID to fetch line items for"}
                    },
                    "required": ["invoice_id"],
                },
            },
        }


class GetProjectTimeEntries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs["project_id"]
        entries = [te['hours_worked'] for te in data["time_entries"] if te["project_id"] == project_id]
        return json.dumps({'project_id': project_id, 'hours': sum(entries)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectTimeEntries",
                "description": "Retrieve all time_entry_ids for a given project_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID to fetch time entries for"}
                    },
                    "required": ["project_id"],
                },
            },
        }


# ---------------- WRITE TOOLS ----------------

class CreateInvoice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Creates a new invoice with core required fields and many optional ones.
        Non-critical fields default to None or empty string if not provided.
        """
        new_invoice = {
            "invoice_id": f'INV{kwargs["invoice_number"]}',
            "invoice_number": kwargs["invoice_number"],
            "publisher_id": kwargs["publisher_id"],
            "invoice_date": kwargs.get("invoice_date", None),
            "period_start": kwargs.get("period_start", None),
            "period_end": kwargs.get("period_end", None),
            "subtotal": kwargs["subtotal"],
            "hst_amount": kwargs["hst_amount"],
            "total_due": kwargs["total_due"],
            "pdf_path": kwargs.get("pdf_path", ""),
            "sent_at": kwargs.get("sent_at", None),
            "paid_at": kwargs.get("paid_at", None),
            "created_at": kwargs.get("created_at", None),
            "currency": kwargs.get("currency", "CAD"),
            "notes": kwargs.get("notes", "")
        }
        data["invoices"].append(new_invoice)
        return json.dumps(new_invoice["invoice_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInvoice",
                "description": "Create a new invoice and append it to invoices.json. Allows optional metadata like notes, pdf_path, dates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_number": {"type": "string"},
                        "publisher_id": {"type": "string"},
                        "subtotal": {"type": "number"},
                        "hst_amount": {"type": "number"},
                        "total_due": {"type": "number"},
                        "invoice_date": {"type": "string"},
                        "period_start": {"type": "string"},
                        "period_end": {"type": "string"},
                        "pdf_path": {"type": "string"},
                        "sent_at": {"type": "string"},
                        "paid_at": {"type": "string"},
                        "created_at": {"type": "string"},
                        "currency": {"type": "string"},
                        "notes": {"type": "string"}
                    },
                    "required": [
                        "invoice_number",
                        "publisher_id",
                        "subtotal",
                        "hst_amount",
                        "total_due"
                    ],
                },
            },
        }


class UpdateInvoicePayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Marks an invoice as paid by updating paid_at field.
        """
        invoice_id = kwargs["invoice_id"]
        paid_at = kwargs["paid_at"]
        updated = None
        for inv in data["invoices"]:
            if inv["invoice_id"] == invoice_id:
                inv["paid_at"] = paid_at
                updated = inv
                break
        return json.dumps(updated if updated else {})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInvoicePayment",
                "description": "Update the paid_at timestamp for a given invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "paid_at": {"type": "string", "description": "Datetime string for payment confirmation"}
                    },
                    "required": ["invoice_id", "paid_at"],
                },
            },
        }


class LogInvoiceAuditEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Logs an audit event for an invoice.
        """
        new_event = {
            "audit_id": f"AUD_{kwargs['invoice_id']}",
            "invoice_id": kwargs["invoice_id"],
            "event_type": kwargs.get("event_type")  , # e.g., "reminder_sent", "escalation"
            "notes": kwargs.get("notes", "")
        }
        data["invoice_audit"].append(new_event)
        return json.dumps(new_event["audit_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogInvoiceAuditEvent",
                "description": "Log an audit event (reminder, escalation, etc.) for a given invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "invoice_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "event_date": {"type": "string"},
                        "notes": {"type": "string"}
                    },
                    "required": ["audit_id", "invoice_id", "event_type"],
                },
            },
        }


# ---------------- READ TOOLS ----------------

class GetDashboardSnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns the snapshot_id if found.
        """
        snapshot_id = kwargs["snapshot_id"]
        snapshot = next((s for s in data["dashboard_snapshots"] if s["snapshot_id"] == snapshot_id), None)
        return json.dumps(snapshot["snapshot_id"] if snapshot else None)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDashboardSnapshot",
                "description": "Retrieve a financial dashboard snapshot by snapshot_id (returns only the snapshot_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string", "description": "Unique ID of the snapshot"}
                    },
                    "required": ["snapshot_id"],
                },
            },
        }


class GetMonthlyRevenueBySnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns row_ids of monthly revenue for a given snapshot_id.
        """
        snapshot_id = kwargs["snapshot_id"]
        records = [mr["row_id"] for mr in data["monthly_revenue"] if mr["snapshot_id"] == snapshot_id]
        return json.dumps(records)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMonthlyRevenueBySnapshot",
                "description": "Retrieve all monthly revenue row_ids tied to a dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string", "description": "Snapshot ID to filter monthly revenue"}
                    },
                    "required": ["snapshot_id"],
                },
            },
        }


class GetProjectRevenueSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns row_ids of project revenue for a given snapshot_id.
        """
        snapshot_id = kwargs["snapshot_id"]
        records = [pr["row_id"] for pr in data["project_revenue"] if pr["snapshot_id"] == snapshot_id]
        return json.dumps(records)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectRevenueSummary",
                "description": "Retrieve project revenue row_ids tied to a snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string", "description": "Snapshot ID to filter project revenue"}
                    },
                    "required": ["snapshot_id"],
                },
            },
        }

class CreateDashboardSnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Create a new dashboard snapshot.
        """
        new_snapshot = {
            "snapshot_id": kwargs["snapshot_id"],
            "snapshot_date": kwargs["snapshot_date"],
            "notes": kwargs.get("notes", "Year-end snapshot")
        }
        data["dashboard_snapshots"].append(new_snapshot)
        return json.dumps(new_snapshot["snapshot_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDashboardSnapshot",
                "description": "Create a new financial dashboard snapshot for a given year.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "snapshot_date": {"type": "string"},
                        "year": {"type": "integer"},
                        "notes": {"type": "string"}
                    },
                    "required": ["snapshot_id", "snapshot_date", "year"],
                },
            },
        }


class CreateDashboardSnapshotWithInvoiceId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Create a new dashboard snapshot.
        """
        invoice_id = kwargs["invoice_id"]
        snapshot_id = f"SNAP_{invoice_id}",
        new_snapshot = {
            "snapshot_id": str(snapshot_id[0]),
            "snapshot_date": kwargs["snapshot_date"],
            "notes": kwargs.get("notes", "Year-end snapshot"),
            "ytd_revenue": kwargs.get("ytd_revenue"),
            "ytd_tax_reserve": kwargs.get("ytd_tax_reserve"),
            "pdf_path": kwargs.get("pdf_path", f"/dashboards/2024/SNAP_{kwargs['snapshot_date']}.pdf")

        }
        data["dashboard_snapshots"].append(new_snapshot)
        return json.dumps(new_snapshot["snapshot_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDashboardSnapshotWithInvoiceId",
                "description": "Create a new financial dashboard snapshot for a given year with invoice id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "snapshot_date": {"type": "string"},
                        "year": {"type": "integer"},
                        "notes": {"type": "string"}
                    },
                    "required": [ "snapshot_date", "year"],
                },
            },
        }

class AddMonthlyRevenue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Insert or update monthly revenue for a given snapshot.
        """

        record = {
            "row_id": "MON_"+kwargs["snapshot_id"],
            "snapshot_id": kwargs["snapshot_id"],
            "month_year": kwargs["month"],
            "revenue": kwargs["revenue"]
        }
        data["monthly_revenue"].append(record)

        return json.dumps(record["row_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddMonthlyRevenue",
                "description": "Insert or update monthly revenue for a given snapshot_id and month.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_id": {"type": "string"},
                        "snapshot_id": {"type": "string"},
                        "month": {"type": "string", "description": "Month in YYYY-MM format"},
                        "revenue": {"type": "number"}
                    },
                    "required": ["snapshot_id", "month", "revenue"],
                },
            },
        }


class AddProjectRevenue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Insert or update project revenue for a given snapshot.
        """
        record = next((pr for pr in data["project_revenue"]
                       if pr["snapshot_id"] == kwargs["snapshot_id"] and pr["project_id"] == kwargs["project_id"]),
                      None)

        if record:
            record["revenue"] = kwargs["revenue"]
        else:
            record = {
                "row_id": kwargs["row_id"],
                "snapshot_id": kwargs["snapshot_id"],
                "project_id": kwargs["project_id"],
                "revenue": kwargs["revenue"]
            }
            data["project_revenue"].append(record)

        return json.dumps(record["row_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddProjectRevenue",
                "description": "Insert or update project revenue for a given snapshot_id and project_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_id": {"type": "string"},
                        "snapshot_id": {"type": "string"},
                        "project_id": {"type": "string"},
                        "revenue": {"type": "number"}
                    },
                    "required": ["row_id", "snapshot_id", "project_id", "revenue"],
                },
            },
        }

class GetProjectPublisher(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        record = next((pr for pr in data["pipeline_opportunities"]
                       if pr["project_title"] == kwargs["name"]),
                      None)

        return json.dumps(record["publisher_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectPublisher",
                "description": "Get project publisher from project's name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                    },
                    "required": ["name"],
                },
            },
        }
# ---------------- READ TOOLS ----------------

class GetExpensesByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns expense_ids for all expenses under a given category_code.
        """
        category_code = kwargs["category_code"]
        expense_ids = [exp["expense_id"] for exp in data["expenses"] if exp["category_code"] == category_code]
        return json.dumps(expense_ids)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetExpensesByCategory",
                "description": "Fetch all expense_ids under a given category_code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category_code": {"type": "string", "description": "Expense category code"}
                    },
                    "required": ["category_code"],
                },
            },
        }


class GetRecurringExpenses(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns recurring_ids for all recurring expenses (optionally filtered by category_code).
        """
        category_code = kwargs.get("category_code")
        recs = data["recurring_schedules"]
        if category_code:
            recs = [r for r in recs if r["category_code"] == category_code]
        recurring_ids = [r["recurring_id"] for r in recs]
        return json.dumps(recurring_ids)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRecurringExpenses",
                "description": "Fetch recurring_ids for all recurring expenses, optionally filtered by category_code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category_code": {"type": "string", "description": "Optional filter by expense category"}
                    },
                    "required": [],
                },
            },
        }


# ---------------- WRITE TOOLS ----------------

class AddExpenseRecord(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Inserts a new expense record.
        """
        new_exp = {
            "expense_id": kwargs["expense_id"],
            "project_id": kwargs.get("project_id"),
            "vendor": kwargs["vendor"],
            "expense_date": kwargs["expense_date"],
            "amount": kwargs["amount"],
            "description": kwargs.get("description", ""),
            "payment_method": kwargs.get("payment_method", ""),
            "category_code": kwargs["category_code"],
            "created_at": kwargs.get("created_at", None)
        }
        data["expenses"].append(new_exp)
        return json.dumps(new_exp["expense_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddExpenseRecord",
                "description": "Insert a new expense record into expenses.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expense_id": {"type": "string"},
                        "vendor": {"type": "string"},
                        "expense_date": {"type": "string"},
                        "amount": {"type": "number"},
                        "description": {"type": "string"},
                        "payment_method": {"type": "string"},
                        "category_code": {"type": "string"},
                        "created_at": {"type": "string"}
                    },
                    "required": ["expense_id", "vendor", "expense_date", "amount", "category_code"],
                },
            },
        }


class AddRecurringExpense(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Inserts a new recurring expense schedule.
        """
        new_rec = {
            "recurring_id": kwargs["recurring_id"],
            "category_code": kwargs["category_code"],
            "amount": kwargs["amount"],
            "frequency": kwargs["frequency"],  # e.g., "monthly", "quarterly"
            "vendor": kwargs.get("vendor", ""),
            "start_date": kwargs.get("start_date", None),
            "end_date": kwargs.get("end_date", None)
        }
        data["recurring_schedules"].append(new_rec)
        return json.dumps(new_rec["recurring_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddRecurringExpense",
                "description": "Insert a new recurring expense schedule into recurring_schedules.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recurring_id": {"type": "string"},
                        "category_code": {"type": "string"},
                        "amount": {"type": "number"},
                        "frequency": {"type": "string"},
                        "vendor": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"}
                    },
                    "required": ["recurring_id", "category_code", "amount", "frequency"],
                },
            },
        }

class AddMonthlyExpense(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Insert or update monthly expense for a given snapshot.
        Deterministic: keyed by snapshot_id + month.
        """

        record = {
            "row_id": kwargs["snapshot_id"]+"_"+kwargs["month"],
            "snapshot_id": kwargs["snapshot_id"],
            "month_year": kwargs["month"],
            "amount": kwargs["amount"]
        }
        data.setdefault("monthly_expenses", []).append(record)

        return json.dumps(record["row_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddMonthlyExpense",
                "description": "Insert or update monthly expense for a given snapshot_id and month.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_id": {"type": "string"},
                        "snapshot_id": {"type": "string"},
                        "month": {"type": "string", "description": "Month in YYYY-MM format"},
                        "amount": {"type": "number"}
                    },
                    "required": ["snapshot_id", "month", "amount"],
                },
            },
        }
class GetMonthlyExpenseBySnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        snapshot_id = kwargs["snapshot_id"]
        for record in data.get("monthly_expenses", []):
            if record["snapshot_id"] == snapshot_id:
                return json.dumps(record["row_id"])
        return None
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMonthlyExpenseBySnapshot",
                "description": "Get monthly expense for a given snapshot_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"}
                    },
                    "required": ["snapshot_id"],
                },
            },
        }


class AddMonthlyAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Insert or update monthly expense for a given snapshot.
        Deterministic: keyed by snapshot_id + month.
        """

        record = {
            "row_id": kwargs["snapshot_id"]+"_"+kwargs["month"],
            "snapshot_id": kwargs["snapshot_id"],
            "month_year": kwargs["month"],
            "amount": kwargs["amount"]
        }
        data.setdefault("monthly_expenses", []).append(record)

        return json.dumps(record["row_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddMonthlyAudit",
                "description": "Insert or update monthly expense for a given snapshot_id and month.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_id": {"type": "string"},
                        "snapshot_id": {"type": "string"},
                        "month": {"type": "string", "description": "Month in YYYY-MM format"},
                        "amount": {"type": "number"}
                    },
                    "required": ["snapshot_id", "month", "amount"],
                },
            },
        }

# ---------------- READ TOOLS ----------------

class GetMonthlyAuditBySnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns row_ids of monthly expenses for a given snapshot_id.
        """
        snapshot_id = kwargs["snapshot_id"]
        records = [me["row_id"] for me in data.get("monthly_expenses", []) if me["snapshot_id"] == snapshot_id]
        return json.dumps(records)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMonthlyAuditBySnapshot",
                "description": "Retrieve all monthly expense row_ids tied to a dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string", "description": "Snapshot ID to filter monthly expenses"}
                    },
                    "required": ["snapshot_id"],
                },
            },
        }

class GetInvoiceAuditTrail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns audit_ids for all audit events tied to a given invoice_id.
        """
        invoice_id = kwargs["invoice_id"]
        audit_ids = [a["audit_id"] for a in data["invoice_audit"] if a["invoice_id"] == invoice_id]
        return json.dumps(audit_ids)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInvoiceAuditTrail",
                "description": "Retrieve audit_ids of all audit events tied to a specific invoice_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string", "description": "Invoice ID to fetch audit trail"}
                    },
                    "required": ["invoice_id"],
                },
            },
        }


class GetPaymentBehavior(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns payment_behavior_id(s) for a given publisher_id.
        """
        publisher_id = kwargs["publisher_id"]
        behaviors = [pb["behavior_id"] for pb in data["payment_behavior"] if pb["publisher_id"] == publisher_id]
        return json.dumps(behaviors)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPaymentBehavior",
                "description": "Retrieve payment_behavior_id(s) for a given publisher_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string", "description": "Publisher ID to fetch payment behavior"}
                    },
                    "required": ["publisher_id"],
                },
            },
        }


# ---------------- WRITE TOOLS ----------------
class ComputeInvoiceAging(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Compute days overdue, bucket, and escalation policy for a given invoice_id and as_of_date.
        """
        invoice_id = kwargs["invoice_id"]
        as_of_date = datetime.strptime(kwargs["as_of_date"], "%Y-%m-%d")

        invoice = next((inv for inv in data["invoices"] if inv["invoice_id"] == invoice_id), None)
        if not invoice:
            return json.dumps({"error": "invoice not found"})

        due_date = datetime.strptime(invoice["invoice_date"], "%Y-%m-%d")  # assume net 0 / same day due
        days_overdue = (as_of_date - due_date).days

        if days_overdue < 0:
            bucket = "upcoming_due"
            escalation = "none"
        elif days_overdue <= 30:
            bucket = "0-30"
            escalation = "friendly_reminder"
        elif days_overdue <= 60:
            bucket = "31-60"
            escalation = "formal_notice"
        elif days_overdue <= 90:
            bucket = "61-90"
            escalation = "phone_call"
        else:
            bucket = "90+"
            escalation = "collections_hold"

        return json.dumps({
            "invoice_id": invoice_id,
            "as_of_date": kwargs["as_of_date"],
            "days_overdue": days_overdue,
            "bucket": bucket,
            "escalation": escalation
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeInvoiceAging",
                "description": "Compute the aging and categorizes into bucket from invoices.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "as_of_date": {"type": "string"}
                    },
                    "required": ["as_of_date", "invoice_id"],
                },
            },
        }


class LogCollectionAction(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Logs a new collection action into invoice_audit.json.
        """
        new_action = {
            "audit_id": kwargs["audit_id"],
            "invoice_id": kwargs["invoice_id"],
            "event_type": kwargs["event_type"],   # e.g., "reminder_sent", "phone_call"
            "event_date": kwargs["event_date"],
            "outcome": kwargs.get("outcome", ""),
            "notes": kwargs.get("notes", "")
        }
        data["invoice_audit"].append(new_action)
        return json.dumps(new_action["audit_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogCollectionAction",
                "description": "Log a new collection event (reminder, call, escalation) for a given invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "invoice_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "event_date": {"type": "string"},
                        "outcome": {"type": "string"},
                        "notes": {"type": "string"}
                    },
                    "required": ["audit_id", "invoice_id", "event_type", "event_date"],
                },
            },
        }


import json
from datetime import datetime
from typing import Dict, Any

from domains.dto import Tool


class UpdatePaymentBehavior(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates or inserts a payment behavior record for a publisher.
        """
        publisher_id = kwargs["publisher_id"]
        record = next((pb for pb in data["payment_behavior"] if pb["publisher_id"] == publisher_id), None)

        if record:
            if "avg_days_to_pay" in kwargs:
                record["avg_days_to_pay"] = kwargs["avg_days_to_pay"]
            if "late_payment_frequency" in kwargs:
                record["late_payment_frequency"] = kwargs["late_payment_frequency"]
            record["last_updated"] = datetime.now().isoformat()
            return json.dumps(record["behavior_id"])

        return json.dumps({"error": f"No payment behavior profile found for publisher {publisher_id}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "UpdatePaymentBehavior",
                "description": "Updates the payment behavior data (e.g., avg_days_to_pay) for a given publisher.",
                "parameters": {
                    "type": "object", "properties": {
                        "publisher_id": {"type": "string", "description": "The ID of the publisher to update."},
                        "avg_days_to_pay": {"type": "number", "description": "The new calculated average days to pay."},
                        "late_payment_frequency": {"type": "number",
                                                   "description": "The new calculated late payment frequency (as a decimal)."}
                    },
                    "required": ["publisher_id"],
                },
            },
        }
# ---------------- READ TOOLS ----------------

class GetConsultantProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns consultant_id(s) (usually only one profile exists).
        """
        for c in data["consultants"]:
            if c["name"] == kwargs.get("name"):
                return json.dumps(c['consultant_id'])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetConsultantProfile",
                "description": "Retrieve consultant_id(s) from consultants.json.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        }


class GetTaxRate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns tax_rate_id(s). Optionally filter by year.
        """
        year = kwargs.get("year")
        if year:
            ids = [t["tax_rate_id"] for t in data["tax_rates"] if t.get("year") == year]
        else:
            ids = [t["tax_rate_id"] for t in data["tax_rates"]]
        return json.dumps(ids)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTaxRate",
                "description": "Retrieve tax_rate_id(s), optionally filtered by year.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "year": {"type": "integer", "description": "Optional tax year filter"}
                    },
                    "required": [],
                },
            },
        }


class GetBankAccountDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns bank_account_id(s). Optionally filter by account_type (chequing/savings).
        """
        account_type = kwargs.get("account_type")
        if account_type:
            ids = [b["account_id"] for b in data["bank_accounts"] if b["account_type"] == account_type]
        else:
            ids = [b["account_id"] for b in data["bank_accounts"]]
        return json.dumps(ids)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBankAccountDetails",
                "description": "Retrieve bank_account_id(s), optionally filtered by account_type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_type": {"type": "string", "description": "Optional filter (chequing, savings, etc.)"}
                    },
                    "required": [],
                },
            },
        }


# ---------------- WRITE TOOLS ----------------

class AddSchedulerRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Logs a scheduler run event.
        """
        new_run = {
            "run_id": kwargs.get("run_id"),
            "task_name": kwargs.get("task_name"),
            "run_date": kwargs["run_date"],
            "status": kwargs.get("status"),
            "notes": kwargs.get("notes", "")
        }
        data["scheduler_runs"].append(new_run)
        return json.dumps(new_run["run_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddSchedulerRun",
                "description": "Log a new scheduler run event into scheduler_runs.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "task_name": {"type": "string"},
                        "run_date": {"type": "string"},
                        "status": {"type": "string"},
                        "notes": {"type": "string"}
                    },
                    "required": ["run_date",],
                },
            },
        }


class UpdateBankAccountBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates or inserts balance for a given bank account.
        """
        account_id = kwargs["account_id"]
        new_balance = kwargs["balance"]
        account = next((b for b in data["bank_accounts"] if b["account_id"] == account_id), None)

        if account:
            account["balance"] = new_balance
        else:
            account = {
                "account_id": account_id,
                "account_type": kwargs.get("account_type", ""),
                "balance": new_balance
            }
            data["bank_accounts"].append(account)

        return json.dumps(account["account_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateBankAccountBalance",
                "description": "Update or insert a bank account balance in bank_accounts.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "balance": {"type": "number"},
                        "account_type": {"type": "string"}
                    },
                    "required": ["account_id", "balance"],
                },
            },
        }

class ListInvoiceAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        audit_id = kwargs.get("audit_id")
        results = []
        if audit_id:
            results = [a for a in data["invoice_audit"] if a["audit_id"] == audit_id]

        invoice_id = kwargs.get("invoice_id")
        if invoice_id:
            results = [a for a in data["invoice_audit"] if a["invoice_id"] == invoice_id]

        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListInvoiceAudit",
                "description": "List invoice audit from invoice_audit.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                    },
                    "required": ["audit_id" ],
                },
            },
        }

class FilterInvoices(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Filter invoices by conditions such as invoice_number, date range, amount, or paid/unpaid status.
        Returns a list of matching invoice_ids.
        """
        invoices = data["invoices"]
        results = invoices

        # Filter by invoice_number
        if "publisher_id" in kwargs:
            results = [inv for inv in results if inv["publisher_id"] == kwargs["publisher_id"]]

        # Filter by invoice_number
        if "invoice_number" in kwargs:
            results = [inv for inv in results if inv["invoice_number"] == kwargs["invoice_number"]]

        if "invoice_date" in kwargs:
            results = [inv for inv in results if inv["invoice_date"] == kwargs["invoice_date"]]

        # Filter by date range
        if "start_date" in kwargs and "end_date" in kwargs:
            start = datetime.strptime(kwargs["start_date"], "%Y-%m-%d")
            end = datetime.strptime(kwargs["end_date"], "%Y-%m-%d")
            results = [
                inv for inv in results
                if start <= datetime.strptime(inv["invoice_date"], "%Y-%m-%d") <= end
            ]

        # Filter unpaid invoices only
        if kwargs.get("unpaid_only"):
            results = [inv for inv in results if inv.get("paid_at") is None]

        # Filter by minimum/maximum amount
        if "min_amount" in kwargs:
            results = [inv for inv in results if float(inv["total_due"]) >= kwargs["min_amount"]]
        if "max_amount" in kwargs:
            results = [inv for inv in results if float(inv["total_due"]) <= kwargs["max_amount"]]

        return json.dumps([inv["invoice_id"] for inv in results])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterInvoices",
                "description": "Filter publisher invoices by invoice_number, date range, unpaid_only, or amount thresholds.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_number": {"type": "string"},
                        "start_date": {"type": "string", "description": "Start of invoice_date range (YYYY-MM-DD)"},
                        "end_date": {"type": "string", "description": "End of invoice_date range (YYYY-MM-DD)"},
                        "unpaid_only": {"type": "boolean", "description": "Filter only unpaid invoices"},
                        "min_amount": {"type": "number", "description": "Minimum invoice total_due"},
                        "max_amount": {"type": "number", "description": "Maximum invoice total_due"}
                    },
                    "required": [],
                },
            },
        }

class ComputeNetCashFlow(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Compute net cash flow from inflows and outflows.
        Returns inflows, outflows, and net result.
        """
        inflows = kwargs["inflows"]
        outflows = kwargs["outflows"]
        net = round(inflows - outflows, 2)

        return json.dumps({
            "inflows": inflows,
            "outflows": outflows,
            "net": net
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeNetCashFlow",
                "description": "Compute net cash flow from inflows and outflows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inflows": {"type": "number", "description": "Sum of expected inflows"},
                        "outflows": {"type": "number", "description": "Sum of expected outflows"}
                    },
                    "required": ["inflows", "outflows"],
                },
            },
        }


class CalculateTotalInflows(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Calculates the sum of `total_due` for all unpaid invoices within a date range.
        Can be filtered by a specific publisher.
        """
        start_date = datetime.strptime(kwargs["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(kwargs["end_date"], "%Y-%m-%d")

        invoices_ids = kwargs.get("invoices_to_consider", None)
        invoices_to_consider = []

        for id in invoices_ids:
            invoices_to_consider.append(next((inv for inv in data["invoices"] if inv["invoice_id"] == id), None))

        # Considers past-due invoices as immediately receivable within the window.
        total_inflow = sum(
            inv["total_due"] for inv in invoices_to_consider
            if datetime.strptime(inv["invoice_date"], "%Y-%m-%d") <= end_date
        )
        return json.dumps({"period_start": kwargs["start_date"], "period_end": kwargs["end_date"], "total_inflows": round(total_inflow, 2)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "CalculateTotalInflows",
                "description": "Calculates the sum of all unpaid invoices expected within a date range, optionally for a specific publisher.",
                "parameters": {
                    "type": "object", "properties": {
                        "start_date": {"type": "string", "description": "Start of the forecast period (YYYY-MM-DD)"},
                        "end_date": {"type": "string", "description": "End of the forecast period (YYYY-MM-DD)"},
                        "invoices_to_consider": {"type": "Object", "description": "List of invoices to consider" }
                    }, "required": ["start_date", "end_date"],
                },
            },
        }
from datetime import datetime, timedelta
class CalculateTotalOutflows(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Calculates the sum of all recurring expenses scheduled to be paid within a date range.
        """
        start_date = datetime.strptime(kwargs["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(kwargs["end_date"], "%Y-%m-%d")
        total_outflow = 0

        for schedule in data["recurring_schedules"]:
            if not schedule.get("is_active"):
                continue

            # This is a simplified logic for monthly/quarterly payments
            if schedule["frequency"] == "monthly":
                # Check for payment in the start month and next month to cover the 30-day window
                for month_offset in range(2):
                    current_month_start = (start_date.replace(day=1) + timedelta(days=32 * month_offset)).replace(day=1)
                    if schedule["payment_day"] != "variable":
                        payment_date = current_month_start.replace(day=int(schedule["payment_day"]))
                        if start_date <= payment_date <= end_date:
                            total_outflow += schedule["amount"]
            elif schedule["frequency"] == "quarterly":
                 if start_date.month in schedule["payment_months"]:
                     total_outflow += schedule["amount"]

        return json.dumps({"period_start": kwargs["start_date"], "period_end": kwargs["end_date"], "total_outflows": round(total_outflow, 2)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "CalculateTotalOutflows",
                "description": "Calculates the sum of all recurring expenses scheduled to be paid within a date range.",
                "parameters": {
                    "type": "object", "properties": {
                        "start_date": {"type": "string", "description": "Start of the forecast period (YYYY-MM-DD)"},
                        "end_date": {"type": "string", "description": "End of the forecast period (YYYY-MM-DD)"},
                    }, "required": ["start_date", "end_date"],
                },
            },
        }


class CreatePublisher(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Creates a new publisher and adds it to the publishers.json data.
        """
        new_publisher = {
            "publisher_id": kwargs["publisher_id"],
            "name": kwargs["name"],
            "address": kwargs.get("address", ""),
            "contact_email": kwargs.get("contact_email", ""),
            "gst_number": kwargs.get("gst_number", ""),
            "created_at": "2024-08-08T12:00:00",
            "updated_at": "2024-08-08T12:00:00",
        }
        data["publishers"].append(new_publisher)
        return json.dumps(new_publisher["publisher_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "CreatePublisher",
                "description": "Create a new publisher record.",
                "parameters": {
                    "type": "object", "properties": {
                        "publisher_id": {"type": "string", "description": "Unique ID for the new publisher"},
                        "name": {"type": "string", "description": "Name of the new publisher"}
                    },
                    "required": ["publisher_id", "name"],
                },
            },
        }

class GetPublisherInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves the full details for a given publisher_id.
        """
        publisher_id = kwargs["publisher_id"]
        publisher = next((p for p in data["publishers"] if p["publisher_id"] == publisher_id), None)
        return json.dumps(publisher)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "GetPublisherInfo",
                "description": "Retrieve full details for a given publisher ID.",
                "parameters": {
                    "type": "object", "properties": {
                        "publisher_id": {"type": "string", "description": "The ID of the publisher to retrieve"}
                    },
                    "required": ["publisher_id"],
                },
            },
        }

class CreateProject(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Creates a new project for a publisher.
        """
        new_project = {
            "project_id": kwargs["project_id"],
            "publisher_id": kwargs["publisher_id"],
            "isbn": kwargs["isbn"],
            "project_title": kwargs["project_title"],
            "default_hourly_rate": kwargs["default_hourly_rate"],
            "is_active": True,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        data["projects"].append(new_project)
        return json.dumps(new_project["project_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "CreateProject",
                "description": "Create a new project record for a publisher.",
                "parameters": {
                    "type": "object", "properties": {
                        "project_id": {"type": "string"},
                        "publisher_id": {"type": "string"},
                        "isbn": {"type": "string"},
                        "project_title": {"type": "string"},
                        "default_hourly_rate": {"type": "number"}
                    },
                    "required": ["project_id", "publisher_id", "isbn", "project_title", "default_hourly_rate"],
                },
            },
        }

class GetProjectDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves the full details for a given project_id.
        """
        project_id = kwargs["project_id"]
        project = next((p for p in data["projects"] if p["project_id"] == project_id), None)
        return json.dumps(project)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "GetProjectDetails",
                "description": "Retrieve full details for a given project ID.",
                "parameters": {
                    "type": "object", "properties": {
                        "project_id": {"type": "string", "description": "The ID of the project to retrieve"}
                    },
                    "required": ["project_id"],
                },
            },
        }

class ComputeCollectionKPIs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        window_months = int(kwargs.get("window_months", 12))
        invs = data.get("invoices", []) or []
        total_ar = sum(float(i.get("total_due", 0)) for i in invs if i.get("paid_at") is None)
        avg_daily_sales = round((sum(float(i.get("subtotal", 0)) for i in invs) / max(1, window_months * 30)), 2)
        dso = round((total_ar / max(0.01, avg_daily_sales)), 2)
        return json.dumps({
            "window_months": window_months,
            "total_ar": round(total_ar, 2),
            "avg_daily_sales": avg_daily_sales,
            "dso": dso
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeCollectionKPIs",
                "description": "Compute A/R collection KPIs (total A/R, avg daily sales, DSO) over a window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "window_months": {"type": "integer"}
                    },
                    "required": []
                }
            }
        }


class CalculateInvoiceTotals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Calculates subtotal, hst, and total for a list of line items.
        """
        lines = kwargs.get("lines", [])
        hst_rate = kwargs.get("hst_rate", 0.13)
        subtotal = sum(line.get("hours", 0) * line.get("rate", 0) for line in lines)
        hst_amount = round(subtotal * hst_rate, 2)
        total_due = round(subtotal + hst_amount, 2)
        return json.dumps({"subtotal": subtotal, "hst_amount": hst_amount, "total_due": total_due})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "CalculateInvoiceTotals",
                "description": "A simple calculator to compute invoice totals from line items.",
                "parameters": {
                    "type": "object", "properties": {
                        "lines": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {"hours": {"type": "number"}, "rate": {"type": "number"}}
                            }
                        },
                        "hst_rate": {"type": "number", "description": "The HST rate to apply, e.g., 0.13 for 13%"}
                    },
                    "required": ["lines", "hst_rate"],
                },
            },
        }

class ExportARAgingReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Simulates the export of an A/R aging report and returns the file path.
        """
        period_label = kwargs["period_label"]
        file_path = f"/reports/ar_aging/AR_Aging_Report_{period_label}.pdf"
        return json.dumps(file_path)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "ExportARAgingReport",
                "description": "Exports an Accounts Receivable (A/R) aging report for a given period.",
                "parameters": {
                    "type": "object", "properties": {
                        "period_label": {"type": "string",
                                         "description": "The period for the report, e.g., '2024-09'"}
                    },
                    "required": ["period_label"],
                },
            },
        }


class SendInvoiceEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Simulates sending an invoice email and updates the sent_at field on the invoice.
        """
        invoice_number = kwargs["invoice_number"]
        sent_time = '2025-09-05T00:00:00Z' #datetime.now().isoformat()
        publisher_id = kwargs.get("publisher_id")
        consultant_id = kwargs.get("consultant_id")
        subject = kwargs.get("subject", "")
        body_text = kwargs.get("body_text", "")
        attachment = kwargs.get("attachment", "")

        invoice = next((inv for inv in data["invoices"] if inv["invoice_number"] == invoice_number), None)
        if invoice:
            invoice["sent_at"] = sent_time
            return json.dumps({"status": "success", "invoice_id": invoice["invoice_id"], "sent_at": sent_time})
        return json.dumps({"status": "error", "message": "Invoice not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "SendInvoiceEmail",
                "description": "Sends an invoice email to a publisher and updates the invoice's sent_at timestamp.",
                "parameters": {
                    "type": "object", "properties": {
                        "publisher_id": {"type": "string"},
                        "consultant_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                        "subject": {"type": "string"},
                        "body_text": {"type": "string"},
                        "attachment": {"type": "string"}
                    },
                    "required": ["publisher_id", "invoice_number", "subject"],
                },
            },
        }


class GetInvoiceDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves the full details for a given invoice_number.
        """
        invoice_number = kwargs["invoice_number"]
        invoice = next((inv for inv in data["invoices"] if inv["invoice_number"] == invoice_number), None)
        return json.dumps(invoice)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "GetInvoiceDetails",
                "description": "Retrieve the full details for a given invoice by its invoice_number.",
                "parameters": {
                    "type": "object", "properties": {
                        "invoice_number": {"type": "string", "description": "The number of the invoice to retrieve"}
                    },
                    "required": ["invoice_number"],
                },
            },
        }


class RecordInvoiceAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Finds an invoice by number and logs an audit event for it.
        """
        invoice_number = kwargs["invoice_number"]
        invoice = next((inv for inv in data["invoices"] if inv["invoice_number"] == invoice_number), None)
        if not invoice:
            return json.dumps({"error": "Invoice not found"})

        new_event = {
            "audit_id": f"AUD_{invoice['invoice_id']}_{len(data['invoice_audit']) + 1}",
            "invoice_id": invoice['invoice_id'],
            "event_type": kwargs.get("event_type"),
            "event_timestamp": "2024-09-05T00:00:00Z",
            "notes": kwargs.get("notes", f"Event '{kwargs.get('event_type')}' triggered.")
        }
        data["invoice_audit"].append(new_event)
        return json.dumps(new_event)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "RecordInvoiceAudit",
                "description": "Records an audit event for a given invoice number.",
                "parameters": {
                    "type": "object", "properties": {
                        "invoice_number": {"type": "string"},
                        "event_type": {"type": "string"}
                    },
                    "required": ["invoice_number", "event_type"],
                },
            },
        }

class SendNotificationEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Simulates sending a general notification email. Does not require an invoice.
        """
        return json.dumps({
            "status": "success",
            "message": "Notification email sent.",
            "recipient_publisher_id": kwargs.get("publisher_id"),
            "sender_consultant_id": kwargs.get("consultant_id"),
            "subject": kwargs.get("subject")
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendNotificationEmail",
                "description": "Sends a general, non-invoice-related email notification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string", "description": "ID of the publisher contact to send the email to."},
                        "consultant_id": {"type": "string", "description": "ID of the consultant sending the email."},
                        "subject": {"type": "string", "description": "The subject line of the email."},
                        "body_text": {"type": "string", "description": "The body content of the email."}
                    },
                    "required": ["publisher_id", "consultant_id", "subject", "body_text"],
                },
            },
        }

class GetProjectByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns project_id for a given project_title.
        """
        project_title = kwargs["project_name"]
        project = next((p for p in data["projects"] if p["project_title"] == project_title), None)
        return json.dumps(project["project_id"] if project else None)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectByName",
                "description": "Retrieve project_id for a given project name/title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string", "description": "Exact project title to look up"}
                    },
                    "required": ["project_name"],
                },
            },
        }

class GetTimeEntryDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves the full details for a given time_entry_id.
        """
        time_entry_id = kwargs["time_entry_id"]
        entry = next((t for t in data["time_entries"] if t["time_entry_id"] == time_entry_id), None)
        return json.dumps(entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTimeEntryDetails",
                "description": "Retrieve the full details for a given time entry ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "time_entry_id": {"type": "string", "description": "The ID of the time entry to retrieve"}
                    },
                    "required": ["time_entry_id"],
                },
            },
        }

TOOLS = [
    GetPublisherByName(), GetPublisherInvoices(), GetInvoiceLines(), GetProjectTimeEntries(), GetProjectPublisher(),
    CreateInvoice(), UpdateInvoicePayment(), LogInvoiceAuditEvent(), CreateDashboardSnapshotWithInvoiceId(),
    GetDashboardSnapshot(), GetMonthlyRevenueBySnapshot(), GetProjectRevenueSummary(), AddMonthlyAudit(),
    CreateDashboardSnapshot(), AddMonthlyRevenue(), AddMonthlyExpense(), AddProjectRevenue(), GetMonthlyAuditBySnapshot(),
    GetExpensesByCategory(), GetRecurringExpenses(), FilterInvoices(),
    AddExpenseRecord(), AddRecurringExpense(), CreateInvoiceLine(), ComputeInvoiceAging(),
    GetInvoiceAuditTrail(), GetPaymentBehavior(), LogCollectionAction(), UpdatePaymentBehavior(),
    GetConsultantProfile(), GetTaxRate(), GetBankAccountDetails(), AddSchedulerRun(), UpdateBankAccountBalance(),
    ComputeNetCashFlow(), CalculateTotalInflows(), CalculateTotalOutflows(), GetMonthlyExpenseBySnapshot(),
    CreatePublisher(), GetPublisherInfo(), CreateProject(), GetProjectDetails(), GetTimeEntryDetails(),
    ComputeCollectionKPIs(), CalculateInvoiceTotals(), ExportARAgingReport(), GetProjectByName(),
    SendInvoiceEmail(), GetInvoiceDetails(), RecordInvoiceAudit(), ListInvoiceAudit(), SendNotificationEmail()
]