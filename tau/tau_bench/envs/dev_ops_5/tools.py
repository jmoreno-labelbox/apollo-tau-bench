import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


class GetBuildRunById(Tool):
    """Fetches a particular build run using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        build_run_id = id
        build_runs = data.get("build_runs", {}).values()
        for run in build_runs.values():
            if run.get("id") == build_run_id:
                payload = run
                out = json.dumps(payload)
                return out
        payload = {"error": f"Build run with ID '{build_run_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBuildRunById",
                "description": "Retrieves a specific build run by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "The unique ID of the build run.",
                        }
                    },
                    "required": ["id"],
                },
            },
        }


class GetBisectResultForBuildRun(Tool):
    """Obtains the bisect result for a designated build run ID."""

    @staticmethod
    def invoke(data: dict[str, Any], build_run_id: str = None) -> str:
        bisect_results = data.get("bisect_results", {}).values()
        for result in bisect_results.values():
            if result.get("build_run_id") == build_run_id:
                payload = result
                out = json.dumps(payload)
                return out
        payload = {"error": f"Bisect result for build run ID '{build_run_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBisectResultForBuildRun",
                "description": "Retrieves the bisect result for a specific build run ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "build_run_id": {
                            "type": "string",
                            "description": "The unique ID of the build run.",
                        }
                    },
                    "required": ["build_run_id"],
                },
            },
        }


class UpdateBuildRunTriageStatus(Tool):
    """Modifies the triage status of a build run."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: Any = None,
        new_status: str = None,
        run_id: str = None,
        triage_status: str = None
    ) -> str:
        # Support 'triage_status' as an alternative to 'new_status'
        if triage_status is not None:
            new_status = triage_status
        build_runs = data.get("build_runs", {}).values()
        for run in build_runs.values():
            if run.get("id") == run_id:
                run["triage_status"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Triage status for build run '{run_id}' updated to '{new_status}'.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Build run with ID '{run_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateBuildRunTriageStatus",
                "description": "Updates the triage status of a build run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "triage_status": {"type": "string"},
                    },
                    "required": ["id", "triage_status"],
                },
            },
        }


class FindFileOwner(Tool):
    """Identifies the owner of a file according to the ownership map."""

    @staticmethod
    def invoke(data: dict[str, Any], file_path: str) -> str:
        ownership_map = data.get("ownership_map", {}).values()
        most_specific_owner = None
        longest_match = -1

        for ownership in ownership_map.values():
            owner_path = ownership.get("file_path")
            if file_path.startswith(owner_path):
                if len(owner_path) > longest_match:
                    longest_match = len(owner_path)
                    most_specific_owner = ownership

        if most_specific_owner:
            payload = most_specific_owner
            out = json.dumps(payload)
            return out
        payload = {"info": f"Owner for file path '{file_path}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindFileOwner",
                "description": "Finds the owner of a file based on the ownership map.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "The path to the file.",
                        }
                    },
                    "required": ["file_path"],
                },
            },
        }


class GetUserById(Tool):
    """Fetches a user using their ID."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: Any = None,
        user_id: str = None
    ) -> str:
        users = data.get("users", {}).values()
        for user in users.values():
            if user.get("id") == user_id:
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": f"User with ID '{user_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserById",
                "description": "Retrieves a user by their ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


class GetUserByName(Tool):
    """Obtains a user based on their name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        users = data.get("users", {}).values()
        for user in users.values():
            if user.get("name") == name:
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": f"User with name '{name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserByName",
                "description": "Retrieves a user by their name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class CreateWorkItem(Tool):
    """Generates a new work item such as a bug, task, or incident."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        type: str,
        title: str,
        state: str = "open",
        assignee_id: str = None,
        priority: str = "high",
        points: int = 0,
        description: str = ""
    ) -> str:
        pass
        work_items = data.get("work_items", {}).values()
        new_id_num = max([int(w["id"].split("_")[1]) for w in work_items.values()]) + 1
        new_id = f"work_{new_id_num:03d}"

        new_item = {
            "id": new_id,
            "project_id": project_id,
            "type": type,
            "title": title,
            "state": state,
            "assignee_id": assignee_id,
            "created_at": "2025-01-28T00:00:00Z",  # Temporary timestamp
            "closed_at": None,
            "priority": priority,
            "points": points,
            "metadata": {"description": description},
        }
        data["work_items"][work_item_id] = new_item
        payload = new_item
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateWorkItem",
                "description": "Creates a new work item (bug, task, story, incident).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "type": {
                            "type": "string",
                            "enum": ["bug", "task", "story", "epic", "incident"],
                        },
                        "title": {"type": "string"},
                        "description": {"type": "string"},
                        "assignee_id": {"type": "string"},
                        "priority": {
                            "type": "string",
                            "enum": ["low", "medium", "high", "critical"],
                        },
                        "state": {"type": "string"},
                        "points": {"type": "integer"},
                    },
                    "required": ["project_id", "type", "title"],
                },
            },
        }


class FindBugByCrashFingerprint(Tool):
    """Locates a bug/work item linked to a crash fingerprint."""

    @staticmethod
    def invoke(data: dict[str, Any], crash_fingerprint: str = None) -> str:
        work_items = data.get("work_items", {}).values()
        for item in work_items.values():
            if item.get("metadata", {}).values().get("crash_fingerprint") == crash_fingerprint:
                payload = item
                out = json.dumps(payload)
                return out
        payload = {"info": f"No bug found for crash fingerprint '{crash_fingerprint}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindBugByCrashFingerprint",
                "description": "Finds a bug associated with a crash fingerprint.",
                "parameters": {
                    "type": "object",
                    "properties": {"crash_fingerprint": {"type": "string"}},
                    "required": ["crash_fingerprint"],
                },
            },
        }


class LinkWorkItems(Tool):
    """Connects two work items (e.g., as duplicates or related items)."""

    @staticmethod
    def invoke(data: dict[str, Any], parent_id: str = None, child_id: str = None, link_type: str = None) -> str:
        links = data.get("work_item_links", {}).values()
        max([int(w["parent_id"].split("_")[1]) for w in links]) + 1

        new_link = {
            "parent_id": parent_id,
            "child_id": child_id,
            "link_type": link_type,
        }
        data["work_item_labels"][new_link["work_item_label_id"]] = new_link
        payload = {
            "status": "success",
            "message": f"Linked {child_id} to {parent_id} as {link_type}.",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkWorkItems",
                "description": "Links two work items together.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "parent_id": {"type": "string"},
                        "child_id": {"type": "string"},
                        "link_type": {
                            "type": "string",
                            "enum": [
                                "epic",
                                "dependency",
                                "related",
                                "blocks",
                                "implements",
                                "duplicate",
                            ],
                        },
                    },
                    "required": ["parent_id", "child_id", "link_type"],
                },
            },
        }


class AddCommentToWorkItem(Tool):
    """Inserts a comment into a work item."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None, comment: str = None) -> str:
        work_item_id = id
        work_items = data.get("work_items", {}).values()
        for item in work_items.values():
            if item.get("id", "") == work_item_id:
                break
        else:
            payload = {
                    "status": "error",
                    "message": f"Work item with id '{work_item_id}' not found.",
                }
            out = json.dumps(
                payload)
            return out
        comments = item.get("comments", [])
        comments += [comment]
        item["comments"] = comments
        payload = {
                "status": "success",
                "message": f"Comment '{comment}' added to work item '{work_item_id}'.",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddCommentToWorkItem",
                "description": "Adds a comment to a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "comment": {"type": "string"},
                    },
                    "required": ["id", "comment"],
                },
            },
        }


