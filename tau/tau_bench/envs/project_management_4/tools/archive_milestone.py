from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ArchiveMilestone(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], milestone_id: str = None) -> str:
        if not milestone_id:
            payload = {"error": "milestone_id is required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", [])
        archived_milestones = data.get("archived_milestones", [])

        milestone_index = None
        milestone_to_archive = None
        for i, milestone in enumerate(milestones):
            if milestone.get("milestone_id") == milestone_id:
                milestone_index = i
                milestone_to_archive = milestone
                break

        if not milestone_to_archive:
            payload = {"error": f"Milestone '{milestone_id}' not found"}
            out = json.dumps(payload)
            return out

        if milestone_to_archive.get("status") != "completed":
            payload = {"error": "Only completed milestones can be archived"}
            out = json.dumps(payload)
            return out

        milestones.pop(milestone_index)

        milestone_to_archive["archived_date"] = datetime.now(timezone.utc).isoformat()
        archived_milestones.append(milestone_to_archive)
        payload = {
                "success": True,
                "archived_milestone": {
                    "milestone_id": milestone_to_archive.get("milestone_id"),
                    "milestone_name": milestone_to_archive.get("milestone_name"),
                    "archived_date": milestone_to_archive.get("archived_date"),
                },
            }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ArchiveMilestone",
                "description": "Archive a completed milestone",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID to archive",
                        },
                    },
                    "required": ["milestone_id"],
                },
            },
        }
