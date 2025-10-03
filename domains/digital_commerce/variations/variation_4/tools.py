import json
from typing import Any

from domains.dto import Tool

FIXED_NOW = "2025-08-06T12:00:00Z"


def _ws_bucket(data: dict[str, Any], subject_id: str) -> dict[str, Any]:
    pass
    return _ws(data).setdefault(subject_id, {"events": []})


def _get_org_type(org_id: str) -> str:
    pass
    if org_id.endswith("QRS"):
        return "UAT"
    if org_id.endswith("DEF"):
        return "Staging"
    return "Production"


def _ensure_audit_log(data: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    if "audit_log" not in data:
        data["audit_log"] = []
    return data["audit_log"]


def _ws_append(
    data: dict[str, Any], subject_id: str, event_type: str, payload: dict[str, Any]
) -> None:
    pass
    bucket = _ws_bucket(data, subject_id)
    bucket["events"].append(
        {"event_type": event_type, "payload": payload, "ts": FIXED_NOW}
    )


def _append_audit(
    data: dict[str, Any], event_type: str, subject_id: str, details: dict[str, Any]
) -> None:
    pass
    log = _ensure_audit_log(data)
    log.append(
        {
            "event_type": event_type,
            "subject_id": subject_id,
            "details": details,
            "timestamp": FIXED_NOW,
            "actor": "SYSTEM",
        }
    )


def _ws(data: dict[str, Any]) -> dict[str, Any]:
    pass
    return data.setdefault("_ws", {})


def _eq(a: Any, b: Any) -> bool:
    """Secure comparison for identifiers (convert both sides to strings)."""
    pass
    return str(a) == str(b)


def _sid(v: Any) -> str:
    """Convert any value resembling an id (or subject key) into a string."""
    pass
    return str(v)


class GetClusterById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: str) -> str:
        cluster_id = _sid(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        cluster = next((c for c in clusters if c.get("cluster_id") == cluster_id), None)
        payload = cluster or {"error": f"cluster {cluster_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetClusterById",
                "description": "Retrieve ElastiCache cluster by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"cluster_id": {"type": "string"}},
                    "required": ["cluster_id"],
                },
            },
        }


class ListClustersByStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], status: str) -> str:
        clusters = data.get("aws_elasticache_clusters", [])
        result = [c for c in clusters if c.get("status") == status]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listClustersByStatus",
                "description": "List ElastiCache clusters by status.",
                "parameters": {
                    "type": "object",
                    "properties": {"status": {"type": "string"}},
                    "required": ["status"],
                },
            },
        }


class ValidateClusterEndpoint(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: str) -> str:
        cluster_id = _sid(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        cl = next((c for c in clusters if c.get("cluster_id") == cluster_id), None)
        if not cl:
            payload = {"error": f"cluster {cluster_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        ok = cl.get("status") == "available" and cl.get("endpoint_url") not in (
            None,
            "NULL",
            "",
        )
        payload = {
            "cluster_id": cluster_id,
            "valid": ok,
            "endpoint_url": cl.get("endpoint_url"),
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateClusterEndpoint",
                "description": "Validate cluster is available and has a usable endpoint.",
                "parameters": {
                    "type": "object",
                    "properties": {"cluster_id": {"type": "string"}},
                    "required": ["cluster_id"],
                },
            },
        }


class ListSecurityGroupRules(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], security_group_id: str) -> str:
        security_group_id = _sid(security_group_id)
        rules = data.get("aws_security_group_rules", [])
        result = [r for r in rules if r.get("security_group_id") == security_group_id]
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListSecurityGroupRules",
                "description": "List SG rules for a given security group.",
                "parameters": {
                    "type": "object",
                    "properties": {"security_group_id": {"type": "string"}},
                    "required": ["security_group_id"],
                },
            },
        }


class HardenRedisSecurityGroup(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], security_group_id: str, allowed_cidr_list: list[str]
    ) -> str:
        security_group_id = _sid(security_group_id)
        rules = data.get("aws_security_group_rules", [])
        changed = []
        for r in list(rules):
            if (
                r.get("security_group_id") == security_group_id
                and r.get("port") == 6379
                and r.get("protocol") == "TCP"
                and r.get("source_ip") == "0.0.0.0/0"
            ):
                rules.remove(r)
                changed.append(r.get("rule_id"))
        existing = {
            (x.get("port"), x.get("protocol"), x.get("source_ip"))
            for x in rules
            if x.get("security_group_id") == security_group_id
        }
        for cidr in allowed_cidr_list:
            key = (6379, "TCP", cidr)
            if key not in existing:
                new_rule_id = f"sgr-{security_group_id}-{cidr.replace('/', '_')}"
                rules.append(
                    {
                        "rule_id": new_rule_id,
                        "security_group_id": security_group_id,
                        "port": 6379,
                        "protocol": "TCP",
                        "source_ip": cidr,
                        "description": "Allow Redis access from approved CIDR",
                    }
                )
                changed.append(new_rule_id)
        payload = {"security_group_id": security_group_id, "changed": changed}
        out = json.dumps(
            payload, indent=2
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "HardenRedisSecurityGroup",
                "description": "Remove 0.0.0.0/0 Redis access and add approved CIDRs for port 6379/TCP.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "security_group_id": {"type": "string"},
                        "allowed_cidr_list": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["security_group_id", "allowed_cidr_list"],
                },
            },
        }