class UpdateWorkItemState(Tool):
    """Modifies the status of a work item (e.g., 'open', 'closed')."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: Any = None,
        item_id: str = None,
        new_state: str = None
    ) -> str:
        work_items = data.get("work_items", {}).values()
        for item in work_items.values():
            if item.get("id") == item_id:
                item["state"] = new_state
                payload = {
                    "status": "success",
                    "message": f"State of work item '{item_id}' updated to '{new_state}'.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Work item with ID '{item_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateWorkItemState",
                "description": "Updates the state of a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "new_state": {"type": "string"},
                    },
                    "required": ["id", "new_state"],
                },
            },
        }


class GetAssetByPath(Tool):
    """Fetches an asset using its file path."""

    @staticmethod
    def invoke(data: dict[str, Any], asset_path: str = None) -> str:
        path = asset_path
        assets = data.get("asset_catalog", {}).values()
        for asset in assets.values():
            if asset.get("asset_path") == path:
                payload = asset
                out = json.dumps(payload)
                return out
        payload = {"error": f"Asset with path '{path}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAssetByPath",
                "description": "Retrieves an asset by its file path.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_path": {"type": "string"}},
                    "required": ["asset_path"],
                },
            },
        }


class UpdateAssetValidationStatus(Tool):
    """Modifies the validation status of an asset."""

    def invoke(
        data: dict[str, Any],
        asset_id: str = None,
        id: Any = None,
        new_status: str = None
    ) -> str:
        assets = data.get("asset_catalog", {}).values()
        for asset in assets.values():
            if asset.get("id") == asset_id:
                asset["validation_status"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Validation status for asset '{asset_id}' updated to '{new_status}'.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Asset with ID '{asset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateAssetValidationStatus",
                "description": "Updates the validation status of an asset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "validation_status": {"type": "string"},
                    },
                    "required": ["id", "validation_status"],
                },
            },
        }


class GetCrashEventById(Tool):
    """Fetches a crash event using its ID."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        crash_id: str = None,
        id: Any = None
    ) -> str:
        crashes = data.get("crash_events", {}).values()
        for crash in crashes.values():
            if crash.get("id") == crash_id:
                payload = crash
                out = json.dumps(payload)
                return out
        payload = {"error": f"Crash event with ID '{crash_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrashEventById",
                "description": "Retrieves a crash event by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


class UpdateCrashEventStatus(Tool):
    """Modifies the status of a crash event."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        crash_id: str = None,
        id: Any = None,
        new_status: str = None,
        status: str = None
    ) -> str:
        # Support 'status' as an alternative to 'new_status'
        if status is not None:
            new_status = status
        crashes = data.get("crash_events", {}).values()
        for crash in crashes.values():
            if crash.get("id") == crash_id:
                crash["status"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Status for crash '{crash_id}' updated to '{new_status}'.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Crash with ID '{crash_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCrashEventStatus",
                "description": "Updates the status of a crash event.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["id", "status"],
                },
            },
        }


class GetVulnerabilityById(Tool):
    """Fetches a vulnerability using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        vuln_id = id
        vulnerabilities = data.get("vulnerabilities", {}).values()
        for vuln in vulnerabilities.values():
            if vuln.get("id") == vuln_id:
                payload = vuln
                out = json.dumps(payload)
                return out
        payload = {"error": f"Vulnerability with ID '{vuln_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getVulnerabilityById",
                "description": "Retrieves a vulnerability by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


class UpdateVulnerabilityStatus(Tool):
    """Modifies the status of a vulnerability."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: Any = None,
        new_status: str = None,
        vuln_id: str = None,
        status: str = None
    ) -> str:
        # Support 'status' as an alternative to 'new_status'
        if status is not None:
            new_status = status
        vulnerabilities = data.get("vulnerabilities", {}).values()
        for vuln in vulnerabilities.values():
            if vuln.get("id") == vuln_id:
                vuln["status"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Status for vulnerability '{vuln_id}' updated to '{new_status}'.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Vulnerability with ID '{vuln_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateVulnerabilityStatus",
                "description": "Updates the status of a vulnerability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "status": {
                            "type": "string",
                            "description": "The new status (e.g., 'triaged', 'open', 'fixed').",
                        },
                    },
                    "required": ["id", "status"],
                },
            },
        }


class GetTranslationByKeyAndLocale(Tool):
    """Fetches a translation using its string key and locale."""

    @staticmethod
    def invoke(data: dict[str, Any], string_key: str = None, locale: str = None) -> str:
        key = string_key
        locale = locale
        translations = data.get("translations", {}).values()
        for t in translations.values():
            if t.get("string_key") == key and t.get("locale") == locale:
                payload = t
                out = json.dumps(payload)
                return out
        payload = {"error": f"Translation for key '{key}' and locale '{locale}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTranslationByKeyAndLocale",
                "description": "Retrieves a translation by its string key and locale.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "string_key": {"type": "string"},
                        "locale": {"type": "string"},
                    },
                    "required": ["string_key", "locale"],
                },
            },
        }


class UpdateTranslation(Tool):
    """Modifies the target string of a translation."""

    def invoke(
        data: dict[str, Any],
        id: Any = None,
        new_string: str = None,
        translation_id: str = None
    ) -> str:
        translations = data.get("translations", {}).values()
        for t in translations.values():
            if t.get("id") == translation_id:
                t["target_string"] = new_string
                payload = {
                    "status": "success",
                    "message": f"Translation '{translation_id}' updated.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Translation with ID '{translation_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateTranslation",
                "description": "Updates the target string of a translation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "target_string": {"type": "string"},
                    },
                    "required": ["id", "target_string"],
                },
            },
        }


class UpdateTranslationValidationStatus(Tool):
    """Modifies the validation status of a translation."""

    def invoke(
        data: dict[str, Any],
        id: Any = None,
        new_status: str = None,
        translation_id: str = None
    ) -> str:
        translations = data.get("translations", {}).values()
        for t in translations.values():
            if t.get("id") == translation_id:
                t["validation_status"] = new_status
                if new_status == "passed":
                    t["validation_issue"] = []
                payload = {
                    "status": "success",
                    "message": f"Validation status for translation '{translation_id}' updated.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Translation with ID '{translation_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateTranslationValidationStatus",
                "description": "Updates the validation status of a translation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "validation_status": {"type": "string"},
                    },
                    "required": ["id", "validation_status"],
                },
            },
        }


class AddRevisionHistoryEntry(Tool):
    """Inserts an entry into the revision history of a translation."""

    @staticmethod
    def invoke(data: dict[str, Any], translation_id: str = None, version: str = None, translation: str = None, translator: str = None, notes: str = None) -> str:
        translations = data.get("translations", {}).values()
        for t in translations.values():
            if t.get("id") == translation_id:
                new_entry = {
                    "version": version,
                    "translation": translation,
                    "timestamp": "2025-01-28T00:00:00Z",
                    "translator": translator,
                    "notes": notes,
                }
                t["revision_history"].append(new_entry)
                payload = {"status": "success", "message": "Revision history updated."}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Translation with ID '{translation_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addRevisionHistoryEntry",
                "description": "Adds an entry to the revision history of a translation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "translation_id": {"type": "string"},
                        "version": {"type": "integer"},
                        "translation": {"type": "string"},
                        "translator": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": [
                        "translation_id",
                        "version",
                        "translation",
                        "translator",
                        "notes",
                    ],
                },
            },
        }


class CreateFixProposal(Tool):
    """Generates a fix proposal for a build run."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        build_run_id: str = None,
        bisect_result_id: str = None,
        repo: str = None,
        branch: str = None,
        fix_type: str = None,
        title: str = None,
        description: str = None
    ) -> str:
        fix_proposals = data.get("fix_proposals", {}).values()
        new_id_num = (
            max([int(p["id"].split("_")[1]) for p in fix_proposals], default=0) + 1
        )
        new_id = f"fix_{new_id_num:03d}"

        new_proposal = {
            "id": new_id,
            "build_run_id": build_run_id,
            "bisect_result_id": bisect_result_id,
            "repo": repo,
            "branch": branch,
            "created_at": "2025-01-28T00:00:00Z",
            "status": "draft",
            "fix_type": fix_type,
            "title": title,
            "description": description,
        }
        data["fix_proposals"][new_proposal["fix_proposal_id"]] = new_proposal
        payload = new_proposal
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFixProposal",
                "description": "Creates a fix proposal for a build run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "build_run_id": {"type": "string"},
                        "bisect_result_id": {"type": "string"},
                        "repo": {"type": "string"},
                        "branch": {"type": "string"},
                        "fix_type": {"type": "string"},
                        "title": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "required": [
                        "build_run_id",
                        "bisect_result_id",
                        "repo",
                        "branch",
                        "fix_type",
                        "title",
                        "description",
                    ],
                },
            },
        }


