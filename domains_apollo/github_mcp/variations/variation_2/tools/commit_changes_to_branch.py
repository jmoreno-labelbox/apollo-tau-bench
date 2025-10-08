from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class CommitChangesToBranch(Tool):
    """Commits modifications to a branch along with a message (produces SHA and metadata)."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None, commit_message: str = None) -> str:
        if not all([repo_name, branch, commit_message]):
            payload = {"error": "repo_name, branch, and commit_message are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        try:
            repo = _find_repo_record(data, repo_name)
            idx = _branch_index(repo, branch)

            new_sha = get_next_commit_sha()
            repo["branch_shas"][idx] = new_sha

            commits = _commits(data)
            me = _auth(data)["username"]

            commit_block = next(
                (
                    c
                    for c in commits
                    if c["owner"] == me and c["repo_name"] == repo_name
                ),
                None,
            )
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
            payload = {
                    "message": "Committed to branch",
                    "repo": repo_name,
                    "branch": branch,
                    "commit_sha": new_sha,
                    "commit_message": commit_message,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        except Exception as e:
            payload = {"error": str(e)}
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CommitChangesToBranch",
                "description": "Commits all current changes to a branch with the given message.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "commit_message": {"type": "string"},
                    },
                    "required": ["repo_name", "branch", "commit_message"],
                },
            },
        }
