import json
from typing import Any

from tau_bench.envs.tool import Tool


class GetInvoiceDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None) -> str:
        if not invoice_id:
            payload = {"error": "invoice_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        invoices = data.get("invoices", [])
        inv = next((i for i in invoices if i.get("invoice_id") == invoice_id), None)
        payload = inv or {"error": f"Invoice {invoice_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInvoiceDetails",
                "description": "Retrieve all data for a specific invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {
                            "type": "string",
                            "description": "The ID of the invoice.",
                        }
                    },
                    "required": ["invoice_id"],
                },
            },
        }


class ComputeInvoiceAging(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, today: str = None) -> str:
        import datetime as _dt

        if not invoice_id or not today:
            payload = {"error": "invoice_id and today are required"}
            out = json.dumps(payload, indent=2)
            return out
        invoices = data.get("invoices", [])
        inv = next((i for i in invoices if i.get("invoice_id") == invoice_id), None)
        if not inv:
            payload = {"error": f"Invoice {invoice_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if inv.get("paid_at"):
            payload = {
                    "invoice_id": invoice_id,
                    "status": "paid",
                    "days_overdue": 0,
                    "bucket": "current",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        inv_date = _dt.datetime.fromisoformat(inv["invoice_date"])
        today_date = _dt.datetime.fromisoformat(today)
        days = (today_date - inv_date).days
        bucket = (
            "0-30"
            if days <= 30
            else "31-60" if days <= 60 else "61-90" if days <= 90 else "90+"
        )
        payload = {
                "invoice_id": invoice_id,
                "status": "unpaid",
                "days_overdue": days,
                "bucket": bucket,
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
                "name": "ComputeInvoiceAging",
                "description": "Compute days overdue and aging bucket for a given invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "today": {
                            "type": "string",
                            "description": "YYYY-MM-DD reference date",
                        },
                    },
                    "required": ["invoice_id", "today"],
                },
            },
        }


class CreateAuditEntry(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, event_type: str = None, notes: str = "") -> str:
        import datetime as _dt

        if not invoice_id or not event_type:
            payload = {"error": "invoice_id and event_type are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        audit = data.setdefault("invoice_audit", [])
        new_id = f"AUTO-AUD-{len(audit)+1:04d}"
        ts = _dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
        record = {
            "audit_id": new_id,
            "invoice_id": invoice_id,
            "event_type": event_type,
            "event_timestamp": ts,
            "notes": notes,
        }
        audit.append(record)
        payload = record
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAuditEntry",
                "description": "Create an audit event for an invoice (reminder, second_notice, escalation, etc).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["invoice_id", "event_type"],
                },
            },
        }


class GetDashboardSnapshot(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], snapshot_id: str = None) -> str:
        snaps = data.get("dashboard_snapshots", [])
        snap = next((s for s in snaps if s.get("snapshot_id") == snapshot_id), None)
        payload = snap or {"error": f"Snapshot {snapshot_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDashboardSnapshot",
                "description": "Get a dashboard snapshot by snapshot_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"snapshot_id": {"type": "string"}},
                    "required": ["snapshot_id"],
                },
            },
        }


class ComputeTaxReserve(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tax_year: int = None, ytd_revenue: float = None) -> str:
        year = tax_year
        revenue = ytd_revenue
        if year is None or revenue is None:
            payload = {"error": "tax_year and ytd_revenue are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        rate = next(
            (
                t["rate_percent"]
                for t in data.get("tax_rates", [])
                if t.get("tax_year") == year
            ),
            None,
        )
        if rate is None:
            payload = {"error": f"No tax rate for {year}"}
            out = json.dumps(payload, indent=2)
            return out
        reserve = round(float(revenue) * (float(rate) / 100.0), 2)
        payload = {
                "ytd_revenue": revenue,
                "tax_year": year,
                "tax_rate": rate,
                "tax_reserve": reserve,
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
                "name": "ComputeTaxReserve",
                "description": "Compute tax reserve given YTD revenue and tax year.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ytd_revenue": {"type": "number"},
                        "tax_year": {"type": "integer"},
                    },
                    "required": ["ytd_revenue", "tax_year"],
                },
            },
        }


