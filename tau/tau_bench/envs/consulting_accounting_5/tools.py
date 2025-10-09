import json
from datetime import datetime
from typing import Any, Dict

from tau_bench.envs.tool import Tool

#---------------- ACCESS TOOLS ----------------



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


class GetPublisherByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], publisher_name: str) -> str:
        """
        Returns publisher_id for a given publisher name.
        """
        name = publisher_name
        pub = next((p for p in data["publishers"].values() if p["name"] == name), None)
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
    def invoke(data: Dict[str, Any], publisher_id: str) -> str:
        """
        Returns all invoice_ids for a given publisher_id.
        """
        invoices = [inv for inv in data["invoices"].values() if inv["publisher_id"] == publisher_id]
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
    def invoke(data: Dict[str, Any], invoice_id: str, project_id: str, hours: int = 1, rate: float = 1.0, hst_rate: float = 0.13) -> str:
        """
        Insert a new invoice line linked to an existing invoice_id.
        Deterministic: uses provided invoice_id, project_id, isbn, hours, rate, hst_rate.
        Returns created line_id.
        """
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
                        "invoice_id": {"type": "string", "description": "Invoice ID to add line to"},
                        "project_id": {"type": "string", "description": "Project ID for the line item"}
                    },
                    "required": ["invoice_id", "project_id"],
                },
            },
        }

class GetInvoiceLines(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], invoice_id: str) -> str:
        """
        Returns invoice_line_ids for a given invoice_id.
        """
        lines = [ln for ln in data["invoice_lines"].values() if ln["invoice_id"] == invoice_id]
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
    def invoke(data: Dict[str, Any], project_id: int) -> str:
        entries = [te['hours_worked'] for te in data["time_entries"].values() if te["project_id"] == project_id]
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


#---------------- MODIFY TOOLS ----------------

class CreateInvoice(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        invoice_number: str,
        publisher_id: str,
        subtotal: float,
        hst_amount: float,
        total_due: float,
        invoice_date: str = None,
        period_start: str = None,
        period_end: str = None,
        pdf_path: str = "",
        sent_at: str = None,
        paid_at: str = None,
        created_at: str = None,
        currency: str = "CAD",
        notes: str = ""
    ) -> str:
        """
        Creates a new invoice with core required fields and many optional ones.
        Non-critical fields default to None or empty string if not provided.
        """
        new_invoice = {
            "invoice_id": f'INV{invoice_number}',
            "invoice_number": invoice_number,
            "publisher_id": publisher_id,
            "invoice_date": invoice_date,
            "period_start": period_start,
            "period_end": period_end,
            "subtotal": subtotal,
            "hst_amount": hst_amount,
            "total_due": total_due,
            "pdf_path": pdf_path,
            "sent_at": sent_at,
            "paid_at": paid_at,
            "created_at": created_at,
            "currency": currency,
            "notes": notes
        }
        data["invoices"][invoice_id] = new_invoice
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
    def invoke(data: Dict[str, Any], invoice_id: str, paid_at: str) -> str:
        """
        Marks an invoice as paid by updating paid_at field.
        """
        updated = None
        for inv in data["invoices"].values():
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
    def invoke(
        data: Dict[str, Any],
        event_type: str = None,
        invoice_id: str = None,
        notes: str = ""
    ) -> str:
        """
        Logs an audit event for an invoice.
        """
        new_event = {
            "audit_id": f"AUD_{invoice_id}",
            "invoice_id": invoice_id,
            "event_type": event_type,
            "notes": notes
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
                        "invoice_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "notes": {"type": "string"}
                    },
                    "required": ["invoice_id", "event_type"],
                },
            },
        }


#---------------- ACCESS TOOLS ----------------

class GetDashboardSnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], snapshot_id: str) -> str:
        """
        Returns the snapshot_id if found.
        """
        snapshot = next((s for s in data["dashboard_snapshots"].values() if s["snapshot_id"] == snapshot_id), None)
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
    def invoke(data: Dict[str, Any], snapshot_id: str) -> str:
        """
        Returns row_ids of monthly revenue for a given snapshot_id.
        """
        records = [mr["row_id"] for mr in data["monthly_revenue"].values() if mr["snapshot_id"] == snapshot_id]
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
    def invoke(data: Dict[str, Any], snapshot_id: str) -> str:
        """
        Returns row_ids of project revenue for a given snapshot_id.
        """
        records = [pr["row_id"] for pr in data["project_revenue"].values() if pr["snapshot_id"] == snapshot_id]
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
    def invoke(
        data: Dict[str, Any],
        notes: str = "Year-end snapshot",
        snapshot_date: str = None,
        snapshot_id: str = None,
        year: Any = None
    ) -> str:
        """
        Create a new dashboard snapshot.
        """
        new_snapshot = {
            "snapshot_id": snapshot_id,
            "snapshot_date": snapshot_date,
            "notes": notes
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
    def invoke(
        data: Dict[str, Any],
        invoice_id: str,
        notes: str = "Year-end snapshot",
        pdf_path: str = None,
        snapshot_date: str = None,
        year: Any = None,
        ytd_revenue: float = None,
        ytd_tax_reserve: float = None
    ) -> str:
        """
        Create a new dashboard snapshot.
        """
        snapshot_id = f"SNAP_{invoice_id}"
        if pdf_path is None:
            pdf_path = f"/dashboards/2024/SNAP_{snapshot_date}.pdf"
        new_snapshot = {
            "snapshot_id": snapshot_id,
            "snapshot_date": snapshot_date,
            "notes": notes,
            "ytd_revenue": ytd_revenue,
            "ytd_tax_reserve": ytd_tax_reserve,
            "pdf_path": pdf_path
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
                        "invoice_id": {"type": "string"},
                        "snapshot_date": {"type": "string"},
                        "year": {"type": "integer"},
                        "notes": {"type": "string"}
                    },
                    "required": ["invoice_id", "snapshot_date", "year"],
                },
            },
        }

