from tau_bench.envs.tool import Tool
import json
from typing import Any

class get_employee_by_ids_by_region(Tool):
    REGION_MAP: dict[str, set[str]] = {
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
            "ESP",
            "SE",
        }
    }

    @staticmethod
    def invoke(data: dict[str, Any], region: str = None, status: str = "Active") -> str:
        if not region or region not in get_employee_by_ids_by_region.REGION_MAP:
            payload = {"error": f"Invalid or unsupported region: {region}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        employees = data.get("employees", [])
        target_nationalities = get_employee_by_ids_by_region.REGION_MAP[region]

        found_employees = [
            emp
            for emp in employees
            if emp.get("nationality") in target_nationalities
            and emp.get("status") == status
        ]
        payload = found_employees
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getEmployeeByIdsByRegion",
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
