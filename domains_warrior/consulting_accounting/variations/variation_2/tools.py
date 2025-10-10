from domains.dto import Tool
import json
from typing import Dict, Any, List
from datetime import datetime, timedelta


# Helpers (pure functions)
def _error(msg: str) -> str:
    return json.dumps({"error": msg})

def _ok(**payload) -> str:
    out = {"status": "success"}
    out.update(payload)
    return json.dumps(out)

def _find_one(lst: List[Dict[str, Any]], key: str, value: Any) -> Dict[str, Any] | None:
    for x in lst or []:
        if x.get(key) == value:
            return x
    return None

def _find_all(lst: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    return [x for x in lst or [] if x.get(key) == value]

def _calculate_hst(subtotal: float, rate: float = 0.13) -> float:
    """Calculate HST (13% default for Ontario)"""
    return round(subtotal * rate, 2)

def _calculate_aging_days(invoice_date: str, current_date: str = "2024-12-10") -> int:
    """Calculate days between invoice date and current date"""
    try:
        invoice = datetime.fromisoformat(invoice_date.replace('Z', '+00:00') if 'T' in invoice_date else invoice_date + "T00:00:00+00:00")
        current = datetime.fromisoformat(current_date + "T00:00:00+00:00")
        return (current - invoice).days
    except:
        return 0


# ENTITY LOOKUPS

class CaV2GetConsultantProfile(Tool):
    """Retrieve consultant profile information."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        consultants = data.get("consultants", [])
        if not consultants:
            return _error("No consultant profile found.")
        return json.dumps(consultants[0])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_consultant_profile",
                "description": "Retrieve the consultant's profile information including contact details and GST number.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class CaV2FindPublisherByName(Tool):
    """Find publisher by name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("publisher_name")
        if not name:
            return _error("publisher_name is required.")
        publishers = data.get("publishers", [])
        publisher = _find_one(publishers, "name", name)
        return json.dumps(publisher) if publisher else _error(f"Publisher '{name}' not found.")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_find_publisher_by_name",
                "description": "Find a publisher by their name.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_name": {"type": "string"}},
                    "required": ["publisher_name"],
                },
            },
        }


class CaV2FindProjectByIsbn(Tool):
    """Find project by ISBN."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        isbn = kwargs.get("isbn")
        if not isbn:
            return _error("isbn is required.")
        projects = data.get("projects", [])
        project = _find_one(projects, "isbn", isbn)
        return json.dumps(project) if project else _error(f"Project with ISBN '{isbn}' not found.")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_find_project_by_isbn",
                "description": "Find a project by its ISBN code.",
                "parameters": {
                    "type": "object",
                    "properties": {"isbn": {"type": "string"}},
                    "required": ["isbn"],
                },
            },
        }


class CaV2GetProjectById(Tool):
    """Get project details by project ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")

        if not project_id:
            return _error("project_id is required.")

        projects = data.get("projects", [])
        project = _find_one(projects, "project_id", project_id)

        if not project:
            return _error(f"Project {project_id} not found.")

        return _ok(
            project_id=project.get("project_id"),
            isbn=project.get("isbn"),
            title=project.get("project_title"),
            publisher_id=project.get("publisher_id"),
            default_hourly_rate=project.get("default_hourly_rate"),
            override_hourly_rate=project.get("override_hourly_rate"),
            status=project.get("is_active")
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_project_by_id",
                "description": "Get project details by project ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"}
                    },
                    "required": ["project_id"],
                },
            },
        }


class CaV2GetProjectById(Tool):
    """Get project details by project ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")

        if not project_id:
            return _error("project_id is required.")

        projects = data.get("projects", [])
        project = _find_one(projects, "project_id", project_id)

        if not project:
            return _error(f"Project {project_id} not found.")

        return _ok(
            project_id=project.get("project_id"),
            isbn=project.get("isbn"),
            title=project.get("project_title"),
            publisher_id=project.get("publisher_id"),
            default_hourly_rate=project.get("default_hourly_rate"),
            override_hourly_rate=project.get("override_hourly_rate"),
            status=project.get("is_active")
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_project_by_id",
                "description": "Get project details by project ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"}
                    },
                    "required": ["project_id"],
                },
            },
        }


class CaV2GetProjectById(Tool):
    """Get project details by project ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")

        if not project_id:
            return _error("project_id is required.")

        projects = data.get("projects", [])
        project = _find_one(projects, "project_id", project_id)

        if not project:
            return _error(f"Project {project_id} not found.")

        return _ok(
            project_id=project.get("project_id"),
            isbn=project.get("isbn"),
            title=project.get("title"),
            publisher_id=project.get("publisher_id"),
            default_hourly_rate=project.get("default_hourly_rate"),
            override_hourly_rate=project.get("override_hourly_rate"),
            status=project.get("status")
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_project_by_id",
                "description": "Get project details by project ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"}
                    },
                    "required": ["project_id"],
                },
            },
        }


