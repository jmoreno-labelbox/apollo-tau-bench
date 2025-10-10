# tools.py
"""
Goal: Define a comprehensive, deterministic, and well-documented suite of tools for the FIGMA–Gmail MCP pipeline.
The tools operate on loaded JSON tables in `data` and follow the reference Tool interface (domains.dto.Tool).

# Checklist (conceptual)
1) Establish helpers & conventions (IDs, timestamps, configs, safe reads/writes).
2) Implement FIGMA artifact & asset tools (query, tags, comments).
3) Implement Gmail thread & message tools (query, labels, DLP, drafts).
4) Implement Review protocol tools (cycles, approvals, intent sync, SLA checks).
5) Implement Release/Audit/Fix-plan tools (summaries, generation, updates).
6) Implement cross-cutting tools (config reads, logs, linking and guardrails).

Proceeding sequentially with validations after each tool block.
"""

import json
import hashlib
from typing import Any, Dict, List, Optional, Tuple, Set
from domains.dto import Tool


# ------------------------- Helpers & Conventions -------------------------

def _require_str(arg: Any, name: str) -> Optional[str]:
    """Return arg as str if valid, else None."""
    return arg if isinstance(arg, str) and arg.strip() else None

def _require_list(arg: Any, name: str) -> Optional[list]:
    """Return arg as list if valid, else None."""
    return arg if isinstance(arg, list) else None

def _det_id(prefix: str, parts: List[str], length: int = 8) -> str:
    """
    Deterministic ID from input parts. Stable across runs.
    """
    m = hashlib.md5()
    m.update(("|".join(parts)).encode("utf-8"))
    return f"{prefix}_{m.hexdigest()[:length]}"

def _safe_table(data: Dict[str, Any], table: str) -> List[Dict[str, Any]]:
    """Get or create a list table."""
    return data.setdefault(table, [])

def _get_config_json(data: Dict[str, Any], key: str) -> Dict[str, Any]:
    """Read a config row from system_config and parse its JSON value."""
    rows = data.get("system_config", [])
    for r in rows:
        if r.get("config_key") == key:
            try:
                return json.loads(r.get("config_value_json") or "{}")
            except Exception:
                return {}
    return {}

def _index_by(table: List[Dict[str, Any]], key: str) -> Dict[str, int]:
    """Build index map from key -> row_index (first occurrence)."""
    idx = {}
    for i, r in enumerate(table):
        k = r.get(key)
        if isinstance(k, str) and k not in idx:
            idx[k] = i
    return idx

def _small_fields(row: Dict[str, Any], fields: List[str]) -> Dict[str, Any]:
    """Return selected fields only (simple outputs)."""
    return {k: row.get(k) for k in fields}


# ------------------------- FIGMA: Artifacts & Assets -------------------------

class ListArtifactsTool(Tool):
    """List Figma artifacts filtered by owner, tags, type, or modified since."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner_email = kwargs.get("owner_email")
        tag = kwargs.get("tag")
        artifact_type = kwargs.get("artifact_type")
        modified_since = kwargs.get("modified_since")  # ISO string

        rows = data.get("figma_artifacts", [])
        out: List[Dict[str, Any]] = []
        for r in rows:
            if owner_email and r.get("owner_email") != owner_email:
                continue
            if artifact_type and r.get("artifact_type") != artifact_type:
                continue
            if tag:
                tags = r.get("current_tags", [])
                if tag not in tags:
                    continue
            if modified_since and r.get("modified_ts", "") < modified_since:
                continue
            out.append(_small_fields(r, ["artifact_id", "artifact_name", "artifact_type", "owner_email", "modified_ts"]))

        out.sort(key=lambda x: (x.get("artifact_type",""), x.get("artifact_name","")))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_artifacts",
                "description": "List Figma artifacts filtered by owner, tag, type, or modified_since (ISO).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner_email": {"type": "string"},
                        "tag": {"type": "string"},
                        "artifact_type": {"type": "string"},
                        "modified_since": {"type": "string", "description": "ISO timestamp; include rows with modified_ts >= this."}
                    }
                }
            }
        }

class GetArtifactSummaryTool(Tool):
    """Get summary details for a specific artifact."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        artifact_id = _require_str(kwargs.get("artifact_id"), "artifact_id")
        if not artifact_id:
            return json.dumps({"error": "artifact_id is required"})

        rows = data.get("figma_artifacts", [])
        for r in rows:
            if r.get("artifact_id") == artifact_id:
                return json.dumps(_small_fields(r, [
                    "artifact_id", "artifact_name", "artifact_type", "owner_email",
                    "deep_link", "current_tags", "modified_ts"
                ]), indent=2)
        return json.dumps({"error": f"artifact_id {artifact_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_artifact_summary",
            "description":"Return concise details for a given artifact.",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"}
            },"required":["artifact_id"]}
        }}

