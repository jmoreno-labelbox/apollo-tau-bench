# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso


class CreateProject(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_code, default_hourly_rate, isbn, override_hourly_rate, project_id, project_title, publisher_id, is_active = True) -> str:
        projects = list(data.get("projects", {}).values())
        row = {
            "project_id": project_id,
            "publisher_id": publisher_id,
            "isbn": isbn,
            "project_title": project_title,
            "default_hourly_rate": default_hourly_rate,
            "override_hourly_rate": override_hourly_rate,
            "account_code": account_code,
            "is_active": is_active,
            "created_at": _fixed_now_iso(),
            "updated_at": _fixed_now_iso()
        }
        projects.append(row)
        return json.dumps(row, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_project",
            "description":"Create a new project row.",
            "parameters":{"type":"object","properties":{
                "project_id":{"type":"string"},
                "publisher_id":{"type":"string"},
                "isbn":{"type":"string"},
                "project_title":{"type":"string"},
                "default_hourly_rate":{"type":"number"},
                "override_hourly_rate":{"type":["number","null"]},
                "account_code":{"type":["string","null"]},
                "is_active":{"type":"boolean"}
            },"required":["project_id","publisher_id","isbn","project_title","default_hourly_rate"]}
        }}
