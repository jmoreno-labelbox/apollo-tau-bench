import json
from typing import Any

from domains.dto import Tool


def _id_from_request(prefix: str, request_id: str) -> str:
    pass
    rid = (request_id or "").strip()
    if not rid:
        return None
    return f"{prefix}_{rid}"


def _resolve_bot_email(data: dict[str, Any]) -> str:
    pass
    cfg = data.get("system_config", None)

    #structure of the dictionary
    if isinstance(cfg, dict):
        val = cfg.get("bot_email")
        if isinstance(val, str) and "@" in val:
            return val

    #shape of the list(s)
    if isinstance(cfg, list):
        for el in cfg:
            #pair of list and tuple
            if isinstance(el, (list, tuple)) and len(el) == 2:
                k, v = el[0], el[1]
                if k == "bot_email" and isinstance(v, str) and "@" in v:
                    return v
            #element of the dictionary
            if isinstance(el, dict):
                v = el.get("bot_email")
                if isinstance(v, str) and "@" in v:
                    return v

    #plain string (is this already an email?)
    if isinstance(cfg, str) and "@" in cfg:
        return cfg.strip()

    #not located → alternative
    return "bot@company.com"


def _ymd(iso_ts: str) -> str:
    pass
    #'2024-08-23T10:00:00Z' becomes '2024-08-23'
    return (iso_ts or "").split("T")[0]


def _norm_list(values: list[str]) -> list[str]:
    pass
    return sorted(list(dict.fromkeys(values or [])))


def _get_next_id(prefix: str, existing_ids: list[str]) -> str:
    pass
    max_id_num = 0
    seen = False
    for s in existing_ids:
        if isinstance(s, str) and s.startswith(prefix + "_"):
            seen = True
            try:
                n = int(s.split("_")[-1])
                if n > max_id_num:
                    max_id_num = n
            except Exception:
                pass
    return f"{prefix}_{(1 if not seen else max_id_num + 1):03d}"

#-----------------------
#Auxiliary functions
#-----------------------


def _table(data: dict[str, Any], name: str) -> list[dict[str, Any]]:
    pass
    tbl = data.get(name)
    if not isinstance(tbl, list):
        tbl = []
        data[name] = tbl
    return tbl


def _iter_dict_rows(obj: Any):
    pass
    if isinstance(obj, dict):
        yield obj
        for v in obj.values():
            if isinstance(v, (list, dict)):
                yield from _iter_dict_rows(v)
    elif isinstance(obj, list):
        for x in obj:
            yield from _iter_dict_rows(x)


#-----------------------
#Accessible Tools
#-----------------------


class create_review_cycle(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cycle_id: str,
        artifact_id: str,
        started_at: str,
        timestamp: str,
        request_id: str,
        recipients: list[str],
    ) -> str:
        cycles = data.setdefault("review_cycles", [])
        for c in cycles:
            if isinstance(c, dict) and c.get("cycle_id") == cycle_id:
                if not c.get("recipients"):
                    c["recipients"] = sorted(list(dict.fromkeys(recipients or [])))
                payload = c
                out = json.dumps(payload, indent=2)
                return out
        row = {
            "cycle_id": cycle_id,
            "artifact_id": artifact_id,
            "status": "NEEDS_REVIEW",
            "started_at": started_at,
            "approvals_recorded": 0,
            "thread_id_nullable": None,
            "recipients": sorted(list(dict.fromkeys(recipients or []))),
            "sla_days": None,
            "day": (timestamp or "").split("T")[0],
        }
        cycles.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReviewCycle",
                "description": "Create or reuse a deterministic review cycle row; stores recipients.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "artifact_id": {"type": "string"},
                        "started_at": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                        "recipients": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "cycle_id",
                        "artifact_id",
                        "started_at",
                        "timestamp",
                        "request_id",
                        "recipients",
                    ],
                },
            },
        }


