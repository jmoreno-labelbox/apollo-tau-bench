# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RunAndRecordSystemAccessChecksTool(Tool):
    """Checks necessary system access for one or more candidates based on their role and records the results."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, candidate_ids) -> str:

        ids_to_process = []
        if candidate_ids:
            ids_to_process.extend(candidate_ids)
        if candidate_id:
            ids_to_process.append(candidate_id)

        if not ids_to_process:
            return _err("candidate_id or candidate_ids is required.")

        candidates_map = {str(c.get("candidate_id")): c for c in data.get("candidates", [])}
        access_checks = data.setdefault("access_checks", [])
        all_created_records = []

        for cid in ids_to_process:
            candidate = candidates_map.get(cid)
            if not candidate:
                if len(ids_to_process) == 1:
                    return _err(f"Candidate '{cid}' not found.", code="not_found")
                continue

            role_title = candidate.get("role_title", "")
            base_systems = ["Email", "SSO", "Slack"]
            role_specific_systems = ROLE_SYSTEMS_MAP.get(role_title, [])
            systems_to_check = base_systems + role_specific_systems

            created_records = []
            for system_name in systems_to_check:
                status = "Success"
                note_nullable = None
                if (sum(ord(c) for c in cid) + len(system_name)) % 7 == 0:
                    status = "Failed"
                    note_nullable = f"Automated check failed. Code: {sum(ord(c) for c in cid[:5])}."

                new_check = {
                    "candidate_id": cid,
                    "system_name": system_name,
                    "status": status,
                    "note_nullable": note_nullable,
                    "checked_ts": HARD_TS
                }
                access_checks.append(new_check)
                created_records.append(new_check)
            all_created_records.extend(created_records)

        return json.dumps(all_created_records, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "run_and_record_system_access_checks",
                "description": "Checks necessary system access for one or more candidates based on their role and records the results.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "A single target candidate identifier."},
                        "candidate_ids": {"type": "array", "items": {"type": "string"}, "description": "A list of target candidate identifiers."}
                    },
                },
            },
        }