class CaV2GetProjectsByPublisher(Tool):
    """Get all projects for a specific publisher."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        publisher_id = kwargs.get("publisher_id")
        active_only = kwargs.get("active_only", True)
        if not publisher_id:
            return _error("publisher_id is required.")

        projects = data.get("projects", [])
        publisher_projects = _find_all(projects, "publisher_id", publisher_id)

        if active_only:
            publisher_projects = [p for p in publisher_projects if p.get("is_active", True)]

        return json.dumps(publisher_projects)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_projects_by_publisher",
                "description": "Get all projects for a specific publisher, optionally filtering to active projects only.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string"},
                        "active_only": {"type": "boolean", "default": True}
                    },
                    "required": ["publisher_id"],
                },
            },
        }


class CaV2GetTimeEntriesForPeriod(Tool):
    """Get time entries for a specific project and date range."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")

        if not all([project_id, start_date, end_date]):
            return _error("project_id, start_date, and end_date are required.")

        time_entries = data.get("time_entries", [])
        filtered_entries = []

        for entry in time_entries:
            if (entry.get("project_id") == project_id and
                start_date <= entry.get("entry_date", "") <= end_date):
                filtered_entries.append(entry)

        return json.dumps(filtered_entries)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_time_entries_for_period",
                "description": "Get time entries for a specific project within a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"}
                    },
                    "required": ["project_id", "start_date", "end_date"],
                },
            },
        }


class CaV2GetUnpaidInvoices(Tool):
    """Get all unpaid invoices."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoices = data.get("invoices", [])
        unpaid_invoices = [inv for inv in invoices if not inv.get("paid_at")]
        return json.dumps(unpaid_invoices)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_unpaid_invoices",
                "description": "Get all invoices that have not been paid yet.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class CaV2GetInvoiceById(Tool):
    """Get specific invoice by ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoice_id = kwargs.get("invoice_id")
        if not invoice_id:
            return _error("invoice_id is required.")

        invoices = data.get("invoices", [])
        invoice = _find_one(invoices, "invoice_id", invoice_id)
        return json.dumps(invoice) if invoice else _error(f"Invoice '{invoice_id}' not found.")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_invoice_by_id",
                "description": "Get a specific invoice by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"invoice_id": {"type": "string"}},
                    "required": ["invoice_id"],
                },
            },
        }


class CaV2GetInvoiceLinesForInvoice(Tool):
    """Get all invoice lines for a specific invoice."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoice_id = kwargs.get("invoice_id")
        if not invoice_id:
            return _error("invoice_id is required.")

        invoice_lines = data.get("invoice_lines", [])
        lines = _find_all(invoice_lines, "invoice_id", invoice_id)
        return json.dumps(lines)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_invoice_lines_for_invoice",
                "description": "Get all line items for a specific invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {"invoice_id": {"type": "string"}},
                    "required": ["invoice_id"],
                },
            },
        }


class CaV2GetExpensesByCategory(Tool):
    """Get expenses filtered by category and optional date range."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category_code = kwargs.get("category_code")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")

        if not category_code:
            return _error("category_code is required.")

        expenses = data.get("expenses", [])
        filtered_expenses = _find_all(expenses, "category_code", category_code)

        if start_date and end_date:
            filtered_expenses = [exp for exp in filtered_expenses
                               if start_date <= exp.get("expense_date", "") <= end_date]

        return json.dumps(filtered_expenses)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_expenses_by_category",
                "description": "Get expenses filtered by category code and optionally by date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category_code": {"type": "string"},
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"}
                    },
                    "required": ["category_code"],
                },
            },
        }


class CaV2GetExpenseCategories(Tool):
    """Get all expense categories with deductibility rules."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        expense_categories = data.get("expense_categories", [])
        return json.dumps(expense_categories)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_expense_categories",
                "description": "Get all expense categories with their deductibility percentages and rules.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class CaV2GetPaymentBehaviorByPublisher(Tool):
    """Get payment behavior data for a specific publisher."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        publisher_id = kwargs.get("publisher_id")
        if not publisher_id:
            return _error("publisher_id is required.")

        payment_behaviors = data.get("payment_behavior", [])
        behavior = _find_one(payment_behaviors, "publisher_id", publisher_id)
        return json.dumps(behavior) if behavior else _error(f"Payment behavior for publisher '{publisher_id}' not found.")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_payment_behavior_by_publisher",
                "description": "Get payment behavior patterns for a specific publisher.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_id": {"type": "string"}},
                    "required": ["publisher_id"],
                },
            },
        }


