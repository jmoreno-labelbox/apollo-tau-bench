import json
from collections import Counter, defaultdict
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def _terminal(data: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    return data.setdefault("terminal", [])


def _branch_index(repo: dict[str, Any], branch: str | None) -> int:
    """
    Associate a branch name with the appropriate index for branch_files/branch_contents.
    If the branch is None, revert to repo['default_branch'].
    """
    pass
    branches = repo.get("branches") or []
    if not branches:
        #Certain repositories might only include default branch files in file_paths; consider that as index 0.
        return 0
    target = branch or repo.get("default_branch")
    if target in branches:
        return branches.index(target)
    #If the caller provided an incorrect branch, raise an error (according to RULES).
    raise Exception(
        f"Branch '{target}' not found in repository '{repo.get('repo_name')}'."
    )


def _issues(data: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    return data.setdefault("issues", [])


def get_next_alert_number() -> int:
    pass
    return 1


def get_next_branch_name(purpose: str) -> str:
    pass
    purpose = (purpose or "change").strip().lower().replace(" ", "-")
    return f"feature-{purpose}"


def _alerts(data: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    return data.setdefault("code_scanning_alerts", [])


#Predictable ID/Number generators (database resets occur between tasks)
def get_next_pr_number() -> int:
    pass
    return 1


def get_next_commit_sha() -> str:
    pass
    #Predictable placeholder SHA-like string
    return "sha_0000000000000000000000000000000000000000"


def _repos(data: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    return data.setdefault("repositories", [])


def get_current_timestamp() -> str:
    pass
    #Static timestamp to ensure runs are predictable
    return "2025-08-21T12:00:00Z"


def get_next_issue_number() -> int:
    pass
    return 1


def _resolve_pr_number(data: dict[str, Any], repo_name: str, pr_number: Any) -> int:
    """
    Determine the PR number, managing placeholder strings by locating the most recently created PR.
    Returns the actual PR number as an integer.
    """
    pass
    #If it is a placeholder string or any non-integer, locate the most recent PR
    if not isinstance(pr_number, int) or str(pr_number) == "{{PR_NUMBER}}":
        me = _auth(data)["username"]
        prs = data.get("pull_requests") or []
        block = next(
            (
                b
                for b in prs.values() if b.get("owner") == me and b.get("repo_name") == repo_name
            ),
            None,
        )
        if not block or not block["pr_numbers"]:
            raise Exception("No pull requests found for this repository")
        #Utilize the most recently created PR (the last one in the list)
        return block["pr_numbers"][-1]
    else:
        #Provide the actual number (expected to be an integer)
        return int(pr_number)


def _find_repo_record(data: dict[str, Any], repo_name: str) -> dict[str, Any]:
    """
    Locate a repository owned by the acting user. repositories is a LIST in our dataset,
    so iterate through it; do NOT utilize dict.get.
    """
    pass
    me = _auth(data)["username"]
    repos = data.get("repositories") or []
    for r in repos.values():
        if r.get("owner") == me and r.get("repo_name") == repo_name:
            return r
    #Reflect RULES: if not located, present a clear error (no alternatives)
    raise Exception(f"Repository not found for owner '{me}': {repo_name}")


def _prs(data: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    return data.setdefault("pull_requests", [])


def _auth(data: dict[str, Any]) -> dict[str, Any]:
    """
    Provide the acting identity as {"username": "...", "email": "..."}.
    Requires get_me(username=...) to have populated data["_me"].
    """
    pass
    me = data.get("_me")
    if isinstance(me, dict) and "username" in me:
        return me
    raise Exception("No acting identity set. Call get_me(username=...) first.")


def _commits(data: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    return data.setdefault("commits", [])


class GetRepository(Tool):
    """Provides information about a repository based on its name, irrespective of the owner."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, name: Any = None) -> str:
        if not repo_name:
            payload = {"error": "repo_name is required."}
            out = json.dumps(payload, indent=2)
            return out

        try:
            # Examine all repositories in the dataset, not solely those owned by the authenticated user
            for repo in _repos(data):
                if repo.get("repo_name") == repo_name:
                    payload = repo
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Repository not found: {repo_name}"}
            out = json.dumps(payload, indent=2)
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
                "name": "GetRepository",
                "description": "Returns details about a repository by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {
                            "type": "string",
                            "description": "The name of the repository",
                        },
                    },
                    "required": ["repo_name"],
                },
            },
        }


class GetDefaultBranch(Tool):
    """Delivers the default branch of a specified repository owned by the acting user."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None) -> str:
        if not repo_name:
            payload = {"error": "repo_name is required."}
            out = json.dumps(payload, indent=2)
            return out

        try:
            repo = _find_repo_record(data, repo_name)
            payload = {"default_branch": repo.get("default_branch")}
            out = json.dumps(payload, indent=2)
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
                "name": "GetDefaultBranch",
                "description": "Returns the default branch name of a given repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                    },
                    "required": ["repo_name"],
                },
            },
        }


class CreateBranch(Tool):
    """Establishes a new branch based on an existing branch within the repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, source_branch: str = None, new_branch: str = None) -> str:
        if not all([repo_name, source_branch, new_branch]):
            payload = {"error": "repo_name, source_branch, and new_branch are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        try:
            repo = _find_repo_record(data, repo_name)
            if new_branch in repo.get("branches", []):
                payload = {"error": f"Branch '{new_branch}' already exists."}
                out = json.dumps(
                    payload, indent=2
                )
                return out

            idx = _branch_index(repo, source_branch)
            repo.setdefault("branches", []).append(new_branch)
            repo.setdefault("branch_files", []).append(list(repo["branch_files"][idx]))
            repo.setdefault("branch_contents", []).append(
                list(repo["branch_contents"][idx])
            )
            repo.setdefault("branch_shas", []).append(get_next_commit_sha())
            payload = {
                    "message": "Branch created",
                    "new_branch": new_branch,
                    "from": source_branch,
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
                "name": "CreateBranch",
                "description": "Creates a new branch from an existing one in the repo.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "source_branch": {"type": "string"},
                        "new_branch": {"type": "string"},
                    },
                    "required": ["repo_name", "source_branch", "new_branch"],
                },
            },
        }


class WriteFileToBranch(Tool):
    """Inserts or modifies a file in a branch (without committing)."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None, path: str = None, content: str = None,
    commit_message: Any = None,
    ) -> str:
        if not all([repo_name, branch, path, content]):
            payload = {"error": "repo_name, branch, path, and content are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        try:
            repo = _find_repo_record(data, repo_name)
            idx = _branch_index(repo, branch)

            files = repo["branch_files"][idx]
            contents = repo["branch_contents"][idx]

            if path in files:
                i = files.index(path)
                contents[i] = content
            else:
                files.append(path)
                contents.append(content)
            payload = {
                    "message": "File added or updated",
                    "repo": repo_name,
                    "branch": branch,
                    "path": path,
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
                "name": "WriteFileToBranch",
                "description": "Adds or updates a file in the given branch (without committing).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "path": {"type": "string"},
                        "content": {"type": "string"},
                    },
                    "required": ["repo_name", "branch", "path", "content"],
                },
            },
        }


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