class GetDeploymentById(Tool):
    """Fetches a deployment using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        deployment_id = id
        deployments = data.get("deployments", {}).values()
        for d in deployments.values():
            if d.get("id") == deployment_id:
                payload = d
                out = json.dumps(payload)
                return out
        payload = {"error": f"Deployment with ID '{deployment_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDeploymentById",
                "description": "Retrieves a deployment by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


class GetRollbackByDeploymentId(Tool):
    """Obtains rollback information for a failed deployment ID."""

    @staticmethod
    def invoke(data: dict[str, Any], deployment_id: str = None) -> str:
        rollbacks = data.get("rollbacks", {}).values()
        for r in rollbacks.values():
            if r.get("deployment_id") == deployment_id:
                payload = r
                out = json.dumps(payload)
                return out
        payload = {"error": f"Rollback for deployment ID '{deployment_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRollbackByDeploymentId",
                "description": "Retrieves rollback details for a failed deployment ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"deployment_id": {"type": "string"}},
                    "required": ["deployment_id"],
                },
            },
        }


class CreateDeployment(Tool):
    """Generates a new deployment entry."""

    @staticmethod
    def invoke(data: dict[str, Any], pipeline_id: str = None, environment_id: str = None, 
               deployed_by: str = None, version: str = None, status: str = None) -> str:
        deployments = data.get("deployments", {}).values()
        new_id_num = max([int(d["id"].split("_")[1]) for d in deployments.values()]) + 1
        new_id = f"deploy_{new_id_num:03d}"

        new_deployment = {
            "id": new_id,
            "pipeline_id": pipeline_id,
            "environment_id": environment_id,
            "deployed_by": deployed_by,
            "version": version,
            "status": status,
            "deployed_at": "2025-01-28T00:00:00Z",
            "duration_minutes": 0,
        }
        data["deployments"][deployment_id] = new_deployment
        payload = new_deployment
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDeployment",
                "description": "Creates a new deployment record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pipeline_id": {"type": "string"},
                        "environment_id": {"type": "string"},
                        "deployed_by": {"type": "string"},
                        "version": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": [
                        "pipeline_id",
                        "environment_id",
                        "deployed_by",
                        "version",
                        "status",
                    ],
                },
            },
        }


class GetTeamByName(Tool):
    """Fetches a team using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        teams = data.get("teams", {}).values()
        for team in teams.values():
            if team.get("name") == name:
                payload = team
                out = json.dumps(payload)
                return out
        payload = {"error": f"Team with name '{name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamByName",
                "description": "Retrieves a team by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class GetTeamLead(Tool):
    """Obtains the lead engineer/lead operations for a particular team."""

    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None) -> str:
        teams = data.get("teams", {}).values()
        for team in teams.values():
            if team.get("id") == team_id:
                lead_id = (
                    team.get("lead_engineer")
                    or team.get("lead_ops")
                    or team.get("lead_security")
                    or team.get("lead_analytics")
                    or team.get("lead_server_ops")
                )
                if lead_id:
                    payload = {"lead_id": lead_id}
                    out = json.dumps(payload)
                    return out

        teams = data.get("team_members", {}).values()
        for team in teams.values():
            if team.get("team_id") == team_id:
                if team.get("role") == "team_lead":
                    payload = {"lead_id": team.get("user_id")}
                    out = json.dumps(payload)
                    return out
        payload = {"error": f"Lead for team ID '{team_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamLead",
                "description": "Retrieves the lead for a specific team.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


class GetLabelByName(Tool):
    """Fetches a label using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        labels = data.get("labels", {}).values()
        for label in labels.values():
            if label.get("name") == name:
                payload = label
                out = json.dumps(payload)
                return out
        payload = {"error": f"Label with name '{name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLabelByName",
                "description": "Retrieves a label by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class AddLabelToWorkItem(Tool):
    """Inserts a label into a work item."""

    @staticmethod
    def invoke(data: dict[str, Any], work_item_id: str = None, label_id: str = None) -> str:
        links = data.get("work_item_labels", {}).values()
        new_link = {
            "work_item_id": work_item_id,
            "label_id": label_id,
        }
        data["work_item_labels"][new_link["work_item_label_id"]] = new_link
        payload = {
                "status": "success",
                "message": f"Label '{label_id}' added to work item '{work_item_id}'.",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddLabelToWorkItem",
                "description": "Adds a label to a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "work_item_id": {"type": "string"},
                        "label_id": {"type": "string"},
                    },
                    "required": ["work_item_id", "label_id"],
                },
            },
        }


class GetPullRequestByNumber(Tool):
    """Fetches a pull request using its repository and number."""

    @staticmethod
    def invoke(data: dict[str, Any], repository_id: str = None, number: int = None) -> str:
        prs = data.get("pull_requests", {}).values()
        for pr in prs.values():
            if pr.get("repository_id") == repository_id and pr.get("number") == number:
                payload = pr
                out = json.dumps(payload)
                return out
        payload = {"error": f"PR #{number} in repo '{repository_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPullRequestByNumber",
                "description": "Retrieves a pull request by its repository and number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {"type": "string"},
                        "number": {"type": "integer"},
                    },
                    "required": ["repository_id", "number"],
                },
            },
        }


class MergePullRequest(Tool):
    """Combines a pull request."""

    def invoke(
        data: dict[str, Any],
        id: Any = None,
        pr_id: str = None
    ) -> str:
        prs = data.get("pull_requests", {}).values()
        for pr in prs.values():
            if pr.get("id") == pr_id:
                pr["state"] = "merged"
                pr["merged_at"] = "2025-01-28T00:00:00Z"
                pr["closed_at"] = "2025-01-28T00:00:00Z"
                payload = {"status": "success", "message": f"PR '{pr_id}' merged."}
                out = json.dumps(payload)
                return out
        payload = {"error": f"PR with ID '{pr_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "mergePullRequest",
                "description": "Merges a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


class GetBranchById(Tool):
    """Fetches a branch using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        branch_id = id
        branches = data.get("branches", {}).values()
        for b in branches.values():
            if b.get("id") == branch_id:
                payload = b
                out = json.dumps(payload)
                return out
        payload = {"error": f"Branch with ID '{branch_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getBranchById",
                "description": "Retrieves a branch by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


class DeleteBranch(Tool):
    """Removes a branch."""

    def invoke(
        data: dict[str, Any],
        branch_id: str = None,
        id: Any = None
    ) -> str:
        branches = data.get("branches", {}).values()
        original_count = len(branches)
        data["branches"] = [b for b in branches.values() if b.get("id") != branch_id]
        if len(data["branches"]) < original_count:
            payload = {"status": "success", "message": f"Branch '{branch_id}' deleted."}
            out = json.dumps(payload)
            return out
        payload = {"error": f"Branch with ID '{branch_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteBranch",
                "description": "Deletes a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


class FindWorkItemByPr(Tool):
    """Locates a work item linked to a pull request number."""

    @staticmethod
    def invoke(data: dict[str, Any], pr_number: int = None, repository_id: int = None) -> str:
        pass
        # This is a simulated implementation since there is no direct connection in the schema.
        # It will locate a work item that closely corresponds to the PR title.
        prs = data.get("pull_requests", {}).values()
        work_items = data.get("work_items", {}).values()

        pr_title = ""
        for pr in prs.values():
            if pr.get("repository_id") == repository_id and pr.get("number") == pr_number:
                pr_title = pr.get("title", "").lower()
                break

        if not pr_title:
            payload = {"error": "PR not found."}
            out = json.dumps(payload)
            return out

        for item in work_items.values():
            if item.get("title", "").lower() in pr_title:
                payload = item
                out = json.dumps(payload)
                return out
        payload = {"info": "No matching work item found for PR."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findWorkItemByPr",
                "description": "Finds a work item associated with a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pr_number": {"type": "integer"},
                        "repository_id": {"type": "string"},
                    },
                    "required": ["pr_number", "repository_id"],
                },
            },
        }


