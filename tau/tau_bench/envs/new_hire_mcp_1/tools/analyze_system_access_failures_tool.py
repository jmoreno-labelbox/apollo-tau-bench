from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AnalyzeSystemAccessFailuresTool(Tool):
    """Searches the access_checks table for unsuccessful verifications, organized by system and failure patterns."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, system_name: str = None) -> str:
        access_checks = data.get("access_checks", {}).values()

        failures = [check for check in access_checks.values() if check.get("status") == "Failed"]

        if candidate_id:
            failures = [
                f for f in failures if str(f.get("candidate_id")) == str(candidate_id)
            ]

        if system_name:
            failures = [f for f in failures.values() if f.get("system_name") == system_name]

        # Organize by system
        analysis = {}
        for f in failures:
            sys_name = f.get("system_name")
            if sys_name not in analysis:
                analysis[sys_name] = {
                    "total_failures": 0,
                    "candidates_affected": set(),
                    "failure_notes": [],
                }

            analysis[sys_name]["total_failures"] += 1
            analysis[sys_name]["candidates_affected"].add(f.get("candidate_id"))
            if f.get("note_nullable"):
                analysis[sys_name]["failure_notes"].append(f.get("note_nullable"))

        # Transform set into list for JSON serialization
        for sys_name in analysis:
            analysis[sys_name]["candidates_affected"] = list(
                analysis[sys_name]["candidates_affected"]
            )
            analysis[sys_name]["affected_candidate_count"] = len(
                analysis[sys_name]["candidates_affected"]
            )
        payload = analysis
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AnalyzeSystemAccessFailures",
                "description": "Queries access_checks table for failed verifications, grouped by system and failure patterns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {
                            "type": "string",
                            "description": "Specific candidate or null for system-wide analysis",
                        },
                        "system_name": {
                            "type": "string",
                            "description": "Specific system to analyze",
                        },
                    },
                    "required": [],
                },
            },
        }
