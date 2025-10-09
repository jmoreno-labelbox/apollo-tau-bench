import json
from datetime import datetime, timedelta
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def _calculate_hst(subtotal: float, rate: float = 0.13) -> float:
    """Compute HST (13% standard for Ontario)"""
    return round(subtotal * rate, 2)


def _find_all(lst: list[dict[str, Any]], key: str, value: Any) -> list[dict[str, Any]]:
    return [x for x in lst or [] if x.get(key) == value]


def _calculate_aging_days(invoice_date: str, current_date: str = "2024-12-10") -> int:
    """Determine days from invoice date to today"""
    try:
        invoice = datetime.fromisoformat(
            invoice_date.replace("Z", "+00:00")
            if "T" in invoice_date
            else invoice_date + "T00:00:00+00:00"
        )
        current = datetime.fromisoformat(current_date + "T00:00:00+00:00")
        return (current - invoice).days
    except:
        return 0


#Utility functions (pure)
def _error(msg: str) -> str:
    payload = {"error": msg}
    out = json.dumps(payload)
    return out


def _find_one(lst: list[dict[str, Any]], key: str, value: Any) -> dict[str, Any] | None:
    for x in lst or []:
        if x.get(key) == value:
            return x
    return None


def _ok(**payload) -> str:
    out = {"status": "success"}
    out.update(payload)
    payload = out
    out = json.dumps(payload)
    return out


#ENTITY SEARCHES


class CaV2GetConsultantProfile(Tool):
    """Fetch consultant profile details."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        consultants = data.get("consultants", {}).values()
        if not consultants:
            return _error("No consultant profile found.")
        payload = consultants[0]
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetConsultantProfile",
                "description": "Retrieve the consultant's profile information including contact details and GST number.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class CaV2FindPublisherByName(Tool):
    """Locate publisher using name."""

    @staticmethod
    def invoke(data: dict[str, Any], publisher_name: str = None) -> str:
        if not publisher_name:
            return _error("publisher_name is required.")
        publishers = data.get("publishers", {}).values()
        publisher = _find_one(list(publishers.values()), "name", publisher_name)
        return (
            json.dumps(publisher)
            if publisher
            else _error(f"Publisher '{publisher_name}' not found.")
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2FindPublisherByName",
                "description": "Find a publisher by their name.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_name": {"type": "string"}},
                    "required": ["publisher_name"],
                },
            },
        }


class CaV2FindProjectByIsbn(Tool):
    """Locate project using ISBN."""

    @staticmethod
    def invoke(data: dict[str, Any], isbn: str = None) -> str:
        if not isbn:
            return _error("isbn is required.")
        projects = data.get("projects", {}).values()
        project = _find_one(list(projects.values()), "isbn", isbn)
        return (
            json.dumps(project)
            if project
            else _error(f"Project with ISBN '{isbn}' not found.")
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2FindProjectByIsbn",
                "description": "Find a project by its ISBN code.",
                "parameters": {
                    "type": "object",
                    "properties": {"isbn": {"type": "string"}},
                    "required": ["isbn"],
                },
            },
        }


class CaV2GetProjectById(Tool):
    """Retrieve project information using project ID."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        if not project_id:
            return _error("project_id is required.")

        projects = data.get("projects", {}).values()
        project = _find_one(list(projects.values()), "project_id", project_id)

        if not project:
            return _error(f"Project {project_id} not found.")

        return _ok(
            project_id=project.get("project_id"),
            isbn=project.get("isbn"),
            title=project.get("title"),
            publisher_id=project.get("publisher_id"),
            default_hourly_rate=project.get("default_hourly_rate"),
            override_hourly_rate=project.get("override_hourly_rate"),
            status=project.get("status"),
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetProjectById",
                "description": "Get project details by project ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }


class CaV2GetProjectsByPublisher(Tool):
    """Retrieve all projects associated with a specific publisher."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        active_only: bool = True,
        publisher_id: str = None
    ) -> str:
        if not publisher_id:
            return _error("publisher_id is required.")

        projects = data.get("projects", {}).values()
        publisher_projects = _find_all(projects, "publisher_id", publisher_id)

        if active_only:
            publisher_projects = [
                p for p in publisher_projects if p.get("is_active", True)
            ]
        payload = publisher_projects
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetProjectsByPublisher",
                "description": "Get all projects for a specific publisher, optionally filtering to active projects only.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string"},
                        "active_only": {"type": "boolean", "default": True},
                    },
                    "required": ["publisher_id"],
                },
            },
        }


class CaV2GetTimeEntriesForPeriod(Tool):
    """Retrieve time logs for a specific project within a date range."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None, start_date: str = None, end_date: str = None) -> str:
        if not all([project_id, start_date, end_date]):
            return _error("project_id, start_date, and end_date are required.")

        time_entries = data.get("time_entries", {}).values()
        filtered_entries = []

        for entry in time_entries.values():
            if (
                entry.get("project_id") == project_id
                and start_date <= entry.get("entry_date", "") <= end_date
            ):
                filtered_entries.append(entry)
        payload = filtered_entries
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetTimeEntriesForPeriod",
                "description": "Get time entries for a specific project within a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"},
                    },
                    "required": ["project_id", "start_date", "end_date"],
                },
            },
        }


