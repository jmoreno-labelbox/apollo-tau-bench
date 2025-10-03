import json
from typing import Any

from domains.dto import Tool

FIXED_TIMESTAMP = "2025-08-14T10:00:00Z"


def _get_next_id(prefix: str, existing_ids: list[str]) -> str:
    """Determines the subsequent sequential ID by identifying the highest current ID for a specified prefix. This approach is more reliable than presuming the list is in order."""
    pass
    max_id_num = 0
    for item_id in existing_ids:
        if item_id.startswith(prefix):
            try:
                num_part = int(item_id.split("_")[-1])
                if num_part > max_id_num:
                    max_id_num = num_part
            except (ValueError, IndexError):
                continue

    if max_id_num == 0:
        if not any(s.startswith(prefix) for s in existing_ids):
            return f"{prefix}_001"

    return f"{prefix}_{max_id_num + 1:03d}"


class get_crash_event_details(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], crash_id: str) -> str:
        pass
        crash_events = data.get("crash_events", [])
        for event in crash_events:
            if event.get("id") == crash_id:
                payload = event
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Crash event with id '{crash_id}' not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetCrashEventDetails",
                "description": "Retrieves the full details for a given crash event.",
                "parameters": {
                    "type": "object",
                    "properties": {"crash_id": {"type": "string"}},
                    "required": ["crash_id"],
                },
            },
        }


class find_work_item_by_crash_fingerprint(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], fingerprint: str) -> str:
        pass
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("metadata") and fingerprint in item["metadata"].get(
                "crash_fingerprint", ""
            ):
                payload = item
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Work item with crash fingerprint '{fingerprint}' not found"}
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindWorkItemByCrashFingerprint",
                "description": "Finds a work item by its associated crash fingerprint.",
                "parameters": {
                    "type": "object",
                    "properties": {"fingerprint": {"type": "string"}},
                    "required": ["fingerprint"],
                },
            },
        }


class get_code_owner_for_module(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], module_name: str) -> str:
        pass
        ownership_map = data.get("ownership_map", [])
        path_map = {"GameEngine.dll": "src/game/engine/renderer.cpp"}
        file_path = path_map.get(module_name)
        if not file_path:
            payload = {"error": f"No known file path for module '{module_name}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        for owner_info in ownership_map:
            if owner_info.get("file_path") in file_path:
                payload = owner_info
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Owner for module '{module_name}' not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetCodeOwnerForModule",
                "description": "Finds the code owner for a given module name by mapping it to a file path.",
                "parameters": {
                    "type": "object",
                    "properties": {"module_name": {"type": "string"}},
                    "required": ["module_name"],
                },
            },
        }


class update_work_item(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], work_item_id: str, updates: dict[str, Any]) -> str:
        pass
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("id") == work_item_id:
                item.update(updates)
                data["work_items"] = work_items
                payload = {"success": f"Work item '{work_item_id}' was updated."}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Work item '{work_item_id}' not found."}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateWorkItem",
                "description": "Updates one or more fields of an existing work item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "work_item_id": {"type": "string"},
                        "updates": {
                            "type": "object",
                            "description": "A dictionary of fields to update.",
                        },
                    },
                    "required": ["work_item_id", "updates"],
                },
            },
        }


class link_work_items(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], parent_id: str, child_id: str, link_type: str
    ) -> str:
        pass
        links = data.get("work_item_links", [])
        new_link = {
            "parent_id": parent_id,
            "child_id": child_id,
            "link_type": link_type,
        }
        links.append(new_link)
        data["work_item_links"] = links
        link_id = f"link_{parent_id}_{child_id}"
        payload = {
                "success": f"Link of type '{link_type}' created between '{parent_id}' and '{child_id}'.",
                "link_id": link_id,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "LinkWorkItems",
                "description": "Links two work items together with a specific relationship type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "parent_id": {"type": "string"},
                        "child_id": {"type": "string"},
                        "link_type": {"type": "string"},
                    },
                    "required": ["parent_id", "child_id", "link_type"],
                },
            },
        }


class get_asset_details(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str) -> str:
        pass
        assets = data.get("asset_catalog", [])
        for asset in assets:
            if asset.get("id") == asset_id:
                payload = asset
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Asset with id '{asset_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getAssetDetails",
                "description": "Retrieves the full details for a given asset from the asset catalog.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_id": {"type": "string"}},
                    "required": ["asset_id"],
                },
            },
        }


class render_asset_preview(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str) -> str:
        pass
        preview_uri = f"https://previews.techcorp.com/{asset_id}_360.mp4"
        payload = {"preview_uri": preview_uri}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "renderAssetPreview",
                "description": "Renders a 360-degree turntable video preview for a given asset.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_id": {"type": "string"}},
                    "required": ["asset_id"],
                },
            },
        }


class find_build_run(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], commit_sha: str) -> str:
        pass
        build_runs = data.get("build_runs", [])
        for run in build_runs:
            if run.get("commit_sha") == commit_sha:
                payload = run
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Build run for commit {commit_sha} not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindBuildRun",
                "description": "Finds a build run by the commit SHA that triggered it.",
                "parameters": {
                    "type": "object",
                    "properties": {"commit_sha": {"type": "string"}},
                    "required": ["commit_sha"],
                },
            },
        }


