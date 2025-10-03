import json
from typing import Any

from domains.dto import Tool

FIXED_NOW = "2025-08-06T12:00:00Z"


def _stable_id(prefix: str, *parts: str) -> str:
    pass
    base = "-".join(_slugify(p) for p in parts if p is not None and str(p) != "")
    return f"{prefix}-{base}" if base else prefix


def _get_network_defaults(db: dict[str, Any], environment: str) -> dict[str, Any]:
    _environmentL = environment or ''.lower()
    pass
    subnets = _ensure_table(db, "aws_subnet_groups")
    row = _find_one(subnets, environment=environment)
    vpc_id = row.get("vpc_id") if row else f"vpc-{environment.lower()}-0001"
    sn = (
        row.get("subnet_ids")
        if row and row.get("subnet_ids")
        else [f"subnet-{environment.lower()}-a", f"subnet-{environment.lower()}-b"]
    )
    allow = (
        row.get("allowlist_cidrs")
        if row and row.get("allowlist_cidrs")
        else ["10.0.0.0/16"]
    )
    return {
        "vpc_id": vpc_id,
        "subnet_ids": sn,
        "allowlist_cidrs": allow,
        "tls_ports": [443],
        "redis_ports": [6379],
    }


def _find_one(rows: list[dict[str, Any]], **crit):
    pass
    for r in rows:
        if all(str(r.get(k)) == str(v) for k, v in crit.items()):
            return r
    return None


def _ensure_unique_id(rows: list, id_field: str, candidate: str) -> str:
    pass
    if not any(r.get(id_field) == candidate for r in rows):
        return candidate
    i = 2
    while any(r.get(id_field) == f"{candidate}-{i}" for r in rows):
        i += 1
    return f"{candidate}-{i}"


def _find_all(rows: list[dict[str, Any]], **crit) -> list[dict[str, Any]]:
    pass
    out = []
    for r in rows:
        ok = True
        for k, v in crit.items():
            if str(r.get(k)) != str(v):
                ok = False
                break
        if ok:
            out.append(r)
    return out


def _slugify(text: str, max_len: int = 40) -> str:
    pass
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


def _ensure_table(db: dict[str, Any], name: str):
    pass
    if name not in db:
        db[name] = []
    return db[name]


def _json(x: Any) -> str:
    pass
    payload = x
    out = json.dumps(payload, separators=(",", ":"))
    return out


#--------------------------- AWS / Security / Infrastructure ---------------------------


class GetEnvironmentNetworkDefaults(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], environment: str) -> str:
        res = _get_network_defaults(data, environment)
        res.update({"environment": environment})
        return _json(res)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEnvironmentNetworkDefaults",
                "description": "Resolve VPC/subnets/allowlist and standard ports for an environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        }
                    },
                    "required": ["environment"],
                },
            },
        }


class GetServiceSecurityGroup(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], environment: str, service_name: str) -> str:
        rules = _ensure_table(data, "aws_security_group_rules")
        # Gather all rules that correspond to environment and service
        matches = _find_all(rules, environment=environment, service_name=service_name)
        if matches:
            sg_id = matches[0]["sg_id"]
            ingress = [
                {"port": r["port"], "cidr": r["cidr"]}
                for r in matches
                if r.get("direction") == "ingress"
            ]
            egress = [
                {"port": r["port"], "cidr": r["cidr"]}
                for r in matches
                if r.get("direction") == "egress"
            ]
        else:
            # fixed sg id (not saved until an update applies rules)
            sg_id = _stable_id("sg", environment, service_name)
            ingress, egress = [], []
        return _json(
            {
                "environment": environment,
                "service_name": service_name,
                "sg_id": sg_id,
                "name": f"{service_name} [{environment}]",
                "ingress_rules": ingress,
                "egress_rules": egress,
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetServiceSecurityGroup",
                "description": "Find the security group for a service in an environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                        "service_name": {"type": "string"},
                    },
                    "required": ["environment", "service_name"],
                },
            },
        }


class UpdateSecurityGroupRuleset(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sg_id: str,
        environment: str,
        service_name: str,
        tcp_ports: list[int],
        allowlist_cidrs: list[str]
    ) -> str:
        rules = _ensure_table(data, "aws_security_group_rules")
        for port in tcp_ports:
            for cidr in allowlist_cidrs:
                row = _find_one(
                    rules,
                    sg_id=sg_id,
                    environment=environment,
                    service_name=service_name,
                    direction="ingress",
                    protocol="tcp",
                    port=int(port),
                    cidr=cidr,
                )
                if row:
                    row["updated_at"] = FIXED_NOW
                else:
                    rules.append(
                        {
                            "sg_id": sg_id,
                            "environment": environment,
                            "service_name": service_name,
                            "direction": "ingress",
                            "protocol": "tcp",
                            "port": int(port),
                            "cidr": cidr,
                            "description": f"{service_name} [{environment}] ingress {port}/{cidr}",
                            "created_at": FIXED_NOW,
                        }
                    )
        summary = f"{service_name} [{environment}] ports={sorted(set(tcp_ports))} cidrs={sorted(set(allowlist_cidrs))}"
        return _json(
            {
                "change_set_id": _stable_id(
                    "chg-sg",
                    sg_id,
                    environment,
                    service_name,
                    *map(str, tcp_ports),
                    *allowlist_cidrs,
                ),
                "labels": {"summary": summary},
                "applied": True,
            }
        )
        pass
        rules = _ensure_table(data, "aws_security_group_rules")
        for port in tcp_ports:
            for cidr in allowlist_cidrs:
                row = _find_one(
                    rules,
                    sg_id=sg_id,
                    environment=environment,
                    service_name=service_name,
                    direction="ingress",
                    protocol="tcp",
                    port=int(port),
                    cidr=cidr,
                )
                if row:
                    row["updated_at"] = FIXED_NOW
                else:
                    rules.append(
                        {
                            "sg_id": sg_id,
                            "environment": environment,
                            "service_name": service_name,
                            "direction": "ingress",
                            "protocol": "tcp",
                            "port": int(port),
                            "cidr": cidr,
                            "description": f"{service_name} [{environment}] ingress {port}/{cidr}",
                            "created_at": FIXED_NOW,
                        }
                    )
        summary = f"{service_name} [{environment}] ports={sorted(set(tcp_ports))} cidrs={sorted(set(allowlist_cidrs))}"
        return _json(
            {
                "change_set_id": _stable_id(
                    "chg-sg",
                    sg_id,
                    environment,
                    service_name,
                    *map(str, tcp_ports),
                    *allowlist_cidrs,
                ),
                "labels": {"summary": summary},
                "applied": True,
            }
        )

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateSecurityGroupRuleset",
                "description": "Upsert ingress rules for an SG using env/service context.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sg_id": {"type": "string"},
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                        "service_name": {"type": "string"},
                        "tcp_ports": {"type": "array", "items": {"type": "integer"}},
                        "allowlist_cidrs": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": [
                        "sg_id",
                        "environment",
                        "service_name",
                        "tcp_ports",
                        "allowlist_cidrs",
                    ],
                },
            },
        }