class CaV2GetUnpaidInvoices(Tool):
    """Retrieve all outstanding invoices."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        invoices = data.get("invoices", {}).values()
        unpaid_invoices = [inv for inv in invoices.values() if not inv.get("paid_at")]
        payload = unpaid_invoices
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetUnpaidInvoices",
                "description": "Get all invoices that have not been paid yet.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class CaV2GetInvoiceById(Tool):
    """Retrieve a specific invoice using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None) -> str:
        if not invoice_id:
            return _error("invoice_id is required.")

        invoices = data.get("invoices", {}).values()
        invoice = _find_one(list(invoices.values()), "invoice_id", invoice_id)
        return (
            json.dumps(invoice)
            if invoice
            else _error(f"Invoice '{invoice_id}' not found.")
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetInvoiceById",
                "description": "Get a specific invoice by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"invoice_id": {"type": "string"}},
                    "required": ["invoice_id"],
                },
            },
        }


class CaV2GetInvoiceLinesForInvoice(Tool):
    """Retrieve all line items for a specific invoice."""

    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None) -> str:
        if not invoice_id:
            return _error("invoice_id is required.")

        invoice_lines = data.get("invoice_lines", {}).values()
        lines = _find_all(invoice_lines, "invoice_id", invoice_id)
        payload = lines
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetInvoiceLinesForInvoice",
                "description": "Get all line items for a specific invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {"invoice_id": {"type": "string"}},
                    "required": ["invoice_id"],
                },
            },
        }


class CaV2GetExpensesByCategory(Tool):
    """Retrieve expenses filtered by category and an optional date range."""

    @staticmethod
    def invoke(data: dict[str, Any], category_code: str = None, start_date: str = None, end_date: str = None) -> str:
        if not category_code:
            return _error("category_code is required.")

        expenses = data.get("expenses", {}).values()
        filtered_expenses = _find_all(expenses, "category_code", category_code)

        if start_date and end_date:
            filtered_expenses = [
                exp
                for exp in filtered_expenses
                if start_date <= exp.get("expense_date", "") <= end_date
            ]
        payload = filtered_expenses
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetExpensesByCategory",
                "description": "Get expenses filtered by category code and optionally by date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category_code": {"type": "string"},
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"},
                    },
                    "required": ["category_code"],
                },
            },
        }


class CaV2GetExpenseCategories(Tool):
    """Retrieve all expense categories along with their deductibility guidelines."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        expense_categories = data.get("expense_categories", {}).values()
        payload = expense_categories
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetExpenseCategories",
                "description": "Get all expense categories with their deductibility percentages and rules.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class CaV2GetPaymentBehaviorByPublisher(Tool):
    """Retrieve payment behavior information for a specific publisher."""

    @staticmethod
    def invoke(data: dict[str, Any], publisher_id: str = None) -> str:
        if not publisher_id:
            return _error("publisher_id is required.")

        payment_behaviors = data.get("payment_behavior", {}).values()
        behavior = _find_one(list(payment_behaviors.values()), "publisher_id", publisher_id)
        return (
            json.dumps(behavior)
            if behavior
            else _error(f"Payment behavior for publisher '{publisher_id}' not found.")
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetPaymentBehaviorByPublisher",
                "description": "Get payment behavior patterns for a specific publisher.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_id": {"type": "string"}},
                    "required": ["publisher_id"],
                },
            },
        }


class CaV2GetBankAccounts(Tool):
    """Retrieve all details regarding bank accounts."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        bank_accounts = data.get("bank_accounts", {}).values()
        payload = bank_accounts
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetBankAccounts",
                "description": "Get all business bank accounts with current balances.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class CaV2GetPipelineOpportunities(Tool):
    """Retrieve pipeline opportunities, optionally filtered by stage or likelihood."""

    @staticmethod
    def invoke(data: dict[str, Any], stage: str = None, min_probability: float = None) -> str:
        opportunities = data.get("pipeline_opportunities", {}).values()

        if stage:
            opportunities = [opp for opp in opportunities.values() if opp.get("stage") == stage]

        if min_probability is not None:
            opportunities = [
                opp
                for opp in opportunities.values() if opp.get("probability", 0) >= min_probability
            ]
        payload = opportunities
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetPipelineOpportunities",
                "description": "Get pipeline opportunities, optionally filtered by stage or minimum probability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "stage": {"type": "string"},
                        "min_probability": {
                            "type": "number",
                            "minimum": 0,
                            "maximum": 1,
                        },
                    },
                    "required": [],
                },
            },
        }


class CaV2GetRecurringSchedules(Tool):
    """Retrieve recurring scheduled payments categorized by type."""

    @staticmethod
    def invoke(data: dict[str, Any], schedule_type: str = None, active_only: bool = True) -> str:
        schedules = data.get("recurring_schedules", {}).values()

        if schedule_type:
            schedules = _find_all(schedules, "schedule_type", schedule_type)

        if active_only:
            schedules = [sch for sch in schedules.values() if sch.get("is_active", True)]
        payload = schedules
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetRecurringSchedules",
                "description": "Get recurring scheduled payments, optionally filtered by type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "schedule_type": {"type": "string"},
                        "active_only": {"type": "boolean", "default": True},
                    },
                    "required": [],
                },
            },
        }