class link_cycle_to_thread(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str, thread_id: str) -> str:
        cycles = data.setdefault("review_cycles", [])
        threads = data.setdefault("gmail_threads", [])
        if not any(
            isinstance(t, dict) and t.get("thread_id") == thread_id for t in threads
        ):
            payload = {"error": f"thread_id '{thread_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        cyc = next(
            (
                c
                for c in cycles
                if isinstance(c, dict) and c.get("cycle_id") == cycle_id
            ),
            None,
        )
        if not cyc:
            payload = {"error": f"cycle_id '{cycle_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        cyc["thread_id_nullable"] = thread_id
        payload = {"cycle_id": cyc["cycle_id"], "thread_id": thread_id}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkCycleToThread",
                "description": "Link an existing Gmail thread to a review cycle (writes thread_id_nullable).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "thread_id": {"type": "string"},
                    },
                    "required": ["cycle_id", "thread_id"],
                },
            },
        }


class export_assets(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str,
        export_profile: str,
        timestamp: str,
        request_id: str,
    ) -> str:
        assets = data.setdefault("assets", [])
        day_iso = (timestamp or "").split("T")[0]
        day_compact = day_iso.replace("-", "")
        prof = (export_profile or "").upper()
        fmt = "png" if "PNG" in prof else ("pdf" if "PDF" in prof else "bin")

        asset_id = _id_from_request("asset", request_id) or _get_next_id(
            "asset", [r.get("asset_id", "") for r in assets if isinstance(r, dict)]
        )
        export_id = f"exp-{artifact_id}-{day_compact}-{fmt}-001"

        for a in assets:
            if isinstance(a, dict) and a.get("asset_id") == asset_id:
                a.setdefault("export_id", export_id)
                payload = {"asset_id": asset_id, "export_id": a["export_id"]}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        row = {
            "asset_id": asset_id,
            "artifact_id_nullable": artifact_id,
            "export_profile": export_profile,
            "mime_type": (
                "image/png"
                if fmt == "png"
                else ("application/pdf" if fmt == "pdf" else "application/octet-stream")
            ),
            "file_name": f"{artifact_id}_{export_profile.replace(' ', '').lower()}.{fmt}",
            "size_bytes": 0,
            "day": day_iso,
            "export_id": export_id,
        }
        assets.append(row)
        payload = {"asset_id": asset_id, "export_id": export_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportAssets",
                "description": "Export/reuse an asset deterministically and return both asset_id and export_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "export_profile": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "artifact_id",
                        "export_profile",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }


class create_release_record(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], artifact_id: str, timestamp: str, request_id: str
    ) -> str:
        releases = data.setdefault("releases", [])
        day_iso = (timestamp or "").split("T")[0]
        day_compact = day_iso.replace("-", "")
        release_id = f"rel-{artifact_id}-{day_compact}-001"

        for r in releases:
            if isinstance(r, dict) and r.get("release_id") == release_id:
                payload = r
                out = json.dumps(payload, indent=2)
                return out

        row = {
            "release_id": release_id,
            "artifact_id": artifact_id,
            "day": day_iso,
            "request_id": request_id,
        }
        releases.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReleaseRecord",
                "description": "Create/reuse a deterministic release row (rel-<artifact>-<YYYYMMDD>-001).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["artifact_id", "timestamp", "request_id"],
                },
            },
        }


class create_gmail_thread(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        subject: str,
        sender_email: str,
        recipients: list[str],
        labels: list[str],
        timestamp: str,
        request_id: str,
    ) -> str:
        threads = _table(data, "gmail_threads")
        thr_id = _id_from_request("thr", request_id)
        if thr_id:
            for t in threads:
                if isinstance(t, dict) and t.get("thread_id") == thr_id:
                    payload = t
                    out = json.dumps(payload, indent=2)
                    return out

        row = {
            "thread_id": thr_id
            or _get_next_id(
                "thread",
                [r.get("thread_id", "") for r in threads if isinstance(r, dict)],
            ),
            "subject": subject,
            "to": _norm_list(recipients),
            "current_labels": _norm_list(labels),
            "sender_email": sender_email,
            "day": _ymd(timestamp),
        }
        threads.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateGmailThread",
                "description": "Create or reuse a deterministic thread (thr_<request_id>).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "sender_email": {"type": "string"},
                        "recipients": {"type": "array", "items": {"type": "string"}},
                        "labels": {"type": "array", "items": {"type": "string"}},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "subject",
                        "sender_email",
                        "recipients",
                        "labels",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }


class append_gmail_message(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        thread_id: str,
        sender_email: str,
        recipients: list[str],
        body_html: str,
        attachments_asset_ids: list[str],
        timestamp: str,
        request_id: str,
    ) -> str:
        threads = _table(data, "gmail_threads")
        if not any(
            isinstance(t, dict) and t.get("thread_id") == thread_id for t in threads
        ):
            payload = {"error": f"thread_id '{thread_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        assets = _table(data, "assets")
        for aid in attachments_asset_ids or []:
            if not any(
                isinstance(a, dict) and a.get("asset_id") == aid for a in assets
            ):
                payload = {"error": f"attachment asset_id '{aid}' not found"}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        msgs = _table(data, "gmail_messages")
        msg_id = _id_from_request("msg", request_id)
        if msg_id:
            for m in msgs:
                if isinstance(m, dict) and m.get("message_id") == msg_id:
                    payload = m
                    out = json.dumps(payload, indent=2)
                    return out

        row = {
            "message_id": msg_id
            or _get_next_id(
                "msg", [m.get("message_id", "") for m in msgs if isinstance(m, dict)]
            ),
            "thread_id": thread_id,
            "sender_email": sender_email,
            "recipients": _norm_list(recipients),
            "body_html": body_html,
            "attachments": list(attachments_asset_ids or []),
            "day": _ymd(timestamp),
        }
        msgs.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendGmailMessage",
                "description": "Append/reuse a deterministic Gmail message (msg_<request_id>).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "sender_email": {"type": "string"},
                        "recipients": {"type": "array", "items": {"type": "string"}},
                        "body_html": {"type": "string"},
                        "attachments_asset_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "thread_id",
                        "sender_email",
                        "recipients",
                        "body_html",
                        "attachments_asset_ids",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }


class governance_update(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str,
        add_tags: list[str],
        remove_tags: list[str],
        timestamp: str,
        request_id: str,
    ) -> str:
        tbl = _table(data, "artifact_tags")
        day = _ymd(timestamp)
        row = next(
            (
                r
                for r in tbl
                if isinstance(r, dict)
                and r.get("artifact_id") == artifact_id
                and r.get("day") == day
            ),
            None,
        )
        if not row:
            row = {"artifact_id": artifact_id, "day": day, "tags": []}
            tbl.append(row)
        current = set(row.get("tags", []))
        current |= set(add_tags or [])
        current -= set(remove_tags or [])
        row["tags"] = sorted(current)
        payload = row
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GovernanceUpdate",
                "description": "Apply deterministic tag updates for an artifact on the instruction day.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "add_tags": {"type": "array", "items": {"type": "string"}},
                        "remove_tags": {"type": "array", "items": {"type": "string"}},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "artifact_id",
                        "add_tags",
                        "remove_tags",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }


class record_automation_run(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        task_name: str,
        status: str,
        started_at: str,
        ended_at: str,
        timestamp: str,
        request_id: str,
    ) -> str:
        runs = _table(data, "automation_runs")
        run_id = _id_from_request("run", request_id)
        if run_id:
            for r in runs:
                if isinstance(r, dict) and r.get("run_id") == run_id:
                    payload = r
                    out = json.dumps(payload, indent=2)
                    return out
        row = {
            "run_id": run_id
            or _get_next_id(
                "run", [r.get("run_id", "") for r in runs if isinstance(r, dict)]
            ),
            "task_name": task_name,
            "status": status,
            "started_at": started_at,
            "ended_at": ended_at,
            "day": _ymd(timestamp),
        }
        runs.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordAutomationRun",
                "description": "Record/reuse a deterministic automation run row (run_<request_id>).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_name": {"type": "string"},
                        "status": {"type": "string"},
                        "started_at": {"type": "string"},
                        "ended_at": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "task_name",
                        "status",
                        "started_at",
                        "ended_at",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }


class get_release_diff(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], release_id: str) -> str:
        diffs = data.get("release_diffs", [])
        for diff in diffs:
            if diff.get("release_id") == release_id:
                payload = diff
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Release diff for {release_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReleaseDiff",
                "description": "Retrieve the diff summary for a given release_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"release_id": {"type": "string"}},
                    "required": ["release_id"],
                },
            },
        }


class apply_gmail_labels(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        thread_id: str,
        add_labels: list[str],
        remove_labels: list[str],
    ) -> str:
        threads = data.get("gmail_threads", [])
        for thread in threads:
            if thread.get("thread_id") == thread_id:
                labels = set(thread.get("current_labels", []))
                labels.update(add_labels)
                labels.difference_update(remove_labels)
                thread["current_labels"] = list(labels)
                payload = thread
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Thread {thread_id} not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "applyGmailLabels",
                "description": "Apply or remove Gmail labels on a thread.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "add_labels": {"type": "array", "items": {"type": "string"}},
                        "remove_labels": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["thread_id"],
                },
            },
        }


class update_review_cycle_status(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], cycle_id: str, status: str, updated_at: str
    ) -> str:
        cycles = data.get("review_cycles", [])
        for cycle in cycles:
            if cycle.get("cycle_id") == cycle_id:
                cycle["status"] = status
                cycle["updated_at"] = updated_at
                payload = cycle
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Cycle {cycle_id} not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReviewCycleStatus",
                "description": "Update the status of a review cycle.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "status": {"type": "string"},
                        "updated_at": {"type": "string"},
                    },
                    "required": ["cycle_id", "status", "updated_at"],
                },
            },
        }


class deliver_fix_plan(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        plan_id: str,
        delivery_method: str,
        timestamp: str,
        request_id: str,
    ) -> str:
        deliveries = data.setdefault("fix_plan_deliveries", [])
        fix_items = data.get("fix_items", [])
        comments_tbl = data.setdefault("figma_comments", [])
        bot_email = _resolve_bot_email(data)
        run_id = _id_from_request("run", request_id) or _get_next_id(
            "run", [r.get("run_id", "") for r in deliveries if isinstance(r, dict)]
        )
        existing = next(
            (
                r
                for r in deliveries
                if isinstance(r, dict) and r.get("run_id") == run_id
            ),
            None,
        )
        if existing:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out

        items_for_plan: list[dict[str, Any]] = []
        for it in fix_items:
            if isinstance(it, dict) and it.get("plan_id") == plan_id:
                items_for_plan.append(it)

        created_comment_ids: list[str] = []
        if (delivery_method or "").upper() == "COMMENTS":
            mirrored = {
                c.get("mirrored_item_id")
                for c in comments_tbl
                if isinstance(c, dict) and c.get("mirrored_item_id")
            }
            existing_ids = [
                c.get("comment_id", "") for c in comments_tbl if isinstance(c, dict)
            ]

            for it in items_for_plan:
                item_id = it.get("item_id")
                status = (it.get("status") or "").upper()
                if not item_id or item_id in mirrored:
                    continue
                if status != "APPLIED":
                    new_cid = _get_next_id("comment", existing_ids)
                    art_id = it.get("artifact_id") or it.get("artifact_id_nullable")
                    title_val = it.get("title")
                    title = (
                        title_val
                        if isinstance(title_val, str) and title_val.strip()
                        else "Pending item"
                    )

                    comments_tbl.append(
                        {
                            "comment_id": new_cid,
                            "artifact_id": art_id,
                            "author_email": bot_email,
                            "content_html": f"[FixPlan] {item_id}: {title} — Status: {status or 'PENDING'}",
                            "mirrored_item_id": item_id,
                            "day": _ymd(timestamp),
                        }
                    )
                    existing_ids.append(new_cid)
                    created_comment_ids.append(new_cid)

        row = {
            "run_id": run_id,
            "plan_id": plan_id,
            "delivery_method": delivery_method,
            "mirrored_count": len(created_comment_ids),
            "comment_ids": created_comment_ids,
            "day": _ymd(timestamp),
        }
        deliveries.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeliverFixPlan",
                "description": "Deliver a fix plan via a method (e.g., COMMENTS). For COMMENTS, mirror non-APPLIED items as Figma comments idempotently.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "delivery_method": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "plan_id",
                        "delivery_method",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }


class update_fix_item_status(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], item_id: str, status: str, timestamp: str, request_id: str
    ) -> str:
        items = data.get("fix_items", [])
        if not isinstance(items, list):
            payload = {"error": "fix_items table missing or invalid"}
            out = json.dumps(payload, indent=2)
            return out

        row = next(
            (
                it
                for it in items
                if isinstance(it, dict) and it.get("item_id") == item_id
            ),
            None,
        )
        if not row:
            payload = {"error": f"fix item '{item_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        status_up = (status or "").upper().strip()
        row["status"] = status_up
        row["status_updated_day"] = _ymd(timestamp)

        trail = data.setdefault("fix_item_updates", [])
        run_id = _id_from_request("run", request_id) or _get_next_id(
            "run", [r.get("run_id", "") for r in trail if isinstance(r, dict)]
        )
        if not any(isinstance(r, dict) and r.get("run_id") == run_id for r in trail):
            trail.append(
                {
                    "run_id": run_id,
                    "item_id": item_id,
                    "status": status_up,
                    "day": _ymd(timestamp),
                }
            )
        payload = row
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFixItemStatus",
                "description": "Set the status for a fix item (e.g., PENDING, APPLIED) deterministically and record an audit trail.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"},
                        "status": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["item_id", "status", "timestamp", "request_id"],
                },
            },
        }


class generate_combined_audit_report(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str,
        artifact_id: str,
        output_format: str,
        timestamp: str,
        request_id: str,
    ) -> str:
        audits = data.get("audits", [])
        arts = data.get("figma_artifacts", [])
        if not any(
            isinstance(a, dict) and a.get("audit_id") == audit_id for a in audits
        ):
            payload = {"error": f"audit_id '{audit_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        if not any(
            isinstance(a, dict) and a.get("artifact_id") == artifact_id for a in arts
        ):
            payload = {"error": f"artifact_id '{artifact_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        reports = data.setdefault("audit_reports", [])
        assets = data.setdefault("assets", [])

        report_id = _id_from_request("rep", request_id) or _get_next_id(
            "rep", [r.get("report_id", "") for r in reports if isinstance(r, dict)]
        )
        existing_report = next(
            (
                r
                for r in reports
                if isinstance(r, dict) and r.get("report_id") == report_id
            ),
            None,
        )
        if existing_report:
            payload = existing_report
            out = json.dumps(payload, indent=2)
            return out

        asset_id = _id_from_request("asset", request_id) or _get_next_id(
            "asset", [r.get("asset_id", "") for r in assets if isinstance(r, dict)]
        )
        mime = (
            "application/pdf"
            if (output_format or "").upper() == "PDF"
            else "application/octet-stream"
        )
        asset_row = {
            "asset_id": asset_id,
            "artifact_id_nullable": artifact_id,
            "export_profile": f"REPORT_{(output_format or '').upper()}",
            "mime_type": mime,
            "file_name": f"{audit_id}_{artifact_id}_combined_report.{(output_format or 'bin').lower()}",
            "size_bytes": 0,
            "day": _ymd(timestamp),
        }
        assets.append(asset_row)

        report_row = {
            "report_id": report_id,
            "audit_id": audit_id,
            "artifact_id": artifact_id,
            "report_asset_id": asset_id,
            "format": (output_format or "").upper(),
            "day": _ymd(timestamp),
        }
        reports.append(report_row)
        payload = report_row
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateCombinedAuditReport",
                "description": "Produce a combined DS + A11Y audit report for an artifact and persist a report asset deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "artifact_id": {"type": "string"},
                        "output_format": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "audit_id",
                        "artifact_id",
                        "output_format",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }


class sync_replies_to_figma_comments(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str, artifact_id: str) -> str:
        """
        Synchronizes replies from Gmail threads into comments in Figma.
        - Retrieves all Gmail messages associated with the specified thread_id.
        - Generates Figma comments for any messages that are not yet included.
        - Connects comments to the corresponding original Gmail message.
        """
        gmail_messages = data.get("gmail_messages", [])
        figma_comments = data.get("figma_comments", [])

        synced_count = 0
        for msg in gmail_messages:
            if msg.get("thread_id") != thread_id:
                continue

            msg_id = msg.get("message_id")
            msg_content = msg.get("body_text_stripped")
            already_synced = any(
                c.get("source_message_id_nullable") == msg_id
                and c.get("artifact_id") == artifact_id
                for c in figma_comments
            )

            if not already_synced:
                new_comment = {
                    "comment_id": f"comment_auto_{len(figma_comments)+1:03d}",
                    "artifact_id": artifact_id,
                    "author_email": msg.get("sender_email"),
                    "content": msg_content,
                    "source_message_id_nullable": msg_id,
                    "created_ts": msg.get("sent_ts"),
                    "resolved_flag": False,
                }
                figma_comments.append(new_comment)
                synced_count += 1
        payload = {"synced_count": synced_count, "total_comments": len(figma_comments)}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SyncRepliesToFigmaComments",
                "description": "Syncs Gmail thread replies into Figma comments for the given artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "artifact_id": {"type": "string"},
                    },
                    "required": ["thread_id", "artifact_id"],
                },
            },
        }


class record_review_approval(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], cycle_id: str, approver_email: str, intent: str
    ) -> str:
        approvals = _table(data, "review_approvals")
        cycles = _table(data, "review_cycles")

        cyc = next((c for c in cycles if c.get("cycle_id") == cycle_id), None)
        if not cyc:
            payload = {"error": f"cycle_id '{cycle_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        existing = next(
            (
                a
                for a in approvals
                if a.get("cycle_id") == cycle_id
                and a.get("approver_email") == approver_email
                and a.get("intent") == intent
            ),
            None,
        )
        if existing:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out

        new_id = _get_next_id("approval", [a.get("approval_id", "") for a in approvals])
        row = {
            "approval_id": new_id,
            "cycle_id": cycle_id,
            "approver_email": approver_email,
            "intent": intent,
        }
        approvals.append(row)

        if intent == "APPROVE":
            count = sum(
                1
                for a in approvals
                if a.get("cycle_id") == cycle_id and a.get("intent") == "APPROVE"
            )
            cyc["approvals_recorded"] = count
        payload = row
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordReviewApproval",
                "description": "Record an approval intent (idempotent). APPROVE contributes to quorum.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "approver_email": {"type": "string"},
                        "intent": {"type": "string"},
                    },
                    "required": ["cycle_id", "approver_email", "intent"],
                },
            },
        }


class update_review_status_by_quorum(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], review_cycles: list[dict] = None, review_approvals: list[dict] = None, system_config: dict = None, cycle_id: str = None) -> str:
        review_cycles = review_cycles or []
        approvals = review_approvals or []
        cfg = system_config or {}

        review_cfg = {}
        if isinstance(cfg, dict):
            review_cfg = cfg.get("review_workflow_config", {}) or {}
        quorum = review_cfg.get("approval_quorum", 2)
        try:
            quorum = int(quorum)
        except Exception:
            quorum = 2

        cycle = None
        if isinstance(review_cycles, list):
            for row in review_cycles:
                if isinstance(row, dict) and row.get("cycle_id") == cycle_id:
                    cycle = row
                    break

        if not cycle:
            payload = {"error": f"Review cycle {cycle_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        approve_emails: list[str] = []
        if isinstance(approvals, list):
            for a in approvals:
                if not isinstance(a, dict):
                    continue
                if a.get("cycle_id") == cycle_id and a.get("intent") == "APPROVE":
                    email = a.get("approver_email")
                    if isinstance(email, str):
                        approve_emails.append(email)

        unique_reviewers = set(approve_emails)
        approvals_count = len(unique_reviewers)

        if approvals_count >= quorum:
            cycle.get("status")
            cycle["status"] = "APPROVED"
        else:
            pass

        try:
            cycle["approvals_recorded"] = approvals_count
        except Exception:
            pass
        payload = cycle
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReviewStatusByQuorum",
                "description": "Checks unique APPROVE intents against configured quorum and sets status to APPROVED if met.",
                "parameters": {
                    "type": "object",
                    "properties": {"cycle_id": {"type": "string"}},
                    "required": ["cycle_id"],
                },
            },
        }