class AddMemberToTeam(Tool):
    """Inserts a user into a team with a designated role."""

    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None, user_id: str = None, role: str = None) -> str:
        members = data.get("team_members", {}).values()
        new_member = {
            "team_id": team_id,
            "user_id": user_id,
            "role": role,
            "added_at": "2025-01-28T00:00:00Z",
        }
        data["team_members"][new_member["team_member_id"]] = new_member
        payload = {
            "status": "success",
            "message": f"User '{user_id}' added to team '{team_id}'.",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addMemberToTeam",
                "description": "Adds a user to a team.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "role": {"type": "string"},
                    },
                    "required": ["team_id", "user_id", "role"],
                },
            },
        }


class GetAlertById(Tool):
    """Fetches an alert using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        alert_id = id
        alerts = data.get("alerts", {}).values()
        for alert in alerts.values():
            if alert.get("id") == alert_id:
                payload = alert
                out = json.dumps(payload)
                return out
        payload = {"error": f"Alert with ID '{alert_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAlertById",
                "description": "Retrieves an alert by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


class UpdateAlertState(Tool):
    """Modifies the status of an alert."""

    def invoke(
        data: dict[str, Any],
        alert_id: str = None,
        id: Any = None,
        new_state: str = None
    ) -> str:
        alerts = data.get("alerts", {}).values()
        for alert in alerts.values():
            if alert.get("id") == alert_id:
                alert["state"] = new_state
                payload = {
                    "status": "success",
                    "message": f"State for alert '{alert_id}' updated to '{new_state}'.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Alert with ID '{alert_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateAlertState",
                "description": "Updates the state of an alert.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "state": {"type": "string"},
                    },
                    "required": ["id", "state"],
                },
            },
        }


class GetProjectById(Tool):
    """Fetches a project using its ID."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: Any = None,
        project_id: str = None
    ) -> str:
        projects = data.get("projects", {}).values()
        for p in projects.values():
            if p.get("id") == project_id:
                payload = p
                out = json.dumps(payload)
                return out
        payload = {"error": f"Project with ID '{project_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectById",
                "description": "Retrieves a project by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


class FindProjectOwnerTeam(Tool):
    """Identifies the owner team for a project."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        repos = data.get("repositories", {}).values()
        teams = data.get("teams", {}).values()

        repo_id = None
        for repo in repos.values():
            if repo.get("project_id") == project_id:
                repo_id = repo.get("id")
                break

        if not repo_id:
            payload = {"error": "Could not determine repository for project."}
            out = json.dumps(payload)
            return out

        for team in teams.values():
            #"project_focus": ["proj_001", "proj_002", "proj_003"],
            if project_id in team["project_focus"]:
                payload = {"team_id": team["id"]}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Could not determine owner for project '{project_id}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindProjectOwnerTeam",
                "description": "Finds the owner team for a project.",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }


class UpdateProjectStatus(Tool):
    """Modifies the active status of a project."""

    def invoke(
        data: dict[str, Any],
        id: Any = None,
        is_active: bool = None,
        project_id: str = None
    ) -> str:
        projects = data.get("projects", {}).values()
        for p in projects.values():
            if p.get("id") == project_id:
                p["is_active"] = is_active
                payload = {
                    "status": "success",
                    "message": f"Project '{project_id}' active status set to {is_active}.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Project with ID '{project_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateProjectStatus",
                "description": "Updates the active status of a project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "is_active": {"type": "boolean"},
                    },
                    "required": ["id", "is_active"],
                },
            },
        }


class CreateRelease(Tool):
    """Generates a new release for a project."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None, version: str = None, notes: str = None, created_by: str = None) -> str:
        releases = data.get("releases", {}).values()
        new_id_num = max([int(r["id"].split("_")[1]) for r in releases]) + 1
        new_id = f"release_{new_id_num:03d}"

        new_release = {
            "id": new_id,
            "project_id": project_id,
            "version": version,
            "notes": notes,
            "created_at": "2025-01-28T00:00:00Z",
            "created_by": created_by,
        }
        data["releases"][new_release["release_id"]] = new_release
        payload = new_release
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createRelease",
                "description": "Creates a new release for a project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "version": {"type": "string"},
                        "notes": {"type": "string"},
                        "created_by": {"type": "string"},
                    },
                    "required": ["project_id", "version", "notes", "created_by"],
                },
            },
        }


