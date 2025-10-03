import json
from pathlib import Path
from typing import List, Dict, Any
import copy

from domains.base import BaseDomain
from domains.dto import Tool


class ProjectManagementSystem(BaseDomain):
    def __init__(self, tools: List[Tool]):
        super().__init__(tools)
        self.master_database = self._load_data()
        self.database = copy.deepcopy(self.master_database)

    def reset_database(self):
        self.database = copy.deepcopy(self.master_database)
        return True

    def _load_data(self) -> Dict[str, Any]:
        db = {}
        data_path = Path(__file__).parent / "data"

        table_files = [
            "employees",
            "projects",
            "allocations",
            "teams",
            "departments",
            "resource_requests",
            "bench_resources",
            "rotation_schedules",
            "utilization_logs",
            "skills",
            "skill_requirements",
            "project_phases",
            "resource_pools",
            "allocation_costs",
            "approvals",
            "capacity_calendar",
            "conflicts",
            "escalations",
            "retrospectives",
            "sprints",
            "task_history",
            "task_logs",
            "tasks",
            "approval_workflows",
            "archived_milestones",
            "artifact_updates",
            "budget_alerts",
            "budget_modifications",
            "budget_transfers",
            "budgets",
            "change_approvals",
            "change_history",
            "change_requests",
            "change_reviews",
            "change_request_reports",
            "compression_analyses",
            "cost_allocations",
            "cost_forecasts",
            "critical_paths",
            "deliverables",
            "emergency_logs",
            "expenses",
            "external_dependencies",
            "financial_alerts",
            "gate_reviews",
            "invoices",
            "leveling_results",
            "milestone_dependencies",
            "milestone_templates",
            "milestone_updates",
            "milestones",
            "payments",
            "purchase_orders",
            "recovery_plans",
            "reimbursements",
            "risk_assessments",
            "schedule_baselines",
            "schedule_buffers",
            "schedule_changes",
            "scope_baselines",
            "stakeholders",
            "vendors"
        ]

        for table_name in table_files:
            file_path = data_path / f"{table_name}.json"
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if content:
                        db[table_name] = json.loads(content)
                    else:
                        db[table_name] = []
            except FileNotFoundError:
                if table_name in ["employees", "projects", "allocations", "departments"]:
                    raise FileNotFoundError(f"Core data file not found: {file_path}")
                db[table_name] = []
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from {file_path}: {e}")
                db[table_name] = []

        return db
