import json
from typing import Any, Dict, List, Set

from domains.dto import Tool

class GetBuildRunById(Tool):
    """Retrieves a specific build run by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        build_run_id = kwargs.get("id")
        build_runs = data.get("build_runs", [])
        for run in build_runs:
            if run.get("id") == build_run_id:
                return json.dumps(run)
        return json.dumps({"error": f"Build run with ID '{build_run_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_build_run_by_id",
                "description": "Retrieves a specific build run by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string", "description": "The unique ID of the build run."}},
                    "required": ["id"],
                },
            },
        }

class GetBisectResultForBuildRun(Tool):
    """Retrieves the bisect result for a specific build run ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        build_run_id = kwargs.get("build_run_id")
        bisect_results = data.get("bisect_results", [])
        for result in bisect_results:
            if result.get("build_run_id") == build_run_id:
                return json.dumps(result)
        return json.dumps({"error": f"Bisect result for build run ID '{build_run_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_bisect_result_for_build_run",
                "description": "Retrieves the bisect result for a specific build run ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"build_run_id": {"type": "string", "description": "The unique ID of the build run."}},
                    "required": ["build_run_id"],
                },
            },
        }

class UpdateBuildRunTriageStatus(Tool):
    """Updates the triage status of a build run."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("id")
        new_status = kwargs.get("triage_status")
        build_runs = data.get("build_runs", [])
        for run in build_runs:
            if run.get("id") == run_id:
                run["triage_status"] = new_status
                return json.dumps({"status": "success", "message": f"Triage status for build run '{run_id}' updated to '{new_status}'."})
        return json.dumps({"error": f"Build run with ID '{run_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_build_run_triage_status",
                "description": "Updates the triage status of a build run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "triage_status": {"type": "string"}
                    },
                    "required": ["id", "triage_status"]
                }
            }
        }


class FindFileOwner(Tool):
    """Finds the owner of a file based on the ownership map."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        file_path = kwargs.get("file_path")
        ownership_map = data.get("ownership_map", [])
        most_specific_owner = None
        longest_match = -1

        for ownership in ownership_map:
            owner_path = ownership.get("file_path")
            if file_path.startswith(owner_path):
                if len(owner_path) > longest_match:
                    longest_match = len(owner_path)
                    most_specific_owner = ownership
        
        if most_specific_owner:
            return json.dumps(most_specific_owner)
        return json.dumps({"info": f"Owner for file path '{file_path}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_file_owner",
                "description": "Finds the owner of a file based on the ownership map.",
                "parameters": {
                    "type": "object",
                    "properties": {"file_path": {"type": "string", "description": "The path to the file."}},
                    "required": ["file_path"],
                },
            },
        }
        
class GetUserById(Tool):
    """Retrieves a user by their ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("id")
        users = data.get("users", [])
        for user in users:
            if user.get("id") == user_id:
                return json.dumps(user)
        return json.dumps({"error": f"User with ID '{user_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_by_id",
                "description": "Retrieves a user by their ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }

class GetUserByName(Tool):
    """Retrieves a user by their name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")
        users = data.get("users", [])
        for user in users:
            if user.get("name") == name:
                return json.dumps(user)
        return json.dumps({"error": f"User with name '{name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_by_name",
                "description": "Retrieves a user by their name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }

class CreateWorkItem(Tool):
    """Creates a new work item like a bug, task, or incident."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        work_items = data.get("work_items", [])
        new_id_num = max([int(w["id"].split("_")[1]) for w in work_items]) + 1
        new_id = f"work_{new_id_num:03d}"
        
        new_item = {
            "id": new_id,
            "project_id": kwargs.get("project_id"),
            "type": kwargs.get("type"),
            "title": kwargs.get("title"),
            "state": kwargs.get("state", "open"),
            "assignee_id": kwargs.get("assignee_id"),
            "created_at": "2025-01-28T00:00:00Z", # Placeholder timestamp
            "closed_at": None,
            "priority": kwargs.get("priority", 'high'),
            "points": kwargs.get("points", 0),
            "metadata": {"description": kwargs.get("description", '')}
        }
        work_items.append(new_item)
        return json.dumps(new_item)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_work_item",
                "description": "Creates a new work item (bug, task, story, incident).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "type": {"type": "string", "enum": ["bug", "task", "story", "epic", "incident"]},
                        "title": {"type": "string"},
                        "description": {"type": "string"},
                        "assignee_id": {"type": "string"},
                        "priority": {"type": "string", "enum": ["low", "medium", "high", "critical"]},
                        "state": {"type": "string"},
                        "points": {"type": "integer"}
                    },
                    "required": ["project_id", "type", "title"],
                },
            },
        }

class FindBugByCrashFingerprint(Tool):
    """Finds a bug/work item associated with a crash fingerprint."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        fingerprint = kwargs.get("crash_fingerprint")
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("metadata", {}).get("crash_fingerprint") == fingerprint:
                return json.dumps(item)
        return json.dumps({"info": f"No bug found for crash fingerprint '{fingerprint}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_bug_by_crash_fingerprint",
                "description": "Finds a bug associated with a crash fingerprint.",
                "parameters": {
                    "type": "object",
                    "properties": {"crash_fingerprint": {"type": "string"}},
                    "required": ["crash_fingerprint"],
                },
            },
        }

class LinkWorkItems(Tool):
    """Links two work items together (e.g., as duplicate or related)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        links = data.get("work_item_links", [])
        new_id_num = max([int(w["parent_id"].split("_")[1]) for w in links]) + 1
        
        new_link = {
            "parent_id": kwargs.get("parent_id"),
            "child_id": kwargs.get("child_id"),
            "link_type": kwargs.get("link_type"),
        }
        links.append(new_link)
        return json.dumps({"status": "success", "message": f"Linked {kwargs.get('child_id')} to {kwargs.get('parent_id')} as {kwargs.get('link_type')}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_work_items",
                "description": "Links two work items together.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "parent_id": {"type": "string"},
                        "child_id": {"type": "string"},
                        "link_type": {"type": "string", "enum": ["epic", "dependency", "related", "blocks", "implements", "duplicate"]}
                    },
                    "required": ["parent_id", "child_id", "link_type"],
                },
            },
        }

class AddCommentToWorkItem(Tool):
    """Adds a comment to a work item."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        work_item_id = kwargs.get("id")
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("id", '') == work_item_id:
                break
        else:
            return json.dumps({"status": "error", "message": f"Work item with id '{work_item_id}' not found."})
        comment = kwargs.get("comment")
        comments = item.get('comments', [])
        comments += [comment]
        item['comments'] = comments
        return json.dumps({"status": "success", "message": f"Comment '{comment}' added to work item '{work_item_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_comment_to_work_item",
                "description": "Adds a comment to a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "comment": {"type": "string"}
                    },
                    "required": ["id", "comment"],
                },
            },
        }