class GetRepositoriesForProject(Tool):
    """Fetches all repositories for a specified project ID."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        repos = data.get("repositories", {}).values()
        project_repos = [r for r in repos.values() if r.get("project_id") == project_id]
        payload = project_repos
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getRepositoriesForProject",
                "description": "Retrieves all repositories for a given project ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }


class GetTeamById(Tool):
    """Fetches a team using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        team_id = id
        teams = data.get("teams", {}).values()
        for team in teams.values():
            if team.get("id") == team_id:
                payload = team
                out = json.dumps(payload)
                return out
        payload = {"error": f"Team with ID '{team_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamById",
                "description": "Retrieves a team by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


class GetRepositoryByName(Tool):
    """Fetches a repository using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        repo_name = name
        repositories = data.get("repositories", {}).values()

        for repo in repositories.values():
            if repo.get("name") == repo_name:
                payload = repo
                out = json.dumps(payload)
                return out
        payload = {"error": f"Repository with name '{repo_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRepositoryByName",
                "description": "Retrieves a repository by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of the repository.",
                        }
                    },
                    "required": ["name"],
                },
            },
        }


class GetOwnerForBisect(Tool):
    """Fetches the primary owner for a bisect operation according to its suspect files."""

    @staticmethod
    def invoke(data: dict[str, Any], bisect_id: str = None) -> str:
        bisect_results = data.get("bisect_results", {}).values()
        ownership_map = data.get("ownership_map", {}).values()

        #1. Locate the bisect result record
        bisect_record = None
        for result in bisect_results.values():
            if result.get("id") == bisect_id:
                bisect_record = result
                break

        if not bisect_record:
            payload = {"error": f"Bisect with ID '{bisect_id}' not found."}
            out = json.dumps(payload)
            return out

        #2. Retrieve the list of suspect files from the bisect record
        suspect_files = bisect_record.get("suspect_files", [])
        if not suspect_files:
            payload = {"owner_id": "user_005"}
            out = json.dumps(payload)
            return out
            payload = {"error": f"No suspect files found for bisect '{bisect_id}'."}
            out = json.dumps(
                payload)
            return out

        #3. Utilize the first suspect file to identify primary ownership, as it is the most probable cause.
        primary_suspect_file = suspect_files[0]

        #4. Identify the most specific owner for the primary suspect file using the ownership map
        most_specific_owner = None
        longest_match = -1
        for ownership in ownership_map.values():
            owner_path = ownership.get("file_path")
            if primary_suspect_file.startswith(owner_path):
                if len(owner_path) > longest_match:
                    longest_match = len(owner_path)
                    most_specific_owner = ownership

        if most_specific_owner:
            payload = most_specific_owner
            out = json.dumps(payload)
            return out
        payload = {"owner_id": "user_008"}
        out = json.dumps(payload)
        return out
        payload = {
                "error": f"Could not determine an owner for the primary suspect file '{primary_suspect_file}' in bisect '{bisect_id}'."
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOwnerForBisect",
                "description": "Retrieves the primary owner for a bisect operation by analyzing its most likely suspect file.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "bisect_id": {
                            "type": "string",
                            "description": "The unique ID of the bisect operation.",
                        }
                    },
                    "required": ["bisect_id"],
                },
            },
        }


class GetProjectIdForRepositoryName(Tool):
    """Fetches the project ID for a specified repository name."""

    @staticmethod
    def invoke(data: dict[str, Any], repository_name: str = None) -> str:
        repositories = data.get("repositories", {}).values()

        for repo in repositories.values():
            if repo.get("name") == repository_name:
                payload = {"project_id": repo.get("project_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Repository with name '{repository_name}' not found."}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectIdForRepositoryName",
                "description": "Retrieves the project ID for a given repository name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_name": {
                            "type": "string",
                            "description": "The name of the repository.",
                        }
                    },
                    "required": ["repository_name"],
                },
            },
        }


class SearchVulnerabilitiesByCVE(Tool):
    """Looks for vulnerabilities that correspond to a particular CVE identifier."""

    @staticmethod
    def invoke(data: dict[str, Any], cve: str = None) -> str:
        cve_id = cve
        vulnerabilities = data.get("vulnerabilities", {}).values()

        matching_vulnerabilities = [
            vuln for vuln in vulnerabilities.values() if vuln.get("cve") == cve_id
        ]
        payload = {"vulnerabilities": matching_vulnerabilities}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchVulnerabilitiesByCve",
                "description": "Searches for vulnerabilities matching a specific CVE identifier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cve": {
                            "type": "string",
                            "description": "The CVE identifier to search for (e.g., 'CVE-2024-1234').",
                        }
                    },
                    "required": ["cve"],
                },
            },
        }


class GetRepositoryByFullName(Tool):
    """Fetches a repository using its complete name (e.g., 'gamecorp/engine-core')."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_full_name: str = None) -> str:
        repositories = data.get("repositories", {}).values()

        for repo in repositories.values():
            if repo.get("repo_full_name") == repo_full_name:
                payload = repo
                out = json.dumps(payload)
                return out
        payload = {"error": f"Repository with full name '{repo_full_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getRepositoryByFullName",
                "description": "Retrieves a repository by its full name (e.g., 'gamecorp/engine-core').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_full_name": {
                            "type": "string",
                            "description": "The full name of the repository, including the owner.",
                        }
                    },
                    "required": ["repo_full_name"],
                },
            },
        }