class get_symbol_bundle_details(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], symbol_id: str) -> str:
        pass
        symbols = data.get("symbols", [])
        for s in symbols:
            if s.get("id") == symbol_id:
                payload = s
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Symbol bundle with id '{symbol_id}' not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetSymbolBundleDetails",
                "description": "Retrieves the details of a specific symbol bundle by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"symbol_id": {"type": "string"}},
                    "required": ["symbol_id"],
                },
            },
        }


class find_team_by_name(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str) -> str:
        pass
        teams = data.get("teams", [])
        for team in teams:
            if team.get("name") == name:
                payload = team
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Team with name '{name}' not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindTeamByName",
                "description": "Finds a team by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class run_git_bisect(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], failing_commit_sha: str, last_known_good_commit_sha: str
    ) -> str:
        pass
        bisect_results = data.get("bisect_results", [])
        for result in bisect_results:
            if (
                result.get("first_bad_commit") == failing_commit_sha
                and result.get("last_good_commit") == last_known_good_commit_sha
            ):
                payload = result
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Bisect result not found for the given commit range."}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "RunGitBisect",
                "description": "Performs a git bisect to find the commit that introduced a failure.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "failing_commit_sha": {"type": "string"},
                        "last_known_good_commit_sha": {"type": "string"},
                    },
                    "required": ["failing_commit_sha", "last_known_good_commit_sha"],
                },
            },
        }


class find_similar_incidents(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], issue_signature: str) -> str:
        pass
        incidents = data.get("incident_history", [])
        hits = [i for i in incidents if i.get("issue_signature") == issue_signature]
        payload = {"count": len(hits), "results": hits}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindSimilarIncidents",
                "description": "Finds past incidents with a similar issue signature.",
                "parameters": {
                    "type": "object",
                    "properties": {"issue_signature": {"type": "string"}},
                    "required": ["issue_signature"],
                },
            },
        }


class create_work_item(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        item_type: str,
        title: str,
        description: str,
    ) -> str:
        pass
        work_items = data.get("work_items", [])
        existing_ids = [item["id"] for item in work_items]
        new_id = _get_next_id("work", existing_ids)
        new_item = {
            "id": new_id,
            "project_id": project_id,
            "type": item_type,
            "title": title,
            "state": "open",
            "assignee_id": None,
            "created_at": FIXED_TIMESTAMP,
            "closed_at": None,
            "priority": "medium",
            "points": 5,
            "metadata": {"description": description},
        }
        work_items.append(new_item)
        data["work_items"] = work_items
        payload = {
                "success": f"Created {item_type} ticket '{new_id}'",
                "work_item_id": new_id,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateWorkItem",
                "description": "Creates a new work item (e.g., bug, task, story).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "item_type": {
                            "type": "string",
                            "enum": ["bug", "task", "story"],
                        },
                        "title": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "required": ["project_id", "item_type", "title", "description"],
                },
            },
        }


class get_work_item_details(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], work_item_id: str) -> str:
        pass
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("id") == work_item_id:
                payload = item
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Work item '{work_item_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getWorkItemDetails",
                "description": "Retrieves the full details for a given work item.",
                "parameters": {
                    "type": "object",
                    "properties": {"work_item_id": {"type": "string"}},
                    "required": ["work_item_id"],
                },
            },
        }


class find_translation_by_key_and_locale(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], string_key: str, locale: str) -> str:
        pass
        translations = data.get("translations", [])
        for t in translations:
            if t.get("string_key") == string_key and t.get("locale") == locale:
                payload = t
                out = json.dumps(payload, indent=2)
                return out
        payload = {
                "error": f"Translation for key '{string_key}' and locale '{locale}' not found"
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindTranslationByKeyAndLocale",
                "description": "Finds a translation record by its string key and locale.",
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


class create_tms_job(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        job_name: str,
        source_locale: str,
        target_locales: list[str],
        string_keys: list[str],
    ) -> str:
        pass
        tms_jobs = data.get("tms_jobs", [])
        existing_ids = [job["id"] for job in tms_jobs]
        new_id = _get_next_id("tms_job", existing_ids)

        new_job = {
            "id": new_id,
            "tms_project_id": project_id,
            "job_name": job_name,
            "job_type": "translation",
            "status": "pending",
            "created_at": FIXED_TIMESTAMP,
            "started_at": None,
            "completed_at": None,
            "total_segments": len(string_keys) * len(target_locales),
            "completed_segments": 0,
            "assigned_translators": [],
            "assigned_reviewers": [],
            "source_locale": source_locale,
            "target_locales": target_locales,
            "priority": "medium",
            "due_date": None,
            "metadata": {"string_keys": string_keys},
        }

        tms_jobs.append(new_job)
        data["tms_jobs"] = tms_jobs
        payload = {"success": f"Created TMS job '{new_id}'.", "tms_job_id": new_id}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateTmsJob",
                "description": "Creates a new job in the Translation Management System (TMS).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "job_name": {"type": "string"},
                        "source_locale": {"type": "string"},
                        "target_locales": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "string_keys": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "project_id",
                        "job_name",
                        "source_locale",
                        "target_locales",
                        "string_keys",
                    ],
                },
            },
        }


