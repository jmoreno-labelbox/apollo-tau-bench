import json
from typing import Any

from domains.dto import Tool


def _actor_name(data: dict[str, Any]) -> str:
    pass
    auth = data.get("authentication") or [{}]
    return auth[0].get("username") or "anonymous"


DEFAULT_TS = "2025-08-21T12:00:00Z"


def _alerts(data: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    return data.setdefault("code_scanning_alerts", [])


def _find_repo(data: dict[str, Any], owner: str, repo: str) -> dict[str, Any] | None:
    pass
    for r in _repos(data):
        if r.get("owner") == owner and (r.get("repo_name") or r.get("name")) == repo:
            return r
    return None


def _issues(data: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    return data.setdefault("issues", [])


def _terminal(data: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    return data.setdefault("terminal", [])


def _prs(data: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    return data.setdefault("pull_requests", [])


def _commits(data: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    return data.setdefault("commits", [])


def _repos(data: dict[str, Any]) -> list[dict[str, Any]]:
    pass
    return data.setdefault("repositories", [])


def get_current_timestamp() -> str:
    """A fixed timestamp utilized for all creation and update operations."""
    pass
    return DEFAULT_TS


#tools


class WhoAmI(Tool):
    """Retrieve the active user based on authentication."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        auth = data.get("authentication") or [{}]
        user = auth[0]
        payload = {"username": user.get("username"), "email": user.get("email")}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "whoAmI",
                "description": "Return the authenticated username and email.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class ListRepos(Tool):
    """Display repositories that belong to the authenticated user."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _actor_name(data)
        items = [r for r in _repos(data) if r.get("owner") == me]
        payload = items
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listRepos",
                "description": "List repositories for the current user.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class CreateRepo(Tool):
    """Establish a repository with fundamental attributes."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, private: bool = False) -> str:
        me = _actor_name(data)
        if not name:
            raise RuntimeError("'name' is required")
        if _find_repo(data, me, name):
            raise RuntimeError("Repository already exists")
        repo = {
            "owner": me,
            "repo_name": name,
            "private": private,
            "default_branch": "main",
            "branches": ["main"],
            "created_at": get_current_timestamp(),
            "topics": [],
        }
        _repos(data).append(repo)
        payload = repo
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRepo",
                "description": "Create a repository for the current user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "private": {"type": "boolean"},
                    },
                    "required": ["name"],
                },
            },
        }


class DeleteRepo(Tool):
    """Remove a repository that you possess."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        me = _actor_name(data)
        if not name:
            raise RuntimeError("'name' is required")
        before = len(_repos(data))
        data["repositories"] = [
            r
            for r in _repos(data)
            if not (
                r.get("owner") == me and (r.get("repo_name") or r.get("name")) == name
            )
        ]
        payload = {"deleted": before - len(_repos(data))}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteRepo",
                "description": "Delete a repository by name (owned by you).",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class ListBranches(Tool):
    """Show branches associated with a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None) -> str:
        owner = owner or _actor_name(data)
        r = _find_repo(data, owner, repo)
        if not r:
            raise RuntimeError("Repository not found")
        payload = {"default": r.get("default_branch"), "branches": r.get("branches") or []}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListBranches",
                "description": "List branches in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                    },
                    "required": ["repo"],
                },
            },
        }


class CreateBranch(Tool):
    """Generate a new branch from the default one."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, branch: str = None) -> str:
        owner = owner or _actor_name(data)
        r = _find_repo(data, owner, repo)
        if not r:
            raise RuntimeError("Repository not found")
        if not branch:
            raise RuntimeError("'branch' is required")
        branches = r.setdefault("branches", [])
        if branch in branches:
            raise RuntimeError("Branch exists")
        branches.append(branch)
        payload = {"created": branch}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateBranch",
                "description": "Create a branch in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo", "branch"],
                },
            },
        }


class OpenIssue(Tool):
    """Initiate a new issue."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, title: str = None, body: str = "") -> str:
        owner = owner or _actor_name(data)
        if not (_find_repo(data, owner, repo)):
            raise RuntimeError("Repository not found")
        if not title:
            raise RuntimeError("'title' is required")
        seq = (
            sum(
                1
                for it in _issues(data)
                if it.get("owner") == owner and it.get("repo") == repo
            )
            + 1
        )
        issue = {
            "owner": owner,
            "repo": repo,
            "number": seq,
            "title": title,
            "body": body,
            "state": "open",
            "assignees": [],
            "labels": [],
            "comments": [],
            "created_at": get_current_timestamp(),
        }
        _issues(data).append(issue)
        payload = issue
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "OpenIssue",
                "description": "Create an issue in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                    },
                    "required": ["repo", "title"],
                },
            },
        }


class ListIssues(Tool):
    """Display issues for a repository with an optional state filter."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, state: str = None) -> str:
        owner = owner or _actor_name(data)
        result = [
            i
            for i in _issues(data)
            if i.get("owner") == owner and i.get("repo") == repo
        ]
        if state:
            result = [i for i in result if i.get("state") == state]
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListIssues",
                "description": "List issues in a repository (optionally by state).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "state": {"type": "string", "enum": ["open", "closed"]},
                    },
                    "required": ["repo"],
                },
            },
        }