class AddMonthlyRevenue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], snapshot_id: str, month: str, revenue: float) -> str:
        """
        Insert or update monthly revenue for a given snapshot.
        """

        record = {
            "row_id": "MON_" + snapshot_id,
            "snapshot_id": snapshot_id,
            "month_year": month,
            "revenue": revenue
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
    def invoke(
        data: Dict[str, Any],
        project_id: int,
        revenue: float,
        row_id: int = None,
        snapshot_id: int = None
    ) -> str:
        """
        Insert or update project revenue for a given snapshot.
        """
        record = next((pr for pr in data["project_revenue"].values()
                       if pr["snapshot_id"] == snapshot_id and pr["project_id"] == project_id),
                      None)

        if record:
            record["revenue"] = revenue
        else:
            record = {
                "row_id": row_id,
                "snapshot_id": snapshot_id,
                "project_id": project_id,
                "revenue": revenue
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
    def invoke(data: Dict[str, Any], name: str) -> str:
        record = next((pr for pr in data["pipeline_opportunities"].values()
                       if pr["project_title"] == name),
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
#---------------- ACCESS TOOLS ----------------

class GetExpensesByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], category_code: str) -> str:
        """
        Returns expense_ids for all expenses under a given category_code.
        """
        expense_ids = [exp["expense_id"] for exp in data["expenses"].values() if exp["category_code"] == category_code]
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
    def invoke(data: Dict[str, Any], category_code: str = None) -> str:
        """
        Returns recurring_ids for all recurring expenses (optionally filtered by category_code).
        """
        recs = data["recurring_schedules"]
        if category_code:
            recs = [r for r in recs.values() if r["category_code"] == category_code]
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


#---------------- MODIFY TOOLS ----------------

class AddExpenseRecord(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        expense_id: str,
        project_id: str = None,
        vendor: str = None,
        expense_date: str = None,
        amount: float = None,
        description: str = "",
        payment_method: str = "",
        category_code: str = None,
        created_at: str = None
    ) -> str:
        """
        Inserts a new expense record.
        """
        new_exp = {
            "expense_id": expense_id,
            "project_id": project_id,
            "vendor": vendor,
            "expense_date": expense_date,
            "amount": amount,
            "description": description,
            "payment_method": payment_method,
            "category_code": category_code,
            "created_at": created_at
        }
        data["expenses"][expense_id] = new_exp
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
    def invoke(
        data: Dict[str, Any], 
        recurring_id: str, 
        category_code: str, 
        amount: float, 
        frequency: str, 
        vendor: str = "", 
        start_date: Any = None, 
        end_date: Any = None
    ) -> str:
        """
        Inserts a new recurring expense schedule.
        """
        new_rec = {
            "recurring_id": recurring_id,
            "category_code": category_code,
            "amount": amount,
            "frequency": frequency,
            "vendor": vendor,
            "start_date": start_date,
            "end_date": end_date
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
    def invoke(data: Dict[str, Any], snapshot_id: str, month: str, amount: float) -> str:
        """
        Insert or update monthly expense for a given snapshot.
        Deterministic: keyed by snapshot_id + month.
        """

        record = {
            "row_id": snapshot_id + "_" + month,
            "snapshot_id": snapshot_id,
            "month_year": month,
            "amount": amount
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
    def invoke(data: Dict[str, Any], snapshot_id: str) -> str:
        for record in data.get("monthly_expenses", {}).values():
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
    def invoke(data: Dict[str, Any], snapshot_id: str, month: str, amount: float) -> str:
        """
        Insert or update monthly expense for a given snapshot.
        Deterministic: keyed by snapshot_id + month.
        """

        record = {
            "row_id": snapshot_id + "_" + month,
            "snapshot_id": snapshot_id,
            "month_year": month,
            "amount": amount
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
                        "snapshot_id": {"type": "string"},
                        "month": {"type": "string", "description": "Month in YYYY-MM format"},
                        "amount": {"type": "number"}
                    },
                    "required": ["snapshot_id", "month", "amount"],
                },
            },
        }

#---------------- ACCESS TOOLS ----------------

class GetMonthlyAuditBySnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], snapshot_id: str) -> str:
        """
        Returns row_ids of monthly expenses for a given snapshot_id.
        """
        records = [me["row_id"] for me in data.get("monthly_expenses", {}).values() if me["snapshot_id"] == snapshot_id]
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
    def invoke(data: Dict[str, Any], invoice_id: str) -> str:
        """
        Returns audit_ids for all audit events tied to a given invoice_id.
        """
        audit_ids = [a["audit_id"] for a in data["invoice_audit"].values() if a["invoice_id"] == invoice_id]
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
    def invoke(data: Dict[str, Any], publisher_id: str) -> str:
        """
        Returns payment_behavior_id(s) for a given publisher_id.
        """
        behaviors = [pb["behavior_id"] for pb in data["payment_behavior"].values() if pb["publisher_id"] == publisher_id]
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