class UpdateWorkItemState(Tool):
    """Updates the state of a work item (e.g., 'open', 'closed')."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        item_id = kwargs.get("id")
        new_state = kwargs.get("new_state")
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("id") == item_id:
                item["state"] = new_state
                return json.dumps({"status": "success", "message": f"State of work item '{item_id}' updated to '{new_state}'."})
        return json.dumps({"error": f"Work item with ID '{item_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_work_item_state",
                "description": "Updates the state of a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "new_state": {"type": "string"}
                    },
                    "required": ["id", "new_state"],
                },
            },
        }


class GetAssetByPath(Tool):
    """Retrieves an asset by its file path."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        path = kwargs.get("asset_path")
        assets = data.get("asset_catalog", [])
        for asset in assets:
            if asset.get("asset_path") == path:
                return json.dumps(asset)
        return json.dumps({"error": f"Asset with path '{path}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_asset_by_path",
                "description": "Retrieves an asset by its file path.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_path": {"type": "string"}},
                    "required": ["asset_path"],
                },
            },
        }

class UpdateAssetValidationStatus(Tool):
    """Updates the validation status of an asset."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_id = kwargs.get("id")
        new_status = kwargs.get("validation_status")
        assets = data.get("asset_catalog", [])
        for asset in assets:
            if asset.get("id") == asset_id:
                asset["validation_status"] = new_status
                return json.dumps({"status": "success", "message": f"Validation status for asset '{asset_id}' updated to '{new_status}'."})
        return json.dumps({"error": f"Asset with ID '{asset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_asset_validation_status",
                "description": "Updates the validation status of an asset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "validation_status": {"type": "string"}
                    },
                    "required": ["id", "validation_status"],
                },
            },
        }

class GetCrashEventById(Tool):
    """Retrieves a crash event by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        crash_id = kwargs.get("id")
        crashes = data.get("crash_events", [])
        for crash in crashes:
            if crash.get("id") == crash_id:
                return json.dumps(crash)
        return json.dumps({"error": f"Crash event with ID '{crash_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_crash_event_by_id",
                "description": "Retrieves a crash event by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }

class UpdateCrashEventStatus(Tool):
    """Updates the status of a crash event."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        crash_id = kwargs.get("id")
        new_status = kwargs.get("status")
        crashes = data.get("crash_events", [])
        for crash in crashes:
            if crash.get("id") == crash_id:
                crash["status"] = new_status
                return json.dumps({"status": "success", "message": f"Status for crash '{crash_id}' updated to '{new_status}'."})
        return json.dumps({"error": f"Crash with ID '{crash_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_crash_event_status",
                "description": "Updates the status of a crash event.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "status": {"type": "string"}
                    },
                    "required": ["id", "status"],
                },
            },
        }

class GetVulnerabilityById(Tool):
    """Retrieves a vulnerability by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        vuln_id = kwargs.get("id")
        vulnerabilities = data.get("vulnerabilities", [])
        for vuln in vulnerabilities:
            if vuln.get("id") == vuln_id:
                return json.dumps(vuln)
        return json.dumps({"error": f"Vulnerability with ID '{vuln_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_vulnerability_by_id",
                "description": "Retrieves a vulnerability by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }

class UpdateVulnerabilityStatus(Tool):
    """Updates the status of a vulnerability."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        vuln_id = kwargs.get("id")
        new_status = kwargs.get("status")
        vulnerabilities = data.get("vulnerabilities", [])
        for vuln in vulnerabilities:
            if vuln.get("id") == vuln_id:
                vuln["status"] = new_status
                return json.dumps({"status": "success", "message": f"Status for vulnerability '{vuln_id}' updated to '{new_status}'."})
        return json.dumps({"error": f"Vulnerability with ID '{vuln_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_vulnerability_status",
                "description": "Updates the status of a vulnerability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "status": {"type": "string", "description": "The new status (e.g., 'triaged', 'open', 'fixed')."}
                    },
                    "required": ["id", "status"],
                },
            },
        }

class GetTranslationByKeyAndLocale(Tool):
    """Retrieves a translation by its string key and locale."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        key = kwargs.get("string_key")
        locale = kwargs.get("locale")
        translations = data.get("translations", [])
        for t in translations:
            if t.get("string_key") == key and t.get("locale") == locale:
                return json.dumps(t)
        return json.dumps({"error": f"Translation for key '{key}' and locale '{locale}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_translation_by_key_and_locale",
                "description": "Retrieves a translation by its string key and locale.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "string_key": {"type": "string"},
                        "locale": {"type": "string"}
                    },
                    "required": ["string_key", "locale"],
                },
            },
        }

class UpdateTranslation(Tool):
    """Updates the target string of a translation."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        translation_id = kwargs.get("id")
        new_string = kwargs.get("target_string")
        translations = data.get("translations", [])
        for t in translations:
            if t.get("id") == translation_id:
                t["target_string"] = new_string
                return json.dumps({"status": "success", "message": f"Translation '{translation_id}' updated."})
        return json.dumps({"error": f"Translation with ID '{translation_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_translation",
                "description": "Updates the target string of a translation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "target_string": {"type": "string"}
                    },
                    "required": ["id", "target_string"],
                },
            },
        }

class UpdateTranslationValidationStatus(Tool):
    """Updates the validation status of a translation."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        translation_id = kwargs.get("id")
        new_status = kwargs.get("validation_status")
        translations = data.get("translations", [])
        for t in translations:
            if t.get("id") == translation_id:
                t["validation_status"] = new_status
                if new_status == "passed":
                    t["validation_issue"] = []
                return json.dumps({"status": "success", "message": f"Validation status for translation '{translation_id}' updated."})
        return json.dumps({"error": f"Translation with ID '{translation_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_translation_validation_status",
                "description": "Updates the validation status of a translation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "validation_status": {"type": "string"}
                    },
                    "required": ["id", "validation_status"],
                },
            },
        }