class SetIssueState(Tool):
    """Either close or reactivate an issue."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, number: int = None, state: str = None) -> str:
        owner = owner or _actor_name(data)
        for i in _issues(data):
            if (
                i.get("owner") == owner
                and i.get("repo") == repo
                and i.get("number") == number
            ):
                i["state"] = state
                i["updated_at"] = get_current_timestamp()
                payload = i
                out = json.dumps(payload)
                return out
        raise RuntimeError("Issue not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setIssueState",
                "description": "Set issue state to open or closed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "state": {"type": "string", "enum": ["open", "closed"]},
                    },
                    "required": ["repo", "number", "state"],
                },
            },
        }


class CommentIssue(Tool):
    """Post a comment on an issue."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, number: int = None, comment: str = "") -> str:
        owner = owner or _actor_name(data)
        for i in _issues(data):
            if (
                i.get("owner") == owner
                and i.get("repo") == repo
                and i.get("number") == number
            ):
                i.setdefault("comments", []).append(
                    {
                        "author": _actor_name(data),
                        "message": comment,
                        "created_at": get_current_timestamp(),
                    }
                )
                payload = {"ok": True}
                out = json.dumps(payload)
                return out
        raise RuntimeError("Issue not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "commentIssue",
                "description": "Add a comment to an issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "comment": {"type": "string"},
                    },
                    "required": ["repo", "number", "comment"],
                },
            },
        }


class AddLabel(Tool):
    """Attach a label to an issue or pull request."""

    @staticmethod
    def invoke(data: dict[str, Any], kind: str = None, owner: str = None, repo: str = None, number: int = None, label: str = None) -> str:
        owner = owner or _actor_name(data)
        target_list = _issues(data) if kind == "issue" else _prs(data)
        for obj in target_list:
            if (
                obj.get("owner") == owner
                and obj.get("repo") == repo
                and obj.get("number") == number
            ):
                labels = obj.setdefault("labels", [])
                if label and label not in labels:
                    labels.append(label)
                payload = obj
                out = json.dumps(payload)
                return out
        raise RuntimeError("Target not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddLabel",
                "description": "Add a label to an issue or PR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kind": {"type": "string", "enum": ["issue", "pr"]},
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "label": {"type": "string"},
                    },
                    "required": ["kind", "repo", "number", "label"],
                },
            },
        }


class OpenPR(Tool):
    """Initiate a pull request."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str = None,
        repo: str = None,
        title: str = None,
        head_branch: str = None,
        base_branch: str = "main"
    ) -> str:
        owner = owner or _actor_name(data)
        if not (_find_repo(data, owner, repo)):
            raise RuntimeError("Repository not found")
        seq = (
            sum(
                1
                for pr in _prs(data)
                if pr.get("owner") == owner and pr.get("repo") == repo
            )
            + 1
        )
        pr = {
            "owner": owner,
            "repo": repo,
            "number": seq,
            "title": title or f"PR {seq}",
            "state": "open",
            "head": head_branch,
            "base": base_branch,
            "labels": [],
            "review_states": [],
            "created_at": get_current_timestamp(),
        }
        _prs(data).append(pr)
        payload = pr
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "OpenPr",
                "description": "Open a pull request with head and base branches.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "title": {"type": "string"},
                        "head_branch": {"type": "string"},
                        "base_branch": {"type": "string"},
                    },
                    "required": ["repo", "head_branch"],
                },
            },
        }


class ListPRs(Tool):
    """Show pull requests for a repository with an optional state filter."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, state: str = None) -> str:
        pass
        owner = owner or _actor_name(data)
        result = [
            p for p in _prs(data) if p.get("owner") == owner and p.get("repo") == repo
        ]
        if state:
            result = [p for p in result if p.get("state") == state]
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListPrs",
                "description": "List pull requests for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "state": {
                            "type": "string",
                            "enum": ["open", "closed", "merged"],
                        },
                    },
                    "required": ["repo"],
                },
            },
        }