class ProvisionOrUpdateRedisCluster(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cluster_name: str,
        node_type: str,
        replicas: int,
        environment: str
    ) -> str:
        _environmentL = environment or ''.lower()
        pass
        clusters = _ensure_table(data, "aws_elasticache_clusters")
        cluster_id = _stable_id("rc", cluster_name, environment)
        endpoint = f"{cluster_name}.{environment.lower()}.cache.local:6379"
        row = _find_one(clusters, cluster_id=cluster_id)
        if row:
            row.update(
                {
                    "cluster_name": cluster_name,
                    "node_type": node_type,
                    "replicas": int(replicas),
                    "environment": environment,
                    "endpoint": endpoint,
                    "status": "available",
                }
            )
        else:
            clusters.append(
                {
                    "cluster_id": cluster_id,
                    "cluster_name": cluster_name,
                    "node_type": node_type,
                    "replicas": int(replicas),
                    "environment": environment,
                    "endpoint": endpoint,
                    "status": "available",
                    "require_auth": False,
                    "tls_in_transit": False,
                }
            )
        return _json(
            {"cluster_id": cluster_id, "endpoint": endpoint, "status": "available"}
        )
        _environmentL = environment or ''.lower()
        pass
        clusters = _ensure_table(data, "aws_elasticache_clusters")
        cluster_id = _stable_id("rc", cluster_name, environment)
        endpoint = f"{cluster_name}.{environment.lower()}.cache.local:6379"
        row = _find_one(clusters, cluster_id=cluster_id)
        if row:
            row.update(
                {
                    "cluster_name": cluster_name,
                    "node_type": node_type,
                    "replicas": int(replicas),
                    "environment": environment,
                    "endpoint": endpoint,
                    "status": "available",
                }
            )
        else:
            clusters.append(
                {
                    "cluster_id": cluster_id,
                    "cluster_name": cluster_name,
                    "node_type": node_type,
                    "replicas": int(replicas),
                    "environment": environment,
                    "endpoint": endpoint,
                    "status": "available",
                    "require_auth": False,
                    "tls_in_transit": False,
                }
            )
        return _json(
            {"cluster_id": cluster_id, "endpoint": endpoint, "status": "available"}
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "provisionOrUpdateRedisCluster",
                "description": "Provision or update an ElastiCache/Redis cluster for an environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_name": {"type": "string"},
                        "node_type": {"type": "string"},
                        "replicas": {"type": "integer", "minimum": 0},
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                    },
                    "required": [
                        "cluster_name",
                        "node_type",
                        "replicas",
                        "environment",
                    ],
                },
            },
        }


class SetRedisAuthAndTLS(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cluster_id: str,
        require_auth: bool = True,
        tls_in_transit: bool = True
    ) -> str:
        clusters = _ensure_table(data, "aws_elasticache_clusters")
        row = _find_one(clusters, cluster_id=cluster_id) or _find_one(
            clusters, cluster_name=cluster_id
        )
        if not row:
            raise ValueError(f"Cluster not found: {cluster_id}")
        env = row.get("environment", "UAT")
        kms_key_alias = f"alias/dcomm-{env.lower()}"
        row.update(
            {
                "require_auth": bool(require_auth),
                "tls_in_transit": bool(tls_in_transit),
                "kms_key_alias": kms_key_alias,
                "secret_arn": f"arn:aws:secretsmanager:local:000000000000:secret:{row.get('cluster_id', cluster_id)}",
                "updated_at": FIXED_NOW,
            }
        )
        return _json(
            {
                "secret_arn": row["secret_arn"],
                "tls_status": "enabled" if row["tls_in_transit"] else "disabled",
                "kms_key_alias": kms_key_alias,
            }
        )
        pass
        clusters = _ensure_table(data, "aws_elasticache_clusters")
        row = _find_one(clusters, cluster_id=cluster_id) or _find_one(
            clusters, cluster_name=cluster_id
        )
        if not row:
            raise ValueError(f"Cluster not found: {cluster_id}")
        env = row.get("environment", "UAT")
        kms_key_alias = f"alias/dcomm-{env.lower()}"
        row.update(
            {
                "require_auth": bool(require_auth),
                "tls_in_transit": bool(tls_in_transit),
                "kms_key_alias": kms_key_alias,
                "secret_arn": f"arn:aws:secretsmanager:local:000000000000:secret:{row.get('cluster_id', cluster_id)}",
                "updated_at": FIXED_NOW,
            }
        )
        return _json(
            {
                "secret_arn": row["secret_arn"],
                "tls_status": "enabled" if row["tls_in_transit"] else "disabled",
                "kms_key_alias": kms_key_alias,
            }
        )

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SetRedisAuthAndTls",
                "description": "Enable AUTH/TLS; booleans default to True if omitted.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "require_auth": {"type": "boolean"},
                        "tls_in_transit": {"type": "boolean"},
                    },
                    "required": ["cluster_id"],
                },
            },
        }


class CreateInterfaceEndpoint(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], vpc_id: str, service_name: str, subnet_ids: list[str]
    ) -> str:
        endpoints = _ensure_table(data, "aws_vpc_endpoints")
        endpoint_id = _stable_id("vpce", vpc_id, service_name, *subnet_ids)
        dns = f"{endpoint_id}.vpce.local"
        row = _find_one(endpoints, endpoint_id=endpoint_id)
        if row:
            row["dns_entries"] = [dns]
        else:
            endpoints.append(
                {
                    "endpoint_id": endpoint_id,
                    "vpc_id": vpc_id,
                    "service_name": service_name,
                    "subnet_ids": list(subnet_ids),
                    "dns_entries": [dns],
                }
            )
        return _json({"endpoint_id": endpoint_id, "dns_entries": [dns]})
        pass
        endpoints = _ensure_table(data, "aws_vpc_endpoints")
        endpoint_id = _stable_id("vpce", vpc_id, service_name, *subnet_ids)
        dns = f"{endpoint_id}.vpce.local"
        row = _find_one(endpoints, endpoint_id=endpoint_id)
        if row:
            row["dns_entries"] = [dns]
        else:
            endpoints.append(
                {
                    "endpoint_id": endpoint_id,
                    "vpc_id": vpc_id,
                    "service_name": service_name,
                    "subnet_ids": list(subnet_ids),
                    "dns_entries": [dns],
                }
            )
        return _json({"endpoint_id": endpoint_id, "dns_entries": [dns]})

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInterfaceEndpoint",
                "description": "Create a VPC Interface Endpoint for a service.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "vpc_id": {"type": "string"},
                        "service_name": {"type": "string"},
                        "subnet_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["vpc_id", "service_name", "subnet_ids"],
                },
            },
        }


class CreateSecretFor(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], environment: str, purpose: str, value_source_id: str
    ) -> str:
        _environmentL = environment or ''.lower()
        pass
        settings = _ensure_table(data, "custom_settings")
        key = f"secret:{purpose}:{environment}"
        kms_key_alias = f"alias/dcomm-{environment.lower()}"
        secret_arn = _stable_id("arn:secret", key, value_source_id, kms_key_alias)
        row = _find_one(settings, name=key)
        payload = {"source": value_source_id, "kms": kms_key_alias, "arn": secret_arn}
        if row:
            row.update({"value": json.dumps(payload), "updated_at": FIXED_NOW})
        else:
            settings.append(
                {
                    "setting_id": _stable_id("sec", key),
                    "name": key,
                    "value": json.dumps(payload),
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"secret_arn": secret_arn})
        _environmentL = environment or ''.lower()
        pass
        settings = _ensure_table(data, "custom_settings")
        key = f"secret:{purpose}:{environment}"
        kms_key_alias = f"alias/dcomm-{environment.lower()}"
        secret_arn = _stable_id("arn:secret", key, value_source_id, kms_key_alias)
        row = _find_one(settings, name=key)
        payload = {"source": value_source_id, "kms": kms_key_alias, "arn": secret_arn}
        if row:
            row.update({"value": json.dumps(payload), "updated_at": FIXED_NOW})
        else:
            settings.append(
                {
                    "setting_id": _stable_id("sec", key),
                    "name": key,
                    "value": json.dumps(payload),
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"secret_arn": secret_arn})

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateSecretFor",
                "description": "Create/rotate a secret using deterministic naming by environment and purpose.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                        "purpose": {
                            "type": "string",
                            "enum": [
                                "REDIS_AUTH_HEADER",
                                "OAUTH_CLIENT_SECRET",
                                "API_AUTH_HEADER",
                            ],
                        },
                        "value_source_id": {"type": "string"},
                    },
                    "required": ["environment", "purpose", "value_source_id"],
                },
            },
        }