#COMPUTATION & ANALYSIS RESOURCES


class CaV2CalculateInvoiceAging(Tool):
    """Determine aging categories for outstanding invoices."""

    @staticmethod
    def invoke(data: dict[str, Any], current_date: str = "2024-12-10") -> str:
        invoices = data.get("invoices", {}).values()
        unpaid_invoices = [inv for inv in invoices.values() if not inv.get("paid_at")]

        aging_buckets = {
            "current": [],  # 0 to 30 days
            "31_60": [],  # 31 to 60 days
            "61_90": [],  # 61 to 90 days
            "over_90": [],  # More than 90 days
        }

        for invoice in unpaid_invoices:
            days_overdue = _calculate_aging_days(
                invoice.get("invoice_date", ""), current_date
            )

            aging_info = {
                "invoice_id": invoice.get("invoice_id"),
                "invoice_number": invoice.get("invoice_number"),
                "publisher_id": invoice.get("publisher_id"),
                "total_due": invoice.get("total_due"),
                "invoice_date": invoice.get("invoice_date"),
                "days_overdue": days_overdue,
            }

            if days_overdue <= 30:
                aging_buckets["current"].append(aging_info)
            elif days_overdue <= 60:
                aging_buckets["31_60"].append(aging_info)
            elif days_overdue <= 90:
                aging_buckets["61_90"].append(aging_info)
            else:
                aging_buckets["over_90"].append(aging_info)
        payload = aging_buckets
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CalculateInvoiceAging",
                "description": "Calculate aging buckets for all unpaid invoices.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_date": {"type": "string", "format": "date"}
                    },
                    "required": [],
                },
            },
        }


class CaV2CalculateYtdRevenue(Tool):
    """Compute revenue and tax reserve from the start of the year."""

    @staticmethod
    def invoke(data: dict[str, Any], year: str = "2024", tax_rate: float = 0.265) -> str:
        invoices = data.get("invoices", {}).values()
        ytd_invoices = [
            inv for inv in invoices.values() if inv.get("invoice_date", "").startswith(year)
        ]

        total_revenue = sum(inv.get("subtotal", 0) for inv in ytd_invoices.values()
        tax_reserve = round(total_revenue * tax_rate, 2)

        revenue_by_month = {}
        for invoice in ytd_invoices:
            month = invoice.get("invoice_date", "")[:7]  # Year-Month
            if month not in revenue_by_month:
                revenue_by_month[month] = 0
            revenue_by_month[month] += invoice.get("subtotal", 0)

        return _ok(
            year=year,
            ytd_revenue=total_revenue,
            ytd_tax_reserve=tax_reserve,
            revenue_by_month=revenue_by_month,
            invoice_count=len(ytd_invoices),
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CalculateYtdRevenue",
                "description": "Calculate year-to-date revenue, tax reserve, and monthly breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "year": {"type": "string"},
                        "tax_rate": {"type": "number", "default": 0.265},
                    },
                    "required": [],
                },
            },
        }


