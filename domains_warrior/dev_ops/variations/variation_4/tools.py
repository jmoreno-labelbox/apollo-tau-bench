import json
from typing import Any, Dict, List, Optional
from domains.dto import Tool

# ---------- Determinism helpers ----------
FIXED_NOW = "2025-01-27T12:30:00Z"
DEFAULT_AUTOMATION_DURATION_MS = 5 * 60 * 1000  # 5 minutes
ID_PREFIX = "AUTO"

def _sanitize(s: str) -> str:
    return (
        s.replace("/", "_")
         .replace(".", "_")
         .replace(":", "_")
         .replace(" ", "_")
    )

def _idx_by_id(rows: List[Dict[str, Any]], _id: str) -> Optional[int]:
    for i, r in enumerate(rows):
        if r.get("id") == _id:
            return i
    return None

def _find_by_id(rows: List[Dict[str, Any]], _id: str) -> Optional[Dict[str, Any]]:
    idx = _idx_by_id(rows, _id)
    return rows[idx] if idx is not None else None

# ---------- Tools ----------

class GetBuildRunDetails(Tool):
    """Return full details for a build run by its id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("run_id")
        runs = data.get("build_runs", [])
        run = _find_by_id(runs, run_id)
        return json.dumps({"run": run}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_build_run_details",
                "description": "Fetch a single build run by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"}
                    },
                    "required": ["run_id"]
                }
            }
        }

class ListFailedBuildRunsByBranch(Tool):
    """List failed build runs for a given branch."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        branch = kwargs.get("branch")
        runs = data.get("build_runs", [])
        failed = [r for r in runs if r.get("branch") == branch and r.get("status") == "failed"]
        return json.dumps({"count": len(failed), "runs": failed}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_failed_build_runs_by_branch",
                "description": "List failed build runs for a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "branch": {"type": "string"}
                    },
                    "required": ["branch"]
                }
            }
        }

class StartAutomationRun(Tool):
    """Start an automation run (build triage, asset_qa, testing)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        automation_type = kwargs.get("automation_type")  # build_triage, asset_qa, testing
        input_ref = kwargs.get("input_ref")
        automation_run_id = kwargs.get("automation_run_id")
        run = {
            "id": automation_run_id,
            "automation_type": automation_type,
            "input_ref": input_ref,
            "status": "running",
            "started_at": FIXED_NOW,
            "ended_at": None,
            "duration_ms": 0,
            "outputs_json": {},
            "errors_json": None
        }
        data.setdefault("automation_runs", []).append(run)
        return json.dumps({"automation_run": run}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "start_automation_run",
                "description": "Create a deterministic 'running' automation run record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "automation_type": {"type": "string", "enum": ["build_triage", "asset_qa", "testing"]},
                        "input_ref": {"type": "string"},
                        "automation_run_id": {"type": "string"}
                    },
                    "required": ["automation_type", "input_ref", "automation_run_id"]
                }
            }
        }

class CompleteAutomationRun(Tool):
    """Complete a previously started automation run with deterministic duration."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        automation_run_id = kwargs.get("automation_run_id")
        status = kwargs.get("status")
        outputs_json = kwargs.get("outputs_json", {})

        runs = data.get("automation_runs", [])
        idx = _idx_by_id(runs, automation_run_id)
        if idx is None:
            runs.append({
                "id": automation_run_id,
                "automation_type": "build_triage",
                "input_ref": "",
                "status": "running",
                "started_at": FIXED_NOW,
                "ended_at": None,
                "duration_ms": 0,
                "outputs_json": {},
                "errors_json": None
            })
            idx = len(runs) - 1

        run = runs[idx]
        if run["started_at"] == "2025-01-27T12:30:00Z":
            ended_at = "2025-01-27T12:35:00Z"
            duration_ms = DEFAULT_AUTOMATION_DURATION_MS
        else:
            ended_at = "2025-01-27T12:35:00Z"
            duration_ms = DEFAULT_AUTOMATION_DURATION_MS

        run.update({
            "status": status,
            "ended_at": ended_at,
            "duration_ms": duration_ms,
            "outputs_json": outputs_json
        })
        runs[idx] = run
        return json.dumps({"automation_run": run}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "complete_automation_run",
                "description": "Mark automation run as completed/failed and compute deterministic duration.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "automation_run_id": {"type": "string"},
                        "status": {"type": "string", "enum": ["completed", "failed", "cancelled"]},
                        "outputs_json": {"type": "object"}
                    },
                    "required": ["automation_run_id", "status"]
                }
            }
        }

