# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2CalculateProjectProfitability(Tool):
    """Calculate profitability metrics for projects."""

    @staticmethod
    def invoke(data: Dict[str, Any], project_id) -> str:

        if not project_id:
            return _error("project_id is required.")

        # Retrieve project information.
        projects = list(data.get("projects", {}).values())
        project = _find_one(projects, "project_id", project_id)
        if not project:
            return _error(f"Project '{project_id}' not found.")

        # Compute revenue based on invoices.
        invoice_lines = data.get("invoice_lines", [])
        project_lines = _find_all(invoice_lines, "project_id", project_id)
        total_revenue = sum(line.get("line_amount", 0) for line in project_lines)
        total_hours = sum(line.get("hours_billed", 0) for line in project_lines)

        # Determine the effective hourly wage.
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