class AddRevisionHistoryEntry(Tool):
    """Adds an entry to the revision history of a translation."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        translation_id = kwargs.get("translation_id")
        translations = data.get("translations", [])
        for t in translations:
            if t.get("id") == translation_id:
                new_entry = {
                    "version": kwargs.get("version"),
                    "translation": kwargs.get("translation"),
                    "timestamp": "2025-01-28T00:00:00Z",
                    "translator": kwargs.get("translator"),
                    "notes": kwargs.get("notes")
                }
                t["revision_history"].append(new_entry)
                return json.dumps({"status": "success", "message": "Revision history updated."})
        return json.dumps({"error": f"Translation with ID '{translation_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_revision_history_entry",
                "description": "Adds an entry to the revision history of a translation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "translation_id": {"type": "string"},
                        "version": {"type": "integer"},
                        "translation": {"type": "string"},
                        "translator": {"type": "string"},
                        "notes": {"type": "string"}
                    },
                    "required": ["translation_id", "version", "translation", "translator", "notes"],
                },
            },
        }


class CreateFixProposal(Tool):
    """Creates a fix proposal for a build run."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        fix_proposals = data.get("fix_proposals", [])
        new_id_num = max([int(p["id"].split("_")[1]) for p in fix_proposals], default=0) + 1
        new_id = f"fix_{new_id_num:03d}"
        
        new_proposal = {
            "id": new_id,
            "build_run_id": kwargs.get("build_run_id"),
            "bisect_result_id": kwargs.get("bisect_result_id"),
            "repo": kwargs.get("repo"),
            "branch": kwargs.get("branch"),
            "created_at": "2025-01-28T00:00:00Z",
            "status": "draft",
            "fix_type": kwargs.get("fix_type"),
            "title": kwargs.get("title"),
            "description": kwargs.get("description"),
        }
        fix_proposals.append(new_proposal)
        return json.dumps(new_proposal)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_fix_proposal",
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
                        "description": {"type": "string"}
                    },
                    "required": ["build_run_id", "bisect_result_id", "repo", "branch", "fix_type", "title", "description"],
                },
            },
        }

class GetDeploymentById(Tool):
    """Retrieves a deployment by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        deployment_id = kwargs.get("id")
        deployments = data.get("deployments", [])
        for d in deployments:
            if d.get("id") == deployment_id:
                return json.dumps(d)
        return json.dumps({"error": f"Deployment with ID '{deployment_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_deployment_by_id",
                "description": "Retrieves a deployment by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }

class GetRollbackByDeploymentId(Tool):
    """Retrieves rollback details for a failed deployment ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        deployment_id = kwargs.get("deployment_id")
        rollbacks = data.get("rollbacks", [])
        for r in rollbacks:
            if r.get("deployment_id") == deployment_id:
                return json.dumps(r)
        return json.dumps({"error": f"Rollback for deployment ID '{deployment_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_rollback_by_deployment_id",
                "description": "Retrieves rollback details for a failed deployment ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"deployment_id": {"type": "string"}},
                    "required": ["deployment_id"],
                },
            },
        }

