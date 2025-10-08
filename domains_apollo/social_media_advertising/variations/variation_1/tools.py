import json
from datetime import datetime
from typing import Any

from domains.dto import Tool


class GetCampaigns(Tool):
    """Fetches all advertising campaigns."""

    @staticmethod
    def invoke(data: dict[str, Any], timestamp: Any = None) -> str:
        campaigns = data.get("campaigns", [])
        ids_ = []
        for i in campaigns:
            ids_ += [i.get("campaign_id")]
        payload = {"campaigns_ids": ids_}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCampaigns",
                "description": "Retrieves all advertising campaign ids.",
                "parameters": {},
            },
        }


class GetNameForCampaign(Tool):
    """Fetches a particular campaign using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        campaigns = data.get("campaigns", [])

        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                payload = {"name": campaign.get("name")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign with ID '{campaign_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNameForCampaign",
                "description": "Retrieves a specific campaign by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The unique ID of the campaign.",
                        }
                    },
                    "required": ["campaign_id"],
                },
            },
        }


class GetObjectiveForCampaign(Tool):
    """Fetches the goal of a specific campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        campaigns = data.get("campaigns", [])

        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                payload = {"objective": campaign.get("objective")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign with ID '{campaign_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getObjectiveForCampaign",
                "description": "Retrieves the objective for a specific campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The unique ID of the campaign.",
                        }
                    },
                    "required": ["campaign_id"],
                },
            },
        }


class GetStatusForCampaign(Tool):
    """Fetches the current status of a specific campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        campaigns = data.get("campaigns", [])

        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                payload = {"status": campaign.get("status")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign with ID '{campaign_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getStatusForCampaign",
                "description": "Retrieves the status for a specific campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The unique ID of the campaign.",
                        }
                    },
                    "required": ["campaign_id"],
                },
            },
        }


class UpdateCampaignStatus(Tool):
    """Modifies the status of a campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, new_status: str = None) -> str:
        campaigns = data.get("campaigns", [])
        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                old_status = campaign["status"]
                campaign["status"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Campaign status updated from '{old_status}' to '{new_status}'",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign {campaign_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateCampaignStatus",
                "description": "Updates the status of a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["campaign_id", "new_status"],
                },
            },
        }


class GetAdSets(Tool):
    """Fetches all IDs of ad sets."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        adsets = data.get("adsets", [])
        ids_ = []
        for i in adsets:
            ids_ += [i.get("adset_id")]
        payload = {"adset_ids": ids_}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAdsets",
                "description": "Retrieves all ad set IDs.",
                "parameters": {},
            },
        }


class GetNameForAdSet(Tool):
    """Fetches the name of a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        adsets = data.get("adsets", [])

        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                payload = {"name": adset.get("name")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set with ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNameForAdset",
                "description": "Retrieves the name for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }


class GetCampaignIdForAdSet(Tool):
    """Fetches the campaign ID associated with a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        adsets = data.get("adsets", [])

        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                payload = {"campaign_id": adset.get("campaign_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set with ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCampaignIdForAdset",
                "description": "Retrieves the campaign ID for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }


class GetDailyBudgetForAdSet(Tool):
    """Fetches the daily budget allocated for a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        adsets = data.get("adsets", [])

        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                payload = {"daily_budget": adset.get("daily_budget")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set with ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDailyBudgetForAdset",
                "description": "Retrieves the daily budget for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }


class UpdateDailyBudgetForAdSet(Tool):
    """Modifies the daily budget of a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, new_budget: float = None) -> str:
        adsets = data.get("adsets", [])
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                old_budget = adset["daily_budget"]
                adset["daily_budget"] = new_budget
                payload = {
                    "status": "success",
                    "message": f"Ad set budget updated from {old_budget} to {new_budget}",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set {adset_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateDailyBudgetForAdset",
                "description": "Updates the daily budget for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_budget": {"type": "number"},
                    },
                    "required": ["adset_id", "new_budget"],
                },
            },
        }


class GetAds(Tool):
    """Fetches all IDs of ads."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        ads = data.get("ads", [])
        ids_ = []
        for i in ads:
            ids_ += [i.get("ad_id")]
        payload = {"ad_ids": ids_}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAds",
                "description": "Retrieves all ad IDs.",
                "parameters": {},
            },
        }


class GetNameForAd(Tool):
    """Fetches the name of a specific ad."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str = None) -> str:
        ads = data.get("ads", [])

        for ad in ads:
            if ad.get("ad_id") == ad_id:
                payload = {"name": ad.get("name")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad with ID '{ad_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getNameForAd",
                "description": "Retrieves the name for a specific ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {
                            "type": "string",
                            "description": "The unique ID of the ad.",
                        }
                    },
                    "required": ["ad_id"],
                },
            },
        }


class GetCreativeTypeForAd(Tool):
    """Fetches the creative type of a specific ad."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str = None) -> str:
        ads = data.get("ads", [])

        for ad in ads:
            if ad.get("ad_id") == ad_id:
                payload = {"creative_type": ad.get("creative_type")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad with ID '{ad_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCreativeTypeForAd",
                "description": "Retrieves the creative_type for a specific ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {
                            "type": "string",
                            "description": "The unique ID of the ad.",
                        }
                    },
                    "required": ["ad_id"],
                },
            },
        }


class GetStatusForAd(Tool):
    """Fetches the current status of a specific ad."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str = None) -> str:
        ads = data.get("ads", [])

        for ad in ads:
            if ad.get("ad_id") == ad_id:
                payload = {"status": ad.get("status")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad with ID '{ad_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetStatusForAd",
                "description": "Retrieves the status for a specific ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {
                            "type": "string",
                            "description": "The unique ID of the ad.",
                        }
                    },
                    "required": ["ad_id"],
                },
            },
        }


class UpdateAdStatus(Tool):
    """Modifies the status of a specific ad."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str = None, new_status: str = None,
    timestamp: Any = None,
    ) -> str:
        ads = data.get("ads", [])
        for ad in ads:
            if ad.get("ad_id") == ad_id:
                old_status = ad["status"]
                ad["status"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Ad status updated from '{old_status}' to '{new_status}'",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad {ad_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdStatus",
                "description": "Updates the status for a specific ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["ad_id", "new_status"],
                },
            },
        }


class GetProducts(Tool):
    """Fetches all IDs of products."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        products = data.get("dim_product", [])
        ids_ = []
        for i in products:
            ids_ += [i.get("product_id")]
        payload = {"product_ids": ids_}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getProducts",
                "description": "Retrieves all product IDs.",
                "parameters": {},
            },
        }


class GetNameForProduct(Tool):
    """Fetches the name of a specific product."""

    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None) -> str:
        products = data.get("dim_product", [])

        for product in products:
            if product.get("product_id") == product_id:
                payload = {"name": product.get("name")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Product with ID '{product_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getNameForProduct",
                "description": "Retrieves the name for a specific product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "The unique ID of the product.",
                        }
                    },
                    "required": ["product_id"],
                },
            },
        }


class GetPlans(Tool):
    """Fetches all IDs of plans."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        plans = data.get("plans", [])
        ids_ = []
        for i in plans:
            ids_ += [i.get("plan_id")]
        payload = {"plan_ids": ids_}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPlans",
                "description": "Retrieves all plan IDs.",
                "parameters": {},
            },
        }


class GetDateForPlan(Tool):
    """Fetches the date associated with a specific plan."""

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None) -> str:
        plans = data.get("plans", [])

        for plan in plans:
            if plan.get("plan_id") == plan_id:
                payload = {"date": plan.get("date")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Plan with ID '{plan_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDateForPlan",
                "description": "Retrieves the date for a specific plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The unique ID of the plan.",
                        }
                    },
                    "required": ["plan_id"],
                },
            },
        }


