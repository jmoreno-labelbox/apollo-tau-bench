from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SummarizeProjectPhaseMetrics(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        allocations = data.get("allocations", {}).values()
        employees = data.get("employees", {}).values()

        project_allocations = [
            alloc
            for alloc in allocations.values() if alloc.get("project_id") == project_id and alloc.get("status") == "active"
        ]

        dev_hours = 0
        qa_hours = 0

        dev_keywords = [
            "developer",
            "dev",
            "architect",
            "engineer",
            "programmer",
            "coder",
        ]
        qa_keywords = ["qa", "test", "quality", "tester"]

        for allocation in project_allocations:
            employee_id = allocation.get("employee_id")
            role = allocation.get("role", "").lower()
            hours = allocation.get("hours_per_week", 0)

            employee = next(
                (emp for emp in employees.values() if emp.get("employee_id") == employee_id),
                None,
            )

            is_dev_role = False
            is_qa_role = False

            for keyword in dev_keywords:
                if keyword in role and "qa" not in role and "test" not in role:
                    is_dev_role = True
                    break

            for keyword in qa_keywords:
                if keyword in role:
                    is_qa_role = True
                    break

            if not is_dev_role and not is_qa_role and employee:
                emp_role = employee.get("role", "").lower()
                emp_dept = employee.get("department", "").lower()

                for keyword in dev_keywords:
                    if (
                        keyword in emp_role
                        and "qa" not in emp_role
                        and "test" not in emp_role
                    ):
                        is_dev_role = True
                        break

                for keyword in qa_keywords:
                    if keyword in emp_role or keyword in emp_dept:
                        is_qa_role = True
                        break

                if emp_dept == "engineering" and not is_qa_role:
                    is_dev_role = True
                elif emp_dept == "qa":
                    is_qa_role = True

            if is_dev_role:
                dev_hours += hours
            elif is_qa_role:
                qa_hours += hours
        payload = {
                "project_id": project_id,
                "dev_hours": dev_hours,
                "qa_hours": qa_hours,
                "total_allocations": len(project_allocations),
                "phase_transition_summary": {
                    "development_hours": dev_hours,
                    "qa_testing_hours": qa_hours,
                    "status": "calculated",
                },
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SummarizeProjectPhaseMetrics",
                "description": "Calculate and summarize development and QA hours for a project phase transition",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID to analyze",
                        }
                    },
                    "required": ["project_id"],
                },
            },
        }
