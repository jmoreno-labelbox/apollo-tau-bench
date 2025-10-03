from tau_bench.envs.tool import Tool
import json
from typing import Any

class InitialCommit(Tool):
    """
    Adds a new commit entry to the commits DB for owner/repo_name/branch_name.
    - Creates the repo record if missing.
    - Creates the branch bucket if missing.
    - Uses deterministic commit SHA ('commit_sha_<total>') and timestamp (max(existing)+1min).
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str = "",
        repo_name: str = "",
        branch_name: str = "",
        commit_message: str = "",
        commit_author: str = ""
    ) -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        branch_name = branch_name.strip()
        commit_message = commit_message.strip()
        commit_author = commit_author.strip()

        if (
            not owner
            or not repo_name
            or not branch_name
            or not commit_message
            or not commit_author
        ):
            payload = {
                "error": "Parameters 'owner', 'repo_name', 'branch_name', 'commit_message', and 'commit_author' are required."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Load commits DB (supports either {"commits": [...]} or a top-level list)
        commits_db = data.get("commits", [])
        if isinstance(commits_db, list):
            pass
        elif isinstance(data, list):
            commits_db = data
        else:
            payload = {
                "error": "Invalid database format: expected a list or a dict with 'commits'."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Find or create the repo record
        rec = next(
            (
                r
                for r in commits_db
                if r.get("owner") == owner and r.get("repo_name") == repo_name
            ),
            None,
        )
        if rec is None:
            rec = {
                "owner": owner,
                "repo_name": repo_name,
                "branch_names": [],
                "commit_shas": [],
                "commit_messages": [],
                "commit_authors": [],
                "commit_timestamps": [],
            }
            commits_db.append(rec)

        branch_names: list[str] = rec.get("branch_names", [])
        commit_shas: list[list[str]] = rec.get("commit_shas", [])
        commit_messages: list[list[str]] = rec.get("commit_messages", [])
        commit_authors: list[list[str]] = rec.get("commit_authors", [])
        commit_timestamps: list[list[str]] = rec.get("commit_timestamps", [])

        # Ensure branch exists and arrays are aligned
        if branch_name not in branch_names:
            branch_names.append(branch_name)
            commit_shas.append([])
            commit_messages.append([])
            commit_authors.append([])
            commit_timestamps.append([])

        idx = branch_names.index(branch_name)

        # Deterministic commit fields
        new_sha = get_next_commit_sha(data)
        new_ts = get_current_timestamp()

        # Append new commit
        commit_shas[idx].append(new_sha)
        commit_messages[idx].append(commit_message)
        commit_authors[idx].append(commit_author)
        commit_timestamps[idx].append(new_ts)

        # Write back (in case keys were missing initially)
        rec["branch_names"] = branch_names
        rec["commit_shas"] = commit_shas
        rec["commit_messages"] = commit_messages
        rec["commit_authors"] = commit_authors
        rec["commit_timestamps"] = commit_timestamps

        add_terminal_message(
            data,
            f"Initial commit added to {owner}/{repo_name}@{branch_name}.",
            get_current_timestamp(),
        )
        payload = {
            "success": f"Initial commit added to {owner}/{repo_name}@{branch_name}.",
            "commit": {
                "sha": new_sha,
                "message": commit_message,
                "author": commit_author,
                "timestamp": new_ts,
            },
            "branch_commit_count": len(commit_shas[idx]),
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InitialCommit",
                "description": "Add a new commit to commits DB (creates repo/branch buckets if needed) with deterministic SHA and timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "Repository owner (account/team).",
                        },
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name.",
                        },
                        "branch_name": {
                            "type": "string",
                            "description": "Branch name to commit to.",
                        },
                        "commit_message": {
                            "type": "string",
                            "description": "Commit message.",
                        },
                        "commit_author": {
                            "type": "string",
                            "description": "Author username for the commit.",
                        },
                    },
                    "required": [
                        "owner",
                        "repo_name",
                        "branch_name",
                        "commit_message",
                        "commit_author",
                    ],
                },
            },
        }
