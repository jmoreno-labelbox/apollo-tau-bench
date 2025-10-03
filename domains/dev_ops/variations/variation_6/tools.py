import json
from typing import Any

from domains.dto import Tool

FIXED_TS = "2025-01-27T10:00:00Z"


def _table(db: dict[str, Any], name: str) -> list[dict[str, Any]]:
    pass
    return db.get(name, [])


def _ok(payload: dict[str, Any]) -> str:
    pass
    payload = {"ok": True, **payload}
    out = json.dumps(payload, indent=2)
    return out


def _loc_table(db: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    return db.get("loc_strings") or db.get("loc_strongs") or []


def _err(msg: str) -> str:
    pass
    payload = {"ok": False, "error": msg}
    out = json.dumps(payload, indent=2)
    return out


class GetLocString(Tool):
    """Retrieve a localization string row using string_key; locale entry can be included optionally."""

    @staticmethod
    def invoke(data: dict[str, Any], string_key: str = None, locale: str = None) -> str:
        rows = _loc_table(data)
        for row in rows:
            if row.get("string_key") == string_key:
                if locale:
                    entry = (row.get("translations") or {}).get(locale)
                    payload = {"loc_string": row, "locale_entry": entry}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                payload = {"loc_string": row}
                out = json.dumps(payload, indent=2)
                return out
        return _err(f"string_key not found: {string_key}")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLocString",
                "description": "Fetch a loc string by string_key (optionally include a single-locale view).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "string_key": {"type": "string"},
                        "locale": {"type": "string"},
                    },
                    "required": ["string_key"],
                },
            },
        }


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

        if any(j.get("id") == jid for j in jobs):
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


class RecordTranslations(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], entries: list = None, reflect_in_loc: bool = True) -> str:
        if entries is None:
            entries = []
        reflect = bool(reflect_in_loc)
        translations = _table(data, "translations")
        loc_rows = _loc_table(data)
        ALLOWED = {"loc_string_id", "string_key", "locale", "target_string", "metadata"}

        added = 0
        for e_in in entries:
            e = {k: v for k, v in e_in.items() if k in ALLOWED}
            eid = f"translation_{len(translations) + 1:04d}"
            e["id"] = eid
            if any(t.get("id") == eid for t in translations):
                continue

            translations.append(e)
            added += 1

            if reflect:
                lsid = e.get("loc_string_id")
                skey = e.get("string_key")
                locale = e.get("locale")
                target = e.get("target_string")
                for row in loc_rows:
                    if (lsid and row.get("id") == lsid) or (
                        skey and row.get("string_key") == skey
                    ):
                        row.setdefault("translations", {})
                        loc_entry = row["translations"].setdefault(locale, {})
                        loc_entry["translation"] = target
                        loc_entry["status"] = loc_entry.get("status", "translated")
                        loc_entry["validation_status"] = loc_entry.get(
                            "validation_status", "pending"
                        )
                        if e.get("metadata") is not None:
                            loc_entry["metadata"] = e["metadata"]
                        break
        return _ok({"added_count": added})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "recordTranslations",
                "description": "Append translation entries and (optionally) reflect into loc_strings. Mirrors per-entry metadata when provided.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entries": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "loc_string_id": {"type": "string"},
                                    "string_key": {"type": "string"},
                                    "locale": {"type": "string"},
                                    "target_string": {"type": "string"},
                                    "metadata": {"type": "object"},
                                },
                                "required": ["locale", "target_string"],
                            },
                        },
                        "reflect_in_loc": {"type": "boolean"},
                    },
                    "required": ["entries"],
                },
            },
        }