class CreateDashboardSnapshot(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], snapshot_date: str = None, ytd_revenue: float = None, ytd_tax_reserve: float = None, pdf_path: str = None) -> str:
        required = ["snapshot_date", "ytd_revenue", "ytd_tax_reserve", "pdf_path"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}
        for k in required:
            if params_dict.get(k) is None:
                payload = {"error": f"{k} is required"}
                out = json.dumps(payload, indent=2)
                return out
        snaps = data.setdefault("dashboard_snapshots", [])
        new_id = f"SNAP-AUTO-{len(snaps)+1:03d}"
        record = {
            "snapshot_id": new_id,
            "snapshot_date": snapshot_date,
            "ytd_revenue": ytd_revenue,
            "ytd_tax_reserve": ytd_tax_reserve,
            "pdf_path": pdf_path,
        }
        snaps.append(record)
        payload = record
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDashboardSnapshot",
                "description": "Append a new dashboard snapshot with artifact path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_date": {"type": "string"},
                        "ytd_revenue": {"type": "number"},
                        "ytd_tax_reserve": {"type": "number"},
                        "pdf_path": {"type": "string"},
                    },
                    "required": [
                        "snapshot_date",
                        "ytd_revenue",
                        "ytd_tax_reserve",
                        "pdf_path",
                    ],
                },
            },
        }


class GetExpenseDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], expense_id: str = None) -> str:
        if not expense_id:
            payload = {"error": "expense_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        expenses = data.get("expenses", [])
        exp = next((e for e in expenses if e.get("expense_id") == expense_id), None)
        payload = exp or {"error": f"Expense {expense_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getExpenseDetails",
                "description": "Retrieve all data for a specific expense.",
                "parameters": {
                    "type": "object",
                    "properties": {"expense_id": {"type": "string"}},
                    "required": ["expense_id"],
                },
            },
        }


class ApplyDeductibilityRules(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], expense_id: str = None) -> str:
        if not expense_id:
            payload = {"error": "expense_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        exp = next(
            (e for e in data.get("expenses", []) if e.get("expense_id") == expense_id),
            None,
        )
        if not exp:
            payload = {"error": f"Expense {expense_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        cat = exp.get("category_code")
        cat_obj = next(
            (
                c
                for c in data.get("expense_categories", [])
                if c.get("category_code") == cat
            ),
            None,
        )
        if not cat_obj:
            payload = {"error": f"Category {cat} not found"}
            out = json.dumps(payload, indent=2)
            return out
        pct = float(cat_obj.get("deductible_percent", 100)) / 100.0
        allowed = round(float(exp.get("gross_amount", 0.0)) * pct, 2)
        result = {
            "expense_id": expense_id,
            "category_code": cat,
            "deductible_percent": pct * 100,
            "allowed_amount": allowed,
        }
        exp["allowed_amount"] = allowed
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyDeductibilityRules",
                "description": "Apply expense category deductibility to compute allowed_amount.",
                "parameters": {
                    "type": "object",
                    "properties": {"expense_id": {"type": "string"}},
                    "required": ["expense_id"],
                },
            },
        }


class GenerateExpenseDashboard(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], quarter: str = None, included_expenses: list = None, as_of: str = None, artifact_name: str = None) -> str:
        if not quarter or not isinstance(included_expenses, list):
            payload = {"error": "quarter and included_expenses list are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        path = (
            f"/dashboards/ExpenseDashboards/{quarter}/expense_dashboard_{quarter}.pdf"
        )
        payload = {"quarter": quarter, "included_expenses": included_expenses, "pdf_path": path}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateExpenseDashboard",
                "description": "Generate an expense dashboard artifact for a given quarter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "quarter": {"type": "string"},
                        "included_expenses": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["quarter", "included_expenses"],
                },
            },
        }