class CaV2CalculateProjectProfitability(Tool):
    """Compute profitability indicators for projects."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        if not project_id:
            return _error("project_id is required.")

        # Retrieve project information
        projects = data.get("projects", {}).values()
        project = _find_one(list(projects.values()), "project_id", project_id)
        if not project:
            return _error(f"Project '{project_id}' not found.")

        # Compute income from invoices
        invoice_lines = data.get("invoice_lines", {}).values()
        project_lines = _find_all(invoice_lines, "project_id", project_id)
        total_revenue = sum(line.get("line_amount", 0) for line in project_lines.values()
        total_hours = sum(line.get("hours_billed", 0) for line in project_lines.values()

        # Determine actual hourly rate
        effective_rate = total_revenue / total_hours if total_hours > 0 else 0
        expected_rate = project.get("override_hourly_rate") or project.get(
            "default_hourly_rate", 0
        )

        return _ok(
            project_id=project_id,
            project_title=project.get("project_title"),
            total_revenue=total_revenue,
            total_hours_billed=total_hours,
            effective_hourly_rate=round(effective_rate, 2),
            expected_hourly_rate=expected_rate,
            rate_variance=round(effective_rate - expected_rate, 2),
            is_active=project.get("is_active"),
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CalculateProjectProfitability",
                "description": "Calculate profitability metrics for a specific project.",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }


class CaV2CalculateExpenseSummary(Tool):
    """Compute a summary of expenses by category for a specified timeframe."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        year: str = "2024",
        start_date: str = None,
        end_date: str = None,
        category_filter: list = None
    ) -> str:
        if category_filter is None:
            category_filter = []

        expenses = data.get("expenses", {}).values()
        expense_categories = data.get("expense_categories", {}).values()

        # Narrow down expenses by date range
        if start_date and end_date:
            filtered_expenses = [
                exp
                for exp in expenses.values() if start_date <= exp.get("expense_date", "") <= end_date
            ]
        else:
            # Narrow down expenses by year
            filtered_expenses = [
                exp for exp in expenses.values() if exp.get("expense_date", "").startswith(year)
            ]

        # Narrow down by categories if provided
        if category_filter:
            filtered_expenses = [
                exp
                for exp in filtered_expenses
                if exp.get("category_code") in category_filter
            ]

        # Categorize by group
        category_summary = {}
        for expense in filtered_expenses:
            category_code = expense.get("category_code")
            if category_code not in category_summary:
                category_summary[category_code] = {
                    "total_gross": 0,
                    "total_deductible": 0,
                    "count": 0,
                }

            gross_amount = expense.get("gross_amount", 0)
            allowed_amount = expense.get("allowed_amount", 0)

            category_summary[category_code]["total_gross"] += gross_amount
            category_summary[category_code]["total_deductible"] += allowed_amount
            category_summary[category_code]["count"] += 1

        # Include category names and verify deductible does not surpass gross
        for category_code, summary in category_summary.items():
            category_info = _find_one(
                expense_categories, "category_code", category_code
            )
            summary["category_name"] = (
                category_info.get("name", "Unknown") if category_info else "Unknown"
            )
            summary["deductible_percent"] = (
                category_info.get("deductible_percent", 0) if category_info else 0
            )

            # Confirm deductible remains below gross amount
            if summary["total_deductible"] > summary["total_gross"]:
                summary["total_deductible"] = summary["total_gross"]

        total_deductible = sum(
            summary["total_deductible"] for summary in category_summary.values()
        )

        return _ok(
            year=year,
            category_summary=category_summary,
            total_deductible_expenses=round(total_deductible, 2),
            total_expense_count=len(filtered_expenses),
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CalculateExpenseSummary",
                "description": "Calculate expense summary by category for a given year.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "year": {"type": "string"},
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"},
                        "category_filter": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": [],
                },
            },
        }


#INVOICE HANDLING RESOURCES


class CaV2CreateInvoice(Tool):
    """Generate a new invoice."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        invoice_id: str = None,
        invoice_number: str = None,
        publisher_id: str = None,
        invoice_date: str = None,
        period_start: str = None,
        period_end: str = None,
        subtotal: float = None,
        sent_at: str = None,
        paid_at: str = None,
        created_at: str = None,
    ) -> str:
        # Necessary parameters

        if not all(
            [
                invoice_number,
                publisher_id,
                invoice_date,
                period_start,
                period_end,
                subtotal,
            ]
        ):
            return _error(
                "Required fields: invoice_number, publisher_id, invoice_date, period_start, period_end, subtotal"
            )

        # Compute HST and overall total
        hst_amount = _calculate_hst(subtotal)
        total_due = round(subtotal + hst_amount, 2)

        # Generate invoice entry
        new_invoice = {
            "invoice_id": invoice_id or f"INV{len(data.get("invoices", {})) + 1:03d}",
            "invoice_number": invoice_number,
            "publisher_id": publisher_id,
            "invoice_date": invoice_date,
            "period_start": period_start,
            "period_end": period_end,
            "subtotal": subtotal,
            "hst_amount": hst_amount,
            "total_due": total_due,
            "pdf_path": f"/invoices/{invoice_date[:4]}/{invoice_number}.pdf",
            "sent_at": sent_at,
            "paid_at": paid_at,
            "created_at": created_at or invoice_date + "T00:00:00Z",
        }

        # Insert into data
        data.setdefault("invoices", []).append(new_invoice)

        return _ok(
            invoice_id=invoice_id,
            invoice_number=invoice_number,
            total_due=total_due,
            hst_amount=hst_amount,
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateInvoice",
                "description": "Create a new invoice with automatic HST calculation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                        "publisher_id": {"type": "string"},
                        "invoice_date": {"type": "string", "format": "date"},
                        "period_start": {"type": "string", "format": "date"},
                        "period_end": {"type": "string", "format": "date"},
                        "subtotal": {"type": "number"},
                        "sent_at": {"type": "string"},
                        "paid_at": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "invoice_number",
                        "publisher_id",
                        "invoice_date",
                        "period_start",
                        "period_end",
                        "subtotal",
                    ],
                },
            },
        }


class CaV2CreateInvoiceLine(Tool):
    """Generate a line item for an invoice."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        invoice_line_id: str = None,
        invoice_id: str = None,
        project_id: str = None,
        isbn: str = None,
        hours_billed: float = None,
        hourly_rate: float = None
    ) -> str:
        # Necessary parameters

        if not all(
            [invoice_line_id, invoice_id, project_id, isbn, hours_billed, hourly_rate]
        ):
            return _error(
                "All line item fields are required: invoice_line_id, invoice_id, project_id, isbn, hours_billed, hourly_rate"
            )

        line_amount = round(hours_billed * hourly_rate, 2)

        new_line = {
            "invoice_line_id": invoice_line_id,
            "invoice_id": invoice_id,
            "project_id": project_id,
            "isbn": isbn,
            "hours_billed": hours_billed,
            "hourly_rate": hourly_rate,
            "line_amount": line_amount,
        }

        # Insert into data
        data.setdefault("invoice_lines", []).append(new_line)

        return _ok(invoice_line_id=invoice_line_id, line_amount=line_amount)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateInvoiceLine",
                "description": "Create an invoice line item with automatic amount calculation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_line_id": {"type": "string"},
                        "invoice_id": {"type": "string"},
                        "project_id": {"type": "string"},
                        "isbn": {"type": "string"},
                        "hours_billed": {"type": "number"},
                        "hourly_rate": {"type": "number"},
                    },
                    "required": [
                        "invoice_line_id",
                        "invoice_id",
                        "project_id",
                        "isbn",
                        "hours_billed",
                        "hourly_rate",
                    ],
                },
            },
        }


