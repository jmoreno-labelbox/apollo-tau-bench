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

class ValidateComplianceStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None, required_clearance: str = "secret") -> str:
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

        cleared_resources = 0
        compliance_violations = []

        for allocation in project_allocations:
            employee_id = allocation.get("employee_id")

            employee = None
            for emp in employees.values():
                if emp.get("employee_id") == employee_id:
                    employee = emp
                    break

            if employee:
                employee_clearance = employee.get("clearance")
                if employee_clearance == required_clearance:
                    cleared_resources += 1
                else:
                    compliance_violations.append(
                        {
                            "employee_id": employee_id,
                            "required_clearance": required_clearance,
                            "actual_clearance": employee_clearance,
                        }
                    )

        compliance_achieved = len(compliance_violations) == 0
        payload = {
                "project_id": project_id,
                "required_clearance": required_clearance,
                "compliance_achieved": compliance_achieved,
                "cleared_resources": cleared_resources,
                "total_allocations": len(project_allocations),
                "compliance_violations": compliance_violations,
                "validation_summary": {
                    "status": "compliant" if compliance_achieved else "non_compliant",
                    "cleared_count": cleared_resources,
                    "violation_count": len(compliance_violations),
                },
            }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateComplianceStatus",
                "description": "Validate security clearance compliance for a project and return compliance status",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID to validate",
                        },
                        "required_clearance": {
                            "type": "string",
                            "description": "Required security clearance level (default: secret)",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }
