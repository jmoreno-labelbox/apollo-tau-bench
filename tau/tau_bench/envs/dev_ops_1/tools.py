import json
from typing import Any, Dict, List, Optional

from domains.dto import Tool


def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])


def _max_int_suffix(items: List[Dict[str, Any]], key: str, prefix: str, default: int = 0) -> int:
    max_val = default
    for it in items:
        raw = it.get(key)
        if isinstance(raw, str) and raw.startswith(prefix + "-"):
            try:
                num = int(raw.split("-")[-1])
                if num > max_val:
                    max_val = num
            except ValueError:
                continue
    return max_val


def _error(msg: str) -> str:
    return json.dumps({"error": msg}, indent=2)


# ------------------------- CI BUILD TRIAGE (13 tools) -------------------------


class ReceiveCiEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], provider: str, run_id: str, status: str, repo: Optional[str] = None, branch: Optional[str] = None, commit_sha: Optional[str] = None, job_name: Optional[str] = None) -> str:
        build_runs = _get_table(data, "build_runs")
        existing = next((r for r in build_runs if r.get("run_id") == run_id), None)
        if existing:
            return json.dumps({"ack": True, "run_id": run_id, "deduplicated": True}, indent=2)
        record = {
            "run_id": run_id,
            "provider": provider,
            "status": status,
            "repo": repo,
            "branch": branch,
            "commit_sha": commit_sha,
            "job_name": job_name,
            "artifacts_uri": None,
            "logs_uri": None,
        }
        build_runs.append(record)
        return json.dumps({"ack": True, "run_id": run_id, "deduplicated": False}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "receive_ci_event", "description": "Registers a CI event run envelope deterministically (idempotent by run_id).", "parameters": {"type": "object", "properties": {"provider": {"type": "string"}, "run_id": {"type": "string"}, "status": {"type": "string"}, "repo": {"type": "string"}, "branch": {"type": "string"}, "commit_sha": {"type": "string"}, "job_name": {"type": "string"}}, "required": ["provider", "run_id", "status"]}}}


class AttachRunArtifacts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str, logs_uri: Optional[str] = None, dumps_uri: Optional[str] = None, reports_uri: Optional[str] = None) -> str:
        build_runs = _get_table(data, "build_runs")
        artifacts = _get_table(data, "artifacts")
        run = next((r for r in build_runs if r.get("run_id") == run_id), None)
        if not run:
            return _error(f"Run '{run_id}' not found.")
        artifact_entry = next((a for a in artifacts if a.get("run_id") == run_id), None)
        if not artifact_entry:
            artifact_entry = {"run_id": run_id}
            artifacts.append(artifact_entry)
        if logs_uri is None:
            logs_uri = f"artifact://logs/{run_id}"
        if reports_uri is None:
            reports_uri = f"artifact://reports/{run_id}"
        artifact_entry.update({"logs_uri": logs_uri, "dumps_uri": dumps_uri, "reports_uri": reports_uri})
        run["logs_uri"] = logs_uri
        run["artifacts_uri"] = reports_uri
        return json.dumps(artifact_entry, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "attach_run_artifacts", "description": "Attaches deterministic artifact URIs to a CI run and persists an artifact record.", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}, "logs_uri": {"type": "string"}, "dumps_uri": {"type": "string"}, "reports_uri": {"type": "string"}}, "required": ["run_id"]}}}


class ExtractFailureSignals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str) -> str:
        artifacts = _get_table(data, "artifacts")
        build_runs = _get_table(data, "build_runs")
        crashes = _get_table(data, "crash_events")
        run = next((r for r in build_runs if r.get("run_id") == run_id), None)
        if not run:
            return _error(f"Run '{run_id}' not found.")
        art = next((a for a in artifacts if a.get("run_id") == run_id), None)
        if not art:
            art = {"run_id": run_id}
            artifacts.append(art)
        reduced_log_uri = f"artifact://reduced_log/{run_id}"
        symbolicated_stack_uri = f"artifact://symbolicated_stack/{run_id}"
        art.update({"reduced_log_uri": reduced_log_uri, "symbolicated_stack_uri": symbolicated_stack_uri})
        signature = f"sig:{run.get('commit_sha') or run_id}:first_failure"
        crashes.append({"crash_id": f"CR-{run_id}", "fingerprint": signature, "build_number": run_id, "platform": run.get("provider"), "count_24h": 1, "top_frame": "main()", "symbolicated_stack_uri": symbolicated_stack_uri})
        return json.dumps({"reduced_log_uri": reduced_log_uri, "symbolicated_stack_uri": symbolicated_stack_uri, "error_signature": signature}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "extract_failure_signals", "description": "Creates deterministic reduced log and symbolicated stack URIs and stores an error signature.", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}}, "required": ["run_id"]}}}