class GetBankBalances(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        accts = data.get("bank_accounts", [])
        total = 0.0
        details: list[dict[str, Any]] = []
        for a in accts:
            bal = float(a.get("current_balance", 0.0))
            total += bal
            details.append(
                {
                    "account_id": a.get("account_id"),
                    "balance": bal,
                    "currency": a.get("currency"),
                }
            )
        payload = {"total_balance": round(total, 2), "accounts": details}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBankBalances",
                "description": "Return total and per-account current balances.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class ListRecurringSchedules(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], horizon_months: int = 3) -> str:
        horizon = int(horizon_months)
        schedules = [
            s for s in data.get("recurring_schedules", []) if s.get("is_active", False)
        ]
        payload = {"horizon_months": horizon, "active_schedules": schedules}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListRecurringSchedules",
                "description": "List active recurring schedules considered for the forecast horizon.",
                "parameters": {
                    "type": "object",
                    "properties": {"horizon_months": {"type": "integer"}},
                },
            },
        }


class ComputePaymentBehavior(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], publisher_id: str = None) -> str:
        if not publisher_id:
            payload = {"error": "publisher_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        pb = next(
            (
                p
                for p in data.get("payment_behavior", [])
                if p.get("publisher_id") == publisher_id
            ),
            None,
        )
        payload = pb or {"error": f"payment_behavior for {publisher_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputePaymentBehavior",
                "description": "Return stored payment behavior stats for a publisher.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_id": {"type": "string"}},
                    "required": ["publisher_id"],
                },
            },
        }


class ForecastInflows(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoices: list = None, probability_rule: str = "overdue_60=0.3") -> str:
        invoices_ids = invoices if invoices is not None else []
        prob_rule = probability_rule
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
            breakdown.append(
                {
                    "invoice_id": inv_id,
                    "days_overdue": days,
                    "amount": amt,
                    "probability": prob,
                    "expected": expected,
                }
            )
        payload = {
                "total_expected_inflows": round(total_expected, 2),
                "breakdown": breakdown,
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
                "name": "ForecastInflows",
                "description": "Forecast expected inflows from invoices (discount >60d overdue).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoices": {"type": "array", "items": {"type": "string"}},
                        "probability_rule": {"type": "string"},
                    },
                    "required": ["invoices"],
                },
            },
        }


class ForecastOutflows(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recurring_schedules: bool = True, taxes: bool = True, horizon_months: int = 3) -> str:
        include_sched = bool(recurring_schedules)
        include_taxes = bool(taxes)
        horizon_months = int(horizon_months)
        total = 0.0
        lines: list[dict[str, Any]] = []
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
                lines.append(
                    {
                        "schedule_id": s.get("schedule_id"),
                        "frequency": freq,
                        "instances": count,
                        "amount_per_instance": amt,
                        "total": round(amt * count, 2),
                    }
                )
        if include_taxes:
            taxes = [
                s
                for s in data.get("recurring_schedules", [])
                if s.get("schedule_type") in ("tax_payment",)
            ]
            for t in taxes:
                amt = float(t.get("amount", 0.0))
                total += amt
                lines.append(
                    {
                        "schedule_id": t.get("schedule_id"),
                        "frequency": t.get("frequency"),
                        "instances": 1,
                        "amount_per_instance": amt,
                        "total": amt,
                        "type": "tax",
                    }
                )
        payload = {"total_expected_outflows": round(total, 2), "lines": lines}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ForecastOutflows",
                "description": "Forecast expected outflows from recurring schedules and taxes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recurring_schedules": {"type": "boolean"},
                        "taxes": {"type": "boolean"},
                        "horizon_months": {"type": "integer"},
                    },
                },
            },
        }


class BuildCashflowView(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], horizon_months: int = 3, granularity: str = "monthly") -> str:
        opening = 0.0
        for a in data.get("bank_accounts", []):
            opening += float(a.get("current_balance", 0.0))
        import datetime as _dt

        today = _dt.datetime.fromisoformat("2024-11-30")
        inv_ids = [
            i.get("invoice_id")
            for i in data.get("invoices", [])
            if i.get("invoice_id") in ("INV008", "INV009", "INV010")
        ]
        inflows_tool = ForecastInflows()
        infl = json.loads(
            inflows_tool.invoke(
                data, invoices=inv_ids, probability_rule="overdue_60=0.3"
            )
        )
        outflows_tool = ForecastOutflows()
        out = json.loads(
            outflows_tool.invoke(
                data, recurring_schedules=True, taxes=True, horizon_months=horizon_months
            )
        )
        closing = round(
            opening
            + float(infl.get("total_expected_inflows", 0.0))
            - float(out.get("total_expected_outflows", 0.0)),
            2,
        )
        payload = {
                "as_of": today.date().isoformat(),
                "granularity": granularity,
                "horizon_months": horizon_months,
                "opening_balance": round(opening, 2),
                "expected_inflows": infl,
                "expected_outflows": out,
                "projected_closing_balance": closing,
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
                "name": "BuildCashflowView",
                "description": "Build a simple monthly cashflow projection combining opening balance, inflows and outflows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "horizon_months": {"type": "integer"},
                        "granularity": {"type": "string"},
                    },
                },
            },
        }


