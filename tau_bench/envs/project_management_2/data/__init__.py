import json
import os
from typing import Any

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> dict[str, Any]:
    db: dict[str, Any] = {}
    # auto-generated from files present in data/
    tables = ['allocation_costs', 'allocations', 'approval_workflows', 'approvals', 'archived_milestones', 'artifact_updates', 'bench_resources', 'budget_alerts', 'budget_modifications', 'budget_transfers', 'budgets', 'capacity_calendar', 'change_approvals', 'change_history', 'change_request_reports', 'change_requests', 'change_reviews', 'compression_analyses', 'conflicts', 'cost_allocations', 'cost_forecasts', 'critical_paths', 'deliverables', 'departments', 'emergency_logs', 'employees', 'escalations', 'expenses', 'external_dependencies', 'financial_alerts', 'gate_reviews', 'invoices', 'leveling_results', 'milestone_dependencies', 'milestone_templates', 'milestone_updates', 'milestones', 'payments', 'project_phases', 'projects', 'purchase_orders', 'recovery_plans', 'reimbursements', 'resource_pools', 'resource_requests', 'retrospectives', 'risk_assessments', 'rotation_schedules', 'schedule_baselines', 'schedule_buffers', 'schedule_changes', 'scope_baselines', 'skill_requirements', 'skills', 'sprints', 'stakeholders', 'task_history', 'task_logs', 'tasks', 'teams', 'utilization_logs', 'vendors']
    for name in tables:
        path = os.path.join(FOLDER_PATH, f"{name}.json")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                db[name] = json.loads(content) if content else []
        except FileNotFoundError:
            db[name] = []
    return db