class ListAssetsForArtifactTool(Tool):
    """List exported assets for a given artifact."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        artifact_id = _require_str(kwargs.get("artifact_id"), "artifact_id")
        if not artifact_id:
            return json.dumps({"error":"artifact_id is required"})

        assets = data.get("assets", [])
        out = []
        for a in assets:
            if a.get("artifact_id_nullable") == artifact_id:
                out.append(_small_fields(a, ["asset_id","profile","file_name","mime_type"]))
        out.sort(key=lambda r: r.get("asset_id",""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_assets_for_artifact",
            "description":"List exported assets linked to the artifact.",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"}
            },"required":["artifact_id"]}
        }}


class AddArtifactTagTool(Tool):
    """Add a tag to an artifact (idempotent). Requires explicit timestamp for auditability."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        artifact_id = _require_str(kwargs.get("artifact_id"), "artifact_id")
        tag = _require_str(kwargs.get("tag"), "tag")
        changed_ts = _require_str(kwargs.get("changed_ts"), "changed_ts")  # must be provided
        if not (artifact_id and tag and changed_ts):
            return json.dumps({"error":"artifact_id, tag, changed_ts are required"})

        artifacts = _safe_table(data, "figma_artifacts")
        idx = _index_by(artifacts, "artifact_id")
        if artifact_id not in idx:
            return json.dumps({"error": f"artifact_id {artifact_id} not found"})

        row = artifacts[idx[artifact_id]]
        tags = row.setdefault("current_tags", [])
        if tag not in tags:
            tags.append(tag)
        row["modified_ts"] = max(changed_ts, row.get("modified_ts",""))

        # Log
        logs = _safe_table(data, "terminal_logs")
        logs.append({"log_ts": changed_ts, "message": f"INFO: Tag '{tag}' added to {artifact_id}"})
        return json.dumps({"success": True, "artifact_id": artifact_id, "tag": tag}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_artifact_tag",
            "description":"Add a tag to artifact (idempotent). Requires 'changed_ts' (ISO).",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "tag":{"type":"string"},
                "changed_ts":{"type":"string","description":"Explicit ISO timestamp"}
            },"required":["artifact_id","tag","changed_ts"]}
        }}

class RemoveArtifactTagTool(Tool):
    """Remove a tag from an artifact (no-op if absent). Requires explicit timestamp."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        artifact_id = _require_str(kwargs.get("artifact_id"), "artifact_id")
        tag = _require_str(kwargs.get("tag"), "tag")
        changed_ts = _require_str(kwargs.get("changed_ts"), "changed_ts")
        if not (artifact_id and tag and changed_ts):
            return json.dumps({"error":"artifact_id, tag, changed_ts are required"})

        artifacts = _safe_table(data, "figma_artifacts")
        idx = _index_by(artifacts, "artifact_id")
        if artifact_id not in idx:
            return json.dumps({"error": f"artifact_id {artifact_id} not found"})

        row = artifacts[idx[artifact_id]]
        tags = row.setdefault("current_tags", [])
        if tag in tags:
            tags.remove(tag)
        row["modified_ts"] = max(changed_ts, row.get("modified_ts",""))

        logs = _safe_table(data, "terminal_logs")
        logs.append({"log_ts": changed_ts, "message": f"INFO: Tag '{tag}' removed from {artifact_id}"})
        return json.dumps({"success": True, "artifact_id": artifact_id, "tag": tag}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"remove_artifact_tag",
            "description":"Remove a tag from artifact (no error if not present). Requires 'changed_ts'.",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "tag":{"type":"string"},
                "changed_ts":{"type":"string"}
            },"required":["artifact_id","tag","changed_ts"]}
        }}

class ListFigmaCommentsTool(Tool):
    """List comments for an artifact, optionally filtered by author or since."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        artifact_id = _require_str(kwargs.get("artifact_id"), "artifact_id")
        author_email = kwargs.get("author_email")
        since_ts = kwargs.get("since_ts")

        if not artifact_id:
            return json.dumps({"error":"artifact_id is required"})

        rows = data.get("figma_comments", [])
        out = []
        for r in rows:
            if r.get("artifact_id") != artifact_id:
                continue
            if author_email and r.get("author_email") != author_email:
                continue
            if since_ts and r.get("created_ts","") < since_ts:
                continue
            out.append(_small_fields(r, ["comment_id","author_email","anchor_ref","body","created_ts"]))

        out.sort(key=lambda r: r.get("created_ts",""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_figma_comments",
            "description":"List Figma comments for an artifact with simple filters.",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "author_email":{"type":"string"},
                "since_ts":{"type":"string"}
            },"required":["artifact_id"]}
        }}

class CreateFigmaCommentTool(Tool):
    """Create an anchored comment on an artifact. Deterministic comment_id from inputs."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        artifact_id = _require_str(kwargs.get("artifact_id"), "artifact_id")
        author_email = _require_str(kwargs.get("author_email"), "author_email")
        body = _require_str(kwargs.get("body"), "body")
        anchor_ref = _require_str(kwargs.get("anchor_ref"), "anchor_ref")
        created_ts = _require_str(kwargs.get("created_ts"), "created_ts")
        if not all([artifact_id, author_email, body, anchor_ref, created_ts]):
            return json.dumps({"error":"artifact_id, author_email, body, anchor_ref, created_ts are required"})

        comments = _safe_table(data, "figma_comments")
        comment_id = _det_id("cmt", [artifact_id, author_email, anchor_ref, created_ts, body[:32]])
        # idempotent upsert by comment_id
        idx = _index_by(comments, "comment_id")
        row = {
            "comment_id": comment_id,
            "artifact_id": artifact_id,
            "author_email": author_email,
            "anchor_ref": anchor_ref,
            "body": body,
            "created_ts": created_ts
        }
        if comment_id in idx:
            comments[idx[comment_id]] = row
        else:
            comments.append(row)

        return json.dumps({"success": True, "comment_id": comment_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_figma_comment",
            "description":"Create/update a Figma comment anchored to an artifact (deterministic id).",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "author_email":{"type":"string"},
                "body":{"type":"string"},
                "anchor_ref":{"type":"string","description":"Anchor reference in Figma (e.g., node path or key)."},
                "created_ts":{"type":"string","description":"Explicit ISO timestamp."}
            },"required":["artifact_id","author_email","body","anchor_ref","created_ts"]}
        }}

# ------------------------- Gmail: Threads & Messages -------------------------

class SearchGmailThreadsTool(Tool):
    """Search Gmail threads by label, participant, or topic keyword."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        label = kwargs.get("label")
        participant = kwargs.get("participant")
        keyword = kwargs.get("keyword")

        threads = data.get("gmail_threads", [])
        out = []
        for t in threads:
            if label and label not in (t.get("current_labels") or []):
                continue
            if participant:
                ps = (t.get("participants") or []) + (t.get("recipients") or [])
                if participant not in ps:
                    continue
            if keyword and keyword.lower() not in (t.get("subject","").lower()):
                continue
            out.append(_small_fields(t, ["thread_id","subject","current_labels","updated_ts"]))
        out.sort(key=lambda r: r.get("thread_id",""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"search_gmail_threads",
            "description":"Search Gmail threads by label, participant, or subject keyword.",
            "parameters":{"type":"object","properties":{
                "label":{"type":"string"},
                "participant":{"type":"string"},
                "keyword":{"type":"string"}
            }}
        }}