class GetAutomationRuns(Tool):
    """Fetches all IDs of automation runs."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        runs = data.get("automation_runs", [])
        ids_ = []
        for i in runs:
            ids_ += [i.get("run_id")]
        payload = {"automation_run_ids": ids_}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAutomationRuns",
                "description": "Retrieves all automation run IDs.",
                "parameters": {},
            },
        }


class GetRunTypeForAutomationRun(Tool):
    """Fetches the type of run for a specific automation run."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None) -> str:
        runs = data.get("automation_runs", [])

        for run in runs:
            if run.get("run_id") == run_id:
                payload = {"run_type": run.get("run_type")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Automation run with ID '{run_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getRunTypeForAutomationRun",
                "description": "Retrieves the run type for a specific automation run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {
                            "type": "string",
                            "description": "The unique ID of the automation run.",
                        }
                    },
                    "required": ["run_id"],
                },
            },
        }


class GetBudgetChanges(Tool):
    """Fetches all IDs of budget changes."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        changes = data.get("budget_changes", [])
        ids_ = []
        for i in changes:
            ids_ += [i.get("change_id")]
        payload = {"budget_change_ids": ids_}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getBudgetChanges",
                "description": "Retrieves all budget change IDs.",
                "parameters": {},
            },
        }


class GetAdSetIdForBudgetChange(Tool):
    """Fetches the ad set ID linked to a specific budget change."""

    @staticmethod
    def invoke(data: dict[str, Any], change_id: str = None) -> str:
        changes = data.get("budget_changes", [])

        for change in changes:
            if change.get("change_id") == change_id:
                payload = {"adset_id": change.get("adset_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Budget change with ID '{change_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAdsetIdForBudgetChange",
                "description": "Retrieves the ad set ID for a specific budget change.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "change_id": {
                            "type": "string",
                            "description": "The unique ID of the budget change.",
                        }
                    },
                    "required": ["change_id"],
                },
            },
        }


class SearchCampaignsByObjective(Tool):
    """Looks for campaigns that have a particular objective."""

    @staticmethod
    def invoke(data: dict[str, Any], objective: str = None) -> str:
        campaigns = data.get("campaigns", [])
        matching_campaigns = []

        for campaign in campaigns:
            if campaign.get("objective") == objective:
                matching_campaigns.append(campaign.get("campaign_id"))
        payload = {"campaign_ids": matching_campaigns}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchCampaignsByObjective",
                "description": "Searches for campaigns with a specific objective.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "objective": {
                            "type": "string",
                            "description": "The objective to search for (e.g., Sales, Awareness, Traffic).",
                        }
                    },
                    "required": ["objective"],
                },
            },
        }


class SearchCampaignsByStatus(Tool):
    """Looks for campaigns that have a specific status."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = None) -> str:
        campaigns = data.get("campaigns", [])
        matching_campaigns = []

        for campaign in campaigns:
            if campaign.get("status") == status:
                matching_campaigns.append(campaign.get("campaign_id"))
        payload = {"campaign_ids": matching_campaigns}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchCampaignsByStatus",
                "description": "Searches for campaigns with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status to search for (e.g., active, paused, archived).",
                        }
                    },
                    "required": ["status"],
                },
            },
        }


class SearchAdSetsByCategory(Tool):
    """Looks for ad sets belonging to a certain category."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None) -> str:
        adsets = data.get("adsets", [])
        matching_adsets = []

        for adset in adsets:
            if adset.get("category") == category:
                matching_adsets.append(adset.get("adset_id"))
        payload = {"adset_ids": matching_adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchAdsetsByCategory",
                "description": "Searches for ad sets with a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to search for (e.g., Electronics, Apparel, Home).",
                        }
                    },
                    "required": ["category"],
                },
            },
        }


class SearchAdSetsByStatus(Tool):
    """Looks for ad sets that have a specific status."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = None) -> str:
        adsets = data.get("adsets", [])
        matching_adsets = []

        for adset in adsets:
            if adset.get("status") == status:
                matching_adsets.append(adset.get("adset_id"))
        payload = {"adset_ids": matching_adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchAdsetsByStatus",
                "description": "Searches for ad sets with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status to search for (e.g., active, paused).",
                        }
                    },
                    "required": ["status"],
                },
            },
        }


class SearchAdsByCreativeType(Tool):
    """Looks for ads that feature a particular creative type."""

    @staticmethod
    def invoke(data: dict[str, Any], creative_type: str = None) -> str:
        ads = data.get("ads", [])
        matching_ads = []

        for ad in ads:
            if ad.get("creative_type") == creative_type:
                matching_ads.append(ad.get("ad_id"))
        payload = {"ad_ids": matching_ads}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchAdsByCreativeType",
                "description": "Searches for ads with a specific creative type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "creative_type": {
                            "type": "string",
                            "description": "The creative type to search for (e.g., image, video, carousel).",
                        }
                    },
                    "required": ["creative_type"],
                },
            },
        }


class SearchAdsByStatus(Tool):
    """Looks for ads that have a specific status."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = None) -> str:
        ads = data.get("ads", [])
        matching_ads = []

        for ad in ads:
            if ad.get("status") == status:
                matching_ads.append(ad.get("ad_id"))
        payload = {"ad_ids": matching_ads}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchAdsByStatus",
                "description": "Searches for ads with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status to search for (e.g., active, paused, archived).",
                        }
                    },
                    "required": ["status"],
                },
            },
        }


class SearchProductsByCategory(Tool):
    """Looks for products that belong to a certain category."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None) -> str:
        products = data.get("dim_product", [])
        matching_products = []

        for product in products:
            if product.get("category") == category:
                matching_products.append(product.get("product_id"))
        payload = {"product_ids": matching_products}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchProductsByCategory",
                "description": "Searches for products with a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to search for (e.g., Electronics, Apparel, Home).",
                        }
                    },
                    "required": ["category"],
                },
            },
        }


class SearchAutomationRunsByType(Tool):
    """Looks for automation runs that have a specific run type."""

    @staticmethod
    def invoke(data: dict[str, Any], run_type: str = None) -> str:
        runs = data.get("automation_runs", [])
        matching_runs = []

        for run in runs:
            if run.get("run_type") == run_type:
                matching_runs.append(run.get("run_id"))
        payload = {"automation_run_ids": matching_runs}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchAutomationRunsByType",
                "description": "Searches for automation runs with a specific run type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_type": {
                            "type": "string",
                            "description": "The run type to search for (e.g., plan_freeze, budget_apply, creative_rotation).",
                        }
                    },
                    "required": ["run_type"],
                },
            },
        }


class SearchAutomationRunsByStatus(Tool):
    """Looks for automation runs that have a specific status."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = None) -> str:
        runs = data.get("automation_runs", [])
        matching_runs = []

        for run in runs:
            if run.get("status") == status:
                matching_runs.append(run.get("run_id"))
        payload = {"automation_run_ids": matching_runs}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchAutomationRunsByStatus",
                "description": "Searches for automation runs with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status to search for (e.g., completed, failed).",
                        }
                    },
                    "required": ["status"],
                },
            },
        }


class SearchBudgetChangesByAdSet(Tool):
    """Looks for budget changes related to a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        changes = data.get("budget_changes", [])
        matching_changes = []

        for change in changes:
            if change.get("adset_id") == adset_id:
                matching_changes.append(change.get("change_id"))
        payload = {"budget_change_ids": matching_changes}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchBudgetChangesByAdset",
                "description": "Searches for budget changes for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID to search for.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }


#Tools for Adding/Deleting Campaigns
class DeleteCampaign(Tool):
    """Removes a campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        if not campaign_id:
            payload = {"error": "campaign_id is a required parameter."}
            out = json.dumps(payload)
            return out

        campaigns = data.get("campaigns", [])
        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                data["campaigns"] = [
                    d for d in data["campaigns"] if d["campaign_id"] != campaign_id
                ]
                payload = {
                    "status": "success",
                    "message": f"Campaign with id {campaign_id} deleted successfully",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign with ID '{campaign_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteCampaign",
                "description": "Deletes a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The unique ID of the campaign to delete.",
                        },
                    },
                    "required": ["campaign_id"],
                },
            },
        }


class AddCampaign(Tool):
    """Creates a new campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, name: str = None, objective: str = None, created_date: str = None, status: str = None) -> str:
        if not campaign_id:
            payload = {"error": "campaign_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not name:
            payload = {"error": "name is a required parameter."}
            out = json.dumps(payload)
            return out
        if not objective:
            payload = {"error": "objective is a required parameter."}
            out = json.dumps(payload)
            return out
        if not created_date:
            payload = {"error": "created_date is a required parameter."}
            out = json.dumps(payload)
            return out
        if not status:
            payload = {"error": "status is a required parameter."}
            out = json.dumps(payload)
            return out

        new_campaign = {
            "campaign_id": campaign_id,
            "name": name,
            "objective": objective,
            "created_date": created_date,
            "status": status,
        }
        data["campaigns"] += [new_campaign]
        payload = {
                "status": "success",
                "message": f"New campaign was added: {new_campaign}",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddCampaign",
                "description": "Adds a new campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The unique ID of the new campaign.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the campaign.",
                        },
                        "objective": {
                            "type": "string",
                            "description": "The objective of the campaign (e.g., Sales, Awareness, Traffic).",
                        },
                        "created_date": {
                            "type": "string",
                            "description": "The creation date of the campaign (YYYY-MM-DD format).",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the campaign (e.g., active, paused, archived).",
                        },
                    },
                    "required": [
                        "campaign_id",
                        "name",
                        "objective",
                        "created_date",
                        "status",
                    ],
                },
            },
        }


#Tools for Adding/Deleting Ad Sets
class DeleteAdSet(Tool):
    """Removes an ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        if not adset_id:
            payload = {"error": "adset_id is a required parameter."}
            out = json.dumps(payload)
            return out

        adsets = data.get("adsets", [])
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                data["adsets"] = [
                    d for d in data["adsets"] if d["adset_id"] != adset_id
                ]
                payload = {
                        "status": "success",
                        "message": f"Ad set with id {adset_id} deleted successfully",
                    }
                out = json.dumps(
                    payload)
                return out
        payload = {"error": f"Ad set with ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteAdset",
                "description": "Deletes an ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set to delete.",
                        },
                    },
                    "required": ["adset_id"],
                },
            },
        }


class AddAdSet(Tool):
    """Creates a new ad set."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str = None,
        campaign_id: str = None,
        name: str = None,
        category: str = None,
        daily_budget: float = None,
        bid_strategy: str = None,
        bid_amount: float = None,
        status: str = None,
        updated_at: str = None
    ) -> str:
        if not adset_id:
            payload = {"error": "adset_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not campaign_id:
            payload = {"error": "campaign_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not name:
            payload = {"error": "name is a required parameter."}
            out = json.dumps(payload)
            return out
        if not category:
            payload = {"error": "category is a required parameter."}
            out = json.dumps(payload)
            return out
        if not daily_budget:
            payload = {"error": "daily_budget is a required parameter."}
            out = json.dumps(payload)
            return out
        if not bid_strategy:
            payload = {"error": "bid_strategy is a required parameter."}
            out = json.dumps(payload)
            return out
        if not status:
            payload = {"error": "status is a required parameter."}
            out = json.dumps(payload)
            return out
        if not updated_at:
            payload = {"error": "updated_at is a required parameter."}
            out = json.dumps(payload)
            return out

        new_adset = {
            "adset_id": adset_id,
            "campaign_id": campaign_id,
            "name": name,
            "category": category,
            "daily_budget": daily_budget,
            "bid_strategy": bid_strategy,
            "bid_amount": bid_amount,
            "status": status,
            "updated_at": updated_at,
        }
        data["adsets"] += [new_adset]
        payload = {
            "status": "success",
            "message": f"New ad set was added: {new_adset}",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddAdset",
                "description": "Adds a new ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the new ad set.",
                        },
                        "campaign_id": {
                            "type": "string",
                            "description": "The ID of the campaign this ad set belongs to.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the ad set.",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category of the ad set (e.g., Electronics, Apparel).",
                        },
                        "daily_budget": {
                            "type": "number",
                            "description": "The daily budget for the ad set.",
                        },
                        "bid_strategy": {
                            "type": "string",
                            "description": "The bid strategy (e.g., lowest_cost, cost_cap).",
                        },
                        "bid_amount": {
                            "type": "number",
                            "description": "The bid amount (if applicable).",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the ad set (e.g., active, paused).",
                        },
                        "updated_at": {
                            "type": "string",
                            "description": "The last update timestamp (ISO format).",
                        },
                    },
                    "required": [
                        "adset_id",
                        "campaign_id",
                        "name",
                        "category",
                        "daily_budget",
                        "bid_strategy",
                        "status",
                        "updated_at",
                    ],
                },
            },
        }


#Tools for Adding/Deleting Ads
class DeleteAd(Tool):
    """Removes an ad."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str = None) -> str:
        if not ad_id:
            payload = {"error": "ad_id is a required parameter."}
            out = json.dumps(payload)
            return out

        ads = data.get("ads", [])
        for ad in ads:
            if ad.get("ad_id") == ad_id:
                data["ads"] = [d for d in data["ads"] if d["ad_id"] != ad_id]
                payload = {
                    "status": "success",
                    "message": f"Ad with id {ad_id} deleted successfully",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad with ID '{ad_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteAd",
                "description": "Deletes an ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {
                            "type": "string",
                            "description": "The unique ID of the ad to delete.",
                        },
                    },
                    "required": ["ad_id"],
                },
            },
        }


class AddAd(Tool):
    """Creates a new ad."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        ad_id: str = None,
        adset_id: str = None,
        name: str = None,
        creative_type: str = None,
        status: str = None,
        start_date: str = None,
        end_date: str = None
    ) -> str:
        if not ad_id:
            payload = {"error": "ad_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not adset_id:
            payload = {"error": "adset_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not name:
            payload = {"error": "name is a required parameter."}
            out = json.dumps(payload)
            return out
        if not creative_type:
            payload = {"error": "creative_type is a required parameter."}
            out = json.dumps(payload)
            return out
        if not status:
            payload = {"error": "status is a required parameter."}
            out = json.dumps(payload)
            return out
        if not start_date:
            payload = {"error": "start_date is a required parameter."}
            out = json.dumps(payload)
            return out

        new_ad = {
            "ad_id": ad_id,
            "adset_id": adset_id,
            "name": name,
            "creative_type": creative_type,
            "status": status,
            "start_date": start_date,
            "end_date": end_date,
        }
        data["ads"] += [new_ad]
        payload = {
            "status": "success",
            "message": f"New ad was added: {new_ad}",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addAd",
                "description": "Adds a new ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {
                            "type": "string",
                            "description": "The unique ID of the new ad.",
                        },
                        "adset_id": {
                            "type": "string",
                            "description": "The ID of the ad set this ad belongs to.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the ad.",
                        },
                        "creative_type": {
                            "type": "string",
                            "description": "The creative type (e.g., image, video, carousel).",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the ad (e.g., active, paused, archived).",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the ad (YYYY-MM-DD format).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the ad (YYYY-MM-DD format, optional).",
                        },
                    },
                    "required": [
                        "ad_id",
                        "adset_id",
                        "name",
                        "creative_type",
                        "status",
                        "start_date",
                    ],
                },
            },
        }


#Tools for Adding/Deleting Products
class DeleteProduct(Tool):
    """Removes a product."""

    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None) -> str:
        if not product_id:
            payload = {"error": "product_id is a required parameter."}
            out = json.dumps(payload)
            return out

        products = data.get("dim_product", [])
        for product in products:
            if product.get("product_id") == product_id:
                data["dim_product"] = [
                    d for d in data["dim_product"] if d["product_id"] != product_id
                ]
                payload = {
                    "status": "success",
                    "message": f"Product with id {product_id} deleted successfully",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Product with ID '{product_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteProduct",
                "description": "Deletes a product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "The unique ID of the product to delete.",
                        },
                    },
                    "required": ["product_id"],
                },
            },
        }