class MergePR(Tool):
    """Combine a pull request by its number (marks it as merged)."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, number: int = None) -> str:
        owner = owner or _actor_name(data)
        for p in _prs(data):
            if (
                p.get("owner") == owner
                and p.get("repo") == repo
                and p.get("number") == number
            ):
                p["state"] = "merged"
                p["merged_at"] = get_current_timestamp()
                payload = p
                out = json.dumps(payload)
                return out
        raise RuntimeError("PR not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "mergePr",
                "description": "Mark a pull request as merged.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                    },
                    "required": ["repo", "number"],
                },
            },
        }


class SubmitReview(Tool):
    """Provide a review on a pull request (approve, request changes, or comment)."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, number: int = None, state: str = None, note: str = "") -> str:
        owner = owner or _actor_name(data)
        for p in _prs(data):
            if (
                p.get("owner") == owner
                and p.get("repo") == repo
                and p.get("number") == number
            ):
                p.setdefault("review_states", []).append(
                    {
                        "reviewer": _actor_name(data),
                        "state": state,
                        "note": note,
                        "created_at": get_current_timestamp(),
                    }
                )
                payload = {"ok": True}
                out = json.dumps(payload)
                return out
        raise RuntimeError("PR not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "submitReview",
                "description": "Submit a review on a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "state": {
                            "type": "string",
                            "enum": ["approve", "request_changes", "comment"],
                        },
                        "note": {"type": "string"},
                    },
                    "required": ["repo", "number", "state"],
                },
            },
        }


class AddCommit(Tool):
    """Log a commit on a branch (extremely lightweight)."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, branch: str = "main", message: str = "") -> str:
        owner = owner or _actor_name(data)
        if not (_find_repo(data, owner, repo)):
            raise RuntimeError("Repository not found")
        seq = (
            sum(
                1
                for c in _commits(data)
                if c.get("owner") == owner and c.get("repo") == repo
            )
            + 1
        )
        sha = f"{branch}-{seq:06d}"
        c = {
            "owner": owner,
            "repo": repo,
            "branch": branch,
            "sha": sha,
            "message": message,
            "author": _actor_name(data),
            "timestamp": get_current_timestamp(),
        }
        _commits(data).append(c)
        payload = c
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddCommit",
                "description": "Add a commit record to a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "branch": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["repo"],
                },
            },
        }


class ListCommits(Tool):
    """Display commits for a repository (with an optional branch filter)."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, branch: str = None) -> str:
        owner = owner or _actor_name(data)
        result = [
            c
            for c in _commits(data)
            if c.get("owner") == owner and c.get("repo") == repo
        ]
        if branch:
            result = [c for c in result if c.get("branch") == branch]
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listCommits",
                "description": "List commit records for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo"],
                },
            },
        }


class SearchWork(Tool):
    """Basic text search through issue and pull request titles."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, query: str = None) -> str:
        owner = owner or _actor_name(data)
        q = (query or "").lower()
        hits_issues = [
            i
            for i in _issues(data)
            if i.get("owner") == owner
            and i.get("repo") == repo
            and q in (i.get("title", "") + " " + i.get("body", "")).lower()
        ]
        hits_prs = [
            p
            for p in _prs(data)
            if p.get("owner") == owner
            and p.get("repo") == repo
            and q in (p.get("title", "") or "").lower()
        ]
        payload = {"issues": hits_issues, "pull_requests": hits_prs}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchWork",
                "description": "Search issues and PRs by text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "query": {"type": "string"},
                    },
                    "required": ["repo", "query"],
                },
            },
        }


class ListAlerts(Tool):
    """Show code scanning alerts for a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None) -> str:
        owner = owner or _actor_name(data)
        result = [
            a
            for a in _alerts(data)
            if a.get("owner") == owner and a.get("repo") == repo
        ]
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listAlerts",
                "description": "List static analysis / scanning alerts for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                    },
                    "required": ["repo"],
                },
            },
        }