class CaV2UpdateInvoicePayment(Tool):
    """Modify the payment status of an invoice."""

    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, paid_at: str = None) -> str:
        if not invoice_id:
            return _error("invoice_id is required.")

        invoices = data.get("invoices", {}).values()
        invoice = _find_one(list(invoices.values()), "invoice_id", invoice_id)

        if not invoice:
            return _error(f"Invoice '{invoice_id}' not found.")

        invoice["paid_at"] = paid_at

        return _ok(invoice_id=invoice_id, paid_at=paid_at, status="payment_updated")

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2UpdateInvoicePayment",
                "description": "Update the payment status of an invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "paid_at": {"type": "string"},
                    },
                    "required": ["invoice_id"],
                },
            },
        }


class CaV2CreateInvoiceAuditEntry(Tool):
    """Generate an audit log entry for invoice activities."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str = None,
        event_timestamp: str = None,
        event_type: str = None,
        invoice_id: str = None,
        notes: str = ""
    ) -> str:
        if not all([audit_id, invoice_id, event_type, event_timestamp]):
            return _error(
                "audit_id, invoice_id, event_type, and event_timestamp are required."
            )

        audit_entry = {
            "audit_id": audit_id,
            "invoice_id": invoice_id,
            "event_type": event_type,
            "event_timestamp": event_timestamp,
            "notes": notes,
        }

        data.setdefault("invoice_audit", []).append(audit_entry)

        return _ok(audit_id=audit_id, event_type=event_type)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateInvoiceAuditEntry",
                "description": "Create an audit trail entry for invoice actions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "invoice_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "event_timestamp": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": [
                        "audit_id",
                        "invoice_id",
                        "event_type",
                        "event_timestamp",
                    ],
                },
            },
        }


#EXPENSE HANDLING RESOURCES


class CaV2CreateExpense(Tool):
    """Generate a new expense entry."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        category_code: str = None,
        created_at: str = None,
        currency: str = "CAD",
        description: str = None,
        expense_date: str = None,
        expense_id: str = None,
        gross_amount: float = None,
        payment_method: str = None,
        receipt_path: str = None,
        vendor: str = None
    ) -> str:
        if not all(
            [expense_id, vendor, expense_date, gross_amount, description, category_code]
        ):
            return _error(
                "Required fields: expense_id, vendor, expense_date, gross_amount, description, category_code"
            )

        # Retrieve category to determine permissible amount
        expense_categories = data.get("expense_categories", {}).values()
        category = _find_one(list(expense_categories.values()), "category_code", category_code)

        if not category:
            return _error(f"Expense category '{category_code}' not found.")

        deductible_percent = category.get("deductible_percent", 100) / 100
        allowed_amount = round(gross_amount * deductible_percent, 2)

        new_expense = {
            "expense_id": expense_id,
            "vendor": vendor,
            "expense_date": expense_date,
            "gross_amount": gross_amount,
            "currency": currency,
            "description": description,
            "payment_method": payment_method,
            "category_code": category_code,
            "allowed_amount": allowed_amount,
            "receipt_path": receipt_path or f"/receipts/{expense_date[:4]}/{expense_id}_receipt.pdf",
            "created_at": created_at or expense_date + "T00:00:00Z",
        }

        data.setdefault("expenses", []).append(new_expense)

        return _ok(
            expense_id=expense_id,
            allowed_amount=allowed_amount,
            deductible_percent=category.get("deductible_percent"),
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateExpense",
                "description": "Create a new expense record with automatic deductible amount calculation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expense_id": {"type": "string"},
                        "vendor": {"type": "string"},
                        "expense_date": {"type": "string", "format": "date"},
                        "gross_amount": {"type": "number"},
                        "currency": {"type": "string", "default": "CAD"},
                        "description": {"type": "string"},
                        "payment_method": {"type": "string"},
                        "category_code": {"type": "string"},
                        "receipt_path": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "expense_id",
                        "vendor",
                        "expense_date",
                        "gross_amount",
                        "description",
                        "category_code",
                    ],
                },
            },
        }


#CASH FLOW & PREDICTION RESOURCES