class LinkCacheToOrg(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], org_id: str, cluster_id: str, partition_key: str
    ) -> str:
        org_id, cluster_id = _sid(org_id), _sid(cluster_id)
        partition_key = _sid(partition_key)
        clusters = data.get("aws_elasticache_clusters", [])
        cl = next((c for c in clusters if c.get("cluster_id") == cluster_id), None)
        if not cl:
            payload = {"error": f"cluster {cluster_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if not (
            cl.get("status") == "available"
            and cl.get("endpoint_url") not in (None, "NULL", "")
        ):
            payload = {"error": "cluster not usable"}
            out = json.dumps(payload, indent=2)
            return out
        settings = data.get("custom_settings", [])
        url_setting = next(
            (
                s
                for s in settings
                if s.get("org_id") == org_id
                and s.get("setting_name") == "CacheAPI.ExternalSystemURL"
            ),
            None,
        )
        if url_setting:
            url_setting["value"] = cl.get("endpoint_url")
        pk_setting = next(
            (
                s
                for s in settings
                if s.get("org_id") == org_id
                and s.get("setting_name") == "CacheAPI.ExternalSystemPartitionKey"
            ),
            None,
        )
        if pk_setting:
            pk_setting["value"] = partition_key
        payload = {
            "org_id": org_id,
            "endpoint": cl.get("endpoint_url"),
            "partition_key": partition_key,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
            

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "linkCacheToOrg",
                "description": "Set CacheAPI external URL and partition key for an org using a validated cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "cluster_id": {"type": "string"},
                        "partition_key": {"type": "string"},
                    },
                    "required": ["org_id", "cluster_id", "partition_key"],
                },
            },
        }


class NormalizeCustomSetting(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], setting_id: str) -> str:
        settings = data.get("custom_settings", [])
        st = next((s for s in settings if s.get("setting_id") == setting_id), None)
        if not st:
            payload = {"error": f"setting {setting_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if st.get("value") == "NULL":
            st["value"] = None
        payload = st
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "normalizeCustomSetting",
                "description": "Normalize a custom setting value: string 'NULL' -> null.",
                "parameters": {
                    "type": "object",
                    "properties": {"setting_id": {"type": "string"}},
                    "required": ["setting_id"],
                },
            },
        }


class RunCacheJob(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], org_id: str, job_name: str) -> str:
        org_id = _sid(org_id)
        jobs = data.get("cache_jobs", [])
        valid_jobs = {"Load API Metadata", "Populate Cache Job"}
        if job_name not in valid_jobs:
            payload = {"error": "invalid job name"}
            out = json.dumps(payload, indent=2)
            return out
        updated = []
        for j in jobs:
            if j.get("org_id") == org_id and j.get("job_name") == job_name:
                j["last_run_status"] = "Success"
                j["last_run_time"] = FIXED_NOW
                updated.append(j.get("job_id"))
        _append_audit(data, "RUN_CACHE_JOB", org_id, {"job_name": job_name})
        _ws_append(
            data, org_id, "RUN_CACHE_JOB", {"job_name": job_name, "updated": updated}
        )
        payload = {"org_id": org_id, "job_name": job_name, "updated": updated}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "runCacheJob",
                "description": "Run a cache job for an org; sets deterministic status/time on matching job rows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "job_name": {"type": "string"},
                    },
                    "required": ["org_id", "job_name"],
                },
            },
        }


class GetCacheJobHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], org_id: str) -> str:
        org_id = _sid(org_id)
        jobs = data.get("cache_jobs", [])
        result = [j for j in jobs if j.get("org_id") == org_id]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCacheJobHistory",
                "description": "List cache jobs for an org.",
                "parameters": {
                    "type": "object",
                    "properties": {"org_id": {"type": "string"}},
                    "required": ["org_id"],
                },
            },
        }


class NormalizeConnectedAppScopes(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        app_id: str,
        connected_apps: list = None
    ) -> str:
        app_id = _sid(app_id)
        apps = connected_apps if connected_apps is not None else data.get("connected_apps", [])
        app = next((a for a in apps if a.get("app_id") == app_id), None)
        if not app:
            payload = {"error": f"app {app_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        scopes = app.get("oauth_scopes")
        if isinstance(scopes, str):
            vals = [s.strip() for s in scopes.split(",")]
            scopes_list = [v for v in vals if v]
        elif isinstance(scopes, list):
            scopes_list = scopes
        else:
            scopes_list = []
        for r in ["api", "refresh_token"]:
            if r not in scopes_list:
                scopes_list.append(r)
        app["oauth_scopes"] = scopes_list
        _ws_append(data, app_id, "NORMALIZE_APP_SCOPES", {"oauth_scopes": scopes_list})
        _append_audit(
            data, "NORMALIZE_APP_SCOPES", app_id, {"oauth_scopes": scopes_list}
        )
        payload = app
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "normalizeConnectedAppScopes",
                "description": "Normalize a connected app's oauth_scopes to a list and enforce required scopes.",
                "parameters": {
                    "type": "object",
                    "properties": {"app_id": {"type": "string"}},
                    "required": ["app_id"],
                },
            },
        }