class ListRepositoriesSortedByLastUpdated(Tool):
    """Provides all repositories owned by the acting user, ordered by the most recent update time (in descending order)."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _auth(data)["username"]
        repos = sorted(
            [r for r in _repos(data) if r.get("owner") == me],
            key=lambda r: r.get("last_updated", ""),
            reverse=True,
        )
        payload = [
            {"repo_name": r["repo_name"], "last_updated": r.get("last_updated")}
            for r in repos.values()
        ]
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listRepositoriesSortedByLastUpdated",
                "description": "Returns repositories owned by the current user, sorted by last_updated.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class AggregateRepositoryActivity(Tool):
    """Delivers an activity summary for each repository owned by the acting user — including counts of PRs, issues, alerts, and commits."""
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _auth(data)["username"]
        repos = [r for r in _repos(data) if r.get("owner") == me]
        repo_names = [r["repo_name"] for r in repos.values()]

        prs = _prs(data)
        issues = _issues(data)
        alerts = _alerts(data)
        commits = _commits(data)

        summary = []
        for repo_name in repo_names:
            pr_count = sum(
                1
                for pr in prs.values() if pr.get("owner") == me and pr.get("repo_name") == repo_name
            )
            issue_count = sum(
                1
                for i in issues
                if i.get("owner") == me and i.get("repo_name") == repo_name
            )
            alert_count = sum(1 for a in alerts if a.get("repo_name") == repo_name)
            commit_block = next(
                (
                    c
                    for c in commits
                    if c["owner"] == me and c["repo_name"] == repo_name
                ),
                None,
            )
            commit_count = (
                sum(len(c) for c in commit_block["commit_shas"]) if commit_block else 0
            )

            summary.append(
                {
                    "repo_name": repo_name,
                    "prs": pr_count,
                    "issues": issue_count,
                    "alerts": alert_count,
                    "commits": commit_count,
                }
            )
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "aggregateRepoActivity",
                "description": "Returns counts of PRs, issues, alerts, and commits per repository owned by current user.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class ListPullRequests(Tool):
    """Enumerates pull requests for a particular repository or for all repositories."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None) -> str:
        pass
        _auth(data)["username"]

        result = []
        for pr in _prs(data):
            if repo_name and pr["repo_name"] != repo_name:
                continue
            result.extend(
                [
                    {
                        "owner": pr["owner"],
                        "repo_name": pr["repo_name"],
                        "pr_number": number,
                        "title": title,
                        "state": state,
                        "head_sha": head_sha,
                        "files": files,
                    }
                    for number, title, state, head_sha, files in zip(
                        pr["pr_numbers"],
                        pr["pr_titles"],
                        pr["pr_states"],
                        pr["head_shas"],
                        [x[0] for x in pr["pr_files"]],
                    )
                ]
            )
        payload = {"pull_requests": result}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListPullRequests",
                "description": "List all pull requests optionally filtered by repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {
                            "type": "string",
                            "description": "Optional name of the repository to filter PRs",
                        }
                    },
                    "required": [],
                },
            },
        }


class ListMergedPullRequestsWithFiles(Tool):
    """Provides merged PRs for a specified repository and owner, along with the changed files."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo_name: str = None) -> str:
        owner = owner or _auth(data)["username"]
        if not all([owner, repo_name]):
            payload = {"error": "owner and repo_name are required."}
            out = json.dumps(payload, indent=2)
            return out

        prs = _prs(data)
        merged = [
            {"number": pr["number"], "title": pr["title"], "files": pr.get("files", [])}
            for pr in prs.values() if pr.get("owner") == owner
            and pr.get("repo_name") == repo_name
            and pr.get("state") == "merged"
        ]
        payload = merged
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listMergedPullRequestsWithFiles",
                "description": "Returns merged PRs for the given owner/repo with changed files.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo_name": {"type": "string"},
                    },
                    "required": ["owner", "repo_name"],
                },
            },
        }


class ListAlerts(Tool):
    """Delivers code scanning alerts for a specified repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None) -> str:
        if not repo_name:
            payload = {"error": "repo_name is required."}
            out = json.dumps(payload, indent=2)
            return out

        alerts = _alerts(data)
        filtered = [
            {
                "alert_number": a.get("alert_number"),
                "rule": a.get("rule"),
                "severity": a.get("severity"),
                "state": a.get("state"),
                "dismissed": a.get("dismissed", False),
            }
            for a in alerts
            if a.get("repo_name") == repo_name
        ]
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listAlerts",
                "description": "Returns code scanning alerts for a given repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class GetAlertSeverityDistribution(Tool):
    """Provides overall severity counts for all code scanning alerts."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        alerts = _alerts(data)
        counter = Counter(a.get("severity", "Unknown") for a in alerts.values())
        payload = dict(counter)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAlertSeverityDistribution",
                "description": "Returns global severity count distribution across all alerts.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class ListOpenAlerts(Tool):
    """Enumerates all active code-scanning alerts along with the repository, alert ID, and severity."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        alerts = _alerts(data)
        open_alerts = [
            {
                "repo_name": a.get("repo_name"),
                "alert_number": a.get("alert_number"),
                "severity": a.get("severity"),
            }
            for a in alerts
            if a.get("state") != "closed"
        ]
        payload = open_alerts
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listOpenAlerts",
                "description": "Returns open alerts across all repositories with ID and severity.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class GetCommitSummary(Tool):
    """Provides the count of commits for a specified repository and owner, categorized by branch."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo_name: str = None) -> str:
        owner = owner or _auth(data)["username"]
        if not all([owner, repo_name]):
            payload = {"error": "owner and repo_name are required."}
            out = json.dumps(payload, indent=2)
            return out

        commits = _commits(data)
        summary = {}

        for c in commits:
            if c.get("owner") == owner and c.get("repo_name") == repo_name:
                for branch, shas in zip(c["branch_names"], c["commit_shas"]):
                    summary[branch] = len(shas)
        payload = {"repo_name": repo_name, "commit_summary": summary}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCommitSummary",
                "description": "Returns commit summary per branch for a repo and owner.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo_name": {"type": "string"},
                    },
                    "required": ["owner", "repo_name"],
                },
            },
        }


class GetTopCommitAuthors(Tool):
    """Delivers the leading commit authors across all repositories globally."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        commits = _commits(data)
        counter = Counter()

        for c in commits:
            for author_list in c.get("commit_authors", []):
                counter.update(author_list)

        top_authors = counter.most_common(10)
        payload = [{"author": a, "commits": count} for a, count in top_authors]
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTopCommitAuthors",
                "description": "Returns top commit authors across all repositories.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class AnalyzeTerminalActivityTypes(Tool):
    """Provides the frequency of inferred terminal activity types (e.g., git, docker, pytest)"""

    DEFAULT_KEYWORDS = [
        "git",
        "docker",
        "kubectl",
        "pytest",
        "helm",
        "make",
        "terraform",
        "pip",
        "npm",
    ]

    @staticmethod
    def invoke(data: dict[str, Any], keywords: list[str] = None) -> str:
        if keywords is None:
            keywords = AnalyzeTerminalActivityTypes.DEFAULT_KEYWORDS
        logs = _terminal(data)

        counter = Counter()
        for entry in logs:
            msg = entry.get("message", "").lower()
            for keyword in keywords:
                if keyword in msg:
                    counter[keyword] += 1
        payload = dict(counter)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyzeTerminalActivityTypes",
                "description": "Returns frequency of terminal activity types using known or custom keywords.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keywords": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of keywords to count (e.g., git, docker)",
                        }
                    },
                },
            },
        }