class GetThreadMessagesTool(Tool):
    """Return simple message info (sender, ts, snippet) for a thread."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        thread_id = _require_str(kwargs.get("thread_id"), "thread_id")
        if not thread_id:
            return json.dumps({"error":"thread_id is required"})

        msgs = data.get("gmail_messages", [])
        out = []
        for m in msgs:
            if m.get("thread_id") == thread_id:
                out.append(_small_fields(m, ["message_id","from_email","created_ts","snippet"]))
        out.sort(key=lambda r: r.get("created_ts",""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_thread_messages",
            "description":"List messages for a thread (sender, ts, snippet only).",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"}
            },"required":["thread_id"]}
        }}

class AppendMessageToThreadTool(Tool):
    """Append (or upsert) a message to a thread. Deterministic message_id from inputs. No send operation."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        thread_id = _require_str(kwargs.get("thread_id"), "thread_id")
        from_email = _require_str(kwargs.get("from_email"), "from_email")
        body = _require_str(kwargs.get("body"), "body")
        created_ts = _require_str(kwargs.get("created_ts"), "created_ts")
        snippet = (body[:120] + "...") if len(body) > 123 else body
        if not all([thread_id, from_email, body, created_ts]):
            return json.dumps({"error":"thread_id, from_email, body, created_ts required"})

        message_id = _det_id("msg", [thread_id, from_email, created_ts, body[:64]])
        messages = _safe_table(data, "gmail_messages")
        idx = _index_by(messages, "message_id")
        row = {
            "message_id": message_id,
            "thread_id": thread_id,
            "from_email": from_email,
            "created_ts": created_ts,
            "body": body,
            "snippet": snippet
        }
        if message_id in idx:
            messages[idx[message_id]] = row
        else:
            messages.append(row)

        # Mark thread updated_ts
        threads = _safe_table(data, "gmail_threads")
        t_idx = _index_by(threads, "thread_id")
        if thread_id in t_idx:
            threads[t_idx[thread_id]]["updated_ts"] = created_ts

        return json.dumps({"success": True, "message_id": message_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"append_message_to_thread",
            "description":"Append/upsert a message in a thread (deterministic id). Stores snippet; does not send email.",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"},
                "from_email":{"type":"string"},
                "body":{"type":"string"},
                "created_ts":{"type":"string"}
            },"required":["thread_id","from_email","body","created_ts"]}
        }}

class UpdateThreadLabelsTool(Tool):
    """Update Gmail thread labels deterministically (idempotent)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        thread_id = _require_str(kwargs.get("thread_id"), "thread_id")
        add_labels = kwargs.get("add_labels", []) or []
        remove_labels = kwargs.get("remove_labels", []) or []
        changed_ts = _require_str(kwargs.get("changed_ts"), "changed_ts")
        if not (thread_id and changed_ts):
            return json.dumps({"error":"thread_id and changed_ts required"})

        threads = _safe_table(data, "gmail_threads")
        idx = _index_by(threads, "thread_id")
        if thread_id not in idx:
            return json.dumps({"error": f"thread_id {thread_id} not found"})

        row = threads[idx[thread_id]]
        labels: List[str] = list(row.get("current_labels", []))
        for lab in add_labels:
            if lab not in labels:
                labels.append(lab)
        for lab in remove_labels:
            if lab in labels:
                labels.remove(lab)
        row["current_labels"] = labels
        row["updated_ts"] = changed_ts

        return json.dumps({"success": True, "thread_id": thread_id, "labels": labels}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_thread_labels",
            "description":"Add/remove labels on a Gmail thread (idempotent). Requires explicit 'changed_ts'.",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"},
                "add_labels":{"type":"array","items":{"type":"string"}},
                "remove_labels":{"type":"array","items":{"type":"string"}},
                "changed_ts":{"type":"string"}
            },"required":["thread_id","changed_ts"]}
        }}

class DlpScanThreadTool(Tool):
    """Scan a thread's messages for DLP block patterns from config; returns found patterns."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        thread_id = _require_str(kwargs.get("thread_id"), "thread_id")
        if not thread_id:
            return json.dumps({"error":"thread_id is required"})

        dlp = _get_config_json(data, "dlp_config")
        patterns = dlp.get("block_patterns", []) if isinstance(dlp, dict) else []
        messages = data.get("gmail_messages", [])
        found: Set[str] = set()
        for m in messages:
            if m.get("thread_id") != thread_id:
                continue
            body = (m.get("body") or "").lower()
            for p in patterns:
                if isinstance(p, str) and p.lower() in body:
                    found.add(p)

        return json.dumps({"thread_id": thread_id, "blocked_terms_found": sorted(found)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"dlp_scan_thread",
            "description":"Scan thread messages for DLP block patterns from system config.",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"}
            },"required":["thread_id"]}
        }}

# ------------------------- Review Workflow -------------------------

