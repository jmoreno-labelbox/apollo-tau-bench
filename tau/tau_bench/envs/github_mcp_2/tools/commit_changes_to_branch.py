# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CommitChangesToBranch(Tool):
    """Commits changes to a branch with a message (generates SHA and metadata)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        branch = kwargs.get("branch")
        commit_message = kwargs.get("commit_message")

        if not all([repo_name, branch, commit_message]):
            return json.dumps({"error": "repo_name, branch, and commit_message are required."}, indent=2)

        try:
            repo = _find_repo_record(data, repo_name)
            idx = _branch_index(repo, branch)

            new_sha = get_next_commit_sha()
            repo["branch_shas"][idx] = new_sha

            commits = _commits(data)
            me = _auth(data)["username"]

            commit_block = next((c for c in commits if c["owner"] == me and c["repo_name"] == repo_name), None)
            if not commit_block:
                commit_block = {
                    "owner": me,
                    "repo_name": repo_name,
                    "branch_names": [],
                    "commit_shas": [],
                    "commit_messages": [],
                    "commit_authors": [],
                    "commit_timestamps": [],
                }
                commits.append(commit_block)

            if branch not in commit_block["branch_names"]:
                commit_block["branch_names"].append(branch)
                commit_block["commit_shas"].append([new_sha])
                commit_block["commit_messages"].append([commit_message])
                commit_block["commit_authors"].append([me])
                commit_block["commit_timestamps"].append([get_current_timestamp()])
            else:
                bidx = commit_block["branch_names"].index(branch)
                commit_block["commit_shas"][bidx].append(new_sha)
                commit_block["commit_messages"][bidx].append(commit_message)
                commit_block["commit_authors"][bidx].append(me)
                commit_block["commit_timestamps"][bidx].append(get_current_timestamp())

            return json.dumps({
                "message": "Committed to branch",
                "repo": repo_name,
                "branch": branch,
                "commit_sha": new_sha,
                "commit_message": commit_message
            }, indent=2)

        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "commit_changes_to_branch",
                "description": "Commits all current changes to a branch with the given message.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "commit_message": {"type": "string"}
                    },
                    "required": ["repo_name", "branch", "commit_message"]
                }
            }
        }