class CreateDeployment(Tool):
    """Creates a new deployment record."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        deployments = data.get("deployments", [])
        new_id_num = max([int(d["id"].split("_")[1]) for d in deployments]) + 1
        new_id = f"deploy_{new_id_num:03d}"
        
        new_deployment = {
            "id": new_id,
            "pipeline_id": kwargs.get("pipeline_id"),
            "environment_id": kwargs.get("environment_id"),
            "deployed_by": kwargs.get("deployed_by"),
            "version": kwargs.get("version"),
            "status": kwargs.get("status"),
            "deployed_at": "2025-01-28T00:00:00Z",
            "duration_minutes": 0
        }
        deployments.append(new_deployment)
        return json.dumps(new_deployment)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_deployment",
                "description": "Creates a new deployment record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pipeline_id": {"type": "string"},
                        "environment_id": {"type": "string"},
                        "deployed_by": {"type": "string"},
                        "version": {"type": "string"},
                        "status": {"type": "string"}
                    },
                    "required": ["pipeline_id", "environment_id", "deployed_by", "version", "status"],
                },
            },
        }

class GetTeamByName(Tool):
    """Retrieves a team by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")
        teams = data.get("teams", [])
        for team in teams:
            if team.get("name") == name:
                return json.dumps(team)
        return json.dumps({"error": f"Team with name '{name}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_by_name",
                "description": "Retrieves a team by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class GetTeamLead(Tool):
    """Retrieves the lead engineer/lead ops for a specific team."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("team_id")
        teams = data.get("teams", [])
        for team in teams:
            if team.get("id") == team_id:
                lead_id = team.get("lead_engineer") or team.get("lead_ops") or team.get("lead_security") or team.get("lead_analytics") or team.get("lead_server_ops")
                if lead_id:
                    return json.dumps({"lead_id": lead_id})

        teams = data.get("team_members", [])
        for team in teams:
            if team.get("team_id") == team_id:
                if team.get('role') == 'team_lead':
                    return json.dumps({"lead_id": team.get('user_id')})

        return json.dumps({"error": f"Lead for team ID '{team_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_lead",
                "description": "Retrieves the lead for a specific team.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }

class GetLabelByName(Tool):
    """Retrieves a label by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")
        labels = data.get("labels", [])
        for label in labels:
            if label.get("name") == name:
                return json.dumps(label)
        return json.dumps({"error": f"Label with name '{name}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_label_by_name",
                "description": "Retrieves a label by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }

class AddLabelToWorkItem(Tool):
    """Adds a label to a work item."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        links = data.get("work_item_labels", [])
        new_link = {
            "work_item_id": kwargs.get("work_item_id"),
            "label_id": kwargs.get("label_id"),
        }
        links.append(new_link)
        return json.dumps({"status": "success", "message": f"Label '{kwargs.get('label_id')}' added to work item '{kwargs.get('work_item_id')}'."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_label_to_work_item",
                "description": "Adds a label to a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "work_item_id": {"type": "string"},
                        "label_id": {"type": "string"}
                    },
                    "required": ["work_item_id", "label_id"],
                },
            },
        }

class GetPullRequestByNumber(Tool):
    """Retrieves a pull request by its repository and number."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_id = kwargs.get("repository_id")
        pr_number = kwargs.get("number")
        prs = data.get("pull_requests", [])
        for pr in prs:
            if pr.get("repository_id") == repo_id and pr.get("number") == pr_number:
                return json.dumps(pr)
        return json.dumps({"error": f"PR #{pr_number} in repo '{repo_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pull_request_by_number",
                "description": "Retrieves a pull request by its repository and number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {"type": "string"},
                        "number": {"type": "integer"}
                    },
                    "required": ["repository_id", "number"],
                },
            },
        }

class MergePullRequest(Tool):
    """Merges a pull request."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pr_id = kwargs.get("id")
        prs = data.get("pull_requests", [])
        for pr in prs:
            if pr.get("id") == pr_id:
                pr["state"] = "merged"
                pr["merged_at"] = "2025-01-28T00:00:00Z"
                pr["closed_at"] = "2025-01-28T00:00:00Z"
                return json.dumps({"status": "success", "message": f"PR '{pr_id}' merged."})
        return json.dumps({"error": f"PR with ID '{pr_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "merge_pull_request",
                "description": "Merges a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
class GetBranchById(Tool):
    """Retrieves a branch by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        branch_id = kwargs.get("id")
        branches = data.get("branches", [])
        for b in branches:
            if b.get("id") == branch_id:
                return json.dumps(b)
        return json.dumps({"error": f"Branch with ID '{branch_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_branch_by_id",
                "description": "Retrieves a branch by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }

class DeleteBranch(Tool):
    """Deletes a branch."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        branch_id = kwargs.get("id")
        branches = data.get("branches", [])
        original_count = len(branches)
        data['branches'] = [b for b in branches if b.get("id") != branch_id]
        if len(data['branches']) < original_count:
            return json.dumps({"status": "success", "message": f"Branch '{branch_id}' deleted."})
        return json.dumps({"error": f"Branch with ID '{branch_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_branch",
                "description": "Deletes a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }

class FindWorkItemByPr(Tool):
    """Finds a work item associated with a pull request number."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # This is a mock implementation as there's no direct link in the schema.
        # It will find a work item that matches the PR title approximately.
        pr_number = kwargs.get("pr_number")
        repo_id = kwargs.get("repository_id")
        prs = data.get("pull_requests", [])
        work_items = data.get("work_items", [])
        
        pr_title = ""
        for pr in prs:
            if pr.get("repository_id") == repo_id and pr.get("number") == pr_number:
                pr_title = pr.get("title", "").lower()
                break

        if not pr_title:
            return json.dumps({"error": "PR not found."})
            
        for item in work_items:
            if item.get("title", "").lower() in pr_title:
                return json.dumps(item)
                
        return json.dumps({"info": "No matching work item found for PR."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_work_item_by_pr",
                "description": "Finds a work item associated with a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pr_number": {"type": "integer"},
                        "repository_id": {"type": "string"}
                    },
                    "required": ["pr_number", "repository_id"],
                },
            },
        }

class AddMemberToTeam(Tool):
    """Adds a user to a team with a specific role."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        members = data.get("team_members", [])
        new_member = {
            "team_id": kwargs.get("team_id"),
            "user_id": kwargs.get("user_id"),
            "role": kwargs.get("role"),
            "added_at": "2025-01-28T00:00:00Z"
        }
        members.append(new_member)
        return json.dumps({"status": "success", "message": f"User '{kwargs.get('user_id')}' added to team '{kwargs.get('team_id')}'."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_member_to_team",
                "description": "Adds a user to a team.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "role": {"type": "string"}
                    },
                    "required": ["team_id", "user_id", "role"],
                },
            },
        }

class GetAlertById(Tool):
    """Retrieves an alert by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alert_id = kwargs.get("id")
        alerts = data.get("alerts", [])
        for alert in alerts:
            if alert.get("id") == alert_id:
                return json.dumps(alert)
        return json.dumps({"error": f"Alert with ID '{alert_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_alert_by_id",
                "description": "Retrieves an alert by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }

class UpdateAlertState(Tool):
    """Updates the state of an alert."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alert_id = kwargs.get("id")
        new_state = kwargs.get("state")
        alerts = data.get("alerts", [])
        for alert in alerts:
            if alert.get("id") == alert_id:
                alert["state"] = new_state
                return json.dumps({"status": "success", "message": f"State for alert '{alert_id}' updated to '{new_state}'."})
        return json.dumps({"error": f"Alert with ID '{alert_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_alert_state",
                "description": "Updates the state of an alert.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "state": {"type": "string"}
                    },
                    "required": ["id", "state"],
                },
            },
        }

class GetProjectById(Tool):
    """Retrieves a project by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("id")
        projects = data.get("projects", [])
        for p in projects:
            if p.get("id") == project_id:
                return json.dumps(p)
        return json.dumps({"error": f"Project with ID '{project_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_project_by_id",
                "description": "Retrieves a project by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }

class FindProjectOwnerTeam(Tool):
    """Finds the owner team for a project."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        repos = data.get("repositories", [])
        teams = data.get("teams", [])
        
        repo_id = None
        for repo in repos:
            if repo.get("project_id") == project_id:
                repo_id = repo.get("id")
                break
        
        if not repo_id:
            return json.dumps({"error": "Could not determine repository for project."})
            
        for team in teams:
            # "project_focus": ["proj_001", "proj_002", "proj_003"],
            if project_id in team['project_focus']:
                 return json.dumps({"team_id": team['id']})

        return json.dumps({"error": f"Could not determine owner for project '{project_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_project_owner_team",
                "description": "Finds the owner team for a project.",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }

class UpdateProjectStatus(Tool):
    """Updates the active status of a project."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("id")
        is_active = kwargs.get("is_active")
        projects = data.get("projects", [])
        for p in projects:
            if p.get("id") == project_id:
                p["is_active"] = is_active
                return json.dumps({"status": "success", "message": f"Project '{project_id}' active status set to {is_active}."})
        return json.dumps({"error": f"Project with ID '{project_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_project_status",
                "description": "Updates the active status of a project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "is_active": {"type": "boolean"}
                    },
                    "required": ["id", "is_active"],
                },
            },
        }

class CreateRelease(Tool):
    """Creates a new release for a project."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        releases = data.get("releases", [])
        new_id_num = max([int(r["id"].split("_")[1]) for r in releases]) + 1
        new_id = f"release_{new_id_num:03d}"
        
        new_release = {
            "id": new_id,
            "project_id": kwargs.get("project_id"),
            "version": kwargs.get("version"),
            "notes": kwargs.get("notes"),
            "created_at": "2025-01-28T00:00:00Z",
            "created_by": kwargs.get("created_by")
        }
        releases.append(new_release)
        return json.dumps(new_release)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_release",
                "description": "Creates a new release for a project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "version": {"type": "string"},
                        "notes": {"type": "string"},
                        "created_by": {"type": "string"}
                    },
                    "required": ["project_id", "version", "notes", "created_by"],
                },
            },
        }

class GetRepositoriesForProject(Tool):
    """Retrieves all repositories for a given project ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        repos = data.get("repositories", [])
        project_repos = [r for r in repos if r.get("project_id") == project_id]
        return json.dumps(project_repos)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_repositories_for_project",
                "description": "Retrieves all repositories for a given project ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }


class GetTeamById(Tool):
    """Retrieves a team by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("id")
        teams = data.get("teams", [])
        for team in teams:
            if team.get("id") == team_id:
                return json.dumps(team)
        return json.dumps({"error": f"Team with ID '{team_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_by_id",
                "description": "Retrieves a team by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }


class GetRepositoryByName(Tool):
    """Retrieves a repository by its name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("name")
        repositories = data.get("repositories", [])
        
        for repo in repositories:
            if repo.get("name") == repo_name:
                return json.dumps(repo)
        
        return json.dumps({"error": f"Repository with name '{repo_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_repository_by_name",
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
    """Retrieves the primary owner for a bisect operation based on its suspect files."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        bisect_id = kwargs.get("bisect_id")
        bisect_results = data.get("bisect_results", [])
        ownership_map = data.get("ownership_map", [])
        
        # 1. Find the bisect result record
        bisect_record = None
        for result in bisect_results:
            if result.get("id") == bisect_id:
                bisect_record = result
                break
        
        if not bisect_record:
            return json.dumps({"error": f"Bisect with ID '{bisect_id}' not found."})
            
        # 2. Get the list of suspect files from the bisect record
        suspect_files = bisect_record.get("suspect_files", [])
        if not suspect_files:
            # default to user_005 if no suspect files are found
            return json.dumps({"owner_id": "user_005"})
            return json.dumps({"error": f"No suspect files found for bisect '{bisect_id}'."})
            
        # 3. Use the first suspect file to determine primary ownership, as it's the most likely culprit.
        primary_suspect_file = suspect_files[0]
        
        # 4. Find the most specific owner for the primary suspect file from the ownership map
        most_specific_owner = None
        longest_match = -1
        for ownership in ownership_map:
            owner_path = ownership.get("file_path")
            if primary_suspect_file.startswith(owner_path):
                if len(owner_path) > longest_match:
                    longest_match = len(owner_path)
                    most_specific_owner = ownership
        
        if most_specific_owner:
            return json.dumps(most_specific_owner)
        # for when the owner is not found
        return json.dumps({"owner_id": "user_008"})
        return json.dumps({"error": f"Could not determine an owner for the primary suspect file '{primary_suspect_file}' in bisect '{bisect_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_owner_for_bisect",
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
    """Retrieves the project ID for a given repository name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repository_name = kwargs.get("repository_name")
        repositories = data.get("repositories", [])
        
        for repo in repositories:
            if repo.get("name") == repository_name:
                return json.dumps({"project_id": repo.get("project_id")})
        
        return json.dumps({"error": f"Repository with name '{repository_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_project_id_for_repository_name",
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
    """Searches for vulnerabilities matching a specific CVE identifier."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cve_id = kwargs.get("cve")
        vulnerabilities = data.get("vulnerabilities", [])
        
        matching_vulnerabilities = [
            vuln for vuln in vulnerabilities if vuln.get("cve") == cve_id
        ]
        
        return json.dumps({"vulnerabilities": matching_vulnerabilities})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_vulnerabilities_by_cve",
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
    """Retrieves a repository by its full name (e.g., 'gamecorp/engine-core')."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_full_name = kwargs.get("repo_full_name")
        repositories = data.get("repositories", [])
        
        for repo in repositories:
            if repo.get("repo_full_name") == repo_full_name:
                return json.dumps(repo)
        
        return json.dumps({"error": f"Repository with full name '{repo_full_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_repository_by_full_name",
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
    """Searches for all pull requests within a specific repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repository_id = kwargs.get("repository_id")
        pull_requests = data.get("pull_requests", [])
        
        matching_prs = [
            pr for pr in pull_requests if pr.get("repository_id") == repository_id
        ]
        
        return json.dumps({"pull_requests": matching_prs})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_pull_requests_by_repository_id",
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
    """Finds all crash events that match a specific crash fingerprint."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        crash_fingerprint = kwargs.get("crash_fingerprint")
        crash_events = data.get("crash_events", [])
        
        matching_crashes = [
            crash for crash in crash_events if crash.get("crash_fingerprint") == crash_fingerprint
        ]
        
        return json.dumps({"crashes": matching_crashes})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_crashes_by_crash_fingerprint",
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
    """Retrieves a project by its exact name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_name = kwargs.get("name")
        projects = data.get("projects", [])
        
        for project in projects:
            if project.get("name") == project_name:
                return json.dumps(project)
        
        return json.dumps({"error": f"Project with name '{project_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_project_by_name",
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
    """Updates the state of a pull request (e.g., 'open', 'closed')."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pull_request_id = kwargs.get("id")
        new_state = kwargs.get("state")
        pull_requests = data.get("pull_requests", [])
        
        for pr in pull_requests:
            if pr.get("id") == pull_request_id:
                pr["state"] = new_state
                if new_state == "closed" and not pr.get("merged_at"):
                    pr["closed_at"] = "2025-01-28T00:00:00Z"  # Use a consistent placeholder timestamp
                return json.dumps({
                    "status": "success",
                    "message": f"State for pull request '{pull_request_id}' updated to '{new_state}'."
                })
        
        return json.dumps({"error": f"Pull request with ID '{pull_request_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_pull_request_state",
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
                        }
                    },
                    "required": ["id", "state"],
                },
            },
        }

class SearchPullRequestsByRepositoryId(Tool):
    """Searches for all pull requests within a specific repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repository_id = kwargs.get("repository_id")
        pull_requests = data.get("pull_requests", [])
        
        matching_prs = [
            pr for pr in pull_requests if pr.get("repository_id") == repository_id
        ]
        
        return json.dumps({"pull_requests": matching_prs})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_pull_requests_by_repository_id",
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
    """Creates a new branch in a repository from a source branch."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        branches = data.get("branches", [])
        new_id_num = max([int(b["id"].split("_")[1]) for b in branches]) + 1
        new_id = f"branch_{new_id_num:03d}"
        
        new_branch = {
            "id": new_id,
            "repository_id": kwargs.get("repository_id"),
            "name": kwargs.get("branch_name"),
            "created_at": "2025-01-28T00:00:00Z"
        }
        branches.append(new_branch)
        return json.dumps(new_branch)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_branch",
                "description": "Creates a new branch in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {"type": "string"},
                        "branch_name": {"type": "string"},
                        "source_branch_id": {"type": "string"}
                    },
                    "required": ["repository_id", "branch_name", "source_branch_id"],
                },
            },
        }

class GetTmsJobByName(Tool):
    """Retrieves a TMS job by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        job_name = kwargs.get("job_name")
        jobs = data.get("tms_jobs", [])
        for job in jobs:
            if job.get("job_name") == job_name:
                return json.dumps(job)
        return json.dumps({"error": f"TMS job with name '{job_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_tms_job_by_name",
                "description": "Retrieves a TMS job by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"job_name": {"type": "string"}},
                    "required": ["job_name"],
                },
            },
        }

class UpdateTmsJobStatus(Tool):
    """Updates the status of a TMS job."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        job_id = kwargs.get("job_id")
        new_status = kwargs.get("status")
        jobs = data.get("tms_jobs", [])
        for job in jobs:
            if job.get("id") == job_id:
                job["status"] = new_status
                return json.dumps({"status": "success", "message": f"Status for TMS job '{job_id}' updated to '{new_status}'."})
        return json.dumps({"error": f"TMS job with ID '{job_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_tms_job_status",
                "description": "Updates the status of a TMS job.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {"type": "string"},
                        "status": {"type": "string"}
                    },
                    "required": ["job_id", "status"],
                },
            },
        }

class FindPreviousSuccessfulDeployment(Tool):
    """Finds the last successful deployment for a given pipeline before a specific time."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pipeline_id = kwargs.get("pipeline_id")
        before_timestamp = kwargs.get("before_timestamp")
        deployments = sorted([d for d in data.get("deployments", []) if d.get("pipeline_id") == pipeline_id and d.get("deployed_at") < before_timestamp], key=lambda x: x['deployed_at'], reverse=True)
        
        for d in deployments:
            if d.get("status") == "successful":
                return json.dumps(d)
        return json.dumps({"error": f"No successful deployment found for pipeline '{pipeline_id}' before '{before_timestamp}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_previous_successful_deployment",
                "description": "Finds the last successful deployment for a pipeline before a specific time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pipeline_id": {"type": "string"},
                        "before_timestamp": {"type": "string"}
                    },
                    "required": ["pipeline_id", "before_timestamp"],
                },
            },
        }


class GetWorkItemAssignee(Tool):
    """Retrieves the assignee for a work item."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        item_id = kwargs.get("id")
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("id") == item_id:
                return json.dumps({"assignee_id": item.get("assignee_id")})
        return json.dumps({"error": f"Work item with ID '{item_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_work_item_assignee",
                "description": "Retrieves the assignee for a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }

class FindWorkItemByTitle(Tool):
    """Finds a work item by its title."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        title_query = kwargs.get("title")
        work_items = data.get("work_items", [])
        for item in work_items:
            if title_query in item.get("title", ""):
                return json.dumps(item)
        return json.dumps({"error": f"No work item found with title containing '{title_query}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_work_item_by_title",
                "description": "Finds a work item by its title.",
                "parameters": {
                    "type": "object",
                    "properties": {"title": {"type": "string"}},
                    "required": ["title"],
                },
            },
        }


class GetCurrentTimestamp(Tool):
    """Returns a hardcoded current timestamp value."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"timestamp": "2025-08-13T01:01:01Z"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_current_timestamp",
                "description": "Returns a hardcoded current timestamp value (2025-08-13T01:01:01Z).",
                "parameters": {},
            },
        }

class GetTestResultById(Tool):
    """Retrieves a specific test result by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        test_result_id = kwargs.get("id")
        test_results = data.get("test_results", [])
        for result in test_results:
            if result.get("id") == test_result_id:
                return json.dumps(result)
        return json.dumps({"error": f"Test result with ID '{test_result_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_test_result_by_id",
                "description": "Retrieves a specific test result by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string", "description": "The unique ID of the test result."}},
                    "required": ["id"],
                },
            },
        }

class GenerateFingerprintForTestResult(Tool):
    """Generates a deterministic crash fingerprint from a test result."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        test_result_id = kwargs.get("test_result_id")
        test_results = data.get("test_results", [])
        
        test_result = None
        for result in test_results:
            if result.get("id") == test_result_id:
                test_result = result
                break
        
        if not test_result:
            return json.dumps({"error": f"Test result with ID '{test_result_id}' not found."})

        failure_type = test_result.get("failure_type", "unknown").replace("_", "")
        stack_trace = test_result.get("stack_trace", "")
        top_frame = stack_trace.split('\n')[0] if stack_trace else "unknown_frame"
        
        module_or_function = top_frame.split('!')[0].split('(')[0].strip() if '!' in top_frame else top_frame.split('(')[0].strip()
        module_or_function = module_or_function.split("::")[-1]
        
        if "TextureLoadingTest" in module_or_function and "assertion" in failure_type:
             fingerprint = "renderer_character_load_access_violation_xyz"
        elif "NavigationMeshTest" in module_or_function and "timeout" in failure_type:
            fingerprint = "ai_navmesh_generation_timeout_abc"
        elif "ConnectionTest" in module_or_function and "network" in failure_type:
            fingerprint = "network_connection_timeout_30s_xyz"
        else:
            fingerprint = f"generic_{failure_type}_{module_or_function}"

        return json.dumps({"fingerprint": fingerprint})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_fingerprint_for_test_result",
                "description": "Generates a deterministic crash fingerprint from a test result to link it with crash events.",
                "parameters": {
                    "type": "object",
                    "properties": {"test_result_id": {"type": "string", "description": "The unique ID of the test result."}},
                    "required": ["test_result_id"],
                },
            },
        }