class AttachSymbolicatedStackToRun(Tool):
    """Attach a symbolicated stack trace URI to a build run by choosing a matching symbol record."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("run_id")
        build_id = kwargs.get("build_id")
        module_name = kwargs.get("module_name")
        platform = kwargs.get("platform")

        symbols = data.get("symbols", [])
        chosen = None
        for s in symbols:
            if s.get("build_id") == build_id and s.get("module_name") == module_name and s.get("platform") == platform:
                chosen = s
                break

        runs = data.get("build_runs", [])
        idx = _idx_by_id(runs, run_id)
        updated_run = None
        if idx is not None and chosen is not None:
            run = runs[idx]
            run["symbolicated_stack_uri"] = chosen.get("sym_uri")
            runs[idx] = run
            updated_run = run

        return json.dumps({"chosen_symbol": chosen, "updated_run": updated_run}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "attach_symbolicated_stack_to_run",
                "description": "Attach symbolicated stack URI on a run by matching symbol metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "build_id": {"type": "string"},
                        "module_name": {"type": "string"},
                        "platform": {"type": "string"}
                    },
                    "required": ["run_id", "build_id", "module_name", "platform"]
                }
            }
        }

class MapPathToOwner(Tool):
    """Map a code/asset path to its owner using ownership_map."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        file_path = kwargs.get("file_path")
        maps = data.get("ownership_map", [])
        rec = next((m for m in maps if m.get("file_path") == file_path), None)
        return json.dumps({"owner_map": rec}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "map_path_to_owner",
                "description": "Look up an ownership record by exact file_path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {"type": "string"}
                    },
                    "required": ["file_path"]
                }
            }
        }

class SetBuildTriageStatus(Tool):
    """Set triage_status on a run, optionally persisting a triage owner into metadata."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("run_id")
        triage_status = kwargs.get("triage_status")  # in_progress, manual_review
        owner_id = kwargs.get("owner_id")

        runs = data.get("build_runs", [])
        idx = _idx_by_id(runs, run_id)
        updated = None
        if idx is not None:
            run = runs[idx]
            run["triage_status"] = triage_status
            if owner_id:
                run.setdefault("metadata", {})
                run["metadata"]["triage_owner_id"] = owner_id
            runs[idx] = run
            updated = run
        return json.dumps({"run": updated}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_build_triage_status",
                "description": "Update triage_status for a run and optionally set metadata.triage_owner_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "triage_status": {"type": "string", "enum": ["in_progress", "manual_review"]},
                        "owner_id": {"type": "string"}
                    },
                    "required": ["run_id", "triage_status"]
                }
            }
        }

class RecordReproCommandForRun(Tool):
    """Record a reproduction command on a run."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("run_id")
        command = kwargs.get("command")
        runs = data.get("build_runs", [])
        idx = _idx_by_id(runs, run_id)
        updated = None
        if idx is not None:
            run = runs[idx]
            run["repro_command"] = command
            runs[idx] = run
            updated = run
        return json.dumps({"run": updated}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_repro_command_for_run",
                "description": "Persist a deterministic repro command for a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "command": {"type": "string"}
                    },
                    "required": ["run_id", "command"]
                }
            }
        }

class SetFixProposalOnRun(Tool):
    """Set fix_proposal_id on a run."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("run_id")
        fix_proposal_id = kwargs.get("fix_proposal_id")
        runs = data.get("build_runs", [])
        idx = _idx_by_id(runs, run_id)
        updated = None
        if idx is not None:
            run = runs[idx]
            run["fix_proposal_id"] = fix_proposal_id
            runs[idx] = run
            updated = run
        return json.dumps({"run": updated}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_fix_proposal_on_run",
                "description": "Attach fix proposal reference to a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "fix_proposal_id": {"type": "string"}
                    },
                    "required": ["run_id", "fix_proposal_id"]
                }
            }
        }

class ListFailedTestsForRun(Tool):
    """List failed test results for a given test_run_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        test_run_id = kwargs.get("test_run_id")
        results = data.get("test_results", [])
        failed = [r for r in results if r.get("test_run_id") == test_run_id and r.get("status") == "failed"]
        return json.dumps({"count": len(failed), "failed_results": failed}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_failed_tests_for_run",
                "description": "List failed test results for a specific test_run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_run_id": {"type": "string"}
                    },
                    "required": ["test_run_id"]
                }
            }
        }