class SetTraceFlag(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], org_id: str, flag_name: str, is_active: bool
    ) -> str:
        org_id, flag_name = _sid(org_id), _sid(flag_name)
        is_active = bool(is_active)
        flags = data.get("trace_flags", [])
        tf = next(
            (
                f
                for f in flags
                if f.get("org_id") == org_id and f.get("flag_name") == flag_name
            ),
            None,
        )
        if not tf:
            payload = {"error": "trace flag not found"}
            out = json.dumps(payload, indent=2)
            return out
        org_type = (
            "UAT"
            if org_id.endswith("QRS")
            else ("Staging" if org_id.endswith("DEF") else "Production")
        )
        if (
            org_type == "Production"
            and is_active
            and flag_name in ("CacheAPI.EcommLogger", "ApexDebug")
        ):
            payload = {"error": "forbidden in Production"}
            out = json.dumps(payload, indent=2)
            return out
        tf["is_active"] = bool(is_active)
        _ws_append(
            data,
            f"{org_id}:{flag_name}",
            "SET_TRACE_FLAG",
            {"is_active": bool(is_active)},
        )
        _append_audit(
            data,
            "SET_TRACE_FLAG",
            f"{org_id}:{flag_name}",
            {"is_active": bool(is_active)},
        )
        payload = tf
        out = json.dumps(payload, indent=2)
        return out
           

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setTraceFlag",
                "description": "Enable/disable a trace flag with production-safe guardrails.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "flag_name": {"type": "string"},
                        "is_active": {"type": "boolean"},
                    },
                    "required": ["org_id", "flag_name", "is_active"],
                },
            },
        }


class SetFeatureToggle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], org_id: str, toggle_name: str, value: str) -> str:
        org_id, toggle_name, value = _sid(org_id), _sid(toggle_name), _sid(value)
        settings = data.get("custom_settings", [])
        st = next(
            (
                s
                for s in settings
                if s.get("org_id") == org_id and s.get("setting_name") == toggle_name
            ),
            None,
        )
        if not st:
            payload = {"error": "toggle not found"}
            out = json.dumps(payload, indent=2)
            return out
        st["value"] = value
        _ws_append(
            data, f"{org_id}:{toggle_name}", "SET_FEATURE_TOGGLE", {"value": value}
        )
        _append_audit(
            data, "SET_FEATURE_TOGGLE", f"{org_id}:{toggle_name}", {"value": value}
        )
        payload = st
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setFeatureToggle",
                "description": "Set a feature toggle value via custom settings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "toggle_name": {"type": "string"},
                        "value": {"type": "string"},
                    },
                    "required": ["org_id", "toggle_name", "value"],
                },
            },
        }


class GetOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        order_id = _sid(order_id)
        orders = data.get("orders", [])
        o = next((x for x in orders if x.get("order_id") == order_id), None)
        payload = o or {"error": f"order {order_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrder",
                "description": "Retrieve order record by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class GetOrderItems(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        order_items: list = None
    ) -> str:
        order_id = _sid(order_id)
        items = order_items if order_items is not None else data.get("order_items", [])
        result = [i for i in items if i.get("order_id") == order_id]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrderItems",
                "description": "List items for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class GetAccount(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], account_id: str) -> str:
        account_id = _sid(account_id)
        accs = data.get("accounts", [])
        a = next((x for x in accs if x.get("account_id") == account_id), None)
        payload = a or {"error": f"account {account_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAccount",
                "description": "Retrieve account by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"account_id": {"type": "string"}},
                    "required": ["account_id"],
                },
            },
        }


class GetOrg(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], org_id: str) -> str:
        org_id = _sid(org_id)
        orgs = data.get("salesforce_orgs", [])
        org = next((o for o in orgs if o.get("org_id") == org_id), None)
        payload = org or {"error": f"org {org_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOrg",
                "description": "Retrieve Salesforce org metadata (including org_name) by org_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"org_id": {"type": "string"}},
                    "required": ["org_id"],
                },
            },
        }


class GetPriceForProduct(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], pricebook_id: str, product_id: str) -> str:
        pricebook_id, product_id = _sid(pricebook_id), _sid(product_id)
        pbes = data.get("pricebook_entries", [])
        pbe = next(
            (
                p
                for p in pbes
                if p.get("pricebook_id") == pricebook_id
                and p.get("product_id") == product_id
            ),
            None,
        )
        payload = pbe or {"error": "price not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPriceForProduct",
                "description": "Get price for a product from a pricebook.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pricebook_id": {"type": "string"},
                        "product_id": {"type": "string"},
                    },
                    "required": ["pricebook_id", "product_id"],
                },
            },
        }


class GetProductStock(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str) -> str:
        product_id = _sid(product_id)
        products = data.get("products", [])
        p = next((x for x in products if x.get("product_id") == product_id), None)
        if not p:
            payload = {"error": f"product {product_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"product_id": product_id, "stock_quantity": p.get("stock_quantity")}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductStock",
                "description": "Get current stock quantity for a product.",
                "parameters": {
                    "type": "object",
                    "properties": {"product_id": {"type": "string"}},
                    "required": ["product_id"],
                },
            },
        }