class CaV2ForecastCashFlow(Tool):
    """Predict cash flow considering outstanding invoices and payment patterns."""

    @staticmethod
    def invoke(data: dict[str, Any], forecast_months: int = 3, current_date: str = "2024-12-10") -> str:
        # Retrieve outstanding invoices
        invoices = data.get("invoices", {}).values()
        unpaid_invoices = [inv for inv in invoices.values() if not inv.get("paid_at")]

        # Retrieve payment patterns
        payment_behaviors = data.get("payment_behavior", {}).values()

        # Predict collections
        forecasted_collections = []
        for invoice in unpaid_invoices:
            publisher_id = invoice.get("publisher_id")
            behavior = _find_one(list(payment_behaviors.values()), "publisher_id", publisher_id)

            avg_days = behavior.get("avg_days_to_pay", 30) if behavior else 30
            invoice_date = datetime.fromisoformat(
                invoice.get("invoice_date") + "T00:00:00"
            )
            expected_payment = invoice_date + timedelta(days=avg_days)

            forecasted_collections.append(
                {
                    "invoice_id": invoice.get("invoice_id"),
                    "invoice_number": invoice.get("invoice_number"),
                    "amount": invoice.get("total_due"),
                    "expected_payment_date": expected_payment.strftime("%Y-%m-%d"),
                    "confidence": (
                        behavior.get("payment_consistency", "moderate")
                        if behavior
                        else "moderate"
                    ),
                }
            )

        # Retrieve regular expenses
        recurring_schedules = data.get("recurring_schedules", {}).values()
        active_schedules = [sch for sch in recurring_schedules.values() if sch.get("is_active")]

        # Condense data monthly
        monthly_summary = {}
        for i in range(forecast_months):
            month_start = datetime.fromisoformat(
                current_date + "T00:00:00"
            ) + timedelta(days=30 * i)
            month_key = month_start.strftime("%Y-%m")
            monthly_summary[month_key] = {
                "expected_collections": 0,
                "scheduled_expenses": 0,
                "net_flow": 0,
            }

        # Include collections in summary
        for collection in forecasted_collections:
            payment_month = collection["expected_payment_date"][:7]
            if payment_month in monthly_summary:
                monthly_summary[payment_month]["expected_collections"] += collection[
                    "amount"
                ]

        # Include expenses in summary
        for schedule in active_schedules:
            monthly_amount = schedule.get("amount", 0)
            for month_key in monthly_summary.keys():
                if schedule.get("frequency") == "monthly":
                    monthly_summary[month_key]["scheduled_expenses"] += monthly_amount

        # Compute net cash flow
        for month_data in monthly_summary.values():
            month_data["net_flow"] = (
                month_data["expected_collections"] - month_data["scheduled_expenses"]
            )

        return _ok(
            forecast_period_months=forecast_months,
            forecasted_collections=forecasted_collections,
            monthly_summary=monthly_summary,
            total_expected_collections=sum(c["amount"] for c in forecasted_collections.values()),
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2ForecastCashFlow",
                "description": "Forecast cash flow based on unpaid invoices, payment behavior, and recurring expenses.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "forecast_months": {"type": "integer", "default": 3},
                        "current_date": {"type": "string", "format": "date"},
                    },
                    "required": [],
                },
            },
        }


#DASHBOARD & ANALYSIS RESOURCES