class ConfigureCacheIntegration(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        external_url: str,
        auth_header_secret_arn: str,
        partition_key: str
    ) -> str:
        settings = _ensure_table(data, "custom_settings")

        def _upsert(name: str, value: str):
            row = _find_one(settings, name=name)
            if row:
                row["value"] = value
                row["updated_at"] = FIXED_NOW
            else:
                settings.append(
                    {
                        "setting_id": _stable_id("cs", name),
                        "name": name,
                        "value": value,
                        "updated_at": FIXED_NOW,
                    }
                )

        _upsert("CacheAPI.ExternalSystemURL", external_url)
        _upsert("CacheAPI.ExternalSystemAuthHeader", auth_header_secret_arn)
        _upsert("CacheAPI.ExternalSystemPartitionKey", partition_key)
        return _json(
            {
                "setting_ids": [
                    "CacheAPI.ExternalSystemURL",
                    "CacheAPI.ExternalSystemAuthHeader",
                    "CacheAPI.ExternalSystemPartitionKey",
                ],
                "verified": True,
            }
        )
        pass
        settings = _ensure_table(data, "custom_settings")

        def _upsert(name: str, value: str):
            pass
            row = _find_one(settings, name=name)
            if row:
                row["value"] = value
                row["updated_at"] = FIXED_NOW
            else:
                settings.append(
                    {
                        "setting_id": _stable_id("cs", name),
                        "name": name,
                        "value": value,
                        "updated_at": FIXED_NOW,
                    }
                )

        _upsert("CacheAPI.ExternalSystemURL", external_url)
        _upsert("CacheAPI.ExternalSystemAuthHeader", auth_header_secret_arn)
        _upsert("CacheAPI.ExternalSystemPartitionKey", partition_key)
        return _json(
            {
                "setting_ids": [
                    "CacheAPI.ExternalSystemURL",
                    "CacheAPI.ExternalSystemAuthHeader",
                    "CacheAPI.ExternalSystemPartitionKey",
                ],
                "verified": True,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConfigureCacheIntegration",
                "description": "Point Commerce to the external cache (URL/auth/partition key).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "external_url": {"type": "string"},
                        "auth_header_secret_arn": {"type": "string"},
                        "partition_key": {"type": "string"},
                    },
                    "required": [
                        "external_url",
                        "auth_header_secret_arn",
                        "partition_key",
                    ],
                },
            },
        }


class RunCacheWarmJobs(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], mode: str) -> str:
        jobs = _ensure_table(data, "cache_jobs")
        job_name = "Load API Metadata" if mode == "metadata" else "Populate Cache Job"
        job_id = _stable_id("job", job_name)
        row = _find_one(jobs, job_id=job_id)
        if row:
            row["last_run_status"] = "Succeeded"
            row["last_run_time"] = FIXED_NOW
        else:
            jobs.append(
                {
                    "job_id": job_id,
                    "job_name": job_name,
                    "last_run_status": "Succeeded",
                    "last_run_time": FIXED_NOW,
                }
            )
        items_warmed = 1234 if mode == "metadata" else 9876
        return _json(
            {
                "job_run_id": _stable_id("run", job_name, FIXED_NOW),
                "status": "Succeeded",
                "items_warmed": items_warmed,
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RunCacheWarmJobs",
                "description": "Execute cache warm jobs for metadata or populate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mode": {"type": "string", "enum": ["metadata", "populate"]}
                    },
                    "required": ["mode"],
                },
            },
        }


class SetCachePartitionKey(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], partition_key: str, version: str) -> str:
        settings = _ensure_table(data, "custom_settings")
        name = "CacheAPI.ExternalSystemPartitionKeyVersion"
        row = _find_one(settings, name=name)
        if row:
            row["value"] = version
            row["updated_at"] = FIXED_NOW
        else:
            settings.append(
                {
                    "setting_id": _stable_id("cs", name),
                    "name": name,
                    "value": version,
                    "updated_at": FIXED_NOW,
                }
            )
        return _json({"applied_version": version})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetCachePartitionKey",
                "description": "Set the cache partition key version.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "partition_key": {"type": "string"},
                        "version": {"type": "string"},
                    },
                    "required": ["partition_key", "version"],
                },
            },
        }


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


class ConfigureTraceSampling(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sample_rate: float) -> str:
        flags = _ensure_table(data, "trace_flags")
        policy_id = _stable_id("trace", f"{sample_rate:.2f}")
        row = _find_one(flags, policy_id=policy_id)
        if row:
            row["sample_rate"] = float(sample_rate)
            row["created_at"] = FIXED_NOW
        else:
            flags.append(
                {
                    "policy_id": policy_id,
                    "sample_rate": float(sample_rate),
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"policy_id": policy_id, "effective_rate": float(sample_rate)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConfigureTraceSampling",
                "description": "Configure API trace sampling rate globally.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sample_rate": {
                            "type": "number",
                            "minimum": 0.0,
                            "maximum": 1.0,
                        }
                    },
                    "required": ["sample_rate"],
                },
            },
        }


class EnableDigitalCommerceGateway(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], api_group_name: str, environment: str) -> str:
        settings = _ensure_table(data, "custom_settings")
        key = f"DCG:{api_group_name}:{environment}"
        row = _find_one(settings, name=key)
        value = json.dumps(
            {"status": "Enabled", "group": api_group_name, "env": environment}
        )
        if row:
            row["value"] = value
            row["updated_at"] = FIXED_NOW
        else:
            settings.append(
                {
                    "setting_id": _stable_id("dcg", api_group_name, environment),
                    "name": key,
                    "value": value,
                    "updated_at": FIXED_NOW,
                }
            )
        return _json(
            {
                "dcg_id": _stable_id("dcg", api_group_name, environment),
                "status": "Enabled",
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EnableDigitalCommerceGateway",
                "description": "Enable the Digital Commerce Gateway group in an environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "api_group_name": {"type": "string"},
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                    },
                    "required": ["api_group_name", "environment"],
                },
            },
        }


#--------------------------- API and Identity ---------------------------