class CaV2GetBankAccounts(Tool):
    """Get all bank account information."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        bank_accounts = data.get("bank_accounts", [])
        return json.dumps(bank_accounts)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_bank_accounts",
                "description": "Get all business bank accounts with current balances.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class CaV2GetPipelineOpportunities(Tool):
    """Get pipeline opportunities, optionally filtered by stage or probability."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        stage = kwargs.get("stage")
        min_probability = kwargs.get("min_probability")

        opportunities = data.get("pipeline_opportunities", [])

        if stage:
            opportunities = [opp for opp in opportunities if opp.get("stage") == stage]

        if min_probability is not None:
            opportunities = [opp for opp in opportunities if opp.get("probability", 0) >= min_probability]

        return json.dumps(opportunities)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_pipeline_opportunities",
                "description": "Get pipeline opportunities, optionally filtered by stage or minimum probability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "stage": {"type": "string"},
                        "min_probability": {"type": "number", "minimum": 0, "maximum": 1}
                    },
                    "required": [],
                },
            },
        }


class CaV2GetRecurringSchedules(Tool):
    """Get recurring scheduled payments by type."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        schedule_type = kwargs.get("schedule_type")
        active_only = kwargs.get("active_only", True)

        schedules = data.get("recurring_schedules", [])

        if schedule_type:
            schedules = _find_all(schedules, "schedule_type", schedule_type)

        if active_only:
            schedules = [sch for sch in schedules if sch.get("is_active", True)]

        return json.dumps(schedules)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_recurring_schedules",
                "description": "Get recurring scheduled payments, optionally filtered by type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "schedule_type": {"type": "string"},
                        "active_only": {"type": "boolean", "default": True}
                    },
                    "required": [],
                },
            },
        }


# CALCULATION & ANALYSIS TOOLS

class CaV2CalculateInvoiceAging(Tool):
    """Calculate aging buckets for unpaid invoices."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        current_date = kwargs.get("current_date", "2024-12-10")

        invoices = data.get("invoices", [])
        unpaid_invoices = [inv for inv in invoices if not inv.get("paid_at")]

        aging_buckets = {
            "current": [],      # 0-30 days
            "31_60": [],        # 31-60 days
            "61_90": [],        # 61-90 days
            "over_90": []       # 90+ days
        }

        for invoice in unpaid_invoices:
            days_overdue = _calculate_aging_days(invoice.get("invoice_date", ""), current_date)

            aging_info = {
                "invoice_id": invoice.get("invoice_id"),
                "invoice_number": invoice.get("invoice_number"),
                "publisher_id": invoice.get("publisher_id"),
                "total_due": invoice.get("total_due"),
                "invoice_date": invoice.get("invoice_date"),
                "days_overdue": days_overdue
            }

            if days_overdue <= 30:
                aging_buckets["current"].append(aging_info)
            elif days_overdue <= 60:
                aging_buckets["31_60"].append(aging_info)
            elif days_overdue <= 90:
                aging_buckets["61_90"].append(aging_info)
            else:
                aging_buckets["over_90"].append(aging_info)

        return json.dumps(aging_buckets)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_calculate_invoice_aging",
                "description": "Calculate aging buckets for all unpaid invoices.",
                "parameters": {
                    "type": "object",
                    "properties": {"current_date": {"type": "string", "format": "date"}},
                    "required": [],
                },
            },
        }


class CaV2CalculateYtdRevenue(Tool):
    """Calculate year-to-date revenue and tax reserve."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        year = kwargs.get("year", "2024")
        tax_rate = kwargs.get("tax_rate", 0.265)  # 26.5% default

        invoices = data.get("invoices", [])
        ytd_invoices = [inv for inv in invoices
                       if inv.get("invoice_date", "").startswith(year)]

        total_revenue = sum(inv.get("subtotal", 0) for inv in ytd_invoices)
        tax_reserve = round(total_revenue * tax_rate, 2)

        revenue_by_month = {}
        for invoice in ytd_invoices:
            month = invoice.get("invoice_date", "")[:7]  # YYYY-MM
            if month not in revenue_by_month:
                revenue_by_month[month] = 0
            revenue_by_month[month] += invoice.get("subtotal", 0)

        return _ok(
            year=year,
            ytd_revenue=total_revenue,
            ytd_tax_reserve=tax_reserve,
            revenue_by_month=revenue_by_month,
            invoice_count=len(ytd_invoices)
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_calculate_ytd_revenue",
                "description": "Calculate year-to-date revenue, tax reserve, and monthly breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "year": {"type": "string"},
                        "tax_rate": {"type": "number", "default": 0.265}
                    },
                    "required": [],
                },
            },
        }


class CaV2CalculateProjectProfitability(Tool):
    """Calculate profitability metrics for projects."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")

        if not project_id:
            return _error("project_id is required.")

        # Get project details
        projects = data.get("projects", [])
        project = _find_one(projects, "project_id", project_id)
        if not project:
            return _error(f"Project '{project_id}' not found.")

        # Calculate revenue from invoices
        invoice_lines = data.get("invoice_lines", [])
        project_lines = _find_all(invoice_lines, "project_id", project_id)
        total_revenue = sum(line.get("line_amount", 0) for line in project_lines)
        total_hours = sum(line.get("hours_billed", 0) for line in project_lines)

        # Calculate effective hourly rate
        effective_rate = total_revenue / total_hours if total_hours > 0 else 0
        expected_rate = project.get("override_hourly_rate") or project.get("default_hourly_rate", 0)

        return _ok(
            project_id=project_id,
            project_title=project.get("project_title"),
            total_revenue=total_revenue,
            total_hours_billed=total_hours,
            effective_hourly_rate=round(effective_rate, 2),
            expected_hourly_rate=expected_rate,
            rate_variance=round(effective_rate - expected_rate, 2),
            is_active=project.get("is_active")
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_calculate_project_profitability",
                "description": "Calculate profitability metrics for a specific project.",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }


class CaV2CalculateExpenseSummary(Tool):
    """Calculate expense summary by category for a given period."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        year = kwargs.get("year", "2024")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")
        category_filter = kwargs.get("category_filter", [])

        expenses = data.get("expenses", [])
        expense_categories = data.get("expense_categories", [])

        # Filter expenses by date range
        if start_date and end_date:
            filtered_expenses = [exp for exp in expenses
                               if start_date <= exp.get("expense_date", "") <= end_date]
        else:
            # Filter expenses by year
            filtered_expenses = [exp for exp in expenses
                               if exp.get("expense_date", "").startswith(year)]

        # Filter by categories if specified
        if category_filter:
            filtered_expenses = [exp for exp in filtered_expenses
                               if exp.get("category_code") in category_filter]

        # Group by category
        category_summary = {}
        for expense in filtered_expenses:
            category_code = expense.get("category_code")
            if category_code not in category_summary:
                category_summary[category_code] = {
                    "total_gross": 0,
                    "total_deductible": 0,
                    "count": 0
                }

            gross_amount = expense.get("gross_amount", 0)
            allowed_amount = expense.get("allowed_amount", 0)

            category_summary[category_code]["total_gross"] += gross_amount
            category_summary[category_code]["total_deductible"] += allowed_amount
            category_summary[category_code]["count"] += 1

        # Add category names and ensure deductible doesn't exceed gross
        for category_code, summary in category_summary.items():
            category_info = _find_one(expense_categories, "category_code", category_code)
            summary["category_name"] = category_info.get("name", "Unknown") if category_info else "Unknown"
            summary["deductible_percent"] = category_info.get("deductible_percent", 0) if category_info else 0

            # Ensure deductible never exceeds gross amount
            if summary["total_deductible"] > summary["total_gross"]:
                summary["total_deductible"] = summary["total_gross"]

        total_deductible = sum(summary["total_deductible"] for summary in category_summary.values())

        return _ok(
            year=year,
            category_summary=category_summary,
            total_deductible_expenses=round(total_deductible, 2),
            total_expense_count=len(filtered_expenses)
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_calculate_expense_summary",
                "description": "Calculate expense summary by category for a given year.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "year": {"type": "string"},
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"},
                        "category_filter": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": [],
                },
            },
        }


# INVOICE MANAGEMENT TOOLS

class CaV2CreateInvoice(Tool):
    """Create a new invoice."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Required parameters
        invoice_id = kwargs.get("invoice_id")
        invoice_number = kwargs.get("invoice_number")
        publisher_id = kwargs.get("publisher_id")
        invoice_date = kwargs.get("invoice_date")
        period_start = kwargs.get("period_start")
        period_end = kwargs.get("period_end")
        subtotal = kwargs.get("subtotal")

        if not all([invoice_number, publisher_id, invoice_date,
                   period_start, period_end, subtotal]):
            return _error("Required fields: invoice_number, publisher_id, invoice_date, period_start, period_end, subtotal")

        # Calculate HST and total
        hst_amount = _calculate_hst(subtotal)
        total_due = round(subtotal + hst_amount, 2)

        # Create invoice record
        new_invoice = {
            "invoice_id": invoice_id or f"INV{len(data.get('invoices', [])) + 1:03d}",
            "invoice_number": invoice_number,
            "publisher_id": publisher_id,
            "invoice_date": invoice_date,
            "period_start": period_start,
            "period_end": period_end,
            "subtotal": subtotal,
            "hst_amount": hst_amount,
            "total_due": total_due,
            "pdf_path": f"/invoices/{invoice_date[:4]}/{invoice_number}.pdf",
            "sent_at": kwargs.get("sent_at"),
            "paid_at": kwargs.get("paid_at"),
            "created_at": kwargs.get("created_at", invoice_date + "T00:00:00Z")
        }

        # Add to data
        data.setdefault("invoices", []).append(new_invoice)

        return _ok(
            invoice_id=invoice_id,
            invoice_number=invoice_number,
            total_due=total_due,
            hst_amount=hst_amount
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_invoice",
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
                        "created_at": {"type": "string"}
                    },
                    "required": ["invoice_number", "publisher_id", "invoice_date", "period_start", "period_end", "subtotal"],
                },
            },
        }


