from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class TrackArtifactUpdates(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cr_id: str,
        artifact_type: str,
        update_description: str,
        version_after: str,
        updated_by: str,
        version_before: str = None,
        update_id: str = None
    ) -> str:
        if not all(
            [cr_id, artifact_type, update_description, version_after, updated_by]
        ):
            payload = {
                "error": "cr_id, artifact_type, update_description, version_after, and updated_by are required"
            }
            out = json.dumps(payload)
            return out

        change_requests = data.get("change_requests", {}).values()
        artifact_updates = data.get("artifact_updates", {}).values()

        cr = next((c for c in change_requests.values() if c.get("cr_id") == cr_id), None)
        if not cr:
            payload = {"error": f"Change request '{cr_id}' not found"}
            out = json.dumps(payload)
            return out

        if cr.get("status") != "approved":
            payload = {"error": "Can only update artifacts for approved change requests"}
            out = json.dumps(payload)
            return out

        update_id = update_id or f"au_{uuid.uuid4().hex[:8]}"

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

        data["artifact_updates"][artifact_update["artifact_update_id"]] = artifact_update

        if "artifacts_updated" not in cr:
            cr["artifacts_updated"] = []
        if artifact_type not in cr["artifacts_updated"]:
            cr["artifacts_updated"].append(artifact_type)

        if "artifacts_pending" in cr and artifact_type in cr["artifacts_pending"]:
            cr["artifacts_pending"].remove(artifact_type)

        all_updated = len(cr.get("artifacts_pending", [])) == 0
        payload = {
            "success": True,
            "artifact_update": artifact_update,
            "all_artifacts_updated": all_updated,
            "remaining_artifacts": cr.get("artifacts_pending", []),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TrackArtifactUpdates",
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