class FindSimilarIncidents(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], signature: str, top_k: int = 5) -> str:
        crashes = _get_table(data, "crash_events")
        neighbors = [c for c in crashes if c.get("fingerprint") == signature][:top_k]
        return json.dumps({"neighbors": neighbors}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_similar_incidents", "description": "Returns prior crash/incidents with identical deterministic fingerprint (simulated semantic match).", "parameters": {"type": "object", "properties": {"signature": {"type": "string"}, "top_k": {"type": "integer"}}, "required": ["signature"]}}}


class EnumerateSuspects(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], failing_sha: str, last_green_sha: Optional[str] = None) -> str:
        commits = _get_table(data, "commits")
        source_changes = _get_table(data, "source_changes")
        ownership = _get_table(data, "ownership_map")
        # Deterministic window: if last_green_sha is missing, use the most recent other change on the same branch/repo as a proxy
        candidate_refs = [failing_sha]
        if last_green_sha:
            candidate_refs.append(last_green_sha)
        candidate = [c for c in source_changes if c.get("commit_sha") in candidate_refs]
        suspects = []
        for ch in candidate:
            files = ch.get("files_changed") or []
            owners = []
            for f in files:
                owner = next((o.get("team_id") for o in ownership if o.get("file_path") and str(o.get("file_path")) in str(f)), None)
                if owner and owner not in owners:
                    owners.append(owner)
            suspects.append({"ref": ch.get("commit_sha"), "author": ch.get("author"), "files": files, "owners": owners})
        return json.dumps({"suspects": suspects}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "enumerate_suspects", "description": "Enumerates suspect changes deterministically from source_changes and ownership_map.", "parameters": {"type": "object", "properties": {"failing_sha": {"type": "string"}, "last_green_sha": {"type": "string"}}, "required": ["failing_sha"]}}}


class RunBisect(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str, suspects: List[Dict[str, Any]], test_target: str) -> str:
        bisects = _get_table(data, "bisect_results")
        existing = next((b for b in bisects if b.get("run_id") == run_id), None)
        if existing:
            return json.dumps(existing, indent=2)
        first_bad = next((s.get("ref") for s in suspects if s.get("ref")), None)
        record = {"run_id": run_id, "test_target": test_target, "first_bad_commit": first_bad, "suspect_count": len(suspects)}
        bisects.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "run_bisect", "description": "Stores a deterministic bisect outcome for a run, selecting the first suspect ref as first_bad_commit.", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}, "suspects": {"type": "array"}, "test_target": {"type": "string"}}, "required": ["run_id", "suspects", "test_target"]}}}


class ProposeFixPatch(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str, logs_uri: Optional[str] = None, first_bad_commit: Optional[str] = None) -> str:
        fixes = _get_table(data, "fix_proposals")
        existing = next((f for f in fixes if f.get("run_id") == run_id), None)
        if existing:
            return json.dumps(existing, indent=2)
        patch_id = f"FP-{run_id}"
        proposal = {"patch_id": patch_id, "run_id": run_id, "logs_uri": logs_uri or f"artifact://logs/{run_id}", "first_bad_commit": first_bad_commit, "status": "proposed"}
        fixes.append(proposal)
        return json.dumps(proposal, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "propose_fix_patch", "description": "Creates a deterministic fix proposal entry for a run.", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}, "logs_uri": {"type": "string"}, "first_bad_commit": {"type": "string"}}, "required": ["run_id"]}}}