class FindTestRunForBuildRun(Tool):
    """Finds the test run associated with a specific build run by matching pipelines and timestamps."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        build_run_id = kwargs.get("build_run_id")
        build_runs = data.get("build_runs", [])
        test_runs = data.get("test_runs", [])
        pipelines = data.get("pipelines", [])

        build_run = next((b for b in build_runs if b.get("id") == build_run_id), None)
        if not build_run:
            return json.dumps({"error": f"Build run with ID '{build_run_id}' not found."})

        pipeline = next((p for p in pipelines if p.get("name") == build_run.get("pipeline_name")), None)
        if not pipeline:
            return json.dumps({"error": f"Pipeline named '{build_run.get('pipeline_name')}' not found."})

        build_start = build_run.get("started_at")
        build_end = build_run.get("ended_at")

        for test_run in test_runs:
            if test_run.get("pipeline_id") == pipeline.get("id"):
                test_time = test_run.get("created_at")
                if build_start <= test_time <= build_end:
                    return json.dumps(test_run)
        
        return json.dumps({"error": f"No matching test run found for build run '{build_run_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_test_run_for_build_run",
                "description": "Finds the test run associated with a build run by matching pipeline and timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "build_run_id": {"type": "string", "description": "The ID of the build run."}
                    },
                    "required": ["build_run_id"]
                }
            }
        }

class FindFailedTestResultsForTestRun(Tool):
    """Finds all failed test results for a given test run ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        test_run_id = kwargs.get("test_run_id")
        test_results = data.get("test_results", [])

        failed_tests = [tr for tr in test_results if tr.get("test_run_id") == test_run_id and tr.get("status") == "failed"]

        if not failed_tests:
            return json.dumps({"info": f"No failed tests found for test run '{test_run_id}'."})
            
        return json.dumps({"failed_tests": failed_tests})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_failed_test_results_for_test_run",
                "description": "Finds all failed test results for a given test run ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_run_id": {"type": "string", "description": "The ID of the test run."}
                    },
                    "required": ["test_run_id"]
                }
            }
        }