class CaV2CreateInvoiceLine(Tool):
    """Create an invoice line item."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Required parameters
        invoice_line_id = kwargs.get("invoice_line_id")
        invoice_id = kwargs.get("invoice_id")
        project_id = kwargs.get("project_id")
        isbn = kwargs.get("isbn")
        hours_billed = kwargs.get("hours_billed")
        hourly_rate = kwargs.get("hourly_rate")

        if not all([invoice_line_id, invoice_id, project_id, isbn, hours_billed, hourly_rate]):
            return _error("All line item fields are required: invoice_line_id, invoice_id, project_id, isbn, hours_billed, hourly_rate")

        line_amount = round(hours_billed * hourly_rate, 2)

        new_line = {
            "invoice_line_id": invoice_line_id,
            "invoice_id": invoice_id,
            "project_id": project_id,
            "isbn": isbn,
            "hours_billed": hours_billed,
            "hourly_rate": hourly_rate,
            "line_amount": line_amount
        }

        # Add to data
        data.setdefault("invoice_lines", []).append(new_line)

        return _ok(
            invoice_line_id=invoice_line_id,
            line_amount=line_amount
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_invoice_line",
                "description": "Create an invoice line item with automatic amount calculation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_line_id": {"type": "string"},
                        "invoice_id": {"type": "string"},
                        "project_id": {"type": "string"},
                        "isbn": {"type": "string"},
                        "hours_billed": {"type": "number"},
                        "hourly_rate": {"type": "number"}
                    },
                    "required": ["invoice_line_id", "invoice_id", "project_id", "isbn", "hours_billed", "hourly_rate"],
                },
            },
        }


class CaV2UpdateInvoicePayment(Tool):
    """Update invoice payment status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoice_id = kwargs.get("invoice_id")
        paid_at = kwargs.get("paid_at")

        if not invoice_id:
            return _error("invoice_id is required.")

        invoices = data.get("invoices", [])
        invoice = _find_one(invoices, "invoice_id", invoice_id)

        if not invoice:
            return _error(f"Invoice '{invoice_id}' not found.")

        invoice["paid_at"] = paid_at

        return _ok(
            invoice_id=invoice_id,
            paid_at=paid_at,
            status="payment_updated"
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_update_invoice_payment",
                "description": "Update the payment status of an invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "paid_at": {"type": "string"}
                    },
                    "required": ["invoice_id"],
                },
            },
        }


class CaV2CreateInvoiceAuditEntry(Tool):
    """Create an audit trail entry for invoice actions."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        audit_id = kwargs.get("audit_id")
        invoice_id = kwargs.get("invoice_id")
        event_type = kwargs.get("event_type")
        event_timestamp = kwargs.get("event_timestamp")
        notes = kwargs.get("notes", "")

        if not all([audit_id, invoice_id, event_type, event_timestamp]):
            return _error("audit_id, invoice_id, event_type, and event_timestamp are required.")

        audit_entry = {
            "audit_id": audit_id,
            "invoice_id": invoice_id,
            "event_type": event_type,
            "event_timestamp": event_timestamp,
            "notes": notes
        }

        data.setdefault("invoice_audit", []).append(audit_entry)

        return _ok(audit_id=audit_id, event_type=event_type)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_invoice_audit_entry",
                "description": "Create an audit trail entry for invoice actions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "invoice_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "event_timestamp": {"type": "string"},
                        "notes": {"type": "string"}
                    },
                    "required": ["audit_id", "invoice_id", "event_type", "event_timestamp"],
                },
            },
        }


# EXPENSE MANAGEMENT TOOLS

class CaV2CreateExpense(Tool):
    """Create a new expense record."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        expense_id = kwargs.get("expense_id")
        vendor = kwargs.get("vendor")
        expense_date = kwargs.get("expense_date")
        gross_amount = kwargs.get("gross_amount")
        currency = kwargs.get("currency", "CAD")
        description = kwargs.get("description")
        payment_method = kwargs.get("payment_method")
        category_code = kwargs.get("category_code")

        if not all([expense_id, vendor, expense_date, gross_amount, description, category_code]):
            return _error("Required fields: expense_id, vendor, expense_date, gross_amount, description, category_code")

        # Get category to calculate allowed amount
        expense_categories = data.get("expense_categories", [])
        category = _find_one(expense_categories, "category_code", category_code)

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
            "receipt_path": kwargs.get("receipt_path", f"/receipts/{expense_date[:4]}/{expense_id}_receipt.pdf"),
            "created_at": kwargs.get("created_at", expense_date + "T00:00:00Z")
        }

        data.setdefault("expenses", []).append(new_expense)

        return _ok(
            expense_id=expense_id,
            allowed_amount=allowed_amount,
            deductible_percent=category.get("deductible_percent")
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_expense",
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
                        "created_at": {"type": "string"}
                    },
                    "required": ["expense_id", "vendor", "expense_date", "gross_amount", "description", "category_code"],
                },
            },
        }


