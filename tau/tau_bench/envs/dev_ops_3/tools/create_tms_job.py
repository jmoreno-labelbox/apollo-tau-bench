from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class create_tms_job(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        job_name: str,
        source_locale: str,
        target_locales: list[str],
        string_keys: list[str],
    ) -> str:
        pass
        tms_jobs = data.get("tms_jobs", [])
        existing_ids = [job["id"] for job in tms_jobs]
        new_id = _get_next_id("tms_job", existing_ids)

        new_job = {
            "id": new_id,
            "tms_project_id": project_id,
            "job_name": job_name,
            "job_type": "translation",
            "status": "pending",
            "created_at": FIXED_TIMESTAMP,
            "started_at": None,
            "completed_at": None,
            "total_segments": len(string_keys) * len(target_locales),
            "completed_segments": 0,
            "assigned_translators": [],
            "assigned_reviewers": [],
            "source_locale": source_locale,
            "target_locales": target_locales,
            "priority": "medium",
            "due_date": None,
            "metadata": {"string_keys": string_keys},
        }

        tms_jobs.append(new_job)
        data["tms_jobs"] = tms_jobs
        payload = {"success": f"Created TMS job '{new_id}'.", "tms_job_id": new_id}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTmsJob",
                "description": "Creates a new job in the Translation Management System (TMS).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "job_name": {"type": "string"},
                        "source_locale": {"type": "string"},
                        "target_locales": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "string_keys": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "project_id",
                        "job_name",
                        "source_locale",
                        "target_locales",
                        "string_keys",
                    ],
                },
            },
        }
