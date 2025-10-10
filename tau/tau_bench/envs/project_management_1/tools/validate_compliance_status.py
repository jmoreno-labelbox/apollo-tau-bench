# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateComplianceStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id, required_clearance = "secret") -> str:

        if not project_id:
            return json.dumps({"error": "project_id is required"})

        allocations = data.get("allocations", [])
        employees = list(data.get("employees", {}).values())

        project_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("project_id") == project_id and alloc.get("status") == "active"
        ]

        cleared_resources = 0
        compliance_violations = []

        for allocation in project_allocations:
            employee_id = allocation.get("employee_id")

            employee = None
            for emp in employees:
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

        return json.dumps(
            {
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
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_compliance_status",
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
