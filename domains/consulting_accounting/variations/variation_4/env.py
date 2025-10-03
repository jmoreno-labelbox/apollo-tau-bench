# Copyright Sierra

from tau_bench.envs.base import Env
from domains.consulting_accounting.service import ConsultingAccountingSystem
from domains.consulting_accounting.variations.variation_4.rules import RULES
from domains.consulting_accounting.variations.variation_4.tools import TOOLS
from typing import Optional, Union
from tau_bench.envs.user import UserStrategy


class MockConsultingAccountingDomainEnv(Env):
    def __init__(
        self,
        user_strategy: Union[str, UserStrategy] = UserStrategy.LLM,
        user_model: str = "gpt-4o",
        user_provider: Optional[str] = None,
        task_split: str = "test",
        task_index: Optional[int] = None,
    ):
        match task_split:
            case "test":
                from domains.consulting_accounting.variations.variation_4.tasks_test import TASKS as tasks
            case _:
                raise ValueError(f"Unknown task split: {task_split}")
        
        # Create service instance to get load_data function
        service = ConsultingAccountingSystem(tools=TOOLS)
        
        super().__init__(
            data_load_func=service._load_data,
            tools=TOOLS,
            tasks=tasks,
            wiki="",  # TODO: Add wiki content if available
            rules=RULES,
            user_strategy=user_strategy,
            user_model=user_model,
            user_provider=user_provider,
            task_index=task_index,
        )
        self.terminate_tools = ["transfer_to_human_agents"]