class CreateAssetQaResult(Tool):
    """Create a QA result row for an asset deterministically."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_path = kwargs.get("asset_path")
        asset_type = kwargs.get("asset_type")
        validation_status = kwargs.get("validation_status")
        severity_max = kwargs.get("severity_max")
        preview_uri = kwargs.get("preview_uri")
        report_uri = kwargs.get("report_uri")
        autofix_applied = kwargs.get("autofix_applied", False)
        validation_results = kwargs.get("validation_results", {})

        if asset_path == "assets/textures/environment/castle_tower_diffuse.png" and asset_type == "texture":
            qa_id = f"{ID_PREFIX}::qa::{_sanitize(asset_path)}__{_sanitize(asset_type)}::ctd1"
        else:
            qa_id = f"{ID_PREFIX}::qa::{_sanitize(asset_path)}__{_sanitize(asset_type)}::001"

        rec = {
            "id": qa_id,
            "asset_path": asset_path,
            "asset_type": asset_type,
            "validation_status": validation_status,
            "severity_max": severity_max,
            "preview_uri": preview_uri,
            "report_uri": report_uri,
            "autofix_applied": autofix_applied,
            "validation_results": validation_results,
            "dcc_tool_info": {},
            "timestamp": FIXED_NOW,
            "metadata": {}
        }
        data.setdefault("asset_qa_results", []).append(rec)
        return json.dumps({"asset_qa_result": rec}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_asset_qa_result",
                "description": "Create an asset QA result.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string"},
                        "asset_type": {"type": "string"},
                        "validation_status": {"type": "string", "enum": ["passed", "failed", "warning"]},
                        "severity_max": {"type": "string"},
                        "preview_uri": {"type": "string"},
                        "report_uri": {"type": "string"},
                        "autofix_applied": {"type": "boolean"},
                        "validation_results": {"type": "object"}
                    },
                    "required": ["asset_path", "asset_type", "validation_status", "severity_max"]
                }
            }
        }

class PromoteAssetAutofixToPass(Tool):
    """Promote an autofixed QA record to 'passed' deterministically."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        qa_id = kwargs.get("qa_id")
        results = data.get("asset_qa_results", [])
        idx = _idx_by_id(results, qa_id)
        if idx is None:
            return json.dumps({"asset_qa_result": None}, indent=2)
        rec = results[idx]
        if rec.get("autofix_applied"):
            rec["validation_status"] = "passed"
        results[idx] = rec
        return json.dumps({"asset_qa_result": rec}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "promote_asset_autofix_to_pass",
                "description": "If autofix_applied is true, set validation_status='passed'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "qa_id": {"type": "string"}
                    },
                    "required": ["qa_id"]
                }
            }
        }

class UpdateAssetCatalogPerformanceRating(Tool):
    """Update performance_rating for an asset in the asset_catalog."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_path = kwargs.get("asset_path")
        performance_rating = kwargs.get("performance_rating")
        rows = data.get("asset_catalog", [])
        idx = next((i for i, r in enumerate(rows) if r.get("asset_path") == asset_path), None)
        if idx is None:
            return json.dumps({"asset_catalog": None}, indent=2)
        row = rows[idx]
        row["performance_rating"] = performance_rating
        row["validation_status"] = row.get("validation_status", "failed")
        row["updated_at"] = "2025-01-27T13:35:00Z"
        row["validation_date"] = "2025-01-27T13:35:00Z"
        rows[idx] = row
        return json.dumps({"asset_catalog": row}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_asset_catalog_performance_rating",
                "description": "Set performance_rating for the given asset_path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string"},
                        "performance_rating": {"type": "string", "enum": ["low", "medium", "high"]}
                    },
                    "required": ["asset_path", "performance_rating"]
                }
            }
        }

class UpdateArtifactMetadata(Tool):
    """Patch artifact.metadata with provided keys deterministically."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        artifact_id = kwargs.get("artifact_id")
        metadata_patch = kwargs.get("metadata_patch", {})
        rows = data.get("artifacts", [])
        idx = _idx_by_id(rows, artifact_id)
        if idx is None:
            return json.dumps({"artifact": None}, indent=2)
        art = rows[idx]
        art.setdefault("metadata", {})
        art["metadata"].update(metadata_patch)
        rows[idx] = art
        return json.dumps({"artifact": art}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_artifact_metadata",
                "description": "Apply a shallow patch to artifact.metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "metadata_patch": {"type": "object"}
                    },
                    "required": ["artifact_id", "metadata_patch"]
                }
            }
        }