class StartReviewCycleTool(Tool):
    """Create or upsert a review cycle for an artifact (deterministic cycle_id from inputs)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        artifact_id = _require_str(kwargs.get("artifact_id"), "artifact_id")
        created_ts = _require_str(kwargs.get("created_ts"), "created_ts")
        status = kwargs.get("status") or "IN_FLIGHT"
        if not (artifact_id and created_ts):
            return json.dumps({"error":"artifact_id and created_ts required"})

        cycle_id = _det_id("cycle", [artifact_id, created_ts, status])
        cycles = _safe_table(data, "review_cycles")
        idx = _index_by(cycles, "cycle_id")
        row = {
            "cycle_id": cycle_id,
            "artifact_id": artifact_id,
            "status": status,
            "created_ts": created_ts,
            "last_updated": created_ts,
            "thread_id_nullable": None,
            "sla_hours": _get_config_json(data, "sla_deadlines").get("design_review", 72)
        }
        if cycle_id in idx:
            # preserve existing thread link
            existing = cycles[idx[cycle_id]]
            row["thread_id_nullable"] = existing.get("thread_id_nullable")
            cycles[idx[cycle_id]] = row
        else:
            cycles.append(row)

        return json.dumps({"success": True, "cycle_id": cycle_id, "status": status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"start_review_cycle",
            "description":"Create/update a review cycle for an artifact (deterministic id).",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "created_ts":{"type":"string"},
                "status":{"type":"string","description":"Default IN_FLIGHT."}
            },"required":["artifact_id","created_ts"]}
        }}

class AdvanceReviewStatusTool(Tool):
    """Advance review cycle status with allowed transitions; deterministic (requires changed_ts)."""

    ALLOWED = {
        "IN_FLIGHT": {"NEEDS_REVIEW","ESCALATED"},
        "NEEDS_REVIEW": {"APPROVED","CHANGES_REQUESTED","ESCALATED"},
        "CHANGES_REQUESTED": {"NEEDS_REVIEW","ESCALATED"},
        "ESCALATED": {"NEEDS_REVIEW","APPROVED","CHANGES_REQUESTED"},
        "APPROVED": set()
    }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cycle_id = _require_str(kwargs.get("cycle_id"), "cycle_id")
        new_status = _require_str(kwargs.get("new_status"), "new_status")
        changed_ts = _require_str(kwargs.get("changed_ts"), "changed_ts")
        allow_override = bool(kwargs.get("allow_override", False))
        if not (cycle_id and new_status and changed_ts):
            return json.dumps({"error":"cycle_id, new_status, changed_ts required"})

        cycles = _safe_table(data, "review_cycles")
        idx = _index_by(cycles, "cycle_id")
        if cycle_id not in idx:
            return json.dumps({"error": f"cycle_id {cycle_id} not found"})

        row = cycles[idx[cycle_id]]
        old = row.get("status")
        if not allow_override and new_status not in AdvanceReviewStatusTool.ALLOWED.get(old, set()):
            return json.dumps({"error": f"transition {old} -> {new_status} not allowed"})

        row["status"] = new_status
        row["last_updated"] = changed_ts
        return json.dumps({"success": True, "cycle_id": cycle_id, "from": old, "to": new_status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"advance_review_status",
            "description":"Advance review status with allowed transitions (override optional). Requires changed_ts.",
            "parameters":{"type":"object","properties":{
                "cycle_id":{"type":"string"},
                "new_status":{"type":"string"},
                "changed_ts":{"type":"string"},
                "allow_override":{"type":"boolean"}
            },"required":["cycle_id","new_status","changed_ts"]}
        }}

class RecordReviewApprovalTool(Tool):
    """Record a reviewer decision for a cycle (deterministic approval_id)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cycle_id = _require_str(kwargs.get("cycle_id"), "cycle_id")
        approver_email = _require_str(kwargs.get("approver_email"), "approver_email")
        decision = _require_str(kwargs.get("decision"), "decision")  # APPROVED|CHANGES_REQUESTED|BLOCKED
        decided_ts = _require_str(kwargs.get("decided_ts"), "decided_ts")
        comment = kwargs.get("comment","")
        if not all([cycle_id, approver_email, decision, decided_ts]):
            return json.dumps({"error":"cycle_id, approver_email, decision, decided_ts required"})

        approvals = _safe_table(data, "review_approvals")
        approval_id = _det_id("appr", [cycle_id, approver_email, decided_ts, decision])
        idx = _index_by(approvals, "approval_id")
        row = {
            "approval_id": approval_id,
            "cycle_id": cycle_id,
            "approver_email": approver_email,
            "decision": decision,
            "decision_ts": decided_ts,
            "comments": comment
        }
        if approval_id in idx:
            approvals[idx[approval_id]] = row
        else:
            approvals.append(row)

        return json.dumps({"success": True, "approval_id": approval_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"record_review_approval",
            "description":"Record reviewer decision (deterministic id).",
            "parameters":{"type":"object","properties":{
                "cycle_id":{"type":"string"},
                "approver_email":{"type":"string"},
                "decision":{"type":"string","description":"APPROVED | CHANGES_REQUESTED | BLOCKED"},
                "decided_ts":{"type":"string"},
                "comment":{"type":"string"}
            },"required":["cycle_id","approver_email","decision","decided_ts"]}
        }}

