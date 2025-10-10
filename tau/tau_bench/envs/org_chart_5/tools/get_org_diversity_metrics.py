# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_org_diversity_metrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department_id, level) -> str:

        employees_to_scan = list(data.get("employees", {}).values())
        if department_id:
            employees_to_scan = [
                e for e in employees_to_scan if e.get("department_id") == department_id
            ]
        if level:
            employees_to_scan = [
                e for e in employees_to_scan if e.get("level_id") == level
            ]

        gender_counts = Counter(e.get("gender") for e in employees_to_scan)
        ethnicity_counts = Counter(e.get("ethnicity_code") for e in employees_to_scan)

        metrics = {
            "filter_department": department_id,
            "filter_level": level,
            "total_employees_in_filter": len(employees_to_scan),
            "gender_distribution": dict(gender_counts),
            "ethnicity_distribution": dict(ethnicity_counts),
        }
        return json.dumps(metrics, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_org_diversity_metrics",
                "description": "Return diversity metrics (gender, ethnicity) by department, level, or company-wide.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {"type": "string"},
                        "level": {"type": "string"},
                    },
                },
            },
        }