# CASH FLOW & FORECASTING TOOLS

class CaV2ForecastCashFlow(Tool):
    """Forecast cash flow based on unpaid invoices and payment behavior."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        forecast_months = kwargs.get("forecast_months", 3)
        current_date = kwargs.get("current_date", "2024-12-10")

        # Get unpaid invoices
        invoices = data.get("invoices", [])
        unpaid_invoices = [inv for inv in invoices if not inv.get("paid_at")]

        # Get payment behaviors
        payment_behaviors = data.get("payment_behavior", [])

        # Forecast collections
        forecasted_collections = []
        for invoice in unpaid_invoices:
            publisher_id = invoice.get("publisher_id")
            behavior = _find_one(payment_behaviors, "publisher_id", publisher_id)

            avg_days = behavior.get("avg_days_to_pay", 30) if behavior else 30
            invoice_date = datetime.fromisoformat(invoice.get("invoice_date") + "T00:00:00")
            expected_payment = invoice_date + timedelta(days=avg_days)

            forecasted_collections.append({
                "invoice_id": invoice.get("invoice_id"),
                "invoice_number": invoice.get("invoice_number"),
                "amount": invoice.get("total_due"),
                "expected_payment_date": expected_payment.strftime("%Y-%m-%d"),
                "confidence": behavior.get("payment_consistency", "moderate") if behavior else "moderate"
            })

        # Get recurring expenses
        recurring_schedules = data.get("recurring_schedules", [])
        active_schedules = [sch for sch in recurring_schedules if sch.get("is_active")]

        # Summarize by month
        monthly_summary = {}
        for i in range(forecast_months):
            month_start = datetime.fromisoformat(current_date + "T00:00:00") + timedelta(days=30*i)
            month_key = month_start.strftime("%Y-%m")
            monthly_summary[month_key] = {
                "expected_collections": 0,
                "scheduled_expenses": 0,
                "net_flow": 0
            }

        # Add collections to summary
        for collection in forecasted_collections:
            payment_month = collection["expected_payment_date"][:7]
            if payment_month in monthly_summary:
                monthly_summary[payment_month]["expected_collections"] += collection["amount"]

        # Add expenses to summary
        for schedule in active_schedules:
            monthly_amount = schedule.get("amount", 0)
            for month_key in monthly_summary.keys():
                if schedule.get("frequency") == "monthly":
                    monthly_summary[month_key]["scheduled_expenses"] += monthly_amount

        # Calculate net flow
        for month_data in monthly_summary.values():
            month_data["net_flow"] = month_data["expected_collections"] - month_data["scheduled_expenses"]

        return _ok(
            forecast_period_months=forecast_months,
            forecasted_collections=forecasted_collections,
            monthly_summary=monthly_summary,
            total_expected_collections=sum(c["amount"] for c in forecasted_collections)
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_forecast_cash_flow",
                "description": "Forecast cash flow based on unpaid invoices, payment behavior, and recurring expenses.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "forecast_months": {"type": "integer", "default": 3},
                        "current_date": {"type": "string", "format": "date"}
                    },
                    "required": [],
                },
            },
        }


# DASHBOARD & REPORTING TOOLS

class CaV2CreateDashboardSnapshot(Tool):
    """Create a dashboard snapshot with current financial metrics."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        snapshot_id = kwargs.get("snapshot_id")
        snapshot_date = kwargs.get("snapshot_date")
        ytd_revenue = kwargs.get("ytd_revenue")
        ytd_tax_reserve = kwargs.get("ytd_tax_reserve")
        pdf_path = kwargs.get("pdf_path")

        if not snapshot_date:
            return _error("snapshot_date is required")

        snapshot = {
            "snapshot_id": snapshot_id or f"SNAP{len(data.get('dashboard_snapshots', [])) + 1:03d}",
            "snapshot_date": snapshot_date,
            "ytd_revenue": ytd_revenue or 0.0,
            "ytd_tax_reserve": ytd_tax_reserve or 0.0,
            "pdf_path": pdf_path or f"/dashboards/{snapshot_date[:4]}/dashboard_{snapshot_date}.pdf"
        }

        data.setdefault("dashboard_snapshots", []).append(snapshot)

        return _ok(
            snapshot_id=snapshot_id,
            snapshot_date=snapshot_date
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_dashboard_snapshot",
                "description": "Create a financial dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "snapshot_date": {"type": "string", "format": "date"},
                        "ytd_revenue": {"type": "number"},
                        "ytd_tax_reserve": {"type": "number"},
                        "pdf_path": {"type": "string"}
                    },
                    "required": ["snapshot_date"],
                },
            },
        }