class SyncGmailIntentsToReviewTool(Tool):
    """Scan thread messages for intent keywords and update review status counts (no status change)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cycle_id = _require_str(kwargs.get("cycle_id"), "cycle_id")
        thread_id = _require_str(kwargs.get("thread_id"), "thread_id")
        if not (cycle_id and thread_id):
            return json.dumps({"error":"cycle_id and thread_id required"})

        intents = _get_config_json(data, "intent_keywords")
        approve = [s.lower() for s in intents.get("approve", [])]
        changes = [s.lower() for s in intents.get("changes", [])]
        blocker = [s.lower() for s in intents.get("blocker", [])]

        msgs = data.get("gmail_messages", [])
        counts = {"approve":0, "changes":0, "blocker":0}
        for m in msgs:
            if m.get("thread_id") != thread_id:
                continue
            body = (m.get("body") or "").lower()
            if any(k in body for k in approve):
                counts["approve"] += 1
            if any(k in body for k in changes):
                counts["changes"] += 1
            if any(k in body for k in blocker):
                counts["blocker"] += 1

        # Store counts on cycle for visibility (non-destructive)
        cycles = _safe_table(data, "review_cycles")
        idx = _index_by(cycles, "cycle_id")
        if cycle_id in idx:
            c = cycles[idx[cycle_id]]
            c["intent_counts"] = counts

        return json.dumps({"cycle_id": cycle_id, "thread_id": thread_id, "intent_counts": counts}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"sync_gmail_intents_to_review",
            "description":"Parse thread for intent keywords (config-driven) and store counts on the cycle (no status change).",
            "parameters":{"type":"object","properties":{
                "cycle_id":{"type":"string"},
                "thread_id":{"type":"string"}
            },"required":["cycle_id","thread_id"]}
        }}


class LinkReviewToThreadTool(Tool):
    """Link a review cycle to a Gmail thread (idempotent)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cycle_id = _require_str(kwargs.get("cycle_id"), "cycle_id")
        thread_id = _require_str(kwargs.get("thread_id"), "thread_id")
        changed_ts = _require_str(kwargs.get("changed_ts"), "changed_ts")
        if not (cycle_id and thread_id and changed_ts):
            return json.dumps({"error":"cycle_id, thread_id, changed_ts required"})

        cycles = _safe_table(data, "review_cycles")
        idx = _index_by(cycles, "cycle_id")
        if cycle_id not in idx:
            return json.dumps({"error": f"cycle_id {cycle_id} not found"})

        cycles[idx[cycle_id]]["thread_id_nullable"] = thread_id
        cycles[idx[cycle_id]]["last_updated"] = changed_ts
        return json.dumps({"success": True, "cycle_id": cycle_id, "thread_id": thread_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"link_review_to_thread",
            "description":"Link review cycle to Gmail thread (idempotent).",
            "parameters":{"type":"object","properties":{
                "cycle_id":{"type":"string"},
                "thread_id":{"type":"string"},
                "changed_ts":{"type":"string"}
            },"required":["cycle_id","thread_id","changed_ts"]}
        }}

class FindStaleReviewsTool(Tool):
    """Return cycles exceeding SLA (status not APPROVED) by comparing last_updated with SLA hours."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        now_iso = _require_str(kwargs.get("now_iso"), "now_iso")  # comparison baseline
        if not now_iso:
            return json.dumps({"error":"now_iso is required (ISO timestamp baseline)"})

        cycles = data.get("review_cycles", [])
        sla_hours = _get_config_json(data, "sla_deadlines").get("design_review", 72)

        def overdue(c: Dict[str, Any]) -> bool:
            return c.get("status") != "APPROVED" and c.get("last_updated","") < now_iso

        out = []
        for c in cycles:
            if overdue(c):
                out.append(_small_fields(c, ["cycle_id","artifact_id","status","last_updated"]))
        out.sort(key=lambda r: r.get("cycle_id",""))
        return json.dumps({"sla_hours": sla_hours, "stale_cycles": out}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"find_stale_reviews",
            "description":"Find review cycles not APPROVED and older than 'now_iso' (approximation for SLA breach).",
            "parameters":{"type":"object","properties":{
                "now_iso":{"type":"string","description":"Current timestamp baseline (ISO)."}
            },"required":["now_iso"]}
        }}

# ------------------------- Release Workflow -------------------------

class ListReleasesTool(Tool):
    """List releases filtered by version_tag prefix or artifact_id reference."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        prefix = kwargs.get("version_prefix", "release/")
        artifact_id = kwargs.get("artifact_id")

        releases = data.get("releases", [])
        out = []
        for r in releases:
            if prefix and not str(r.get("version_tag","")).startswith(prefix):
                continue
            if artifact_id and r.get("artifact_id") != artifact_id:
                continue
            out.append(_small_fields(r, ["release_id","version_tag","artifact_id","created_ts","thread_id_nullable"]))
        out.sort(key=lambda r: r.get("version_tag",""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_releases",
            "description":"List releases with optional version prefix and artifact filter.",
            "parameters":{"type":"object","properties":{
                "version_prefix":{"type":"string","description":"Default 'release/'."},
                "artifact_id":{"type":"string"}
            }}
        }}

