# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterByProductIdPerProductName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], product_names: List[str], product_ids: List[str] = None) -> str:
        """
        Filter and get product IDs based on product names (case-insensitive search)
        Returns product IDs in the same order as input product names
        Optionally filters results to only include products from a specified list of product IDs

        Data Sources: products.json (product_id, name)
        """
        if not product_names:
            return json.dumps({
                "error": "Product names list cannot be empty",
                "status": "failed"
            })

        # Clean and validate input
        cleaned_product_names = []
        for name in product_names:
            if not name or not str(name).strip():
                cleaned_product_names.append("")
            else:
                cleaned_product_names.append(str(name).strip())

        # Convert product_ids filter to set for faster lookup
        product_ids_filter = None
        if product_ids:
            product_ids_filter = set(product_ids)

        products = list(data.get("products", {}).values())
        result_mapping = []
        total_matches = 0
        total_not_found = 0
        total_filtered_out = 0

        # Process each product name in order
        for i, search_name in enumerate(cleaned_product_names):
            if not search_name:
                result_mapping.append({
                    "index": i,
                    "search_name": search_name,
                    "product_id": None,
                    "product_name": None,
                    "match_type": "empty_input",
                    "status": "failed"
                })
                total_not_found += 1
                continue

            # Find matching product (case-insensitive)
            matching_product = None
            match_type = "not_found"

            for product in products:
                stored_name = product.get("name", "")
                product_id = product.get("product_id")

                # Apply product_ids filter if specified
                if product_ids_filter and product_id not in product_ids_filter:
                    continue  # Skip products not in the filter list

                # Exact match (case-insensitive)
                if stored_name.lower() == search_name.lower():
                    matching_product = product
                    match_type = "exact_match"
                    break
                # Partial match (case-insensitive) - only if no exact match found
                elif search_name.lower() in stored_name.lower() and not matching_product:
                    matching_product = product
                    match_type = "partial_match"

            if matching_product:
                result_mapping.append({
                    "index": i,
                    "search_name": search_name,
                    "product_id": matching_product.get("product_id"),
                    "product_name": matching_product.get("name"),
                    "match_type": match_type,
                    "status": "success"
                })
                total_matches += 1
            else:
                # Check if there would have been a match without the product_ids filter
                if product_ids_filter:
                    found_without_filter = False
                    for product in products:
                        stored_name = product.get("name", "")
                        if (stored_name.lower() == search_name.lower() or
                            search_name.lower() in stored_name.lower()):
                            found_without_filter = True
                            break

                    if found_without_filter:
                        result_mapping.append({
                            "index": i,
                            "search_name": search_name,
                            "product_id": None,
                            "product_name": None,
                            "match_type": "filtered_out",
                            "status": "failed"
                        })
                        total_filtered_out += 1
                    else:
                        result_mapping.append({
                            "index": i,
                            "search_name": search_name,
                            "product_id": None,
                            "product_name": None,
                            "match_type": "not_found",
                            "status": "failed"
                        })
                        total_not_found += 1
                else:
                    result_mapping.append({
                        "index": i,
                        "search_name": search_name,
                        "product_id": None,
                        "product_name": None,
                        "match_type": "not_found",
                        "status": "failed"
                    })
                    total_not_found += 1

        # Create simple arrays for easy access
        product_ids_array = [mapping.get("product_id") for mapping in result_mapping]
        successful_matches = [mapping for mapping in result_mapping if mapping["status"] == "success"]
        failed_matches = [mapping for mapping in result_mapping if mapping["status"] == "failed"]
        filtered_out_matches = [mapping for mapping in failed_matches if mapping.get("match_type") == "filtered_out"]

        result = {
            "status": "success",
            "search_criteria": {
                "product_names": product_names,
                "product_ids_filter": product_ids,
                "filter_applied": product_ids_filter is not None
            },
            "search_summary": {
                "total_searches": len(cleaned_product_names),
                "successful_matches": total_matches,
                "failed_matches": total_not_found,
                "filtered_out_matches": total_filtered_out,
                "match_rate_percent": round((total_matches / len(cleaned_product_names) * 100), 1) if cleaned_product_names else 0,
                "filter_effectiveness": {
                    "would_match_without_filter": total_matches + total_filtered_out,
                    "matches_after_filter": total_matches,
                    "reduction_percent": round((total_filtered_out / (total_matches + total_filtered_out) * 100), 1) if (total_matches + total_filtered_out) > 0 else 0
                } if product_ids_filter else None
            },
            "product_ids": product_ids_array,
            "detailed_mapping": result_mapping,
            "successful_matches": successful_matches,
            "failed_matches": failed_matches,
            "filtered_out_matches": filtered_out_matches
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filter_by_product_id_per_product_name",
                "description": "Filter and get product IDs based on product names with case-insensitive search. Returns product IDs in the same order as input product names, with null values for unmatched names. Optionally filters results to only include products from a specified list of product IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_names": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of product names to search for (case-insensitive, supports partial matching). Returns corresponding product IDs at the same index positions."
                        },
                        "product_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of product IDs to filter results. Only products with IDs in this list will be considered for matching. If not provided, all products are considered."
                        }
                    },
                    "required": ["product_names"]
                }
            }
        }
