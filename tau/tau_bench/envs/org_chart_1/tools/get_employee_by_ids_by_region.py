# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_employee_by_ids_by_region(Tool):
    REGION_MAP: Dict[str, Set[str]] = {
        "EU": {
            "AT",
            "BE",
            "BG",
            "HR",
            "CY",
            "CZ",
            "DK",
            "EE",
            "FI",
            "FR",
            "DE",
            "GR",
            "HU",
            "IE",
            "IT",
            "LV",
            "LT",
            "LU",
            "MT",
            "NL",
            "PL",
            "PT",
            "RO",
            "SK",
            "SI",
            "ES",
            "SE",
        }
    }

    @staticmethod
    def invoke(data: Dict[str, Any], region, status = "Active") -> str:
        status_filter = status

        if not region or region not in get_employee_by_ids_by_region.REGION_MAP:
            return json.dumps(
                {"error": f"Invalid or unsupported region: {region}"}, indent=2
            )

        employees = list(data.get("employees", {}).values())
        target_nationalities = get_employee_by_ids_by_region.REGION_MAP[region]

        found_employees = [
            emp
            for emp in employees
            if emp.get("nationality") in target_nationalities
            and emp.get("status") == status_filter
        ]

        return json.dumps(found_employees, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_by_ids_by_region",
                "description": "Retrieves a list of employees belonging to a specific geographical or political region (e.g., EU).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "region": {
                            "type": "string",
                            "description": "The geographical or political region to search for.",
                            "enum": ["EU"],
                        },
                        "status": {
                            "type": "string",
                            "description": "The employment status to filter by. Defaults to 'Active'.",
                        },
                    },
                    "required": ["region"],
                },
            },
        }