class get_review_cycle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str) -> str:
        cyc = next(
            (c for c in _table(data, "review_cycles") if c.get("cycle_id") == cycle_id),
            None,
        )
        if not cyc:
            payload = {"error": f"cycle_id '{cycle_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"cycle_id": cyc.get("cycle_id"), "status": cyc.get("status")}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReviewCycle",
                "description": "Return (cycle_id, status) as a structured JSON object.",
                "parameters": {
                    "type": "object",
                    "properties": {"cycle_id": {"type": "string"}},
                    "required": ["cycle_id"],
                },
            },
        }


class compute_fix_plan_summary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], plan_id: str, timestamp: str, request_id: str
    ) -> str:
        items = data.get("fix_items", [])
        total = 0
        pending_ids: list[str] = []
        applied_ids: list[str] = []
        for it in items:
            if not isinstance(it, dict) or it.get("plan_id") != plan_id:
                continue
            total += 1
            status = (it.get("status") or "").upper()
            if status == "APPLIED":
                applied_ids.append(it.get("item_id"))
            else:
                pending_ids.append(it.get("item_id"))
        summary = {
            "plan_id": plan_id,
            "total_count": total,
            "pending_count": len(pending_ids),
            "pending_item_ids": pending_ids,
            "applied_item_ids": applied_ids,
            "day": (timestamp or "").split("T")[0],
            "request_id": request_id,
        }
        payload = summary
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeFixPlanSummary",
                "description": "Summarize fix plan items, counting APPLIED vs pending and listing pending item IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["plan_id", "timestamp", "request_id"],
                },
            },
        }


class create_tickets_for_pending(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        plan_id: str,
        tracker_project: str,
        timestamp: str,
        request_id: str,
    ) -> str:
        items = data.get("fix_items", [])
        tickets = data.setdefault("tickets", [])
        day = (timestamp or "").split("T")[0]
        pending_ids = []
        for it in items:
            if not isinstance(it, dict) or it.get("plan_id") != plan_id:
                continue
            status = (it.get("status") or "").upper()
            if status != "APPLIED":
                iid = it.get("item_id")
                if iid:
                    pending_ids.append(iid)

        existing_ids = {t.get("ticket_id") for t in tickets if isinstance(t, dict)}
        created: list[str] = []
        for iid in pending_ids:
            ticket_id = f"tix-{iid}"
            if ticket_id in existing_ids:
                created.append(ticket_id)
                continue
            row = {
                "ticket_id": ticket_id,
                "plan_id": plan_id,
                "item_id": iid,
                "project": tracker_project,
                "status": "OPEN",
                "day": day,
                "request_id": request_id,
            }
            tickets.append(row)
            created.append(ticket_id)
            existing_ids.add(ticket_id)
        payload = {"plan_id": plan_id, "ticket_ids": created, "count": len(created)}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTicketsForPending",
                "description": "Create idempotent tracker tickets (tix-<item_id>) for all non-APPLIED items in a plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "tracker_project": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "plan_id",
                        "tracker_project",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }


TOOLS = [
    create_review_cycle(),
    create_gmail_thread(),
    sync_replies_to_figma_comments(),
    record_review_approval(),
    update_review_status_by_quorum(),
    get_review_cycle(),
    export_assets(),
    append_gmail_message(),
    governance_update(),
    record_automation_run(),
    get_release_diff(),
    apply_gmail_labels(),
    update_review_cycle_status(),
    deliver_fix_plan(),
    update_fix_item_status(),
    generate_combined_audit_report(),
    link_cycle_to_thread(),
    create_release_record(),
    compute_fix_plan_summary(),
    create_tickets_for_pending(),
]
