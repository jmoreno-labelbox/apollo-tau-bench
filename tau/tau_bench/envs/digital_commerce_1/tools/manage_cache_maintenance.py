# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ManageCacheMaintenance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], environment: str, action: str) -> str:
        jobs = _ensure_table(data, "cache_jobs")
        targets = ["Load API Metadata", "Populate Cache Job"]
        job_ids = []
        if action in ("create", "update", "verify"):

            for name in targets:
                jid = _stable_id("job", name, environment)
                job_ids.append(jid)
                row = _find_one(jobs, job_id=jid)
                if action in ("create", "update"):
                    if row:
                        row["job_name"] = name
                        row["last_run_status"] = "Queued"
                        row["last_run_time"] = FIXED_NOW
                    else:
                        jobs.append(
                            {
                                "job_id": jid,
                                "job_name": name,
                                "last_run_status": "Queued",
                                "last_run_time": FIXED_NOW,
                            }
                        )
        if action == "remove":
            for name in targets:
                jid = _stable_id("job", name, environment)
                jobs[:] = [r for r in jobs if r.get("job_id") != jid]
        last = _find_one(jobs, job_name=targets[0])
        return _json(
            {
                "schedule_id": _stable_id("cm", environment),
                "job_ids": job_ids,
                "last_run_status": (last or {}).get("last_run_status", "Unknown"),
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_cache_maintenance",
                "description": "Manage cache maintenance scheduling for an environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {"type": "string", "enum": ["DEV", "UAT", "PROD"]},
                        "action": {
                            "type": "string",
                            "enum": ["create", "update", "remove", "verify"],
                        },
                    },
                    "required": ["environment", "action"],
                },
            },
        }
