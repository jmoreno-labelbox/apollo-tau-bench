# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table
def _slugify(text: str, max_len: int = 40) -> str:
    s = str(text).lower()
    out = []
    prev_dash = False
    for ch in s:
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        else:
            if not prev_dash:
                out.append("-")
                prev_dash = True
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug[:max_len] if max_len > 0 else slug


def _stable_id(prefix: str, *parts: str) -> str:
    base = "-".join(_slugify(p) for p in parts if p is not None and str(p) != "")
    return f"{prefix}-{base}" if base else prefix

def _json(x: Any) -> str:
    return json.dumps(x, separators=(",", ":"))

def _find_one(rows: List[Dict[str, Any]], **crit):
    crit_items = sorted(crit.items(), key=lambda kv: kv[0])
    for r in rows:
        match = True
        for k, v in crit_items:
            if str(r.get(k)) != str(v):
                match = False
                break
        if match:
            return r
    return None

def _ensure_table(db: Dict[str, Any], name: str):
    if name not in db:
        db[name] = []
    return db[name]

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