class GetTerminalTimelineBounds(Tool):
    """Delivers the first and last printed_ts from the terminal log."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        logs = _terminal(data)
        timestamps = sorted(
            [entry.get("printed_ts") for entry in logs if entry.get("printed_ts")]
        )
        if not timestamps:
            payload = {"error": "No terminal entries with timestamps found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"first_timestamp": timestamps[0], "last_timestamp": timestamps[-1]}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTerminalTimelineBounds",
                "description": "Returns first and last terminal log timestamps.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class CountPublicPrivateRepos(Tool):
    """Provides the count of public and private repositories owned by the acting user."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _auth(data)["username"]
        repos = [r for r in _repos(data) if r.get("owner") == me]

        result = {"public": 0, "private": 0}
        for r in repos.values():
            vis = r.get("visibility")
            if vis == "public":
                result["public"] += 1
            elif vis == "private":
                result["private"] += 1
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "countPublicPrivateRepos",
                "description": "Returns counts of public and private repositories owned by the user.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class FindReposWithDocsFolder(Tool):
    """Delivers repositories that have files located in the 'docs/' directory."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _auth(data)["username"]
        matches = []

        for r in _repos(data):
            if r.get("owner") != me:
                continue
            for file_list in r.get("branch_files", []):
                if any(f.startswith("docs/") for f in file_list.values()):
                    matches.append(r["repo_name"])
                    break
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "findReposWithDocsFolder",
                "description": "Finds repositories with files under 'docs/' folder.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class FindReposWithDockerCompose(Tool):
    """Provides repositories that include a 'docker-compose.yml' file in any branch."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _auth(data)["username"]
        results = []

        for r in _repos(data):
            if r.get("owner") != me:
                continue
            for files in r.get("branch_files", []):
                if "docker-compose.yml" in files:
                    results.append(r["repo_name"])
                    break
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "findReposWithDockerCompose",
                "description": "Finds repositories that contain 'docker-compose.yml'.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class FindReposWithKubernetesFolder(Tool):
    """Delivers repositories that have files within the 'kubernetes/' directory."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _auth(data)["username"]
        matched = []

        for r in _repos(data):
            if r.get("owner") != me:
                continue
            for file_list in r.get("branch_files", []):
                if any(f.startswith("kubernetes/") for f in file_list.values()):
                    matched.append(r["repo_name"])
                    break
        payload = matched
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "findReposWithKubernetesFolder",
                "description": "Finds repositories with files under 'kubernetes/' folder.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class ListAllMergedPullRequests(Tool):
    """Provides all merged PRs from all repositories owned by the acting user."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _auth(data)["username"]
        prs = [
            {
                "repo_name": pr["repo_name"],
                "number": pr["number"],
                "title": pr["title"],
                "state": pr["state"],
            }
            for pr in _prs(data)
            if pr.get("owner") == me and pr.get("state") == "merged"
        ]
        payload = prs
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "listAllMergedPullRequests",
                "description": "Returns all merged pull requests for repos owned by current user.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class ListIssuesByLabel(Tool):
    """Delivers all issues that possess a specific label (e.g., 'bug')"""

    @staticmethod
    def invoke(data: dict[str, Any], label: str = None,
    repo_name: Any = None,
    ) -> str:
        if not label:
            payload = {"error": "label is required."}
            out = json.dumps(payload, indent=2)
            return out

        issues = _issues(data)
        result = []

        for issue in issues:
            numbers = issue["issue_numbers"]
            labels_list = issue.get("labels", [])

            for idx, lbls in enumerate(labels_list):
                if label in lbls:
                    result.append(numbers[idx])
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListIssuesByLabel",
                "description": "Returns all issues containing the given label.",
                "parameters": {
                    "type": "object",
                    "properties": {"label": {"type": "string"}},
                    "required": ["label"],
                },
            },
        }


class GetAlertSummaryPerRepo(Tool):
    """Provides a summary of code scanning alerts (count and severity breakdown) for the specified repositories."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_names: list[str] = None, repo_name: Any = None) -> str:
        if not repo_names:
            payload = {"error": "repo_names is required."}
            out = json.dumps(payload, indent=2)
            return out

        alerts = _alerts(data)
        summary = defaultdict(lambda: {"total": 0, "severity_counts": defaultdict(int)})

        for a in alerts:
            repo = a.get("repo_name")
            if repo in repo_names:
                summary[repo]["total"] += 1
                sev = a.get("severity", "Unknown")
                summary[repo]["severity_counts"][sev] += 1

        # Transform nested defaultdicts into standard dictionaries
        clean_summary = {
            repo: {
                "total": val["total"],
                "severity_counts": dict(val["severity_counts"]),
            }
            for repo, val in summary.items()
        }
        payload = clean_summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getAlertSummaryPerRepo",
                "description": "Returns alert summary (total and by severity) for given repo list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_names": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["repo_names"],
                },
            },
        }


class GetBranchFileInventory(Tool):
    """Delivers the list of files and the latest SHA for a specified branch in a repository owned by the user."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None) -> str:
        if not all([repo_name, branch]):
            payload = {"error": "repo_name and branch are required."}
            out = json.dumps(payload, indent=2)
            return out

        try:
            repo = _find_repo_record(data, repo_name)
            idx = _branch_index(repo, branch)

            files = repo.get("branch_files", [])[idx]
            sha = repo.get("branch_shas", [])[idx]
            payload = {
                    "repo_name": repo_name,
                    "branch": branch,
                    "commit_sha": sha,
                    "files": files,
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
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getBranchFileInventory",
                "description": "Returns latest SHA and file list for a given repo and branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name", "branch"],
                },
            },
        }


class RenameRepository(Tool):
    """Changes the name of a repository owned by the acting user."""

    @staticmethod
    def invoke(data: dict[str, Any], old_name: str = None, new_name: str = None) -> str:
        me = _auth(data)["username"]

        if not all([old_name, new_name]):
            payload = {"error": "old_name and new_name are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        repos = _repos(data)
        for r in repos.values():
            if r.get("owner") == me and r.get("repo_name") == old_name:
                r["repo_name"] = new_name
                payload = {"message": "Repository renamed", "new_name": new_name}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Repository '{old_name}' not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "RenameRepository",
                "description": "Renames an existing repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "old_name": {"type": "string"},
                        "new_name": {"type": "string"},
                    },
                    "required": ["old_name", "new_name"],
                },
            },
        }


