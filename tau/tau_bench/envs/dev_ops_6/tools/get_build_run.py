# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBuildRun(Tool):
    """Fetch a build run by id; optionally filter by commit_sha."""

    @staticmethod
    def invoke(data: Dict[str, Any], commit_sha, id) -> str:
        rid = id
        commit = commit_sha
        rows = _table(data, 'build_runs')
        row = next((r for r in rows if rid and r.get('id') == rid or (commit and r.get('commit_sha') == commit)), None)
        return _ok({'build_run': row}) if row else _err('build_run not found')

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {'type': 'function', 'function': {'name': 'get_build_run', 'description': 'Fetch a build run by id (or commit_sha).', 'parameters': {'type': 'object', 'properties': {'id': {'type': 'string'}, 'commit_sha': {'type': 'string'}}, 'required': []}}}