class AddProduct(Tool):
    """Creates a new product."""

    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None, sku: str = None, name: str = None, category: str = None) -> str:
        if not product_id:
            payload = {"error": "product_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not sku:
            payload = {"error": "sku is a required parameter."}
            out = json.dumps(payload)
            return out
        if not name:
            payload = {"error": "name is a required parameter."}
            out = json.dumps(payload)
            return out
        if not category:
            payload = {"error": "category is a required parameter."}
            out = json.dumps(payload)
            return out

        new_product = {
            "product_id": product_id,
            "sku": sku,
            "name": name,
            "category": category,
        }
        data["dim_product"] += [new_product]
        payload = {
                "status": "success",
                "message": f"New product was added: {new_product}",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addProduct",
                "description": "Adds a new product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "The unique ID of the new product.",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the product.",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category of the product (e.g., Electronics, Apparel).",
                        },
                    },
                    "required": ["product_id", "sku", "name", "category"],
                },
            },
        }


class SearchAdSetsByCampaignId(Tool):
    """Looks for ad sets that are part of a specific campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        adsets = data.get("adsets", [])
        matching_adsets = []

        for adset in adsets:
            if adset.get("campaign_id") == campaign_id:
                matching_adsets.append(adset.get("adset_id"))
        payload = {"adset_ids": matching_adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchAdsetsByCampaignId",
                "description": "Searches for ad sets belonging to a specific campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The campaign ID to search for ad sets.",
                        }
                    },
                    "required": ["campaign_id"],
                },
            },
        }


#Tools for Calculations and Comparisons
class CalculateROAS(Tool):
    """Computes Return on Ad Spend (ROAS) based on revenue and expenditure."""

    @staticmethod
    def invoke(data: dict[str, Any], revenue: float = None, spend: float = None) -> str:
        if revenue is None or spend is None:
            payload = {"error": "revenue and spend are required parameters."}
            out = json.dumps(payload)
            return out

        if spend == 0:
            payload = {"error": "spend cannot be zero."}
            out = json.dumps(payload)
            return out

        roas = revenue / spend
        payload = {"roas": roas}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculateRoas",
                "description": "Calculates Return on Ad Spend (ROAS) from revenue and spend.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "revenue": {
                            "type": "number",
                            "description": "The revenue generated.",
                        },
                        "spend": {
                            "type": "number",
                            "description": "The amount spent.",
                        },
                    },
                    "required": ["revenue", "spend"],
                },
            },
        }


class CalculateCPA(Tool):
    """Computes Cost Per Acquisition (CPA) using expenditure and purchases."""

    @staticmethod
    def invoke(data: dict[str, Any], spend: float = None, purchases: int = None) -> str:
        if spend is None or purchases is None:
            payload = {"error": "spend and purchases are required parameters."}
            out = json.dumps(payload)
            return out

        if purchases == 0:
            payload = {"error": "purchases cannot be zero."}
            out = json.dumps(payload)
            return out

        cpa = spend / purchases
        payload = {"cpa": cpa}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculateCpa",
                "description": "Calculates Cost Per Acquisition (CPA) from spend and purchases.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "spend": {
                            "type": "number",
                            "description": "The amount spent.",
                        },
                        "purchases": {
                            "type": "number",
                            "description": "The number of purchases.",
                        },
                    },
                    "required": ["spend", "purchases"],
                },
            },
        }


class CompareValue(Tool):
    """Evaluates a value against a threshold with a defined operator."""

    @staticmethod
    def invoke(data: dict[str, Any], value: Any = None, threshold: Any = None, operator: str = None) -> str:
        if value is None or threshold is None or operator is None:
            payload = {"error": "value, threshold, and operator are required parameters."}
            out = json.dumps(payload)
            return out

        result = False
        if operator == "greater":
            result = value > threshold
        elif operator == "greater_equal":
            result = value >= threshold
        elif operator == "less":
            result = value < threshold
        elif operator == "less_equal":
            result = value <= threshold
        elif operator == "equal":
            result = value == threshold
        else:
            payload = {"error": f"Unknown operator: {operator}"}
            out = json.dumps(payload)
            return out
        payload = {"result": result}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CompareValue",
                "description": "Compares a value with a threshold using a specified operator.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "number",
                            "description": "The value to compare.",
                        },
                        "threshold": {
                            "type": "number",
                            "description": "The threshold value.",
                        },
                        "operator": {
                            "type": "string",
                            "description": "The comparison operator (greater, greater_equal, less, less_equal, equal).",
                        },
                    },
                    "required": ["value", "threshold", "operator"],
                },
            },
        }


class IncreaseValueWithPercent(Tool):
    """Boosts a value by a defined percentage."""

    @staticmethod
    def invoke(data: dict[str, Any], value: float = None, percent: float = None) -> str:
        if value is None or percent is None:
            payload = {"error": "value and percent are required parameters."}
            out = json.dumps(payload)
            return out

        new_value = value * (100 + percent) / 100
        payload = {"new_value": new_value}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "IncreaseValueWithPercent",
                "description": "Increases a value by a specified percentage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "number",
                            "description": "The original value.",
                        },
                        "percent": {
                            "type": "number",
                            "description": "The percentage to increase by.",
                        },
                    },
                    "required": ["value", "percent"],
                },
            },
        }


#Tools for Logging Audits
class LogBudgetChange(Tool):
    """Inserts a new record into the budget_changes table."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, old_budget: float = None, new_budget: float = None, changed_at: str = None, reason: str = None) -> str:
        if not adset_id:
            payload = {"error": "adset_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not old_budget:
            payload = {"error": "old_budget is a required parameter."}
            out = json.dumps(payload)
            return out
        if not new_budget:
            payload = {"error": "new_budget is a required parameter."}
            out = json.dumps(payload)
            return out
        if not changed_at:
            payload = {"error": "changed_at is a required parameter."}
            out = json.dumps(payload)
            return out
        if not reason:
            payload = {"error": "reason is a required parameter."}
            out = json.dumps(payload)
            return out

        new_budget_change = {
            "change_id": f"BC-{adset_id}",
            "adset_id": adset_id,
            "old_budget": old_budget,
            "new_budget": new_budget,
            "changed_at": changed_at,
            "reason": reason,
        }

        if "budget_changes" not in data:
            data["budget_changes"] = []

        data["budget_changes"].append(new_budget_change)
        payload = {
                "status": "success",
                "message": f"New budget change was added: {new_budget_change}",
            }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogBudgetChange",
                "description": "Adds a new entry to the budget_changes table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ID of the ad set.",
                        },
                        "old_budget": {
                            "type": "number",
                            "description": "The old budget value.",
                        },
                        "new_budget": {
                            "type": "number",
                            "description": "The new budget value.",
                        },
                        "changed_at": {
                            "type": "string",
                            "description": "The timestamp of the change (ISO format).",
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the budget change.",
                        },
                    },
                    "required": [
                        "change_id",
                        "adset_id",
                        "old_budget",
                        "new_budget",
                        "changed_at",
                        "reason",
                    ],
                },
            },
        }