class SetRepositoryVisibility(Tool):
    """Modifies the visibility status of a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, visibility: str = None) -> str:
        _auth(data)["username"]

        if not all([repo_name, visibility]):
            payload = {"error": "repo_name and visibility are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        repo = _find_repo_record(data, repo_name)
        if visibility not in ["public", "private"]:
            payload = {"error": "Invalid visibility. Must be 'public' or 'private'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repo["visibility"] = visibility
        payload = {
                "message": "Visibility updated",
                "repo_name": repo_name,
                "visibility": visibility,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SetRepositoryVisibility",
                "description": "Updates visibility of a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "visibility": {"type": "string", "enum": ["public", "private"]},
                    },
                    "required": ["repo_name", "visibility"],
                },
            },
        }


class ListBranches(Tool):
    """Enumerates all branches within a specified repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None) -> str:
        if not repo_name:
            payload = {"error": "repo_name is required."}
            out = json.dumps(payload, indent=2)
            return out

        try:
            for repo in _repos(data):
                if repo.get("repo_name") == repo_name:
                    payload = {"branches": repo.get("branches", [])}
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Repository not found: {repo_name}"}
            out = json.dumps(payload, indent=2)
            return out
        except Exception as e:
            payload = {"error": str(e)}
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListBranches",
                "description": "Returns all branches in the given repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class GetPullRequest(Tool):
    """Provides information about a particular pull request."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, pr_number: int = None) -> str:
        if not all([repo_name, pr_number]):
            payload = {"error": "repo_name and pr_number are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        me = _auth(data)["username"]
        for pr in _prs(data):
            if pr["owner"] == me and pr["repo_name"] == repo_name:
                if pr_number in pr["pr_numbers"]:
                    idx = pr["pr_numbers"].index(pr_number)
                    single_pr = {
                        "repo_name": pr["repo_name"],
                        "pr_number": pr_number,
                        "title": pr["pr_titles"][idx],
                        "body": pr["pr_bodies"][idx],
                        "state": pr["pr_states"][idx],
                        "head_branch": pr["head_branches"][idx],
                        "base_branch": pr["base_branches"][idx],
                        "head_sha": pr["head_shas"][idx],
                        "mergeable": pr["mergeable_flags"][idx],
                        "merged": pr["merged_flags"][idx],
                        "files": pr["pr_files"][idx],
                        "comments": pr["pr_comments"][idx],
                        "comment_users": pr["pr_comment_users"][idx],
                        "reviewers": pr["reviewers"][idx],
                        "review_states": pr["review_states"][idx],
                        "review_events": pr["review_events"][idx],
                        "created_ts": pr["created_ts"][idx],
                        "updated_ts": pr["updated_ts"][idx],
                    }
                    payload = single_pr
                    out = json.dumps(payload, indent=2)
                    return out
        payload = {"error": "Pull request not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetPullRequest",
                "description": "Returns details of a specific pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                    },
                    "required": ["repo_name"],
                },
            },
        }


class GetIssue(Tool):
    """Delivers information regarding a specific issue."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, issue_number: int = None) -> str:
        if not all([repo_name, issue_number]):
            payload = {"error": "repo_name and issue_number are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        for issue in _issues(data):
            #print("ISUEEE: ", issue)

            #✅ Scenario 1: flat dictionary containing a single issue
            if issue.get("repo_name") == repo_name and issue.get("number") == int(
                issue_number
            ):
                payload = issue
                out = json.dumps(payload, indent=2)
                return out

            #✅ Scenario 2: batched structure for issues
            if issue.get("repo_name") == repo_name and int(issue_number) in (
                issue.get("issue_numbers") or []
            ):
                idx = issue["issue_numbers"].index(int(issue_number))
                payload = {
                        "repo_name": repo_name,
                        "number": int(issue_number),
                        "title": issue["issue_titles"][idx],
                        "body": issue["issue_bodies"][idx],
                        "state": issue["issue_states"][idx],
                        "labels": issue["labels"][idx],
                        "assignees": issue["assignees"][idx],
                        "comments": issue["issue_comments"][idx],
                        "comment_users": issue["issue_comment_users"][idx],
                        "created_ts": issue["created_ts"][idx],
                        "updated_ts": issue["updated_ts"][idx],
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": "Issue not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetIssue",
                "description": "Returns details of a specific issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "issue_number"],
                },
            },
        }


class CreateIssue(Tool):
    """Generates a new issue within a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, title: str, body: str = "", labels: list = []) -> str:
        if not all([repo_name, title]):
            payload = {"error": "repo_name and title are required."}
            out = json.dumps(payload, indent=2)
            return out

        number = get_next_issue_number()
        me = _auth(data)["username"]

        issue = {
            "repo_name": repo_name,
            "number": number,
            "title": title,
            "body": body,
            "labels": labels,
            "state": "open",
            "creator": me,
            "comments": [],
        }
        #print("issue:", issue)

        _issues(data).append(issue)
        payload = {"message": "Issue created", "number": number}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateIssue",
                "description": "Creates a new issue in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                        "labels": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["repo_name", "title"],
                },
            },
        }


class UpdateIssue(Tool):
    """Modifies the fields of an issue. Accommodates both aggregated blocks and flat issue rows."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        repo_name: str = None,
        issue_number: int = None,
        state: str = None,
        updates: str = None,
        title: str = None,
        body: str = None,
        labels: list = None
    ) -> str:
        # Allow either `state` or legacy `updates` for compatibility
        new_state = state or updates
        new_title = title
        new_body = body
        new_labels = labels  # substitute the complete label list if supplied

        if not repo_name or issue_number is None:
            payload = {"error": "repo_name and issue_number are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        target = int(issue_number)

        # 1) Aggregated blocks (shape of the original dataset)
        for block in _issues(data):
            if block.get("repo_name") != repo_name:
                continue

            nums = block.get("issue_numbers")
            if isinstance(nums, list) and target in nums:
                idx = nums.index(target)

                # Verify that parallel arrays are present and sufficiently long, then update them in place
                def _ensure_len(lst, fill, n):
                    if lst is None or not isinstance(lst, list):
                        lst = []
                    if len(lst) < n:
                        lst += [fill] * (n - len(lst))
                    return lst

                n = len(nums)

                if new_state is not None:
                    states = _ensure_len(block.get("issue_states"), "open", n)
                    states[idx] = new_state
                    block["issue_states"] = states

                if new_title is not None:
                    titles = _ensure_len(block.get("issue_titles"), "", n)
                    titles[idx] = new_title
                    block["issue_titles"] = titles

                if new_body is not None:
                    bodies = _ensure_len(block.get("issue_bodies"), "", n)
                    bodies[idx] = new_body
                    block["issue_bodies"] = bodies

                if new_labels is not None:
                    labels = _ensure_len(block.get("labels"), [], n)
                    labels[idx] = list(new_labels)
                    block["labels"] = labels

                # Update updated_ts if it exists
                if "updated_ts" in block and isinstance(block["updated_ts"], list):
                    from datetime import datetime, timezone

                    iso = (
                        datetime.now(timezone.utc)
                        .isoformat(timespec="seconds")
                        .replace("+00:00", "Z")
                    )
                    uts = _ensure_len(block.get("updated_ts"), iso, n)
                    uts[idx] = iso
                    block["updated_ts"] = uts
                payload = {
                    "message": "Issue updated",
                    "number": target,
                    "state": (new_state or block.get("issue_states", [None])[idx]),
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

        # 2) Flat rows (generated by CreateIssue)
        for row in _issues(data):
            if row.get("repo_name") == repo_name and row.get("number") == target:
                if new_state is not None:
                    row["state"] = new_state
                if new_title is not None:
                    row["title"] = new_title
                if new_body is not None:
                    row["body"] = new_body
                if new_labels is not None:
                    row["labels"] = list(new_labels)
                payload = {
                    "message": "Issue updated",
                    "number": target,
                    "state": row.get("state"),
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": "Issue not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateIssue",
                "description": "Updates an issue's fields (state/title/body/labels).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"},
                        "state": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                        "labels": {"type": "array", "items": {"type": "string"}},
                        "updates": {"type": "string"},  #historical alias for state
                    },
                    "required": ["repo_name", "issue_number"],
                },
            },
        }


