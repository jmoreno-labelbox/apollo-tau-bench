import json
from typing import Any

from tau_bench.envs.tool import Tool

#---------- Helpers for Determinism ----------
FIXED_NOW = "2025-01-27T12:30:00Z"
DEFAULT_AUTOMATION_DURATION_MS = 5 * 60 * 1000  #5 minutes
ID_PREFIX = "AUTO"




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def _find_by_id(rows: list[dict[str, Any]], _id: str) -> dict[str, Any] | None:
    pass
    idx = _idx_by_id(rows, _id)
    return rows[idx] if idx is not None else None


def _sanitize(s: str) -> str:
    pass
    return s.replace("/", "_").replace(".", "_").replace(":", "_").replace(" ", "_")


def _idx_by_id(rows: list[dict[str, Any]], _id: str) -> int | None:
    pass
    for i, r in enumerate(rows):
        if r.get("id") == _id:
            return i
    return None


#---------- Available Tools ----------


class GetBuildRunDetails(Tool):
    """Retrieve complete information for a build run using its identifier."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None) -> str:
        runs = data.get("build_runs", {}).values()
        run = _find_by_id(runs, run_id)
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBuildRunDetails",
                "description": "Fetch a single build run by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"run_id": {"type": "string"}},
                    "required": ["run_id"],
                },
            },
        }


class ListFailedBuildRunsByBranch(Tool):
    """Enumerate unsuccessful build runs for a specified branch."""

    @staticmethod
    def invoke(data: dict[str, Any], branch: str = None) -> str:
        runs = data.get("build_runs", {}).values()
        failed = [
            r for r in runs.values() if r.get("branch") == branch and r.get("status") == "failed"
        ]
        payload = {"count": len(failed), "runs": failed}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListFailedBuildRunsByBranch",
                "description": "List failed build runs for a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {"branch": {"type": "string"}},
                    "required": ["branch"],
                },
            },
        }


class StartAutomationRun(Tool):
    """Initiate an automated run (build triage, asset_qa, testing)."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        automation_type: str = None, 
        input_ref: str = None, 
        automation_run_id: str = None
    ) -> str:
        pass
        # build_triage, asset_qa, testing
        run = {
            "id": automation_run_id,
            "automation_type": automation_type,
            "input_ref": input_ref,
            "status": "running",
            "started_at": FIXED_NOW,
            "ended_at": None,
            "duration_ms": 0,
            "outputs_json": {},
            "errors_json": None,
        }
        data.setdefault("automation_runs", []).append(run)
        payload = {"automation_run": run}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StartAutomationRun",
                "description": "Create a deterministic 'running' automation run record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "automation_type": {
                            "type": "string",
                            "enum": ["build_triage", "asset_qa", "testing"],
                        },
                        "input_ref": {"type": "string"},
                        "automation_run_id": {"type": "string"},
                    },
                    "required": ["automation_type", "input_ref", "automation_run_id"],
                },
            },
        }


