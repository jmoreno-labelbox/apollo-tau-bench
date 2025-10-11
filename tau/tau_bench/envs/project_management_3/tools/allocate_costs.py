# Copyright Sierra

import datetime, uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AllocateCosts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], allocator_id, expense_id, allocation_splits = [], fiscal_year = datetime.now().year) -> str:

        if not all([expense_id, allocation_splits, allocator_id]):
            return json.dumps(
                {
                    "error": "expense_id, allocation_splits, and allocator_id are required"
                }
            )

        expenses = data.get("expenses", [])
        cost_allocations = data.get("cost_allocations", [])
        budgets = data.get("budgets", [])

        expense = next((e for e in expenses if e.get("expense_id") == expense_id), None)
        if not expense:
            return json.dumps({"error": f"Expense {expense_id} not found"})

        total_percentage = sum(
            split.get("percentage", 0) for split in allocation_splits
        )
        if abs(total_percentage - 100) > 0.01:
            return json.dumps(
                {
                    "error": f"Allocations must sum to 100%, currently {total_percentage}%"
                }
            )

        total_allocated = sum(split.get("amount", 0) for split in allocation_splits)
        if abs(total_allocated - expense["amount"]) > 0.01:
            return json.dumps(
                {
                    "error": f"Allocated amounts must match expense total ${expense['amount']}"
                }
            )

        allocation_id = f"alloc_{uuid.uuid4().hex[:8]}"

        new_allocation = {
            "allocation_id": allocation_id,
            "expense_id": expense_id,
            "original_amount": expense["amount"],
            "allocation_splits": allocation_splits,
            "allocated_by": allocator_id,
            "allocation_date": datetime.now().isoformat(),
            "status": "completed",
        }

        cost_allocations.append(new_allocation)

        for split in allocation_splits:
            budget = next(
                (
                    b
                    for b in budgets
                    if b.get("project_id") == split["project_id"]
                    and b.get("fiscal_year") == fiscal_year
                ),
                None,
            )
            if budget:
                budget["spent_amount"] = budget.get("spent_amount", 0) + split["amount"]
                budget["last_modified"] = datetime.now().isoformat()

        unallocated = [
            e
            for e in expenses
            if e.get("expense_id")
            not in [a.get("expense_id") for a in cost_allocations]
            and e.get("amount", 0) > 10000
        ]

        result = {"success": True, "allocation": new_allocation}

        if unallocated:
            result[
                "warning"
            ] = f"{len(unallocated)} expenses over $10,000 remain unallocated"

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "allocate_costs",
                "description": "Allocate costs across multiple projects",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expense_id": {
                            "type": "string",
                            "description": "Expense ID to allocate",
                        },
                        "allocation_splits": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "project_id": {"type": "string"},
                                    "percentage": {"type": "number"},
                                    "amount": {"type": "number"},
                                },
                            },
                            "description": "List of allocation splits",
                        },
                        "allocator_id": {
                            "type": "string",
                            "description": "Employee performing allocation",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": ["expense_id", "allocation_splits", "allocator_id"],
                },
            },
        }