class CaV2CreateDashboardSnapshot(Tool):
    """Generate a dashboard snapshot displaying current financial metrics."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        snapshot_id: str = None,
        snapshot_date: str = None,
        ytd_revenue: float = None,
        ytd_tax_reserve: float = None,
        pdf_path: str = None
    ) -> str:
        if not snapshot_date:
            return _error("snapshot_date is required")

        snapshot = {
            "snapshot_id": snapshot_id
            or f"SNAP{len(data.get("dashboard_snapshots", {})) + 1:03d}",
            "snapshot_date": snapshot_date,
            "ytd_revenue": ytd_revenue or 0.0,
            "ytd_tax_reserve": ytd_tax_reserve or 0.0,
            "pdf_path": pdf_path
            or f"/dashboards/{snapshot_date[:4]}/dashboard_{snapshot_date}.pdf",
        }

        data.setdefault("dashboard_snapshots", []).append(snapshot)

        return _ok(snapshot_id=snapshot_id, snapshot_date=snapshot_date)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateDashboardSnapshot",
                "description": "Create a financial dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "snapshot_date": {"type": "string", "format": "date"},
                        "ytd_revenue": {"type": "number"},
                        "ytd_tax_reserve": {"type": "number"},
                        "pdf_path": {"type": "string"},
                    },
                    "required": ["snapshot_date"],
                },
            },
        }


class CaV2GetTaxRateByYear(Tool):
    """Retrieve the tax rate for a particular year."""

    @staticmethod
    def invoke(data: dict[str, Any], year: int = None) -> str:
        if not year:
            return _error("year is required.")

        tax_rates = data.get("tax_rates", {}).values()
        tax_rate = _find_one(list(tax_rates.values()), "tax_year", int(year))
        return (
            json.dumps(tax_rate)
            if tax_rate
            else _error(f"Tax rate for year {year} not found.")
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetTaxRateByYear",
                "description": "Get the tax rate for a specific year.",
                "parameters": {
                    "type": "object",
                    "properties": {"year": {"type": "string"}},
                    "required": ["year"],
                },
            },
        }


class CaV2CreateProjectRevenue(Tool):
    """Generate a project revenue entry for the dashboard snapshot."""

    @staticmethod
    def invoke(data: dict[str, Any], row_id: str = None, snapshot_id: str = None, project_id: str = None, ytd_revenue: float = None) -> str:
        if not all([row_id, snapshot_id, project_id, ytd_revenue]):
            return _error(
                "Required fields: row_id, snapshot_id, project_id, ytd_revenue"
            )

        project_revenue = {
            "row_id": row_id,
            "snapshot_id": snapshot_id,
            "project_id": project_id,
            "ytd_revenue": ytd_revenue,
        }

        data.setdefault("project_revenue", []).append(project_revenue)

        return _ok(row_id=row_id, project_id=project_id, ytd_revenue=ytd_revenue)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateProjectRevenue",
                "description": "Create a project revenue record for a dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_id": {"type": "string"},
                        "snapshot_id": {"type": "string"},
                        "project_id": {"type": "string"},
                        "ytd_revenue": {"type": "number"},
                    },
                    "required": ["row_id", "snapshot_id", "project_id", "ytd_revenue"],
                },
            },
        }


class CaV2CreateMonthlyRevenue(Tool):
    """Generate a monthly revenue entry for the dashboard snapshot."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        row_id: str = None,
        snapshot_id: str = None,
        month_year: str = None,
        revenue: float = None,
        tax_reserve: float = None,
        profit_flag: str = "normal"
    ) -> str:
        if not all([month_year, revenue, tax_reserve]):
            return _error("Required fields: month_year, revenue, tax_reserve")

        monthly_revenue = {
            "row_id": row_id or f"REV{len(data.get("monthly_revenue", {})) + 1:03d}",
            "snapshot_id": snapshot_id
            or f"SNAP{len(data.get("dashboard_snapshots", {})) + 1:03d}",
            "month_year": month_year,
            "revenue": revenue,
            "tax_reserve": tax_reserve,
            "profit_flag": profit_flag,
        }

        data.setdefault("monthly_revenue", []).append(monthly_revenue)

        return _ok(
            row_id=monthly_revenue["row_id"], month_year=month_year, revenue=revenue
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateMonthlyRevenue",
                "description": "Create a monthly revenue record for a dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_id": {"type": "string"},
                        "snapshot_id": {"type": "string"},
                        "month_year": {"type": "string"},
                        "revenue": {"type": "number"},
                        "tax_reserve": {"type": "number"},
                        "profit_flag": {"type": "string"},
                    },
                    "required": ["month_year", "revenue", "tax_reserve"],
                },
            },
        }


class CaV2CreateSchedulerRun(Tool):
    """Generate an entry for the scheduler run log."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None, task_name: str = None, scheduled_for: str = None, executed_at: str = None, status: str = None, log_path: str = None) -> str:
        if not all([task_name, status]):
            return _error("Required fields: task_name, status")

        scheduler_run = {
            "run_id": run_id or f"RUN{len(data.get("scheduler_runs", {})) + 1:03d}",
            "task_name": task_name,
            "scheduled_for": scheduled_for,
            "executed_at": executed_at,
            "status": status,
            "log_path": log_path,
        }

        data.setdefault("scheduler_runs", []).append(scheduler_run)

        return _ok(run_id=run_id, task_name=task_name, status=status)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateSchedulerRun",
                "description": "Create a scheduler run log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "task_name": {"type": "string"},
                        "scheduled_for": {"type": "string"},
                        "executed_at": {"type": "string"},
                        "status": {"type": "string"},
                        "log_path": {"type": "string"},
                    },
                    "required": ["task_name", "status"],
                },
            },
        }


class CaV2GenerateInvoiceNumber(Tool):
    """Create the next sequential invoice number for a specified year."""

    @staticmethod
    def invoke(data: dict[str, Any], year: str = None) -> str:
        if not year:
            return _error("year is required.")

        invoices = data.get("invoices", {}).values()
        year_invoices = [
            inv for inv in invoices.values() if inv.get("invoice_date", "").startswith(year)
        ]

        # Identify the maximum value for the year
        max_number = 0
        for invoice in year_invoices:
            invoice_number = invoice.get("invoice_number", "")
            if invoice_number.startswith(f"{year}-"):
                try:
                    number = int(invoice_number.split("-")[1])
                    max_number = max(max_number, number)
                except:
                    continue

        next_number = max_number + 1
        next_invoice_number = f"{year}-{next_number:03d}"

        return _ok(
            next_invoice_number=next_invoice_number,
            sequence_number=next_number,
            year=year,
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GenerateInvoiceNumber",
                "description": "Generate the next sequential invoice number for a given year.",
                "parameters": {
                    "type": "object",
                    "properties": {"year": {"type": "string"}},
                    "required": ["year"],
                },
            },
        }


class CaV2CalculateHoursWorkedInPeriod(Tool):
    """Compute the total hours worked on projects for a defined period."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        end_date: str = None,
        project_ids: list = None,
        start_date: str = None
    ) -> str:
        if project_ids is None:
            project_ids = []

        if not all([start_date, end_date]):
            return _error("start_date and end_date are required.")

        time_entries = data.get("time_entries", {}).values()

        # Narrow down by date and optionally by project IDs
        filtered_entries = []
        for entry in time_entries.values():
            entry_date = entry.get("entry_date", "")
            if start_date <= entry_date <= end_date:
                if not project_ids or entry.get("project_id") in project_ids:
                    filtered_entries.append(entry)

        # Compute overall totals
        total_hours = sum(entry.get("hours_worked", 0) for entry in filtered_entries.values()

        # Categorize by project
        hours_by_project = {}
        for entry in filtered_entries:
            project_id = entry.get("project_id")
            if project_id not in hours_by_project:
                hours_by_project[project_id] = 0
            hours_by_project[project_id] += entry.get("hours_worked", 0)

        return _ok(
            total_hours=total_hours,
            hours_by_project=hours_by_project,
            entry_count=len(filtered_entries),
            period_start=start_date,
            period_end=end_date,
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CalculateHoursWorkedInPeriod",
                "description": "Calculate total hours worked for a specific period, optionally filtered by project IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"},
                        "project_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["start_date", "end_date"],
                },
            },
        }


