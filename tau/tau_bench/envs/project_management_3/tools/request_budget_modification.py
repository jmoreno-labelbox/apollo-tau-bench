# Copyright Sierra

import datetime, uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RequestBudgetModification(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], justification, modification_amount, modification_type, project_id, requestor_id, fiscal_year = datetime.now().year) -> str:

        if not all(
            [
                project_id,
                modification_amount,
                modification_type,
                justification,
                requestor_id,
            ]
        ):
            return json.dumps({"error": "All fields are required"})

        budget_modifications = data.get("budget_modifications", [])
        budgets = data.get("budgets", [])

        current_budget = next(
            (
                b
                for b in budgets
                if b.get("project_id") == project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        if not current_budget:
            return json.dumps(
                {"error": f"No active budget found for project {project_id}"}
            )

        current_overrun = (
            current_budget.get("spent_amount", 0) / current_budget["total_budget"] - 1
        ) * 100
        is_emergency = (
            current_overrun > 10
            and current_overrun <= 15
            and modification_type == "increase"
        )

        modification_id = f"mod_{uuid.uuid4().hex[:8]}"

        new_modification = {
            "modification_id": modification_id,
            "project_id": project_id,
            "current_budget": current_budget["total_budget"],
            "modification_amount": modification_amount,
            "modification_type": modification_type,
            "new_budget": current_budget["total_budget"] + modification_amount
            if modification_type == "increase"
            else current_budget["total_budget"] - modification_amount,
            "justification": justification,
            "requestor_id": requestor_id,
            "status": "pending_approval",
            "requires_approval": ["project_sponsor", "finance_director"],
            "is_emergency": is_emergency,
            "created_date": datetime.now().isoformat(),
            "fiscal_year": fiscal_year,
        }

        budget_modifications.append(new_modification)

        result = {"success": True, "modification_request": new_modification}

        if is_emergency:
            result[
                "info"
            ] = "Emergency modification - can be approved retroactively within 48 hours"

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "request_budget_modification",
                "description": "Request a budget increase or decrease",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "modification_amount": {
                            "type": "number",
                            "description": "Amount to modify",
                        },
                        "modification_type": {
                            "type": "string",
                            "description": "increase or decrease",
                        },
                        "justification": {
                            "type": "string",
                            "description": "Justification for modification",
                        },
                        "requestor_id": {
                            "type": "string",
                            "description": "Employee requesting modification",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": [
                        "project_id",
                        "modification_amount",
                        "modification_type",
                        "justification",
                        "requestor_id",
                    ],
                },
            },
        }