class LogStrategyChange(Tool):
    """Inserts a new record into the strategy_changes table."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str = None,
        old_strategy: str = None,
        new_strategy: str = None,
        old_bid: float = None,
        new_bid: float = None,
        changed_at: str = None,
        reason: str = None
,
    change_id: Any = None,
    ) -> str:
        if not adset_id:
            payload = {"error": "adset_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not old_strategy:
            payload = {"error": "old_strategy is a required parameter."}
            out = json.dumps(payload)
            return out
        if not new_strategy:
            payload = {"error": "new_strategy is a required parameter."}
            out = json.dumps(payload)
            return out
        if not changed_at:
            payload = {"error": "changed_at is a required parameter."}
            out = json.dumps(payload)
            return out
        if not reason:
            payload = {"error": "reason is a required parameter."}
            out = json.dumps(payload)
            return out

        new_strategy_change = {
            "change_id": f"SC-{adset_id}",
            "adset_id": adset_id,
            "old_strategy": old_strategy,
            "new_strategy": new_strategy,
            "old_bid": old_bid,
            "new_bid": new_bid,
            "changed_at": changed_at,
            "reason": reason,
        }

        if "strategy_changes" not in data:
            data["strategy_changes"] = []

        data["strategy_changes"].append(new_strategy_change)
        payload = {
            "status": "success",
            "message": f"New strategy change was added: {new_strategy_change}",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogStrategyChange",
                "description": "Adds a new entry to the strategy_changes table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ID of the ad set.",
                        },
                        "old_strategy": {
                            "type": "string",
                            "description": "The old bid strategy.",
                        },
                        "new_strategy": {
                            "type": "string",
                            "description": "The new bid strategy.",
                        },
                        "old_bid": {
                            "type": "number",
                            "description": "The old bid amount.",
                        },
                        "new_bid": {
                            "type": "number",
                            "description": "The new bid amount.",
                        },
                        "changed_at": {
                            "type": "string",
                            "description": "The timestamp of the change (ISO format).",
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the strategy change.",
                        },
                    },
                    "required": [
                        "adset_id",
                        "old_strategy",
                        "new_strategy",
                        "changed_at",
                        "reason",
                    ],
                },
            },
        }


class AddAutomationRun(Tool):
    """Inserts a new record into the automation_runs table."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        run_id: str = None,
        run_type: str = None,
        started_at: str = None,
        ended_at: str = None,
        status: str = None,
        input_ref: str = None,
        errors_json: str = None,
        reason: str = None
    ) -> str:
        if not run_id:
            payload = {"error": "run_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not run_type:
            payload = {"error": "run_type is a required parameter."}
            out = json.dumps(payload)
            return out
        if not started_at:
            payload = {"error": "started_at is a required parameter."}
            out = json.dumps(payload)
            return out
        if not ended_at:
            payload = {"error": "ended_at is a required parameter."}
            out = json.dumps(payload)
            return out
        if not status:
            payload = {"error": "status is a required parameter."}
            out = json.dumps(payload)
            return out
        if not input_ref:
            payload = {"error": "input_ref is a required parameter."}
            out = json.dumps(payload)
            return out
        if not errors_json:
            payload = {"error": "errors_json is a required parameter."}
            out = json.dumps(payload)
            return out

        new_automation_run = {
            "run_id": run_id,
            "run_type": run_type,
            "started_at": started_at,
            "ended_at": ended_at,
            "status": status,
            "input_ref": input_ref,
            "errors_json": errors_json,
        }

        if reason:
            new_automation_run["reason"] = reason

        if "automation_runs" not in data:
            data["automation_runs"] = []

        data["automation_runs"].append(new_automation_run)
        payload = {
            "status": "success",
            "message": f"New automation run was added: {new_automation_run}",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddAutomationRun",
                "description": "Adds a new entry to the automation_runs table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {
                            "type": "string",
                            "description": "The unique ID of the automation run.",
                        },
                        "run_type": {
                            "type": "string",
                            "description": "The type of automation run.",
                        },
                        "started_at": {
                            "type": "string",
                            "description": "The start timestamp (ISO format).",
                        },
                        "ended_at": {
                            "type": "string",
                            "description": "The end timestamp (ISO format).",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the run.",
                        },
                        "input_ref": {
                            "type": "string",
                            "description": "The input reference for the run.",
                        },
                        "errors_json": {
                            "type": "string",
                            "description": "JSON string of any errors.",
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the automation run.",
                        },
                    },
                    "required": [
                        "run_id",
                        "run_type",
                        "started_at",
                        "ended_at",
                        "status",
                        "input_ref",
                        "errors_json",
                    ],
                },
            },
        }


#Tools for Bid Strategies
class UpdateBidStrategyForAdSet(Tool):
    """Modifies the bid strategy of a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, new_strategy: str = None, new_bid: float = None) -> str:
        adsets = data.get("adsets", [])
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                old_strategy = adset["bid_strategy"]
                adset["bid_amount"]
                adset["bid_strategy"] = new_strategy
                adset["bid_amount"] = new_bid
                payload = {
                    "status": "success",
                    "message": f"Ad set bid strategy updated from '{old_strategy}' to '{new_strategy}' with bid {new_bid}",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set {adset_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateBidStrategyForAdset",
                "description": "Updates the bid strategy for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_strategy": {"type": "string"},
                        "new_bid": {"type": "number"},
                    },
                    "required": ["adset_id", "new_strategy", "new_bid"],
                },
            },
        }


#Tools for Ad Set Status
class UpdateAdSetStatus(Tool):
    """Modifies the status of a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, new_status: str = None) -> str:
        adsets = data.get("adsets", [])
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                old_status = adset["status"]
                adset["status"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Ad set status updated from '{old_status}' to '{new_status}'",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set {adset_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdsetStatus",
                "description": "Updates the status for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["adset_id", "new_status"],
                },
            },
        }


#Tools for Managing Plans
class CreatePlanAllocation(Tool):
    """Establishes a plan allocation for an ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, budget: float = None, bid_strategy: str = None, bid_amount: float = None, creative_type: str = None) -> str:
        # This tool is generally utilized for developing a complete plan
        # Currently, we will only provide the allocation information
        allocation = {
            "adset_id": adset_id,
            "budget": budget,
            "bid_strategy": bid_strategy,
            "bid_amount": bid_amount,
            "creative_type": creative_type,
        }
        payload = {"status": "success", "allocation": allocation}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createPlanAllocation",
                "description": "Creates a plan allocation for an ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ID of the ad set.",
                        },
                        "budget": {
                            "type": "number",
                            "description": "The allocated budget.",
                        },
                        "bid_strategy": {
                            "type": "string",
                            "description": "The bid strategy.",
                        },
                        "bid_amount": {
                            "type": "number",
                            "description": "The bid amount.",
                        },
                        "creative_type": {
                            "type": "string",
                            "description": "The creative type.",
                        },
                    },
                    "required": ["adset_id", "budget", "bid_strategy", "creative_type"],
                },
            },
        }


#Tools for Policy Parameters
class GetPolicyParam(Tool):
    """Fetches the value of a policy parameter."""

    @staticmethod
    def invoke(data: dict[str, Any], param_name: str = None) -> str:
        policy_params = data.get("policy_params", [])

        for param in policy_params:
            if param.get("param_name") == param_name:
                payload = {"param_value": param.get("param_value")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Policy parameter '{param_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyParam",
                "description": "Retrieves a policy parameter value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "param_name": {
                            "type": "string",
                            "description": "The name of the policy parameter.",
                        }
                    },
                    "required": ["param_name"],
                },
            },
        }


class UpdatePolicyParam(Tool):
    """Modifies the value of a policy parameter."""

    @staticmethod
    def invoke(data: dict[str, Any], param_name: str = None, param_value: Any = None, updated_at: str = None) -> str:
        policy_params = data.get("policy_params", [])
        for param in policy_params:
            if param.get("param_name") == param_name:
                old_value = param["param_value"]
                param["param_value"] = param_value
                param["updated_at"] = updated_at
                payload = {
                    "status": "success",
                    "message": f"Policy parameter '{param_name}' updated from '{old_value}' to '{param_value}'",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Policy parameter '{param_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdatePolicyParam",
                "description": "Updates a policy parameter value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "param_name": {"type": "string"},
                        "param_value": {"type": "string"},
                        "updated_at": {"type": "string"},
                    },
                    "required": ["param_name", "param_value", "updated_at"],
                },
            },
        }


#Extra utility tools
class CheckNoPurchases(Tool):
    """Verifies if a list of purchase counts consists solely of zeros."""

    @staticmethod
    def invoke(data: dict[str, Any], purchases_list: list[int] = None) -> str:
        if purchases_list is None:
            payload = {"error": "purchases_list is a required parameter."}
            out = json.dumps(payload)
            return out

        all_zeros = all(purchase == 0 for purchase in purchases_list)
        payload = {"all_zeros": all_zeros}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "checkNoPurchases",
                "description": "Checks if a list of purchase counts contains only zeros.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "purchases_list": {
                            "type": "array",
                            "description": "List of purchase counts.",
                            "items": {"type": "number"},
                        }
                    },
                    "required": ["purchases_list"],
                },
            },
        }


class CalculatePercentageChange(Tool):
    """Computes the percentage difference in revenue between two amounts."""

    @staticmethod
    def invoke(data: dict[str, Any], current_value: float = None, previous_value: float = None) -> str:
        if current_value is None or previous_value is None:
            payload = {"error": "current_value and previous_value are required parameters."}
            out = json.dumps(payload)
            return out

        if previous_value == 0:
            payload = {"error": "previous_value cannot be zero."}
            out = json.dumps(payload)
            return out

        change_percent = ((current_value - previous_value) / previous_value) * 100
        payload = {"change_percent": change_percent}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculatePercentageChange",
                "description": "Calculates the percentage change between two values.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_value": {
                            "type": "number",
                            "description": "The current value.",
                        },
                        "previous_value": {
                            "type": "number",
                            "description": "The previous value.",
                        },
                    },
                    "required": ["current_value", "previous_value"],
                },
            },
        }


class CalculateSpendVariance(Tool):
    """Computes the percentage variance between projected and actual expenditure."""

    @staticmethod
    def invoke(data: dict[str, Any], planned_spend: float = None, actual_spend: float = None) -> str:
        if planned_spend is None or actual_spend is None:
            payload = {"error": "planned_spend and actual_spend are required parameters."}
            out = json.dumps(payload)
            return out

        if planned_spend == 0:
            payload = {"error": "planned_spend cannot be zero."}
            out = json.dumps(payload)
            return out

        variance_percent = ((actual_spend - planned_spend) / planned_spend) * 100
        payload = {"variance_percent": variance_percent}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateSpendVariance",
                "description": "Calculates the variance percentage between planned and actual spend.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "planned_spend": {
                            "type": "number",
                            "description": "The planned spend amount.",
                        },
                        "actual_spend": {
                            "type": "number",
                            "description": "The actual spend amount.",
                        },
                    },
                    "required": ["planned_spend", "actual_spend"],
                },
            },
        }


class CalculateCampaignROASForPeriod(Tool):
    """Computes ROAS for a campaign during a specified timeframe."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, start_date: str = None, end_date: str = None) -> str:
        adsets = data.get("adsets", [])
        campaign_adsets = [
            adset for adset in adsets if adset.get("campaign_id") == campaign_id
        ]
        adset_ids = [adset.get("adset_id") for adset in campaign_adsets]

        insights = data.get("f_insights", [])
        total_revenue = 0
        total_spend = 0

        for insight in insights:
            if (
                insight.get("adset_id") in adset_ids
                and start_date <= insight.get("date") <= end_date
            ):
                total_revenue += insight.get("revenue", 0)
                total_spend += insight.get("spend", 0)

        if total_spend == 0:
            payload = {"error": "No spend found for the period."}
            out = json.dumps(payload)
            return out

        roas = total_revenue / total_spend
        payload = {"roas": roas}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculateCampaignRoasForPeriod",
                "description": "Calculates ROAS for a campaign over a period.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The campaign ID.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date in YYYY-MM-DD format.",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["campaign_id", "start_date", "end_date"],
                },
            },
        }