class ConfigureConnectedAppOAuth(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        app_name_hint: str,
        scopes: list[str],
        callback_urls: list[str]
    ) -> str:
        apps = _ensure_table(data, "connected_apps")
        app_id = _stable_id("app", app_name_hint)
        row = _find_one(apps, app_id=app_id)
        client_id = _stable_id("client", app_name_hint)
        secret_arn = f"arn:aws:secretsmanager:local:000000000000:secret:{app_id}"
        payload = {
            "name": app_name_hint,
            "scopes": list(scopes),
            "callbacks": list(callback_urls),
        }
        if row:
            row.update(
                {
                    "name": app_name_hint,
                    "scopes": list(scopes),
                    "callback_urls": list(callback_urls),
                    "client_id": client_id,
                    "secret_arn": secret_arn,
                    "updated_at": FIXED_NOW,
                }
            )
        else:
            apps.append(
                {
                    "app_id": app_id,
                    "name": app_name_hint,
                    "scopes": list(scopes),
                    "callback_urls": list(callback_urls),
                    "client_id": client_id,
                    "secret_arn": secret_arn,
                    "created_at": FIXED_NOW,
                }
            )
        return _json(
            {"app_id": app_id, "client_id": client_id, "secret_arn": secret_arn}
        )
        pass
        apps = _ensure_table(data, "connected_apps")
        app_id = _stable_id("app", app_name_hint)
        row = _find_one(apps, app_id=app_id)
        client_id = _stable_id("client", app_name_hint)
        secret_arn = f"arn:aws:secretsmanager:local:000000000000:secret:{app_id}"
        payload = {
            "name": app_name_hint,
            "scopes": list(scopes),
            "callbacks": list(callback_urls),
        }
        if row:
            row.update(
                {
                    "name": app_name_hint,
                    "scopes": list(scopes),
                    "callback_urls": list(callback_urls),
                    "client_id": client_id,
                    "secret_arn": secret_arn,
                    "updated_at": FIXED_NOW,
                }
            )
        else:
            apps.append(
                {
                    "app_id": app_id,
                    "name": app_name_hint,
                    "scopes": list(scopes),
                    "callback_urls": list(callback_urls),
                    "client_id": client_id,
                    "secret_arn": secret_arn,
                    "created_at": FIXED_NOW,
                }
            )
        return _json(
            {"app_id": app_id, "client_id": client_id, "secret_arn": secret_arn}
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConfigureConnectedAppOauth",
                "description": "Configure connected app OAuth scopes and callbacks.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "app_name_hint": {"type": "string"},
                        "scopes": {"type": "array", "items": {"type": "string"}},
                        "callback_urls": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["app_name_hint", "scopes", "callback_urls"],
                },
            },
        }


class PublishOpenAPISpec(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], spec_name: str, spec_version: str, spec_blob_id: str
    ) -> str:
        settings = _ensure_table(data, "custom_settings")
        spec_id = _stable_id("spec", spec_name, spec_version)
        name = f"OpenAPI:{spec_name}"
        value = json.dumps(
            {"spec_id": spec_id, "version": spec_version, "blob": spec_blob_id}
        )
        row = _find_one(settings, name=name)
        if row:
            row["value"] = value
            row["updated_at"] = FIXED_NOW
        else:
            settings.append(
                {
                    "setting_id": _stable_id("cs", name),
                    "name": name,
                    "value": value,
                    "updated_at": FIXED_NOW,
                }
            )
        return _json({"spec_id": spec_id, "version": spec_version})
        pass
        settings = _ensure_table(data, "custom_settings")
        spec_id = _stable_id("spec", spec_name, spec_version)
        name = f"OpenAPI:{spec_name}"
        value = json.dumps(
            {"spec_id": spec_id, "version": spec_version, "blob": spec_blob_id}
        )
        row = _find_one(settings, name=name)
        if row:
            row["value"] = value
            row["updated_at"] = FIXED_NOW
        else:
            settings.append(
                {
                    "setting_id": _stable_id("cs", name),
                    "name": name,
                    "value": value,
                    "updated_at": FIXED_NOW,
                }
            )
        return _json({"spec_id": spec_id, "version": spec_version})

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PublishOpenapiSpec",
                "description": "Publish/register an OpenAPI spec artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "spec_name": {"type": "string"},
                        "spec_version": {"type": "string"},
                        "spec_blob_id": {"type": "string"},
                    },
                    "required": ["spec_name", "spec_version", "spec_blob_id"],
                },
            },
        }


class RegisterApiEndpoints(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], spec_id: str, gateway_id: str) -> str:
        settings = _ensure_table(data, "custom_settings")
        # Simple mapping (to ensure consistency, we only provide a single GET endpoint)
        endpoint_id = _stable_id("ep", spec_id, gateway_id)
        route_map = {"GET /v3/offers": endpoint_id}
        key = f"Endpoints:{spec_id}:{gateway_id}"
        row = _find_one(settings, name=key)
        val = json.dumps({"endpoint_ids": [endpoint_id], "route_map": route_map})
        if row:
            row["value"] = val
            row["updated_at"] = FIXED_NOW
        else:
            settings.append(
                {
                    "setting_id": _stable_id("cs", key),
                    "name": key,
                    "value": val,
                    "updated_at": FIXED_NOW,
                }
            )
        return _json({"endpoint_ids": [endpoint_id], "route_map": route_map})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterApiEndpoints",
                "description": "Register endpoints from an OpenAPI spec into a gateway.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "spec_id": {"type": "string"},
                        "gateway_id": {"type": "string"},
                    },
                    "required": ["spec_id", "gateway_id"],
                },
            },
        }


class RunTestCollection(Tool):
    @staticmethod
    def invoke(data, environment: str, collection_name: str = "SMOKE") -> str:
        cases = _ensure_table(data, "cases")
        run_id = _stable_id("run", collection_name, environment, FIXED_NOW)
        cases.append(
            {
                "case_id": run_id,
                "title": f"Test: {collection_name} [{environment}]",
                "status": "Passed",
                "passed": 42,
                "failed": 0,
                "duration_ms": 12000,
                "created_at": FIXED_NOW,
            }
        )
        return _json(
            {"run_id": run_id, "passed": 42, "failed": 0, "duration_ms": 12000}
        )
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "RunTestCollection",
                "description": "Execute a named API test collection. Defaults to 'SMOKE'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                        "collection_name": {"type": "string"},
                    },
                    "required": ["environment"],
                },
            },
        }


class RecordApiChangeLog(Tool):
    @staticmethod
    def invoke(data, target_id: str, environment: str, change_type: str = "ops") -> str:
        cases = _ensure_table(data, "cases")
        change_log_id = _stable_id(
            "chg", change_type, target_id, environment, FIXED_NOW
        )
        title = f"{change_type.capitalize()} – {target_id} [{environment}]"
        cases.append(
            {
                "case_id": change_log_id,
                "title": title,
                "status": "Recorded",
                "created_at": FIXED_NOW,
            }
        )
        return _json(
            {"change_log_id": change_log_id, "title": title, "timestamp": FIXED_NOW}
        )
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "RecordApiChangeLog",
                "description": "Record an API change event. Defaults change_type='ops'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_id": {"type": "string"},
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                        "change_type": {"type": "string"},
                    },
                    "required": ["target_id", "environment"],
                },
            },
        }