class CompleteAutomationRun(Tool):
    """Finish an earlier initiated automation run with a fixed duration."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        automation_run_id: str = None,
        status: str = None,
        outputs_json: dict = {}
    ) -> str:
        runs = data.get("automation_runs", {}).values()
        idx = _idx_by_id(runs, automation_run_id)
        if idx is None:
            runs.append(
                {
                    "id": automation_run_id,
                    "automation_type": "build_triage",
                    "input_ref": "",
                    "status": "running",
                    "started_at": FIXED_NOW,
                    "ended_at": None,
                    "duration_ms": 0,
                    "outputs_json": {},
                    "errors_json": None,
                }
            )
            idx = len(runs) - 1

        run = runs[idx]
        if run["started_at"] == "2025-01-27T12:30:00Z":
            ended_at = "2025-01-27T12:35:00Z"
            duration_ms = DEFAULT_AUTOMATION_DURATION_MS
        else:
            ended_at = "2025-01-27T12:35:00Z"
            duration_ms = DEFAULT_AUTOMATION_DURATION_MS

        run.update(
            {
                "status": status,
                "ended_at": ended_at,
                "duration_ms": duration_ms,
                "outputs_json": outputs_json,
            }
        )
        runs[idx] = run
        payload = {"automation_run": run}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CompleteAutomationRun",
                "description": "Mark automation run as completed/failed and compute deterministic duration.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "automation_run_id": {"type": "string"},
                        "status": {
                            "type": "string",
                            "enum": ["completed", "failed", "cancelled"],
                        },
                        "outputs_json": {"type": "object"},
                    },
                    "required": ["automation_run_id", "status"],
                },
            },
        }


class AttachSymbolicatedStackToRun(Tool):
    """Link a symbolicated stack trace URI to a build run by selecting a corresponding symbol record."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None, build_id: str = None, module_name: str = None, platform: str = None) -> str:
        symbols = data.get("symbols", {}).values()
        chosen = None
        for s in symbols.values():
            if (
                s.get("build_id") == build_id
                and s.get("module_name") == module_name
                and s.get("platform") == platform
            ):
                chosen = s
                break

        runs = data.get("build_runs", {}).values()
        idx = _idx_by_id(runs, run_id)
        updated_run = None
        if idx is not None and chosen is not None:
            run = runs[idx]
            run["symbolicated_stack_uri"] = chosen.get("sym_uri")
            runs[idx] = run
            updated_run = run
        payload = {"chosen_symbol": chosen, "updated_run": updated_run}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AttachSymbolicatedStackToRun",
                "description": "Attach symbolicated stack URI on a run by matching symbol metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "build_id": {"type": "string"},
                        "module_name": {"type": "string"},
                        "platform": {"type": "string"},
                    },
                    "required": ["run_id", "build_id", "module_name", "platform"],
                },
            },
        }


class MapPathToOwner(Tool):
    """Associate a code/asset path with its owner utilizing ownership_map."""

    @staticmethod
    def invoke(data: dict[str, Any], file_path: str = None) -> str:
        maps = data.get("ownership_map", {}).values()
        rec = next((m for m in maps.values() if m.get("file_path") == file_path), None)
        payload = {"owner_map": rec}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MapPathToOwner",
                "description": "Look up an ownership record by exact file_path.",
                "parameters": {
                    "type": "object",
                    "properties": {"file_path": {"type": "string"}},
                    "required": ["file_path"],
                },
            },
        }


class SetBuildTriageStatus(Tool):
    """Assign triage_status to a run, with the option to save a triage owner in the metadata."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None, triage_status: str = None, owner_id: str = None) -> str:
        runs = data.get("build_runs", {}).values()
        idx = _idx_by_id(runs, run_id)
        updated = None
        if idx is not None:
            run = runs[idx]
            run["triage_status"] = triage_status
            if owner_id:
                run.setdefault("metadata", {}).values()
                run["metadata"]["triage_owner_id"] = owner_id
            runs[idx] = run
            updated = run
        payload = {"run": updated}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetBuildTriageStatus",
                "description": "Update triage_status for a run and optionally set metadata.triage_owner_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "triage_status": {
                            "type": "string",
                            "enum": ["in_progress", "manual_review"],
                        },
                        "owner_id": {"type": "string"},
                    },
                    "required": ["run_id", "triage_status"],
                },
            },
        }


class RecordReproCommandForRun(Tool):
    """Log a reproduction command for a run."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None, command: str = None) -> str:
        runs = data.get("build_runs", {}).values()
        idx = _idx_by_id(runs, run_id)
        updated = None
        if idx is not None:
            run = runs[idx]
            run["repro_command"] = command
            runs[idx] = run
            updated = run
        payload = {"run": updated}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordReproCommandForRun",
                "description": "Persist a deterministic repro command for a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "command": {"type": "string"},
                    },
                    "required": ["run_id", "command"],
                },
            },
        }


