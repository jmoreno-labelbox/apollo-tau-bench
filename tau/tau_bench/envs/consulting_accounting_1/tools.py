import json
from typing import Dict, Any, List
from domains.dto import Tool

class GetInvoiceDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoice_id = kwargs.get("invoice_id")
        if not invoice_id:
            return json.dumps({"error": "invoice_id is required"}, indent=2)
        invoices = data.get("invoices", [])
        inv = next((i for i in invoices if i.get("invoice_id") == invoice_id), None)
        return json.dumps(inv or {"error": f"Invoice {invoice_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "get_invoice_details","description": "Retrieve all data for a specific invoice.","parameters": {"type": "object","properties": {"invoice_id": {"type": "string","description": "The ID of the invoice."}},"required": ["invoice_id"]}}}

class ComputeInvoiceAging(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        import datetime as _dt
        invoice_id = kwargs.get("invoice_id")
        today_str = kwargs.get("today")
        if not invoice_id or not today_str:
            return json.dumps({"error": "invoice_id and today are required"}, indent=2)
        invoices = data.get("invoices", [])
        inv = next((i for i in invoices if i.get("invoice_id") == invoice_id), None)
        if not inv:
            return json.dumps({"error": f"Invoice {invoice_id} not found"}, indent=2)
        if inv.get("paid_at"):
            return json.dumps({"invoice_id": invoice_id,"status": "paid","days_overdue": 0,"bucket": "current"}, indent=2)
        inv_date = _dt.datetime.fromisoformat(inv["invoice_date"])
        today = _dt.datetime.fromisoformat(today_str)
        days = (today - inv_date).days
        bucket = "0-30" if days <= 30 else "31-60" if days <= 60 else "61-90" if days <= 90 else "90+"
        return json.dumps({"invoice_id": invoice_id,"status": "unpaid","days_overdue": days,"bucket": bucket}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "compute_invoice_aging","description": "Compute days overdue and aging bucket for a given invoice.","parameters": {"type": "object","properties": {"invoice_id": {"type": "string"},"today": {"type": "string","description": "YYYY-MM-DD reference date"}},"required": ["invoice_id","today"]}}}

class CreateAuditEntry(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        import datetime as _dt
        inv_id = kwargs.get("invoice_id")
        event_type = kwargs.get("event_type")
        notes = kwargs.get("notes", "")
        if not inv_id or not event_type:
            return json.dumps({"error": "invoice_id and event_type are required"}, indent=2)
        audit = data.setdefault("invoice_audit", [])
        new_id = f"AUTO-AUD-{len(audit)+1:04d}"
        ts = _dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
        record = {"audit_id": new_id,"invoice_id": inv_id,"event_type": event_type,"event_timestamp": ts,"notes": notes}
        audit.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "create_audit_entry","description": "Create an audit event for an invoice (reminder, second_notice, escalation, etc).","parameters": {"type": "object","properties": {"invoice_id": {"type": "string"},"event_type": {"type": "string"},"notes": {"type": "string"}},"required": ["invoice_id","event_type"]}}}

class GetDashboardSnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sid = kwargs.get("snapshot_id")
        snaps = data.get("dashboard_snapshots", [])
        snap = next((s for s in snaps if s.get("snapshot_id") == sid), None)
        return json.dumps(snap or {"error": f"Snapshot {sid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "get_dashboard_snapshot","description": "Get a dashboard snapshot by snapshot_id.","parameters": {"type": "object","properties": {"snapshot_id": {"type": "string"}},"required": ["snapshot_id"]}}}

class ComputeTaxReserve(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        year = kwargs.get("tax_year")
        revenue = kwargs.get("ytd_revenue")
        if year is None or revenue is None:
            return json.dumps({"error": "tax_year and ytd_revenue are required"}, indent=2)
        rate = next((t["rate_percent"] for t in data.get("tax_rates", []) if t.get("tax_year") == year), None)
        if rate is None:
            return json.dumps({"error": f"No tax rate for {year}"}, indent=2)
        reserve = round(float(revenue) * (float(rate) / 100.0), 2)
        return json.dumps({"ytd_revenue": revenue,"tax_year": year,"tax_rate": rate,"tax_reserve": reserve}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "compute_tax_reserve","description": "Compute tax reserve given YTD revenue and tax year.","parameters": {"type": "object","properties": {"ytd_revenue": {"type": "number"},"tax_year": {"type": "integer"}},"required": ["ytd_revenue","tax_year"]}}}

class CreateDashboardSnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["snapshot_date","ytd_revenue","ytd_tax_reserve","pdf_path"]
        for k in required:
            if kwargs.get(k) is None:
                return json.dumps({"error": f"{k} is required"}, indent=2)
        snaps = data.setdefault("dashboard_snapshots", [])
        new_id = f"SNAP-AUTO-{len(snaps)+1:03d}"
        record = {"snapshot_id": new_id,"snapshot_date": kwargs["snapshot_date"],"ytd_revenue": kwargs["ytd_revenue"],"ytd_tax_reserve": kwargs["ytd_tax_reserve"],"pdf_path": kwargs["pdf_path"]}
        snaps.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "create_dashboard_snapshot","description": "Append a new dashboard snapshot with artifact path.","parameters": {"type": "object","properties": {"snapshot_date": {"type": "string"},"ytd_revenue": {"type": "number"},"ytd_tax_reserve": {"type": "number"},"pdf_path": {"type": "string"}},"required": ["snapshot_date","ytd_revenue","ytd_tax_reserve","pdf_path"]}}}

class GetExpenseDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        expense_id = kwargs.get("expense_id")
        if not expense_id:
            return json.dumps({"error": "expense_id is required"}, indent=2)
        expenses = data.get("expenses", [])
        exp = next((e for e in expenses if e.get("expense_id") == expense_id), None)
        return json.dumps(exp or {"error": f"Expense {expense_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "get_expense_details","description": "Retrieve all data for a specific expense.","parameters": {"type": "object","properties": {"expense_id": {"type": "string"}},"required": ["expense_id"]}}}

class ApplyDeductibilityRules(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        expense_id = kwargs.get("expense_id")
        if not expense_id:
            return json.dumps({"error": "expense_id is required"}, indent=2)
        exp = next((e for e in data.get("expenses", []) if e.get("expense_id") == expense_id), None)
        if not exp:
            return json.dumps({"error": f"Expense {expense_id} not found"}, indent=2)
        cat = exp.get("category_code")
        cat_obj = next((c for c in data.get("expense_categories", []) if c.get("category_code") == cat), None)
        if not cat_obj:
            return json.dumps({"error": f"Category {cat} not found"}, indent=2)
        pct = float(cat_obj.get("deductible_percent", 100)) / 100.0
        allowed = round(float(exp.get("gross_amount", 0.0)) * pct, 2)
        result = {"expense_id": expense_id,"category_code": cat,"deductible_percent": pct * 100,"allowed_amount": allowed}
        exp["allowed_amount"] = allowed
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "apply_deductibility_rules","description": "Apply expense category deductibility to compute allowed_amount.","parameters": {"type": "object","properties": {"expense_id": {"type": "string"}},"required": ["expense_id"]}}}

class GenerateExpenseDashboard(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        quarter = kwargs.get("quarter")
        included = kwargs.get("included_expenses", [])
        if not quarter or not isinstance(included, list):
            return json.dumps({"error": "quarter and included_expenses list are required"}, indent=2)
        path = f"/dashboards/ExpenseDashboards/{quarter}/expense_dashboard_{quarter}.pdf"
        return json.dumps({"quarter": quarter,"included_expenses": included,"pdf_path": path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "generate_expense_dashboard","description": "Generate an expense dashboard artifact for a given quarter.","parameters": {"type": "object","properties": {"quarter": {"type": "string"},"included_expenses": {"type": "array","items": {"type": "string"}}},"required": ["quarter","included_expenses"]}}}

class GetBankBalances(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        accts = data.get("bank_accounts", [])
        total = 0.0
        details: List[Dict[str, Any]] = []
        for a in accts:
            bal = float(a.get("current_balance", 0.0))
            total += bal
            details.append({"account_id": a.get("account_id"),"balance": bal,"currency": a.get("currency")})
        return json.dumps({"total_balance": round(total, 2),"accounts": details}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "get_bank_balances","description": "Return total and per-account current balances.","parameters": {"type": "object","properties": {}}}}

class ListRecurringSchedules(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        horizon = int(kwargs.get("horizon_months", 3))
        schedules = [s for s in data.get("recurring_schedules", []) if s.get("is_active", False)]
        return json.dumps({"horizon_months": horizon,"active_schedules": schedules}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "list_recurring_schedules","description": "List active recurring schedules considered for the forecast horizon.","parameters": {"type": "object","properties": {"horizon_months": {"type": "integer"}}}}}

class ComputePaymentBehavior(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pub_id = kwargs.get("publisher_id")
        if not pub_id:
            return json.dumps({"error": "publisher_id is required"}, indent=2)
        pb = next((p for p in data.get("payment_behavior", []) if p.get("publisher_id") == pub_id), None)
        return json.dumps(pb or {"error": f"payment_behavior for {pub_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "compute_payment_behavior","description": "Return stored payment behavior stats for a publisher.","parameters": {"type": "object","properties": {"publisher_id": {"type": "string"}},"required": ["publisher_id"]}}}

class ForecastInflows(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoices_ids = kwargs.get("invoices", [])
        prob_rule = kwargs.get("probability_rule", "overdue_60=0.3")
        discount = 0.3
        try:
            if "overdue_60=" in prob_rule:
                discount = float(prob_rule.split("overdue_60=")[1])
        except Exception:
            discount = 0.3
        import datetime as _dt
        today = _dt.datetime.fromisoformat("2024-11-30")
        invoices = data.get("invoices", [])
        total_expected = 0.0
        breakdown = []
        for inv_id in invoices_ids:
            inv = next((i for i in invoices if i.get("invoice_id") == inv_id), None)
            if not inv or inv.get("paid_at"):
                continue
            inv_date = _dt.datetime.fromisoformat(inv["invoice_date"])
            days = (today - inv_date).days
            amt = float(inv.get("total_due", 0.0))
            prob = discount if days > 60 else 1.0
            expected = round(amt * prob, 2)
            total_expected += expected
            breakdown.append({"invoice_id": inv_id,"days_overdue": days,"amount": amt,"probability": prob,"expected": expected})
        return json.dumps({"total_expected_inflows": round(total_expected, 2),"breakdown": breakdown}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "forecast_inflows","description": "Forecast expected inflows from invoices (discount >60d overdue).","parameters": {"type": "object","properties": {"invoices": {"type": "array","items": {"type": "string"}},"probability_rule": {"type": "string"}},"required": ["invoices"]}}}

class ForecastOutflows(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        include_sched = bool(kwargs.get("recurring_schedules", True))
        include_taxes = bool(kwargs.get("taxes", True))
        horizon_months = int(kwargs.get("horizon_months", 3))
        total = 0.0
        lines: List[Dict[str, Any]] = []
        if include_sched:
            for s in data.get("recurring_schedules", []):
                if not s.get("is_active", False):
                    continue
                freq = s.get("frequency")
                amt = float(s.get("amount", 0.0))
                if freq == "monthly":
                    count = horizon_months
                elif freq == "quarterly":
                    count = max(1, horizon_months // 3)
                elif freq == "annual":
                    count = 1 if horizon_months >= 12 else 0
                elif freq == "one_time":
                    count = 1
                else:
                    count = 1
                total += amt * count
                lines.append({"schedule_id": s.get("schedule_id"),"frequency": freq,"instances": count,"amount_per_instance": amt,"total": round(amt * count, 2)})
        if include_taxes:
            taxes = [s for s in data.get("recurring_schedules", []) if s.get("schedule_type") in ("tax_payment",)]
            for t in taxes:
                amt = float(t.get("amount", 0.0))
                total += amt
                lines.append({"schedule_id": t.get("schedule_id"),"frequency": t.get("frequency"),"instances": 1,"amount_per_instance": amt,"total": amt,"type": "tax"})
        return json.dumps({"total_expected_outflows": round(total, 2),"lines": lines}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "forecast_outflows","description": "Forecast expected outflows from recurring schedules and taxes.","parameters": {"type": "object","properties": {"recurring_schedules": {"type": "boolean"},"taxes": {"type": "boolean"},"horizon_months": {"type": "integer"}}}}}

class BuildCashflowView(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        horizon = int(kwargs.get("horizon_months", 3))
        gran = kwargs.get("granularity", "monthly")
        opening = 0.0
        for a in data.get("bank_accounts", []):
            opening += float(a.get("current_balance", 0.0))
        import datetime as _dt
        today = _dt.datetime.fromisoformat("2024-11-30")
        inv_ids = [i.get("invoice_id") for i in data.get("invoices", []) if i.get("invoice_id") in ("INV008","INV009","INV010")]
        inflows_tool = ForecastInflows()
        infl = json.loads(inflows_tool.invoke(data,invoices=inv_ids,probability_rule="overdue_60=0.3"))
        outflows_tool = ForecastOutflows()
        out = json.loads(outflows_tool.invoke(data,recurring_schedules=True,taxes=True,horizon_months=horizon))
        closing = round(opening + float(infl.get("total_expected_inflows", 0.0)) - float(out.get("total_expected_outflows", 0.0)), 2)
        return json.dumps({"as_of": today.date().isoformat(),"granularity": gran,"horizon_months": horizon,"opening_balance": round(opening, 2),"expected_inflows": infl,"expected_outflows": out,"projected_closing_balance": closing}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "build_cashflow_view","description": "Build a simple monthly cashflow projection combining opening balance, inflows and outflows.","parameters": {"type": "object","properties": {"horizon_months": {"type": "integer"},"granularity": {"type": "string"}}}}}

class GetConsultantProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("consultant_id")
        cons = next((c for c in data.get("consultants", []) if c.get("consultant_id") == cid), None)
        return json.dumps(cons or {"error": f"Consultant {cid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "get_consultant_profile","description": "Retrieve consultant master data.","parameters": {"type": "object","properties": {"consultant_id": {"type": "string"}},"required": ["consultant_id"]}}}

class ListTimeEntries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pid = kwargs.get("project_id")
        month = kwargs.get("month")
        entries = [t for t in data.get("time_entries", []) if t.get("project_id") == pid]
        if month:
            entries = [t for t in entries if str(t.get("entry_date", "")).startswith(month)]
        return json.dumps({"project_id": pid,"month": month,"time_entries": entries}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "list_time_entries","description": "List time entries filtered by project and optional month.","parameters": {"type": "object","properties": {"project_id": {"type": "string"},"month": {"type": "string"}},"required": ["project_id"]}}}

class ResolveHourlyRate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pid = kwargs.get("project_id")
        proj = next((p for p in data.get("projects", []) if p.get("project_id") == pid), None)
        if not proj:
            return json.dumps({"error": f"Project {pid} not found"}, indent=2)
        rate = proj.get("override_hourly_rate") or proj.get("default_hourly_rate") or 0.0
        return json.dumps({"project_id": pid,"hourly_rate": float(rate)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "resolve_hourly_rate","description": "Return effective hourly rate for a project (override > default).","parameters": {"type": "object","properties": {"project_id": {"type": "string"}},"required": ["project_id"]}}}

class BuildInvoiceLines(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        time_entries_ids = kwargs.get("time_entries", [])
        hourly_rate = float(kwargs.get("hourly_rate", 0.0))
        entries_index = {t["time_entry_id"]: t for t in data.get("time_entries", [])}
        lines = []
        subtotal = 0.0
        for idx, tid in enumerate(time_entries_ids, start=1):
            te = entries_index.get(tid)
            if not te:
                continue
            hours = float(te.get("hours_worked", 0.0))
            amount = round(hours * hourly_rate, 2)
            line_id = f"LINE-AUTO-{idx:03d}"
            lines.append({"invoice_line_id": line_id,"project_id": te.get("project_id"),"hours_billed": hours,"hourly_rate": hourly_rate,"line_amount": amount})
            subtotal += amount
        return json.dumps({"invoice_lines": lines,"subtotal": round(subtotal, 2)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "build_invoice_lines","description": "Build invoice lines from a list of time entry IDs and an hourly rate.","parameters": {"type": "object","properties": {"time_entries": {"type": "array","items": {"type": "string"}},"hourly_rate": {"type": "number"}},"required": ["time_entries","hourly_rate"]}}}

class GenerateInvoiceNumber(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        year = kwargs.get("year")
        if not year:
            return json.dumps({"error": "year is required"}, indent=2)
        existing = [i.get("invoice_number") for i in data.get("invoices", []) if str(i.get("invoice_number", "")).startswith(f"{year}-")]
        seqs = []
        for num in existing:
            try:
                seqs.append(int(str(num).split("-")[-1]))
            except Exception:
                continue
        next_seq = (max(seqs) + 1) if seqs else 1
        inv_number = f"{year}-{next_seq:03d}"
        return json.dumps({"invoice_number": inv_number}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "generate_invoice_number","description": "Generate the next sequential invoice number for a given year (format: INV-YYYY-XXX equivalent backbone).","parameters": {"type": "object","properties": {"year": {"type": "integer"}},"required": ["year"]}}}

class CalculateTotals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        hst_rate = float(kwargs.get("hst_rate", 0.13))
        invoice_lines = kwargs.get("invoice_lines", [])
        if isinstance(invoice_lines, list) and invoice_lines and isinstance(invoice_lines[0], dict):
            subtotal = sum(float(l.get("line_amount", 0.0)) for l in invoice_lines)
        else:
            subtotal = 0.0
            lines_index = {l["invoice_line_id"]: l for l in data.get("invoice_lines", [])}
            for lid in invoice_lines:
                line = lines_index.get(lid)
                if line:
                    subtotal += float(line.get("line_amount", 0.0))
        hst_amount = round(subtotal * hst_rate, 2)
        total_due = round(subtotal + hst_amount, 2)
        return json.dumps({"subtotal": round(subtotal, 2),"hst_amount": hst_amount,"total_due": total_due}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "calculate_totals","description": "Calculate subtotal, HST and total due based on provided invoice lines.","parameters": {"type": "object","properties": {"invoice_lines": {"type": "array","items": {"anyOf": [{"type": "string"},{"type": "object"}]}},"hst_rate": {"type": "number"}},"required": ["invoice_lines"]}}}

class ComposeInvoicePdf(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoice_id = kwargs.get("invoice_id")
        publisher_id = kwargs.get("publisher_id")
        if not invoice_id or not publisher_id:
            return json.dumps({"error": "invoice_id and publisher_id are required"}, indent=2)
        path = f"/invoices/auto/{invoice_id}.pdf"
        return json.dumps({"invoice_id": invoice_id,"publisher_id": publisher_id,"pdf_path": path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "compose_invoice_pdf","description": "Generate a PDF artifact path for the invoice.","parameters": {"type": "object","properties": {"invoice_id": {"type": "string"},"publisher_id": {"type": "string"}},"required": ["invoice_id","publisher_id"]}}}

class InsertInvoice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["invoice_id","publisher_id","subtotal","hst_amount","total_due"]
        for k in required:
            if kwargs.get(k) is None:
                return json.dumps({"error": f"{k} is required"}, indent=2)
        invs = data.setdefault("invoices", [])
        record = {"invoice_id": kwargs["invoice_id"],"invoice_number": kwargs.get("invoice_number"),"publisher_id": kwargs["publisher_id"],"invoice_date": kwargs.get("invoice_date"),"period_start": kwargs.get("period_start"),"period_end": kwargs.get("period_end"),"subtotal": kwargs["subtotal"],"hst_amount": kwargs["hst_amount"],"total_due": kwargs["total_due"],"pdf_path": kwargs.get("pdf_path"),"sent_at": kwargs.get("sent_at"),"paid_at": kwargs.get("paid_at"),"created_at": kwargs.get("created_at")}
        invs.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "insert_invoice","description": "Insert a new invoice header into the dataset.","parameters": {"type": "object","properties": {"invoice_id": {"type": "string"},"publisher_id": {"type": "string"},"subtotal": {"type": "number"},"hst_amount": {"type": "number"},"total_due": {"type": "number"},"invoice_number": {"type": "string"},"invoice_date": {"type": "string"},"period_start": {"type": "string"},"period_end": {"type": "string"},"pdf_path": {"type": "string"},"sent_at": {"type": "string"},"paid_at": {"type": "string"},"created_at": {"type": "string"}},"required": ["invoice_id","publisher_id","subtotal","hst_amount","total_due"]}}}

class ListPublisherOpenInvoices(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pub_id = kwargs.get("publisher_id")
        if not pub_id:
            return json.dumps({"error": "publisher_id is required"}, indent=2)
        invoices = data.get("invoices", [])
        open_invs = [i for i in invoices if i.get("publisher_id") == pub_id and not i.get("paid_at")]
        return json.dumps({"publisher_id": pub_id,"invoice_ids": [i["invoice_id"] for i in open_invs]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "list_publisher_open_invoices","description": "Return unpaid invoice IDs for a publisher.","parameters": {"type": "object","properties": {"publisher_id": {"type": "string"}},"required": ["publisher_id"]}}}
    

class ComputeYtdFromMonthlyRevenue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        year = kwargs.get("year")
        through = kwargs.get("through_month")
        if not year or not through:
            return json.dumps({"error":"year and through_month are required"}, indent=2)
        rows = [r for r in data.get("monthly_revenue", []) if str(r.get("month_year","")).startswith(f"{year}-")]
        total = 0.0
        for r in rows:
            try:
                m = int(r["month_year"].split("-")[1])
                if m <= through:
                    total += float(r.get("revenue",0.0))
            except Exception:
                continue
        return json.dumps({"year": year,"through_month": through,"ytd_revenue": round(total,2)}, indent=2)

    @staticmethod
    def get_info(self=None) -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"compute_ytd_from_monthly_revenue",
            "description":"Compute YTD revenue summing monthly_revenue rows up to a month.",
            "parameters":{"type":"object","properties":{
                "year":{"type":"integer"},
                "through_month":{"type":"integer"}
            },"required":["year","through_month"]}
        }}

class ReconcileTaxReserve(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        comp_ref = kwargs.get("computed_tax_reserve_ref")
        snap_ref = kwargs.get("snapshot_ref")
        threshold = float(kwargs.get("threshold", 0.0))
        if not comp_ref or not snap_ref:
            return json.dumps({"error":"computed_tax_reserve_ref and snapshot_ref are required"}, indent=2)
        computed = float(comp_ref.get("tax_reserve") or comp_ref.get("ytd_tax_reserve") or 0.0)
        snap_val = float(snap_ref.get("ytd_tax_reserve") or 0.0)
        diff = round(computed - snap_val, 2)
        adj = diff if abs(diff) > threshold else 0.00
        return json.dumps({"adjustment": round(adj,2)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"reconcile_tax_reserve",
            "description":"Compute adjustment needed between computed and snapshot tax reserve.",
            "parameters":{"type":"object","properties":{
                "computed_tax_reserve_ref":{"type":"object"},
                "snapshot_ref":{"type":"object"},
                "threshold":{"type":"number"}
            },"required":["computed_tax_reserve_ref","snapshot_ref"]}
        }}

class PostJournalEntry(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        date = kwargs.get("date")
        account = kwargs.get("account")
        memo = kwargs.get("memo","")
        amount_ref = kwargs.get("amount_ref", {})
        amount = float(amount_ref.get("adjustment", 0.0))
        journals = data.setdefault("journals", [])
        rec = {"journal_id": f"JRN-{len(journals)+1:05d}", "date": date, "account": account, "amount": round(amount,2), "memo": memo}
        journals.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"post_journal_entry",
            "description":"Post a simple journal entry (in-memory).",
            "parameters":{"type":"object","properties":{
                "date":{"type":"string"},
                "account":{"type":"string"},
                "amount_ref":{"type":"object"},
                "memo":{"type":"string"}
            },"required":["date","account","amount_ref"]}
        }}

class BuildKpiReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        as_of = kwargs.get("as_of","2024-11-30")
        sections = kwargs.get("sections",[])
        name = kwargs.get("artifact_name","AR_KPI_Report")
        path = f"/reports/kpi/{name}.pdf"
        return json.dumps({"as_of": as_of, "sections": sections, "pdf_path": path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"build_kpi_report",
            "description":"Generate a KPI report artifact path.",
            "parameters":{"type":"object","properties":{
                "as_of":{"type":"string"},
                "sections":{"type":"array","items":{"type":"string"}},
                "artifact_name":{"type":"string"}
            },"required":["as_of","sections","artifact_name"]}
        }}

class ListExpensesByDateRangeAndCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        start = kwargs.get("start_date")
        end = kwargs.get("end_date")
        cats = kwargs.get("categories", [])
        if not start or not end or not cats:
            return json.dumps({"error":"start_date, end_date, categories are required"}, indent=2)
        exp = []
        for e in data.get("expenses", []):
            d = str(e.get("expense_date",""))
            if start <= d <= end and e.get("category_code") in cats:
                exp.append(e)
        return json.dumps({"expenses": exp}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_expenses_by_date_range_and_category",
            "description":"Return expenses in [start_date, end_date] for given categories.",
            "parameters":{"type":"object","properties":{
                "start_date":{"type":"string"},
                "end_date":{"type":"string"},
                "categories":{"type":"array","items":{"type":"string"}}
            },"required":["start_date","end_date","categories"]}
        }}

class FlagHighValueMeals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ref = kwargs.get("expenses_ref", {})
        threshold = float(kwargs.get("threshold", 150.0))
        items = ref.get("expenses", [])
        decisions = []
        for e in items:
            if e.get("category_code") == "MEALS_ENTERTAIN" and float(e.get("gross_amount",0.0)) > threshold:
                decisions.append({"invoice_id": None, "action": "email_reminder", "notes": f"High value meal: {e.get('expense_id')} > {threshold}"})
        return json.dumps({"decisions": decisions, "count": len(decisions)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"flag_high_value_meals",
            "description":"Produce decisions for meals exceeding threshold (for audit entries).",
            "parameters":{"type":"object","properties":{
                "expenses_ref":{"type":"object"},
                "threshold":{"type":"number"}
            },"required":["expenses_ref"]}
        }}


TOOLS = [
    GetInvoiceDetails(),
    ComputeInvoiceAging(),
    CreateAuditEntry(),
    GetDashboardSnapshot(),
    ComputeTaxReserve(),
    CreateDashboardSnapshot(),
    ComputeYtdFromMonthlyRevenue(),
    ReconcileTaxReserve(),
    PostJournalEntry(),
    BuildKpiReport(),
    GetExpenseDetails(),
    ApplyDeductibilityRules(),
    GenerateExpenseDashboard(),
    ListExpensesByDateRangeAndCategory(),
    FlagHighValueMeals(),
    GetBankBalances(),
    ListRecurringSchedules(),
    ComputePaymentBehavior(),
    ForecastInflows(),
    ForecastOutflows(),
    BuildCashflowView(),
    GetConsultantProfile(),
    ListTimeEntries(),
    ResolveHourlyRate(),
    BuildInvoiceLines(),
    GenerateInvoiceNumber(),
    CalculateTotals(),
    ComposeInvoicePdf(),
    InsertInvoice(),
    ListPublisherOpenInvoices()]
