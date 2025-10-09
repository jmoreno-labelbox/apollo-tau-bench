import json
import os
from typing import Any

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> dict[str, Any]:
    db: dict[str, Any] = {}
    # auto-generated from files present in data/
    tables = ['bank_accounts', 'consultants', 'dashboard_snapshots', 'expense_categories', 'expenses', 'invoice_audit', 'invoice_lines', 'invoices', 'monthly_revenue', 'payment_behavior', 'pipeline_opportunities', 'project_revenue', 'projects', 'publishers', 'recurring_schedules', 'scheduler_runs', 'tax_rates', 'time_entries']
    for name in tables:
        path = os.path.join(FOLDER_PATH, f"{name}.json")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                db[name] = json.loads(content) if content else []
        except FileNotFoundError:
            db[name] = []
    return db