class ResolveAlert(Tool):
    """Address a code scanning alert using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, alert_id: str = None) -> str:
        owner = owner or _actor_name(data)
        for a in _alerts(data):
            if (
                a.get("owner") == owner
                and a.get("repo") == repo
                and a.get("id") == alert_id
            ):
                a["state"] = "resolved"
                a["resolved_at"] = get_current_timestamp()
                payload = a
                out = json.dumps(payload)
                return out
        raise RuntimeError("Alert not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "resolveAlert",
                "description": "Mark a code scanning alert as resolved.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "alert_id": {"type": "string"},
                    },
                    "required": ["repo", "alert_id"],
                },
            },
        }


class ActivityFeed(Tool):
    """Provide a straightforward combined feed of recent issues, pull requests, and commits for a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, limit: int = 20) -> str:
        owner = owner or _actor_name(data)
        feed: list[dict[str, Any]] = []
        for i in _issues(data):
            if i.get("owner") == owner and i.get("repo") == repo:
                feed.append(
                    {
                        "type": "issue",
                        "title": i.get("title"),
                        "state": i.get("state"),
                        "ts": i.get("created_at"),
                    }
                )
        for p in _prs(data):
            if p.get("owner") == owner and p.get("repo") == repo:
                feed.append(
                    {
                        "type": "pr",
                        "title": p.get("title"),
                        "state": p.get("state"),
                        "ts": p.get("created_at"),
                    }
                )
        for c in _commits(data):
            if c.get("owner") == owner and c.get("repo") == repo:
                feed.append(
                    {
                        "type": "commit",
                        "title": c.get("message"),
                        "state": "n/a",
                        "ts": c.get("timestamp"),
                    }
                )
        feed.sort(key=lambda x: x.get("ts") or "", reverse=True)
        payload = feed[:limit]
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "activityFeed",
                "description": "Return a simple sorted feed of repo activity (issues/PRs/commits).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "limit": {"type": "integer"},
                    },
                    "required": ["repo"],
                },
            },
        }


class AppendTerminal(Tool):
    """Add a line to the terminal log stored in memory."""

    @staticmethod
    def invoke(data: dict[str, Any], line: str = "") -> str:
        cmd = line or ""
        _terminal(data).append({"line": cmd, "when": get_current_timestamp()})
        payload = {"ok": True}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "appendTerminal",
                "description": "Append a line to an in-memory terminal log.",
                "parameters": {
                    "type": "object",
                    "properties": {"line": {"type": "string"}},
                    "required": ["line"],
                },
            },
        }


class ListTerminal(Tool):
    """Display terminal log entries with the most recent ones first."""

    @staticmethod
    def invoke(data: dict[str, Any], limit: int = 50) -> str:
        logs = list(reversed(_terminal(data)))[:limit]
        payload = logs
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listTerminal",
                "description": "List recent terminal log entries.",
                "parameters": {
                    "type": "object",
                    "properties": {"limit": {"type": "integer"}},
                },
            },
        }


class AssignUser(Tool):
    """Designate a user for an issue or pull request."""

    @staticmethod
    def invoke(data: dict[str, Any], kind: str = None, owner: str = None, repo: str = None, number: int = None, username: str = None) -> str:
        owner = owner or _actor_name(data)
        target_list = _issues(data) if kind == "issue" else _prs(data)
        for obj in target_list:
            if (
                obj.get("owner") == owner
                and obj.get("repo") == repo
                and obj.get("number") == number
            ):
                assignees = obj.setdefault("assignees", [])
                if username and username not in assignees:
                    assignees.append(username)
                payload = obj
                out = json.dumps(payload)
                return out
        raise RuntimeError("Target not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignUser",
                "description": "Assign a username to an issue or PR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kind": {"type": "string", "enum": ["issue", "pr"]},
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "username": {"type": "string"},
                    },
                    "required": ["kind", "repo", "number", "username"],
                },
            },
        }


class SetMilestone(Tool):
    """Establish a plain-text milestone attribute on an issue or pull request."""

    @staticmethod
    def invoke(data: dict[str, Any], kind: str = None, owner: str = None, repo: str = None, number: int = None, milestone: str = None) -> str:
        owner = owner or _actor_name(data)
        target_list = _issues(data) if kind == "issue" else _prs(data)
        for obj in target_list:
            if (
                obj.get("owner") == owner
                and obj.get("repo") == repo
                and obj.get("number") == number
            ):
                obj["milestone"] = milestone
                payload = obj
                out = json.dumps(payload)
                return out
        raise RuntimeError("Target not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setMilestone",
                "description": "Set a milestone string on an issue or PR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kind": {"type": "string", "enum": ["issue", "pr"]},
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "milestone": {"type": "string"},
                    },
                    "required": ["kind", "repo", "number", "milestone"],
                },
            },
        }


