from tau_bench.envs.tool import Tool
import json
from typing import Any

class CollectSubjectSnapshot(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cache_jobs: list[dict[str, Any]] = None,
        orders: list[dict[str, Any]] = None,
        order_items: list[dict[str, Any]] = None,
        accounts: list[dict[str, Any]] = None,
        aws_security_group_rules: list[dict[str, Any]] = None,
        connected_apps: list[dict[str, Any]] = None,
        cases: list[dict[str, Any]] = None,
        subject_id: str = None
    ) -> str:
        def is_org_catalog(s: str) -> bool:
            pass
            return ":" in s and len(s.split(":", 1)[0]) > 0

        def org_from(s: str) -> str:
            pass
            return s.split(":", 1)[0]

        def cat_from(s: str) -> str:
            pass
            return s.split(":", 1)[1]

        #data collections
        cache_jobs = cache_jobs or []
        orders = orders or []
        items = order_items or []
        accounts = accounts or []
        sgs = aws_security_group_rules or []
        apps = connected_apps or []
        cases = cases or []

        details: dict[str, Any] = {"subject_id": subject_id}

        if is_org_catalog(subject_id):
            org_id = org_from(subject_id)
            #policy mandates two jobs
            required = {"Load API Metadata", "Populate Cache Job"}
            org_jobs = [j for j in cache_jobs.values() if j.get("org_id") == org_id]
            found = {j.get("job_name") for j in org_jobs}
            details.update(
                {
                    "org_id": org_id,
                    "has_required_sequence": required.issubset(found),
                    "present_jobs": sorted(list(found)),
                    "last_run_times": {
                        j["job_name"]: j.get("last_run_time") for j in org_jobs
                    },
                }
            )

        elif subject_id.startswith("00D8"):  #appears to be an organization identifier
            org_jobs = [j for j in cache_jobs.values() if j.get("org_id") == subject_id]
            details.update(
                {
                    "org_id": subject_id,
                    "job_count": len(org_jobs),
                    "job_names": sorted({j.get("job_name") for j in org_jobs}),
                    "last_run_times": {
                        j["job_name"]: j.get("last_run_time") for j in org_jobs
                    },
                }
            )

        elif subject_id.isdigit():  #order or case (these are numeric in your dataset)
            #is it an order?
            o = next((o for o in orders if o.get("order_id") == subject_id), None)
            if o:
                its = [li for li in items.values() if li.get("order_id") == subject_id]
                acct = next(
                    (a for a in accounts if a.get("account_id") == o.get("account_id")),
                    None,
                )
                details.update(
                    {
                        "kind": "order",
                        "status": o.get("status"),
                        "subtotal": o.get("subtotal"),
                        "discount_amount": o.get("discount_amount"),
                        "total_amount": o.get("total_amount"),
                        "item_count": len(its),
                        "account_type": acct.get("type") if acct else None,
                    }
                )
            else:
                c = next((c for c in cases if c.get("case_id") == subject_id), None)
                details.update(
                    {
                        "kind": "case",
                        "status": c.get("status") if c else None,
                        "resolution": c.get("resolution") if c else None,
                    }
                )

        elif subject_id.startswith("sg-"):  #identifier for the security group
            grp = [r for r in sgs.values() if r.get("security_group_id") == subject_id]
            has_public_redis = any(
                r.get("port") == 6379
                and r.get("protocol") == "TCP"
                and r.get("source_ip") == "0.0.0.0/0"
                for r in grp
            )
            details.update(
                {
                    "security_group_id": subject_id,
                    "rule_count": len(grp),
                    "has_public_redis": has_public_redis,
                }
            )

        else:  #presume app_id (for instance, "203")
            app = next((a for a in apps if a.get("app_id") == subject_id), None)
            scopes = app.get("oauth_scopes") if app else []
            if isinstance(scopes, str):
                scopes = [x.strip() for x in scopes.split(",") if x.strip()]
            details.update(
                {
                    "app_id": subject_id,
                    "scope_count": len(scopes),
                    "has_required_scopes": all(
                        s in scopes for s in ("api", "refresh_token")
                    ),
                }
            )

        #Transfer to workspace and conduct a self-review
        _ws_append(data, subject_id, "SNAPSHOT_COLLECTED", details)
        _append_audit(data, "SNAPSHOT_COLLECTED", subject_id, {"ok": True})
        payload = details
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CollectSubjectSnapshot",
                "description": "Collect a deterministic read-only snapshot of a subject (order, case, org, org:catalog, security group, connected app) for evidence-only use.",
                "parameters": {
                    "type": "object",
                    "properties": {"subject_id": {"type": "string"}},
                    "required": ["subject_id"],
                },
            },
        }
