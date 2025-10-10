# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MakeCommit(Tool):
    """
    Append a new commit to an existing commits entry for (owner/repo_name/branch_name).
    - Errors if repo or branch bucket doesn't exist (use InitialCommit first).
    - Deterministic commit SHA ('commit_sha_<total>') and timestamp (max(existing)+1min).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = kwargs.get("repo_name", "").strip()
        branch_name = kwargs.get("branch_name", "").strip()
        commit_message = kwargs.get("commit_message", "").strip()
        commit_author = kwargs.get("commit_author", "").strip()

        if not owner or not repo_name or not branch_name or not commit_message or not commit_author:
            return json.dumps({
                "error": "Parameters 'owner', 'repo_name', 'branch_name', 'commit_message', and 'commit_author' are required."
            })

        # Load commits database using dict["commits"], with a fallback to the top-level list.
        commits_db = None
        if isinstance(data, dict):
            commits_db = list(data.get("commits", {}).values())
        elif isinstance(data, list):
            commits_db = data
        else:
            return json.dumps({"error": "Invalid database format for commits."})

        if not isinstance(commits_db, list):
            return json.dumps({"error": "Invalid commits store: expected a list."})

        # Locate the current repository entry.
        rec = next((r for r in commits_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps({"error": f"No commits entry for {owner}/{repo_name}. Use InitialCommit first."})

        branch_names: List[str] = rec.get("branch_names", [])
        commit_shas: List[List[str]] = rec.get("commit_shas", [])
        commit_messages: List[List[str]] = rec.get("commit_messages", [])
        commit_authors: List[List[str]] = rec.get("commit_authors", [])
        commit_timestamps: List[List[str]] = rec.get("commit_timestamps", [])

        if branch_name not in branch_names:
            return json.dumps({"error": f"No commit bucket for branch '{branch_name}' in {owner}/{repo_name}. Use InitialCommit first."})

        idx = branch_names.index(branch_name)

        # Defensive setup (verify presence of branch arrays)
        while len(commit_shas) <= idx: commit_shas.append([])
        while len(commit_messages) <= idx: commit_messages.append([])
        while len(commit_authors) <= idx: commit_authors.append([])
        while len(commit_timestamps) <= idx: commit_timestamps.append([])

        # Predictable fields
        new_sha = get_next_commit_sha(data)         # <- invoked
        new_ts = get_current_updated_timestamp()

        # Add commit
        commit_shas[idx].append(new_sha)
        commit_messages[idx].append(commit_message)
        commit_authors[idx].append(commit_author)
        commit_timestamps[idx].append(new_ts)

        # Respond if any keys were initially absent.
        rec["branch_names"] = branch_names
        rec["commit_shas"] = commit_shas
        rec["commit_messages"] = commit_messages
        rec["commit_authors"] = commit_authors
        rec["commit_timestamps"] = commit_timestamps

        add_terminal_message(data, f"Commit added to {owner}/{repo_name}@{branch_name}.", new_ts)

        return json.dumps({
            "success": f"Commit added to {owner}/{repo_name}@{branch_name}.",
            "commit": {
                "sha": new_sha,
                "message": commit_message,
                "author": commit_author,
                "timestamp": new_ts
            },
            "branch_commit_count": len(commit_shas[idx])
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "make_commit",
                "description": "Append a new commit to an existing commits entry (owner/repo_name/branch_name) with deterministic SHA and timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner (account/team)."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "branch_name": {"type": "string", "description": "Branch name to commit to."},
                        "commit_message": {"type": "string", "description": "Commit message."},
                        "commit_author": {"type": "string", "description": "Author username for the commit."}
                    },
                    "required": ["owner", "repo_name", "branch_name", "commit_message", "commit_author"]
                }
            }
        }
