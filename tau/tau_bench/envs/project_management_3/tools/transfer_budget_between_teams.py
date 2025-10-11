# Copyright Sierra

import datetime, uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TransferBudgetBetweenTeams(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], source_team_id, target_team_id, transfer_amount, fiscal_year = datetime.now().year) -> str:

        if not all([source_team_id, target_team_id, transfer_amount]):
            return json.dumps({"error": "All fields are required"})

        teams = data.get("teams", [])
        budgets = data.get("budgets", [])
        budget_transfers = data.get("budget_transfers", [])

        source_team = next(
            (t for t in teams if t.get("team_id") == source_team_id), None
        )
        target_team = next(
            (t for t in teams if t.get("team_id") == target_team_id), None
        )

        if not source_team or not target_team:
            return json.dumps({"error": "Source or target team not found"})

        source_project_id = source_team.get("project_id")
        target_project_id = target_team.get("project_id")

        source_budget = next(
            (
                b
                for b in budgets
                if b.get("project_id") == source_project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        if not source_budget:
            return json.dumps({"error": "No budget found for source team's project"})

        available = (
            source_budget["total_budget"]
            - source_budget.get("spent_amount", 0)
            - source_budget.get("committed_amount", 0)
        )

        if transfer_amount > available * 0.25:
            return json.dumps(
                {
                    "error": f"Transfer amount exceeds 25% of available budget. Maximum allowed: ${available * 0.25}"
                }
            )

        source_dept = source_budget.get("department")
        target_budget = next(
            (
                b
                for b in budgets
                if b.get("project_id") == target_project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        cross_department = False
        if target_budget:
            cross_department = source_dept != target_budget.get("department")

        transfer_id = f"xfer_{uuid.uuid4().hex[:8]}"

        new_transfer = {
            "transfer_id": transfer_id,
            "source_team_id": source_team_id,
            "target_team_id": target_team_id,
            "source_project_id": source_project_id,
            "target_project_id": target_project_id,
            "transfer_amount": transfer_amount,
            "cross_department": cross_department,
            "status": "approved" if not cross_department else "pending_finance_review",
            "created_date": datetime.now().isoformat(),
            "fiscal_year": fiscal_year,
        }

        budget_transfers.append(new_transfer)

        if new_transfer["status"] == "approved":
            source_budget["total_budget"] -= transfer_amount
            if target_budget:
                target_budget["total_budget"] += transfer_amount

        return json.dumps({"success": True, "transfer": new_transfer})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_budget_between_teams",
                "description": "Transfer budget between teams based on their projects",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_team_id": {
                            "type": "string",
                            "description": "Source team ID",
                        },
                        "target_team_id": {
                            "type": "string",
                            "description": "Target team ID",
                        },
                        "transfer_amount": {
                            "type": "number",
                            "description": "Amount to transfer",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": [
                        "source_team_id",
                        "target_team_id",
                        "transfer_amount",
                    ],
                },
            },
        }