class OpenAutoBranch(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], base_ref: str, run_id: str) -> str:
        branches = _get_table(data, "branches")
        name = f"auto/fix-{run_id}"
        existing = next((b for b in branches if b.get("name") == name), None)
        if existing:
            return json.dumps({"branch_ref": name}, indent=2)
        branches.append({"name": name, "base": base_ref})
        return json.dumps({"branch_ref": name}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "open_auto_branch", "description": "Creates a deterministic automation branch 'auto/fix-<run_id>'.", "parameters": {"type": "object", "properties": {"base_ref": {"type": "string"}, "run_id": {"type": "string"}}, "required": ["base_ref", "run_id"]}}}


class CommitPatchToBranch(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], branch_ref: str, patch_id: str, message: str) -> str:
        commits = _get_table(data, "commits")
        max_id = _max_int_suffix(commits, "commit_id", "CMT", 0)
        commit_id = f"CMT-{max_id + 1}"
        commits.append({"commit_id": commit_id, "ref": commit_id, "message": message, "branch": branch_ref, "patch_id": patch_id})
        return json.dumps({"commit_sha": commit_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "commit_patch_to_branch", "description": "Commits the proposed patch as a new commit, deterministically incrementing commit IDs.", "parameters": {"type": "object", "properties": {"branch_ref": {"type": "string"}, "patch_id": {"type": "string"}, "message": {"type": "string"}}, "required": ["branch_ref", "patch_id", "message"]}}}


class OpenDraftPullRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], head: str, base: str, title: str, body: str, run_id: str) -> str:
        prs = _get_table(data, "pull_requests")
        build_runs = _get_table(data, "build_runs")
        artifacts = _get_table(data, "artifacts")
        # Determine max existing PR number, supporting both 'number' (data file) and 'pr_number' (our tool records)
        current_max = 0
        for p in prs:
            val = p.get("pr_number")
            if isinstance(val, int) and val > current_max:
                current_max = val
            val2 = p.get("number")
            if isinstance(val2, int) and val2 > current_max:
                current_max = val2
        pr_number = current_max + 1
        # Resolve structured links from existing records
        br = next((r for r in build_runs if r.get("run_id") == run_id), {})
        art = next((a for a in artifacts if a.get("run_id") == run_id), {})
        links = {
            "run_id": run_id,
            "logs_uri": br.get("logs_uri") or art.get("logs_uri"),
            "artifacts_uri": br.get("artifacts_uri") or art.get("reports_uri"),
        }
        record = {"pr_number": pr_number, "head": head, "base": base, "title": title, "body": body, "draft": True, "links": links}
        prs.append(record)
        return json.dumps({"pr_number": pr_number}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "open_draft_pull_request", "description": "Opens a draft pull request with deterministic pr_number sequencing.", "parameters": {"type": "object", "properties": {"head": {"type": "string"}, "base": {"type": "string"}, "title": {"type": "string"}, "body": {"type": "string"}, "run_id": {"type": "string"}}, "required": ["head", "base", "title", "body", "run_id"]}}}


class CreateOrUpdateTicket(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_key: str, summary: str, description: str, run_id: str, pr_number: Optional[int] = None) -> str:
        work_items = _get_table(data, "work_items")
        existing = next((w for w in work_items if w.get("run_id") == run_id and w.get("project_key") == project_key), None)
        if existing:
            existing.update({"summary": summary, "description": description, "pr_number": pr_number})
            return json.dumps({"ticket_key": existing.get("ticket_key")}, indent=2)
        max_id = _max_int_suffix(work_items, "ticket_key", project_key, 0)
        ticket_key = f"{project_key}-{max_id + 1}"
        rec = {"ticket_key": ticket_key, "project_key": project_key, "summary": summary, "description": description, "run_id": run_id, "pr_number": pr_number, "state": "Open"}
        work_items.append(rec)
        return json.dumps({"ticket_key": ticket_key}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_or_update_ticket", "description": "Creates or updates a deterministic work item ticket keyed by project and run_id.", "parameters": {"type": "object", "properties": {"project_key": {"type": "string"}, "summary": {"type": "string"}, "description": {"type": "string"}, "run_id": {"type": "string"}, "pr_number": {"type": "integer"}}, "required": ["project_key", "summary", "description", "run_id"]}}}


class RunValidationChecks(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], pr_number: int, test_target: str) -> str:
        test_runs = _get_table(data, "test_runs")
        found = next((t for t in test_runs if t.get("pr_number") == pr_number and t.get("test_target") == test_target), None)
        status = found.get("status") if found else "completed"
        result = {"pr_number": pr_number, "test_target": test_target, "status": status}
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "run_validation_checks", "description": "Returns a deterministic validation status for the PR based on existing test_runs rows.", "parameters": {"type": "object", "properties": {"pr_number": {"type": "integer"}, "test_target": {"type": "string"}}, "required": ["pr_number", "test_target"]}}}


class RecordAutomationRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], automation_type: str, inputs: Dict[str, Any], outputs: Dict[str, Any], status: str) -> str:
        runs = _get_table(data, "automation_runs")
        max_id = _max_int_suffix(runs, "run_id", "AR", 0)
        run_id = f"AR-{max_id + 1}"
        rec = {"run_id": run_id, "automation_type": automation_type, "inputs": inputs, "outputs": outputs, "status": status}
        runs.append(rec)
        return json.dumps({"automation_run_id": run_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "record_automation_run", "description": "Persists a deterministic automation_runs entry with next run_id.", "parameters": {"type": "object", "properties": {"automation_type": {"type": "string"}, "inputs": {"type": "object"}, "outputs": {"type": "object"}, "status": {"type": "string"}}, "required": ["automation_type", "inputs", "outputs", "status"]}}}


# ------------------------- ASSET QA (10 tools) -------------------------


class RunDccValidation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], files: List[str]) -> str:
        results = [{"file": f, "issues": []} for f in files]
        return json.dumps({"qa_json": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "run_dcc_validation", "description": "Returns deterministic headless DCC validation results (simulated).", "parameters": {"type": "object", "properties": {"files": {"type": "array", "items": {"type": "string"}}}, "required": ["files"]}}}


class GetAssetFiles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id: str) -> str:
        catalog = _get_table(data, "asset_catalog")
        rec = next((a for a in catalog if a.get("id") == asset_id), None)
        files = [rec.get("asset_path")] if rec and rec.get("asset_path") else []
        return json.dumps({"files": files}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_asset_files", "description": "Retrieves asset file paths from asset_catalog by asset_id.", "parameters": {"type": "object", "properties": {"asset_id": {"type": "string"}}, "required": ["asset_id"]}}}


class ValidateTextures(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], files: List[str]) -> str:
        report = [{"file": f, "ok": True} for f in files]
        return json.dumps({"tex_report": report}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "validate_textures", "description": "Deterministic texture policy checks (simulated).", "parameters": {"type": "object", "properties": {"files": {"type": "array", "items": {"type": "string"}}}, "required": ["files"]}}}


class RunEngineBudgetChecks(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], files: List[str], scene: str) -> str:
        report = {"scene": scene, "files": files, "violations": []}
        return json.dumps({"engine_report": report}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "run_engine_budget_checks", "description": "Runs deterministic engine commandlet budget checks (simulated).", "parameters": {"type": "object", "properties": {"files": {"type": "array", "items": {"type": "string"}}, "scene": {"type": "string"}}, "required": ["files", "scene"]}}}


class ApplyAssetAutofixes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], qa_json: Any, tex_report: Any) -> str:
        commits = _get_table(data, "commits")
        # Determine next deterministic autofix patch id
        next_idx = _max_int_suffix(commits, "patch_id", "AF", 0) + 1
        patch_id = f"AF-{next_idx}"
        return json.dumps({"patch_set": {"mechanical_changes": True, "patch_id": patch_id}}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "apply_asset_autofixes", "description": "Produces a deterministic patch_set representing mechanical fixes only.", "parameters": {"type": "object", "properties": {"qa_json": {"type": "array"}, "tex_report": {"type": "array"}}, "required": ["qa_json", "tex_report"]}}}