class GetReleaseDiffSummaryTool(Tool):
    """Summarize a release diff: counts of added/updated/removed frames."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        release_id = _require_str(kwargs.get("release_id"), "release_id")
        if not release_id:
            return json.dumps({"error":"release_id is required"})

        diffs = data.get("release_diffs", [])
        adds = updates = removes = 0
        for d in diffs:
            if d.get("release_id") != release_id:
                continue
            t = d.get("change_type")
            if t == "ADDED": adds += 1
            elif t == "UPDATED": updates += 1
            elif t == "REMOVED": removes += 1

        return json.dumps({"release_id": release_id, "added": adds, "updated": updates, "removed": removes}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_release_diff_summary",
            "description":"Return counts of ADDED/UPDATED/REMOVED items for a release.",
            "parameters":{"type":"object","properties":{
                "release_id":{"type":"string"}
            },"required":["release_id"]}
        }}

class ComposeReleaseEmailDraftTool(Tool):
    """Compose a release email draft message in gmail_messages (deterministic message_id)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        release_id = _require_str(kwargs.get("release_id"), "release_id")
        thread_id = _require_str(kwargs.get("thread_id"), "thread_id")  # existing or new thread id
        from_email = _require_str(kwargs.get("from_email"), "from_email")
        created_ts = _require_str(kwargs.get("created_ts"), "created_ts")
        subject = _require_str(kwargs.get("subject"), "subject")
        body = _require_str(kwargs.get("body"), "body")
        if not all([release_id, thread_id, from_email, created_ts, subject, body]):
            return json.dumps({"error":"release_id, thread_id, from_email, created_ts, subject, body required"})

        message_id = _det_id("relmsg", [release_id, thread_id, created_ts, subject[:32]])
        messages = _safe_table(data, "gmail_messages")
        idx = _index_by(messages, "message_id")
        row = {
            "message_id": message_id,
            "thread_id": thread_id,
            "from_email": from_email,
            "created_ts": created_ts,
            "subject": subject,
            "body": body,
            "snippet": (body[:120] + "...") if len(body) > 123 else body
        }
        if message_id in idx:
            messages[idx[message_id]] = row
        else:
            messages.append(row)

        return json.dumps({"success": True, "message_id": message_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"compose_release_email_draft",
            "description":"Create/update a release email draft message (deterministic id) in an existing thread.",
            "parameters":{"type":"object","properties":{
                "release_id":{"type":"string"},
                "thread_id":{"type":"string"},
                "from_email":{"type":"string"},
                "created_ts":{"type":"string"},
                "subject":{"type":"string"},
                "body":{"type":"string"}
            },"required":["release_id","thread_id","from_email","created_ts","subject","body"]}
        }}

# ------------------------- Audit Workflow -------------------------

class ListAuditsTool(Tool):
    """List audit sessions filtered by artifact or status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        artifact_id = kwargs.get("artifact_id")
        status = kwargs.get("status")

        audits = data.get("audits", [])
        out = []
        for a in audits:
            if artifact_id and a.get("artifact_id") != artifact_id:
                continue
            if status and a.get("status") != status:
                continue
            out.append(_small_fields(a, ["audit_id","artifact_id","audit_type","status","created_ts"]))
        out.sort(key=lambda r: r.get("audit_id",""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_audits",
            "description":"List audits filtered by artifact_id and/or status.",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "status":{"type":"string"}
            }}
        }}

class SummarizeAuditTool(Tool):
    """Summarize DS and A11y finding counts for an audit."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        audit_id = _require_str(kwargs.get("audit_id"), "audit_id")
        if not audit_id:
            return json.dumps({"error":"audit_id is required"})

        ds = data.get("audit_findings_ds", [])
        a11y = data.get("audit_findings_a11y", [])
        ds_count = sum(1 for r in ds if r.get("audit_id") == audit_id)
        a11y_count = sum(1 for r in a11y if r.get("audit_id") == audit_id)
        return json.dumps({"audit_id": audit_id, "ds_findings": ds_count, "a11y_findings": a11y_count}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"summarize_audit",
            "description":"Return simple counts of design-system and accessibility findings for an audit.",
            "parameters":{"type":"object","properties":{
                "audit_id":{"type":"string"}
            },"required":["audit_id"]}
        }}

class CreateAuditSessionTool(Tool):
    """Create/upsert an audit session for an artifact (deterministic audit_id)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        artifact_id = _require_str(kwargs.get("artifact_id"), "artifact_id")
        created_ts = _require_str(kwargs.get("created_ts"), "created_ts")
        audit_type = kwargs.get("audit_type") or "COMBINED_DS_A11Y"
        if not (artifact_id and created_ts):
            return json.dumps({"error":"artifact_id and created_ts required"})

        audit_id = _det_id("audit", [artifact_id, created_ts, audit_type])
        audits = _safe_table(data, "audits")
        idx = _index_by(audits, "audit_id")
        row = {
            "audit_id": audit_id,
            "artifact_id": artifact_id,
            "audit_type": audit_type,
            "status": "IN_PROGRESS",
            "created_ts": created_ts
        }
        if audit_id in idx:
            audits[idx[audit_id]] = row
        else:
            audits.append(row)
        return json.dumps({"success": True, "audit_id": audit_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_audit_session",
            "description":"Create/update an audit session (deterministic id).",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "created_ts":{"type":"string"},
                "audit_type":{"type":"string"}
            },"required":["artifact_id","created_ts"]}
        }}

class MapFindingsToFramesSummaryTool(Tool):
    """Produce a per-frame summary of counts from DS and A11y findings for a given audit."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        audit_id = _require_str(kwargs.get("audit_id"), "audit_id")
        if not audit_id:
            return json.dumps({"error":"audit_id is required"})

        ds = [r for r in data.get("audit_findings_ds", []) if r.get("audit_id") == audit_id]
        a11y = [r for r in data.get("audit_findings_a11y", []) if r.get("audit_id") == audit_id]
        counts: Dict[str, Dict[str,int]] = {}
        for r in ds:
            fid = r.get("frame_id")
            bucket = counts.setdefault(fid, {"ds":0,"a11y":0})
            bucket["ds"] += 1
        for r in a11y:
            fid = r.get("frame_id")
            bucket = counts.setdefault(fid, {"ds":0,"a11y":0})
            bucket["a11y"] += 1

        out = [{"frame_id": k, "ds_count": v["ds"], "a11y_count": v["a11y"]} for k,v in sorted(counts.items())]
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"map_findings_to_frames_summary",
            "description":"Return per-frame counts of DS and A11y findings for a given audit.",
            "parameters":{"type":"object","properties":{
                "audit_id":{"type":"string"}
            },"required":["audit_id"]}
        }}

# ------------------------- Fix Plan Workflow -------------------------

