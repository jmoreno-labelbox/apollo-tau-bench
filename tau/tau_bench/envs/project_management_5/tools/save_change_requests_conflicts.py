# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SaveChangeRequestsConflicts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        conflicting_cr_id = kwargs.get("conflicting_cr_id")
        conflict_type = kwargs.get("type")
        conflicting_deliverables = kwargs.get("conflicting_deliverables")
        severity = kwargs.get("severity")
        rule_violation = kwargs.get("rule_violation")
        action_required = kwargs.get("action_required")
        recommendation = kwargs.get("recommendation")

        if not cr_id or not conflicting_cr_id:
            return json.dumps({"error": "cr_id and conflicting_cr_id are required parameters"})

        conflict_cr_id_1 = {
            "conflicting_cr_id": conflicting_cr_id,
            "conflict_id": f"cf_{uuid.uuid4().hex[:8]}"
        }
        if conflict_type:
            conflict_cr_id_1["conflict_type"] = conflict_type
        if conflicting_deliverables:
            conflict_cr_id_1["conflicting_deliverables"] = conflicting_deliverables
        if severity:
            conflict_cr_id_1["severity"] = severity
        if rule_violation:
            conflict_cr_id_1["rule_violation"] = rule_violation
        if action_required:
            conflict_cr_id_1["action_required"] = action_required
        if recommendation:
            conflict_cr_id_1["recommendation"] = recommendation

        change_requests = data.get("change_requests", [])
        for change_request in change_requests:
            if change_request.get("cr_id") == cr_id:
                if "conflicts" in change_request:
                    change_request["conflicts"].append(conflict_cr_id_1)
                else:
                    change_request["conflicts"] = [conflict_cr_id_1]

                return json.dumps({"success": True})

            elif change_request.get("cr_id") == conflicting_cr_id:
                conflict_cr_id_2 = conflict_cr_id_1.copy()
                conflict_cr_id_2["conflicting_cr_id"] = cr_id
                if "conflicts" in change_request:
                    change_request["conflicts"].append(conflict_cr_id_2)
                else:
                    change_request["conflicts"] = [conflict_cr_id_2]

        return json.dumps({"error": f"It wasn't found any change request with the ID {cr_id}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "save_change_requests_conflicts",
                "description": "Save conflicts into change requests",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {
                            "type": "string",
                            "description": "Change request ID to save conflicts",
                        },
                        "type": {
                            "type": "string",
                            "description": "Conflict type",
                        },
                        "conflicting_cr_id": {
                            "type": "string",
                            "description": "Conflicting change request ID",
                        },
                        "conflicting_deliverables": {
                            "type": "array",
                            "description": "Conflicting deliverable IDs",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Conflict severity",
                        },
                        "rule_violation": {
                            "type": "string",
                            "description": "Rule violation description",
                        },
                        "action_required": {
                            "type": "string",
                            "description": "Action required description",
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "Recommendation description",
                        }
                    },
                    "required": ["cr_id", "conflicting_cr"],
                },
            },
        }