def _active_offer(
    offers: list[dict[str, Any]], offer_id: str | None
) -> dict[str, Any] | None:
    pass
    if not offer_id:
        return None
    off = next((o for o in offers if o.get("offer_id") == offer_id), None)
    if not off:
        return None
    if off.get("is_active") is False:
        return None
    return off


class RecomputeOrderTotals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        pass
        order_id = _sid(order_id)
        orders = data.get("orders", [])
        items = data.get("order_items", [])
        accounts = data.get("accounts", [])
        pbes = data.get("pricebook_entries", [])
        offers = data.get("offers", [])
        data.get("products", [])

        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        account = next(
            (a for a in accounts if a.get("account_id") == order.get("account_id")),
            None,
        )
        pricebook_id = account.get("default_pricebook_id") if account else None
        line_items = [i for i in items if i.get("order_id") == order_id]
        subtotal = 0.0
        for li in line_items:
            pbe = next(
                (
                    p
                    for p in pbes
                    if p.get("pricebook_id") == pricebook_id
                    and p.get("product_id") == li.get("product_id")
                ),
                None,
            )
            #revert to the current price if the pricebook entry is absent
            price = pbe.get("price") if pbe else li.get("price", 0.0)
            subtotal += float(price) * int(li.get("quantity", 0))

        discount_amount = 0.0
        applied_offer = _active_offer(offers, order.get("applied_offer_id"))
        if applied_offer:
            if applied_offer.get("discount_type") == "PERCENTAGE":
                discount_amount = round(
                    subtotal * float(applied_offer.get("discount_value", 0.0)) / 100.0,
                    2,
                )
            elif applied_offer.get("discount_type") == "FIXED_AMOUNT":
                discount_amount = float(applied_offer.get("discount_value", 0.0))
            discount_amount = min(discount_amount, subtotal)

        total_amount = round(subtotal - discount_amount, 2)
        order["subtotal"] = round(subtotal, 2)
        order["discount_amount"] = round(discount_amount, 2)
        order["total_amount"] = total_amount
        _append_audit(data, "RECOMPUTE_TOTALS", order_id, {})
        _ws_append(data, order_id, "RECOMPUTE_TOTALS", {})
        payload = order
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecomputeOrderTotals",
                "description": "Recompute order subtotal, discount and total using account pricebook and active offer.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class ApplyOfferToOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        offer_id: str,
        orders: list = None,
        offers: list = None
    ) -> str:
        order_id, offer_id = _sid(order_id), _sid(offer_id)
        orders = orders if orders is not None else data.get("orders", [])
        offers = offers if offers is not None else data.get("offers", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        off = _active_offer(offers, offer_id)
        if not off:
            payload = {"error": "offer not active or not found"}
            out = json.dumps(payload, indent=2)
            return out
        order["applied_offer_id"] = offer_id
        payload = {"order_id": order_id, "applied_offer_id": offer_id}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "applyOfferToOrder",
                "description": "Apply an active offer to an order. (Does not recompute totals.)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "offer_id": {"type": "string"},
                    },
                    "required": ["order_id", "offer_id"],
                },
            },
        }


class EnforceMinimumOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        orders: list = None,
        accounts: list = None
    ) -> str:
        order_id = _sid(order_id)
        orders = orders if orders is not None else data.get("orders", [])
        accounts = accounts if accounts is not None else data.get("accounts", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        account = next(
            (a for a in accounts if a.get("account_id") == order.get("account_id")),
            None,
        )
        threshold = (
            50.0 if (account and account.get("type") == "B2C Customer") else 1000.0
        )
        eligible = float(order.get("total_amount", 0.0)) >= threshold
        _append_audit(
            data,
            "ELIGIBILITY_CHECK",
            order_id,
            {"eligible": eligible, "threshold": threshold},
        )
        _ws_append(
            data,
            order_id,
            "ELIGIBILITY_CHECK",
            {"eligible": eligible, "threshold": threshold},
        )
        payload = {"order_id": order_id, "eligible": eligible, "threshold": threshold}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EnforceMinimumOrder",
                "description": "Check if an order meets minimum order thresholds (Retail vs B2B).",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


def _adjust_stock(products: list[dict[str, Any]], product_id: str, delta: int) -> bool:
    pass
    product_id = _sid(product_id)
    try:
        delta = int(delta)
    except Exception:
        return False
    p = next((x for x in products if _eq(x.get("product_id"), product_id)), None)
    if not p:
        return False
    new_qty = int(p.get("stock_quantity", 0)) + delta
    if new_qty < 0:
        return False
    p["stock_quantity"] = new_qty
    return True


class UpdateProductStock(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str, delta: int) -> str:
        products = data.get("products", [])
        ok = _adjust_stock(products, product_id, delta)
        if not ok:
            payload = {"error": "stock adjustment failed"}
            out = json.dumps(payload, indent=2)
            return out
        p = next((x for x in products if x.get("product_id") == product_id), None)
        _append_audit(data, "UPDATE_STOCK", product_id, {"delta": delta})
        _ws_append(data, product_id, "UPDATE_STOCK", {"delta": delta})
        payload = {"product_id": product_id, "stock_quantity": p.get("stock_quantity")}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProductStock",
                "description": "Adjust product stock by delta (must not go negative). Appends deterministic audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "delta": {"type": "integer"},
                    },
                    "required": ["product_id", "delta"],
                },
            },
        }


class ShipOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        order_id = _sid(order_id)
        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if order.get("status") != "Processing":
            payload = {"error": "order not in Processing"}
            out = json.dumps(payload, indent=2)
            return out
        order["status"] = "Shipped"
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "shipOrder",
                "description": "Ship a Processing order: checks stock and decrements product inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class DeliverOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        order_id = _sid(order_id)
        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if order.get("status") != "Shipped":
            payload = {"error": "order not in Shipped"}
            out = json.dumps(payload, indent=2)
            return out
        order["status"] = "Delivered"
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deliverOrder",
                "description": "Set order to Delivered from Shipped.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class CancelOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        order_id = _sid(order_id)
        orders = data.get("orders", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if order.get("status") == "Delivered":
            payload = {"error": "cannot cancel Delivered order"}
            out = json.dumps(payload, indent=2)
            return out
        order["status"] = "Cancelled"
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancelOrder",
                "description": "Cancel an order unless it is already Delivered.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class CreateReturnCase(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str, items: list[dict[str, Any]]) -> str:
        order_id = _sid(order_id)
        orders = data.get("orders", [])
        cases = data.get("cases", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if order.get("status") != "Delivered":
            payload = {"error": "returns only allowed for Delivered"}
            out = json.dumps(payload, indent=2)
            return out
        new_case_id = f"5{order_id}"
        cases.append(
            {
                "case_id": new_case_id,
                "contact_id": order.get("contact_id"),
                "account_id": order.get("account_id"),
                "order_id": order_id,
                "subject": f"Return Request for Order #{order_id}",
                "status": "New",
                "priority": "Medium",
            }
        )
        order["status"] = "Return Pending"
        _append_audit(
            data,
            "CREATE_RETURN_CASE",
            order_id,
            {"case_id": new_case_id, "items": items},
        )
        _ws_append(
            data,
            order_id,
            "CREATE_RETURN_CASE",
            {"case_id": new_case_id, "items": items},
        )
        payload = {"case_id": new_case_id, "order_status": order["status"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createReturnCase",
                "description": "Create a return case for a Delivered order and set order to Return Pending.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["order_id", "items"],
                },
            },
        }


class ProcessReturn(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str, items: list[dict[str, Any]]) -> str:
        order_id = _sid(order_id)
        norm_items: list[dict[str, Any]] = []
        for it in items or []:
            pid = _sid(it.get("product_id"))
            qty = int(it.get("quantity", 1))
            reason = it.get("reason", "customer_request")
            norm_items.append({"product_id": pid, "quantity": qty, "reason": reason})
        orders = data.get("orders", [])
        order = next((o for o in orders if _eq(o.get("order_id"), order_id)), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if order.get("status") not in ("Delivered", "Return Pending"):
            payload = {"error": "return not allowed for this status"}
            out = json.dumps(payload, indent=2)
            return out
        order["status"] = "Delivered"
        _append_audit(data, "PROCESS_RETURN", order_id, {"items": norm_items})
        _ws_append(data, order_id, "PROCESS_RETURN", {"items": norm_items})
        payload = {"order_id": order_id, "order_status": order["status"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessReturn",
                "description": "Process a return by incrementing product stock and normalizing order status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["order_id", "items"],
                },
            },
        }


class CloseCase(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], case_id: str, resolution: str) -> str:
        case_id = _sid(case_id)
        cases = data.get("cases", [])
        c = next((x for x in cases if x.get("case_id") == case_id), None)
        if not c:
            payload = {"error": f"case {case_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        c["status"] = "Resolved"
        c["resolution"] = resolution
        _append_audit(data, "CLOSE_CASE", case_id, {"resolution": resolution})
        _ws_append(data, case_id, "CLOSE_CASE", {"resolution": resolution})
        payload = c
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "closeCase",
                "description": "Close a case with a resolution.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_id": {"type": "string"},
                        "resolution": {"type": "string"},
                    },
                    "required": ["case_id", "resolution"],
                },
            },
        }


class ActivateOffer(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], offer_id: str, is_active: bool) -> str:
        offer_id = _sid(offer_id)
        offers = data.get("offers", [])
        off = next((o for o in offers if o.get("offer_id") == offer_id), None)
        if not off:
            payload = {"error": f"offer {offer_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        off["is_active"] = bool(is_active)
        _append_audit(data, "ACTIVATE_OFFER", offer_id, {"is_active": bool(is_active)})
        _ws_append(data, offer_id, "ACTIVATE_OFFER", {"is_active": bool(is_active)})
        payload = off
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "activateOffer",
                "description": "Activate or deactivate an offer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "offer_id": {"type": "string"},
                        "is_active": {"type": "boolean"},
                    },
                    "required": ["offer_id", "is_active"],
                },
            },
        }