#---------------- MODIFY TOOLS ----------------
class ComputeInvoiceAging(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], invoice_id: str, as_of_date: str) -> str:
        """
        Compute days overdue, bucket, and escalation policy for a given invoice_id and as_of_date.
        """
        as_of_date = datetime.strptime(as_of_date, "%Y-%m-%d")

        invoice = next((inv for inv in data["invoices"].values() if inv["invoice_id"] == invoice_id), None)
        if not invoice:
            return json.dumps({"error": "invoice not found"})

        due_date = datetime.strptime(invoice["invoice_date"], "%Y-%m-%d")
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
            "as_of_date": as_of_date.strftime("%Y-%m-%d"),
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
    def invoke(
        data: Dict[str, Any],
        audit_id: str,
        event_date: str = None,
        event_type: str = None,
        invoice_id: str = None,
        notes: str = "",
        outcome: str = ""
    ) -> str:
        """
        Logs a new collection action into invoice_audit.json.
        """
        new_action = {
            "audit_id": audit_id,
            "invoice_id": invoice_id,
            "event_type": event_type,
            "event_date": event_date,
            "outcome": outcome,
            "notes": notes
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


class UpdatePaymentBehavior(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], publisher_id: str, avg_days_to_pay: int = None, late_payment_frequency: int = None) -> str:
        """
        Updates or inserts a payment behavior record for a publisher.
        """
        record = next((pb for pb in data["payment_behavior"].values() if pb["publisher_id"] == publisher_id), None)

        if record:
            if avg_days_to_pay is not None:
                record["avg_days_to_pay"] = avg_days_to_pay
            if late_payment_frequency is not None:
                record["late_payment_frequency"] = late_payment_frequency
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
#---------------- ACCESS TOOLS ----------------

class GetConsultantProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name: str = None) -> str:
        """
        Returns consultant_id(s) (usually only one profile exists).
        """
        for c in data["consultants"].values():
            if c["name"] == name:
                return json.dumps(c['consultant_id'])
        return json.dumps(None)
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
    def invoke(data: Dict[str, Any], year: int = None) -> str:
        """
        Returns tax_rate_id(s). Optionally filter by year.
        """
        if year:
            ids = [t["tax_rate_id"] for t in data["tax_rates"].values() if t.get("year") == year]
        else:
            ids = [t["tax_rate_id"] for t in data["tax_rates"].values()]
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
    def invoke(data: Dict[str, Any], account_type: str = None) -> str:
        """
        Returns bank_account_id(s). Optionally filter by account_type (chequing/savings).
        """
        if account_type:
            ids = [b["account_id"] for b in data["bank_accounts"].values() if b["account_type"] == account_type]
        else:
            ids = [b["account_id"] for b in data["bank_accounts"].values()]
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


#---------------- MODIFY TOOLS ----------------

class AddSchedulerRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str = None, task_name: str = None, run_date: str = None, status: str = None, notes: str = "", note: str = None) -> str:
        """
        Logs a scheduler run event.
        """
        # Accept either 'note' or 'notes' parameter
        if note is not None:
            notes = note
        new_run = {
            "run_id": run_id,
            "task_name": task_name,
            "run_date": run_date,
            "status": status,
            "notes": notes
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
                    "required": ["run_date"],
                },
            },
        }


class UpdateBankAccountBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, balance: float, account_type: str = "") -> str:
        """
        Updates or inserts balance for a given bank account.
        """
        account = next((b for b in data["bank_accounts"].values() if b["account_id"] == account_id), None)

        if account:
            account["balance"] = balance
        else:
            account = {
                "account_id": account_id,
                "account_type": account_type,
                "balance": balance
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
    def invoke(data: Dict[str, Any], audit_id: str = None, invoice_id: str = None) -> str:
        results = []
        if audit_id:
            results = [a for a in data["invoice_audit"].values() if a["audit_id"] == audit_id]

        if invoice_id:
            results = [a for a in data["invoice_audit"].values() if a["invoice_id"] == invoice_id]

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
                    "required": ["audit_id"],
                },
            },
        }