class RenderAssetPreviews(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], files: List[str]) -> str:
        previews = {"turntable_uri": f"artifact://turntable/{len(files)}", "stills_uris": [f"artifact://still/{i}" for i, _ in enumerate(files, start=1)]}
        return json.dumps(previews, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "render_asset_previews", "description": "Creates deterministic preview URIs for assets.", "parameters": {"type": "object", "properties": {"files": {"type": "array", "items": {"type": "string"}}}, "required": ["files"]}}}


class UploadQaReports(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], qa_json: Any, tex_report: Any, engine_report: Any, previews: Dict[str, Any]) -> str:
        return json.dumps({"report_uris": {"summary": "artifact://qa/summary", "details": "artifact://qa/details"}}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "upload_qa_reports", "description": "Returns deterministic report URIs for uploaded QA artifacts.", "parameters": {"type": "object", "properties": {"qa_json": {"type": "array"}, "tex_report": {"type": "array"}, "engine_report": {"type": "object"}, "previews": {"type": "object"}}, "required": ["qa_json", "tex_report", "engine_report", "previews"]}}}


class AnnotatePrWithQa(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], pr_number: int, summary: str, report_uri: str) -> str:
        prs = _get_table(data, "pull_requests")
        pr = next((p for p in prs if p.get("pr_number") == pr_number), None)
        if not pr:
            return _error(f"PR '{pr_number}' not found.")
        comments = pr.setdefault("comments", [])
        comments.append({"summary": summary, "report_uri": report_uri})
        return json.dumps({"commented": True, "count": len(comments)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "annotate_pr_with_qa", "description": "Adds a deterministic QA annotation to a PR.", "parameters": {"type": "object", "properties": {"pr_number": {"type": "integer"}, "summary": {"type": "string"}, "report_uri": {"type": "string"}}, "required": ["pr_number", "summary", "report_uri"]}}}


class SetAssetQaCheck(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], pr_number: int, conclusion: str, details_uri: str) -> str:
        prs = _get_table(data, "pull_requests")
        pr = next((p for p in prs if p.get("pr_number") == pr_number), None)
        if not pr:
            return _error(f"PR '{pr_number}' not found.")
        checks = pr.setdefault("checks", [])
        checks.append({"name": "Asset QA", "conclusion": conclusion, "details_uri": details_uri})
        return json.dumps({"check_count": len(checks)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "set_asset_qa_check", "description": "Sets a deterministic PR check result named 'Asset QA'.", "parameters": {"type": "object", "properties": {"pr_number": {"type": "integer"}, "conclusion": {"type": "string"}, "details_uri": {"type": "string"}}, "required": ["pr_number", "conclusion", "details_uri"]}}}


class PersistAssetQaResults(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id: str, commit_sha: str, severity_max: str, errors_count: int, warnings_count: int, preview_uri: str, report_uri: str) -> str:
        qa = _get_table(data, "asset_qa_results")
        qa_id = f"QA-{asset_id}-{commit_sha}"
        existing = next((q for q in qa if q.get("qa_id") == qa_id), None)
        rec = {"qa_id": qa_id, "asset_id": asset_id, "commit_sha": commit_sha, "severity_max": severity_max, "errors_count": errors_count, "warnings_count": warnings_count, "preview_uri": preview_uri, "report_uri": report_uri}
        if existing:
            existing.update(rec)
        else:
            qa.append(rec)
        return json.dumps({"qa_id": qa_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "persist_asset_qa_results", "description": "Persists an asset QA results row keyed by (asset_id, commit_sha).", "parameters": {"type": "object", "properties": {"asset_id": {"type": "string"}, "commit_sha": {"type": "string"}, "severity_max": {"type": "string"}, "errors_count": {"type": "integer"}, "warnings_count": {"type": "integer"}, "preview_uri": {"type": "string"}, "report_uri": {"type": "string"}}, "required": ["asset_id", "commit_sha", "severity_max", "errors_count", "warnings_count", "preview_uri", "report_uri"]}}}


# ------------------------- BUG/FEEDBACK INTAKE (7 tools) -------------------------