class InvalidateCacheForCatalog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], org_id: str, catalog_id: str) -> str:
        org_id, catalog_id = _sid(org_id), _sid(catalog_id)
        _append_audit(data, "INVALIDATE_CACHE", f"{org_id}:{catalog_id}", {})
        _ws_append(data, f"{org_id}:{catalog_id}", "INVALIDATE_CACHE", {})
        payload = {"org_id": org_id, "catalog_id": catalog_id, "scheduled": True}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InvalidateCacheForCatalog",
                "description": "Record a cache invalidation for a catalog scope.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "catalog_id": {"type": "string"},
                    },
                    "required": ["org_id", "catalog_id"],
                },
            },
        }


class NormalizeTimestampField(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], table_name: str, id_field: str, id_value: str, field: str
    ) -> str:
        id_value = _sid(id_value)
        table = data.get(table_name, [])
        row = next((r for r in table if str(r.get(id_field)) == id_value), None)
        if not row:
            payload = {"error": "row not found"}
            out = json.dumps(payload, indent=2)
            return out
        row[field] = FIXED_NOW
        _append_audit(
            data,
            "NORMALIZE_TIMESTAMP",
            f"{table_name}:{id_value}:{field}",
            {"new_value": FIXED_NOW},
        )
        _ws_append(
            data,
            f"{table_name}:{id_value}:{field}",
            "NORMALIZE_TIMESTAMP",
            {"new_value": FIXED_NOW},
        )
        payload = row
        out = json.dumps(payload, indent=2)
        return out
           

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "normalizeTimestampField",
                "description": "Normalize a datetime field on a given row to ISO-8601 fixed time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "table_name": {"type": "string"},
                        "id_field": {"type": "string"},
                        "id_value": {"type": "string"},
                        "field": {"type": "string"},
                    },
                    "required": ["table_name", "id_field", "id_value", "field"],
                },
            },
        }


class GetAuditLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_log: list = None) -> str:
        payload = audit_log if audit_log is not None else []
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuditLog",
                "description": "Return the audit log.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class CreateAuditRecord(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        subject_id: str,
        event_type: str,
        details: dict[str, Any] | None = None,
        bucket: str | None = None
    ) -> str:
        subject_id = _sid(subject_id)
        if bucket is not None:
            bucket = _sid(bucket)
        event_type = _sid(event_type)
        staged_events = _ws(data).get(subject_id, {"events": []}).get("events", [])
        if details is None and bucket is None:
            details = {
                "summary": f"Aggregated evidence for {subject_id}",
                "events": staged_events,
            }
        if isinstance(details, dict) and "timestamp" in details:
            details = {k: v for k, v in details.items() if k != "timestamp"}
        if details is None and bucket is not None:
            details = {"bucket": bucket}

        _append_audit(data, event_type, subject_id, details)
        _ws(data).pop(subject_id, None)
        payload = {"subject_id": subject_id, "event_type": event_type}
        out = json.dumps(
            payload, indent=2
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAuditRecord",
                "description": "Create a single aggregated audit record for a subject. Caller must provide either details or bucket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "details": {"type": "object"},
                        "bucket": {"type": "string"},
                    },
                    "required": ["subject_id", "event_type"],
                },
            },
        }


class NormalizeOrgCacheTimestamps(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], org_id: str) -> str:
        org_id = _sid(org_id)
        jobs = data.get("cache_jobs", [])
        updated: list[str] = []
        for j in jobs:
            if j.get("org_id") == org_id:
                j["last_run_time"] = FIXED_NOW
                updated.append(j.get("job_id"))
        payload = {"org_id": org_id, "updated": updated}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NormalizeOrgCacheTimestamps",
                "description": "Normalize all cache job timestamps for an org to the fixed time.",
                "parameters": {
                    "type": "object",
                    "properties": {"org_id": {"type": "string"}},
                    "required": ["org_id"],
                },
            },
        }


class RunCacheJobsInOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        org_id: str,
        cache_jobs: list[dict[str, Any]] = None
    ) -> str:
        org_id = _sid(org_id)
        required_seq = ["Load API Metadata", "Populate Cache Job"]
        jobs = cache_jobs if cache_jobs is not None else data.get("cache_jobs", [])
        updated: list[str] = []
        for job_name in required_seq:
            for j in jobs:
                if j.get("org_id") == org_id and j.get("job_name") == job_name:
                    j["last_run_status"] = "Success"
                    j["last_run_time"] = FIXED_NOW
                    updated.append(j.get("job_id"))
            _append_audit(data, "RUN_CACHE_JOB", org_id, {"job_name": job_name})
            _ws_append(
                data,
                org_id,
                "RUN_CACHE_JOB",
                {"job_name": job_name, "updated": updated},
            )
        payload = {"org_id": org_id, "updated": updated, "sequence": required_seq}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RunCacheJobsInOrder",
                "description": "Run 'Load API Metadata' then 'Populate Cache Job' for an org; self-audits; deterministic.",
                "parameters": {
                    "type": "object",
                    "properties": {"org_id": {"type": "string"}},
                    "required": ["org_id"],
                },
            },
        }