class GetConsultantProfile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], consultant_id: str = None) -> str:
        cid = consultant_id
        cons = next(
            (c for c in data.get("consultants", []) if c.get("consultant_id") == cid),
            None,
        )
        payload = cons or {"error": f"Consultant {cid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getConsultantProfile",
                "description": "Retrieve consultant master data.",
                "parameters": {
                    "type": "object",
                    "properties": {"consultant_id": {"type": "string"}},
                    "required": ["consultant_id"],
                },
            },
        }


class ListTimeEntries(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None, month: str = None) -> str:
        pid = project_id
        entries = [
            t for t in data.get("time_entries", []) if t.get("project_id") == pid
        ]
        if month:
            entries = [
                t for t in entries if str(t.get("entry_date", "")).startswith(month)
            ]
        payload = {"project_id": pid, "month": month, "time_entries": entries}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListTimeEntries",
                "description": "List time entries filtered by project and optional month.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "month": {"type": "string"},
                    },
                    "required": ["project_id"],
                },
            },
        }


class ResolveHourlyRate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        proj = next(
            (p for p in data.get("projects", []) if p.get("project_id") == project_id), None
        )
        if not proj:
            payload = {"error": f"Project {project_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        rate = (
            proj.get("override_hourly_rate") or proj.get("default_hourly_rate") or 0.0
        )
        payload = {"project_id": project_id, "hourly_rate": float(rate)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ResolveHourlyRate",
                "description": "Return effective hourly rate for a project (override > default).",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }


class BuildInvoiceLines(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], time_entries: list = None, hourly_rate: float = 0.0) -> str:
        time_entries_ids = time_entries or []
        hourly_rate = float(hourly_rate)
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
            lines.append(
                {
                    "invoice_line_id": line_id,
                    "project_id": te.get("project_id"),
                    "hours_billed": hours,
                    "hourly_rate": hourly_rate,
                    "line_amount": amount,
                }
            )
            subtotal += amount
        payload = {"invoice_lines": lines, "subtotal": round(subtotal, 2)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildInvoiceLines",
                "description": "Build invoice lines from a list of time entry IDs and an hourly rate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "time_entries": {"type": "array", "items": {"type": "string"}},
                        "hourly_rate": {"type": "number"},
                    },
                    "required": ["time_entries", "hourly_rate"],
                },
            },
        }


class GenerateInvoiceNumber(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], year: str = None) -> str:
        if not year:
            payload = {"error": "year is required"}
            out = json.dumps(payload, indent=2)
            return out
        existing = [
            i.get("invoice_number")
            for i in data.get("invoices", [])
            if str(i.get("invoice_number", "")).startswith(f"{year}-")
        ]
        seqs = []
        for num in existing:
            try:
                seqs.append(int(str(num).split("-")[-1]))
            except Exception:
                continue
        next_seq = (max(seqs) + 1) if seqs else 1
        inv_number = f"{year}-{next_seq:03d}"
        payload = {"invoice_number": inv_number}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateInvoiceNumber",
                "description": "Generate the next sequential invoice number for a given year (format: INV-YYYY-XXX equivalent backbone).",
                "parameters": {
                    "type": "object",
                    "properties": {"year": {"type": "integer"}},
                    "required": ["year"],
                },
            },
        }