class AddIssueComment(Tool):
    """Inserts a comment into an issue. Supports both aggregated blocks and flat issue rows."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, issue_number: int = None, comment: str = "") -> str:
        if not all([repo_name, issue_number is not None, comment is not None]):
            payload = {"error": "repo_name, issue_number, and comment are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        target = int(issue_number)
        me = _auth(data)["username"]  #maintain consistency with CreateIssue

        #1) Aggregated blocks (original dataset structure)
        for block in _issues(data):
            if block.get("repo_name") != repo_name:
                continue

            nums = block.get("issue_numbers")
            if isinstance(nums, list) and target in nums:
                idx = nums.index(target)

                #Confirm that parallel lists are present and sufficiently lengthy
                if "issue_comments" not in block or not isinstance(
                    block["issue_comments"], list
                ):
                    block["issue_comments"] = [[] for _ in nums]
                while len(block["issue_comments"]) < len(nums):
                    block["issue_comments"].append([])

                block["issue_comments"][idx].append(comment)

                #Optionally monitor the comment user if the structure is available
                if "issue_comment_users" in block and isinstance(
                    block["issue_comment_users"], list
                ):
                    while len(block["issue_comment_users"]) < len(nums):
                        block["issue_comment_users"].append([])
                    block["issue_comment_users"][idx].append(me)

                #Refresh updated_ts if it exists (maintains dataset consistency)
                if "updated_ts" in block and isinstance(block["updated_ts"], list):
                    from datetime import datetime, timezone

                    iso = (
                        datetime.now(timezone.utc)
                        .isoformat(timespec="seconds")
                        .replace("+00:00", "Z")
                    )
                    if len(block["updated_ts"]) < len(nums):
                        block["updated_ts"] += [iso] * (
                            len(nums) - len(block["updated_ts"])
                        )
                    block["updated_ts"][idx] = iso
                payload = {"message": "Comment added."}
                out = json.dumps(payload, indent=2)
                return out

        #2) Flat issue rows (produced by CreateIssue)
        for row in _issues(data):
            if row.get("repo_name") == repo_name and row.get("number") == target:
                comments = row.get("comments")
                if not isinstance(comments, list):
                    comments = []
                comments.append(comment)
                row["comments"] = comments
                payload = {"message": "Comment added."}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Issue not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddIssueComment",
                "description": "Adds a comment to an issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"},
                        "comment": {"type": "string"},
                    },
                    "required": ["repo_name", "issue_number", "comment"],
                },
            },
        }


class MergePullRequest(Tool):
    """Integrates the specified pull request into its base branch."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, pr_number: int = None) -> str:
        if not all([repo_name, pr_number]):
            payload = {"error": "repo_name and pr_number are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        me = _auth(data)["username"]
        pr = next(
            (
                p
                for p in _prs(data)
                if p["owner"] == me
                and p["repo_name"] == repo_name
                and int(pr_number) in p["pr_numbers"]
            ),
            None,
        )
        if not pr:
            payload = {"error": "Pull request not found."}
            out = json.dumps(payload, indent=2)
            return out

        try:
            idx = pr["pr_numbers"].index(int(pr_number))
        except ValueError:
            payload = {"error": "PR number not found in PR block."}
            out = json.dumps(payload, indent=2)
            return out

        #✅ Confirm that the PR is open before proceeding
        if pr["pr_states"][idx] != "open":
            payload = {"error": "PR is not open."}
            out = json.dumps(payload, indent=2)
            return out

        #✅ Prohibit merging when head equals base (no-operation merges)
        head_branch = pr["head_branches"][idx]
        base_branch = pr["base_branches"][idx]
        if head_branch == base_branch:
            pr["pr_states"][idx] = "rejected"
            payload = {
                    "message": "Pull request rejected.",
                    "reason": "head and base branch are the same",
                    "merged": "false",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repo = _find_repo_record(data, repo_name)
        head_idx = _branch_index(repo, head_branch)
        base_idx = _branch_index(repo, base_branch)

        #Merge means substituting base branch content with head branch content
        repo["branch_files"][base_idx] = list(repo["branch_files"][head_idx])
        repo["branch_contents"][base_idx] = list(repo["branch_contents"][head_idx])
        repo["branch_shas"][base_idx] = get_next_commit_sha()

        pr["pr_states"][idx] = "merged"
        payload = {
                "message": "Pull request merged.",
                "merged": "true",
                "merge_method": "merge",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "MergePullRequest",
                "description": "Merges the pull request into base branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "pr_number"],
                },
            },
        }


class CommentOnPullRequest(Tool):
    """Inserts a human comment into the discussion thread of the pull request."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, pr_number: int = None, comment: str = None) -> str:
        if not all([repo_name, pr_number, comment]):
            payload = {"error": "repo_name, pr_number and comment are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        me = _auth(data)["username"]
        pr = next(
            (
                p
                for p in _prs(data)
                if p["owner"] == me
                and p["repo_name"] == repo_name
                and int(pr_number) in p["pr_numbers"]
            ),
            None,
        )

        if not pr:
            payload = {"error": "Pull request not found."}
            out = json.dumps(payload, indent=2)
            return out

        pr.setdefault("comments", []).append(
            {"author": me, "comment": comment, "timestamp": get_current_timestamp()}
        )
        payload = {"message": "Comment added to pull request."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CommentOnPullRequest",
                "description": "Adds a comment to a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "comment": {"type": "string"},
                    },
                    "required": ["repo_name", "pr_number", "comment"],
                },
            },
        }


class CreatePullRequestReview(Tool):
    """Incorporates a review (approval, requested changes, or merely a comment) into a pull request."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, pr_number: int = None, review_decision: str = None, comment: str = "",
    body: Any = None,
    ) -> str:
        if not all([repo_name, pr_number, review_decision]):
            payload = {"error": "repo_name, pr_number, and review_decision are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if review_decision not in ["approve", "request_changes", "comment"]:
            payload = {
                    "error": "Invalid review_decision (must be 'approve' or 'request_changes' or 'comment)."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        me = _auth(data)["username"]
        pr = next(
            (
                p
                for p in _prs(data)
                if p["owner"] == me
                and p["repo_name"] == repo_name
                and int(pr_number) in p["pr_numbers"]
            ),
            None,
        )

        if not pr:
            payload = {"error": "Pull request not found."}
            out = json.dumps(payload, indent=2)
            return out

        pr.setdefault("reviews", []).append(
            {
                "author": me,
                "decision": review_decision,
                "comment": comment,
                "timestamp": get_current_timestamp(),
            }
        )
        payload = {"message": "Review submitted."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreatePullRequestReview",
                "description": "Adds a review (approve or request_changes or comment) to a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "review_decision": {
                            "type": "string",
                            "enum": ["approve", "request_changes", "comment"],
                        },
                        "comment": {"type": "string"},
                    },
                    "required": ["repo_name", "pr_number", "review_decision"],
                },
            },
        }


class RequestPullRequestReviewers(Tool):
    """Solicits one or more reviewers for a pull request."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, pr_number: str = None, reviewers: list[str] = None) -> str:
        if reviewers is None:
            reviewers = []

        if (
            not all([repo_name, pr_number])
            or not isinstance(reviewers, list)
            or len(reviewers) == 0
        ):
            payload = {
                    "error": "repo_name, pr_number and non-empty reviewers[] are required."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        me = _auth(data)["username"]

        #locate PR owned by the current user (aligned with your other tools)
        pr = next(
            (
                p
                for p in _prs(data)
                if p["owner"] == me
                and p["repo_name"] == repo_name
                and int(pr_number) in p["pr_numbers"]
            ),
            None,
        )
        if not pr:
            payload = {"error": "Pull request not found."}
            out = json.dumps(payload, indent=2)
            return out

        #Include reviewers
        existing = set(pr.get("requested_reviewers", []))
        for r in reviewers:
            if r != me:
                existing.add(r)
        pr["requested_reviewers"] = sorted(existing)
        payload = {
                "message": "Reviewers requested.",
                "pr_number": pr_number,
                "requested_reviewers": pr["requested_reviewers"],
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "RequestPullRequestReviewers",
                "description": "Request reviewers on a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "reviewers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Usernames to request for review",
                        },
                    },
                    "required": ["repo_name", "pr_number", "reviewers"],
                },
            },
        }


class AddLabelToIssue(Tool):
    """Attaches a label to the specified issue. Accommodates both aggregated and flat issue formats."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, issue_number: int = None, label: str = None) -> str:
        if not all([repo_name, issue_number, label]):
            payload = {"error": "repo_name, issue_number, and label are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        target = int(issue_number)

        #1) Facilitate aggregated blocks (original dataset structure)
        for block in _issues(data):
            if block.get("repo_name") != repo_name:
                continue
            if "issue_numbers" in block and "labels" in block:
                issue_numbers = block["issue_numbers"]
                if target in issue_numbers:
                    idx = issue_numbers.index(target)
                    labels_at_idx = list(set(block["labels"][idx] + [label]))
                    block["labels"][idx] = labels_at_idx
                    payload = {"message": f"Label '{label}' added."}
                    out = json.dumps(payload, indent=2)
                    return out

        #2) Facilitate flat rows (generated by CreateIssue)
        for row in _issues(data):
            if row.get("repo_name") == repo_name and row.get("number") == target:
                cur = set(row.get("labels", []))
                cur.add(label)
                row["labels"] = list(cur)
                payload = {"message": f"Label '{label}' added."}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Issue not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddLabelToIssue",
                "description": "Adds a label to an issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"},
                        "label": {"type": "string"},
                    },
                    "required": ["repo_name", "issue_number", "label"],
                },
            },
        }