class ReceiveTicketWebhook(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], event: str, payload: Dict[str, Any]) -> str:
        work_items = _get_table(data, "work_items")
        key = payload.get("ticket_key") or f"WB-{len(work_items)+1}"
        existing = next((w for w in work_items if w.get("ticket_key") == key), None)
        if existing:
            existing.update({"source": "webhook", "raw": payload})
        else:
            work_items.append({"ticket_key": key, "source": "webhook", "raw": payload, "state": payload.get("state") or "Open"})
        return json.dumps({"ticket_key": key}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "receive_ticket_webhook", "description": "Stores/updates a work item from a webhook payload deterministically.", "parameters": {"type": "object", "properties": {"event": {"type": "string"}, "payload": {"type": "object"}}, "required": ["event", "payload"]}}}


class NormalizeIssue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ticket_key: str) -> str:
        work_items = _get_table(data, "work_items")
        item = next((w for w in work_items if w.get("ticket_key") == ticket_key), None)
        if not item:
            return _error(f"Ticket '{ticket_key}' not found.")
        raw = item.get("raw") or {}
        normalized = {"ticket_key": ticket_key, "title": raw.get("title") or item.get("title"), "description": raw.get("description") or item.get("description"), "severity": raw.get("severity") or "Medium", "module": raw.get("module")}
        item["normalized"] = normalized
        return json.dumps(normalized, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "normalize_issue", "description": "Derives a normalized subset of issue fields deterministically from stored payload.", "parameters": {"type": "object", "properties": {"ticket_key": {"type": "string"}}, "required": ["ticket_key"]}}}


class SummarizeIssue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ticket_key: str) -> str:
        work_items = _get_table(data, "work_items")
        item = next((w for w in work_items if w.get("ticket_key") == ticket_key), None)
        if not item:
            return _error(f"Ticket '{ticket_key}' not found.")
        norm = item.get("normalized") or {}
        desc = (norm.get("description") or "")[:140]
        summary = f"{norm.get('title') or 'Issue'} :: {desc}"
        item["summary_text"] = summary
        return json.dumps({"summary_text": summary}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "summarize_issue", "description": "Creates a deterministic short summary from normalized fields.", "parameters": {"type": "object", "properties": {"ticket_key": {"type": "string"}}, "required": ["ticket_key"]}}}


class ComputeImpactScore(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ticket_key: str, fingerprint: Optional[str] = None) -> str:
        work_items = _get_table(data, "work_items")
        crashes = _get_table(data, "crash_events")
        item = next((w for w in work_items if w.get("ticket_key") == ticket_key), None)
        if not item:
            return _error(f"Ticket '{ticket_key}' not found.")
        sev = (item.get("normalized") or {}).get("severity", "Medium")
        sev_weight = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}.get(sev, 2)
        crash_count = 0
        if fingerprint:
            crash_count = sum(1 for c in crashes if c.get("fingerprint") == fingerprint)
        impact = sev_weight * (1 + crash_count)
        item["impact_score"] = impact
        return json.dumps({"impact_score": impact}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "compute_impact_score", "description": "Deterministically computes an impact score from severity weight and optional crash fingerprint count.", "parameters": {"type": "object", "properties": {"ticket_key": {"type": "string"}, "fingerprint": {"type": "string"}}, "required": ["ticket_key"]}}}


class ResolveOwnerFromMap(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], module_or_path: str) -> str:
        ownership = _get_table(data, "ownership_map")
        # Support both 'module_or_path' and 'file_path' keys from the dataset; return the owning team_id deterministically
        match = next((o for o in ownership if o.get("module_or_path") == module_or_path or o.get("file_path") == module_or_path), None)
        owner_team = (match or {}).get("owner_team") or (match or {}).get("team_id")
        return json.dumps({"owner_team": owner_team}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "resolve_owner_from_map", "description": "Resolves owner team deterministically from ownership_map.", "parameters": {"type": "object", "properties": {"module_or_path": {"type": "string"}}, "required": ["module_or_path"]}}}