class SetFixProposalOnRun(Tool):
    """Assign fix_proposal_id to a run."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None, fix_proposal_id: str = None) -> str:
        runs = data.get("build_runs", {}).values()
        idx = _idx_by_id(runs, run_id)
        updated = None
        if idx is not None:
            run = runs[idx]
            run["fix_proposal_id"] = fix_proposal_id
            runs[idx] = run
            updated = run
        payload = {"run": updated}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetFixProposalOnRun",
                "description": "Attach fix proposal reference to a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "fix_proposal_id": {"type": "string"},
                    },
                    "required": ["run_id", "fix_proposal_id"],
                },
            },
        }


class ListFailedTestsForRun(Tool):
    """Display failed test results for a specified test_run_id."""

    @staticmethod
    def invoke(data: dict[str, Any], test_run_id: str = None) -> str:
        results = data.get("test_results", {}).values()
        failed = [
            r
            for r in results.values() if r.get("test_run_id") == test_run_id and r.get("status") == "failed"
        ]
        payload = {"count": len(failed), "failed_results": failed}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListFailedTestsForRun",
                "description": "List failed test results for a specific test_run.",
                "parameters": {
                    "type": "object",
                    "properties": {"test_run_id": {"type": "string"}},
                    "required": ["test_run_id"],
                },
            },
        }


class CreateAssetQaResult(Tool):
    """Generate a QA result entry for an asset in a deterministic manner."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        asset_path: str = None,
        asset_type: str = None,
        validation_status: str = None,
        severity_max: str = None,
        autofix_applied: bool = False,
        preview_uri: str = None,
        report_uri: str = None,
        validation_results: dict = {}
    ) -> str:
        if (
            asset_path == "assets/textures/environment/castle_tower_diffuse.png"
            and asset_type == "texture"
        ):
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
            "metadata": {},
        }
        data.setdefault("asset_qa_results", []).append(rec)
        payload = {"asset_qa_result": rec}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAssetQaResult",
                "description": "Create an asset QA result.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string"},
                        "asset_type": {"type": "string"},
                        "validation_status": {
                            "type": "string",
                            "enum": ["passed", "failed", "warning"],
                        },
                        "severity_max": {"type": "string"},
                        "preview_uri": {"type": "string"},
                        "report_uri": {"type": "string"},
                        "autofix_applied": {"type": "boolean"},
                        "validation_results": {"type": "object"},
                    },
                    "required": [
                        "asset_path",
                        "asset_type",
                        "validation_status",
                        "severity_max",
                    ],
                },
            },
        }


class PromoteAssetAutofixToPass(Tool):
    """Upgrade an autofixed QA record to 'passed' in a deterministic way."""

    @staticmethod
    def invoke(data: dict[str, Any], qa_id: str = None) -> str:
        results = data.get("asset_qa_results", {}).values()
        idx = _idx_by_id(results, qa_id)
        if idx is None:
            payload = {"asset_qa_result": None}
            out = json.dumps(payload, indent=2)
            return out
        rec = results[idx]
        if rec.get("autofix_applied"):
            rec["validation_status"] = "passed"
        results[idx] = rec
        payload = {"asset_qa_result": rec}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PromoteAssetAutofixToPass",
                "description": "If autofix_applied is true, set validation_status='passed'.",
                "parameters": {
                    "type": "object",
                    "properties": {"qa_id": {"type": "string"}},
                    "required": ["qa_id"],
                },
            },
        }


class UpdateAssetCatalogPerformanceRating(Tool):
    """Revise performance_rating for an asset within the asset_catalog."""

    @staticmethod
    def invoke(data: dict[str, Any], asset_path: str = None, performance_rating: str = None) -> str:
        rows = data.get("asset_catalog", {}).values()
        idx = next(
            (i for i, r in enumerate(rows) if r.get("asset_path") == asset_path), None
        )
        if idx is None:
            payload = {"asset_catalog": None}
            out = json.dumps(payload, indent=2)
            return out
        row = rows[idx]
        row["performance_rating"] = performance_rating
        row["validation_status"] = row.get("validation_status", "failed")
        row["updated_at"] = "2025-01-27T13:35:00Z"
        row["validation_date"] = "2025-01-27T13:35:00Z"
        rows[idx] = row
        payload = {"asset_catalog": row}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAssetCatalogPerformanceRating",
                "description": "Set performance_rating for the given asset_path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string"},
                        "performance_rating": {
                            "type": "string",
                            "enum": ["low", "medium", "high"],
                        },
                    },
                    "required": ["asset_path", "performance_rating"],
                },
            },
        }