class FilterInvoices(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        publisher_id: str = None,
        invoice_number: str = None,
        invoice_date: str = None,
        start_date: str = None,
        end_date: str = None,
        unpaid_only: bool = False,
        min_amount: float = None,
        max_amount: float = None
    ) -> str:
        """
        Filter invoices by conditions such as invoice_number, date range, amount, or paid/unpaid status.
        Returns a list of matching invoice_ids.
        """
        invoices = data["invoices"]
        results = invoices

        if publisher_id is not None:
            results = [inv for inv in results.values() if inv["publisher_id"] == publisher_id]

        if invoice_number is not None:
            results = [inv for inv in results.values() if inv["invoice_number"] == invoice_number]

        if invoice_date is not None:
            results = [inv for inv in results.values() if inv["invoice_date"] == invoice_date]

        if start_date is not None and end_date is not None:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            results = [
                inv for inv in results
                if start <= datetime.strptime(inv["invoice_date"], "%Y-%m-%d") <= end
            ]

        if unpaid_only:
            results = [inv for inv in results.values() if inv.get("paid_at") is None]

        if min_amount is not None:
            results = [inv for inv in results.values() if float(inv["total_due"]) >= min_amount]
        if max_amount is not None:
            results = [inv for inv in results.values() if float(inv["total_due"]) <= max_amount]

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
    def invoke(data: Dict[str, Any], inflows: float, outflows: float) -> str:
        """
        Compute net cash flow from inflows and outflows.
        Returns inflows, outflows, and net result.
        """
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
    def invoke(data: Dict[str, Any], start_date: str, end_date: str, invoices_to_consider: list = None) -> str:
        """
        Calculates the sum of `total_due` for all unpaid invoices within a date range.
        Can be filtered by a specific publisher.
        """
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

        invoices_to_consider = invoices_to_consider or []
        invoices_to_consider_list = []

        for id in invoices_to_consider:
            invoices_to_consider_list.append(next((inv for inv in data["invoices"].values() if inv["invoice_id"] == id), None))

        total_inflow = sum(
            inv["total_due"] for inv in invoices_to_consider_list
            if inv and datetime.strptime(inv["invoice_date"], "%Y-%m-%d") <= end_date_obj
        )
        return json.dumps({"period_start": start_date_obj.strftime("%Y-%m-%d"), "period_end": end_date_obj.strftime("%Y-%m-%d"), "total_inflows": round(total_inflow, 2)})
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
                        "invoices_to_consider": {"type": "array", "items": {"type": "string"}, "description": "List of invoices to consider" }
                    }, "required": ["start_date", "end_date"],
                },
            },
        }
from datetime import timedelta