class DeployLambdaFunction(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        environment: str,
        service_name: str,
        source_bundle_id: str,
        function_purpose: str
    ) -> str:
        _service_nameL = service_name or ''.lower()
        _function_purposeL = function_purpose or ''.lower()
        _environmentL = environment or ''.lower()
        pass
        lambdas = _ensure_table(data, "aws_lambdas")
        fn_slug = f"{service_name.lower().replace(' ','-')}-{function_purpose.lower()}-{environment.lower()}"
        function_name = f"fn-{fn_slug}"
        function_arn = f"arn:aws:lambda:local:000000000000:function:{function_name}"
        row = _find_one(lambdas, function_arn=function_arn)
        payload = {
            "function_arn": function_arn,
            "function_name": function_name,
            "service_name": service_name,
            "environment": environment,
            "function_purpose": function_purpose,
            "source_bundle_id": source_bundle_id,
        }
        if row:
            row.update({**payload, "updated_at": FIXED_NOW})
        else:
            lambdas.append({**payload, "created_at": FIXED_NOW})
        return _json({"function_arn": function_arn, "function_name": function_name})
        _service_nameL = service_name or ''.lower()
        _function_purposeL = function_purpose or ''.lower()
        _environmentL = environment or ''.lower()
        pass
        lambdas = _ensure_table(data, "aws_lambdas")
        fn_slug = f"{service_name.lower().replace(' ','-')}-{function_purpose.lower()}-{environment.lower()}"
        function_name = f"fn-{fn_slug}"
        function_arn = f"arn:aws:lambda:local:000000000000:function:{function_name}"
        row = _find_one(lambdas, function_arn=function_arn)
        payload = {
            "function_arn": function_arn,
            "function_name": function_name,
            "service_name": service_name,
            "environment": environment,
            "function_purpose": function_purpose,
            "source_bundle_id": source_bundle_id,
        }
        if row:
            row.update({**payload, "updated_at": FIXED_NOW})
        else:
            lambdas.append({**payload, "created_at": FIXED_NOW})
        return _json({"function_arn": function_arn, "function_name": function_name})

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "DeployLambdaFunction",
                "description": "Deploy Lambda; deterministic name from service/purpose/environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                        "service_name": {"type": "string"},
                        "source_bundle_id": {"type": "string"},
                        "function_purpose": {
                            "type": "string",
                            "enum": [
                                "cache_warmer",
                                "webhook",
                                "ingest",
                                "maintenance",
                            ],
                        },
                    },
                    "required": [
                        "environment",
                        "service_name",
                        "source_bundle_id",
                        "function_purpose",
                    ],
                },
            },
        }


class CreateLambdaSchedule(Tool):
    @staticmethod
    def invoke(
        data, function_arn: str, schedule_expression: str = "rate(15 minutes)"
    ) -> str:
        schedules = _ensure_table(data, "aws_lambda_schedules")
        schedule_id = _stable_id("sched", function_arn, schedule_expression)
        rule_name = f"rule-{schedule_id}"
        row = _find_one(schedules, schedule_id=schedule_id)
        if row:
            row.update(
                {
                    "function_arn": function_arn,
                    "schedule_expression": schedule_expression,
                    "updated_at": FIXED_NOW,
                }
            )
        else:
            schedules.append(
                {
                    "schedule_id": schedule_id,
                    "rule_name": rule_name,
                    "function_arn": function_arn,
                    "schedule_expression": schedule_expression,
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"schedule_id": schedule_id, "rule_name": rule_name})
        pass
        schedules = _ensure_table(data, "aws_lambda_schedules")
        schedule_id = _stable_id("sched", function_arn, schedule_expression)
        rule_name = f"rule-{schedule_id}"
        row = _find_one(schedules, schedule_id=schedule_id)
        if row:
            row.update(
                {
                    "function_arn": function_arn,
                    "schedule_expression": schedule_expression,
                    "updated_at": FIXED_NOW,
                }
            )
        else:
            schedules.append(
                {
                    "schedule_id": schedule_id,
                    "rule_name": rule_name,
                    "function_arn": function_arn,
                    "schedule_expression": schedule_expression,
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"schedule_id": schedule_id, "rule_name": rule_name})

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateLambdaSchedule",
                "description": "Create an EventBridge schedule for a Lambda. Defaults to rate(15 minutes).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "function_arn": {"type": "string"},
                        "schedule_expression": {"type": "string"},
                    },
                    "required": ["function_arn"],
                },
            },
        }


class CreateCloudWatchAlarm(Tool):
    @staticmethod
    def invoke(
        data,
        resource_id: str,
        metric_name: str = "Errors",
        threshold: float = 1.0,
        period_seconds: int = 300,
        comparison: str = "GreaterThanOrEqualToThreshold"
    ) -> str:
        alarms = _ensure_table(data, "aws_cloudwatch_alarms")
        alarm_id = _stable_id(
            "al",
            resource_id,
            metric_name,
            str(threshold),
            str(period_seconds),
            comparison,
        )
        alarm_name = f"{metric_name}-{resource_id}"
        row = _find_one(alarms, alarm_id=alarm_id)
        payload = {
            "resource_id": resource_id,
            "metric_name": metric_name,
            "threshold": float(threshold),
            "period_seconds": int(period_seconds),
            "comparison": comparison,
        }
        if row:
            row.update(payload)
            row["state"] = "OK"
            row["updated_at"] = FIXED_NOW
        else:
            alarms.append(
                {
                    "alarm_id": alarm_id,
                    "alarm_name": alarm_name,
                    "state": "OK",
                    **payload,
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"alarm_id": alarm_id, "alarm_name": alarm_name, "state": "OK"})
        pass
        alarms = _ensure_table(data, "aws_cloudwatch_alarms")
        alarm_id = _stable_id(
            "al",
            resource_id,
            metric_name,
            str(threshold),
            str(period_seconds),
            comparison,
        )
        alarm_name = f"{metric_name}-{resource_id}"
        row = _find_one(alarms, alarm_id=alarm_id)
        payload = {
            "resource_id": resource_id,
            "metric_name": metric_name,
            "threshold": float(threshold),
            "period_seconds": int(period_seconds),
            "comparison": comparison,
        }
        if row:
            row.update(payload)
            row["state"] = "OK"
            row["updated_at"] = FIXED_NOW
        else:
            alarms.append(
                {
                    "alarm_id": alarm_id,
                    "alarm_name": alarm_name,
                    "state": "OK",
                    **payload,
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"alarm_id": alarm_id, "alarm_name": alarm_name, "state": "OK"})

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateCloudwatchAlarm",
                "description": "Create a CloudWatch alarm. Defaults: Errors, 1.0, 300s, GTE.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {"type": "string"},
                        "metric_name": {"type": "string"},
                        "threshold": {"type": "number"},
                        "period_seconds": {"type": "integer"},
                        "comparison": {"type": "string"},
                    },
                    "required": ["resource_id"],
                },
            },
        }


class CreateCloudWatchDashboard(Tool):
    @staticmethod
    def invoke(data, environment: str, purpose: str = "cache") -> str:
        dashboards = _ensure_table(data, "aws_cloudwatch_dashboards")
        dashboard_name = _stable_id("dash", environment, purpose)
        url = f"https://console.aws.amazon.com/cloudwatch/home#dashboards:name={dashboard_name}"
        row = _find_one(dashboards, dashboard_name=dashboard_name)
        payload = {
            "dashboard_name": dashboard_name,
            "purpose": purpose,
            "environment": environment,
            "url": url,
        }
        if row:
            row.update({**payload, "updated_at": FIXED_NOW})
        else:
            dashboards.append({**payload, "created_at": FIXED_NOW})
        return _json({"dashboard_name": dashboard_name, "url": url})
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateCloudwatchDashboard",
                "description": "Create a CloudWatch dashboard. Defaults purpose to 'cache'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                        "purpose": {"type": "string"},
                    },
                    "required": ["environment"],
                },
            },
        }


#── CACHE & INTEGRATION (1) ─────────────────────────────────────────────────────────────


class InvalidateCacheByKeys(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], keys: list[str]) -> str:
        inv = _ensure_table(data, "cache_invalidations")
        ts = FIXED_NOW
        for k in keys:
            inv.append({"key": k, "invalidated_at": ts})
        return _json({"invalidated_count": len(keys)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InvalidateCacheByKeys",
                "description": "Invalidate specific cache entries by key.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keys": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["keys"],
                },
            },
        }


#── CATALOG & CHECKOUT (5) ─────────────────────────────────────────────────────────────