class GenerateFixPlanFromAuditTool(Tool):
    """Generate or upsert a minimal fix plan from audit findings, obeying change budget config."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        audit_id = _require_str(kwargs.get("audit_id"), "audit_id")
        owner_email = _require_str(kwargs.get("owner_email"), "owner_email")
        created_ts = _require_str(kwargs.get("created_ts"), "created_ts")
        if not all([audit_id, owner_email, created_ts]):
            return json.dumps({"error":"audit_id, owner_email, created_ts required"})

        cfg = _get_config_json(data, "fix_workflow_config")
        budget = int(cfg.get("change_budget_per_frame", 5))

        plan_id = _det_id("plan", [audit_id, owner_email, created_ts])
        plans = _safe_table(data, "fix_plans")
        p_idx = _index_by(plans, "plan_id")
        plan_row = {
            "plan_id": plan_id,
            "audit_id": audit_id,
            "status": "IN_PROGRESS",
            "created_ts": created_ts,
            "owner_email": owner_email
        }
        if plan_id in p_idx:
            plans[p_idx[plan_id]] = plan_row
        else:
            plans.append(plan_row)

        # Select top findings per frame until budget
        ds = [r for r in data.get("audit_findings_ds", []) if r.get("audit_id") == audit_id]
        a11y = [r for r in data.get("audit_findings_a11y", []) if r.get("audit_id") == audit_id]
        grouped: Dict[str, List[Dict[str, Any]]] = {}
        for r in ds + a11y:
            fid = r.get("frame_id")
            grouped.setdefault(fid, []).append(r)

        items = _safe_table(data, "fix_items")
        i_idx = _index_by(items, "item_id")
        created_item_ids: List[str] = []

        # Deterministic ordering by frame_id then finding_id
        for frame_id in sorted(grouped.keys()):
            picks = sorted(grouped[frame_id], key=lambda r: str(r.get("finding_id")))[:budget]
            for f in picks:
                item_id = _det_id("fix", [plan_id, frame_id, str(f.get("finding_id"))])
                row = {
                    "item_id": item_id,
                    "plan_id": plan_id,
                    "finding_id": f.get("finding_id"),
                    "frame_id": frame_id,
                    "status": "PENDING",
                    "suggested_fix": f.get("suggested_fix",""),
                    "created_ts": created_ts
                }
                if item_id in i_idx:
                    items[i_idx[item_id]] = row
                else:
                    items.append(row)
                created_item_ids.append(item_id)

        return json.dumps({"success": True, "plan_id": plan_id, "created_items": created_item_ids}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"generate_fix_plan_from_audit",
            "description":"Create/update a fix plan from an audit, obeying per-frame change budget from config.",
            "parameters":{"type":"object","properties":{
                "audit_id":{"type":"string"},
                "owner_email":{"type":"string"},
                "created_ts":{"type":"string"}
            },"required":["audit_id","owner_email","created_ts"]}
        }}

class UpdateFixItemStatusDeterministicTool(Tool):
    """Update a fix item status deterministically (requires explicit changed_ts)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        item_id = _require_str(kwargs.get("item_id"), "item_id")
        new_status = _require_str(kwargs.get("new_status"), "new_status")
        changed_ts = _require_str(kwargs.get("changed_ts"), "changed_ts")
        note = kwargs.get("note","")
        if not all([item_id, new_status, changed_ts]):
            return json.dumps({"error":"item_id, new_status, changed_ts required"})

        items = _safe_table(data, "fix_items")
        idx = _index_by(items, "item_id")
        if item_id not in idx:
            return json.dumps({"error": f"item_id {item_id} not found"})

        row = items[idx[item_id]]
        old = row.get("status")
        row["status"] = new_status
        row["last_updated"] = changed_ts
        hist = row.setdefault("status_history", [])
        hist.append({"from": old, "to": new_status, "changed_ts": changed_ts, "note": note})
        return json.dumps({"success": True, "item_id": item_id, "from": old, "to": new_status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_fix_item_status_deterministic",
            "description":"Update fix item status (deterministic; requires changed_ts).",
            "parameters":{"type":"object","properties":{
                "item_id":{"type":"string"},
                "new_status":{"type":"string"},
                "changed_ts":{"type":"string"},
                "note":{"type":"string"}
            },"required":["item_id","new_status","changed_ts"]}
        }}

class EnforceChangeBudgetForFrameTool(Tool):
    """Check if a frame exceeds fix-item change budget (from config) within a plan."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        plan_id = _require_str(kwargs.get("plan_id"), "plan_id")
        frame_id = _require_str(kwargs.get("frame_id"), "frame_id")
        if not (plan_id and frame_id):
            return json.dumps({"error":"plan_id and frame_id required"})

        cfg = _get_config_json(data, "fix_workflow_config")
        budget = int(cfg.get("change_budget_per_frame", 5))

        items = data.get("fix_items", [])
        count = sum(1 for r in items if r.get("plan_id")==plan_id and r.get("frame_id")==frame_id)
        return json.dumps({"plan_id": plan_id, "frame_id": frame_id, "count": count, "budget": budget, "exceeds": count > budget}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"enforce_change_budget_for_frame",
            "description":"Return whether a frame's fix items exceed the per-frame budget.",
            "parameters":{"type":"object","properties":{
                "plan_id":{"type":"string"},
                "frame_id":{"type":"string"}
            },"required":["plan_id","frame_id"]}
        }}

# ------------------------- System Config & Logs -------------------------

class ReadSystemConfigTool(Tool):
    """Read a config by key and return limited fields (avoid large blobs)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        config_key = _require_str(kwargs.get("config_key"), "config_key")
        if not config_key:
            return json.dumps({"error":"config_key is required"})

        rows = data.get("system_config", [])
        for r in rows:
            if r.get("config_key") == config_key:
                return json.dumps({
                    "config_key": r.get("config_key"),
                    "sample": (r.get("config_value_json") or "")[:200]  # preview only
                }, indent=2)
        return json.dumps({"error": f"config_key {config_key} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"read_system_config",
            "description":"Return a preview of the config value by key (first 200 chars).",
            "parameters":{"type":"object","properties":{
                "config_key":{"type":"string"}
            },"required":["config_key"]}
        }}