class CalculateROASForAdSetForPeriod(Tool):
    """Computes ROAS for a specific ad set during a specified timeframe."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, start_date: str = None, end_date: str = None) -> str:
        insights = data.get("f_insights", [])
        total_revenue = 0
        total_spend = 0

        for insight in insights:
            if (
                insight.get("adset_id") == adset_id
                and start_date <= insight.get("date") <= end_date
            ):
                total_revenue += insight.get("revenue", 0)
                total_spend += insight.get("spend", 0)

        if total_spend == 0:
            payload = {"error": "No spend found for the period."}
            out = json.dumps(payload)
            return out

        roas = total_revenue / total_spend
        payload = {"roas": roas}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateAdsetRoasForPeriod",
                "description": "Calculates ROAS for a specific ad set over a period.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date in YYYY-MM-DD format.",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["adset_id", "start_date", "end_date"],
                },
            },
        }


class CalculateCPAForAdSetForPeriod(Tool):
    """Computes CPA for a specific ad set during a specified timeframe."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, start_date: str = None, end_date: str = None) -> str:
        insights = data.get("f_insights", [])
        total_spend = 0
        total_purchases = 0

        for insight in insights:
            if (
                insight.get("adset_id") == adset_id
                and start_date <= insight.get("date") <= end_date
            ):
                total_spend += insight.get("spend", 0)
                total_purchases += insight.get("purchases", 0)

        if total_purchases == 0:
            payload = {"cpa": 0}
            out = json.dumps(payload)
            return out
            payload = {"error": "No purchases found for the period."}
            out = json.dumps(payload)
            return out

        cpa = total_spend / total_purchases
        payload = {"cpa": cpa}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateAdsetCpaForPeriod",
                "description": "Calculates CPA for a specific ad set over a period.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date in YYYY-MM-DD format.",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["adset_id", "start_date", "end_date"],
                },
            },
        }


class CalculateROASForAdSetForDay(Tool):
    """Computes ROAS for a specific ad set on a particular day."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None) -> str:
        insights = data.get("f_insights", [])

        for insight in insights:
            if insight.get("adset_id") == adset_id and insight.get("date") == date:
                revenue = insight.get("revenue", 0)
                spend = insight.get("spend", 0)
                if spend == 0:
                    payload = {"error": "Spend is zero, cannot calculate ROAS."}
                    out = json.dumps(payload)
                    return out
                roas = revenue / spend
                payload = {"roas": roas}
                out = json.dumps(payload)
                return out
        payload = {"error": f"No insights found for ad set {adset_id} on date {date}."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateAdsetRoasForDay",
                "description": "Calculates ROAS for a specific ad set on a specific day.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID.",
                        },
                        "date": {
                            "type": "string",
                            "description": "The date in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["adset_id", "date"],
                },
            },
        }


class CalculateCPAForAdSetForDay(Tool):
    """Computes CPA for a specific ad set on a particular day."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None) -> str:
        insights = data.get("f_insights", [])

        for insight in insights:
            if insight.get("adset_id") == adset_id and insight.get("date") == date:
                spend = insight.get("spend", 0)
                purchases = insight.get("purchases", 0)
                if purchases == 0:
                    payload = {"error": "No purchases, cannot calculate CPA."}
                    out = json.dumps(payload)
                    return out
                cpa = spend / purchases
                payload = {"cpa": cpa}
                out = json.dumps(payload)
                return out
        payload = {"error": f"No insights found for ad set {adset_id} on date {date}."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculateAdsetCpaForDay",
                "description": "Calculates CPA for a specific ad set on a specific day.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID.",
                        },
                        "date": {
                            "type": "string",
                            "description": "The date in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["adset_id", "date"],
                },
            },
        }


class SearchAdSetsByName(Tool):
    """Looks for ad sets whose names include the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        adsets = data.get("adsets", [])
        matching_adsets = []
        
        if not name_query:
            payload = {"adset_ids": []}
            out = json.dumps(payload)
            return out

        for adset in adsets:
            if name_query.lower() in adset.get("name", "").lower():
                matching_adsets.append(adset.get("adset_id"))
        payload = {"adset_ids": matching_adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchAdsetsByName",
                "description": "Searches for ad sets with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in ad set names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }


class SearchCampaignsByName(Tool):
    """Looks for campaigns whose names include the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        campaigns = data.get("campaigns", [])
        matching_campaigns = []
        
        if not name_query:
            payload = {"campaign_ids": []}
            out = json.dumps(payload)
            return out

        for campaign in campaigns:
            if name_query.lower() in campaign.get("name", "").lower():
                matching_campaigns.append(campaign.get("campaign_id"))
        payload = {"campaign_ids": matching_campaigns}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchCampaignsByName",
                "description": "Searches for campaigns with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in campaign names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }


class GetCurrentTimestamp(Tool):
    """Provides a fixed current timestamp value."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = {"timestamp": "2025-08-13T01:01:01Z"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCurrentTimestamp",
                "description": "Returns a hardcoded current timestamp value (2025-08-13T01:01:01Z).",
                "parameters": {},
            },
        }


class DeleteAutomationRun(Tool):
    """Removes a record of an automation run."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None) -> str:
        if not run_id:
            payload = {"error": "run_id is a required parameter."}
            out = json.dumps(payload)
            return out

        runs = data.get("automation_runs", [])
        original_count = len(runs)
        data["automation_runs"] = [r for r in runs if r.get("run_id") != run_id]

        if len(data["automation_runs"]) < original_count:
            payload = {
                    "status": "success",
                    "message": f"Automation run with id {run_id} deleted successfully.",
                }
            out = json.dumps(
                payload)
            return out
        else:
            payload = {"error": f"Automation run with ID '{run_id}' not found."}
            out = json.dumps(
                payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteAutomationRun",
                "description": "Deletes an automation run record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {
                            "type": "string",
                            "description": "The unique ID of the automation run to delete.",
                        },
                    },
                    "required": ["run_id"],
                },
            },
        }


class AddPlan(Tool):
    """Creates a new plan."""

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, date: str = None, author: str = None, allocations: list = None) -> str:
        if not all([plan_id, date, author, allocations]):
            payload = {
                    "error": "plan_id, date, author, and allocations are required parameters."
                }
            out = json.dumps(
                payload)
            return out

        # Fundamental checks for allocations
        if not isinstance(allocations, list):
            payload = {"error": "allocations must be a list."}
            out = json.dumps(payload)
            return out

        total_budget = sum(alloc.get("budget", 0) for alloc in allocations)

        new_plan = {
            "plan_id": plan_id,
            "date": date,
            "total_budget": total_budget,
            "author": author,
            "created_at": "2025-08-13T01:01:01Z",  # Employing a fixed timestamp for uniformity
            "checksum": "manual_override_checksum",
            "allocations": allocations,
        }

        if "plans" not in data:
            data["plans"] = []
        data["plans"].append(new_plan)
        payload = {
                "status": "success",
                "message": f"New plan was added: {new_plan}",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addPlan",
                "description": "Adds a new plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "date": {"type": "string"},
                        "author": {"type": "string"},
                        "allocations": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["plan_id", "date", "author", "allocations"],
                },
            },
        }


class GetStatusForAdSet(Tool):
    """Fetches the current status of a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        adsets = data.get("adsets", [])

        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                payload = {"status": adset.get("status")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set with ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetStatusForAdset",
                "description": "Retrieves the status for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }


class DecreaseValueWithPercent(Tool):
    """Reduces a value by a defined percentage."""

    @staticmethod
    def invoke(data: dict[str, Any], value: float = None, percent: float = None) -> str:
        if value is None or percent is None:
            payload = {"error": "value and percent are required parameters."}
            out = json.dumps(payload)
            return out

        new_value = value * (100 - percent) / 100
        payload = {"new_value": new_value}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DecreaseValueWithPercent",
                "description": "Decreases a value by a specified percentage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "number",
                            "description": "The original value.",
                        },
                        "percent": {
                            "type": "number",
                            "description": "The percentage to decrease by.",
                        },
                    },
                    "required": ["value", "percent"],
                },
            },
        }


class RoundNumberToUnit(Tool):
    """Rounds a number to the closest multiple of a defined unit."""

    @staticmethod
    def invoke(data: dict[str, Any], number: float = None, unit: float = None) -> str:
        if number is None or unit is None:
            payload = {"error": "number and unit are required parameters."}
            out = json.dumps(payload)
            return out

        if unit <= 0:
            payload = {"error": "unit must be a positive number."}
            out = json.dumps(payload)
            return out

        rounded_number = round(number / unit) * unit
        payload = {"rounded_number": rounded_number}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RoundNumberToUnit",
                "description": "Rounds a number to the nearest multiple of a specified unit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "number": {
                            "type": "number",
                            "description": "The number to round.",
                        },
                        "unit": {
                            "type": "number",
                            "description": "The unit to round to (e.g., 10 for rounding to nearest 10).",
                        },
                    },
                    "required": ["number", "unit"],
                },
            },
        }


class SearchAdsByName(Tool):
    """Looks for ads whose names include the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        ads = data.get("ads", [])
        matching_ads = []
        
        if not name_query:
            payload = {"ad_ids": []}
            out = json.dumps(payload)
            return out

        for ad in ads:
            if name_query.lower() in ad.get("name", "").lower():
                matching_ads.append(ad.get("ad_id"))
        payload = {"ad_ids": matching_ads}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchAdsByName",
                "description": "Searches for ads with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in ad names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }


class SearchAdsByAdSet(Tool):
    """Looks for ads that are part of a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        ads = data.get("ads", [])
        matching_ads = []

        for ad in ads:
            if ad.get("adset_id") == adset_id:
                matching_ads.append(ad.get("ad_id"))
        payload = {"ad_ids": matching_ads}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchAdsByAdset",
                "description": "Searches for ads belonging to a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID to search for ads.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }


class GetBidStrategyForAdSet(Tool):
    """Fetches the bid strategy associated with a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        adsets = data.get("adsets", [])

        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                payload = {"bid_strategy": adset.get("bid_strategy")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set with ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBidStrategyForAdset",
                "description": "Retrieves the bid strategy for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }


class GetBidAmountForAdSet(Tool):
    """Fetches the bid amount set for a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        adsets = data.get("adsets", [])

        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                payload = {"bid_amount": adset.get("bid_amount")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set with ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBidAmountForAdset",
                "description": "Retrieves the bid amount for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }


class GetAllocationsForPlan(Tool):
    """Fetches the allocations linked to a specific plan."""

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None) -> str:
        plans = data.get("plans", [])

        for plan in plans:
            if plan.get("plan_id") == plan_id:
                payload = {"allocations": plan.get("allocations", [])}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Plan with ID '{plan_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllocationsForPlan",
                "description": "Retrieves the allocations for a specific plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The unique ID of the plan.",
                        }
                    },
                    "required": ["plan_id"],
                },
            },
        }


class GetCategoryForProduct(Tool):
    """Fetches the category associated with a specific product."""

    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None) -> str:
        products = data.get("dim_product", [])

        for product in products:
            if product.get("product_id") == product_id:
                payload = {"category": product.get("category")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Product with ID '{product_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCategoryForProduct",
                "description": "Retrieves the category for a specific product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "The unique ID of the product.",
                        }
                    },
                    "required": ["product_id"],
                },
            },
        }


class SearchProductsByName(Tool):
    """Looks for products whose names include the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        products = data.get("dim_product", [])
        matching_products = []
        
        if not name_query:
            payload = {"product_ids": []}
            out = json.dumps(payload)
            return out

        for product in products:
            if name_query.lower() in product.get("name", "").lower():
                matching_products.append(product.get("product_id"))
        payload = {"product_ids": matching_products}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchProductsByName",
                "description": "Searches for products with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in product names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }


class SearchAdSetsByBidStrategy(Tool):
    """Looks for ad sets that utilize a specific bid strategy."""

    @staticmethod
    def invoke(data: dict[str, Any], bid_strategy: str = None) -> str:
        adsets = data.get("adsets", [])
        matching_adsets = []

        for adset in adsets:
            if adset.get("bid_strategy") == bid_strategy:
                matching_adsets.append(adset.get("adset_id"))
        payload = {"adset_ids": matching_adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchAdsetsByBidStrategy",
                "description": "Searches for ad sets with a specific bid strategy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "bid_strategy": {
                            "type": "string",
                            "description": "The bid strategy to search for (e.g., cost_cap, lowest_cost).",
                        }
                    },
                    "required": ["bid_strategy"],
                },
            },
        }