class ResolveCatalogEntities(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], kind: str, names: list[str]) -> str:
        out = []
        if kind == "product":
            products = _ensure_table(data, "products")
            for n in names:
                row = _find_one(products, name=n) or _find_one(products, product_code=n)
                if not row:
                    # generate in a deterministic manner if absent
                    pid = _stable_id("prod", n)
                    code = n if "-" in n else f"{n.upper().replace(' ','_')}-001"
                    row = {"product_id": pid, "name": n, "product_code": code}
                    products.append(row)
                out.append(
                    {
                        "name": row.get("name", n),
                        "id": row.get("product_id"),
                        "product_code": row.get("product_code"),
                    }
                )
        elif kind == "pricebook":
            pbs = _ensure_table(data, "pricebooks")
            for n in names:
                row = _find_one(pbs, name=n)
                if not row:
                    pbid = _stable_id("pb", n)
                    row = {"pricebook_id": pbid, "name": n}
                    pbs.append(row)
                out.append({"name": row["name"], "id": row["pricebook_id"]})
        elif kind == "offer":
            offers = _ensure_table(data, "offers")
            for n in names:
                row = _find_one(offers, offer_code=n) or _find_one(offers, name=n)
                if not row:
                    oid = _stable_id("off", n)
                    row = {
                        "offer_id": oid,
                        "offer_code": n,
                        "description": n,
                        "active": False,
                    }
                    offers.append(row)
                out.append(
                    {
                        "name": row.get("name", row.get("offer_code")),
                        "id": row["offer_id"],
                    }
                )
        elif kind == "pbe":
            pbes = _ensure_table(data, "pricebook_entries")
            for n in names:
                row = _find_one(pbes, pbe_id=n)
                if row:
                    out.append(
                        {
                            "name": n,
                            "id": row["pbe_id"],
                            "product_code": row.get("product_code"),
                        }
                    )
        else:
            raise ValueError(f"Unsupported kind: {kind}")
        return _json({"entities": out})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "resolveCatalogEntities",
                "description": "Resolve names to canonical catalog entity ids and codes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kind": {
                            "type": "string",
                            "enum": ["product", "pricebook", "offer", "pbe"],
                        },
                        "names": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["kind", "names"],
                },
            },
        }


class UpsertPricebookEntriesBatch(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], pricebook_name: str, items: list[dict[str, Any]]
    ) -> str:
        pbs = _ensure_table(data, "pricebooks")
        pbes = _ensure_table(data, "pricebook_entries")
        products = _ensure_table(data, "products")

        pb = _find_one(pbs, name=pricebook_name)
        if not pb:
            pb = {
                "pricebook_id": _stable_id("pb", pricebook_name),
                "name": pricebook_name,
            }
            pbs.append(pb)

        pbe_ids = []
        for it in items:
            code = it["product_code"]
            unit_price = float(it["unit_price"])
            prod = _find_one(products, product_code=code)
            if not prod:
                prod = {
                    "product_id": _stable_id("prod", code),
                    "name": code,
                    "product_code": code,
                }
                products.append(prod)

            pbe_id = _stable_id("pbe", pb["pricebook_id"], code)
            row = _find_one(pbes, pbe_id=pbe_id)
            payload = {
                "pbe_id": pbe_id,
                "pricebook_id": pb["pricebook_id"],
                "product_code": code,
                "unit_price": unit_price,
                "updated_at": FIXED_NOW,
            }
            if row:
                row.update(payload)
            else:
                pbes.append(payload)
            pbe_ids.append(pbe_id)

        return _json({"upserted_count": len(pbe_ids), "pbe_ids": pbe_ids})
        pass
        pbs = _ensure_table(data, "pricebooks")
        pbes = _ensure_table(data, "pricebook_entries")
        products = _ensure_table(data, "products")

        pb = _find_one(pbs, name=pricebook_name)
        if not pb:
            pb = {
                "pricebook_id": _stable_id("pb", pricebook_name),
                "name": pricebook_name,
            }
            pbs.append(pb)

        pbe_ids = []
        for it in items:
            code = it["product_code"]
            unit_price = float(it["unit_price"])
            prod = _find_one(products, product_code=code)
            if not prod:
                prod = {
                    "product_id": _stable_id("prod", code),
                    "name": code,
                    "product_code": code,
                }
                products.append(prod)

            pbe_id = _stable_id("pbe", pb["pricebook_id"], code)
            row = _find_one(pbes, pbe_id=pbe_id)
            payload = {
                "pbe_id": pbe_id,
                "pricebook_id": pb["pricebook_id"],
                "product_code": code,
                "unit_price": unit_price,
                "updated_at": FIXED_NOW,
            }
            if row:
                row.update(payload)
            else:
                pbes.append(payload)
            pbe_ids.append(pbe_id)

        return _json({"upserted_count": len(pbe_ids), "pbe_ids": pbe_ids})

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertPricebookEntriesBatch",
                "description": "Upsert multiple price book entries at once.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pricebook_name": {"type": "string"},
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_code": {"type": "string"},
                                    "unit_price": {"type": "number"},
                                },
                                "required": ["product_code", "unit_price"],
                            },
                        },
                    },
                    "required": ["pricebook_name", "items"],
                },
            },
        }


class UpsertOffer(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], offer_code: str, active: bool) -> str:
        offers = _ensure_table(data, "offers")
        row = _find_one(offers, offer_code=offer_code) or _find_one(
            offers, name=offer_code
        )
        if not row:
            raise ValueError(f"Offer code not found: {offer_code}")
        row["active"] = (
            bool(active)
            if "active" in row
            else (
                bool(active)
                if "is_active" not in row
                else row.update({"is_active": bool(active)})
            )
        )
        row["updated_at"] = FIXED_NOW
        return _json(
            {
                "offer_id": row.get("offer_id") or _stable_id("off", offer_code),
                "active": bool(row.get("active") or row.get("is_active", False)),
            }
        )
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "upsertOffer",
                "description": "Activate/deactivate an existing offer by code (no free-text fields).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "offer_code": {"type": "string"},
                        "active": {"type": "boolean"},
                    },
                    "required": ["offer_code", "active"],
                },
            },
        }


class SetPricingTierForCustomer(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], customer_email: str, pricing_tier_name: str
    ) -> str:
        customers = _ensure_table(data, "customers")
        cust = _find_one(customers, email=customer_email)
        if cust:
            cust["pricing_tier"] = pricing_tier_name
            cust["updated_at"] = FIXED_NOW
            cid = cust["customer_id"]
        else:
            cid = _stable_id("cust", customer_email)
            customers.append(
                {
                    "customer_id": cid,
                    "email": customer_email,
                    "pricing_tier": pricing_tier_name,
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"customer_id": cid, "applied_tier": pricing_tier_name})
        pass
        customers = _ensure_table(data, "customers")
        cust = _find_one(customers, email=customer_email)
        if cust:
            cust["pricing_tier"] = pricing_tier_name
            cust["updated_at"] = FIXED_NOW
            cid = cust["customer_id"]
        else:
            cid = _stable_id("cust", customer_email)
            customers.append(
                {
                    "customer_id": cid,
                    "email": customer_email,
                    "pricing_tier": pricing_tier_name,
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"customer_id": cid, "applied_tier": pricing_tier_name})

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetPricingTierForCustomer",
                "description": "Apply a named pricing tier for a customer by email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_email": {"type": "string"},
                        "pricing_tier_name": {"type": "string"},
                    },
                    "required": ["customer_email", "pricing_tier_name"],
                },
            },
        }