class RemoveLabel(Tool):
    """Detach a label from an issue or pull request."""

    @staticmethod
    def invoke(data: dict[str, Any], kind: str = None, owner: str = None, repo: str = None, number: int = None, label: str = None) -> str:
        owner = owner or _actor_name(data)
        target_list = _issues(data) if kind == "issue" else _prs(data)
        for obj in target_list:
            if (
                obj.get("owner") == owner
                and obj.get("repo") == repo
                and obj.get("number") == number
            ):
                labels = obj.setdefault("labels", [])
                if label in labels:
                    labels.remove(label)
                payload = obj
                out = json.dumps(payload)
                return out
        raise RuntimeError("Target not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeLabel",
                "description": "Remove a label from an issue or PR.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kind": {"type": "string", "enum": ["issue", "pr"]},
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                        "label": {"type": "string"},
                    },
                    "required": ["kind", "repo", "number", "label"],
                },
            },
        }


class ClosePR(Tool):
    """Shut a pull request without merging."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, number: int = None) -> str:
        owner = owner or _actor_name(data)
        for p in _prs(data):
            if (
                p.get("owner") == owner
                and p.get("repo") == repo
                and p.get("number") == number
            ):
                p["state"] = "closed"
                p["closed_at"] = get_current_timestamp()
                payload = p
                out = json.dumps(payload)
                return out
        raise RuntimeError("PR not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ClosePr",
                "description": "Close a pull request without merging.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                    },
                    "required": ["repo", "number"],
                },
            },
        }


class ReopenPR(Tool):
    """Reactivate a pull request that was closed earlier."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, number: int = None) -> str:
        owner = owner or _actor_name(data)
        for p in _prs(data):
            if (
                p.get("owner") == owner
                and p.get("repo") == repo
                and p.get("number") == number
            ):
                p["state"] = "open"
                p["reopened_at"] = get_current_timestamp()
                payload = p
                out = json.dumps(payload)
                return out
        raise RuntimeError("PR not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReopenPr",
                "description": "Reopen a pull request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "number": {"type": "integer"},
                    },
                    "required": ["repo", "number"],
                },
            },
        }


class RepoTopics(Tool):
    """Define or display repository topics (a simple list of strings)."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, topics: list = None) -> str:
        owner = owner or _actor_name(data)
        r = _find_repo(data, owner, repo)
        if not r:
            raise RuntimeError("Repository not found")
        if isinstance(topics, list):
            r["topics"] = [str(t) for t in topics]
        payload = {"topics": r.get("topics", [])}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RepoTopics",
                "description": "Set or get repo topics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "topics": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["repo"],
                },
            },
        }


class TransferRepo(Tool):
    """Change repository ownership to a different username (string only)."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, new_owner: str = None) -> str:
        current = owner or _actor_name(data)
        r = _find_repo(data, current, repo)
        if not r:
            raise RuntimeError("Repository not found")
        r["owner"] = new_owner
        payload = {"ok": True, "owner": new_owner}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TransferRepo",
                "description": "Transfer repo ownership to a new owner.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "new_owner": {"type": "string"},
                    },
                    "required": ["repo", "new_owner"],
                },
            },
        }


TOOLS: list[type] = [
    WhoAmI(),
    ListRepos(),
    CreateRepo(),
    DeleteRepo(),
    ListBranches(),
    CreateBranch(),
    OpenIssue(),
    ListIssues(),
    SetIssueState(),
    CommentIssue(),
    AddLabel(),
    RemoveLabel(),
    AssignUser(),
    SetMilestone(),
    OpenPR(),
    ListPRs(),
    ClosePR(),
    ReopenPR(),
    MergePR(),
    SubmitReview(),
    AddCommit(),
    ListCommits(),
    SearchWork(),
    ListAlerts(),
    ResolveAlert(),
    ActivityFeed(),
    AppendTerminal(),
    ListTerminal(),
    RepoTopics(),
    TransferRepo(),
]
