import json
import os
from typing import Any

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> dict[str, Any]:
    db: dict[str, Any] = {}
    # auto-generated from files present in data/
    tables = ['archive_instructions', 'backup_schedules', 'completion_messages', 'directories', 'disk_quotas', 'error_logs', 'error_message_templates', 'error_messages', 'file_check_db', 'file_check_logs', 'file_lists', 'file_system', 'network_config', 'remote_servers', 'security_policies', 'slack_channels', 'slack_messages', 'ssh_keys', 'system_resources', 'task_instructions', 'task_logs', 'tmux_sessions', 'user_contacts', 'user_preferences']
    for name in tables:
        path = os.path.join(FOLDER_PATH, f"{name}.json")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                db[name] = json.loads(content) if content else []
        except FileNotFoundError:
            db[name] = []
    return db