class SearchPullRequestsByRepositoryId(Tool):
    """Looks for all pull requests in a particular repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repository_id: str = None) -> str:
        pull_requests = data.get("pull_requests", {}).values()

        matching_prs = [
            pr for pr in pull_requests.values() if pr.get("repository_id") == repository_id
        ]
        payload = {"pull_requests": matching_prs}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchPullRequestsByRepositoryId",
                "description": "Searches for all pull requests within a specific repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {
                            "type": "string",
                            "description": "The unique ID of the repository to search within.",
                        }
                    },
                    "required": ["repository_id"],
                },
            },
        }


class FindCrashesByCrashFingerprint(Tool):
    """Locates all crash events that correspond to a specific crash fingerprint."""

    @staticmethod
    def invoke(data: dict[str, Any], crash_fingerprint: str = None) -> str:
        crash_events = data.get("crash_events", {}).values()

        matching_crashes = [
            crash
            for crash in crash_events.values() if crash.get("crash_fingerprint") == crash_fingerprint
        ]
        payload = {"crashes": matching_crashes}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCrashesByCrashFingerprint",
                "description": "Finds all crash events that match a specific crash fingerprint.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crash_fingerprint": {
                            "type": "string",
                            "description": "The unique fingerprint identifier of the crash to search for.",
                        }
                    },
                    "required": ["crash_fingerprint"],
                },
            },
        }


class GetProjectByName(Tool):
    """Fetches a project using its precise name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        project_name = name
        projects = data.get("projects", {}).values()

        for project in projects.values():
            if project.get("name") == project_name:
                payload = project
                out = json.dumps(payload)
                return out
        payload = {"error": f"Project with name '{project_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectByName",
                "description": "Retrieves a project by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The exact name of the project.",
                        }
                    },
                    "required": ["name"],
                },
            },
        }


class UpdatePullRequestState(Tool):
    """Modifies the status of a pull request (e.g., 'open', 'closed')."""

    def invoke(
        data: dict[str, Any],
        id: Any = None,
        new_state: str = None,
        pull_request_id: str = None
    ) -> str:
        pull_requests = data.get("pull_requests", {}).values()

        for pr in pull_requests.values():
            if pr.get("id") == pull_request_id:
                pr["state"] = new_state
                if new_state == "closed" and not pr.get("merged_at"):
                    pr["closed_at"] = (
                        "2025-01-28T00:00:00Z"  # Employ a uniform placeholder timestamp
                    )
                payload = {
                    "status": "success",
                    "message": f"State for pull request '{pull_request_id}' updated to '{new_state}'.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Pull request with ID '{pull_request_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updatePullRequestState",
                "description": "Updates the state of a pull request (e.g., 'open', 'closed').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "The unique ID of the pull request.",
                        },
                        "state": {
                            "type": "string",
                            "description": "The new state for the pull request (e.g., 'open', 'closed').",
                        },
                    },
                    "required": ["id", "state"],
                },
            },
        }


class SearchPullRequestsByRepositoryId(Tool):
    """Looks for all pull requests in a particular repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repository_id: str = None) -> str:
        pull_requests = data.get("pull_requests", {}).values()

        matching_prs = [
            pr for pr in pull_requests.values() if pr.get("repository_id") == repository_id
        ]
        payload = {"pull_requests": matching_prs}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchPullRequestsByRepositoryId",
                "description": "Searches for all pull requests within a specific repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {
                            "type": "string",
                            "description": "The unique ID of the repository to search within.",
                        }
                    },
                    "required": ["repository_id"],
                },
            },
        }


class CreateBranch(Tool):
    """Generates a new branch in a repository based on a source branch."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        branch_name: str = None,
        repository_id: str = None,
        source_branch_id: Any = None
    ) -> str:
        branches = data.get("branches", {}).values()
        new_id_num = max([int(b["id"].split("_")[1]) for b in branches.values()]) + 1
        new_id = f"branch_{new_id_num:03d}"

        new_branch = {
            "id": new_id,
            "repository_id": repository_id,
            "name": branch_name,
            "created_at": "2025-01-28T00:00:00Z",
        }
        data["branches"][new_branch["branche_id"]] = new_branch
        payload = new_branch
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateBranch",
                "description": "Creates a new branch in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {"type": "string"},
                        "branch_name": {"type": "string"},
                        "source_branch_id": {"type": "string"},
                    },
                    "required": ["repository_id", "branch_name", "source_branch_id"],
                },
            },
        }