class UpdateArtifactMetadata(Tool):
    """Modify artifact.metadata with specified keys in a deterministic manner."""

    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None, metadata_patch: dict[str, Any] = {}) -> str:
        rows = data.get("artifacts", {}).values()
        idx = _idx_by_id(rows, artifact_id)
        if idx is None:
            payload = {"artifact": None}
            out = json.dumps(payload, indent=2)
            return out
        art = rows[idx]
        art.setdefault("metadata", {}).values()
        art["metadata"].update(metadata_patch)
        rows[idx] = art
        payload = {"artifact": art}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateArtifactMetadata",
                "description": "Apply a shallow patch to artifact.metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "metadata_patch": {"type": "object"},
                    },
                    "required": ["artifact_id", "metadata_patch"],
                },
            },
        }


class CreateTestRunSummary(Tool):
    """Generate a summary of a test run with a fixed identifier."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        pipeline_id: str = None,
        total: int = None,
        failed: int = None,
        passed: int = None,
        coverage_pct: float = None,
        report_uri: str = None,
        skipped: int = 0
    ) -> str:
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
            "created_at": FIXED_NOW,
        }
        data.setdefault("test_runs", []).append(row)
        payload = {"test_run": row}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTestRunSummary",
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
                        "report_uri": {"type": "string"},
                    },
                    "required": ["pipeline_id", "total", "failed", "passed"],
                },
            },
        }


class AddTestResultToRun(Tool):
    """Add a test result to a test run in a deterministic manner."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        test_run_id: str = None,
        test_name: str = None,
        status: str = None,
        failure_type: str = None,
        issue_message: str = None,
        file_path: str = None,
        line_number: int = None,
        issue_code: str = None,
        duration_ms: int = None
    ) -> str:
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
            "metadata": {},
        }
        data.setdefault("test_results", []).append(rec)
        payload = {"test_result": rec}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddTestResultToRun",
                "description": "Append a test result.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_run_id": {"type": "string"},
                        "test_name": {"type": "string"},
                        "status": {
                            "type": "string",
                            "enum": ["passed", "failed", "skipped"],
                        },
                        "failure_type": {"type": "string"},
                        "issue_message": {"type": "string"},
                        "file_path": {"type": "string"},
                        "line_number": {"type": "integer"},
                        "issue_code": {"type": "string"},
                        "duration_ms": {"type": "integer"},
                    },
                    "required": ["test_run_id", "test_name", "status"],
                },
            },
        }