class LinkDuplicateIssue(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], primary_ticket_key: str, duplicate_ticket_key: str, confidence: float) -> str:
        links = _get_table(data, "bug_links")
        link_id = f"LINK-{len(links) + 1}"
        rec = {"link_id": link_id, "primary_bug_id": primary_ticket_key, "related_bug_id": duplicate_ticket_key, "relation_type": "duplicate", "confidence": confidence}
        links.append(rec)
        return json.dumps({"link_id": link_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "link_duplicate_issue", "description": "Links two tickets as duplicate with provided confidence.", "parameters": {"type": "object", "properties": {"primary_ticket_key": {"type": "string"}, "duplicate_ticket_key": {"type": "string"}, "confidence": {"type": "number"}}, "required": ["primary_ticket_key", "duplicate_ticket_key", "confidence"]}}}


class UpdateTicketFields(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ticket_key: str, fields: Dict[str, Any]) -> str:
        work_items = _get_table(data, "work_items")
        # Support both schemas: some datasets store the key under 'id', others under 'ticket_key'
        item = next((w for w in work_items if w.get("ticket_key") == ticket_key or w.get("id") == ticket_key), None)
        if not item:
            return _error(f"Ticket '{ticket_key}' not found.")
        item.update(fields or {})
        return json.dumps({"updated": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_ticket_fields", "description": "Updates fields on a ticket deterministically.", "parameters": {"type": "object", "properties": {"ticket_key": {"type": "string"}, "fields": {"type": "object"}}, "required": ["ticket_key", "fields"]}}}


# ------------------------- LOCALIZATION/VO (6 tools) -------------------------


class DetectChangedStrings(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], pr_number: int) -> str:
        loc_strings = _get_table(data, "loc_strings")
        # Deterministically return all keys changed in last_changed_commit matching PR head commit if linked
        prs = _get_table(data, "pull_requests")
        pr = next((p for p in prs if p.get("pr_number") == pr_number), None)
        head_commit = (pr or {}).get("head")
        changed = [row.get("string_key") for row in loc_strings if row.get("last_changed_commit") == head_commit]
        return json.dumps({"changed_keys": changed}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "detect_changed_strings", "description": "Returns string keys whose last_changed_commit equals the PR head commit.", "parameters": {"type": "object", "properties": {"pr_number": {"type": "integer"}}, "required": ["pr_number"]}}}


class CaptureLocContext(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], keys: List[str]) -> str:
        context = {k: f"artifact://context/{k}" for k in keys}
        return json.dumps({"context_uris": context}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "capture_loc_context", "description": "Returns deterministic context media URIs per string key.", "parameters": {"type": "object", "properties": {"keys": {"type": "array", "items": {"type": "string"}}}, "required": ["keys"]}}}


class LocLint(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], locale: str, keys: List[str], ui_px_limit: int) -> str:
        # Simple deterministic length check against limit
        translations = _get_table(data, "translations")
        issues = []
        for k in keys:
            row = next((t for t in translations if t.get("string_key") == k and t.get("locale") == locale), None)
            if row and len(row.get("target_text", "")) > ui_px_limit:
                issues.append({"string_key": k, "overflow": len(row.get("target_text")) - ui_px_limit})
        return json.dumps({"lint_report": issues}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "loc_lint", "description": "Checks translated texts against a deterministic pixel budget by length proxy.", "parameters": {"type": "object", "properties": {"locale": {"type": "string"}, "keys": {"type": "array", "items": {"type": "string"}}, "ui_px_limit": {"type": "integer"}}, "required": ["locale", "keys", "ui_px_limit"]}}}


class ValidateSubtitleTiming(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], line_id: str, locale: str) -> str:
        timing = _get_table(data, "subtitle_timing")
        # Support either 'line_id' or 'id' for record identification and nested timing status
        row = next((r for r in timing if (r.get("line_id") or r.get("id")) == line_id and r.get("locale") == locale), None)
        status = "unknown"
        if row:
            # Prefer flat 'validation_status' if present; otherwise read nested timing_validation.status
            status = row.get("validation_status") or ((row.get("timing_validation") or {}).get("status") or "unknown")
        return json.dumps({"validation_status": status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "validate_subtitle_timing", "description": "Returns stored validation status for a subtitle line and locale.", "parameters": {"type": "object", "properties": {"line_id": {"type": "string"}, "locale": {"type": "string"}}, "required": ["line_id", "locale"]}}}