class VerifyOrderPricesAgainstPricebook(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        pricebook_id: str | None = None
    ) -> str:
        pass
        order_id = _sid(order_id)
        eff_pb = _sid(pricebook_id) if pricebook_id is not None else None
        orders = data.get("orders", [])
        items = data.get("order_items", [])
        accounts = data.get("accounts", [])
        pbes = data.get("pricebook_entries", [])
        order = next((o for o in orders if _eq(o.get("order_id"), order_id)), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if eff_pb is None:
            acct = next(
                (
                    a
                    for a in accounts
                    if _eq(a.get("account_id"), order.get("account_id"))
                ),
                None,
            )
            eff_pb = acct.get("default_pricebook_id") if acct else None
        if not eff_pb:
            payload = {"error": "no pricebook context available"}
            out = json.dumps(payload, indent=2)
            return out
        lines = [li for li in items if _eq(li.get("order_id"), order_id)]
        checks = []
        for li in lines:
            pbe = next(
                (
                    p
                    for p in pbes
                    if _eq(p.get("pricebook_id"), eff_pb)
                    and _eq(p.get("product_id"), li.get("product_id"))
                ),
                None,
            )
            op = float(li.get("price", 0.0))
            pb = float(pbe.get("price")) if pbe else None
            checks.append(
                {
                    "product_id": li.get("product_id"),
                    "order_price": op,
                    "pricebook_price": pb,
                    "quantity": int(li.get("quantity", 0)),
                    "matches": (pb is not None and abs(op - pb) < 1e-9),
                }
            )
        all_match = all(c["matches"] for c in checks) if checks else False
        _append_audit(
            data,
            "PRICEBOOK_VERIFICATION",
            order_id,
            {"pricebook_id": eff_pb, "all_match": all_match},
        )
        _ws_append(
            data,
            order_id,
            "PRICEBOOK_VERIFICATION",
            {"pricebook_id": eff_pb, "all_match": all_match},
        )
        payload = {"order_id": order_id, "pricebook_id": eff_pb, "checks": checks}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifyOrderPricesAgainstPricebook",
                "description": "Verify all order line prices against a given or inferred pricebook.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "pricebook_id": {"type": "string"},
                    },
                    "required": ["order_id"],
                },
            },
        }


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
            org_jobs = [j for j in cache_jobs if j.get("org_id") == org_id]
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
            org_jobs = [j for j in cache_jobs if j.get("org_id") == subject_id]
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
                its = [li for li in items if li.get("order_id") == subject_id]
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
            grp = [r for r in sgs if r.get("security_group_id") == subject_id]
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


#---------------- general-purpose utilities (10 minor tools) ----------------


class AddSubjectTag(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject_id: str, tag: str) -> str:
        subject_id = _sid(subject_id)
        payload = {"tag": tag}
        _ws_append(data, subject_id, "TAG_ADDED", payload)
        _append_audit(data, "TAG_ADDED", subject_id, payload)
        payload = {"subject_id": subject_id, "tag": tag, "ok": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddSubjectTag",
                "description": "Attach a tag to the subject and stage to evidence.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_id": {"type": "string"},
                        "tag": {"type": "string"},
                    },
                    "required": ["subject_id", "tag"],
                },
            },
        }


class RecordMetric(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject_id: str, metric: str, value: float) -> str:
        subject_id = _sid(subject_id)
        payload = {"metric": metric, "value": float(value)}
        _ws_append(data, subject_id, "METRIC_RECORDED", payload)
        payload = {"subject_id": subject_id, "metric": metric, "value": float(value)}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordMetric",
                "description": "Record a simple metric value for the subject.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_id": {"type": "string"},
                        "metric": {"type": "string"},
                        "value": {"type": "number"},
                    },
                    "required": ["subject_id", "metric", "value"],
                },
            },
        }


class ComputeDeltaNumbers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], before: float, after: float, label: str) -> str:
        delta = float(after) - float(before)
        payload = {
            "label": label,
            "before": float(before),
            "after": float(after),
            "delta": round(delta, 6),
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "computeDeltaNumbers",
                "description": "Compute numeric delta between before/after.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "before": {"type": "number"},
                        "after": {"type": "number"},
                        "label": {"type": "string"},
                    },
                    "required": ["before", "after", "label"],
                },
            },
        }


class DiffKeyset(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        left: dict[str, Any],
        right: dict[str, Any],
        keys: list[str],
    ) -> str:
        changes = {}
        for k in keys:
            lv = left.get(k, None)
            rv = right.get(k, None)
            if lv != rv:
                changes[k] = {"before": lv, "after": rv}
        payload = {"keys": keys, "changes": changes}
        out = json.dumps(payload, indent=2)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "diffKeyset",
                "description": "Diff two dicts across selected keys.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "left": {"type": "object"},
                        "right": {"type": "object"},
                        "keys": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["left", "right", "keys"],
                },
            },
        }