class CreateRelease(Tool):
    """Generates a release for a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, tag: str, body: str = "", title: str = "",
    name: Any = None,
    ) -> str:
        if not all([repo_name, tag]):
            payload = {"error": "repo_name and tag are required."}
            out = json.dumps(payload, indent=2)
            return out

        repo = _find_repo_record(data, repo_name)
        repo.setdefault("releases", []).append(
            {
                "tag_name": tag,
                "body": body,
                "created_by": _auth(data)["username"],
                "created_at": get_current_timestamp(),
            }
        )
        payload = {
                "message": "Release created.",
                "repo_name": repo_name,
                "tag_name": tag,
                "title": title,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateRelease",
                "description": "Creates a new release (tag + body).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "tag": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                    },
                    "required": ["repo_name", "tag"],
                },
            },
        }


class GetLatestRelease(Tool):
    """Provides the most recent release (sorted by timestamp) for a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None) -> str:
        if not repo_name:
            payload = {"error": "repo_name is required."}
            out = json.dumps(payload, indent=2)
            return out

        repo = _find_repo_record(data, repo_name)
        releases = repo.get("releases", [])
        if not releases:
            payload = {"error": "No releases found."}
            out = json.dumps(payload, indent=2)
            return out

        latest = sorted(releases, key=lambda r: r["created_at"], reverse=True)[0]
        payload = latest
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetLatestRelease",
                "description": "Gets the latest release for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class ListRepoTopics(Tool):
    """Enumerates all topics associated with a specified repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None) -> str:
        repo = _find_repo_record(data, repo_name)
        payload = {"topics": repo.get("topics", [])}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListRepoTopics",
                "description": "Returns the list of repository topics.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class AddRepoTopic(Tool):
    """Attaches a topic to a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, topic: str = None) -> str:
        repo = _find_repo_record(data, repo_name)
        if not topic:
            payload = {"error": "topic is required."}
            out = json.dumps(payload, indent=2)
            return out

        topics = set(repo.get("topics", []))
        topics.add(topic)
        repo["topics"] = list(topics)
        payload = {"message": f"Topic '{topic}' added."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddRepoTopic",
                "description": "Adds a topic to a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "topic": {"type": "string"},
                    },
                    "required": ["repo_name", "topic"],
                },
            },
        }


class RemoveRepoTopic(Tool):
    """Detaches a topic from a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, topic: str = None) -> str:
        repo = _find_repo_record(data, repo_name)
        if not topic:
            payload = {"error": "topic is required."}
            out = json.dumps(payload, indent=2)
            return out

        repo["topics"] = [t for t in repo.get("topics", []) if t != topic]
        payload = {"message": f"Topic '{topic}' removed."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "RemoveRepoTopic",
                "description": "Removes a topic from a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "topic": {"type": "string"},
                    },
                    "required": ["repo_name", "topic"],
                },
            },
        }


class GetBranchProtection(Tool):
    """Retrieves protection settings for a specific branch."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None) -> str:
        repo = _find_repo_record(data, repo_name)
        idx = _branch_index(repo, branch)
        if "branch_protections" not in repo:
            repo["branch_protections"] = [False] * len(repo.get("branches", []))

        # Set up if absent
        if "branch_protection_rules" not in repo:
            repo["branch_protection_rules"] = {}

        protection = repo.get("branch_protections", [{}])[idx]
        rules = repo.get("branch_protection_rules", {}).values()[idx]
        payload = {"protected": protection if protection else "false", "rules": rules}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetBranchProtection",
                "description": "Gets branch protection rules for a given branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name", "branch"],
                },
            },
        }


class SetBranchProtection(Tool):
    """Establishes branch protection rules for a specified branch."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None, protected: bool = None, rules: dict = None) -> str:
        repo = _find_repo_record(data, repo_name)
        idx = _branch_index(repo, branch)
        protection = protected

        # Set up if absent
        if "branch_protections" not in repo:
            repo["branch_protections"] = [False] * len(repo.get("branches", []))
        repo["branch_protections"][idx] = protection

        # Set up if absent
        if "branch_protection_rules" not in repo:
            repo["branch_protection_rules"] = {}

        repo["branch_protection_rules"][idx] = rules
        payload = {
            "message": (
                "Branch protection enabled."
                if protection
                else "Branch protection disabled."
            ),
            "repo_name": repo["repo_name"],
            "branch": branch,
            "protected": protection if protection else "false",
            "rules": rules,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SetBranchProtection",
                "description": "Sets protection rules for a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "protected": {"type": "string"},
                        "rules": {
                            "type": "object",
                            "description": "Protection rule dictionary",
                        },
                    },
                    "required": ["repo_name", "branch", "rules", "protected"],
                },
            },
        }


class SearchRepositories(Tool):
    """Looks for repositories using a name substring or owner."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = "", owner: str = "") -> str:
        name_query = name.lower()
        owner_query = owner.lower()
        results = []

        for repo in _repos(data):
            if (name_query and name_query in repo.get("repo_name", "").lower()) or (
                owner_query and owner_query in repo.get("owner", "").lower()
            ):
                results.append(repo)
        payload = {"results": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchRepositories",
                "description": "Search repositories by name or owner substring.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "owner": {"type": "string"},
                    },
                },
            },
        }


class ListCommits(Tool):
    """Enumerates commits for a specified repository and optional branch."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None) -> str:
        commits = _commits(data)

        for entry in commits:
            if entry["repo_name"] == repo_name:
                if not branch:
                    payload = entry
                    out = json.dumps(payload, indent=2)
                    return out

                if branch in entry["branch_names"]:
                    idx = entry["branch_names"].index(branch)
                    payload = {
                        "branch": branch,
                        "commit_shas": entry["commit_shas"][idx],
                        "messages": entry["commit_messages"][idx],
                        "authors": entry["commit_authors"][idx],
                        "timestamps": entry["commit_timestamps"][idx],
                    }
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out
        payload = {
            "branch": branch,
            "commit_shas": [],
            "messages": [],
            "authors": [],
            "timestamps": [],
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListCommits",
                "description": "Lists commits in a repository and branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name"],
                },
            },
        }


class SearchIssues(Tool):
    """Looks for issues based on title, label, or body keyword."""

    @staticmethod
    def invoke(data: dict[str, Any], query: str = "") -> str:
        query = query.lower()
        results = []

        for issue in _issues(data):
            #print("ISWEU::", issue)
            title = issue.get("title", "").lower()
            body = issue.get("body", "").lower()
            raw_labels = issue.get("labels", [])
            flat_labels = [
                l
                for sub in raw_labels
                for l in (sub if isinstance(sub, list) else [sub])
            ]
            labels = [l.lower() for l in flat_labels]

            if query in title or query in body or query in labels:
                results.append(issue.get("number"))
        payload = {"results": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchIssues",
                "description": "Search issues by keyword in title, body, or labels.",
                "parameters": {
                    "type": "object",
                    "properties": {"query": {"type": "string"}},
                    "required": ["query"],
                },
            },
        }


class ListRepositories(Tool):
    """Enumerates all repositories that belong to the current user."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _auth(data)["username"]
        owned = [r for r in _repos(data) if r["owner"] == me]
        payload = {"repositories": owned}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListRepositories",
                "description": "Returns all repositories owned by the current user.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class ListFiles(Tool):
    """Enumerates all file paths within the specified branch of a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None) -> str:
        if not repo_name:
            payload = {"error": "repo_name is required."}
            out = json.dumps(payload, indent=2)
            return out

        repo = _find_repo_record(data, repo_name)
        idx = _branch_index(repo, branch)
        files = repo["branch_files"][idx]
        payload = {"files": files}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListFiles",
                "description": "Lists all files in a given branch of a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name", "branch"],
                },
            },
        }


class CreateRepository(Tool):
    """Generates a new repository that is owned by the current user."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, visibility: str = "public", default_branch: str = "main") -> str:
        if not repo_name:
            payload = {"error": "repo_name is required."}
            out = json.dumps(payload, indent=2)
            return out

        me = _auth(data)["username"]

        repos = _repos(data)
        if any(r["owner"] == me and r["repo_name"] == repo_name for r in repos.values()):
            payload = {"error": "Repository already exists."}
            out = json.dumps(payload, indent=2)
            return out

        new_repo = {
            "owner": me,
            "repo_name": repo_name,
            "visibility": visibility,
            "default_branch": default_branch,
            "branches": [default_branch],
            "branch_files": [[]],
            "branch_contents": [[]],
            "branch_shas": [get_next_commit_sha()],
            "branch_protections": [{}],
            "topics": [],
            "releases": [],
        }
        data["repositories"][new_repo["repositorie_id"]] = new_repo
        payload = {"message": "Repository created", "repo_name": repo_name}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateRepository",
                "description": "Creates a new repository for the current user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "visibility": {"type": "string"},
                        "default_branch": {"type": "string"},
                    },
                    "required": ["repo_name"],
                },
            },
        }


