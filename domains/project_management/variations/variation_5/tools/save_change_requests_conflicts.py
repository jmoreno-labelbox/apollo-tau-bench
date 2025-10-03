from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta
from typing import Any

class SaveChangeRequestsConflicts(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cr_id: str = None,
        conflicting_cr_id: str = None,
        conflict_type: str = None,
        conflicting_deliverables: list = None,
        severity: str = None,
        rule_violation: str = None,
        action_required: str = None,
        recommendation: str = None
,
    type: Any = None,
    ) -> str:
        if not cr_id or not conflicting_cr_id:
            payload = {"error": "cr_id and conflicting_cr_id are required parameters"}
            out = json.dumps(payload)
            return out

        conflict_cr_id_1 = {
            "conflicting_cr_id": conflicting_cr_id,
            "conflict_id": f"cf_{uuid.uuid4().hex[:8]}",
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
                payload = {"success": True}
                out = json.dumps(payload)
                return out

            elif change_request.get("cr_id") == conflicting_cr_id:
                conflict_cr_id_2 = conflict_cr_id_1.copy()
                conflict_cr_id_2["conflicting_cr_id"] = cr_id
                if "conflicts" in change_request:
                    change_request["conflicts"].append(conflict_cr_id_2)
                else:
                    change_request["conflicts"] = [conflict_cr_id_2]
        payload = {"error": f"It wasn't found any change request with the ID {cr_id}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SaveChangeRequestsConflicts",
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
                            "type": "list",
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
                        },
                    },
                    "required": ["cr_id", "conflicting_cr"],
                },
            },
        }
