from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class Action:
    name: str
    kwargs: Dict[str, Any]


@dataclass
class Task:
    annotator: str
    user_id: str
    instruction: str
    actions: List[Action]
    outputs: List[str]


class Tool:
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        raise NotImplementedError

    @staticmethod
    def get_info() -> Dict[str, Any]:
        raise NotImplementedError
