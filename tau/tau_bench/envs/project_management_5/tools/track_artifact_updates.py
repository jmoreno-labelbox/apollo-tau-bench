# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TrackArtifactUpdates(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], artifact_type, cr_id, update_description, updated_by, version_after, version_before, update_id = f"au_{uuid.uuid4().hex[:8]}") -> str:

        if not all(
            [cr_id, artifact_type, update_description, version_after, updated_by]
        ):
            return json.dumps(
                {
                    "error": "cr_id, artifact_type, update_description, version_after, and updated_by are required"
                }
            )

        change_requests = list(data.get("change_requests", {}).values())
        artifact_updates = list(data.get("artifact_updates", {}).values())

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        if cr.get("status") != "approved":
            return json.dumps(
                {"error": "Can only update artifacts for approved change requests"}
            )

        artifact_update = {
            "update_id": update_id,
            "cr_id": cr_id,
            "artifact_type": artifact_type,
            "update_description": update_description,
            "version_before": version_before,
            "version_after": version_after,
            "updated_by": updated_by,
            "update_date": datetime.now().isoformat(),
        }

        artifact_updates.append(artifact_update)

        if "artifacts_updated" not in cr:
            cr["artifacts_updated"] = []
        if artifact_type not in cr["artifacts_updated"]:
            cr["artifacts_updated"].append(artifact_type)

        if "artifacts_pending" in cr and artifact_type in cr["artifacts_pending"]:
            cr["artifacts_pending"].remove(artifact_type)

        all_updated = len(cr.get("artifacts_pending", [])) == 0

        return json.dumps(
            {
                "success": True,
                "artifact_update": artifact_update,
                "all_artifacts_updated": all_updated,
                "remaining_artifacts": cr.get("artifacts_pending", []),
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "track_artifact_updates",
                "description": "Track updates to project artifacts after change approval",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "update_id": {"type": "string", "description": "Update ID"},
                        "artifact_type": {
                            "type": "string",
                            "description": "Type: budget, schedule, resource_plan, scope_statement, requirements",
                        },
                        "update_description": {
                            "type": "string",
                            "description": "Description of the update",
                        },
                        "version_before": {
                            "type": "string",
                            "description": "Version before update",
                        },
                        "version_after": {
                            "type": "string",
                            "description": "Version after update",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Person updating the artifact",
                        },
                    },
                    "required": [
                        "cr_id",
                        "artifact_type",
                        "update_description",
                        "version_after",
                        "updated_by",
                    ],
                },
            },
        }