class UpdateLocaleValidation(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        loc_string_id: str = None,
        string_key: str = None,
        locale: str = None,
        validation_status: str = None,
        validation_error: str = None,
        metadata: dict[str, Any] = None
    ) -> str:
        loc_rows = _loc_table(data)
        target_row: dict[str, Any] | None = None
        for row in loc_rows:
            if (
                loc_string_id
                and row.get("id") == loc_string_id
                or (string_key and row.get("string_key") == string_key)
            ):
                target_row = row
                break
        if not target_row:
            return _err("loc string not found")
        target_row.setdefault("translations", {})
        entry = target_row["translations"].setdefault(locale, {})
        if validation_status is not None:
            entry["validation_status"] = validation_status
        if validation_error is not None:
            entry["validation_error"] = validation_error
        if metadata is not None:
            entry["metadata"] = metadata
        return _ok(
            {
                "updated": {
                    "string_key": target_row.get("string_key"),
                    "locale": locale,
                    "validation_status": validation_status,
                    "validation_error": validation_error,
                }
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateLocaleValidation",
                "description": "Update locale validation and mirror into translations. Optionally attach CI/linkage metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loc_string_id": {"type": "string"},
                        "string_key": {"type": "string"},
                        "locale": {"type": "string"},
                        "validation_status": {"type": "string"},
                        "validation_error": {"type": "string"},
                        "metadata": {"type": "object"},
                    },
                    "required": ["locale"],
                },
            },
        }


class LinkWorkItems(Tool):
    """Establish or verify a link {parent_id, child_id, link_type} (idempotent)."""

    @staticmethod
    def invoke(data: dict[str, Any], parent_id: str = None, child_id: str = None, link_type: str = "relates_to") -> str:
        if not parent_id or not child_id:
            return _err("parent_id and child_id are required")
        if parent_id == child_id:
            return _err("cannot link an item to itself")
        links = _table(data, "work_item_links")
        for l in links:
            if (
                l.get("parent_id") == parent_id
                and l.get("child_id") == child_id
                and (l.get("link_type") == link_type)
            ):
                return _ok(
                    {
                        "message": "link already exists",
                        "parent_id": parent_id,
                        "child_id": child_id,
                        "link_type": link_type,
                    }
                )
        links.append(
            {"parent_id": parent_id, "child_id": child_id, "link_type": link_type}
        )
        return _ok(
            {
                "created_link": {
                    "parent_id": parent_id,
                    "child_id": child_id,
                    "link_type": link_type,
                }
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "linkWorkItems",
                "description": "Link two work items (parent/child/link_type).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "parent_id": {"type": "string"},
                        "child_id": {"type": "string"},
                        "link_type": {"type": "string"},
                    },
                    "required": ["parent_id", "child_id"],
                },
            },
        }


class TagWorkItemWithLabel(Tool):
    """Assign a label to a work item; generate label by name if necessary (deterministic ids)."""

    @staticmethod
    def invoke(data: dict[str, Any], work_item_id: str = None, label_id: str = None, label_name: str = None) -> str:
        labels = _table(data, "labels")
        wils = _table(data, "work_item_labels")
        if not label_id:
            if not label_name:
                return _err("either label_id or label_name must be provided")
            found = next((l for l in labels if l.get("name") == label_name), None)
            if found:
                label_id = found.get("id")
            else:
                label_id = f"label_{len(labels) + 1:03d}"
                labels.append(
                    {
                        "id": label_id,
                        "project_id": "project_001",
                        "name": label_name,
                        "color": "#000000",
                    }
                )
        for m in wils:
            if m.get("work_item_id") == work_item_id and m.get("label_id") == label_id:
                return _ok(
                    {
                        "message": "label already attached",
                        "work_item_id": work_item_id,
                        "label_id": label_id,
                    }
                )
        wils.append({"work_item_id": work_item_id, "label_id": label_id})
        return _ok({"tagged": {"work_item_id": work_item_id, "label_id": label_id}})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "tagWorkItemWithLabel",
                "description": "Attach a label to a work item (idempotent).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "work_item_id": {"type": "string"},
                        "label_id": {"type": "string"},
                        "label_name": {"type": "string"},
                    },
                    "required": ["work_item_id"],
                },
            },
        }


