# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MergeBranch(Tool):
    """
    Replace the target branch's file list with the source branch's file list (source snapshot wins).
    - Inputs: owner, repo_name, source_branch_name, target_branch_name
    - Behavior:
        * Validates repo and branch existence; rejects self-merge.
        * Sets target branch files/contents to EXACT copies of source branch files/contents.
          (Any previous files on the target branch are discarded.)
        * If target is the default branch, mirrors to repo-level file_paths/file_contents.
        * Assigns a new deterministic SHA to the target branch (via get_next_branch_sha(data)).
        * Updates repo['updated_ts'] via get_current_updated_timestamp().
        * Appends a terminal log entry via add_terminal_message(data, msg, timestamp).
    - Deterministic and idempotent for repeated runs on unchanged source.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], owner, repo_name, reponame, source_branch_name, target_branch_name) -> str:
        owner = (owner or "").strip()
        repo_name = (repo_name or reponame or "").strip()
        source_branch_name = (source_branch_name or "").strip()
        target_branch_name = (target_branch_name or "").strip()

        if not owner or not repo_name or not source_branch_name or not target_branch_name:
            return json.dumps(
                {"error": "Required: owner, repo_name, source_branch_name, target_branch_name."},
                indent=2
            )
        if source_branch_name == target_branch_name:
            return json.dumps(
                {"error": "source_branch_name and target_branch_name must differ."},
                indent=2
            )

        # Load the repositories database
        repos: List[Dict[str, Any]] = list(data.get("repositories", {}).values())
        if not isinstance(repos, list):
            return json.dumps({"error": "Invalid database: 'repositories' must be a list."}, indent=2)

        # Find the repository.
        repo = next((r for r in repos if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if repo is None:
            return json.dumps({"error": f"Repository '{owner}/{repo_name}' not found."}, indent=2)

        branches: List[str] = repo.get("branches", [])
        if source_branch_name not in branches:
            return json.dumps({"error": f"Source branch '{source_branch_name}' not found."}, indent=2)
        if target_branch_name not in branches:
            return json.dumps({"error": f"Target branch '{target_branch_name}' not found."}, indent=2)

        src_idx = branches.index(source_branch_name)
        tgt_idx = branches.index(target_branch_name)

        # Verify that per-branch arrays exist and are appropriately padded.
        branch_files_all: List[List[str]] = repo.setdefault("branch_files", [])
        branch_contents_all: List[List[str]] = repo.setdefault("branch_contents", [])
        branch_shas: List[str] = repo.setdefault("branch_shas", [])

        while len(branch_files_all)    < len(branches): branch_files_all.append([])
        while len(branch_contents_all) < len(branches): branch_contents_all.append([])
        while len(branch_shas)        < len(branches): branch_shas.append("")

        # Original snapshot
        src_files = list(branch_files_all[src_idx])
        src_contents_full = list(branch_contents_all[src_idx])
        # Standardize content size relative to the number of files.
        normalized_src_contents: List[str] = []
        for i, _path in enumerate(src_files):
            normalized_src_contents.append(src_contents_full[i] if i < len(src_contents_full) else "")

        # Substitute target with source snapshot.
        branch_files_all[tgt_idx] = list(src_files)
        branch_contents_all[tgt_idx] = list(normalized_src_contents)

        # If the target is the default branch, synchronize with repository-level files.
        default_branch = repo.get("default_branch", "main")
        if target_branch_name == default_branch:
            repo["file_paths"] = list(src_files)
            repo["file_contents"] = list(normalized_src_contents)

        # Fixed timestamp and updated target SHA
        new_ts = get_current_updated_timestamp()
        repo["updated_ts"] = new_ts

        new_target_sha = get_next_merge_sha(data)  # "branch_sha_number_<N>"

        branch_shas[tgt_idx] = new_target_sha

        # Command line output
        add_terminal_message(
            data,
            f"Merged '{source_branch_name}' into '{target_branch_name}' for {owner}/{repo_name} with SHA {new_target_sha}.",
            new_ts
        )

        return json.dumps(
            {
                "success": f"Merged '{source_branch_name}' into '{target_branch_name}' for {owner}/{repo_name} with SHA {new_target_sha}.",
                "repo": f"{owner}/{repo_name}",
                "source_branch": source_branch_name,
                "target_branch": target_branch_name,
                "target_branch_file_count": len(src_files),
                "target_branch_sha": new_target_sha,
                "updated_ts": new_ts
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "merge_branch",
                "description": "Replace target branch files/contents with a snapshot of source (source snapshot wins); mirrors to repo-level if target is default; assigns new deterministic SHA to target; updates repo updated_ts; logs a terminal entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias: reponame)."},
                        "source_branch_name": {"type": "string", "description": "Branch to copy FROM."},
                        "target_branch_name": {"type": "string", "description": "Branch to replace (copy INTO)."}
                    },
                    "required": ["owner", "repo_name", "source_branch_name", "target_branch_name"]
                }
            }
        }