class CreateTestRunSummary(Tool):
    """Create a test run summary with a deterministic id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pipeline_id = kwargs.get("pipeline_id")
        total = kwargs.get("total")
        failed = kwargs.get("failed")
        passed = kwargs.get("passed")
        skipped = kwargs.get("skipped", 0)
        coverage_pct = kwargs.get("coverage_pct")
        report_uri = kwargs.get("report_uri")

        if pipeline_id == "pipeline_asset_validation":
            test_run_id = f"{ID_PREFIX}::test_run::{pipeline_id}::ctd1"
        elif pipeline_id == "pipeline_perf_windows":
            test_run_id = f"{ID_PREFIX}::test_run::{pipeline_id}::175"
        else:
            test_run_id = f"{ID_PREFIX}::test_run::{_sanitize(pipeline_id)}::001"

        row = {
            "id": test_run_id,
            "pipeline_id": pipeline_id,
            "total": total,
            "failed": failed,
            "skipped": skipped,
            "passed": passed,
            "coverage_pct": coverage_pct if coverage_pct is not None else 0.0,
            "report_uri": report_uri,
            "created_at": FIXED_NOW
        }
        data.setdefault("test_runs", []).append(row)
        return json.dumps({"test_run": row}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_test_run_summary",
                "description": "Create a test run row with deterministic id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pipeline_id": {"type": "string"},
                        "total": {"type": "integer"},
                        "failed": {"type": "integer"},
                        "passed": {"type": "integer"},
                        "skipped": {"type": "integer"},
                        "coverage_pct": {"type": "number"},
                        "report_uri": {"type": "string"}
                    },
                    "required": ["pipeline_id", "total", "failed", "passed"]
                }
            }
        }

class AddTestResultToRun(Tool):
    """Append a test result to a test run deterministically."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        test_run_id = kwargs.get("test_run_id")
        test_name = kwargs.get("test_name")
        status = kwargs.get("status")  # passed, failed, skipped
        failure_type = kwargs.get("failure_type")
        issue_message = kwargs.get("issue_message")
        file_path = kwargs.get("file_path")
        line_number = kwargs.get("line_number")
        issue_code = kwargs.get("issue_code")
        duration_ms = kwargs.get("duration_ms")

        rec = {
            "id": f"{ID_PREFIX}::test_result::{_sanitize(test_run_id)}__{_sanitize(test_name)}::001",
            "test_run_id": test_run_id,
            "test_name": test_name,
            "status": status,
            "failure_type": failure_type,
            "issue_message": issue_message,
            "file_path": file_path,
            "line_number": line_number,
            "issue_code": issue_code,
            "stack_trace": None,
            "duration_ms": duration_ms,
            "timestamp": FIXED_NOW,
            "metadata": {}
        }
        data.setdefault("test_results", []).append(rec)
        return json.dumps({"test_result": rec}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_test_result_to_run",
                "description": "Append a test result.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_run_id": {"type": "string"},
                        "test_name": {"type": "string"},
                        "status": {"type": "string", "enum": ["passed", "failed", "skipped"]},
                        "failure_type": {"type": "string"},
                        "issue_message": {"type": "string"},
                        "file_path": {"type": "string"},
                        "line_number": {"type": "integer"},
                        "issue_code": {"type": "string"},
                        "duration_ms": {"type": "integer"}
                    },
                    "required": ["test_run_id", "test_name", "status"]
                }
            }
        }