class CalculateTotals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], hst_rate: float = 0.13, invoice_lines: list = None) -> str:
        if invoice_lines is None:
            invoice_lines = []
        if (
            isinstance(invoice_lines, list)
            and invoice_lines
            and isinstance(invoice_lines[0], dict)
        ):
            subtotal = sum(float(l.get("line_amount", 0.0)) for l in invoice_lines)
        else:
            subtotal = 0.0
            lines_index = {
                l["invoice_line_id"]: l for l in data.get("invoice_lines", [])
            }
            for lid in invoice_lines:
                line = lines_index.get(lid)
                if line:
                    subtotal += float(line.get("line_amount", 0.0))
        hst_amount = round(subtotal * hst_rate, 2)
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
                "name": "CalculateTotals",
                "description": "Calculate subtotal, HST and total due based on provided invoice lines.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_lines": {
                            "type": "array",
                            "items": {
},
                        },
                        "hst_rate": {"type": "number"},
                    },
                    "required": ["invoice_lines"],
                },
            },
        }


class ComposeInvoicePdf(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, publisher_id: str = None) -> str:
        if not invoice_id or not publisher_id:
            payload = {"error": "invoice_id and publisher_id are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        path = f"/invoices/auto/{invoice_id}.pdf"
        payload = {"invoice_id": invoice_id, "publisher_id": publisher_id, "pdf_path": path}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComposeInvoicePdf",
                "description": "Generate a PDF artifact path for the invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "publisher_id": {"type": "string"},
                    },
                    "required": ["invoice_id", "publisher_id"],
                },
            },
        }


class InsertInvoice(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        invoice_id: str,
        publisher_id: str,
        subtotal: float,
        hst_amount: float,
        total_due: float,
        invoice_number: str = None,
        invoice_date: str = None,
        period_start: str = None,
        period_end: str = None,
        pdf_path: str = None,
        sent_at: str = None,
        paid_at: str = None,
        created_at: str = None
    ) -> str:
        required = ["invoice_id", "publisher_id", "subtotal", "hst_amount", "total_due"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}
        for k in required:
            if params_dict.get(k) is None:
                payload = {"error": f"{k} is required"}
                out = json.dumps(payload, indent=2)
                return out
        invs = data.setdefault("invoices", [])
        record = {
            "invoice_id": invoice_id,
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
        }
        invs.append(record)
        payload = record
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertInvoice",
                "description": "Insert a new invoice header into the dataset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "publisher_id": {"type": "string"},
                        "subtotal": {"type": "number"},
                        "hst_amount": {"type": "number"},
                        "total_due": {"type": "number"},
                        "invoice_number": {"type": "string"},
                        "invoice_date": {"type": "string"},
                        "period_start": {"type": "string"},
                        "period_end": {"type": "string"},
                        "pdf_path": {"type": "string"},
                        "sent_at": {"type": "string"},
                        "paid_at": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "invoice_id",
                        "publisher_id",
                        "subtotal",
                        "hst_amount",
                        "total_due",
                    ],
                },
            },
        }


class ListPublisherOpenInvoices(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], publisher_id: str = None) -> str:
        if not publisher_id:
            payload = {"error": "publisher_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        invoices = data.get("invoices", [])
        open_invs = [
            i
            for i in invoices
            if i.get("publisher_id") == publisher_id and not i.get("paid_at")
        ]
        payload = {
                "publisher_id": publisher_id,
                "invoice_ids": [i["invoice_id"] for i in open_invs],
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
                "name": "ListPublisherOpenInvoices",
                "description": "Return unpaid invoice IDs for a publisher.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_id": {"type": "string"}},
                    "required": ["publisher_id"],
                },
            },
        }


class ComputeYtdFromMonthlyRevenue(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], year: int = None, through_month: int = None) -> str:
        if not year or not through_month:
            payload = {"error": "year and through_month are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        rows = [
            r
            for r in data.get("monthly_revenue", [])
            if str(r.get("month_year", "")).startswith(f"{year}-")
        ]
        total = 0.0
        for r in rows:
            try:
                m = int(r["month_year"].split("-")[1])
                if m <= through_month:
                    total += float(r.get("revenue", 0.0))
            except Exception:
                continue
        payload = {"year": year, "through_month": through_month, "ytd_revenue": round(total, 2)}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info(self=None) -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "ComputeYtdFromMonthlyRevenue",
                "description": "Compute YTD revenue summing monthly_revenue rows up to a month.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "year": {"type": "integer"},
                        "through_month": {"type": "integer"},
                    },
                    "required": ["year", "through_month"],
                },
            },
        }