class LogTerminalEventTool(Tool):
    """Append a log entry to terminal_logs (requires explicit log_ts)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        log_ts = _require_str(kwargs.get("log_ts"), "log_ts")
        message = _require_str(kwargs.get("message"), "message")
        if not (log_ts and message):
            return json.dumps({"error":"log_ts and message required"})

        logs = _safe_table(data, "terminal_logs")
        log_id = _det_id("log", [log_ts, message[:64]])
        # store as simple row; deterministic id not used by dataset but included as field
        logs.append({"log_ts": log_ts, "message": message, "log_id": log_id})
        return json.dumps({"success": True, "log_id": log_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"log_terminal_event",
            "description":"Append a new terminal log row (deterministic).",
            "parameters":{"type":"object","properties":{
                "log_ts":{"type":"string"},
                "message":{"type":"string"}
            },"required":["log_ts","message"]}
        }}

# ------------------------- Cross-Checks & Guardrails -------------------------

class DlpScanAndLabelThreadTool(Tool):
    """Scan a thread for DLP issues and apply a label if any issues found (idempotent)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        thread_id = _require_str(kwargs.get("thread_id"), "thread_id")
        label_if_found = _require_str(kwargs.get("label_if_found"), "label_if_found") or "dlp-flag"
        changed_ts = _require_str(kwargs.get("changed_ts"), "changed_ts")
        if not (thread_id and label_if_found and changed_ts):
            return json.dumps({"error":"thread_id, label_if_found, changed_ts required"})

        # Reuse DLP scan
        scan = json.loads(DlpScanThreadTool.invoke(data, thread_id=thread_id))
        found = scan.get("blocked_terms_found", [])
        if found:
            # apply label
            _ = UpdateThreadLabelsTool.invoke(data, thread_id=thread_id, add_labels=[label_if_found], remove_labels=[], changed_ts=changed_ts)
        return json.dumps({"thread_id": thread_id, "blocked_terms_found": found, "label_applied": bool(found)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"dlp_scan_and_label_thread",
            "description":"If DLP violations found in thread, apply a chosen label.",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"},
                "label_if_found":{"type":"string"},
                "changed_ts":{"type":"string"}
            },"required":["thread_id","label_if_found","changed_ts"]}
        }}

class GuardAttachmentPolicyOnDraftTool(Tool):
    """Check draft body length against release policy; returns OK/violation flags (simplified guard)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        message_id = _require_str(kwargs.get("message_id"), "message_id")
        if not message_id:
            return json.dumps({"error":"message_id is required"})

        # Simplified: check body size approximates attachment concerns
        messages = data.get("gmail_messages", [])
        target = None
        for m in messages:
            if m.get("message_id") == message_id:
                target = m
                break
        if not target:
            return json.dumps({"error": f"message_id {message_id} not found"})

        body = target.get("body","")
        size = len(body.encode("utf-8"))
        policy = _get_config_json(data, "release_workflow_config").get("attachment_policy", {})
        max_total = int(policy.get("max_total_size", 10_000_000))
        ok = size <= max_total
        return json.dumps({"message_id": message_id, "approx_body_bytes": size, "max_total_bytes": max_total, "ok": ok}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"guard_attachment_policy_on_draft",
            "description":"Approximate a policy check by comparing draft body bytes to max_total_size from config.",
            "parameters":{"type":"object","properties":{
                "message_id":{"type":"string"}
            },"required":["message_id"]}
        }}

TOOLS = [
    # ---------------- FIGMA: Artifacts & Assets ----------------
    ListArtifactsTool(),
    GetArtifactSummaryTool(),
    ListAssetsForArtifactTool(),
    AddArtifactTagTool(),
    RemoveArtifactTagTool(),
    ListFigmaCommentsTool(),
    CreateFigmaCommentTool(),

    # ---------------- Gmail: Threads & Messages ----------------
    SearchGmailThreadsTool(),
    GetThreadMessagesTool(),
    AppendMessageToThreadTool(),
    UpdateThreadLabelsTool(),
    DlpScanThreadTool(),

    # ---------------- Review Workflow ----------------
    StartReviewCycleTool(),
    AdvanceReviewStatusTool(),
    RecordReviewApprovalTool(),
    SyncGmailIntentsToReviewTool(),
    LinkReviewToThreadTool(),
    FindStaleReviewsTool(),

    # ---------------- Release Workflow ----------------
    ListReleasesTool(),
    GetReleaseDiffSummaryTool(),
    ComposeReleaseEmailDraftTool(),

    # ---------------- Audit Workflow ----------------
    ListAuditsTool(),
    SummarizeAuditTool(),
    CreateAuditSessionTool(),
    MapFindingsToFramesSummaryTool(),

    # ---------------- Fix Plan Workflow ----------------
    GenerateFixPlanFromAuditTool(),
    UpdateFixItemStatusDeterministicTool(),
    EnforceChangeBudgetForFrameTool(),

    # ---------------- System Config & Logs ----------------
    ReadSystemConfigTool(),
    LogTerminalEventTool(),

    # ---------------- Cross-Checks & Guardrails ----------------
    DlpScanAndLabelThreadTool(),
    GuardAttachmentPolicyOnDraftTool(),
]
