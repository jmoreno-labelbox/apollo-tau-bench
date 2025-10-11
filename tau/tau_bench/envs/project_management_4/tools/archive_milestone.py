# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ArchiveMilestone(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], milestone_id) -> str:

        if not milestone_id:
            return json.dumps({"error": "milestone_id is required"})

        milestones = list(data.get("milestones", {}).values())
        archived_milestones = data.get("archived_milestones", [])

        milestone_index = None
        milestone_to_archive = None
        for i, milestone in enumerate(milestones):
            if milestone.get("milestone_id") == milestone_id:
                milestone_index = i
                milestone_to_archive = milestone
                break

        if not milestone_to_archive:
            return json.dumps({"error": f"Milestone '{milestone_id}' not found"})

        if milestone_to_archive.get("status") != "completed":
            return json.dumps({"error": "Only completed milestones can be archived"})

        milestones.pop(milestone_index)

        milestone_to_archive["archived_date"] = datetime.now(timezone.utc).isoformat()
        archived_milestones.append(milestone_to_archive)

        return json.dumps(
            {
                "success": True,
                "archived_milestone": {
                    "milestone_id": milestone_to_archive.get("milestone_id"),
                    "milestone_name": milestone_to_archive.get("milestone_name"),
                    "archived_date": milestone_to_archive.get("archived_date"),
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "archive_milestone",
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