class DeleteBranch(Tool):
    """Removes a branch from a repository, excluding the default branch (deduplicated)."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None) -> str:
        if not all([repo_name, branch]):
            payload = {"error": "repo_name and branch are required."}
            out = json.dumps(payload, indent=2)
            return out

        repo = _find_repo_record(data, repo_name)
        if branch == repo.get("default_branch"):
            payload = {"error": "Cannot delete the default branch."}
            out = json.dumps(payload, indent=2)
            return out

        if branch not in repo.get("branches", []):
            payload = {"error": "Branch not found."}
            out = json.dumps(payload, indent=2)
            return out

        idx = repo["branches"].index(branch)

        # Safely eliminate parallel entries
        for key in ["branches", "branch_files", "branch_contents", "branch_shas"]:
            if key in repo and len(repo[key]) > idx:
                repo[key].pop(idx)

        # Arrays that are optional
        if "branch_protections" in repo and len(repo["branch_protections"]) > idx:
            repo["branch_protections"].pop(idx)
        payload = {"message": f"Branch '{branch}' deleted from repo '{repo_name}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "DeleteBranch",
                "description": "Deletes a branch (except the default branch).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name", "branch"],
                },
            },
        }


class ListCodeScanningAlerts(Tool):
    """Enumerates all code scanning alerts for a specified repository and optional severity."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, severity: str = None) -> str:
        flat_alerts = []

        for record in _alerts(data):
            if repo_name and record.get("repo_name") != repo_name:
                continue

            for i, alert_number in enumerate(record.get("alert_numbers", [])):
                alert = {
                    "alert_number": alert_number,
                    "severity": record.get("severities", [])[i],
                    "state": record.get("states", [])[i],
                    "description": record.get("descriptions", [])[i],
                }

                if severity:
                    if alert["severity"].lower() != severity.lower():
                        continue

                flat_alerts.append(alert)
        payload = {"alerts": flat_alerts}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListCodeScanningAlerts",
                "description": "Lists all code scanning alerts optionally filtered by repository and severity.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "severity": {"type": "string"},
                    },
                },
            },
        }


class ListTerminalLastMessage(Tool):
    """Provides the most recent terminal log entry."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        terminal_log = _terminal(data)
        #print("terminal log:", terminal_log)
        if not terminal_log:
            payload = {"error": "No terminal messages found."}
            out = json.dumps(payload, indent=2)
            return out

        #Retrieve the last message from the latest log group
        last_ts = terminal_log[-1]["printed_ts"]
        #print("term_log::", terminal_log)
        last_item = terminal_log[-1]
        last_msg = (
            last_item.get("messages")[-1]
            if last_item.get("messages")
            else last_item.get("message")
        )
        print("last_msg:::", last_msg)
        payload = {"timestamp": last_ts, "message": last_msg}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListTerminalLastMessage",
                "description": "Returns terminal last log message with timestamp.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class GetHeadSha(Tool):
    """Delivers the SHA of the most recent commit on a specified branch."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None) -> str:
        if not repo_name:
            payload = {"error": "repo_name is required."}
            out = json.dumps(payload, indent=2)
            return out

        repo = _find_repo_record(data, repo_name)
        idx = _branch_index(repo, branch)
        payload = {"branch": repo["branches"][idx], "sha": repo["branch_shas"][idx]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetHeadSha",
                "description": "Gets the SHA of the head commit on a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name"],
                },
            },
        }


class AppendTerminal(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message: str = None) -> str:
        if not message:
            payload = {"error": "message is required."}
            out = json.dumps(payload, indent=2)
            return out
        entry = {"printed_ts": get_current_timestamp(), "message": str(message)}
        _terminal(data).append(entry)
        payload = entry
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "AppendTerminal",
                "description": "Appends a message to terminal log with timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }


class GetMe(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], username: str = None) -> str:
        existing = data.get("_me")
        if isinstance(existing, dict) and "username" in existing and not username:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out

        if username:
            auth_list = data.get("authentication") or []
            match = next((a for a in auth_list.values() if a.get("username") == username), None)
            if not match:
                payload = {"error": f"Unknown username: {username}"}
                out = json.dumps(payload, indent=2)
                return out
            me = {"username": match.get("username"), "email": match.get("email")}
            data["_me"] = me
            payload = me
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "No acting identity set. Provide username to get_me."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetMe",
                "description": "Gets/sets the acting identity.",
                "parameters": {
                    "type": "object",
                    "properties": {"username": {"type": "string"}},
                    "required": ["username"],
                },
            },
        }


class GetFileContents(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, path: str = None, branch: str = None) -> str:
        if not all([repo_name, path]):
            payload = {"error": "repo_name and path are required."}
            out = json.dumps(payload, indent=2)
            return out

        repo = _find_repo_record(data, repo_name)
        idx = _branch_index(repo, branch)
        files = repo["branch_files"][idx]
        #print("files:", files)
        contents = repo["branch_contents"][idx]
        #print("contents:", contents)

        if path not in files:
            payload = {"error": f"File '{path}' not found."}
            out = json.dumps(payload, indent=2)
            return out

        i = files.index(path)
        payload = {"path": path, "content": contents[i]}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetFileContents",
                "description": "Gets the contents of a file in a repository branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "path": {"type": "string"},
                    },
                    "required": ["repo_name", "path"],
                },
            },
        }


