from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class MakeCommit(Tool):
    """
    Append a new commit to an existing commits entry for (owner/repo_name/branch_name).
    - Errors if repo or branch bucket doesn't exist (use InitialCommit first).
    - Deterministic commit SHA ('commit_sha_<total>') and timestamp (max(existing)+1min).
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
            out = json.dumps(payload)
            return out

        # Load commits DB (prefer dict["commits"], fallback to top-level list)
        commits_db = None
        if isinstance(data, dict):
            commits_db = _convert_db_to_list(data.get("commits", {}).values())
        elif isinstance(data, list):
            commits_db = data
        else:
            payload = {"error": "Invalid database format for commits."}
            out = json.dumps(payload)
            return out

        if not isinstance(commits_db, list):
            payload = {"error": "Invalid commits store: expected a list."}
            out = json.dumps(payload)
            return out

        # Find existing repo record
        rec = next(
            (
                r
                for r in commits_db
                if r.get("owner") == owner and r.get("repo_name") == repo_name
            ),
            None,
        )
        if rec is None:
            payload = {
                "error": f"No commits entry for {owner}/{repo_name}. Use InitialCommit first."
            }
            out = json.dumps(payload)
            return out

        branch_names: list[str] = rec.get("branch_names", [])
        commit_shas: list[list[str]] = rec.get("commit_shas", [])
        commit_messages: list[list[str]] = rec.get("commit_messages", [])
        commit_authors: list[list[str]] = rec.get("commit_authors", [])
        commit_timestamps: list[list[str]] = rec.get("commit_timestamps", [])

        if branch_name not in branch_names:
            payload = {
                "error": f"No commit bucket for branch '{branch_name}' in {owner}/{repo_name}. Use InitialCommit first."
            }
            out = json.dumps(payload)
            return out

        idx = branch_names.index(branch_name)

        # Defensive alignment (ensure branch arrays exist)
        while len(commit_shas) <= idx:
            commit_shas.append([])
        while len(commit_messages) <= idx:
            commit_messages.append([])
        while len(commit_authors) <= idx:
            commit_authors.append([])
        while len(commit_timestamps) <= idx:
            commit_timestamps.append([])

        # Deterministic fields
        new_sha = get_next_commit_sha(data)  # <- called
        new_ts = get_current_updated_timestamp()

        # Append commit
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
            data, f"Commit added to {owner}/{repo_name}@{branch_name}.", new_ts
        )
        payload = {
            "success": f"Commit added to {owner}/{repo_name}@{branch_name}.",
            "commit": {
                "sha": new_sha,
                "message": commit_message,
                "author": commit_author,
                "timestamp": new_ts,
            },
            "branch_commit_count": len(commit_shas[idx]),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MakeCommit",
                "description": "Append a new commit to an existing commits entry (owner/repo_name/branch_name) with deterministic SHA and timestamp.",
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