class CaV2GetTaxRateByYear(Tool):
    """Get tax rate for a specific year."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        year = kwargs.get("year")
        if not year:
            return _error("year is required.")

        tax_rates = data.get("tax_rates", [])
        tax_rate = _find_one(tax_rates, "tax_year", int(year))
        return json.dumps(tax_rate) if tax_rate else _error(f"Tax rate for year {year} not found.")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_tax_rate_by_year",
                "description": "Get the tax rate for a specific year.",
                "parameters": {
                    "type": "object",
                    "properties": {"year": {"type": "string"}},
                    "required": ["year"],
                },
            },
        }


class CaV2CreateProjectRevenue(Tool):
    """Create project revenue record for dashboard snapshot."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        row_id = kwargs.get("row_id")
        snapshot_id = kwargs.get("snapshot_id")
        project_id = kwargs.get("project_id")
        ytd_revenue = kwargs.get("ytd_revenue")

        if not all([row_id, snapshot_id, project_id, ytd_revenue]):
            return _error("Required fields: row_id, snapshot_id, project_id, ytd_revenue")

        project_revenue = {
            "row_id": row_id,
            "snapshot_id": snapshot_id,
            "project_id": project_id,
            "ytd_revenue": ytd_revenue
        }

        data.setdefault("project_revenue", []).append(project_revenue)

        return _ok(row_id=row_id, project_id=project_id, ytd_revenue=ytd_revenue)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_project_revenue",
                "description": "Create a project revenue record for a dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_id": {"type": "string"},
                        "snapshot_id": {"type": "string"},
                        "project_id": {"type": "string"},
                        "ytd_revenue": {"type": "number"}
                    },
                    "required": ["row_id", "snapshot_id", "project_id", "ytd_revenue"],
                },
            },
        }


class CaV2CreateMonthlyRevenue(Tool):
    """Create monthly revenue record for dashboard snapshot."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        row_id = kwargs.get("row_id")
        snapshot_id = kwargs.get("snapshot_id")
        month_year = kwargs.get("month_year")
        revenue = kwargs.get("revenue")
        tax_reserve = kwargs.get("tax_reserve")
        profit_flag = kwargs.get("profit_flag", "normal")

        if not all([month_year, revenue, tax_reserve]):
            return _error("Required fields: month_year, revenue, tax_reserve")

        monthly_revenue = {
            "row_id": row_id or f"REV{len(data.get('monthly_revenue', [])) + 1:03d}",
            "snapshot_id": snapshot_id or f"SNAP{len(data.get('dashboard_snapshots', [])) + 1:03d}",
            "month_year": month_year,
            "revenue": revenue,
            "tax_reserve": tax_reserve,
            "profit_flag": profit_flag
        }

        data.setdefault("monthly_revenue", []).append(monthly_revenue)

        return _ok(row_id=monthly_revenue["row_id"], month_year=month_year, revenue=revenue)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_monthly_revenue",
                "description": "Create a monthly revenue record for a dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_id": {"type": "string"},
                        "snapshot_id": {"type": "string"},
                        "month_year": {"type": "string"},
                        "revenue": {"type": "number"},
                        "tax_reserve": {"type": "number"},
                        "profit_flag": {"type": "string"}
                    },
                    "required": ["month_year", "revenue", "tax_reserve"],
                },
            },
        }


class CaV2CreateSchedulerRun(Tool):
    """Create a scheduler run log entry."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("run_id")
        task_name = kwargs.get("task_name")
        scheduled_for = kwargs.get("scheduled_for")
        executed_at = kwargs.get("executed_at")
        status = kwargs.get("status")
        log_path = kwargs.get("log_path")

        if not all([task_name, status]):
            return _error("Required fields: task_name, status")

        scheduler_run = {
            "run_id": run_id or f"RUN{len(data.get('scheduler_runs', [])) + 1:03d}",
            "task_name": task_name,
            "scheduled_for": scheduled_for,
            "executed_at": executed_at,
            "status": status,
            "log_path": log_path
        }

        data.setdefault("scheduler_runs", []).append(scheduler_run)

        return _ok(run_id=run_id, task_name=task_name, status=status)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_scheduler_run",
                "description": "Create a scheduler run log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "task_name": {"type": "string"},
                        "scheduled_for": {"type": "string"},
                        "executed_at": {"type": "string"},
                        "status": {"type": "string"},
                        "log_path": {"type": "string"}
                    },
                    "required": ["task_name", "status"],
                },
            },
        }


