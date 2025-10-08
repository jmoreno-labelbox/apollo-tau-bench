# Copyright Sierra

import os
import json
import random
import traceback
from math import comb
import multiprocessing
from typing import List, Dict, Any
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from tau_bench.envs import get_env
from tau_bench.agents.base import Agent
from tau_bench.types import EnvRunResult, RunConfig
from litellm import provider_list
from tau_bench.envs.user import UserStrategy


def run(config: RunConfig) -> List[EnvRunResult]:
    assert config.env in ["academic_search_1",
        "academic_search_2",
        "academic_search_3",
        "academic_search_4",
        "academic_search_5",
        "airline",
        "airline_1",
        "airline_2",
        "airline_3",
        "airline_4",
        "airline_5",
        "banking_services_1",
        "banking_services_2",
        "banking_services_4",
        "banking_services_5",
        "banking_services_6",
        "career_planner_1",
        "career_planner_2",
        "career_planner_3",
        "career_planner_4",
        "career_planner_5",
        "consulting_accounting_1",
        "consulting_accounting_2",
        "consulting_accounting_4",
        "consulting_accounting_5",
        "consulting_accounting_6",
        "data_science_1",
        "data_science_2",
        "data_science_3",
        "data_science_4",
        "data_science_5",
        "data_science_6",
        "dev_ops_1",
        "dev_ops_2",
        "dev_ops_3",
        "dev_ops_4",
        "dev_ops_5",
        "dev_ops_6",
        "digital_commerce_1",
        "digital_commerce_2",
        "digital_commerce_3",
        "digital_commerce_4",
        "digital_commerce_5",
        "figma_gmail_mcp_pipeline_1",
        "figma_gmail_mcp_pipeline_2",
        "figma_gmail_mcp_pipeline_3",
        "figma_gmail_mcp_pipeline_4",
        "figma_gmail_mcp_pipeline_5",
        "figma_gmail_mcp_pipeline_6",
        "file_system_1",
        "file_system_7",
        "file_system_8",
        "file_system_9",
        "github_mcp_1",
        "github_mcp_2",
        "github_mcp_5",
        "github_mcp_6",
        "github_mcp_7",
        "it_help_desk_2",
        "it_help_desk_4",
        "it_help_desk_5",
        "it_help_desk_6",
        "logistics_supply_chain_1",
        "logistics_supply_chain_2",
        "logistics_supply_chain_3",
        "logistics_supply_chain_5",
        "logistics_supply_chain_6",
        "new_hire_mcp_1",
        "new_hire_mcp_2",
        "new_hire_mcp_3",
        "new_hire_mcp_4",
        "new_hire_mcp_5",
        "org_chart_1",
        "org_chart_2",
        "org_chart_3",
        "org_chart_4",
        "org_chart_5",
        "project_management_1",
        "project_management_2",
        "project_management_3",
        "project_management_4",
        "project_management_5",
        "rbac_1",
        "rbac_2",
        "rbac_3",
        "rbac_4",
        "rbac_5",
        "real_estate_sales_1",
        "real_estate_sales_2",
        "real_estate_sales_3",
        "real_estate_sales_4",
        "real_estate_sales_7",
        "recipes_1",
        "recipes_2",
        "recipes_3",
        "recipes_4",
        "recipes_5",
        "retail",
        "retail_1",
        "retail_2",
        "retail_3",
        "retail_4",
        "retail_5",
        "retail_6",
        "retail_point_of_sale_and_inventory_system_1",
        "retail_point_of_sale_and_inventory_system_2",
        "retail_point_of_sale_and_inventory_system_4",
        "retail_point_of_sale_and_inventory_system_5",
        "retail_point_of_sale_and_inventory_system_6",
        "smart_home_1",
        "smart_home_2",
        "smart_home_3",
        "smart_home_4",
        "smart_home_5",
        "social_media_advertising_1",
        "social_media_advertising_2",
        "social_media_advertising_3",
        "social_media_advertising_4",
        "social_media_advertising_5",
        "social_media_advertising_6",
        "sports_analytics_2",
        "sports_analytics_3",
        "sports_analytics_4",
        "sports_analytics_5"], "Only retail, airline, and banking_services_{1,2,4,5,6} envs are supported"
    # Normalize provider values to strings for validation and downstream usage
    provider_strs = [getattr(p, "value", p) for p in provider_list]
    model_provider_str = getattr(config.model_provider, "value", config.model_provider)
    user_model_provider_str = getattr(
        config.user_model_provider, "value", config.user_model_provider
    )
    assert model_provider_str in provider_strs, "Invalid model provider"
    assert user_model_provider_str in provider_strs, "Invalid user model provider"
    # Ensure config uses normalized strings so agents/envs receive provider names they expect
    try:
        config.model_provider = model_provider_str
        config.user_model_provider = user_model_provider_str
    except Exception:
        pass
    assert config.agent_strategy in ["tool-calling", "act", "react", "few-shot"], "Invalid agent strategy"
    assert config.task_split in ["train", "test", "dev"], "Invalid task split"
    assert config.user_strategy in [item.value for item in UserStrategy], "Invalid user strategy"

    random.seed(config.seed)
    time_str = datetime.now().strftime("%m%d%H%M%S")
    ckpt_path = f"{config.log_dir}/{config.agent_strategy}-{config.model.split('/')[-1]}-{config.temperature}_range_{config.start_index}-{config.end_index}_user-{config.user_model}-{config.user_strategy}_{time_str}.json"
    if not os.path.exists(config.log_dir):
        os.makedirs(config.log_dir)

    print(f"Loading user with strategy: {config.user_strategy}")
    env = get_env(
        config.env,
        user_strategy=config.user_strategy,
        user_model=config.user_model,
        user_provider=config.user_model_provider,
        task_split=config.task_split,
    )
    agent = agent_factory(
        tools_info=env.tools_info,
        wiki=env.wiki,
        config=config,
    )
    end_index = (
        len(env.tasks) if config.end_index == -1 else min(config.end_index, len(env.tasks))
    )
    results: List[EnvRunResult] = []
    lock = multiprocessing.Lock()
    if config.task_ids and len(config.task_ids) > 0:
        print(f"Running tasks {config.task_ids} (checkpoint path: {ckpt_path})")
    else:
        print(
            f"Running tasks {config.start_index} to {end_index} (checkpoint path: {ckpt_path})"
    )
    for i in range(config.num_trials):
        if config.task_ids and len(config.task_ids) > 0:
            idxs = config.task_ids
        else:
            idxs = list(range(config.start_index, end_index))
        if config.shuffle:
            random.shuffle(idxs)

        def _run(idx: int) -> EnvRunResult:
            isolated_env = get_env(
                config.env,
                user_strategy=config.user_strategy,
                user_model=config.user_model,
                task_split=config.task_split,
                user_provider=config.user_model_provider,
                task_index=idx,
            )

            print(f"Running task {idx}")
            try:
                res = agent.solve(
                    env=isolated_env,
                    task_index=idx,
                )
                result = EnvRunResult(
                    task_id=idx,
                    reward=res.reward,
                    info=res.info,
                    traj=res.messages,
                    trial=i,
                )
            except Exception as e:
                result = EnvRunResult(
                    task_id=idx,
                    reward=0.0,
                    info={"error": str(e), "traceback": traceback.format_exc()},
                    traj=[],
                    trial=i,
                )
            print(
                "✅" if result.reward == 1 else "❌",
                f"task_id={idx}",
                result.info,
            )
            print("-----")
            with lock:
                data = []
                if os.path.exists(ckpt_path):
                    with open(ckpt_path, "r") as f:
                        data = json.load(f)
                with open(ckpt_path, "w") as f:
                    json.dump(data + [result.model_dump()], f, indent=2)
            return result

        with ThreadPoolExecutor(max_workers=config.max_concurrency) as executor:
            res = list(executor.map(_run, idxs))
            results.extend(res)

    display_metrics(results)

    with open(ckpt_path, "w") as f:
        json.dump([result.model_dump() for result in results], f, indent=2)
        print(f"\n📄 Results saved to {ckpt_path}\n")
    return results


