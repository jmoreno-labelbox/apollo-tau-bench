# Copyright Sierra

from typing import Optional, Union
import importlib
import os
from tau_bench.envs.base import Env
from tau_bench.envs.user import UserStrategy


def get_env(
    env_name: str,
    user_strategy: Union[str, UserStrategy],
    user_model: str,
    task_split: str,
    user_provider: Optional[str] = None,
    task_index: Optional[int] = None,
) -> Env:
    # Dynamic import path: allow alternate envs package via env var
    envs_pkg = os.environ.get("TAU_BENCH_ENVS_PACKAGE", "tau_bench.envs")
    try:
        module = importlib.import_module(f"{envs_pkg}.{env_name}")
        # Find an exported Env class ending with 'DomainEnv'
        for attr in dir(module):
            if attr.endswith("DomainEnv"):
                EnvCls = getattr(module, attr)
                return EnvCls(
                    user_strategy=user_strategy,
                    user_model=user_model,
                    task_split=task_split,
                    user_provider=user_provider,
                    task_index=task_index,
                )
    except Exception:
        # Fall back to static mapping below
        pass
    # dynamic import root
    envs_pkg = os.environ.get("TAU_BENCH_ENVS_PACKAGE", "tau_bench.envs")
    # fast path for retail/airline for backwards-compat
    if env_name in ["retail", "airline"]:
        module = importlib.import_module(f"{envs_pkg}.{env_name}")
        EnvCls = getattr(module, "MockRetailDomainEnv" if env_name.startswith("retail") else "MockAirlineDomainEnv")
        return EnvCls(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "banking_services_1":
        from tau_bench.envs.banking_services_1 import MockBankingServicesDomainEnv

        return MockBankingServicesDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "banking_services_2":
        from tau_bench.envs.banking_services_2 import MockBankingServicesDomainEnv

        return MockBankingServicesDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "banking_services_4":
        from tau_bench.envs.banking_services_4 import MockBankingServicesDomainEnv

        return MockBankingServicesDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "banking_services_5":
        from tau_bench.envs.banking_services_5 import MockBankingServicesDomainEnv

        return MockBankingServicesDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "banking_services_6":
        from tau_bench.envs.banking_services_6 import MockBankingServicesDomainEnv

        return MockBankingServicesDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "academic_search_1":
        from tau_bench.envs.academic_search_1 import MockAcademicSearchDomainEnv

        return MockAcademicSearchDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "academic_search_2":
        from tau_bench.envs.academic_search_2 import MockAcademicSearchDomainEnv

        return MockAcademicSearchDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "academic_search_3":
        from tau_bench.envs.academic_search_3 import MockAcademicSearchDomainEnv

        return MockAcademicSearchDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "academic_search_4":
        from tau_bench.envs.academic_search_4 import MockAcademicSearchDomainEnv

        return MockAcademicSearchDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "academic_search_5":
        from tau_bench.envs.academic_search_5 import MockAcademicSearchDomainEnv

        return MockAcademicSearchDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "airline_1":
        module = importlib.import_module(f"{envs_pkg}.airline_1")
        return getattr(module, "MockAirlineDomainEnv")(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "airline_2":
        from tau_bench.envs.airline_2 import MockAirlineDomainEnv

        return MockAirlineDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "airline_3":
        from tau_bench.envs.airline_3 import MockAirlineDomainEnv

        return MockAirlineDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "airline_4":
        from tau_bench.envs.airline_4 import MockAirlineDomainEnv

        return MockAirlineDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "airline_5":
        from tau_bench.envs.airline_5 import MockAirlineDomainEnv

        return MockAirlineDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "career_planner_1":
        from tau_bench.envs.career_planner_1 import MockCareerPlannerDomainEnv

        return MockCareerPlannerDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "career_planner_2":
        from tau_bench.envs.career_planner_2 import MockCareerPlannerDomainEnv

        return MockCareerPlannerDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "career_planner_3":
        from tau_bench.envs.career_planner_3 import MockCareerPlannerDomainEnv

        return MockCareerPlannerDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "career_planner_4":
        from tau_bench.envs.career_planner_4 import MockCareerPlannerDomainEnv

        return MockCareerPlannerDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "career_planner_5":
        from tau_bench.envs.career_planner_5 import MockCareerPlannerDomainEnv

        return MockCareerPlannerDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "consulting_accounting_1":
        from tau_bench.envs.consulting_accounting_1 import MockConsultingAccountingDomainEnv

        return MockConsultingAccountingDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "consulting_accounting_2":
        from tau_bench.envs.consulting_accounting_2 import MockConsultingAccountingDomainEnv

        return MockConsultingAccountingDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "consulting_accounting_4":
        from tau_bench.envs.consulting_accounting_4 import MockConsultingAccountingDomainEnv

        return MockConsultingAccountingDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "consulting_accounting_5":
        from tau_bench.envs.consulting_accounting_5 import MockConsultingAccountingDomainEnv

        return MockConsultingAccountingDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "consulting_accounting_6":
        from tau_bench.envs.consulting_accounting_6 import MockConsultingAccountingDomainEnv

        return MockConsultingAccountingDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "data_science_1":
        from tau_bench.envs.data_science_1 import MockDataScienceDomainEnv

        return MockDataScienceDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "data_science_2":
        from tau_bench.envs.data_science_2 import MockDataScienceDomainEnv

        return MockDataScienceDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "data_science_3":
        from tau_bench.envs.data_science_3 import MockDataScienceDomainEnv

        return MockDataScienceDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "data_science_4":
        from tau_bench.envs.data_science_4 import MockDataScienceDomainEnv

        return MockDataScienceDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "data_science_5":
        from tau_bench.envs.data_science_5 import MockDataScienceDomainEnv

        return MockDataScienceDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "data_science_6":
        from tau_bench.envs.data_science_6 import MockDataScienceDomainEnv

        return MockDataScienceDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "dev_ops_1":
        from tau_bench.envs.dev_ops_1 import MockDevOpsDomainEnv

        return MockDevOpsDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "dev_ops_2":
        from tau_bench.envs.dev_ops_2 import MockDevOpsDomainEnv

        return MockDevOpsDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "dev_ops_3":
        from tau_bench.envs.dev_ops_3 import MockDevOpsDomainEnv

        return MockDevOpsDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "dev_ops_4":
        from tau_bench.envs.dev_ops_4 import MockDevOpsDomainEnv

        return MockDevOpsDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "dev_ops_5":
        from tau_bench.envs.dev_ops_5 import MockDevOpsDomainEnv

        return MockDevOpsDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "dev_ops_6":
        from tau_bench.envs.dev_ops_6 import MockDevOpsDomainEnv

        return MockDevOpsDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "digital_commerce_1":
        from tau_bench.envs.digital_commerce_1 import MockDigitalCommerceDomainEnv

        return MockDigitalCommerceDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "digital_commerce_2":
        from tau_bench.envs.digital_commerce_2 import MockDigitalCommerceDomainEnv

        return MockDigitalCommerceDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "digital_commerce_3":
        from tau_bench.envs.digital_commerce_3 import MockDigitalCommerceDomainEnv

        return MockDigitalCommerceDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "digital_commerce_4":
        from tau_bench.envs.digital_commerce_4 import MockDigitalCommerceDomainEnv

        return MockDigitalCommerceDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "digital_commerce_5":
        from tau_bench.envs.digital_commerce_5 import MockDigitalCommerceDomainEnv

        return MockDigitalCommerceDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "figma_gmail_mcp_pipeline_1":
        from tau_bench.envs.figma_gmail_mcp_pipeline_1 import MockFigmaGmailMcpPipelineDomainEnv

        return MockFigmaGmailMcpPipelineDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "figma_gmail_mcp_pipeline_2":
        from tau_bench.envs.figma_gmail_mcp_pipeline_2 import MockFigmaGmailMcpPipelineDomainEnv

        return MockFigmaGmailMcpPipelineDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "figma_gmail_mcp_pipeline_3":
        from tau_bench.envs.figma_gmail_mcp_pipeline_3 import MockFigmaGmailMcpPipelineDomainEnv

        return MockFigmaGmailMcpPipelineDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "figma_gmail_mcp_pipeline_4":
        from tau_bench.envs.figma_gmail_mcp_pipeline_4 import MockFigmaGmailMcpPipelineDomainEnv

        return MockFigmaGmailMcpPipelineDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "figma_gmail_mcp_pipeline_5":
        from tau_bench.envs.figma_gmail_mcp_pipeline_5 import MockFigmaGmailMcpPipelineDomainEnv

        return MockFigmaGmailMcpPipelineDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "figma_gmail_mcp_pipeline_6":
        from tau_bench.envs.figma_gmail_mcp_pipeline_6 import MockFigmaGmailMcpPipelineDomainEnv

        return MockFigmaGmailMcpPipelineDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "file_system_1":
        from tau_bench.envs.file_system_1 import MockFileSystemDomainEnv

        return MockFileSystemDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "file_system_7":
        from tau_bench.envs.file_system_7 import MockFileSystemDomainEnv

        return MockFileSystemDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "file_system_8":
        from tau_bench.envs.file_system_8 import MockFileSystemDomainEnv

        return MockFileSystemDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "file_system_9":
        from tau_bench.envs.file_system_9 import MockFileSystemDomainEnv

        return MockFileSystemDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "github_mcp_1":
        from tau_bench.envs.github_mcp_1 import MockGithubMcpDomainEnv

        return MockGithubMcpDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "github_mcp_2":
        from tau_bench.envs.github_mcp_2 import MockGithubMcpDomainEnv

        return MockGithubMcpDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "github_mcp_5":
        from tau_bench.envs.github_mcp_5 import MockGithubMcpDomainEnv

        return MockGithubMcpDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "github_mcp_6":
        from tau_bench.envs.github_mcp_6 import MockGithubMcpDomainEnv

        return MockGithubMcpDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "github_mcp_7":
        from tau_bench.envs.github_mcp_7 import MockGithubMcpDomainEnv

        return MockGithubMcpDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "it_help_desk_2":
        from tau_bench.envs.it_help_desk_2 import MockItHelpDeskDomainEnv

        return MockItHelpDeskDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "it_help_desk_4":
        from tau_bench.envs.it_help_desk_4 import MockItHelpDeskDomainEnv

        return MockItHelpDeskDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "it_help_desk_5":
        from tau_bench.envs.it_help_desk_5 import MockItHelpDeskDomainEnv

        return MockItHelpDeskDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "it_help_desk_6":
        from tau_bench.envs.it_help_desk_6 import MockItHelpDeskDomainEnv

        return MockItHelpDeskDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "logistics_supply_chain_1":
        from tau_bench.envs.logistics_supply_chain_1 import MockLogisticsSupplyChainDomainEnv

        return MockLogisticsSupplyChainDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "logistics_supply_chain_2":
        from tau_bench.envs.logistics_supply_chain_2 import MockLogisticsSupplyChainDomainEnv

        return MockLogisticsSupplyChainDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "logistics_supply_chain_3":
        from tau_bench.envs.logistics_supply_chain_3 import MockLogisticsSupplyChainDomainEnv

        return MockLogisticsSupplyChainDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "logistics_supply_chain_5":
        from tau_bench.envs.logistics_supply_chain_5 import MockLogisticsSupplyChainDomainEnv

        return MockLogisticsSupplyChainDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "logistics_supply_chain_6":
        from tau_bench.envs.logistics_supply_chain_6 import MockLogisticsSupplyChainDomainEnv

        return MockLogisticsSupplyChainDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "new_hire_mcp_1":
        from tau_bench.envs.new_hire_mcp_1 import MockNewHireMcpDomainEnv

        return MockNewHireMcpDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "new_hire_mcp_2":
        from tau_bench.envs.new_hire_mcp_2 import MockNewHireMcpDomainEnv

        return MockNewHireMcpDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "new_hire_mcp_3":
        from tau_bench.envs.new_hire_mcp_3 import MockNewHireMcpDomainEnv

        return MockNewHireMcpDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "new_hire_mcp_4":
        from tau_bench.envs.new_hire_mcp_4 import MockNewHireMcpDomainEnv

        return MockNewHireMcpDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "new_hire_mcp_5":
        from tau_bench.envs.new_hire_mcp_5 import MockNewHireMcpDomainEnv

        return MockNewHireMcpDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "org_chart_1":
        from tau_bench.envs.org_chart_1 import MockOrgChartDomainEnv

        return MockOrgChartDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "org_chart_2":
        from tau_bench.envs.org_chart_2 import MockOrgChartDomainEnv

        return MockOrgChartDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "org_chart_3":
        from tau_bench.envs.org_chart_3 import MockOrgChartDomainEnv

        return MockOrgChartDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "org_chart_4":
        from tau_bench.envs.org_chart_4 import MockOrgChartDomainEnv

        return MockOrgChartDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "org_chart_5":
        from tau_bench.envs.org_chart_5 import MockOrgChartDomainEnv

        return MockOrgChartDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "project_management_1":
        from tau_bench.envs.project_management_1 import MockProjectManagementDomainEnv

        return MockProjectManagementDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "project_management_2":
        from tau_bench.envs.project_management_2 import MockProjectManagementDomainEnv

        return MockProjectManagementDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "project_management_3":
        from tau_bench.envs.project_management_3 import MockProjectManagementDomainEnv

        return MockProjectManagementDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "project_management_4":
        from tau_bench.envs.project_management_4 import MockProjectManagementDomainEnv

        return MockProjectManagementDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "project_management_5":
        from tau_bench.envs.project_management_5 import MockProjectManagementDomainEnv

        return MockProjectManagementDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "rbac_1":
        from tau_bench.envs.rbac_1 import MockRbacDomainEnv

        return MockRbacDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "rbac_2":
        from tau_bench.envs.rbac_2 import MockRbacDomainEnv

        return MockRbacDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "rbac_3":
        from tau_bench.envs.rbac_3 import MockRbacDomainEnv

        return MockRbacDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "rbac_4":
        from tau_bench.envs.rbac_4 import MockRbacDomainEnv

        return MockRbacDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "rbac_5":
        from tau_bench.envs.rbac_5 import MockRbacDomainEnv

        return MockRbacDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "real_estate_sales_1":
        from tau_bench.envs.real_estate_sales_1 import MockRealEstateSalesDomainEnv

        return MockRealEstateSalesDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "real_estate_sales_2":
        from tau_bench.envs.real_estate_sales_2 import MockRealEstateSalesDomainEnv

        return MockRealEstateSalesDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "real_estate_sales_3":
        from tau_bench.envs.real_estate_sales_3 import MockRealEstateSalesDomainEnv

        return MockRealEstateSalesDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "real_estate_sales_4":
        from tau_bench.envs.real_estate_sales_4 import MockRealEstateSalesDomainEnv

        return MockRealEstateSalesDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "real_estate_sales_7":
        from tau_bench.envs.real_estate_sales_7 import MockRealEstateSalesDomainEnv

        return MockRealEstateSalesDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "recipes_1":
        from tau_bench.envs.recipes_1 import MockRecipesDomainEnv

        return MockRecipesDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "recipes_2":
        from tau_bench.envs.recipes_2 import MockRecipesDomainEnv

        return MockRecipesDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "recipes_3":
        from tau_bench.envs.recipes_3 import MockRecipesDomainEnv

        return MockRecipesDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "recipes_4":
        from tau_bench.envs.recipes_4 import MockRecipesDomainEnv

        return MockRecipesDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "recipes_5":
        from tau_bench.envs.recipes_5 import MockRecipesDomainEnv

        return MockRecipesDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "retail_1":
        from tau_bench.envs.retail_1 import MockRetailDomainEnv

        return MockRetailDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "retail_2":
        from tau_bench.envs.retail_2 import MockRetailDomainEnv

        return MockRetailDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "retail_3":
        from tau_bench.envs.retail_3 import MockRetailDomainEnv

        return MockRetailDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "retail_4":
        from tau_bench.envs.retail_4 import MockRetailDomainEnv

        return MockRetailDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "retail_5":
        from tau_bench.envs.retail_5 import MockRetailDomainEnv

        return MockRetailDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "retail_6":
        from tau_bench.envs.retail_6 import MockRetailDomainEnv

        return MockRetailDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "retail_point_of_sale_and_inventory_system_1":
        from tau_bench.envs.retail_point_of_sale_and_inventory_system_1 import MockRetailPointOfSaleAndInventorySystemDomainEnv

        return MockRetailPointOfSaleAndInventorySystemDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "retail_point_of_sale_and_inventory_system_2":
        from tau_bench.envs.retail_point_of_sale_and_inventory_system_2 import MockRetailPointOfSaleAndInventorySystemDomainEnv

        return MockRetailPointOfSaleAndInventorySystemDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "retail_point_of_sale_and_inventory_system_4":
        from tau_bench.envs.retail_point_of_sale_and_inventory_system_4 import MockRetailPointOfSaleAndInventorySystemDomainEnv

        return MockRetailPointOfSaleAndInventorySystemDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "retail_point_of_sale_and_inventory_system_5":
        from tau_bench.envs.retail_point_of_sale_and_inventory_system_5 import MockRetailPointOfSaleAndInventorySystemDomainEnv

        return MockRetailPointOfSaleAndInventorySystemDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "retail_point_of_sale_and_inventory_system_6":
        from tau_bench.envs.retail_point_of_sale_and_inventory_system_6 import MockRetailPointOfSaleAndInventorySystemDomainEnv

        return MockRetailPointOfSaleAndInventorySystemDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "smart_home_1":
        from tau_bench.envs.smart_home_1 import MockSmartHomeDomainEnv

        return MockSmartHomeDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "smart_home_2":
        from tau_bench.envs.smart_home_2 import MockSmartHomeDomainEnv

        return MockSmartHomeDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "smart_home_3":
        from tau_bench.envs.smart_home_3 import MockSmartHomeDomainEnv

        return MockSmartHomeDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "smart_home_4":
        from tau_bench.envs.smart_home_4 import MockSmartHomeDomainEnv

        return MockSmartHomeDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "smart_home_5":
        from tau_bench.envs.smart_home_5 import MockSmartHomeDomainEnv

        return MockSmartHomeDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "social_media_advertising_1":
        from tau_bench.envs.social_media_advertising_1 import MockSocialMediaAdvertisingDomainEnv

        return MockSocialMediaAdvertisingDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "social_media_advertising_2":
        from tau_bench.envs.social_media_advertising_2 import MockSocialMediaAdvertisingDomainEnv

        return MockSocialMediaAdvertisingDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "social_media_advertising_3":
        from tau_bench.envs.social_media_advertising_3 import MockSocialMediaAdvertisingDomainEnv

        return MockSocialMediaAdvertisingDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "social_media_advertising_4":
        from tau_bench.envs.social_media_advertising_4 import MockSocialMediaAdvertisingDomainEnv

        return MockSocialMediaAdvertisingDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "social_media_advertising_5":
        from tau_bench.envs.social_media_advertising_5 import MockSocialMediaAdvertisingDomainEnv

        return MockSocialMediaAdvertisingDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "social_media_advertising_6":
        from tau_bench.envs.social_media_advertising_6 import MockSocialMediaAdvertisingDomainEnv

        return MockSocialMediaAdvertisingDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "sports_analytics_2":
        from tau_bench.envs.sports_analytics_2 import MockSportsAnalyticsDomainEnv

        return MockSportsAnalyticsDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "sports_analytics_3":
        from tau_bench.envs.sports_analytics_3 import MockSportsAnalyticsDomainEnv

        return MockSportsAnalyticsDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "sports_analytics_4":
        from tau_bench.envs.sports_analytics_4 import MockSportsAnalyticsDomainEnv

        return MockSportsAnalyticsDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )
    elif env_name == "sports_analytics_5":
        from tau_bench.envs.sports_analytics_5 import MockSportsAnalyticsDomainEnv

        return MockSportsAnalyticsDomainEnv(
            user_strategy=user_strategy,
            user_model=user_model,
            task_split=task_split,
            user_provider=user_provider,
            task_index=task_index,
        )





















































































































    else:
        raise ValueError(f"Unknown environment: {env_name}")