class CaV2ApproveTimeEntry(Tool):
    """Approve time entry for invoicing manually when synced_at is not set."""

    @staticmethod
    def invoke(data: dict[str, Any], entry_id: str = None, approved_by: str = None, approval_reason: str = None) -> str:
        if not all([entry_id, approved_by, approval_reason]):
            return _error("entry_id, approved_by, and approval_reason are required.")

        return _ok(
            entry_id=entry_id,
            approved_by=approved_by,
            approval_reason=approval_reason,
            approved_at="2024-12-16T15:00:00Z",
            status="approved_for_billing",
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2ApproveTimeEntry",
                "description": "Manually approve time entry for invoicing when synced_at is null.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entry_id": {"type": "string"},
                        "approved_by": {"type": "string"},
                        "approval_reason": {"type": "string"},
                    },
                    "required": ["entry_id", "approved_by", "approval_reason"],
                },
            },
        }


class CaV2CalculateBankTotal(Tool):
    """Compute the overall balance across all bank accounts."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        bank_accounts = data.get("bank_accounts", {}).values()

        total_balance = 0.0
        account_details = []

        # Compute only liquid assets (checking and savings accounts)
        liquid_account_types = ["checking", "savings"]

        for account in bank_accounts.values():
            account_type = account.get("account_type", "")
            balance = float(account.get("current_balance", 0.0))

            account_details.append(
                {
                    "account_id": account.get("account_id"),
                    "account_type": account_type,
                    "balance": balance,
                }
            )

            # Include only liquid accounts in total
            if account_type in liquid_account_types:
                total_balance += balance
        payload = {
            "status": "success",
            "total_balance": total_balance,
            "account_count": len(bank_accounts),
            "account_details": account_details,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CalculateBankTotal",
                "description": "Calculate total balance across all bank accounts.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        }


#LIST OF TOOLS
TOOLS = [
    #Entity Searches
    CaV2GetConsultantProfile(),
    CaV2FindPublisherByName(),
    CaV2FindProjectByIsbn(),
    CaV2GetProjectById(),
    CaV2GetProjectsByPublisher(),
    CaV2GetTimeEntriesForPeriod(),
    CaV2GetUnpaidInvoices(),
    CaV2GetInvoiceById(),
    CaV2GetInvoiceLinesForInvoice(),
    CaV2GetExpensesByCategory(),
    CaV2GetExpenseCategories(),
    CaV2GetPaymentBehaviorByPublisher(),
    CaV2GetBankAccounts(),
    CaV2GetPipelineOpportunities(),
    CaV2GetRecurringSchedules(),
    #Computation & Analysis
    CaV2CalculateInvoiceAging(),
    CaV2CalculateYtdRevenue(),
    CaV2CalculateProjectProfitability(),
    CaV2CalculateExpenseSummary(),
    #Invoice Handling
    CaV2CreateInvoice(),
    CaV2CreateInvoiceLine(),
    CaV2UpdateInvoicePayment(),
    CaV2CreateInvoiceAuditEntry(),
    #Expense Handling
    CaV2CreateExpense(),
    #Cash Flow & Prediction
    CaV2ForecastCashFlow(),
    #Dashboard & Analysis
    CaV2CreateDashboardSnapshot(),
    CaV2GetTaxRateByYear(),
    CaV2CreateProjectRevenue(),
    CaV2CreateMonthlyRevenue(),
    CaV2CreateSchedulerRun(),
    CaV2GenerateInvoiceNumber(),
    CaV2CalculateHoursWorkedInPeriod(),
    CaV2ApproveTimeEntry(),
    CaV2CalculateBankTotal(),
]