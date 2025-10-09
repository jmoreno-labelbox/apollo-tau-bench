from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class get_org_diversity_metrics(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_id: str = None, level: str = None) -> str:
        employees_to_scan = data.get("employees", {}).values()
        if department_id:
            employees_to_scan = [
                e for e in employees_to_scan.values() if e.get("department_id") == department_id
            ]
        if level:
            employees_to_scan = [
                e for e in employees_to_scan.values() if e.get("level_id") == level
            ]

        gender_counts = Counter(e.get("gender") for e in employees_to_scan.values())
        ethnicity_counts = Counter(e.get("ethnicity_code") for e in employees_to_scan.values())

        metrics = {
            "filter_department": department_id,
            "filter_level": level,
            "total_employees_in_filter": len(employees_to_scan),
            "gender_distribution": dict(gender_counts),
            "ethnicity_distribution": dict(ethnicity_counts),
        }
        payload = metrics
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrgDiversityMetrics",
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