class SetBuildFailureCategorization(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SetBuildFailureCategorization",
                "description": "Sets failure categorization for a build run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "category": {
                            "type": "string",
                            "description": "Top-level category",
                        },
                        "subcategory": {
                            "type": "string",
                            "description": "Optional subcategory",
                        },
                    },
                    "required": ["run_id", "category"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, category=None, subcategory=None):
        runs = data.get("build_runs", {}).values()
        run = next((r for r in runs.values() if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        meta = run.get("metadata") or {}
        fc = meta.get("failure_category") or {}
        fc["category"] = category
        if subcategory is not None:
            fc["subcategory"] = subcategory
        meta["failure_category"] = fc
        run["metadata"] = meta
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
class SetFirstBadCommitOnRun(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SetFirstBadCommitOnRun",
                "description": "Annotates a run with a first-bad commit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "commit_sha": {
                            "type": "string",
                            "description": "First bad commit sha",
                        },
                    },
                    "required": ["run_id", "commit_sha"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, commit_sha=None):
        pass
        runs = data.get("build_runs", {}).values()
        run = next((r for r in runs.values() if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        meta = run.get("metadata") or {}
        meta["first_bad_commit"] = commit_sha
        run["metadata"] = meta
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
class SetBisectResultOnRun(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SetBisectResultOnRun",
                "description": "Stores a bisect result on a run's metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "first_bad_commit_sha": {
                            "type": "string",
                            "description": "First bad commit sha",
                        },
                        "last_good_commit_sha": {
                            "type": "string",
                            "description": "Last good commit sha",
                        },
                        "confidence": {
                            "type": "number",
                            "description": "Confidence score between 0 and 1",
                        },
                    },
                    "required": [
                        "run_id",
                        "first_bad_commit_sha",
                        "last_good_commit_sha",
                    ],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, first_bad_commit_sha=None, last_good_commit_sha=None, confidence=None, bisect_result=None):
        # Support bisect_result as an alternative parameter
        if bisect_result is not None:
            if isinstance(bisect_result, dict):
                first_bad_commit_sha = bisect_result.get('first_bad_commit_sha', first_bad_commit_sha)
                last_good_commit_sha = bisect_result.get('last_good_commit_sha', last_good_commit_sha)
        run = next((r for r in data.get("build_runs", {}).values() if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        meta = run.get("metadata") or {}
        meta["bisect"] = {
            "first_bad_commit_sha": first_bad_commit_sha,
            "last_good_commit_sha": last_good_commit_sha,
            "confidence": confidence,
        }
        run["metadata"] = meta
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
class AppendSimilarIncidentToRun(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "AppendSimilarIncidentToRun",
                "description": "Appends a similar incident reference to a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {
                            "type": "string",
                            "description": "Current build run id",
                        },
                        "incident_run_id": {
                            "type": "string",
                            "description": "Related incident run id",
                        },
                        "similarity_score": {
                            "type": "number",
                            "description": "Similarity score 0..1",
                        },
                    },
                    "required": ["run_id", "incident_run_id"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, incident_run_id=None, similarity_score=None):
        runs = data.get("build_runs", {}).values()
        run = next((r for r in runs.values() if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        meta = run.get("metadata") or {}
        arr = meta.get("similar_incidents") or []
        arr.append({"incident_run_id": incident_run_id, "similarity_score": similarity_score})
        meta["similar_incidents"] = arr
        run["metadata"] = meta
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
class UpdateRunMetadata(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateRunMetadata",
                "description": "Patches a run's metadata object by merging the provided fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "metadata_patch": {
                            "type": "object",
                            "description": "Partial metadata patch",
                        },
                    },
                    "required": ["run_id", "metadata_patch"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, metadata_patch=None):
        run_id = run_id
        patch = metadata_patch or {}
        runs = data.get("build_runs", {}).values()
        run = next((r for r in runs.values() if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        meta = run.get("metadata") or {}
        meta.update(patch)
        run["metadata"] = meta
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
class AddRunStep(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddRunStep",
                "description": "Adds a step entry to a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "step_id": {"type": "string", "description": "Unique step id"},
                        "name": {
                            "type": "string",
                            "description": "Human readable step name",
                        },
                        "status": {
                            "type": "string",
                            "description": "pending|running|completed|failed",
                            "enum": ["pending", "running", "completed", "failed"],
                        },
                        "started_at": {
                            "type": "string",
                            "description": "ISO8601 start time",
                        },
                        "ended_at": {
                            "type": "string",
                            "description": "ISO8601 end time",
                        },
                    },
                    "required": ["run_id", "step_id", "name", "status"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, step_id=None, name=None, status=None, started_at=None, ended_at=None):
        step = {
            "id": step_id,
            "name": name,
            "status": status,
            "started_at": started_at,
            "ended_at": ended_at,
        }
        runs = data.get("build_runs", {}).values()
        run = next((r for r in runs.values() if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        steps = run.get("steps") or []
        steps.append(step)
        run["steps"] = steps
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
class UpdateRunStepStatus(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateRunStepStatus",
                "description": "Updates the status or fields of an existing run step.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "step_id": {
                            "type": "string",
                            "description": "Step id to update",
                        },
                        "status": {"type": "string", "description": "New status"},
                        "exit_code": {
                            "type": "integer",
                            "description": "Optional exit code",
                        },
                        "duration_ms": {
                            "type": "integer",
                            "description": "Optional duration",
                        },
                        "log_uri": {
                            "type": "string",
                            "description": "Optional log location",
                        },
                    },
                    "required": ["run_id", "step_id"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, step_id=None, status=None, exit_code=None, duration_ms=None, log_uri=None):
        run_id = run_id
        step_id = step_id
        runs = data.get("build_runs", {}).values()
        run = next((r for r in runs.values() if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        steps = run.get("steps") or []
        step = next((s for s in steps if s.get("id") == step_id), None)
        if not step:
            payload = {"error": "step_not_found", "run_id": run_id, "step_id": step_id}
            out = json.dumps(payload)
            return out
        for k, v in [("status", status), ("exit_code", exit_code), ("duration_ms", duration_ms), ("log_uri", log_uri)]:
            if v is not None:
                step[k] = v
        run["steps"] = steps
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
class LinkArtifactToRun(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "LinkArtifactToRun",
                "description": "Sets the artifacts_uri on a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "artifacts_uri": {
                            "type": "string",
                            "description": "Artifacts URI",
                        },
                    },
                    "required": ["run_id", "artifacts_uri"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, artifacts_uri=None, artifact_id=None):
        # Support artifact_id as an alternative to artifacts_uri
        if artifact_id is not None:
            artifacts_uri = artifact_id
        runs = data.get("build_runs", {}).values()
        run = next((r for r in runs.values() if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        run["artifacts_uri"] = artifacts_uri
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
class RegisterSymbol(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "RegisterSymbol",
                "description": "Registers a symbol record for a build module.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "build_id": {"type": "string", "description": "Build id"},
                        "module_name": {"type": "string", "description": "Module name"},
                        "platform": {"type": "string", "description": "Platform name"},
                        "pdb_uri": {"type": "string", "description": "PDB/Symbol uri"},
                        "status": {
                            "type": "string",
                            "description": "available|deprecated",
                            "enum": ["available", "deprecated"],
                        },
                    },
                    "required": [
                        "build_id",
                        "module_name",
                        "platform",
                        "pdb_uri",
                        "status",
                    ],
                },
            },
        }

    @staticmethod
    def invoke(data, build_id=None, module_name=None, platform=None, pdb_uri=None, status=None):
        symbols = data.get("symbols", {}).values()
        sym_id = f"AUTO::symbol::{build_id}::{module_name}"
        existing = next((s for s in symbols.values() if s.get("id") == sym_id), None)
        if existing:
            existing.update(
                {
                    "build_id": build_id,
                    "module_name": module_name,
                    "platform": platform,
                    "pdb_uri": pdb_uri,
                    "status": status,
                }
            )
        else:
            symbols.append(
                {
                    "id": sym_id,
                    "build_id": build_id,
                    "module_name": module_name,
                    "platform": platform,
                    "pdb_uri": pdb_uri,
                    "status": status,
                }
            )
        data["symbols"] = symbols
        payload = {"symbol": next(s for s in symbols.values() if s.get("id") == sym_id)}
        out = json.dumps(
            payload, indent=2
        )
        return out
class DeprecateSymbol(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "DeprecateSymbol",
                "description": "Marks a symbol record as deprecated.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbol_id": {"type": "string", "description": "Symbol id"}
                    },
                    "required": ["symbol_id"],
                },
            },
        }

    @staticmethod
    def invoke(data, symbol_id=None):
        pass
        symbols = data.get("symbols", {}).values()
        sym = next((s for s in symbols.values() if s.get("id") == symbol_id), None)
        if not sym:
            payload = {"error": "symbol_not_found", "symbol_id": symbol_id}
            out = json.dumps(payload)
            return out
        sym["status"] = "deprecated"
        payload = {"symbol": sym}
        out = json.dumps(payload, indent=2)
        return out
class RegisterAssetInCatalog(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "RegisterAssetInCatalog",
                "description": "Registers or updates an asset in the catalog.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string", "description": "Asset path"},
                        "asset_type": {"type": "string", "description": "Asset type"},
                        "validation_status": {
                            "type": "string",
                            "description": "Validation status",
                        },
                        "performance_rating": {
                            "type": "string",
                            "description": "Performance rating",
                        },
                    },
                    "required": ["asset_path", "asset_type", "validation_status"],
                },
            },
        }

    @staticmethod
    def invoke(data, asset_path=None, asset_type=None, validation_status=None, performance_rating=None, asset_name=None):
        # Support asset_name as an alternative to asset_path
        if asset_name is not None:
            asset_path = asset_name
        catalog = data.get("asset_catalog", {}).values()
        row = next((a for a in catalog.values() if a.get("asset_path") == asset_path), None)
        if row:
            row["asset_type"] = asset_type
            row["validation_status"] = validation_status
            if performance_rating is not None:
                row["performance_rating"] = performance_rating
        else:
            catalog.append(
                {
                    "asset_path": asset_path,
                    "asset_type": asset_type,
                    "validation_status": validation_status,
                    "performance_rating": performance_rating,
                }
            )
        data["asset_catalog"] = catalog
        payload = {"asset": next(a for a in catalog.values() if a.get("asset_path") == asset_path)}
        out = json.dumps(
            payload, indent=2,
        )
        return out