class GetTmsJobByName(Tool):
    """Fetches a TMS job using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], job_name: str = None) -> str:
        jobs = data.get("tms_jobs", {}).values()
        for job in jobs.values():
            if job.get("job_name") == job_name:
                payload = job
                out = json.dumps(payload)
                return out
        payload = {"error": f"TMS job with name '{job_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTmsJobByName",
                "description": "Retrieves a TMS job by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"job_name": {"type": "string"}},
                    "required": ["job_name"],
                },
            },
        }


class UpdateTmsJobStatus(Tool):
    """Modifies the status of a TMS job."""

    @staticmethod
    def invoke(data: dict[str, Any], job_id: str = None, status: str = None) -> str:
        jobs = data.get("tms_jobs", {}).values()
        for job in jobs.values():
            if job.get("id") == job_id:
                job["status"] = status
                payload = {
                    "status": "success",
                    "message": f"Status for TMS job '{job_id}' updated to '{status}'.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"TMS job with ID '{job_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateTmsJobStatus",
                "description": "Updates the status of a TMS job.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["job_id", "status"],
                },
            },
        }


class FindPreviousSuccessfulDeployment(Tool):
    """Locates the most recent successful deployment for a specified pipeline prior to a certain time."""

    @staticmethod
    def invoke(data: dict[str, Any], pipeline_id: str = None, before_timestamp: str = None) -> str:
        deployments = sorted(
            [
                d
                for d in data.get("deployments", {}).values()
                if d.get("pipeline_id") == pipeline_id
                and d.get("deployed_at") < before_timestamp
            ],
            key=lambda x: x["deployed_at"],
            reverse=True,
        )

        for d in deployments.values():
            if d.get("status") == "successful":
                payload = d
                out = json.dumps(payload)
                return out
        payload = {
                "error": f"No successful deployment found for pipeline '{pipeline_id}' before '{before_timestamp}'."
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindPreviousSuccessfulDeployment",
                "description": "Finds the last successful deployment for a pipeline before a specific time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pipeline_id": {"type": "string"},
                        "before_timestamp": {"type": "string"},
                    },
                    "required": ["pipeline_id", "before_timestamp"],
                },
            },
        }


class GetWorkItemAssignee(Tool):
    """Fetches the assignee for a work item."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: Any = None,
        item_id: str = None
    ) -> str:
        work_items = data.get("work_items", {}).values()
        for item in work_items.values():
            if item.get("id") == item_id:
                payload = {"assignee_id": item.get("assignee_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Work item with ID '{item_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWorkItemAssignee",
                "description": "Retrieves the assignee for a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


class FindWorkItemByTitle(Tool):
    """Locates a work item using its title."""

    @staticmethod
    def invoke(data: dict[str, Any], title: str = None) -> str:
        title_query = title
        work_items = data.get("work_items", {}).values()
        for item in work_items.values():
            if title_query in item.get("title", ""):
                payload = item
                out = json.dumps(payload)
                return out
        payload = {"error": f"No work item found with title containing '{title_query}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindWorkItemByTitle",
                "description": "Finds a work item by its title.",
                "parameters": {
                    "type": "object",
                    "properties": {"title": {"type": "string"}},
                    "required": ["title"],
                },
            },
        }


class GetCurrentTimestamp(Tool):
    """Provides a fixed current timestamp value."""

    def invoke(data: dict[str, Any], unused: Any = None) -> str:
        payload = {"timestamp": "2025-08-13T01:01:01Z"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCurrentTimestamp",
                "description": "Returns a hardcoded current timestamp value (2025-08-13T01:01:01Z).",
                "parameters": {},
            },
        }


class GetTestResultById(Tool):
    """Fetches a specific test result using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        test_result_id = id
        test_results = data.get("test_results", {}).values()
        for result in test_results.values():
            if result.get("id") == test_result_id:
                payload = result
                out = json.dumps(payload)
                return out
        payload = {"error": f"Test result with ID '{test_result_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTestResultById",
                "description": "Retrieves a specific test result by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "The unique ID of the test result.",
                        }
                    },
                    "required": ["id"],
                },
            },
        }


class GenerateFingerprintForTestResult(Tool):
    """Creates a consistent crash fingerprint from a test result."""

    @staticmethod
    def invoke(data: dict[str, Any], test_result_id: str = None) -> str:
        test_results = data.get("test_results", {}).values()

        test_result = None
        for result in test_results.values():
            if result.get("id") == test_result_id:
                test_result = result
                break

        if not test_result:
            payload = {"error": f"Test result with ID '{test_result_id}' not found."}
            out = json.dumps(payload)
            return out

        failure_type = test_result.get("failure_type", "unknown").replace("_", "")
        stack_trace = test_result.get("stack_trace", "")
        top_frame = stack_trace.split("\n")[0] if stack_trace else "unknown_frame"

        module_or_function = (
            top_frame.split("!")[0].split("(")[0].strip()
            if "!" in top_frame
            else top_frame.split("(")[0].strip()
        )
        module_or_function = module_or_function.split("::")[-1]

        if "TextureLoadingTest" in module_or_function and "assertion" in failure_type:
            fingerprint = "renderer_character_load_access_violation_xyz"
        elif "NavigationMeshTest" in module_or_function and "timeout" in failure_type:
            fingerprint = "ai_navmesh_generation_timeout_abc"
        elif "ConnectionTest" in module_or_function and "network" in failure_type:
            fingerprint = "network_connection_timeout_30s_xyz"
        else:
            fingerprint = f"generic_{failure_type}_{module_or_function}"
        payload = {"fingerprint": fingerprint}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateFingerprintForTestResult",
                "description": "Generates a deterministic crash fingerprint from a test result to link it with crash events.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_result_id": {
                            "type": "string",
                            "description": "The unique ID of the test result.",
                        }
                    },
                    "required": ["test_result_id"],
                },
            },
        }


class FindTestRunForBuildRun(Tool):
    """Locates the test run linked to a specific build run by aligning pipelines and timestamps."""

    @staticmethod
    def invoke(data: dict[str, Any], build_run_id: str = None) -> str:
        build_runs = data.get("build_runs", {}).values()
        test_runs = data.get("test_runs", {}).values()
        pipelines = data.get("pipelines", {}).values()

        build_run = next((b for b in build_runs.values() if b.get("id") == build_run_id), None)
        if not build_run:
            payload = {"error": f"Build run with ID '{build_run_id}' not found."}
            out = json.dumps(payload)
            return out

        pipeline = next(
            (p for p in pipelines.values() if p.get("name") == build_run.get("pipeline_name")),
            None,
        )
        if not pipeline:
            payload = {
                "error": f"Pipeline named '{build_run.get('pipeline_name')}' not found."
            }
            out = json.dumps(payload)
            return out

        build_start = build_run.get("started_at")
        build_end = build_run.get("ended_at")

        for test_run in test_runs.values():
            if test_run.get("pipeline_id") == pipeline.get("id"):
                test_time = test_run.get("created_at")
                if build_start <= test_time <= build_end:
                    payload = test_run
                    out = json.dumps(payload)
                    return out
        payload = {"error": f"No matching test run found for build run '{build_run_id}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findTestRunForBuildRun",
                "description": "Finds the test run associated with a build run by matching pipeline and timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "build_run_id": {
                            "type": "string",
                            "description": "The ID of the build run.",
                        }
                    },
                    "required": ["build_run_id"],
                },
            },
        }


class FindFailedTestResultsForTestRun(Tool):
    """Locates all unsuccessful test results for a specified test run ID."""

    @staticmethod
    def invoke(data: dict[str, Any], test_run_id: str = None) -> str:
        test_results = data.get("test_results", {}).values()

        failed_tests = [
            tr
            for tr in test_results.values() if tr.get("test_run_id") == test_run_id and tr.get("status") == "failed"
        ]

        if not failed_tests:
            payload = {"info": f"No failed tests found for test run '{test_run_id}'."}
            out = json.dumps(payload)
            return out
        payload = {"failed_tests": failed_tests}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findFailedTestResultsForTestRun",
                "description": "Finds all failed test results for a given test run ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_run_id": {
                            "type": "string",
                            "description": "The ID of the test run.",
                        }
                    },
                    "required": ["test_run_id"],
                },
            },
        }


class GetBranchByName(Tool):
    """Fetches a branch using its name within a particular repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repository_id: str = None, branch_name: str = None) -> str:
        branches = data.get("branches", {}).values()
        for branch in branches.values():
            if (
                branch.get("repository_id") == repository_id
                and branch.get("name") == branch_name
            ):
                payload = branch
                out = json.dumps(payload)
                return out
        payload = {"error": f"Branch '{branch_name}' not found in repository '{repository_id}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBranchByName",
                "description": "Retrieves a branch by its name within a specific repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {
                            "type": "string",
                            "description": "The ID of the repository.",
                        },
                        "branch_name": {
                            "type": "string",
                            "description": "The name of the branch.",
                        },
                    },
                    "required": ["repository_id", "branch_name"],
                },
            },
        }


