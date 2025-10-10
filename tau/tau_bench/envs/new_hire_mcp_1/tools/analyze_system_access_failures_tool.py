# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AnalyzeSystemAccessFailuresTool(Tool):
    """Queries access_checks table for failed verifications, grouped by system and failure patterns."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        system_name = kwargs.get("system_name")

        access_checks = data.get("access_checks", [])

        failures = [check for check in access_checks if check.get("status") == "Failed"]

        if candidate_id:
            failures = [f for f in failures if str(f.get("candidate_id")) == str(candidate_id)]

        if system_name:
            failures = [f for f in failures if f.get("system_name") == system_name]

        # Categorize by system
        analysis = {}
        for f in failures:
            sys_name = f.get("system_name")
            if sys_name not in analysis:
                analysis[sys_name] = {
                    "total_failures": 0,
                    "candidates_affected": set(),
                    "failure_notes": []
                }

            analysis[sys_name]["total_failures"] += 1
            analysis[sys_name]["candidates_affected"].add(f.get("candidate_id"))
            if f.get("note_nullable"):
                analysis[sys_name]["failure_notes"].append(f.get("note_nullable"))

        # Transform the set into a list for JSON encoding.
        for sys_name in analysis:
            analysis[sys_name]["candidates_affected"] = list(analysis[sys_name]["candidates_affected"])
            analysis[sys_name]["affected_candidate_count"] = len(analysis[sys_name]["candidates_affected"])

        return json.dumps(analysis, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyze_system_access_failures",
                "description": "Queries access_checks table for failed verifications, grouped by system and failure patterns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "Specific candidate or null for system-wide analysis"},
                        "system_name": {"type": "string", "description": "Specific system to analyze"}
                    },
                    "required": [],
                },
            },
        }