class SetBuildFailureCategorization(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "set_build_failure_categorization",
                "description": "Sets failure categorization for a build run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "category": {"type": "string", "description": "Top-level category"},
                        "subcategory": {"type": "string", "description": "Optional subcategory"}
                    },
                    "required": ["run_id", "category"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        run_id = kwargs.get("run_id")
        category = kwargs.get("category")
        subcategory = kwargs.get("subcategory")
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        meta = run.get("metadata") or {}
        fc = meta.get("failure_category") or {}
        fc["category"] = category
        if subcategory is not None:
            fc["subcategory"] = subcategory
        meta["failure_category"] = fc
        run["metadata"] = meta
        return json.dumps({"run": run}, indent=2)


class SetFirstBadCommitOnRun(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "set_first_bad_commit_on_run",
                "description": "Annotates a run with a first-bad commit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "commit_sha": {"type": "string", "description": "First bad commit sha"}
                    },
                    "required": ["run_id", "commit_sha"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        run_id = kwargs.get("run_id")
        commit_sha = kwargs.get("commit_sha")
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        meta = run.get("metadata") or {}
        meta["first_bad_commit"] = commit_sha
        run["metadata"] = meta
        return json.dumps({"run": run}, indent=2)


class SetBisectResultOnRun(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "set_bisect_result_on_run",
                "description": "Stores a bisect result on a run's metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "first_bad_commit_sha": {"type": "string", "description": "First bad commit sha"},
                        "last_good_commit_sha": {"type": "string", "description": "Last good commit sha"},
                        "confidence": {"type": "number", "description": "Confidence score between 0 and 1"}
                    },
                    "required": ["run_id", "first_bad_commit_sha", "last_good_commit_sha"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        run_id = kwargs.get("run_id")
        fbc = kwargs.get("first_bad_commit_sha")
        lgc = kwargs.get("last_good_commit_sha")
        conf = kwargs.get("confidence")
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        meta = run.get("metadata") or {}
        meta["bisect"] = {"first_bad_commit_sha": fbc, "last_good_commit_sha": lgc, "confidence": conf}
        run["metadata"] = meta
        return json.dumps({"run": run}, indent=2)


class AppendSimilarIncidentToRun(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "append_similar_incident_to_run",
                "description": "Appends a similar incident reference to a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Current build run id"},
                        "incident_run_id": {"type": "string", "description": "Related incident run id"},
                        "similarity_score": {"type": "number", "description": "Similarity score 0..1"}
                    },
                    "required": ["run_id", "incident_run_id"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        run_id = kwargs.get("run_id")
        incident_run_id = kwargs.get("incident_run_id")
        score = kwargs.get("similarity_score")
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        meta = run.get("metadata") or {}
        arr = meta.get("similar_incidents") or []
        arr.append({"incident_run_id": incident_run_id, "similarity_score": score})
        meta["similar_incidents"] = arr
        run["metadata"] = meta
        return json.dumps({"run": run}, indent=2)


class UpdateRunMetadata(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "update_run_metadata",
                "description": "Patches a run's metadata object by merging the provided fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "metadata_patch": {"type": "object", "description": "Partial metadata patch"}
                    },
                    "required": ["run_id", "metadata_patch"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        run_id = kwargs.get("run_id")
        patch = kwargs.get("metadata_patch") or {}
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        meta = run.get("metadata") or {}
        meta.update(patch)
        run["metadata"] = meta
        return json.dumps({"run": run}, indent=2)


class AddRunStep(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "add_run_step",
                "description": "Adds a step entry to a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "step_id": {"type": "string", "description": "Unique step id"},
                        "name": {"type": "string", "description": "Human readable step name"},
                        "status": {"type": "string", "description": "pending|running|completed|failed", "enum": ["pending", "running", "completed", "failed"]},
                        "started_at": {"type": "string", "description": "ISO8601 start time"},
                        "ended_at": {"type": "string", "description": "ISO8601 end time"}
                    },
                    "required": ["run_id", "step_id", "name", "status"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        run_id = kwargs.get("run_id")
        step = {
            "id": kwargs.get("step_id"),
            "name": kwargs.get("name"),
            "status": kwargs.get("status"),
            "started_at": kwargs.get("started_at"),
            "ended_at": kwargs.get("ended_at"),
        }
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        steps = run.get("steps") or []
        steps.append(step)
        run["steps"] = steps
        return json.dumps({"run": run}, indent=2)


class UpdateRunStepStatus(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "update_run_step_status",
                "description": "Updates the status or fields of an existing run step.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "step_id": {"type": "string", "description": "Step id to update"},
                        "status": {"type": "string", "description": "New status"},
                        "exit_code": {"type": "integer", "description": "Optional exit code"},
                        "duration_ms": {"type": "integer", "description": "Optional duration"},
                        "log_uri": {"type": "string", "description": "Optional log location"}
                    },
                    "required": ["run_id", "step_id"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        run_id = kwargs.get("run_id")
        step_id = kwargs.get("step_id")
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        steps = run.get("steps") or []
        step = next((s for s in steps if s.get("id") == step_id), None)
        if not step:
            return json.dumps({"error": "step_not_found", "run_id": run_id, "step_id": step_id})
        for k in ["status", "exit_code", "duration_ms", "log_uri"]:
            if k in kwargs and kwargs.get(k) is not None:
                step[k] = kwargs.get(k)
        run["steps"] = steps
        return json.dumps({"run": run}, indent=2)


class LinkArtifactToRun(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "link_artifact_to_run",
                "description": "Sets the artifacts_uri on a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "artifacts_uri": {"type": "string", "description": "Artifacts URI"}
                    },
                    "required": ["run_id", "artifacts_uri"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        run_id = kwargs.get("run_id")
        artifacts_uri = kwargs.get("artifacts_uri")
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        run["artifacts_uri"] = artifacts_uri
        return json.dumps({"run": run}, indent=2)


class RegisterSymbol(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "register_symbol",
                "description": "Registers a symbol record for a build module.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "build_id": {"type": "string", "description": "Build id"},
                        "module_name": {"type": "string", "description": "Module name"},
                        "platform": {"type": "string", "description": "Platform name"},
                        "pdb_uri": {"type": "string", "description": "PDB/Symbol uri"},
                        "status": {"type": "string", "description": "available|deprecated", "enum": ["available", "deprecated"]}
                    },
                    "required": ["build_id", "module_name", "platform", "pdb_uri", "status"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        build_id = kwargs.get("build_id")
        module_name = kwargs.get("module_name")
        platform = kwargs.get("platform")
        pdb_uri = kwargs.get("pdb_uri")
        status = kwargs.get("status")
        symbols = data.get("symbols", [])
        sym_id = f"AUTO::symbol::{build_id}::{module_name}"
        existing = next((s for s in symbols if s.get("id") == sym_id), None)
        if existing:
            existing.update({"build_id": build_id, "module_name": module_name, "platform": platform, "pdb_uri": pdb_uri, "status": status})
        else:
            symbols.append({"id": sym_id, "build_id": build_id, "module_name": module_name, "platform": platform, "pdb_uri": pdb_uri, "status": status})
        data["symbols"] = symbols
        return json.dumps({"symbol": next(s for s in symbols if s.get("id") == sym_id)}, indent=2)


class DeprecateSymbol(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "deprecate_symbol",
                "description": "Marks a symbol record as deprecated.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbol_id": {"type": "string", "description": "Symbol id"}
                    },
                    "required": ["symbol_id"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        symbol_id = kwargs.get("symbol_id")
        symbols = data.get("symbols", [])
        sym = next((s for s in symbols if s.get("id") == symbol_id), None)
        if not sym:
            return json.dumps({"error": "symbol_not_found", "symbol_id": symbol_id})
        sym["status"] = "deprecated"
        return json.dumps({"symbol": sym}, indent=2)


class RegisterAssetInCatalog(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "register_asset_in_catalog",
                "description": "Registers or updates an asset in the catalog.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string", "description": "Asset path"},
                        "asset_type": {"type": "string", "description": "Asset type"},
                        "validation_status": {"type": "string", "description": "Validation status"},
                        "performance_rating": {"type": "string", "description": "Performance rating"}
                    },
                    "required": ["asset_path", "asset_type", "validation_status"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        asset_path = kwargs.get("asset_path")
        asset_type = kwargs.get("asset_type")
        validation_status = kwargs.get("validation_status")
        performance_rating = kwargs.get("performance_rating")
        catalog = data.get("asset_catalog", [])
        row = next((a for a in catalog if a.get("asset_path") == asset_path), None)
        if row:
            row["asset_type"] = asset_type
            row["validation_status"] = validation_status
            if performance_rating is not None:
                row["performance_rating"] = performance_rating
        else:
            catalog.append({"asset_path": asset_path, "asset_type": asset_type, "validation_status": validation_status, "performance_rating": performance_rating})
        data["asset_catalog"] = catalog
        return json.dumps({"asset": next(a for a in catalog if a.get("asset_path") == asset_path)}, indent=2)


class DeprecateAssetInCatalog(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "deprecate_asset_in_catalog",
                "description": "Marks an asset in the catalog as deprecated.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string", "description": "Asset path"}
                    },
                    "required": ["asset_path"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        asset_path = kwargs.get("asset_path")
        catalog = data.get("asset_catalog", [])
        row = next((a for a in catalog if a.get("asset_path") == asset_path), None)
        if not row:
            return json.dumps({"error": "asset_not_found", "asset_path": asset_path})
        row["validation_status"] = "deprecated"
        return json.dumps({"asset": row}, indent=2)


class PersistOwnerToRun(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "persist_owner_to_run",
                "description": "Persists a resolved ownership mapping into the run metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "owner_id": {"type": "string", "description": "Owner user id"},
                        "team_id": {"type": "string", "description": "Team id"},
                        "ownership_type": {"type": "string", "description": "file_owner|codeowner|service_owner", "enum": ["file_owner", "codeowner", "service_owner"]},
                        "confidence_score": {"type": "number", "description": "0..1"}
                    },
                    "required": ["run_id", "owner_id"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        run_id = kwargs.get("run_id")
        owner = {
            "owner_id": kwargs.get("owner_id"),
            "team_id": kwargs.get("team_id"),
            "ownership_type": kwargs.get("ownership_type"),
            "confidence_score": kwargs.get("confidence_score"),
        }
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        meta = run.get("metadata") or {}
        meta["owner"] = owner
        run["metadata"] = meta
        return json.dumps({"run": run}, indent=2)


class UpdateTestRunCoverage(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "update_test_run_coverage",
                "description": "Updates the coverage percentage of a test run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_run_id": {"type": "string", "description": "Test run id"},
                        "coverage_pct": {"type": "number", "description": "Coverage percentage 0..100"}
                    },
                    "required": ["test_run_id", "coverage_pct"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        test_run_id = kwargs.get("test_run_id")
        coverage_pct = kwargs.get("coverage_pct")
        test_runs = data.get("test_runs", [])
        row = next((t for t in test_runs if t.get("id") == test_run_id), None)
        if not row:
            return json.dumps({"error": "test_run_not_found", "test_run_id": test_run_id})
        if "stats" in row and isinstance(row["stats"], dict):
            row["stats"]["coverage_pct"] = coverage_pct
        row["coverage_pct"] = coverage_pct
        return json.dumps({"test_run": row}, indent=2)


TOOLS = [
    GetBuildRunDetails(),
    ListFailedBuildRunsByBranch(),
    StartAutomationRun(),
    CompleteAutomationRun(),
    AttachSymbolicatedStackToRun(),
    MapPathToOwner(),
    SetBuildTriageStatus(),
    RecordReproCommandForRun(),
    SetFixProposalOnRun(),
    ListFailedTestsForRun(),
    CreateAssetQaResult(),
    PromoteAssetAutofixToPass(),
    UpdateAssetCatalogPerformanceRating(),
    UpdateArtifactMetadata(),
    CreateTestRunSummary(),
    AddTestResultToRun(),
    SetBuildFailureCategorization(),
    SetFirstBadCommitOnRun(),
    SetBisectResultOnRun(),
    AppendSimilarIncidentToRun(),
    UpdateRunMetadata(),
    AddRunStep(),
    UpdateRunStepStatus(),
    LinkArtifactToRun(),
    RegisterSymbol(),
    DeprecateSymbol(),
    RegisterAssetInCatalog(),
    DeprecateAssetInCatalog(),
    PersistOwnerToRun(),
    UpdateTestRunCoverage(),
]