def agent_factory(
    tools_info: List[Dict[str, Any]], wiki, config: RunConfig
) -> Agent:
    if config.agent_strategy == "tool-calling":
        # native tool calling
        from tau_bench.agents.tool_calling_agent import ToolCallingAgent

        return ToolCallingAgent(
            tools_info=tools_info,
            wiki=wiki,
            model=config.model,
            provider=config.model_provider,
            temperature=config.temperature,
        )
    elif config.agent_strategy == "act":
        # `act` from https://arxiv.org/abs/2210.03629
        from tau_bench.agents.chat_react_agent import ChatReActAgent

        return ChatReActAgent(
            tools_info=tools_info,
            wiki=wiki,
            model=config.model,
            provider=config.model_provider,
            use_reasoning=False,
            temperature=config.temperature,
        )
    elif config.agent_strategy == "react":
        # `react` from https://arxiv.org/abs/2210.03629
        from tau_bench.agents.chat_react_agent import ChatReActAgent

        return ChatReActAgent(
            tools_info=tools_info,
            wiki=wiki,
            model=config.model,
            provider=config.model_provider,
            use_reasoning=True,
            temperature=config.temperature,
        )
    elif config.agent_strategy == "few-shot":
        from tau_bench.agents.few_shot_agent import FewShotToolCallingAgent
        assert config.few_shot_displays_path is not None, "Few shot displays path is required for few-shot agent strategy"
        with open(config.few_shot_displays_path, "r") as f:
            few_shot_displays = [json.loads(line)["messages_display"] for line in f]

        return FewShotToolCallingAgent(
            tools_info=tools_info,
            wiki=wiki,
            model=config.model,
            provider=config.model_provider,
            few_shot_displays=few_shot_displays,
            temperature=config.temperature,
        )
    else:
        raise ValueError(f"Unknown agent strategy: {config.agent_strategy}")


def display_metrics(results: List[EnvRunResult]) -> None:
    def is_successful(reward: float) -> bool:
        return (1 - 1e-6) <= reward <= (1 + 1e-6)

    num_trials = len(set([r.trial for r in results]))
    rewards = [r.reward for r in results]
    avg_reward = sum(rewards) / len(rewards)
    # c from https://arxiv.org/pdf/2406.12045
    c_per_task_id: dict[int, int] = {}
    for result in results:
        if result.task_id not in c_per_task_id:
            c_per_task_id[result.task_id] = 1 if is_successful(result.reward) else 0
        else:
            c_per_task_id[result.task_id] += 1 if is_successful(result.reward) else 0
    pass_hat_ks: dict[int, float] = {}
    for k in range(1, num_trials + 1):
        sum_task_pass_hat_k = 0
        for c in c_per_task_id.values():
            sum_task_pass_hat_k += comb(c, k) / comb(num_trials, k)
        pass_hat_ks[k] = sum_task_pass_hat_k / len(c_per_task_id)
    print(f"🏆 Average reward: {avg_reward}")
    print("📈 Pass^k")
    for k, pass_hat_k in pass_hat_ks.items():
        print(f"  k={k}: {pass_hat_k}")