class CreateCartWithItems(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        customer_email: str,
        items: list[dict[str, Any]],
        promo_code: str | None,
        shipping_method: str | None
    ) -> str:
        customers = _ensure_table(data, "customers")
        carts = _ensure_table(data, "carts")
        cart_items = _ensure_table(data, "cart_items")
        pbes = _ensure_table(data, "pricebook_entries")
        products = _ensure_table(data, "products")
        offers = _ensure_table(data, "offers")
        methods = _ensure_table(data, "shipping_methods")

        cust = _find_one(customers, email=customer_email)
        if not cust:
            cid = _stable_id("cust", customer_email)
            cust = {
                "customer_id": cid,
                "email": customer_email,
                "created_at": FIXED_NOW,
            }
            customers.append(cust)

        subtotal = 0.0
        lines = []
        for it in items:
            code = it["product_code"]
            qty = int(it["qty"])
            pbe = next((r for r in pbes if r.get("product_code") == code), None)
            if pbe:
                unit = float(pbe.get("unit_price", 0.0))
            else:
                prod = _find_one(products, product_code=code) or {}
                unit = float(prod.get("base_price", 0.0))
            line_total = round(unit * qty, 2)
            subtotal = round(subtotal + line_total, 2)
            lines.append(
                {
                    "product_code": code,
                    "qty": qty,
                    "unit_price": unit,
                    "line_total": line_total,
                }
            )

        discount = 0.0
        if promo_code:
            promo = _find_one(offers, offer_code=promo_code) or _find_one(
                offers, name=promo_code
            )
            if promo and bool(promo.get("active", promo.get("is_active", False))):
                dt = (promo.get("discount_type") or "").upper()
                dv = float(promo.get("discount_value", 0.0))
                if dt == "PERCENTAGE":
                    discount = round(subtotal * dv / 100.0, 2)
                elif dt == "FIXED_AMOUNT":
                    discount = round(min(dv, subtotal), 2)

        method = (shipping_method or "STANDARD").upper()
        rate_row = _find_one(methods, code=method) or {"code": "STANDARD", "rate": 5.00}
        shipping = float(rate_row.get("rate", 5.00))

        total = round(subtotal - discount + shipping, 2)
        candidate = _stable_id("cart", cust["customer_id"], FIXED_NOW)
        cart_id = _ensure_unique_id(carts, "cart_id", candidate)

        carts.append(
            {
                "cart_id": cart_id,
                "customer_id": cust["customer_id"],
                "customer_email": customer_email,
                "subtotal": subtotal,
                "discount": discount,
                "shipping": shipping,
                "total": total,
                "created_at": FIXED_NOW,
            }
        )
        for li in lines:
            cart_items.append({"cart_id": cart_id, **li})

        return _json(
            {
                "cart_id": cart_id,
                "subtotal": subtotal,
                "discount": discount,
                "shipping": shipping,
                "total": total,
                "shipping_method": method,
            }
        )
        pass
        customers = _ensure_table(data, "customers")
        carts = _ensure_table(data, "carts")
        cart_items = _ensure_table(data, "cart_items")
        pbes = _ensure_table(data, "pricebook_entries")
        products = _ensure_table(data, "products")
        offers = _ensure_table(data, "offers")
        methods = _ensure_table(data, "shipping_methods")

        cust = _find_one(customers, email=customer_email)
        if not cust:
            cid = _stable_id("cust", customer_email)
            cust = {
                "customer_id": cid,
                "email": customer_email,
                "created_at": FIXED_NOW,
            }
            customers.append(cust)

        subtotal = 0.0
        lines = []
        for it in items:
            code = it["product_code"]
            qty = int(it["qty"])
            pbe = next((r for r in pbes if r.get("product_code") == code), None)
            if pbe:
                unit = float(pbe.get("unit_price", 0.0))
            else:
                prod = _find_one(products, product_code=code) or {}
                unit = float(prod.get("base_price", 0.0))
            line_total = round(unit * qty, 2)
            subtotal = round(subtotal + line_total, 2)
            lines.append(
                {
                    "product_code": code,
                    "qty": qty,
                    "unit_price": unit,
                    "line_total": line_total,
                }
            )

        discount = 0.0
        if promo_code:
            promo = _find_one(offers, offer_code=promo_code) or _find_one(
                offers, name=promo_code
            )
            if promo and bool(promo.get("active", promo.get("is_active", False))):
                dt = (promo.get("discount_type") or "").upper()
                dv = float(promo.get("discount_value", 0.0))
                if dt == "PERCENTAGE":
                    discount = round(subtotal * dv / 100.0, 2)
                elif dt == "FIXED_AMOUNT":
                    discount = round(min(dv, subtotal), 2)

        method = (shipping_method or "STANDARD").upper()
        rate_row = _find_one(methods, code=method) or {"code": "STANDARD", "rate": 5.00}
        shipping = float(rate_row.get("rate", 5.00))

        total = round(subtotal - discount + shipping, 2)
        candidate = _stable_id("cart", cust["customer_id"], FIXED_NOW)
        cart_id = _ensure_unique_id(carts, "cart_id", candidate)

        carts.append(
            {
                "cart_id": cart_id,
                "customer_id": cust["customer_id"],
                "customer_email": customer_email,
                "subtotal": subtotal,
                "discount": discount,
                "shipping": shipping,
                "total": total,
                "created_at": FIXED_NOW,
            }
        )
        for li in lines:
            cart_items.append({"cart_id": cart_id, **li})

        return _json(
            {
                "cart_id": cart_id,
                "subtotal": subtotal,
                "discount": discount,
                "shipping": shipping,
                "total": total,
                "shipping_method": method,
            }
        )

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateCartWithItems",
                "description": "Create a cart; auto-calc prices, promo, and shipping method.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_email": {"type": "string"},
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_code": {"type": "string"},
                                    "qty": {"type": "integer", "minimum": 1},
                                },
                                "required": ["product_code", "qty"],
                            },
                        },
                        "promo_code": {"type": "string"},
                        "shipping_method": {
                            "type": "string",
                            "description": "e.g., STANDARD, EXPRESS, OVERNIGHT",
                        },
                    },
                    "required": ["customer_email", "items"],
                },
            },
        }


#── PERSONALIZATION & PROMOTIONS (2) ───────────────────────────────────────────────────


class UpsertPromotion(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], code: str, active: bool) -> str:
        offers = _ensure_table(data, "offers")
        row = _find_one(offers, offer_code=code) or _find_one(offers, name=code)
        if not row:
            raise ValueError(f"Promotion code not found: {code}")
        if "is_active" in row:
            row["is_active"] = bool(active)
        else:
            row["active"] = bool(active)
        row["updated_at"] = FIXED_NOW
        return _json(
            {
                "promo_id": row.get("offer_id") or _stable_id("promo", code),
                "active": bool(row.get("active") or row.get("is_active", False)),
            }
        )
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpsertPromotion",
                "description": "Activate/deactivate an existing promotion by code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "code": {"type": "string"},
                        "active": {"type": "boolean"},
                    },
                    "required": ["code", "active"],
                },
            },
        }