class ReconcileTaxReserve(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        computed_tax_reserve_ref: dict[str, Any] = None, 
        snapshot_ref: dict[str, Any] = None, 
        threshold: float = 0.0
    ) -> str:
        if not computed_tax_reserve_ref or not snapshot_ref:
            payload = {"error": "computed_tax_reserve_ref and snapshot_ref are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        computed = float(
            computed_tax_reserve_ref.get("tax_reserve") or computed_tax_reserve_ref.get("ytd_tax_reserve") or 0.0
        )
        snap_val = float(snapshot_ref.get("ytd_tax_reserve") or 0.0)
        diff = round(computed - snap_val, 2)
        adj = diff if abs(diff) > threshold else 0.00
        payload = {"adjustment": round(adj, 2)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReconcileTaxReserve",
                "description": "Compute adjustment needed between computed and snapshot tax reserve.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "computed_tax_reserve_ref": {"type": "object"},
                        "snapshot_ref": {"type": "object"},
                        "threshold": {"type": "number"},
                    },
                    "required": ["computed_tax_reserve_ref", "snapshot_ref"],
                },
            },
        }


class PostJournalEntry(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], date: str, account: str, memo: str = "", amount_ref: dict[str, Any] = {}, amount: float = None) -> str:
        if amount is None:
            amount = float(amount_ref.get("adjustment", 0.0))
        else:
            amount = float(amount)
        journals = data.setdefault("journals", [])
        rec = {
            "journal_id": f"JRN-{len(journals)+1:05d}",
            "date": date,
            "account": account,
            "amount": round(amount, 2),
            "memo": memo,
        }
        journals.append(rec)
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PostJournalEntry",
                "description": "Post a simple journal entry (in-memory).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "account": {"type": "string"},
                        "amount_ref": {"type": "object"},
                        "memo": {"type": "string"},
                    },
                    "required": ["date", "account", "amount_ref"],
                },
            },
        }


class BuildKpiReport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], as_of: str = "2024-11-30", sections: list = None, artifact_name: str = "AR_KPI_Report") -> str:
        if sections is None:
            sections = []
        path = f"/reports/kpi/{artifact_name}.pdf"
        payload = {"as_of": as_of, "sections": sections, "pdf_path": path}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildKpiReport",
                "description": "Generate a KPI report artifact path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "as_of": {"type": "string"},
                        "sections": {"type": "array", "items": {"type": "string"}},
                        "artifact_name": {"type": "string"},
                    },
                    "required": ["as_of", "sections", "artifact_name"],
                },
            },
        }


class ListExpensesByDateRangeAndCategory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], start_date: str = None, end_date: str = None, categories: list = None) -> str:
        if not start_date or not end_date or not categories:
            payload = {"error": "start_date, end_date, categories are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        exp = []
        for e in data.get("expenses", []):
            d = str(e.get("expense_date", ""))
            if start_date <= d <= end_date and e.get("category_code") in categories:
                exp.append(e)
        payload = {"expenses": exp}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListExpensesByDateRangeAndCategory",
                "description": "Return expenses in [start_date, end_date] for given categories.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "categories": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["start_date", "end_date", "categories"],
                },
            },
        }


class FlagHighValueMeals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], expenses_ref: dict = None, threshold: float = 150.0) -> str:
        ref = expenses_ref if expenses_ref is not None else {}
        items = ref.get("expenses", [])
        decisions = []
        for e in items:
            if (
                e.get("category_code") == "MEALS_ENTERTAIN"
                and float(e.get("gross_amount", 0.0)) > threshold
            ):
                decisions.append(
                    {
                        "invoice_id": None,
                        "action": "email_reminder",
                        "notes": f"High value meal: {e.get('expense_id')} > {threshold}",
                    }
                )
        payload = {"decisions": decisions, "count": len(decisions)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FlagHighValueMeals",
                "description": "Produce decisions for meals exceeding threshold (for audit entries).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expenses_ref": {"type": "object"},
                        "threshold": {"type": "number"},
                    },
                    "required": ["expenses_ref"],
                },
            },
        }


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
    ListPublisherOpenInvoices(),
]
