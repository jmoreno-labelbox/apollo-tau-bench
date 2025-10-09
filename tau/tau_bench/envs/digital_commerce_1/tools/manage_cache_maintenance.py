from tau_bench.envs.tool import Tool
import json
from typing import Any

class ManageCacheMaintenance(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], environment: str, action: str) -> str:
        jobs = _ensure_table(data, "cache_jobs")
        # Structure maintenance as two designated tasks
        targets = ["Load API Metadata", "Populate Cache Job"]
        job_ids = []
        if action in ("create", "update", "verify"):
            status = (
                "Queued"
                if action != "verify"
                else (_find_one(jobs, job_name=targets[0]) or {}).get(
                    "last_run_status", "Unknown"
                )
            )
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
                jobs[:] = [r for r in jobs.values() if r.get("job_id") != jid]
        last = _find_one(jobs, job_name=targets[0])
        return _json(
            {
                "schedule_id": _stable_id("cm", environment),
                "job_ids": job_ids,
                "last_run_status": (last or {}).get("last_run_status", "Unknown"),
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageCacheMaintenance",
                "description": "Manage cache maintenance scheduling for an environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                        "action": {
                            "type": "string",
                            "enum": ["create", "update", "remove", "verify"],
                        },
                    },
                    "required": ["environment", "action"],
                },
            },
        }