class WriteLocaleBundle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], locale: str, keys: List[str]) -> str:
        localization_workflow = _get_table(data, "localization_workflow")
        bundle_name = f"bundle-{locale}-{len(keys)}"
        entry = {"bundle": bundle_name, "locale": locale, "keys": keys}
        localization_workflow.append(entry)
        return json.dumps({"bundle_uri": f"artifact://bundle/{bundle_name}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "write_locale_bundle", "description": "Writes a deterministic locale bundle record and returns a bundle URI.", "parameters": {"type": "object", "properties": {"locale": {"type": "string"}, "keys": {"type": "array", "items": {"type": "string"}}}, "required": ["locale", "keys"]}}}


class CreateTmsJob(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], bundle_name: str, locales: List[str], status: str) -> str:
        tms = _get_table(data, "tms_jobs")
        max_id = _max_int_suffix(tms, "job_id", "TMS", 0)
        job_id = f"TMS-{max_id + 1}"
        rec = {"job_id": job_id, "bundle_name": bundle_name, "locales": locales, "status": status}
        tms.append(rec)
        return json.dumps({"job_id": job_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_tms_job", "description": "Creates a deterministic TMS job with next job_id.", "parameters": {"type": "object", "properties": {"bundle_name": {"type": "string"}, "locales": {"type": "array", "items": {"type": "string"}}, "status": {"type": "string"}}, "required": ["bundle_name", "locales", "status"]}}}


# Utility tool to return a deterministic scalar value as the final task output
class ReturnScalar(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], value: str) -> str:
        return str(value)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "return_scalar", "description": "Returns the provided scalar value as-is.", "parameters": {"type": "object", "properties": {"value": {"type": "string"}}, "required": ["value"]}}}


# Deterministic helper to retrieve a project key from projects.json
class GetProjectKey(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id: Optional[str] = None) -> str:
        projects = _get_table(data, "projects")
        proj = None
        if project_id:
            proj = next((p for p in projects if p.get("id") == project_id), None)
        if not proj:
            # Fallback deterministically to the lexicographically smallest id
            proj = sorted(projects, key=lambda x: x.get("id", ""))[0] if projects else None
        key = (proj or {}).get("project_key")
        return json.dumps({"project_key": key}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_project_key", "description": "Returns a deterministic project_key from projects.json (by id if provided, else first by id).", "parameters": {"type": "object", "properties": {"project_id": {"type": "string"}}, "required": []}}}


TOOLS = [
    # CI triage
    ReceiveCiEvent(),
    AttachRunArtifacts(),
    ExtractFailureSignals(),
    FindSimilarIncidents(),
    EnumerateSuspects(),
    RunBisect(),
    ProposeFixPatch(),
    OpenAutoBranch(),
    CommitPatchToBranch(),
    OpenDraftPullRequest(),
    CreateOrUpdateTicket(),
    RunValidationChecks(),
    RecordAutomationRun(),

    # Asset QA
    GetAssetFiles(),
    RunDccValidation(),
    ValidateTextures(),
    RunEngineBudgetChecks(),
    ApplyAssetAutofixes(),
    RenderAssetPreviews(),
    UploadQaReports(),
    AnnotatePrWithQa(),
    SetAssetQaCheck(),
    PersistAssetQaResults(),

    # Bug intake
    ReceiveTicketWebhook(),
    NormalizeIssue(),
    SummarizeIssue(),
    ComputeImpactScore(),
    ResolveOwnerFromMap(),
    LinkDuplicateIssue(),
    UpdateTicketFields(),

    # Localization/VO
    DetectChangedStrings(),
    CaptureLocContext(),
    LocLint(),
    ValidateSubtitleTiming(),
    WriteLocaleBundle(),
    CreateTmsJob(),
    # utility
    # ReturnScalar must be listed to be invokable in tasks
    ReturnScalar(),
    GetProjectKey(),
]