class GetBidStrategyForAdSet(Tool):
    """Fetches the bid strategy linked to a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        adsets = data.get("adsets", [])

        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                payload = {"bid_strategy": adset.get("bid_strategy")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set with ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBidStrategyForAdset",
                "description": "Retrieves the bid strategy for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }


class GetViewershipForDateAndCategory(Tool):
    """Fetches viewership statistics for a specific date and category."""

    @staticmethod
    def invoke(data: dict[str, Any], date: str = None, category: str = None) -> str:
        viewership_data = data.get("f_viewership", [])

        for entry in viewership_data:
            if entry.get("date") == date and entry.get("category") == category:
                payload = {
                    "sessions": entry.get("sessions"),
                    "active_users": entry.get("active_users"),
                }
                out = json.dumps(payload)
                return out
        payload = {
            "error": f"No viewership data found for category '{category}' on date '{date}'."
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetViewershipForDateAndCategory",
                "description": "Retrieves viewership data for a specific date and category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "The date to get viewership for (YYYY-MM-DD format).",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category to get viewership for.",
                        },
                    },
                    "required": ["date", "category"],
                },
            },
        }


class GetTotalViewershipForCategoryInPeriod(Tool):
    """Computes total viewership for a category within a date range."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, start_date: str = None, end_date: str = None) -> str:
        viewership_data = data.get("f_viewership", [])

        total_sessions = 0
        total_active_users = 0

        for entry in viewership_data:
            if (
                entry.get("category") == category
                and start_date <= entry.get("date") <= end_date
            ):
                total_sessions += entry.get("sessions", 0)
                total_active_users += entry.get("active_users", 0)
        payload = {"total_sessions": total_sessions, "total_active_users": total_active_users}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTotalViewershipForCategoryInPeriod",
                "description": "Calculates total viewership for a category over a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to analyze.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the period (YYYY-MM-DD format).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the period (YYYY-MM-DD format).",
                        },
                    },
                    "required": ["category", "start_date", "end_date"],
                },
            },
        }


class GetAverageViewershipForCategoryInPeriod(Tool):
    """Computes average daily viewership for a category across a date range."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str, start_date: str, end_date: str) -> str:
        viewership_data = data.get("f_viewership", [])

        # Determine the total days within the timeframe
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        days_in_period = (end - start).days + 1

        total_sessions = 0
        total_active_users = 0
        days_with_data = 0

        for entry in viewership_data:
            if (
                entry.get("category") == category
                and start_date <= entry.get("date") <= end_date
            ):
                total_sessions += entry.get("sessions", 0)
                total_active_users += entry.get("active_users", 0)
                days_with_data += 1

        # Compute averages
        avg_sessions = total_sessions / days_in_period if days_in_period > 0 else 0
        avg_active_users = (
            total_active_users / days_in_period if days_in_period > 0 else 0
        )
        payload = {
            "average_sessions": avg_sessions,
            "average_active_users": avg_active_users,
            "days_in_period": days_in_period,
            "days_with_data": days_with_data,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAverageViewershipForCategoryInPeriod",
                "description": "Calculates average daily viewership for a category over a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to analyze.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the period (YYYY-MM-DD format).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the period (YYYY-MM-DD format).",
                        },
                    },
                    "required": ["category", "start_date", "end_date"],
                },
            },
        }


class GetSalesForCategoryInPeriod(Tool):
    """Fetches sales statistics for a specific category within a date range."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, start_date: str = None, end_date: str = None) -> str:
        sales_data = data.get("f_sales", [])

        matching_sales = []

        for entry in sales_data:
            if (
                entry.get("category") == category
                and entry.get("start_date") >= start_date
                and entry.get("end_date") <= end_date
            ):
                matching_sales.append(entry)
        payload = {"sales_data": matching_sales}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSalesForCategoryInPeriod",
                "description": "Retrieves sales data for a specific category and date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to analyze.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the period (YYYY-MM-DD format).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the period (YYYY-MM-DD format).",
                        },
                    },
                    "required": ["category", "start_date", "end_date"],
                },
            },
        }


class GetAverageDailySalesForCategoryInPeriod(Tool):
    """Computes average daily sales for a category during a date range."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, start_date: str = None, end_date: str = None) -> str:
        sales_data = data.get("f_sales", [])

        # Determine the total days within the timeframe
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        days_in_period = (end - start).days + 1

        total_units = 0
        total_revenue = 0

        for entry in sales_data:
            if (
                entry.get("category") == category
                and entry.get("start_date") >= start_date
                and entry.get("end_date") <= end_date
            ):
                total_units += entry.get("units", 0)
                total_revenue += entry.get("revenue", 0)

        # Compute averages
        avg_units = total_units / days_in_period if days_in_period > 0 else 0
        avg_revenue = total_revenue / days_in_period if days_in_period > 0 else 0
        payload = {
            "average_units": avg_units,
            "average_revenue": avg_revenue,
            "days_in_period": days_in_period,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAverageDailySalesForCategoryInPeriod",
                "description": "Calculates average daily sales for a category over a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to analyze.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the period (YYYY-MM-DD format).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the period (YYYY-MM-DD format).",
                        },
                    },
                    "required": ["category", "start_date", "end_date"],
                },
            },
        }


#--- Compilation of all accessible tools ---
TOOLS = [
    GetCampaigns(),
    GetNameForCampaign(),
    GetObjectiveForCampaign(),
    GetStatusForCampaign(),
    UpdateCampaignStatus(),
    GetAdSets(),
    GetNameForAdSet(),
    GetCampaignIdForAdSet(),
    GetDailyBudgetForAdSet(),
    UpdateDailyBudgetForAdSet(),
    GetAds(),
    GetNameForAd(),
    GetStatusForAd(),
    UpdateAdStatus(),
    GetProducts(),
    GetNameForProduct(),
    GetPlans(),
    GetDateForPlan(),
    GetAutomationRuns(),
    GetRunTypeForAutomationRun(),
    GetBudgetChanges(),
    GetAdSetIdForBudgetChange(),
    SearchCampaignsByObjective(),
    SearchCampaignsByStatus(),
    SearchAdSetsByCategory(),
    SearchAdSetsByStatus(),
    SearchAdsByCreativeType(),
    SearchAdsByStatus(),
    SearchProductsByCategory(),
    SearchAutomationRunsByType(),
    SearchAutomationRunsByStatus(),
    SearchBudgetChangesByAdSet(),
    DeleteCampaign(),
    AddCampaign(),
    DeleteAdSet(),
    AddAdSet(),
    DeleteAd(),
    AddAd(),
    DeleteProduct(),
    AddProduct(),
    SearchAdSetsByCampaignId(),
    CalculateROAS(),
    CalculateCPA(),
    CompareValue(),
    IncreaseValueWithPercent(),
    LogBudgetChange(),
    LogStrategyChange(),
    AddAutomationRun(),
    UpdateBidStrategyForAdSet(),
    UpdateAdSetStatus(),
    CreatePlanAllocation(),
    GetPolicyParam(),
    UpdatePolicyParam(),
    CheckNoPurchases(),
    CalculatePercentageChange(),
    CalculateSpendVariance(),
    CalculateCampaignROASForPeriod(),
    CalculateROASForAdSetForPeriod(),
    CalculateCPAForAdSetForPeriod(),
    CalculateROASForAdSetForDay(),
    CalculateCPAForAdSetForDay(),
    SearchAdSetsByName(),
    SearchCampaignsByName(),
    GetCurrentTimestamp(),
    DeleteAutomationRun(),
    AddPlan(),
    GetStatusForAdSet(),
    DecreaseValueWithPercent(),
    RoundNumberToUnit(),
    SearchAdsByName(),
    SearchAdsByAdSet(),
    GetCreativeTypeForAd(),
    GetBidStrategyForAdSet(),
    GetBidAmountForAdSet(),
    GetAllocationsForPlan(),
    GetCategoryForProduct(),
    SearchProductsByName(),
    SearchAdSetsByBidStrategy(),
    GetBidStrategyForAdSet(),
    GetViewershipForDateAndCategory(),
    GetTotalViewershipForCategoryInPeriod(),
    GetAverageViewershipForCategoryInPeriod(),
    GetSalesForCategoryInPeriod(),
    GetAverageDailySalesForCategoryInPeriod(),
]