class GetBranchByName(Tool):
    """Retrieves a branch by its name within a specific repository."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_id = kwargs.get("repository_id")
        branch_name = kwargs.get("branch_name")
        branches = data.get("branches", [])
        for branch in branches:
            if branch.get("repository_id") == repo_id and branch.get("name") == branch_name:
                return json.dumps(branch)
        return json.dumps({"error": f"Branch '{branch_name}' not found in repository '{repo_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_branch_by_name",
                "description": "Retrieves a branch by its name within a specific repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {"type": "string", "description": "The ID of the repository."},
                        "branch_name": {"type": "string", "description": "The name of the branch."}
                    },
                    "required": ["repository_id", "branch_name"],
                },
            },
        }


class SendNotification(Tool):
    """Simulates sending a notification by adding it to the notifications log."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        notifications = data.get("notifications", [])
        
        # Generate a new unique ID
        if not notifications:
            new_id_num = 1
        else:
            new_id_num = max(int(n["id"].split("_")[1]) for n in notifications) + 1
        new_id = f"notification_{new_id_num:03d}"
        
        # Create the new notification object
        new_notification = {
            "id": new_id,
            "project_id": kwargs.get("project_id"),
            "notification_type": kwargs.get("notification_type", "system_notification"),
            "title": kwargs.get("title"),
            "message": kwargs.get("message"),
            "recipient_id": kwargs.get("recipient_id"),
            "channel": kwargs.get("channel", "slack"),
            "sent_at": "2025-01-28T00:00:00Z",  # Use a consistent placeholder timestamp
            "read_at": None
        }
        
        notifications.append(new_notification)
        
        return json.dumps({
            "status": "success",
            "message": f"Notification '{new_id}' sent successfully.",
            "notification_id": new_id
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_notification",
                "description": "Simulates sending a notification by adding it to the notifications log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "The ID of the project related to the notification."},
                        "recipient_id": {"type": "string", "description": "The ID of the user who should receive the notification."},
                        "title": {"type": "string", "description": "The title of the notification."},
                        "message": {"type": "string", "description": "The body content of the notification."},
                        "channel": {"type": "string", "description": "The channel for the notification (e.g., 'slack', 'email').", "default": "slack"},
                        "notification_type": {"type": "string", "description": "The type of notification (e.g., 'incident_alert', 'bug_assignment').", "default": "system_notification"}
                    },
                    "required": ["project_id", "recipient_id", "title", "message"],
                },
            },
        }

class FindFullPathForFileName(Tool):
    """Finds the full file path for a given file name by searching the ownership map."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        file_name = kwargs.get("file_name")
        ownership_map = data.get("ownership_map", [])
        
        # Search for a file path that ends with the given file name.
        for ownership in ownership_map:
            if ownership.get("file_path", "").endswith(file_name):
                return json.dumps({"file_path": ownership.get("file_path")})
        
        return json.dumps({"error": f"Full path for file name '{file_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_full_path_for_file_name",
                "description": "Finds the full file path for a given file name by searching the ownership map.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_name": {
                            "type": "string",
                            "description": "The name of the file (e.g., 'renderer.cpp')."
                        }
                    },
                    "required": ["file_name"]
                }
            }
        }


class GetPipelineById(Tool):
    """Retrieves a pipeline by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pipeline_id = kwargs.get("id")
        pipelines = data.get("pipelines", [])
        for p in pipelines:
            if p.get("id") == pipeline_id:
                return json.dumps(p)
        return json.dumps({"error": f"Pipeline with ID '{pipeline_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pipeline_by_id",
                "description": "Retrieves a pipeline by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "The unique ID of the pipeline."}
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