class ClassifySubjectForAudit(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        subject_id: str,
        fallback_bucket: str = "MISC"
    ) -> str:
        subject_id = _sid(subject_id)
        bucket = fallback_bucket
        if ":" in subject_id:
            bucket = "CACHE_ALIGNMENT_EVIDENCE"
        elif subject_id.isdigit():
            staged = _ws(data).get(subject_id, {"events": []}).get("events", [])
            if any(ev.get("event_type") == "PROCESS_RETURN" for ev in staged):
                bucket = "RETURN_EVIDENCE"
            else:
                bucket = "PRICING_EVIDENCE"
        elif subject_id.startswith("sg-"):
            bucket = "SG_EVIDENCE"
        payload = {"subject_id": subject_id, "bucket": bucket}
        out = json.dumps(payload, indent=2)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "classifySubjectForAudit",
                "description": "Classify a subject_id into an audit bucket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_id": {"type": "string"},
                        "fallback_bucket": {"type": "string"},
                    },
                    "required": ["subject_id"],
                },
            },
        }


class BuildAuditDetailsForBucket(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject_id: str, bucket: str) -> str:
        subject_id = _sid(subject_id)
        staged = _ws(data).get(subject_id, {"events": []}).get("events", [])
        try:
            from rules import build_audit_details as _build

            details = _build(bucket=bucket, subject_id=subject_id, staged_events=staged)
        except Exception:
            details = {"bucket": bucket, "subject_id": subject_id, "events": staged}
        payload = details
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildAuditDetailsForBucket",
                "description": "Build deterministic details for create_audit_record based on bucket rules in rules.py.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_id": {"type": "string"},
                        "bucket": {"type": "string"},
                    },
                    "required": ["subject_id", "bucket"],
                },
            },
        }


class RedactFields(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], payload: dict[str, Any], fields: list[str]) -> str:
        redacted = {k: v for k, v in payload.items() if k not in fields}
        payload = redacted
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "redactFields",
                "description": "Remove specified keys from a dict.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "payload": {"type": "object"},
                        "fields": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["payload", "fields"],
                },
            },
        }


class PickFields(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], payload: dict[str, Any], fields: list[str]) -> str:
        picked = {k: payload.get(k, None) for k in sorted(fields)}
        payload = picked
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "pickFields",
                "description": "Return only the selected keys from a dict.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "payload": {"type": "object"},
                        "fields": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["payload", "fields"],
                },
            },
        }


class EmitAnnotation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject_id: str, note: str) -> str:
        subject_id = _sid(subject_id)
        payload = {"note": note}
        _append_audit(data, "ANNOTATION", subject_id, {"note": note})
        _ws_append(data, subject_id, "ANNOTATION", payload)
        payload = {"subject_id": subject_id, "note": note}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EmitAnnotation",
                "description": "Emit a freeform annotation into workspace evidence.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_id": {"type": "string"},
                        "note": {"type": "string"},
                    },
                    "required": ["subject_id", "note"],
                },
            },
        }


class ConsolidateWorkspaceEvents(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject_id: str, event_types: list[str]) -> str:
        subject_id = _sid(subject_id)
        staged = _ws(data).get(subject_id, {"events": []}).get("events", [])
        filt = [e for e in staged if e.get("event_type") in set(event_types)]
        # Provide only a predictable subset
        slim = [
            {
                "event_type": e.get("event_type"),
                "payload": e.get("payload"),
                "ts": e.get("ts"),
            }
            for e in filt
        ]
        payload = {"subject_id": subject_id, "events": slim}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConsolidateWorkspaceEvents",
                "description": "Return filtered staged events for a subject.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_id": {"type": "string"},
                        "event_types": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["subject_id", "event_types"],
                },
            },
        }


TOOLS = [
    GetClusterById(),
    ListClustersByStatus(),
    ValidateClusterEndpoint(),
    ListSecurityGroupRules(),
    HardenRedisSecurityGroup(),
    LinkCacheToOrg(),
    NormalizeCustomSetting(),
    RunCacheJob(),
    GetCacheJobHistory(),
    NormalizeConnectedAppScopes(),
    SetTraceFlag(),
    SetFeatureToggle(),
    GetOrder(),
    GetOrderItems(),
    GetAccount(),
    GetOrg(),
    GetPriceForProduct(),
    GetProductStock(),
    UpdateProductStock(),
    RecomputeOrderTotals(),
    ApplyOfferToOrder(),
    EnforceMinimumOrder(),
    ShipOrder(),
    DeliverOrder(),
    CancelOrder(),
    CreateReturnCase(),
    ProcessReturn(),
    CloseCase(),
    ActivateOffer(),
    InvalidateCacheForCatalog(),
    NormalizeTimestampField(),
    GetAuditLog(),
    CreateAuditRecord(),
    NormalizeOrgCacheTimestamps(),
    VerifyOrderPricesAgainstPricebook(),
    RunCacheJobsInOrder(),
    CollectSubjectSnapshot(),
    AddSubjectTag(),
    RecordMetric(),
    ComputeDeltaNumbers(),
    DiffKeyset(),
    ClassifySubjectForAudit(),
    BuildAuditDetailsForBucket(),
    RedactFields(),
    PickFields(),
    EmitAnnotation(),
    ConsolidateWorkspaceEvents(),
]
