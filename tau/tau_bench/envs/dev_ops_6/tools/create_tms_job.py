from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateTmsJob(Tool):
    """Establish a basic TMS job entry (deterministic; will error on duplicate id)."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: str = None,
        tms_project_id: str = "proj_001",
        job_name: str = None,
        job_type: str = "translation",
        created_at: str = FIXED_TS,
        total_segments: int = 0,
        assigned_translators: list = None,
        assigned_reviewers: list = None,
        source_locale: str = "en",
        target_locales: list = None,
        priority: str = "medium",
        due_date: str = None,
        metadata: dict = None
    ) -> str:
        if assigned_translators is None:
            assigned_translators = []
        if assigned_reviewers is None:
            assigned_reviewers = []
        if target_locales is None:
            target_locales = []
        if metadata is None:
            metadata = {}

        jobs = _table(data, "tms_jobs")
        jid = id
        if not jid:
            jid = f"tms_job_{len(jobs) + 1:04d}"

        if any(j.get("id") == jid for j in jobs.values()):
            return _err(f"TMS job id {jid} already exists")
        job = {
            "id": jid,
            "tms_project_id": tms_project_id,
            "job_name": job_name or f"tms_job_{jid}",
            "job_type": job_type,
            "status": "queued",
            "created_at": created_at,
            "started_at": None,
            "completed_at": None,
            "total_segments": total_segments,
            "completed_segments": 0,
            "assigned_translators": assigned_translators,
            "assigned_reviewers": assigned_reviewers,
            "source_locale": source_locale,
            "target_locales": target_locales,
            "priority": priority,
            "due_date": due_date,
            "metadata": metadata,
        }
        jobs.append(job)
        return _ok({"tms_job": job})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createTmsJob",
                "description": "Create a queued TMS job with deterministic fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "tms_project_id": {"type": "string"},
                        "job_name": {"type": "string"},
                        "job_type": {"type": "string"},
                        "source_locale": {"type": "string"},
                        "target_locales": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "priority": {"type": "string"},
                        "due_date": {"type": "string"},
                        "total_segments": {"type": "integer"},
                        "assigned_translators": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "assigned_reviewers": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "metadata": {"type": "object"},
                    },
                    "required": ["source_locale", "target_locales"],
                },
            },
        }
