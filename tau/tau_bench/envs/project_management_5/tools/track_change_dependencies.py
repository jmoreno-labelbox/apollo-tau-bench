# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TrackChangeDependencies(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cr_id, blocks = [], depends_on = []) -> str:

        if not cr_id:
            return json.dumps({"error": "cr_id is required"})

        change_requests = list(data.get("change_requests", {}).values())

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        for dep_id in depends_on:
            if not any(c.get("cr_id") == dep_id for c in change_requests):
                return json.dumps({"error": f"Dependency CR '{dep_id}' not found"})

        for block_id in blocks:
            if not any(c.get("cr_id") == block_id for c in change_requests):
                return json.dumps({"error": f"Blocked CR '{block_id}' not found"})

        def has_circular_dependency(start_id, check_id, visited=None):
            if visited is None:
                visited = set()
            if start_id in visited:
                return True
            visited.add(start_id)

            cr_to_check = next(
                (c for c in change_requests if c.get("cr_id") == start_id), None
            )
            if not cr_to_check:
                return False

            for dep_id in cr_to_check.get("depends_on", []):
                if dep_id == check_id:
                    return True
                if has_circular_dependency(dep_id, check_id, visited):
                    return True
            return False

        for dep_id in depends_on:
            if has_circular_dependency(dep_id, cr_id):
                return json.dumps(
                    {
                        "error": f"Adding dependency on '{dep_id}' would create a circular dependency"
                    }
                )

        if "depends_on" not in cr:
            cr["depends_on"] = []
        if "blocks" not in cr:
            cr["blocks"] = []

        cr["depends_on"].extend([d for d in depends_on if d not in cr["depends_on"]])
        cr["blocks"].extend([b for b in blocks if b not in cr["blocks"]])

        for block_id in blocks:
            blocked_cr = next(
                (c for c in change_requests if c.get("cr_id") == block_id), None
            )
            if blocked_cr:
                if "blocked_by" not in blocked_cr:
                    blocked_cr["blocked_by"] = []
                if cr_id not in blocked_cr["blocked_by"]:
                    blocked_cr["blocked_by"].append(cr_id)

                if (
                    blocked_cr.get("status") == "pending_approval"
                    and cr.get("status") != "completed"
                ):
                    blocked_cr["dependency_hold"] = True

        can_proceed = True
        blocking_crs = []
        for dep_id in cr.get("depends_on", []):
            dep_cr = next(
                (c for c in change_requests if c.get("cr_id") == dep_id), None
            )
            if dep_cr and dep_cr.get("status") not in [
                "completed",
                "approved",
                "in_implementation",
            ]:
                can_proceed = False
                blocking_crs.append({"cr_id": dep_id, "status": dep_cr.get("status")})

        return json.dumps(
            {
                "success": True,
                "dependencies": {
                    "cr_id": cr_id,
                    "depends_on": cr.get("depends_on", []),
                    "blocks": cr.get("blocks", []),
                    "can_proceed": can_proceed,
                    "blocking_crs": blocking_crs,
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "track_change_dependencies",
                "description": "Track dependencies between change requests",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "depends_on": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "CRs this change depends on",
                        },
                        "blocks": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "CRs blocked by this change",
                        },
                    },
                    "required": ["cr_id"],
                },
            },
        }