class UpsertContextRule(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        segment_name: str,
        rule_name_hint: str,
        attributes: dict[str, Any],
        bind_to_offer_code: str | None
    ) -> str:
        rules = _ensure_table(data, "context_rules")
        binds = _ensure_table(data, "context_rule_bindings")

        context_rule_id = _stable_id("ctx", segment_name, rule_name_hint)
        title = f"{segment_name} – {rule_name_hint}"
        row = _find_one(rules, context_rule_id=context_rule_id)
        if row:
            row.update(
                {
                    "segment_name": segment_name,
                    "rule_name_hint": rule_name_hint,
                    "attributes": attributes,
                    "title": title,
                    "updated_at": FIXED_NOW,
                }
            )
        else:
            rules.append(
                {
                    "context_rule_id": context_rule_id,
                    "segment_name": segment_name,
                    "rule_name_hint": rule_name_hint,
                    "attributes": attributes,
                    "title": title,
                    "created_at": FIXED_NOW,
                }
            )

        binding_id = None
        if bind_to_offer_code:
            binding_id = _stable_id("bind", context_rule_id, bind_to_offer_code)
            existing = _find_one(binds, binding_id=binding_id)
            if existing:
                existing.update(
                    {"offer_code": bind_to_offer_code, "updated_at": FIXED_NOW}
                )
            else:
                binds.append(
                    {
                        "binding_id": binding_id,
                        "context_rule_id": context_rule_id,
                        "offer_code": bind_to_offer_code,
                        "created_at": FIXED_NOW,
                    }
                )

        return _json(
            {
                "context_rule_id": context_rule_id,
                "binding_id": binding_id,
                "title": title,
            }
        )
        pass
        rules = _ensure_table(data, "context_rules")
        binds = _ensure_table(data, "context_rule_bindings")

        context_rule_id = _stable_id("ctx", segment_name, rule_name_hint)
        title = f"{segment_name} – {rule_name_hint}"
        row = _find_one(rules, context_rule_id=context_rule_id)
        if row:
            row.update(
                {
                    "segment_name": segment_name,
                    "rule_name_hint": rule_name_hint,
                    "attributes": attributes,
                    "title": title,
                    "updated_at": FIXED_NOW,
                }
            )
        else:
            rules.append(
                {
                    "context_rule_id": context_rule_id,
                    "segment_name": segment_name,
                    "rule_name_hint": rule_name_hint,
                    "attributes": attributes,
                    "title": title,
                    "created_at": FIXED_NOW,
                }
            )

        binding_id = None
        if bind_to_offer_code:
            binding_id = _stable_id("bind", context_rule_id, bind_to_offer_code)
            existing = _find_one(binds, binding_id=binding_id)
            if existing:
                existing.update(
                    {"offer_code": bind_to_offer_code, "updated_at": FIXED_NOW}
                )
            else:
                binds.append(
                    {
                        "binding_id": binding_id,
                        "context_rule_id": context_rule_id,
                        "offer_code": bind_to_offer_code,
                        "created_at": FIXED_NOW,
                    }
                )

        return _json(
            {
                "context_rule_id": context_rule_id,
                "binding_id": binding_id,
                "title": title,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertContextRule",
                "description": "Create/update a context rule and optionally bind it to an offer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "segment_name": {"type": "string"},
                        "rule_name_hint": {"type": "string"},
                        "attributes": {"type": "object"},
                        "bind_to_offer_code": {"type": "string"},
                    },
                    "required": ["segment_name", "rule_name_hint", "attributes"],
                },
            },
        }


class GetCacheCluster(Tool):
    @staticmethod
    def invoke(data, cluster_id: str, endpoint_url: str = None, instance_type: str = None, security_group_id: str = None, status: str = None) -> str:
        rows = data.setdefault("aws_elasticache_clusters", [])
        row = next((r for r in rows if str(r.get("cluster_id")) == cluster_id), None)
        if not row:
            raise ValueError(f"cache cluster not found: {cluster_id}")
        payload = {
            "cluster_id": row["cluster_id"],
            "endpoint_url": row["endpoint_url"],
            "instance_type": row["instance_type"],
            "security_group_id": row["security_group_id"],
            "status": row["status"],
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetCacheCluster",
                "description": "Read existing ElastiCache cluster by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"cluster_id": {"type": "string"}},
                    "required": ["cluster_id"],
                },
            },
        }


class GetOfferByCode(Tool):
    @staticmethod
    def invoke(data, offer_code: str, offer_id: str = None, id: str = None, discount_type: str = None, discount_value: float = None, is_active: bool = None, active: bool = False) -> str:
        rows = data.setdefault("offers", [])
        row = next((r for r in rows if str(r.get("offer_code")) == offer_code), None)
        if not row:
            raise ValueError(f"offer not found: {offer_code}")
        payload = {
            "offer_id": row.get("offer_id") or row.get("id"),
            "offer_code": row["offer_code"],
            "discount_type": row.get("discount_type"),
            "discount_value": row.get("discount_value"),
            "is_active": bool(row.get("is_active", row.get("active", False))),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetOfferByCode",
                "description": "Read an existing promotion/offer by code.",
                "parameters": {
                    "type": "object",
                    "properties": {"offer_code": {"type": "string"}},
                    "required": ["offer_code"],
                },
            },
        }


class GetPricebookByName(Tool):
    @staticmethod
    def invoke(data, pricebook_name: str) -> str:
        rows = data.setdefault("pricebooks", [])
        row = next(
            (
                r
                for r in rows
                if str(r.get("pricebook_name")) == pricebook_name
                or str(r.get("name")) == pricebook_name
            ),
            None,
        )
        if not row:
            raise ValueError(f"pricebook not found: {pricebook_name}")
        payload = {
            "pricebook_id": row.get("pricebook_id") or row.get("id"),
            "pricebook_name": row.get("pricebook_name") or row.get("name"),
            "is_active": bool(row.get("is_active", True)),
            "is_standard": bool(row.get("is_standard", False)),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetPricebookByName",
                "description": "Read an existing pricebook by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"pricebook_name": {"type": "string"}},
                    "required": ["pricebook_name"],
                },
            },
        }


class GetProductByName(Tool):
    @staticmethod
    def invoke(data, name: str) -> str:
        rows = data.setdefault("products", [])
        row = next((r for r in rows if str(r.get("name")) == name), None)
        if not row:
            raise ValueError(f"product not found: {name}")
        payload = {
            "product_id": row["product_id"],
            "name": row["name"],
            "sku": row.get("sku") or row.get("product_code"),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetProductByName",
                "description": "Read an existing product by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class GetSecurityGroupRules(Tool):
    @staticmethod
    def invoke(data, security_group_id: str) -> str:
        rows = data.setdefault("aws_security_group_rules", [])
        rules = [
            r for r in rows if str(r.get("security_group_id")) == security_group_id
        ]
        payload = {"security_group_id": security_group_id, "rules": rules}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getSecurityGroupRules",
                "description": "Read all rules for a given security group.",
                "parameters": {
                    "type": "object",
                    "properties": {"security_group_id": {"type": "string"}},
                    "required": ["security_group_id"],
                },
            },
        }


TOOLS = [
    GetEnvironmentNetworkDefaults(),
    GetServiceSecurityGroup(),
    UpdateSecurityGroupRuleset(),
    ProvisionOrUpdateRedisCluster(),
    SetRedisAuthAndTLS(),
    CreateInterfaceEndpoint(),
    DeployLambdaFunction(),
    CreateLambdaSchedule(),
    CreateCloudWatchAlarm(),
    CreateCloudWatchDashboard(),
    CreateSecretFor(),
    GetProductByName(),
    ConfigureCacheIntegration(),
    RunCacheWarmJobs(),
    SetCachePartitionKey(),
    InvalidateCacheByKeys(),
    ManageCacheMaintenance(),
    ConfigureTraceSampling(),
    EnableDigitalCommerceGateway(),
    ConfigureConnectedAppOAuth(),
    PublishOpenAPISpec(),
    RegisterApiEndpoints(),
    RunTestCollection(),
    RecordApiChangeLog(),
    GetOfferByCode(),
    GetCacheCluster(),
    GetPricebookByName(),
    ResolveCatalogEntities(),
    UpsertPricebookEntriesBatch(),
    UpsertOffer(),
    SetPricingTierForCustomer(),
    CreateCartWithItems(),
    GetSecurityGroupRules(),
    UpsertPromotion(),
    UpsertContextRule(),
]
