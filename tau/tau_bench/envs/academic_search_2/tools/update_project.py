from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateProject(Tool):
    """Modifies the status, collaborators, linked articles, or funding source of an existing project."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        project_id: Any = None,
        project_name: str = None,
        status: str = None,
        end_date: str = None,
        funding_source_id: Any = None,
        linked_articles: Any = None,
        add_collaborators: Any = None
    ) -> str:
        project_id = project_id
        if not project_id:
            payload = {"error": "project_id is required."}
            out = json.dumps(payload)
            return out
        project = next(
            (p for p in data.get("projects", []) if p.get("project_id") == project_id),
            None,
        )
        if not project:
            payload = {"error": "Project not found."}
            out = json.dumps(payload)
            return out

        standard_updatable_fields = [
            "project_name",
            "status",
            "end_date",
            "funding_source_id",
        ]
        for key, value in {
            "project_name": project_name,
            "status": status,
            "end_date": end_date,
            "funding_source_id": funding_source_id,
        }.items():
            if key in standard_updatable_fields:
                project[key] = value

        if linked_articles is not None:
            project["linked_articles"] = linked_articles

        if add_collaborators is not None:
            if "collaborators" not in project:
                project["collaborators"] = []

            provided_collaborators = add_collaborators
            users = data.get("users", [])

            valid_collaborator_ids = []
            for collab_item in provided_collaborators:
                # Verify if the item is a valid user_id
                if any(u["person_id"] == collab_item for u in users):
                    valid_collaborator_ids.append(collab_item)
                # If not, attempt to search by name
                else:
                    found_user = next(
                        (u for u in users if u["name"] == collab_item), None
                    )
                    if found_user:
                        valid_collaborator_ids.append(found_user["user_id"])

            existing_collaborators = set(project.get("collaborators", []))
            updated_collaborators = sorted(
                list(existing_collaborators.union(set(valid_collaborator_ids)))
            )
            project["collaborators"] = updated_collaborators
        payload = {"success": True, "project": project}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProject",
                "description": "Updates a project's details, such as status, collaborators, linked articles, or funding.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "status": {"type": "string"},
                        "project_name": {"type": "string"},
                        "add_collaborators": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "funding_source_id": {"type": "string"},
                        "linked_articles": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }
