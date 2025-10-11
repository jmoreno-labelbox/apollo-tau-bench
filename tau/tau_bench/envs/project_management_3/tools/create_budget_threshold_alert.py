# Sierra Copyright

import datetime, uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateBudgetThresholdAlert(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], alert_name, project_id, alert_recipients = [], threshold_percentage = 80) -> str:

        if not all([project_id, alert_recipients]):
            return json.dumps({"error": "project_id and alert_recipients are required"})

        if threshold_percentage < 50 or threshold_percentage > 100:
            return json.dumps(
                {"error": "threshold_percentage must be between 50 and 100"}
            )

        budgets = data.get("budgets", [])
        budget_alerts = data.get("budget_alerts", [])
        projects = list(data.get("projects", {}).values())

        project = next((p for p in projects if p.get("project_id") == project_id), None)
        if not project:
            return json.dumps({"error": f"Project {project_id} not found"})

        existing_alert = next(
            (
                a
                for a in budget_alerts
                if a.get("project_id") == project_id
                and a.get("threshold_percentage") == threshold_percentage
                and a.get("active")
            ),
            None,
        )

        if existing_alert:
            return json.dumps(
                {"error": "Similar active alert already exists for this project"}
            )

        alert_id = f"alert_{uuid.uuid4().hex[:8]}"

        new_alert = {
            "alert_id": alert_id,
            "alert_name": alert_name
            or f"{project['name']} - {threshold_percentage}% Budget Alert",
            "project_id": project_id,
            "threshold_percentage": threshold_percentage,
            "alert_recipients": alert_recipients,
            "active": True,
            "triggered": False,
            "last_triggered": None,
            "created_date": datetime.now().isoformat(),
            "alert_type": "budget_threshold",
        }

        budget_alerts.append(new_alert)

        current_budget = next(
            (
                b
                for b in budgets
                if b.get("project_id") == project_id
                and b.get("fiscal_year") == datetime.now().year
            ),
            None,
        )

        current_utilization = 0
        if current_budget:
            current_utilization = round(
                (
                    current_budget.get("spent_amount", 0)
                    / current_budget["total_budget"]
                    * 100
                ),
                2,
            )

        return json.dumps(
            {
                "success": True,
                "budget_alert": new_alert,
                "current_utilization": current_utilization,
                "will_trigger_immediately": current_utilization >= threshold_percentage,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_budget_threshold_alert",
                "description": "Create budget threshold alert for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "threshold_percentage": {
                            "type": "integer",
                            "description": "Budget threshold percentage (50-100)",
                        },
                        "alert_recipients": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee IDs to alert",
                        },
                        "alert_name": {
                            "type": "string",
                            "description": "Custom alert name",
                        },
                    },
                    "required": ["project_id", "alert_recipients"],
                },
            },
        }