class SendNotification(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: str = None,
        project_id: str = "project_001",
        notification_type: str = "info",
        title: str = "",
        message: str = "",
        recipient_id: str = "user_000",
        channel: str = "slack",
        sent_at: str = FIXED_TS,
        read_at: str = None,
        metadata: dict[str, Any] = None
    ) -> str:
        notifications = _table(data, "notifications")
        nid = id
        #--- FIX: Create ID if it is not supplied ---
        if not nid:
            nid = f"notification_{len(notifications) + 1:04d}"

        if any(n.get("id") == nid for n in notifications):
            return _err(f"notification id {nid} already exists")
        record = {
            "id": nid,
            "project_id": project_id,
            "notification_type": notification_type,
            "title": title,
            "message": message,
            "recipient_id": recipient_id,
            "channel": channel,
            "sent_at": sent_at,
            "read_at": read_at,
        }
        if not record["message"]:
            return _err("message must be non-empty")
        if metadata is not None:
            record["metadata"] = metadata
        notifications.append(record)
        return _ok({"notification": record})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "sendNotification",
                "description": "Record a notification (deterministic timestamp). Optionally include CI/linkage metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "project_id": {"type": "string"},
                        "notification_type": {"type": "string"},
                        "title": {"type": "string"},
                        "message": {"type": "string"},
                        "recipient_id": {"type": "string"},
                        "channel": {"type": "string"},
                        "sent_at": {"type": "string"},
                        "read_at": {"type": "string"},
                        "metadata": {"type": "object"},
                    },
                    "required": ["message"],
                },
            },
        }


class UpdateSubtitleTiming(Tool):
    """Modify subtitle_timing row fields (e.g., subtitle_start/end/text) with basic safeguards."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: Any = None,
        sub_id: str = None,
        updates: dict[str, Any] = None
    ) -> str:
        if updates is None:
            updates = {}
        table = _table(data, "subtitle_timing")
        row = next((r for r in table if r.get("id") == sub_id), None)
        if not row:
            return _err(f"subtitle_timing id not found: {sub_id}")
        if "subtitle_start" in updates and "subtitle_end" in updates:
            s, e = (updates["subtitle_start"], updates["subtitle_end"])
            if not (isinstance(s, (int, float)) and isinstance(e, (int, float))):
                return _err("subtitle_start/subtitle_end must be numeric")
            if not 0 <= s < e:
                return _err("subtitle_start must be >= 0 and < subtitle_end")
        row.update(updates)
        return _ok({"updated_subtitle": {"id": sub_id, "applied_updates": updates}})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateSubtitleTiming",
                "description": "Update a subtitle_timing record with basic timing guards.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["id", "updates"],
                },
            },
        }


class CreateLocalizationWorkflow(Tool):
    """Generate a localization_workflow record (deterministic; will error on duplicate id)."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: str = None,
        pr_number: int = None,
        changed_keys: list = None,
        locales_processed: list = None,
        bundle_uris: dict = None,
        overflow_issues: int = 0,
        tms_job_id: str = None,
        status: str = "queued",
        timestamp: str = FIXED_TS,
        metadata: dict = None
    ) -> str:
        pass
        table = _table(data, "localization_workflow")
        wid = id
        #--- FIX: Create ID if it is not supplied ---
        if not wid:
            wid = f"loc_workflow_{len(table) + 1:04d}"

        if any(w.get("id") == wid for w in table):
            return _err(f"localization_workflow id {wid} already exists")
        record = {
            "id": wid,
            "pr_number": pr_number,
            "changed_keys": changed_keys or [],
            "locales_processed": locales_processed or [],
            "bundle_uris": bundle_uris or {},
            "overflow_issues": overflow_issues,
            "tms_job_id": tms_job_id,
            "status": status,
            "timestamp": timestamp,
            "metadata": metadata or {},
        }
        table.append(record)
        return _ok({"localization_workflow": record})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createLocalizationWorkflow",
                "description": "Create a localization_workflow record (deterministic fields).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "changed_keys": {"type": "array", "items": {"type": "string"}},
                        "locales_processed": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "bundle_uris": {"type": "object"},
                        "overflow_issues": {"type": "integer"},
                        "tms_job_id": {"type": "string"},
                        "status": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "metadata": {"type": "object"},
                    },
                    "required": ["pr_number", "changed_keys"],
                },
            },
        }