class CreatePullRequest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, title: str, head: str, base: str, body: str = "") -> str:
        me = _auth(data)["username"]
        repo = _find_repo_record(data, repo_name)
        #print("repo:", repo)

        #Verify that the pull request record is present
        pr_block = next(
            (
                b
                for b in _prs(data)
                if b.get("owner") == me and b.get("repo_name") == repo_name
            ),
            None,
        )
        if not pr_block:
            #✅ Generate PR block if it is absent
            pr_block = {
                "owner": me,
                "repo_name": repo_name,
                "pr_numbers": [],
                "pr_titles": [],
                "pr_bodies": [],
                "pr_states": [],
                "head_branches": [],
                "base_branches": [],
                "head_shas": [],
                "mergeable_flags": [],
                "merged_flags": [],
                "created_ts": [],
                "updated_ts": [],
                "pr_files": [],
                "pr_comments": [],
                "pr_comment_users": [],
                "reviewers": [],
                "review_states": [],
                "review_events": [],
            }
            _prs(data).append(pr_block)

        #Add PR metadata
        pr_number = 1
        pr_block["pr_numbers"].append(pr_number)
        pr_block["pr_titles"].append(title)
        pr_block["pr_bodies"].append(body)
        pr_block["pr_states"].append("open")
        pr_block["head_branches"].append(head)
        pr_block["base_branches"].append(base)
        pr_block["head_shas"].append("sha_0000000000000000000000000000000000000000")
        pr_block["mergeable_flags"].append(True)
        pr_block["merged_flags"].append(False)
        pr_block["created_ts"].append("2025-08-23T12:00:00Z")
        pr_block["updated_ts"].append("2025-08-23T12:00:00Z")

        #Identify modified files based on their names and content
        try:
            head_idx = repo["branches"].index(head)
            base_idx = repo["branches"].index(base)
        except ValueError:
            payload = {"error": "Invalid head or base branch."}
            out = json.dumps(payload, indent=2)
            return out

        head_files = set(repo["branch_files"][head_idx])
        base_files = set(repo["branch_files"][base_idx])
        file_diff = head_files.symmetric_difference(base_files)

        #Additionally verify for content alterations if filenames match
        if not file_diff:
            file_diff = set()
            for path in repo["branch_files"][head_idx]:
                if path in repo["branch_files"][base_idx]:
                    head_i = next(
                        (
                            i
                            for i, p in enumerate(repo["branch_files"][head_idx])
                            if p == path
                        ),
                        None,
                    )
                    base_i = next(
                        (
                            i
                            for i, p in enumerate(repo["branch_files"][base_idx])
                            if p == path
                        ),
                        None,
                    )

                    if head_i is not None and base_i is not None:
                        if (
                            repo["branch_contents"][head_idx][head_i]
                            != repo["branch_contents"][base_idx][base_i]
                        ):
                            file_diff.add(path)

                    if (
                        repo["branch_contents"][head_idx][head_i]
                        != repo["branch_contents"][base_idx][base_i]
                    ):
                        file_diff.add(path)

        changed_files = sorted(list(file_diff))

        #Add the list of changed files as a nested list (List[List[str]])
        if "pr_files" not in pr_block:
            pr_block["pr_files"] = []
        pr_block["pr_files"].append([changed_files])

        #Set up empty nested structures for comments/reviews if required
        pr_block.setdefault("pr_comments", []).append([[]])
        pr_block.setdefault("pr_comment_users", []).append([[]])
        pr_block.setdefault("reviewers", []).append([[]])
        pr_block.setdefault("review_states", []).append([[]])
        pr_block.setdefault("review_events", []).append([[]])
        payload = {
                "message": "Pull request opened",
                "title": title,
                "base": base,
                "head": head,
                "pr_number": pr_number,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreatePullRequest",
                "description": "Creates a pull request from head to base branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                        "base": {"type": "string"},
                        "head": {"type": "string"},
                    },
                    "required": ["repo_name", "title", "base", "head"],
                },
            },
        }


class ListPullRequestFiles(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, pr_number: int = None) -> str:
        pr_number = _resolve_pr_number(data, repo_name, pr_number)

        prs = _prs(data)
        pr_block = next((b for b in prs.values() if b.get("repo_name") == repo_name), None)

        if not pr_block:
            payload = {"error": "Pull request not found."}
            out = json.dumps(payload, indent=2)
            return out

        try:
            idx = pr_block["pr_numbers"].index(pr_number)
        except Exception:
            payload = {"files": []}
            out = json.dumps(payload, indent=2)
            return out

        try:
            pr_files = pr_block["pr_files"][idx][0]
            if pr_files:
                payload = {"files": pr_files}
                out = json.dumps(payload, indent=2)
                return out
        except Exception:
            pass  # fallback below

        # fallback to calculate the difference
        head_branch = pr_block["head_branches"][idx]
        base_branch = pr_block["base_branches"][idx]

        try:
            repo = next(r for r in _repos(data) if r["repo_name"] == repo_name)
            head_idx = _branch_index(repo, head_branch)
            base_idx = _branch_index(repo, base_branch)

            head_files = set(repo["branch_files"][head_idx])
            base_files = set(repo["branch_files"][base_idx])

            diff_files = list(head_files.symmetric_difference(base_files))
            if not diff_files:
                payload = {"error": "No file diff found in fallback."}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            payload = {"files": diff_files}
            out = json.dumps(payload, indent=2)
            return out
        except Exception as e:
            payload = {"error": f"No file diff recorded for this pull request. {str(e)}"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListPullRequestFiles",
                "description": "Lists files changed in pull request's head branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "pr_number"],
                },
            },
        }


class ListOpenPullRequests(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None) -> str:
        pass
        me = _auth(data)["username"]

        prs = _prs(data)
        for block in prs.values():
            #print("block:::", block)
            if block["owner"] == me and block["repo_name"] == repo_name:
                results = [
                    {"number": n, "title": t, "state": s, "base": b, "head": h}
                    for n, t, s, b, h in zip(
                        block["pr_numbers"],
                        block["pr_titles"],
                        block["pr_states"],
                        block["base_branches"],
                        block["head_branches"],
                    )
                    if s == "open"
                ]
                payload = {"pull_requests": results}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"pull_requests": []}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListOpenPullRequests",
                "description": "Lists all open pull requests in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }


class InitializePullRequestsBlock(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        me = _auth(data)["username"]
        existing = next(
            (
                pr
                for pr in _prs(data)
                if pr["owner"] == me and pr["repo_name"] == repo_name
            ),
            None,
        )
        if existing:
            payload = {"message": "PR block already exists"}
            out = json.dumps(payload)
            return out
        _prs(data).append(
            {
                "owner": me,
                "repo_name": repo_name,
                "pr_numbers": [],
                "pr_titles": [],
                "pr_bodies": [],
                "pr_states": [],
                "head_branches": [],
                "base_branches": [],
                "head_shas": [],
                "mergeable_flags": [],
                "merged_flags": [],
                "created_ts": [],
                "updated_ts": [],
                "pr_files": [],
            }
        )
        payload = {"message": "Initialized pull_requests block for repo."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "InitializePullRequestsBlock",
                "description": "Manually initializes a pull_requests entry for a new repo",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                    },
                    "required": ["repo_name"],
                },
            },
        }


TOOLS = [
    GetMe(),
    GetRepository(),
    GetDefaultBranch(),
    CreateBranch(),
    WriteFileToBranch(),
    CreatePullRequestReview(),
    CreatePullRequest(),
    CreateRepository(),
    DeleteBranch(),
    CommitChangesToBranch(),
    GetPullRequest(),
    CommentOnPullRequest(),
    MergePullRequest(),
    CreateIssue(),
    UpdateIssue(),
    AddIssueComment(),
    ListIssuesByLabel(),
    ListBranches(),
    RenameRepository(),
    ListRepoTopics(),
    AddRepoTopic(),
    GetBranchProtection(),
    SetBranchProtection(),
    ListPullRequests(),
    GetIssue(),
    AddLabelToIssue(),
    CreateRelease(),
    GetLatestRelease(),
    SearchRepositories(),
    ListCommits(),
    SearchIssues(),
    ListFiles(),
    GetHeadSha(),
    ListCodeScanningAlerts(),
    AppendTerminal(),
    GetFileContents(),
    ListPullRequestFiles(),
    ListOpenPullRequests(),
    InitializePullRequestsBlock(),
    ListTerminalLastMessage(),
    RequestPullRequestReviewers(),
    ListRepositories(),
    RemoveRepoTopic(),
    SetRepositoryVisibility(),
]