class DeprecateAssetInCatalog(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "deprecateAssetInCatalog",
                "description": "Marks an asset in the catalog as deprecated.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string", "description": "Asset path"}
                    },
                    "required": ["asset_path"],
                },
            },
        }

    @staticmethod
    def invoke(data, asset_path=None):
        pass
        catalog = data.get("asset_catalog", {}).values()
        row = next((a for a in catalog.values() if a.get("asset_path") == asset_path), None)
        if not row:
            payload = {"error": "asset_not_found", "asset_path": asset_path}
            out = json.dumps(payload)
            return out
        row["validation_status"] = "deprecated"
        payload = {"asset": row}
        out = json.dumps(payload, indent=2)
        return out
class PersistOwnerToRun(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "PersistOwnerToRun",
                "description": "Persists a resolved ownership mapping into the run metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "owner_id": {"type": "string", "description": "Owner user id"},
                        "team_id": {"type": "string", "description": "Team id"},
                        "ownership_type": {
                            "type": "string",
                            "description": "file_owner|codeowner|service_owner",
                            "enum": ["file_owner", "codeowner", "service_owner"],
                        },
                        "confidence_score": {"type": "number", "description": "0..1"},
                    },
                    "required": ["run_id", "owner_id"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, owner_id=None, team_id=None, ownership_type=None, confidence_score=None, owner_path=None):
        # Support owner_path as an alternative to owner_id
        if owner_path is not None:
            owner_id = owner_path
        owner = {
            "owner_id": owner_id,
            "team_id": team_id,
            "ownership_type": ownership_type,
            "confidence_score": confidence_score,
        }
        runs = data.get("build_runs", {}).values()
        run = next((r for r in runs.values() if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        meta = run.get("metadata") or {}
        meta["owner"] = owner
        run["metadata"] = meta
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
class UpdateTestRunCoverage(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateTestRunCoverage",
                "description": "Updates the coverage percentage of a test run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_run_id": {"type": "string", "description": "Test run id"},
                        "coverage_pct": {
                            "type": "number",
                            "description": "Coverage percentage 0..100",
                        },
                    },
                    "required": ["test_run_id", "coverage_pct"],
                },
            },
        }

    @staticmethod
    def invoke(data, test_run_id=None, coverage_pct=None):
        test_runs = data.get("test_runs", {}).values()
        row = next((t for t in test_runs.values() if t.get("id") == test_run_id), None)
        if not row:
            payload = {"error": "test_run_not_found", "test_run_id": test_run_id}
            out = json.dumps(payload)
            return out
        if "stats" in row and isinstance(row["stats"], dict):
            row["stats"]["coverage_pct"] = coverage_pct
        row["coverage_pct"] = coverage_pct
        payload = {"test_run": row}
        out = json.dumps(payload, indent=2)
        return out
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