class SendNotification(Tool):
    """Emulates sending a notification by appending it to the notifications log."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        notification_type: str = "system_notification",
        title: str = None,
        message: str = None,
        recipient_id: str = None,
        channel: str = "slack"
    ) -> str:
        notifications = data.get("notifications", {}).values()

        # Create a new distinct ID
        if not notifications:
            new_id_num = 1
        else:
            new_id_num = max(int(n["id"].split("_")[1]) for n in notifications.values() + 1
        new_id = f"notification_{new_id_num:03d}"

        # Construct the new notification object
        new_notification = {
            "id": new_id,
            "project_id": project_id,
            "notification_type": notification_type,
            "title": title,
            "message": message,
            "recipient_id": recipient_id,
            "channel": channel,
            "sent_at": "2025-01-28T00:00:00Z",  # Utilize a standard placeholder timestamp
            "read_at": None,
        }

        data["notifications"][notification_id] = new_notification
        payload = {
            "status": "success",
            "message": f"Notification '{new_id}' sent successfully.",
            "notification_id": new_id,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendNotification",
                "description": "Simulates sending a notification by adding it to the notifications log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project related to the notification.",
                        },
                        "recipient_id": {
                            "type": "string",
                            "description": "The ID of the user who should receive the notification.",
                        },
                        "title": {
                            "type": "string",
                            "description": "The title of the notification.",
                        },
                        "message": {
                            "type": "string",
                            "description": "The body content of the notification.",
                        },
                        "channel": {
                            "type": "string",
                            "description": "The channel for the notification (e.g., 'slack', 'email').",
                            "default": "slack",
                        },
                        "notification_type": {
                            "type": "string",
                            "description": "The type of notification (e.g., 'incident_alert', 'bug_assignment').",
                            "default": "system_notification",
                        },
                    },
                    "required": ["project_id", "recipient_id", "title", "message"],
                },
            },
        }


class FindFullPathForFileName(Tool):
    """Locates the complete file path for a specified file name by querying the ownership map."""

    @staticmethod
    def invoke(data: dict[str, Any], file_name: str = None) -> str:
        ownership_map = data.get("ownership_map", {}).values()

        # Look for a file path that concludes with the specified file name.
        for ownership in ownership_map.values():
            if ownership.get("file_path", "").endswith(file_name):
                payload = {"file_path": ownership.get("file_path")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Full path for file name '{file_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindFullPathForFileName",
                "description": "Finds the full file path for a given file name by searching the ownership map.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_name": {
                            "type": "string",
                            "description": "The name of the file (e.g., 'renderer.cpp').",
                        }
                    },
                    "required": ["file_name"],
                },
            },
        }


class GetPipelineById(Tool):
    """Fetches a pipeline using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        pipeline_id = id
        pipelines = data.get("pipelines", {}).values()
        for p in pipelines.values():
            if p.get("id") == pipeline_id:
                payload = p
                out = json.dumps(payload)
                return out
        payload = {"error": f"Pipeline with ID '{pipeline_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPipelineById",
                "description": "Retrieves a pipeline by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "The unique ID of the pipeline.",
                        }
                    },
                    "required": ["id"],
                },
            },
        }


TOOLS = [
    GetBuildRunById(),
    GetBisectResultForBuildRun(),
    UpdateBuildRunTriageStatus(),
    FindFileOwner(),
    GetUserById(),
    GetUserByName(),
    CreateWorkItem(),
    FindBugByCrashFingerprint(),
    LinkWorkItems(),
    AddCommentToWorkItem(),
    UpdateWorkItemState(),
    GetAssetByPath(),
    UpdateAssetValidationStatus(),
    GetCrashEventById(),
    UpdateCrashEventStatus(),
    GetVulnerabilityById(),
    UpdateVulnerabilityStatus(),
    GetTranslationByKeyAndLocale(),
    UpdateTranslation(),
    UpdateTranslationValidationStatus(),
    AddRevisionHistoryEntry(),
    CreateFixProposal(),
    GetDeploymentById(),
    GetRollbackByDeploymentId(),
    CreateDeployment(),
    GetTeamByName(),
    GetTeamLead(),
    GetLabelByName(),
    AddLabelToWorkItem(),
    GetPullRequestByNumber(),
    MergePullRequest(),
    GetBranchById(),
    DeleteBranch(),
    FindWorkItemByPr(),
    AddMemberToTeam(),
    GetAlertById(),
    UpdateAlertState(),
    GetProjectById(),
    FindProjectOwnerTeam(),
    UpdateProjectStatus(),
    CreateRelease(),
    GetRepositoriesForProject(),
    GetTeamById(),
    GetRepositoryByName(),
    GetOwnerForBisect(),
    GetProjectIdForRepositoryName(),
    SearchVulnerabilitiesByCVE(),
    GetRepositoryByFullName(),
    SearchPullRequestsByRepositoryId(),
    FindCrashesByCrashFingerprint(),
    GetProjectByName(),
    UpdatePullRequestState(),
    SearchPullRequestsByRepositoryId(),
    CreateBranch(),
    GetTmsJobByName(),
    UpdateTmsJobStatus(),
    FindPreviousSuccessfulDeployment(),
    GetWorkItemAssignee(),
    FindWorkItemByTitle(),
    GetCurrentTimestamp(),
    GetTestResultById(),
    GenerateFingerprintForTestResult(),
    FindTestRunForBuildRun(),
    FindFailedTestResultsForTestRun(),
    GetBranchByName(),
    FindFullPathForFileName(),
    SendNotification(),
    GetPipelineById(),
]
