from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetLicenseAssignments(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str | None = None,
        account_id: str | None = None,
    ) -> str:
        pass
        results: list[dict[str, Any]] = []
        for a in data["license_assignments"].values():
            if employee_id and a["employee_id"] != employee_id:
                continue
            if account_id and a["account_id"] != account_id:
                continue
            results.append(a)
        payload = {"status": "ok", "assignments": results}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLicenseAssignments",
                "description": "List license assignments filtered by employee_id or account_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "account_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