class CaV2GenerateInvoiceNumber(Tool):
    """Generate next sequential invoice number for a given year."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        year = kwargs.get("year")
        if not year:
            return _error("year is required.")

        invoices = data.get("invoices", [])
        year_invoices = [inv for inv in invoices if inv.get("invoice_date", "").startswith(year)]

        # Find highest number for the year
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
            year=year
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_generate_invoice_number",
                "description": "Generate the next sequential invoice number for a given year.",
                "parameters": {
                    "type": "object",
                    "properties": {"year": {"type": "string"}},
                    "required": ["year"],
                },
            },
        }


class CaV2CalculateHoursWorkedInPeriod(Tool):
    """Calculate total hours worked across projects for a specific period."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")
        project_ids = kwargs.get("project_ids", [])

        if not all([start_date, end_date]):
            return _error("start_date and end_date are required.")

        time_entries = data.get("time_entries", [])

        # Filter by date and optionally by project_ids
        filtered_entries = []
        for entry in time_entries:
            entry_date = entry.get("entry_date", "")
            if start_date <= entry_date <= end_date:
                if not project_ids or entry.get("project_id") in project_ids:
                    filtered_entries.append(entry)

        # Calculate totals
        total_hours = sum(entry.get("hours_worked", 0) for entry in filtered_entries)

        # Group by project
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
            period_end=end_date
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_calculate_hours_worked_in_period",
                "description": "Calculate total hours worked for a specific period, optionally filtered by project IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"},
                        "project_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["start_date", "end_date"],
                },
            },
        }


class CaV2ApproveTimeEntry(Tool):
    """Manually approve time entry for invoicing when synced_at is null."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        entry_id = kwargs.get("entry_id")
        approved_by = kwargs.get("approved_by")
        approval_reason = kwargs.get("approval_reason")

        if not all([entry_id, approved_by, approval_reason]):
            return _error("entry_id, approved_by, and approval_reason are required.")

        return _ok(
            entry_id=entry_id,
            approved_by=approved_by,
            approval_reason=approval_reason,
            approved_at="2024-12-16T15:00:00Z",
            status="approved_for_billing"
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_approve_time_entry",
                "description": "Manually approve time entry for invoicing when synced_at is null.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entry_id": {"type": "string"},
                        "approved_by": {"type": "string"},
                        "approval_reason": {"type": "string"}
                    },
                    "required": ["entry_id", "approved_by", "approval_reason"],
                },
            },
        }

class CaV2CalculateBankTotal(Tool):
    """Calculate total balance across all bank accounts."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        bank_accounts = data.get("bank_accounts", [])

        total_balance = 0.0
        account_details = []

        # Calculate liquid assets only (checking and savings accounts)
        liquid_account_types = ["checking", "savings"]

        for account in bank_accounts:
            account_type = account.get("account_type", "")
            balance = float(account.get("current_balance", 0.0))

            account_details.append({
                "account_id": account.get("account_id"),
                "account_type": account_type,
                "balance": balance
            })

            # Only add liquid accounts to total
            if account_type in liquid_account_types:
                total_balance += balance

        return json.dumps({
            "status": "success",
            "total_balance": total_balance,
            "account_count": len(bank_accounts),
            "account_details": account_details
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_calculate_bank_total",
                "description": "Calculate total balance across all bank accounts.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        }

# TOOLS LIST
TOOLS = [
    # Entity Lookups
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

    # Calculation & Analysis
    CaV2CalculateInvoiceAging(),
    CaV2CalculateYtdRevenue(),
    CaV2CalculateProjectProfitability(),
    CaV2CalculateExpenseSummary(),

    # Invoice Management
    CaV2CreateInvoice(),
    CaV2CreateInvoiceLine(),
    CaV2UpdateInvoicePayment(),
    CaV2CreateInvoiceAuditEntry(),

    # Expense Management
    CaV2CreateExpense(),

    # Cash Flow & Forecasting
    CaV2ForecastCashFlow(),

    # Dashboard & Reporting
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
