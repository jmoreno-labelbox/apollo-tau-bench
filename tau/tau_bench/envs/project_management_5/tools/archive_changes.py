# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ArchiveChanges(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        archive_before_date = kwargs.get("archive_before_date")
        archived_by = kwargs.get("archived_by")

        if not all([project_id, archived_by]):
            return json.dumps({"error": "project_id and archived_by are required"})

        change_requests = data.get("change_requests", [])

        if "archived_changes" not in data:
            data["archived_changes"] = []
        archived_changes = data["archived_changes"]

        if not archive_before_date:

            archive_before_date = (datetime.now() - timedelta(days=90)).isoformat()

        to_archive = []
        for cr in change_requests:
            if (
                cr.get("project_id") == project_id
                and cr.get("status") in ["completed", "cancelled", "rejected"]
                and cr.get("updated_date", cr.get("created_date", ""))
                < archive_before_date
            ):

                if cr.get("status") == "completed" or cr.get("status") != "approved":
                    to_archive.append(cr)

        archived_count = 0
        for cr in to_archive:

            archive_entry = cr.copy()
            archive_entry["archived_date"] = datetime.now().isoformat()
            archive_entry["archived_by"] = archived_by

            archived_changes.append(archive_entry)

            cr["archived"] = True
            cr["archive_date"] = datetime.now().isoformat()

            archived_count += 1

        return json.dumps(
            {
                "success": True,
                "archive_summary": {
                    "project_id": project_id,
                    "archived_count": archived_count,
                    "archive_date": datetime.now().isoformat(),
                    "criteria": {
                        "before_date": archive_before_date,
                        "statuses": ["completed", "cancelled", "rejected"],
                    },
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "archive_changes",
                "description": "Archive completed, cancelled, or rejected change requests",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "archive_before_date": {
                            "type": "string",
                            "description": "Archive changes before this date (ISO format)",
                        },
                        "archived_by": {
                            "type": "string",
                            "description": "Person performing the archive",
                        },
                    },
                    "required": ["project_id", "archived_by"],
                },
            },
        }