class GetBuildRun(Tool):
    """Retrieve a build run using id; can optionally filter by commit_sha."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None, commit_sha: str = None) -> str:
        rid = id
        commit = commit_sha
        rows = _table(data, "build_runs")
        row = next(
            (
                r
                for r in rows
                if rid
                and r.get("id") == rid
                or (commit and r.get("commit_sha") == commit)
            ),
            None,
        )
        return _ok({"build_run": row}) if row else _err("build_run not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getBuildRun",
                "description": "Fetch a build run by id (or commit_sha).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "commit_sha": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class GetSourceChange(Tool):
    """Retrieve a source change using commit_sha or id."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None, commit_sha: str = None) -> str:
        rows = _table(data, "source_changes")
        row = next(
            (
                r
                for r in rows
                if id and r.get("id") == id or (commit_sha and r.get("commit_sha") == commit_sha)
            ),
            None,
        )
        return _ok({"source_change": row}) if row else _err("source_change not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getSourceChange",
                "description": "Fetch a source change by commit_sha (or id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "commit_sha": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class GetTestResult(Tool):
    """Retrieve a test result using id."""

    @staticmethod
    def invoke(data: dict[str, Any], id: Any = None) -> str:
        tid = id
        rows = _table(data, "test_results")
        row = next((r for r in rows if r.get("id") == tid), None)
        return _ok({"test_result": row}) if row else _err("test_result not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTestResult",
                "description": "Fetch a test result by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


class GetAutomationRun(Tool):
    """Retrieve an automation run using id."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        rows = _table(data, "automation_runs")
        row = next((r for r in rows if r.get("id") == id), None)
        return _ok({"automation_run": row}) if row else _err("automation_run not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAutomationRun",
                "description": "Fetch an automation run by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


class GetOwnershipForPath(Tool):
    """Retrieve ownership entry for a specified file_path."""

    @staticmethod
    def invoke(data: dict[str, Any], file_path: str = None) -> str:
        path = file_path
        rows = _table(data, "ownership_map")
        row = next((r for r in rows if r.get("file_path") == path), None)
        return _ok({"ownership": row}) if row else _err("ownership not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOwnershipForPath",
                "description": "Fetch ownership record by file_path.",
                "parameters": {
                    "type": "object",
                    "properties": {"file_path": {"type": "string"}},
                    "required": ["file_path"],
                },
            },
        }


class GetAsset(Tool):
    """Retrieve an asset using asset_path or id."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None, asset_path: str = None) -> str:
        rows = _table(data, "asset_catalog")
        row = next(
            (
                r
                for r in rows
                if id
                and r.get("id") == id
                or (asset_path and r.get("asset_path") == asset_path)
            ),
            None,
        )
        return _ok({"asset": row}) if row else _err("asset not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAsset",
                "description": "Fetch an asset by asset_path (or id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "asset_path": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class GetTmsJob(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        rows = _table(data, "tms_jobs")
        row = next((r for r in rows if r.get("id") == id), None)
        return _ok({"tms_job": row}) if row else _err("tms_job not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTmsJob",
                "description": "Fetch TMS job by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


class GetLocalizationWorkflow(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        wid = id
        rows = _table(data, "localization_workflow")
        row = next((r for r in rows if r.get("id") == wid), None)
        return (
            _ok({"localization_workflow": row})
            if row
            else _err("localization_workflow not found")
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLocalizationWorkflow",
                "description": "Fetch localization_workflow by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


TOOLS = [
    GetLocString(),
    CreateTmsJob(),
    RecordTranslations(),
    UpdateLocaleValidation(),
    LinkWorkItems(),
    TagWorkItemWithLabel(),
    SendNotification(),
    UpdateSubtitleTiming(),
    CreateLocalizationWorkflow(),
    GetBuildRun(),
    GetSourceChange(),
    GetTestResult(),
    GetAutomationRun(),
    GetOwnershipForPath(),
    GetAsset(),
    GetTmsJob(),
    GetLocalizationWorkflow(),
]