class get_tms_job_details(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tms_job_id: str) -> str:
        pass
        tms_jobs = data.get("tms_jobs", [])
        for job in tms_jobs:
            if job.get("id") == tms_job_id:
                payload = job
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"TMS job with id '{tms_job_id}' not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getTmsJobDetails",
                "description": "Retrieves the full details for a given TMS job.",
                "parameters": {
                    "type": "object",
                    "properties": {"tms_job_id": {"type": "string"}},
                    "required": ["tms_job_id"],
                },
            },
        }


class find_newly_added_loc_strings(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str, hours_ago: int) -> str:
        pass
        from datetime import datetime, timedelta

        loc_strings = data.get("loc_strings", [])
        now = datetime.fromisoformat(FIXED_TIMESTAMP.replace("Z", "+00:00"))
        time_threshold = now - timedelta(hours=hours_ago)

        new_strings = []
        for s in loc_strings:
            if s.get("project_id") == project_id:
                try:
                    created_at_dt = datetime.fromisoformat(
                        s["created_at"].replace("Z", "+00:00")
                    )
                    if created_at_dt >= time_threshold:
                        new_strings.append(s)
                except (ValueError, TypeError, KeyError):
                    continue
        payload = {"count": len(new_strings), "results": new_strings}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "findNewlyAddedLocStrings",
                "description": "Finds all localization strings for a given project that were created within a specified time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "hours_ago": {"type": "integer"},
                    },
                    "required": ["project_id", "hours_ago"],
                },
            },
        }


class post_slack_message(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], channel: str, message: str) -> str:
        pass
        payload = {"success": f"Message posted to channel '{channel}'."}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "PostSlackMessage",
                "description": "Posts a message to a specified Slack channel.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["channel", "message"],
                },
            },
        }


class create_compliance_record(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        compliance_type: str,
        requirement: str,
        status: str,
        details: str,
        assignee_id: str,
    ) -> str:
        pass
        compliance_records = data.get("compliance", [])
        existing_ids = [item["id"] for item in compliance_records]
        new_id = _get_next_id("compliance", existing_ids)

        new_record = {
            "id": new_id,
            "project_id": project_id,
            "compliance_type": compliance_type,
            "requirement": requirement,
            "status": status,
            "details": details,
            "due_date": None,
            "assigned_to": assignee_id,
            "created_at": FIXED_TIMESTAMP,
        }

        compliance_records.append(new_record)
        data["compliance"] = compliance_records
        payload = {
                "success": f"Created compliance record '{new_id}'.",
                "compliance_id": new_id,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateComplianceRecord",
                "description": "Creates a new compliance record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "compliance_type": {"type": "string"},
                        "requirement": {"type": "string"},
                        "status": {"type": "string"},
                        "details": {"type": "string"},
                        "assignee_id": {"type": "string"},
                    },
                    "required": [
                        "project_id",
                        "compliance_type",
                        "requirement",
                        "status",
                        "details",
                        "assignee_id",
                    ],
                },
            },
        }


class find_project_by_name(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str) -> str:
        pass
        projects = data.get("projects", [])
        for project in projects:
            if project.get("name") == name:
                payload = project
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Project with name '{name}' not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "findProjectByName",
                "description": "Finds a project by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class create_notification_record(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message: str) -> str:
        pass
        notifications = data.get("notifications", [])
        existing_ids = [n["id"] for n in notifications]
        new_id = _get_next_id("notification", existing_ids)
        new_notification = {
            "id": new_id,
            "message": message,
            "created_at": FIXED_TIMESTAMP,
            "status": "unread",
        }
        notifications.append(new_notification)
        data["notifications"] = notifications
        payload = {
                "success": f"Created notification record '{new_id}'.",
                "notification_id": new_id,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateNotificationRecord",
                "description": "Creates a new notification record.",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }


class list_tms_jobs(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        pass
        tms_jobs = data.get("tms_jobs", [])
        payload = {"count": len(tms_jobs), "results": tms_jobs}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListTmsJobs",
                "description": "Retrieves a list of all jobs in the Translation Management System (TMS).",
                "parameters": {"type": "object", "properties": {}},
            },
        }


TOOLS = [
    get_crash_event_details(),
    find_work_item_by_crash_fingerprint(),
    get_code_owner_for_module(),
    update_work_item(),
    link_work_items(),
    find_build_run(),
    run_git_bisect(),
    create_work_item(),
    find_similar_incidents(),
    get_symbol_bundle_details(),
    find_team_by_name(),
    get_work_item_details(),
    find_translation_by_key_and_locale(),
    create_tms_job(),
    get_tms_job_details(),
    find_newly_added_loc_strings(),
    post_slack_message(),
    create_compliance_record(),
    find_project_by_name(),
    create_notification_record(),
    list_tms_jobs(),
]