class CalculateTotalOutflows(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], start_date: str, end_date: str) -> str:
        """
        Calculates the sum of all recurring expenses scheduled to be paid within a date range.
        """
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        total_outflow = 0

        for schedule in data["recurring_schedules"].values():
            if not schedule.get("is_active"):
                continue

            if schedule["frequency"] == "monthly":
                for month_offset in range(2):
                    current_month_start = (start_date_obj.replace(day=1) + timedelta(days=32 * month_offset)).replace(day=1)
                    if schedule["payment_day"] != "variable":
                        payment_date = current_month_start.replace(day=int(schedule["payment_day"]))
                        if start_date_obj <= payment_date <= end_date_obj:
                            total_outflow += schedule["amount"]
            elif schedule["frequency"] == "quarterly":
                if start_date_obj.month in schedule["payment_months"]:
                    total_outflow += schedule["amount"]

        return json.dumps({"period_start": start_date_obj.strftime("%Y-%m-%d"), "period_end": end_date_obj.strftime("%Y-%m-%d"), "total_outflows": round(total_outflow, 2)})
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
    def invoke(data: Dict[str, Any], publisher_id: str, name: str, address: str = "", contact_email: str = "", gst_number: str = "") -> str:
        """
        Creates a new publisher and adds it to the publishers.json data.
        """
        new_publisher = {
            "publisher_id": publisher_id,
            "name": name,
            "address": address,
            "contact_email": contact_email,
            "gst_number": gst_number,
            "created_at": "2024-08-08T12:00:00",
            "updated_at": "2024-08-08T12:00:00",
        }
        data["publishers"][publisher_id] = new_publisher
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
    def invoke(data: Dict[str, Any], publisher_id: str) -> str:
        """
        Retrieves the full details for a given publisher_id.
        """
        publisher = next((p for p in data["publishers"].values() if p["publisher_id"] == publisher_id), None)
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
    def invoke(data: Dict[str, Any], project_id: str, publisher_id: str, isbn: str, project_title: str, default_hourly_rate: float) -> str:
        """
        Creates a new project for a publisher.
        """
        new_project = {
            "project_id": project_id,
            "publisher_id": publisher_id,
            "isbn": isbn,
            "project_title": project_title,
            "default_hourly_rate": default_hourly_rate,
            "is_active": True,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        data["projects"][project_id] = new_project
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
    def invoke(data: Dict[str, Any], project_id: str) -> str:
        """
        Retrieves the full details for a given project_id.
        """
        project = next((p for p in data["projects"].values() if p["project_id"] == project_id), None)
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
    def invoke(data: Dict[str, Any], window_months: int = 12) -> str:
        invs = data.get("invoices", {}).values() or []
        total_ar = sum(float(i.get("total_due", 0)) for i in invs.values() if i.get("paid_at") is None)
        avg_daily_sales = round((sum(float(i.get("subtotal", 0)) for i in invs.values()) / max(1, window_months * 30)), 2)
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
    def invoke(data: Dict[str, Any], lines: list = None, hst_rate: float = 0.13) -> str:
        """
        Calculates subtotal, hst, and total for a list of line items.
        """
        if lines is None:
            lines = []
        subtotal = sum(line.get("hours", 0) * line.get("rate", 0) for line in lines.values())
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
    def invoke(data: Dict[str, Any], period_label: str) -> str:
        """
        Simulates the export of an A/R aging report and returns the file path.
        """
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
    def invoke(data: Dict[str, Any], invoice_number: str, publisher_id: str = None, consultant_id: str = None, subject: str = "", body_text: str = "", attachment: str = "") -> str:
        """
        Simulates sending an invoice email and updates the sent_at field on the invoice.
        """
        sent_time = '2025-09-05T00:00:00Z'

        invoice = next((inv for inv in data["invoices"].values() if inv["invoice_number"] == invoice_number), None)
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
    def invoke(data: Dict[str, Any], invoice_number: str) -> str:
        """
        Retrieves the full details for a given invoice_number.
        """
        invoice = next((inv for inv in data["invoices"].values() if inv["invoice_number"] == invoice_number), None)
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
    def invoke(data: Dict[str, Any], invoice_number: str, event_type: str = None, notes: str = None) -> str:
        """
        Finds an invoice by number and logs an audit event for it.
        """
        invoice = next((inv for inv in data["invoices"].values() if inv["invoice_number"] == invoice_number), None)
        if not invoice:
            return json.dumps({"error": "Invoice not found"})

        new_event = {
            "audit_id": f"AUD_{invoice['invoice_id']}_{len(data['invoice_audit']) + 1}",
            "invoice_id": invoice['invoice_id'],
            "event_type": event_type,
            "event_timestamp": "2024-09-05T00:00:00Z",
            "notes": notes if notes is not None else f"Event '{event_type}' triggered."
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
    def invoke(
        data: Dict[str, Any],
        body_text: Any = None,
        consultant_id: str = None,
        publisher_id: str = None,
        subject: str = None
    ) -> str:
        """
        Simulates sending a general notification email. Does not require an invoice.
        """
        return json.dumps({
            "status": "success",
            "message": "Notification email sent.",
            "recipient_publisher_id": publisher_id,
            "sender_consultant_id": consultant_id,
            "subject": subject
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
    def invoke(data: Dict[str, Any], project_name: str) -> str:
        """
        Returns project_id for a given project_title.
        """
        project_title = project_name
        project = next((p for p in data["projects"].values() if p["project_title"] == project_title), None)
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
    def invoke(data: Dict[str, Any], time_entry_id: str) -> str:
        """
        Retrieves the full details for a given time_entry_id.
        """
        entry = next((t for t in data["time_entries"].values() if t["time_entry_id"] == time_entry_id), None)
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