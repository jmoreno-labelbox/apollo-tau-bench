
tasks = [
    {
        "annotator": 0,
        "user_id": "001",
        "instruction": "Acting as a meal planning assistant for the Bennett Family, your task is to delete 'Grilled Salmon with Lemon' from their meal plan for the week of Aug 25, 2025, to Aug 31, 2025. The removal reason is noted as 'temporary fish aversion'. Substitute it with 'Chicken Tacos' on the same date (2025-08-27) and include a note to 'use mild seasoning'. Additionally, record these changes in the audit trail and use 'replacement for salmon' as the reason for adding the new dish. Ensure this adjustment is applied solely to them and not to other clients.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Bennett Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Grilled Salmon with Lemon"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 404
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6001,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "salmon"
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6103
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chicken Tacos"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6001,
                    "plan_date": "2025-08-27",
                    "recipe_id": 402,
                    "notes": "use mild seasoning"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6103,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "temporary fish aversion"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "replacement for salmon"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "002",
        "instruction": "Serving as assistance to Sofia Martinez (user 102) from the Martinez Household (household 202), note that she has run out of 'Turkey Deli Slices' (ingredient 1039, inventory item 7022), so you need to update her inventory to show a quantity of 0. She also wishes to add 'Chicken Breast' (ingredient 1001) to her grocery list (list_id 8002) as she intends to prepare a different lunch. Add 500g of chicken breast to the list. Document the inventory update in the audit logs.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Sofia Martinez"
                },
            },
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Martinez Household"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Turkey Deli Slices"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Chicken Breast"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 202,
                    "ingredient_id": 1039
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 202,
                    "ingredient_id": 1001
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7022,
                    "new_quantity": 0
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8002,
                    "ingredient_id": 1001,
                    "quantity": 500,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "inventory_items",
                    "entity_id": 7022,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "quantity",
                        "new_value": 0
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "003",
        "instruction": "Support Emily Wang in the development of a meal plan. Arrange a weekly meal plan for her household beginning '2025-09-01'. Subsequently, include the 'Teriyaki Tofu Bowl' for '2025-09-01' and the 'Mediterranean Quinoa Salad' on '2025-09-02'. Record the meal plan creation in the audit logs.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Emily Wang"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 103
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Teriyaki Tofu Bowl"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Mediterranean Quinoa Salad"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 203,
                    "week_start_date": "2025-09-01",
                    "created_by_user_id": 103
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-01",
                    "recipe_id": 405,
                    "notes": ""
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-02",
                    "recipe_id": 406,
                    "notes": ""
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 203,
                    "user_id": 103,
                    "entity_type": "meal_plans",
                    "entity_id": 6003,
                    "action_enum": "create"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "004",
        "instruction": "Assist the Brown-Brown Family (household 204). They require a fresh meal plan for the week commencing '2025-09-01' and a corresponding grocery list. Generate a new grocery list associated with this meal plan. Insert 'Gluten-Free Pasta' (ingredient 1065, 400g) and 'Almond Milk' (ingredient 1092, 1000ml) into this list. Finally, document the creation of the grocery list.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Brown-Brown Family"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 204,
                    "week_start_date": "2025-09-01",
                    "created_by_user_id": 104
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 204,
                    "meal_plan_id": 6003,
                    "user_id": 104
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Gluten-Free Pasta"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Almond Milk"
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1065,
                    "quantity": 400,
                    "unit": "g"
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1092,
                    "quantity": 1000,
                    "unit": "ml"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 204,
                    "user_id": 104,
                    "entity_type": "grocery_lists",
                    "entity_id": 8003,
                    "action_enum": "create"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "005",
        "instruction": "Handle the creation of a grocery order for the Shah Extended Family. For the week starting '2025-09-01', devise a new meal plan alongside a grocery list. Generate a new grocery list tied to this meal plan. From this list, organize an order at 'Gourmet Pantry Supply'. The subtotal amounts to 3500 cents, with the total being 3850 cents. Document the order placement in the audit logs.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Shah Extended Family"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 205,
                    "week_start_date": "2025-09-01",
                    "created_by_user_id": 105
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 205,
                    "meal_plan_id": 6003,
                    "user_id": 105
                },
            },
            {
                "name": "SearchStoresByName",
                "arguments": {
                    "name_query": "Gourmet Pantry Supply"
                },
            },
            {
                "name": "CreateOrderFromGroceryList",
                "arguments": {
                    "household_id": 205,
                    "store_id": 9005,
                    "list_id": 8003,
                    "subtotal_cents": 3500,
                    "total_cents": 3850
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 205,
                    "user_id": 105,
                    "entity_type": "orders",
                    "entity_id": 10003,
                    "action_enum": "place_order"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "006",
        "instruction": "Coordinate as a recipe assistant for the Brown Large Family. With chicken breast available in their inventory, propose a dinner suggestion for August 20, 2025. Ensure recipes from the past 7 days are excluded. Locate the 'Chicken Tacos' recipe, verify it satisfies the requirements, and record it in their meal history as 'prepared' with a 5-star rating. Additionally, create an audit log for this activity with the reason 'User cooked recipe suggestion'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Brown Large Family"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "chicken breast"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 207,
                    "ingredient_id": 1001
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 207,
                    "days_ago": 7
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chicken Tacos"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 207,
                    "recipe_id": 402,
                    "plan_date": "2025-08-20",
                    "was_prepared": true,
                    "rating_int": 5
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 207,
                    "user_id": 107,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User cooked recipe suggestion"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "007",
        "instruction": "You are supporting the Martinez Household, which includes a child with a peanut allergy. They plan to make 'Spaghetti with Tomato Sauce' but lack regular spaghetti. Locate a peanut-free pasta substitute. Add 500g of 'Gluten-Free Pasta' to their grocery list for the upcoming shopping trip. Record this choice to replace ingredients in the audit trail for future reference, with the explanation 'Substitution for out-of-stock item, allergy consideration'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Martinez Household"
                },
            },
            {
                "name": "GetMembersByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Spaghetti with Tomato Sauce"
                },
            },
            {
                "name": "GetRecipeIngredients",
                "arguments": {
                    "recipe_id": 401
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Spaghetti Pasta"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 202,
                    "ingredient_id": 1005
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Gluten-Free Pasta"
                },
            },
            {
                "name": "GetGroceryListsByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8002,
                    "ingredient_id": 1065,
                    "quantity": 500,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "grocery_list_items",
                    "entity_id": 8114,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "Substitution for out-of-stock item, allergy consideration"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "008",
        "instruction": "You are serving as a grocery shopping assistant for the Lee-Anderson Family. Initially, prepare a new meal plan for the week commencing '2025-09-08'. Include two peanut-free lunch recipes: 'Hummus Veggie Wrap' for the 8th and 'Turkey Sandwich' for the 9th. Subsequently, compile a grocery list from this revised meal plan. Also, arrange an order from this list at 'FoodExpress', with a subtotal of 2500 cents and a total of 2750 cents.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Lee-Anderson Family"
                },
            },
            {
                "name": "SearchRecipes",
                "arguments": {
                    "meal_type": "Lunch",
                    "is_peanut_free": true
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 209,
                    "week_start_date": "2025-09-08",
                    "created_by_user_id": 109
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-08",
                    "recipe_id": 410,
                    "meal_type": "Lunch"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-09",
                    "recipe_id": 409,
                    "meal_type": "Lunch"
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 209,
                    "meal_plan_id": 6003,
                    "user_id": 109
                },
            },
            {
                "name": "SearchStoresByName",
                "arguments": {
                    "name_query": "FoodExpress"
                },
            },
            {
                "name": "CreateOrderFromGroceryList",
                "arguments": {
                    "household_id": 209,
                    "store_id": 9002,
                    "list_id": 8003,
                    "subtotal_cents": 2500,
                    "total_cents": 2750
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "009",
        "instruction": "As a meal plan manager for the Bennett Family, identify their meal plan for the week of August 25th. Seek out the entry with the note 'Cut pasta shorter'. Alter the notes for this particular entry to include 'Cut pasta shorter and add extra cheese for Maya'. Record this note alteration in the audit trail citing 'User request to add detail' as the reason.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Bennett Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6001,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Cut pasta shorter"
                },
            },
            {
                "name": "UpdateMealPlanEntryNotes",
                "arguments": {
                    "entry_id": 6102,
                    "new_notes": "Cut pasta shorter and add extra cheese for Maya"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6102,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "notes",
                        "reason": "User request to add detail"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "010",
        "instruction": "Act as an assistant for the Brown Large Family. They have recently prepared 'Stuffed Bell Peppers' from their meal history on 2025-08-08. Revise this meal to reflect it as prepared and assign it a 3-star rating, noting it was just okay. Furthermore, search for 'Bell Pepper' in the 'Rodriguez Household' inventory and reduce the quantity by 4, acknowledging their use in a recent recipe.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Brown Large Family"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Stuffed Bell Peppers"
                },
            },
            {
                "name": "GetMealHistoryByHouseholdAndDate",
                "arguments": {
                    "household_id": 207,
                    "plan_date": "2025-08-08"
                },
            },
            {
                "name": "UpdateMealHistory",
                "arguments": {
                    "history_id": 6262,
                    "was_prepared": true,
                    "rating_int": 3
                },
            },
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Rodriguez Household"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Bell Pepper"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 208,
                    "ingredient_id": 1009
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7076,
                    "new_quantity": 0
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "011",
        "instruction": "Assist Michael Peterson from the Peterson Couple as he needs to update a grocery list for the Martinez Household. Locate the item 'Turkey Deli Slices' on the list and remove it. Then, add 2 'Avocados' to the list, as he prefers to prepare fresh guacamole instead. Register this change stating 'User substitution' as the reason.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Michael Peterson"
                },
            },
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Martinez Household"
                },
            },
            {
                "name": "GetGroceryListsByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Turkey Deli Slices"
                },
            },
            {
                "name": "GetGroceryListItemsByListIdAndIngredientId",
                "arguments": {
                    "list_id": 8002,
                    "ingredient_id": 1039
                },
            },
            {
                "name": "RemoveItemFromGroceryList",
                "arguments": {
                    "item_id": 8112
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Avocado"
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8002,
                    "ingredient_id": 1086,
                    "quantity": 2,
                    "unit": "pcs"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 106,
                    "entity_type": "grocery_list_items",
                    "entity_id": 8112,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "User substitution"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 106,
                    "entity_type": "grocery_list_items",
                    "entity_id": 8114,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User substitution"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "012",
        "instruction": "As a meal planning assistant for Emily Wang, ensure she receives an Italian-themed dinner plan for three consecutive days. Develop a new meal strategy starting from the week of '2025-09-15'. Identify three distinct dinner recipes featuring 'Italian' cuisine and include them for the 15th, 16th, and 17th days. These recipes should be 'Spaghetti with Tomato Sauce', 'Mushroom Risotto', and 'Gluten-Free Pasta Primavera'. Lastly, document this new meal plan creation with the theme labeled as Italian.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Emily Wang"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 103
                },
            },
            {
                "name": "SearchRecipes",
                "arguments": {
                    "cuisine": "Italian",
                    "meal_type": "Dinner"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Spaghetti with Tomato Sauce"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Mushroom Risotto"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Gluten-Free Pasta Primavera"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 203,
                    "week_start_date": "2025-09-15",
                    "created_by_user_id": 103
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-15",
                    "recipe_id": 401
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-16",
                    "recipe_id": 426
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-17",
                    "recipe_id": 431
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 203,
                    "user_id": 103,
                    "entity_type": "meal_plans",
                    "entity_id": 6003,
                    "action_enum": "create",
                    "payload_json": {
                        "theme": "Italian"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "013",
        "instruction": "Act as a meal planning assistant for Emily Wang. She requires a specially themed dinner plan for three days. Draft a new meal plan for her commencing the week of '2025-09-15'. Include the recipes 'Mediterranean Quinoa Salad', 'Baked Cod with Herbs', and 'Mediterranean Bowl' and schedule them for the 15th, 16th, and 17th. In conclusion, log the creation of this new meal plan with the theme designated as 'Mediterranean'.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Emily Wang"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 103
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Mediterranean Quinoa Salad"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Baked Cod with Herbs"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Mediterranean Bowl"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 203,
                    "week_start_date": "2025-09-15",
                    "created_by_user_id": 103
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-15",
                    "recipe_id": 406
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-16",
                    "recipe_id": 425
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-17",
                    "recipe_id": 442
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 203,
                    "user_id": 103,
                    "entity_type": "meal_plans",
                    "entity_id": 6003,
                    "action_enum": "create",
                    "payload_json": {
                        "theme": "Mediterranean"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "014",
        "instruction": "Serve as a meal planning assistant for the Martinez Household. The task is to delete 'Lentil Soup' from their meal plan for the week of Aug 25, 2025. It should be removed due to a note indicating it's 'too warm for soup this week'. Substitute it with 'Mediterranean Quinoa Salad' for the same date (2025-08-25) and attach a note to 'add extra feta cheese'. Document these alterations in the audit trail, citing 'weather-appropriate replacement' as the rationale for the addition.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Alvarez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Lentil Soup"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 408
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6111
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Mediterranean Quinoa Salad"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6002,
                    "plan_date": "2025-08-25",
                    "recipe_id": 406,
                    "notes": "add extra feta cheese"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6111,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "weather-appropriate replacement"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "weather-appropriate replacement"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "015",
        "instruction": "As a meal planning assistant for the Bennett Family, eliminate 'Spaghetti with Tomato Sauce' from their meal plan on 2025-08-26. The client mentioned they 'want a lower-carb option'. Substitute it with 'Teriyaki Tofu Bowl' on the same date and include a note 'make tofu extra crispy'. Record these updates in the audit log with the reason 'replacement for dietary preference'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Mercer Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Spaghetti with Tomato Sauce"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 401
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6001,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "pasta shorter"
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6102
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Teriyaki Tofu Bowl"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6001,
                    "plan_date": "2025-08-26",
                    "recipe_id": 405,
                    "notes": "make tofu extra crispy"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6102,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "replacement for dietary preference"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "replacement for dietary preference"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "016",
        "instruction": "As a meal planning assistant for the Martinez Household, your task is to take out 'Grilled Salmon with Lemon' from their meal plan for 2025-08-28. The client is 'not in the mood for fish'. Replace it with 'Baked Cod with Herbs' on the same date and include a note 'serve with a side of asparagus'. Document the alterations in the audit log with the reason 'user preference change'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Alvarez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Grilled Salmon with Lemon"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 404
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6002,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Flake salmon"
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6114
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Baked Cod with Herbs"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6002,
                    "plan_date": "2025-08-28",
                    "recipe_id": 425,
                    "notes": "serve with a side of asparagus"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6114,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "user preference change"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "user preference change"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "017",
        "instruction": "Handle the role of meal planning assistant for the Bennett Family. Remove 'Chickpea Curry' from their schedule on 2025-08-28. The reason is 'Child doesn't like chickpeas'. Substitute it with the 'Beef Stir-Fry' recipe on the same date, ensuring to 'use low-sodium soy sauce'. Record both adjustments in the audit trail with the note 'replacement for child preference'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Bennett Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chickpea Curry"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 403
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6104
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Beef Stir-Fry"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6001,
                    "plan_date": "2025-08-28",
                    "recipe_id": 423,
                    "notes": "use low-sodium soy sauce"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6104,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "replacement for child preference"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "replacement for child preference"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "018",
        "instruction": "Coordinate meal planning for the Martinez Household. The user wishes to interchange 'Spaghetti with Tomato Sauce' for 2025-08-26 as they desire something 'less heavy'. Substitute it with 'Keto Zucchini Lasagna'. Include a note 'use extra mozzarella'. Document the removal and addition in the audit trail with the note 'dietary swap for lighter meal'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Martinez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Spaghetti with Tomato Sauce"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 401
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6002,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "pasta shorter"
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6112
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Keto Zucchini Lasagna"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6002,
                    "plan_date": "2025-08-26",
                    "recipe_id": 434,
                    "notes": "use extra mozzarella"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6112,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "dietary swap for lighter meal"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "dietary swap for lighter meal"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "019",
        "instruction": "As the Bennett Family's meal planning assistant, manage a menu adjustment for 2025-08-29. They wish to replace the 'Teriyaki Tofu Bowl' due to the need for a 'more universally liked dish'. Substitute it with 'Stuffed Bell Peppers' for that date. Include a note to 'make a vegetarian filling option'. Record both updates in the audit trail citing the reason as 'guest-friendly meal replacement'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Mercer Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Teriyaki Tofu Bowl"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 405
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6001,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Crispy tofu"
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6105
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Stuffed Bell Peppers"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6001,
                    "plan_date": "2025-08-29",
                    "recipe_id": 428,
                    "notes": "make a vegetarian filling option"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6105,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "guest-friendly meal replacement"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "guest-friendly meal replacement"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "020",
        "instruction": "Coordinate a meal plan update for the Martinez Household as their assistant. On 2025-08-29, they originally planned 'Teriyaki Tofu Bowl' but seek a change. The motivation is 'craving Korean food'. Replace it with 'Korean Beef Bowl' on the same day. Append a note to 'use chicken instead of beef'. Document the modification indicating the reason as 'cuisine preference change'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Alvarez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Teriyaki Tofu Bowl"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 405
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6002,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Tofu well-cooked"
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6115
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Korean Beef Bowl"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6002,
                    "plan_date": "2025-08-29",
                    "recipe_id": 427,
                    "notes": "use chicken instead of beef"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6115,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "cuisine preference change"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "cuisine preference change"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "021",
        "instruction": "Assist the Bennett Family and note that on 2025-08-30, their plan includes 'Mediterranean Quinoa Salad'. They wish to switch it out because they 'want a warmer meal'. Substitute it with 'Lentil Soup'. Include a remark 'serve with crusty bread'. Record the modifications citing 'comfort food replacement' as the reason.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Mercer Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Mediterranean Quinoa Salad"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 406
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6106
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Lentil Soup"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6001,
                    "plan_date": "2025-08-30",
                    "recipe_id": 408,
                    "notes": "serve with crusty bread"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6106,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "comfort food replacement"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "comfort food replacement"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "022",
        "instruction": "Support the Martinez Household as they have a salad arranged for 2025-08-30, but the 'weather is turning cold'. Eliminate the 'Mediterranean Quinoa Salad' from their menu. Introduce 'Vegetarian Chili' instead. Append a remark 'top with sour cream and cheddar'. Log the change in the audit with the justification 'replacement for cold weather'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Alvarez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Mediterranean Quinoa Salad"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 406
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6116
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Vegetarian Chili"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6002,
                    "plan_date": "2025-08-30",
                    "recipe_id": 424,
                    "notes": "top with sour cream and cheddar"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6116,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "replacement for cold weather"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "replacement for cold weather"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "023",
        "instruction": "Act as a meal planning assistant for the Bennett Family. Their desire is to exchange 'Thai Chicken Stir-Fry' on 2025-08-31 due to 'ran out of soy sauce'. Substitute it with 'Chicken Tacos', for which they possess the ingredients. Include a note 'serve with guacamole'. Document the modification with the reason 'ran out of soy sauce'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Mercer Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Thai Chicken Stir-Fry"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 407
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6001,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Reduce spice"
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6107
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chicken Tacos"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6001,
                    "plan_date": "2025-08-31",
                    "recipe_id": 402,
                    "notes": "serve with guacamole"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6107,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "ran out of soy sauce"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "ran out of soy sauce"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "024",
        "instruction": "Function as an assistant for the Martinez Household. The user intends to delete 'Thai Chicken Stir-Fry' from their 2025-08-31 plan, as they 'prefer something with beef'. Substitute it with 'Beef Stir-Fry'. Include the note 'add extra broccoli'. Record the change in the audit trail with the reason 'prefer something with beef'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Alvarez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Thai Chicken Stir-Fry"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 407
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6002,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Low spice"
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6117
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Beef Stir-Fry"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6002,
                    "plan_date": "2025-08-31",
                    "recipe_id": 423,
                    "notes": "add extra broccoli"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6117,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "prefer something with beef"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6117,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "prefer something with beef"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "025",
        "instruction": "Support the Bennett Family with a meal change. They need to modify their meal for 2025-08-25 from 'Chicken Tacos' because they 'had Mexican food last night'. Substitute it with 'Spaghetti with Tomato Sauce'. Include a note: 'use garlic bread on the side'. Record the change and its reason as 'had Mexican food last night'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Mercer Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chicken Tacos"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 402
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6101
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Spaghetti with Tomato Sauce"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6001,
                    "plan_date": "2025-08-25",
                    "recipe_id": 401,
                    "notes": "use garlic bread on the side"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6101,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "had Mexican food last night"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "had Mexican food last night"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "026",
        "instruction": "Assist with meal planning for the Martinez Household. Their menu includes 'Chicken Tacos' on 2025-08-27. They wish to opt for a vegetarian option for that day. Change the tacos to 'Chickpea Curry'. Add a note: 'serve with naan bread'. Document the removal and addition, stating 'vegetarian day' as the reason.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Alvarez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chicken Tacos"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 402
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6002,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Peanut-free confirmed"
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6113
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chickpea Curry"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6002,
                    "plan_date": "2025-08-27",
                    "recipe_id": 403,
                    "notes": "serve with naan bread"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6113,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "vegetarian day"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "vegetarian day"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "027",
        "instruction": "Act as a meal planning assistant for the Bennett Family. 'Spaghetti with Tomato Sauce' on 2025-08-26 should be swapped with something that 'feels healthier'. Substitute it with 'Mediterranean Quinoa Salad'. Include the note 'add grilled chicken for extra protein'. Record the reason 'user wants a healthier option' for the swap in the audit trail.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Mercer Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Spaghetti with Tomato Sauce"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 401
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6001,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "pasta shorter"
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6102
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Mediterranean Quinoa Salad"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6001,
                    "plan_date": "2025-08-26",
                    "recipe_id": 406,
                    "notes": "add grilled chicken for extra protein"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6102,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "user wants a healthier option"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "user wants a healthier option"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "028",
        "instruction": "Support the Martinez Household. The user considers 'Lentil Soup' dull and wishes to remove it from their plan for 2025-08-25. Replace it with 'Chicken Tacos', including the note 'use corn tortillas'. Document the change with the reason 'user preference for more exciting meal'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Alvarez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Lentil Soup"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 408
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6111
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chicken Tacos"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6002,
                    "plan_date": "2025-08-25",
                    "recipe_id": 402,
                    "notes": "use corn tortillas"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6111,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "user preference for more exciting meal"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "user preference for more exciting meal"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "029",
        "instruction": "As a meal planning assistant for the Bennett Family, substitute 'Grilled Salmon with Lemon' on 2025-08-27 since 'salmon is too expensive this week'. Choose a cost-effective alternative, 'Baked Cod with Herbs', for the same date. Include a note stating 'use frozen cod fillets'. Document the modification, citing 'budgetary reasons' for the replacement.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Mercer Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Grilled Salmon with Lemon"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 404
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6001,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Flake salmon"
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6103
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Baked Cod with Herbs"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6001,
                    "plan_date": "2025-08-27",
                    "recipe_id": 425,
                    "notes": "use frozen cod fillets"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6103,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "salmon is too expensive this week"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "budgetary reasons"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "030",
        "instruction": "While aiding the Martinez Household, eliminate 'Spaghetti with Tomato Sauce' on 2025-08-26 due to a 'gluten-free guest'. Substitute it with 'Gluten-Free Pasta Primavera'. Include a note to 'ensure all vegetables are fresh'. Record the adjustment, with the reason stated as 'gluten-free guest'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Alvarez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Spaghetti with Tomato Sauce"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 401
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6002,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "pasta shorter"
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6112
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Gluten-Free Pasta Primavera"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6002,
                    "plan_date": "2025-08-26",
                    "recipe_id": 431,
                    "notes": "ensure all vegetables are fresh"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6112,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "gluten-free guest"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "gluten-free guest"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "031",
        "instruction": "Assist the Bennett Family in removing 'Chickpea Curry' from their plan for 2025-08-28 due to 'not enough time for prep'. Substitute it with a faster meal: 'Chicken Tacos'. Include a note saying 'use pre-cooked chicken to save time' and document the swap.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Mercer Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chickpea Curry"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 403
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6104
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chicken Tacos"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6001,
                    "plan_date": "2025-08-28",
                    "recipe_id": 402,
                    "notes": "use pre-cooked chicken to save time"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6104,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "not enough time for prep"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "not enough time for prep"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "032",
        "instruction": "Assist the Martinez Household with replacing 'Teriyaki Tofu Bowl' on 2025-08-29 because they 'want to try a new recipe'.swap it with 'Moroccan Tagine'. Note 'keep spices mild for the kids' and record this alteration.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Alvarez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Teriyaki Tofu Bowl"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 405
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6002,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Tofu well-cooked"
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6115
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Moroccan Tagine"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6002,
                    "plan_date": "2025-08-29",
                    "recipe_id": 429,
                    "notes": "keep spices mild for the kids"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6115,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "want to try a new recipe"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "want to try a new recipe"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "033",
        "instruction": "Assist the Bennett Family in removing 'Chicken Tacos' from their schedule for 2025-08-25 due to 'want to use up leftover chickpeas'. Substitute it with 'Chickpea Curry' and include a note 'use coconut milk for creaminess'. Record the change citing 'inventory management swap' for the addition and 'want to use up leftover chickpeas' for the removal.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Mercer Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chicken Tacos"
                },
            },
            {
                "name": "GetMealPlanEntriesByRecipeId",
                "arguments": {
                    "recipe_id": 402
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6001,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Reduce chili powder"
                },
            },
            {
                "name": "RemoveRecipeFromMealPlan",
                "arguments": {
                    "entry_id": 6101
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chickpea Curry"
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6001,
                    "plan_date": "2025-08-25",
                    "recipe_id": 403,
                    "notes": "use coconut milk for creaminess"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6101,
                    "action_enum": "delete",
                    "payload_json": {
                        "reason": "want to use up leftover chickpeas"
                    }
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6118,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "inventory management swap"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "034",
        "instruction": "Assist Ryan Bennett from the Bennett Family with updating his inventory, as he has exhausted the 'Spaghetti Pasta'. Reflect a quantity of 0 in the inventory and add 500g of 'Penne Pasta' to the grocery list since he wishes to purchase a different type. Document the inventory update in the audit logs.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Aiden Mercer"
                },
            },
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Mercer Family"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Spaghetti Pasta"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Penne Pasta"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 201,
                    "ingredient_id": 1005
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7001,
                    "new_quantity": 0
                },
            },
            {
                "name": "GetGroceryListsByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8001,
                    "ingredient_id": 1062,
                    "quantity": 500,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "inventory_items",
                    "entity_id": 7001,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "quantity",
                        "new_value": 0
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "035",
        "instruction": "Guide Emily Wang in her tasks. She has depleted her stock of 'Firm Tofu' and needs to adjust her inventory to 0. A new meal plan is needed for the week commencing '2025-09-01', complete with a corresponding grocery list. Formulate the new grocery list associated with this meal plan. Since she wishes to explore new options, include 250g of 'Tempeh' in her grocery list. Document the inventory change.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Sarah Chen"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 103
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Firm Tofu"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Tempeh"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 203,
                    "ingredient_id": 1003
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7031,
                    "new_quantity": 0
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 203,
                    "week_start_date": "2025-09-01",
                    "created_by_user_id": 103
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 203,
                    "meal_plan_id": 6003,
                    "user_id": 103
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1054,
                    "quantity": 250,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 203,
                    "user_id": 103,
                    "entity_type": "inventory_items",
                    "entity_id": 7031,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "quantity",
                        "new_value": 0
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "036",
        "instruction": "Provide assistance to Olivia Brown of the Brown Large Family. They are out of 'Eggs'. Adjust the inventory to reflect a quantity of 0. They require a new meal plan for the upcoming week starting '2025-09-02', along with a grocery list. Develop a new grocery list that corresponds with this meal plan. Proceed to add a dozen (12 pcs) 'Eggs' to their grocery list for replenishment. Record this inventory modification.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Emma Johnson"
                },
            },
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Johnson Large Family"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Eggs"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 207,
                    "ingredient_id": 1030
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7065,
                    "new_quantity": 0
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 207,
                    "week_start_date": "2025-09-02",
                    "created_by_user_id": 107
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 207,
                    "meal_plan_id": 6003,
                    "user_id": 107
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1030,
                    "quantity": 12,
                    "unit": "pcs"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 207,
                    "user_id": 107,
                    "entity_type": "inventory_items",
                    "entity_id": 7065,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "quantity",
                        "new_value": 0
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "038",
        "instruction": "Support Michael Peterson by updating his inventory, as he has run out of 'Avocado'. Set the quantity to 0. Prepare a new meal plan for the week commencing '2025-09-03' alongside a grocery list. Connect this grocery list to the new meal plan. Replace snacks with 'Hummus' and add 200g to his grocery list. Record the modification.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "David Kowalski"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 106
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Avocado"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Hummus"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 206,
                    "ingredient_id": 1086
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7061,
                    "new_quantity": 0
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 206,
                    "week_start_date": "2025-09-03",
                    "created_by_user_id": 106
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 206,
                    "meal_plan_id": 6003,
                    "user_id": 106
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1038,
                    "quantity": 200,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 206,
                    "user_id": 106,
                    "entity_type": "inventory_items",
                    "entity_id": 7061,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "quantity",
                        "new_value": 0
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "039",
        "instruction": "Assist William Davis at the Davis Retirement household by adjusting the inventory to show 0 quantity for 'Broccoli'. A new meal plan is needed for the week starting '2025-09-04', along with a grocery list. Link the new grocery list to this meal plan. Add 1 head of 'Cauliflower' to their grocery list for variety. Note the inventory update.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "James Thompson"
                },
            },
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Thompson Retirement"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Broccoli"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Cauliflower"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 210,
                    "ingredient_id": 1066
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7088,
                    "new_quantity": 0
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 210,
                    "week_start_date": "2025-09-04",
                    "created_by_user_id": 110
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 210,
                    "meal_plan_id": 6003,
                    "user_id": 110
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1067,
                    "quantity": 1,
                    "unit": "pcs"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 210,
                    "user_id": 110,
                    "entity_type": "inventory_items",
                    "entity_id": 7088,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "quantity",
                        "new_value": 0
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "040",
        "instruction": "Assist Ryan Bennett once more. His stock of 'Chicken Breast' is depleted; adjust the inventory quantity to 0. He plans to make burgers, so incorporate 500g of 'Ground Beef' into the Bennett Family's grocery list. Record the update.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Ryan Bennett"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 101
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Chicken Breast"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Ground Beef"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 201,
                    "ingredient_id": 1001
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7004,
                    "new_quantity": 0
                },
            },
            {
                "name": "GetGroceryListsByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8001,
                    "ingredient_id": 1045,
                    "quantity": 500,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "inventory_items",
                    "entity_id": 7004,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "quantity",
                        "new_value": 0
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "041",
        "instruction": "Support Sofia Martinez. Her supply of 'Classic Hummus' is used up; amend the inventory for her household to show a quantity of 0. She aims to prepare a sandwich, therefore add a 'loaf' of 'Whole Wheat Bread' to her grocery list. Document the inventory update.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Sofia Martinez"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 102
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Hummus"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Whole Wheat Bread"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 202,
                    "ingredient_id": 1038
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7023,
                    "new_quantity": 0
                },
            },
            {
                "name": "GetGroceryListsByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8002,
                    "ingredient_id": 1026,
                    "quantity": 1,
                    "unit": "loaf"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "inventory_items",
                    "entity_id": 7023,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "quantity",
                        "new_value": 0
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "042",
        "instruction": "Assist Anjali Shah. She has depleted her 'Basmati Rice'. Adjust the Shah Extended Family inventory count to 0. A new meal plan is required for the week commencing '2025-09-05' along with an accompanying grocery list. Generate a fresh grocery list associated with this new meal plan. Priya has decided to purchase 'Jasmine Rice', therefore add 1kg to their grocery list. Record the inventory modification.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Anjali Shah"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 105
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Basmati Rice"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Jasmine Rice"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 205,
                    "ingredient_id": 1058
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7054,
                    "new_quantity": 0
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 205,
                    "week_start_date": "2025-09-05",
                    "created_by_user_id": 105
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 205,
                    "meal_plan_id": 6003,
                    "user_id": 105
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1059,
                    "quantity": 1000,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 205,
                    "user_id": 105,
                    "entity_type": "inventory_items",
                    "entity_id": 7054,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "quantity",
                        "new_value": 0
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "043",
        "instruction": "Support Diego Rodriguez of the Rodriguez Household. They have run out of 'Bell Pepper'. Set the inventory to 0. A fresh meal plan for the upcoming week starting '2025-09-06' along with a grocery list is necessary. Formulate a new grocery list that corresponds with this meal plan. To prepare a salad, add a bag of 'Romaine Lettuce' (300g) to their grocery list. Document the update.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Diego Rodriguez"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 108
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Bell Pepper"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Romaine Lettuce"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 208,
                    "ingredient_id": 1009
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7076,
                    "new_quantity": 0
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 208,
                    "week_start_date": "2025-09-06",
                    "created_by_user_id": 108
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 208,
                    "meal_plan_id": 6003,
                    "user_id": 108
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1013,
                    "quantity": 300,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 208,
                    "user_id": 108,
                    "entity_type": "inventory_items",
                    "entity_id": 7076,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "quantity",
                        "new_value": 0
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "044",
        "instruction": "Assist Grace Lee of the Lee-Anderson Family. Their 'Almond Milk' is depleted; set the inventory level to 0. A new meal plan is needed for the week commencing '2025-09-07', along with a corresponding grocery list. Generate a new grocery list associated with this meal plan. They wish to try 'Oat Milk' next, so include 1000ml in their grocery list.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Grace Lee"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 109
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Almond Milk"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Oat Milk"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 209,
                    "ingredient_id": 1092
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7078,
                    "new_quantity": 0
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 209,
                    "week_start_date": "2025-09-07",
                    "created_by_user_id": 109
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 209,
                    "meal_plan_id": 6003,
                    "user_id": 109
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1093,
                    "quantity": 1000,
                    "unit": "ml"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "045",
        "instruction": "Help the Bennett Family. Their stock of 'Cheddar Cheese' is exhausted; adjust the inventory quantity to 0. For pizza night, add 200g of 'Mozzarella Cheese' to their grocery list. Record the inventory change.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Bennett Family"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Cheddar Cheese"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Mozzarella Cheese"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 201,
                    "ingredient_id": 1024
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7012,
                    "new_quantity": 0
                },
            },
            {
                "name": "GetGroceryListsByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8001,
                    "ingredient_id": 1025,
                    "quantity": 200,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "inventory_items",
                    "entity_id": 7012,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "quantity",
                        "new_value": 0
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "046",
        "instruction": "Assist Sofia Martinez by noting she is out of 'Plain Greek Yogurt'. Adjust her inventory to reflect a quantity of 0. Since she intends to prepare parfaits, incorporate 500g of 'Yogurt (Vanilla)' into her grocery list. Record the update accordingly.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Sofia Martinez"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 102
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Plain Greek Yogurt"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Yogurt (Vanilla)"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 202,
                    "ingredient_id": 1023
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7027,
                    "new_quantity": 0
                },
            },
            {
                "name": "GetGroceryListsByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8002,
                    "ingredient_id": 1042,
                    "quantity": 500,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "inventory_items",
                    "entity_id": 7027,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "quantity",
                        "new_value": 0
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "047",
        "instruction": "Support Emily Wang by updating her inventory of 'Spinach' to 0 as she has run out. Develop a new meal plan for the week commencing '2025-09-07' and generate a grocery list associated with this plan. Include 150g of 'Kale' in her grocery list to ensure she has sufficient greens. Document the inventory adjustment.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Emily Wang"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 103
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Spinach"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Kale"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 203,
                    "ingredient_id": 1070
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7036,
                    "new_quantity": 0
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 203,
                    "week_start_date": "2025-09-07",
                    "created_by_user_id": 103
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 203,
                    "meal_plan_id": 6003,
                    "user_id": 103
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1071,
                    "quantity": 150,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 203,
                    "user_id": 103,
                    "entity_type": "inventory_items",
                    "entity_id": 7036,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "quantity",
                        "new_value": 0
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "048",
        "instruction": "Support William Davis with his needs. He has used up the 'Plain Greek Yogurt'. Adjust the Davis Retirement inventory to 0. A fresh meal plan for the week commencing '2025-09-07' along with a grocery list is necessary. Generate a new grocery list associated with this new meal plan. Since additional dairy is required, include 1000ml of 'Milk' in their grocery list. Record the inventory change.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "William Davis"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 110
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Plain Greek Yogurt"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Milk"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 210,
                    "ingredient_id": 1023
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7090,
                    "new_quantity": 0
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 210,
                    "week_start_date": "2025-09-07",
                    "created_by_user_id": 110
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 210,
                    "meal_plan_id": 6003,
                    "user_id": 110
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1037,
                    "quantity": 1000,
                    "unit": "ml"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 210,
                    "user_id": 110,
                    "entity_type": "inventory_items",
                    "entity_id": 7090,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "quantity",
                        "new_value": 0
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "049",
        "instruction": "Assist Olivia Brown from the Brown Large Family. They have depleted their supply of 'Milk'. Modify the inventory to reflect a quantity of 0. They require a new meal plan for the week beginning '2025-09-07' along with a grocery list. Develop a new grocery list connected to this new meal plan. Include a dairy-free alternative for a guest by adding 1000ml of 'Almond Milk' to their grocery list.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Olivia Brown"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 107
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Milk"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Almond Milk"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 207,
                    "ingredient_id": 1037
                },
            },
            {
                "name": "UpdateInventoryItemQuantity",
                "arguments": {
                    "inv_item_id": 7063,
                    "new_quantity": 0
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 207,
                    "week_start_date": "2025-09-07",
                    "created_by_user_id": 107
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 207,
                    "meal_plan_id": 6003,
                    "user_id": 107
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1092,
                    "quantity": 1000,
                    "unit": "ml"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "050",
        "instruction": "Assist Daniel Brown in developing a new meal plan for the Brown-Brown Family. Organize a schedule for the week starting '2025-09-08'. Include 'Gluten-Free Pasta Primavera' on '2025-09-08' and 'Vegan Black Bean Burgers' on '2025-09-10'. Record the meal plan creation in the audit logs.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Daniel Brown"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 104
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Gluten-Free Pasta Primavera"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Vegan Black Bean Burgers"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 204,
                    "week_start_date": "2025-09-08",
                    "created_by_user_id": 104
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-08",
                    "recipe_id": 431,
                    "notes": ""
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-10",
                    "recipe_id": 432,
                    "notes": ""
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 204,
                    "user_id": 104,
                    "entity_type": "meal_plans",
                    "entity_id": 6003,
                    "action_enum": "create"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "051",
        "instruction": "Assist Anjali Shah from the Shah Extended Family. Construct a new vegetarian meal plan for the week commencing '2025-09-15'. Incorporate 'Vegetarian Chili' on '2025-09-15' and 'Chickpea Curry' on '2025-09-16'. Document the meal plan creation.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Anjali Shah"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 105
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Vegetarian Chili"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chickpea Curry"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 205,
                    "week_start_date": "2025-09-15",
                    "created_by_user_id": 105
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-15",
                    "recipe_id": 424,
                    "notes": ""
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-16",
                    "recipe_id": 403,
                    "notes": ""
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 205,
                    "user_id": 105,
                    "entity_type": "meal_plans",
                    "entity_id": 6003,
                    "action_enum": "create"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "052",
        "instruction": "Assist Michael Peterson by developing a new low-carb meal plan for the Peterson Couple for the week beginning '2025-09-22'. Include 'Keto Zucchini Lasagna' for '2025-09-22' and 'Heart-Healthy Baked Salmon' for '2025-09-23'. Record the meal plan creation.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Michael Peterson"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 106
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Keto Zucchini Lasagna"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Heart-Healthy Baked Salmon"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 206,
                    "week_start_date": "2025-09-22",
                    "created_by_user_id": 106
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-22",
                    "recipe_id": 434,
                    "notes": ""
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-23",
                    "recipe_id": 435,
                    "notes": ""
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 206,
                    "user_id": 106,
                    "entity_type": "meal_plans",
                    "entity_id": 6003,
                    "action_enum": "create"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "053",
        "instruction": "Support Olivia Brown of the Brown Large Family in creating a meal plan for the week of '2025-10-06'. Schedule 'Pancakes' for dinner on '2025-10-06' and 'Stuffed Bell Peppers' on '2025-10-07'. Document the new plan in the audit trail.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Olivia Brown"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 107
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Pancakes"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Stuffed Bell Peppers"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 207,
                    "week_start_date": "2025-10-06",
                    "created_by_user_id": 107
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-10-06",
                    "recipe_id": 422,
                    "notes": ""
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-10-07",
                    "recipe_id": 428,
                    "notes": ""
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 207,
                    "user_id": 107,
                    "entity_type": "meal_plans",
                    "entity_id": 6003,
                    "action_enum": "create"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "054",
        "instruction": "Assist Diego Rodriguez of the Rodriguez Household. Develop a meal plan for the week starting '2025-09-01'. Include 'Chicken Tacos' on '2025-09-01' and 'Korean Beef Bowl' on '2025-09-03'. Record the creation of the plan.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Diego Rodriguez"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 108
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chicken Tacos"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Korean Beef Bowl"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 208,
                    "week_start_date": "2025-09-01",
                    "created_by_user_id": 108
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-01",
                    "recipe_id": 402,
                    "notes": ""
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-03",
                    "recipe_id": 427,
                    "notes": ""
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 208,
                    "user_id": 108,
                    "entity_type": "meal_plans",
                    "entity_id": 6003,
                    "action_enum": "create"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "055",
        "instruction": "Aid Grace Lee from the Lee-Anderson Family. Draft a new meal plan for the week beginning '2025-09-08'. Incorporate 'Dairy-Free Coconut Curry' on '2025-09-09' and 'Vegan Black Bean Burgers' on '2025-09-11'. Document the new meal plan.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Grace Lee"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 109
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Dairy-Free Coconut Curry"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Vegan Black Bean Burgers"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 209,
                    "week_start_date": "2025-09-08",
                    "created_by_user_id": 109
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-09",
                    "recipe_id": 433,
                    "notes": ""
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-11",
                    "recipe_id": 432,
                    "notes": ""
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 209,
                    "user_id": 109,
                    "entity_type": "meal_plans",
                    "entity_id": 6003,
                    "action_enum": "create"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "056",
        "instruction": "Assist William Davis from the Davis Retirement household by preparing a heart-healthy meal plan for the week starting '2025-09-15'. Include 'Heart-Healthy Baked Salmon' on '2025-09-15' and 'Baked Cod with Herbs' on '2025-09-17'. Record the creation of this plan.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "William Davis"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 110
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Heart-Healthy Baked Salmon"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Baked Cod with Herbs"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 210,
                    "week_start_date": "2025-09-15",
                    "created_by_user_id": 110
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-15",
                    "recipe_id": 435,
                    "notes": ""
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-17",
                    "recipe_id": 425,
                    "notes": ""
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 210,
                    "user_id": 110,
                    "entity_type": "meal_plans",
                    "entity_id": 6003,
                    "action_enum": "create"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "057",
        "instruction": "Support Emily Wang in constructing another meal plan. Draft a plan for the week beginning '2025-09-22'. Incorporate 'Vegan Black Bean Burgers' on '2025-09-22' and 'Buddha Bowl' on '2025-09-24'. Document this new plan.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Emily Wang"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 103
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Vegan Black Bean Burgers"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Buddha Bowl"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 203,
                    "week_start_date": "2025-09-22",
                    "created_by_user_id": 103
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-22",
                    "recipe_id": 432,
                    "notes": ""
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-09-24",
                    "recipe_id": 446,
                    "notes": ""
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 203,
                    "user_id": 103,
                    "entity_type": "meal_plans",
                    "entity_id": 6003,
                    "action_enum": "create"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "059",
        "instruction": "Assist Anjali Shah in crafting a flavorful meal plan. Design a new plan for the Shah Extended Family for the week starting '2025-10-06'. Include 'Moroccan Tagine' for '2025-10-06' and 'Chickpea Curry' for '2025-10-08'. Document this newly created meal plan.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Anjali Shah"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 105
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Moroccan Tagine"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chickpea Curry"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 205,
                    "week_start_date": "2025-10-06",
                    "created_by_user_id": 105
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-10-06",
                    "recipe_id": 429,
                    "notes": ""
                },
            },
            {
                "name": "AddRecipeToMealPlan",
                "arguments": {
                    "meal_plan_id": 6003,
                    "plan_date": "2025-10-08",
                    "recipe_id": 403,
                    "notes": ""
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 205,
                    "user_id": 105,
                    "entity_type": "meal_plans",
                    "entity_id": 6003,
                    "action_enum": "create"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "060",
        "instruction": "Serve as a recipe aide for the Bennett Family. They have Salmon Fillet in their freezer and require a dinner suggestion for tonight, August 21, 2025. Ensure no meals from the past two weeks are repeated. Locate the 'Grilled Salmon with Lemon' recipe, verify its suitability, and then record it in their meal history as 'prepared' with a 4-star rating. Additionally, create an audit log for this activity with the reason 'User prepared a healthy dinner'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Bennett Family"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Salmon Fillet"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 201,
                    "ingredient_id": 1002
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 201,
                    "days_ago": 14
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Grilled Salmon with Lemon"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 201,
                    "recipe_id": 404,
                    "plan_date": "2025-08-21",
                    "was_prepared": true,
                    "rating_int": 4
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User prepared a healthy dinner"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "061",
        "instruction": "As a recipe assistant for Emily Wang, handle her request for a dinner suggestion featuring tofu she has in her fridge for tonight, August 22, 2025. Ensure she hasn't enjoyed this meal in the previous 6 days. Locate the 'Teriyaki Tofu Bowl' recipe, verify its suitability, and record it in her meal history as 'prepared' with a 5-star rating. Additionally, update the audit log for this action citing 'User enjoyed a suggested vegetarian meal'.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Sarah Chen"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 103
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Tofu"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 203,
                    "ingredient_id": 1003
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 203,
                    "days_ago": 6
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Teriyaki Tofu Bowl"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 203,
                    "recipe_id": 405,
                    "plan_date": "2025-08-22",
                    "was_prepared": true,
                    "rating_int": 5
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 203,
                    "user_id": 103,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User enjoyed a suggested vegetarian meal"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "062",
        "instruction": "Assist the Rodriguez Household by suggesting a dinner using the ground beef they have for tonight, August 20, 2025. Check that this meal hasn't been consumed in the past week. Identify the 'Stuffed Bell Peppers' recipe, confirm it fits their needs, and document it in their meal history as 'prepared' with a 4-star rating. Also, include an entry in the audit log indicating the reason 'User logged a favorite meal'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Rodriguez Household"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Ground Beef"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 208,
                    "ingredient_id": 1045
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 208,
                    "days_ago": 7
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Stuffed Bell Peppers"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 208,
                    "recipe_id": 428,
                    "plan_date": "2025-08-20",
                    "was_prepared": true,
                    "rating_int": 4
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 208,
                    "user_id": 108,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User logged a favorite meal"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "063",
        "instruction": "Assist the Shah Extended Family. They have lentils and require a dinner suggestion for tonight, August 23, 2025. Ensure they haven't had this meal in the previous 10 days. Locate the 'Lentil Soup' recipe, verify it meets the requirements, and then record it in their meal history as 'prepared' with a 5-star rating. Also, include an audit log for this action, citing the reason 'User logged a prepared family meal'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Shah Extended Family"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Lentils"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 205,
                    "ingredient_id": 1053
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 205,
                    "days_ago": 10
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Lentil Soup"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 205,
                    "recipe_id": 408,
                    "plan_date": "2025-08-23",
                    "was_prepared": true,
                    "rating_int": 5
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 205,
                    "user_id": 105,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User logged a prepared family meal"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "064",
        "instruction": "Help the Peterson Couple as a recipe assistant. They possess salmon and are looking for a keto-friendly dinner for the evening of August 24, 2025. Confirm they haven't consumed this meal in the last 14 days. Identify the 'Heart-Healthy Baked Salmon' recipe, check its suitability, and subsequently register it in their meal history as 'prepared' with a 5-star rating. Also, make sure to add an audit log for this action with reason 'User logged a keto-friendly recipe'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Peterson Couple"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Salmon"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 206,
                    "ingredient_id": 1002
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 206,
                    "days_ago": 14
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Heart-Healthy Baked Salmon"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 206,
                    "recipe_id": 435,
                    "plan_date": "2025-08-24",
                    "was_prepared": true,
                    "rating_int": 5
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 206,
                    "user_id": 106,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User logged a keto-friendly recipe"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "065",
        "instruction": "Assist the Brown-Brown Family. They have black beans in their pantry and desire a vegan dinner for this evening, August 21, 2025. Ensure the meal was not prepared in the last week. Locate the 'Vegan Black Bean Burgers' recipe, verify its suitability, and document it in their meal history as 'prepared' with a 4-star rating. Include an audit log for this action citing 'User prepared a suggested vegan dinner'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Brown-Brown Family"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Black Beans"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 204,
                    "ingredient_id": 1051
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 204,
                    "days_ago": 7
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Vegan Black Bean Burgers"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 204,
                    "recipe_id": 432,
                    "plan_date": "2025-08-21",
                    "was_prepared": true,
                    "rating_int": 4
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 204,
                    "user_id": 104,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User prepared a suggested vegan dinner"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "066",
        "instruction": "Assist the Davis Retirement household. They possess cod fillets and are looking for a dinner idea for tonight, August 22, 2025. Confirm this meal hasn't been prepared in the past 14 days. Find the 'Baked Cod with Herbs' recipe, assess its appropriateness, and log it into their meal history as 'prepared' with a 5-star rating. Add an audit log for this action specifying 'User cooked a recommended heart-healthy meal'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Davis Retirement"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Cod Fillet"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 210,
                    "ingredient_id": 1049
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 210,
                    "days_ago": 14
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Baked Cod with Herbs"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 210,
                    "recipe_id": 425,
                    "plan_date": "2025-08-22",
                    "was_prepared": true,
                    "rating_int": 5
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 210,
                    "user_id": 110,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User cooked a recommended heart-healthy meal"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "067",
        "instruction": "Act as the recipe assistant for the Bennett Family. They have chicken breast and seek a new dinner idea for tonight, August 25, 2025. Ensure they haven't consumed this meal in the past week. Locate the 'Thai Chicken Stir-Fry' recipe, verify its suitability, and document it in their meal history as 'prepared' with a 4-star rating. Additionally, create an audit log for this activity with the reason 'User tried a new stir-fry recipe'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Bennett Family"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Chicken Breast"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 201,
                    "ingredient_id": 1001
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 201,
                    "days_ago": 7
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Thai Chicken Stir-Fry"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 201,
                    "recipe_id": 407,
                    "plan_date": "2025-08-25",
                    "was_prepared": true,
                    "rating_int": 4
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User tried a new stir-fry recipe"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "068",
        "instruction": "Assist the Martinez Household. They have chickpeas available and request a vegetarian meal for tonight, August 26, 2025. Confirm that this meal wasn't made last week. Retrieve the 'Chickpea Curry' recipe, ensure it meets the requirements, and record it in their meal history as 'prepared' with a 3-star rating. Include an audit log with the reason 'User cooked a vegetarian meal, rating provided'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Martinez Household"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Chickpeas"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 202,
                    "ingredient_id": 1004
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 202,
                    "days_ago": 7
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chickpea Curry"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 202,
                    "recipe_id": 403,
                    "plan_date": "2025-08-26",
                    "was_prepared": true,
                    "rating_int": 3
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User cooked a vegetarian meal, rating provided"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "069",
        "instruction": "Help Emily Wang. She has quinoa available and is looking for a light dinner this evening, August 27, 2025. Ensure she hasn't prepared it within the last 2 weeks. Locate the 'Mediterranean Quinoa Salad' recipe, verify its appropriateness, and record it in her meal history marked as 'prepared' with a 5-star rating. Insert an audit log noting the reason 'User logged preparation of a favorite salad'.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Emily Wang"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 103
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Quinoa"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 203,
                    "ingredient_id": 1007
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 203,
                    "days_ago": 14
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Mediterranean Quinoa Salad"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 203,
                    "recipe_id": 406,
                    "plan_date": "2025-08-27",
                    "was_prepared": true,
                    "rating_int": 5
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 203,
                    "user_id": 103,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User logged preparation of a favorite salad"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "070",
        "instruction": "Support the Rodriguez Household. They have black beans ready and need a dinner suggestion for tonight, August 21, 2025. Confirm they haven't consumed this dish in the past week. Identify the 'Vegetarian Chili' recipe, ensure it's suitable, and enter it into their meal history as 'prepared' with a 5-star rating. Create an audit log for this step with reason 'User cooked a hearty chili'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Rodriguez Household"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Black Beans"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 208,
                    "ingredient_id": 1051
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 208,
                    "days_ago": 7
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Vegetarian Chili"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 208,
                    "recipe_id": 424,
                    "plan_date": "2025-08-21",
                    "was_prepared": true,
                    "rating_int": 5
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 208,
                    "user_id": 108,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User cooked a hearty chili"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "071",
        "instruction": "Serve as a recipe assistant for the Brown Large Family. They have ground beef and require a quick dinner option for tonight, August 22, 2025. Ensure this dish was not consumed by them last week. Locate the 'Korean Beef Bowl' recipe, verify its suitability, and then document it in their meal history as 'prepared' with a 4-star rating. Additionally, create an audit log for this action citing the reason 'User cooked a quick weeknight meal'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Brown Large Family"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Ground Beef"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 207,
                    "ingredient_id": 1045
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 207,
                    "days_ago": 7
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Korean Beef Bowl"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 207,
                    "recipe_id": 427,
                    "plan_date": "2025-08-22",
                    "was_prepared": true,
                    "rating_int": 4
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 207,
                    "user_id": 107,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User cooked a quick weeknight meal"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "072",
        "instruction": "Assist the Peterson Couple with their dinner plans. They possess zucchini and ground beef and want to prepare a low-carb dinner for tonight, August 25, 2025. Confirm that this meal was not made by them in the last 4 days. Retrieve the 'Keto Zucchini Lasagna' recipe, validate its appropriateness, and record it in their meal history as 'prepared' with a 5-star rating. Also, generate an audit log for this action with the reason 'User prepared a suggested low-carb dinner'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Peterson Couple"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Zucchini"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 206,
                    "ingredient_id": 1073
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 206,
                    "days_ago": 4
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Keto Zucchini Lasagna"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 206,
                    "recipe_id": 434,
                    "plan_date": "2025-08-25",
                    "was_prepared": true,
                    "rating_int": 5
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 206,
                    "user_id": 106,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User prepared a suggested low-carb dinner"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "073",
        "instruction": "Assist the Davis Retirement household as a recipe assistant. They possess chicken thighs and are seeking a comforting dinner for this evening, August 23, 2025. This meal was not made last week. Locate the 'Moroccan Tagine' recipe, verify it as a viable option, and register it in their meal history as 'prepared' with a 4-star rating. Include an audit log stating 'User logged a flavorful dinner'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Davis Retirement"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Chicken Thighs"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 210,
                    "ingredient_id": 1047
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 210,
                    "days_ago": 7
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Moroccan Tagine"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 210,
                    "recipe_id": 429,
                    "plan_date": "2025-08-23",
                    "was_prepared": true,
                    "rating_int": 4
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 210,
                    "user_id": 110,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User logged a flavorful dinner"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "074",
        "instruction": "Assist the Lee-Anderson Family. They have quinoa at hand and desire a healthy breakfast idea for the following day, August 21, 2025. This meal has not been consumed by them in the past 2 weeks. Locate the 'Quinoa Breakfast Bowl' recipe, ensure it's appropriate, and document it into their meal history as 'prepared' with a 5-star rating. Further, insert an audit log with the reason 'User planned a new breakfast'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Lee-Anderson Family"
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Quinoa"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 209,
                    "ingredient_id": 1007
                },
            },
            {
                "name": "GetMealHistoryForHousehold",
                "arguments": {
                    "household_id": 209,
                    "days_ago": 14
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Quinoa Breakfast Bowl"
                },
            },
            {
                "name": "AddMealHistory",
                "arguments": {
                    "household_id": 209,
                    "recipe_id": 436,
                    "plan_date": "2025-08-21",
                    "was_prepared": true,
                    "rating_int": 5
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 209,
                    "user_id": 109,
                    "entity_type": "meal_history",
                    "entity_id": 6301,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "User planned a new breakfast"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "075",
        "instruction": "Assist the Bennett Family in their preparation of 'Chicken Tacos'. They lack 'Cheddar Cheese', so identify an appropriate cheese substitute. Add 200g of 'Mozzarella Cheese' to their grocery list for this dish. Record this ingredient substitution in the audit trail for future reference, citing 'Out of stock, cheese substitution' as the reason.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Bennett Family"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chicken Tacos"
                },
            },
            {
                "name": "GetRecipeIngredients",
                "arguments": {
                    "recipe_id": 402
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Cheddar Cheese"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 201,
                    "ingredient_id": 1024
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Mozzarella Cheese"
                },
            },
            {
                "name": "GetGroceryListsByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8001,
                    "ingredient_id": 1025,
                    "quantity": 200,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "grocery_list_items",
                    "entity_id": 8114,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "Out of stock, cheese substitution"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "076",
        "instruction": "Aid the Brown-Brown Family in sourcing gluten-free options. They're planning to make 'Gluten-Free Pancakes' but are short on 'Gluten-Free Flour'. Find a suitable alternative flour. Develop a new meal plan for the week beginning '2025-09-01' and create a grocery list linked to it. Include 500g of 'Almond Flour' in their grocery list. Log this change as 'Out of stock, gluten-free flour alternative'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Brown-Brown Family"
                },
            },
            {
                "name": "GetMembersByHouseholdId",
                "arguments": {
                    "household_id": 204
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Gluten-Free Pancakes"
                },
            },
            {
                "name": "GetRecipeIngredients",
                "arguments": {
                    "recipe_id": 440
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Gluten-Free Flour"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 204,
                    "ingredient_id": 1119
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Almond Flour"
                },
            },
            {
                "name": "GetGroceryListsByHouseholdId",
                "arguments": {
                    "household_id": 204
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 204,
                    "week_start_date": "2025-09-01",
                    "created_by_user_id": 104
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 204,
                    "meal_plan_id": 6003,
                    "user_id": 104
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1120,
                    "quantity": 500,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 204,
                    "user_id": 104,
                    "entity_type": "grocery_list_items",
                    "entity_id": 8114,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "Out of stock, gluten-free flour alternative"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "077",
        "instruction": "Assist the Brown Large Family, who are allergic to shellfish. They aim to prepare 'Beef Stir-Fry' but lack 'Ground Beef'. Identify a suitable, non-shellfish protein alternative. They are in need of a new meal plan for the week beginning '2025-09-01' along with a grocery list. Develop a new grocery list associated with this new meal plan. Include 600g of 'Chicken Thighs' to their grocery list. Document this substitution with the reason 'Out of beef, protein swap'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Brown Large Family"
                },
            },
            {
                "name": "GetMembersByHouseholdId",
                "arguments": {
                    "household_id": 207
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Beef Stir-Fry"
                },
            },
            {
                "name": "GetRecipeIngredients",
                "arguments": {
                    "recipe_id": 423
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Ground Beef"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 207,
                    "ingredient_id": 1045
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Chicken Thighs"
                },
            },
            {
                "name": "GetGroceryListsByHouseholdId",
                "arguments": {
                    "household_id": 207
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 207,
                    "week_start_date": "2025-09-01",
                    "created_by_user_id": 107
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 207,
                    "meal_plan_id": 6003,
                    "user_id": 107
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1047,
                    "quantity": 600,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 207,
                    "user_id": 107,
                    "entity_type": "grocery_list_items",
                    "entity_id": 8114,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "Out of beef, protein swap"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "078",
        "instruction": "Aid the Shah Extended Family, who maintain a vegetarian diet. They are preparing 'Dairy-Free Coconut Curry' but are short on 'Firm Tofu'. Discover another vegetarian protein option for the curry. They require a new meal plan commencing '2025-09-01' as well as a grocery list. Formulate a new grocery list connected to this new meal plan. Incorporate a 400g can of 'Canned Chickpeas' into their grocery list. Record this substitution with the note 'Tofu out of stock, using chickpeas'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Shah Extended Family"
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Dairy-Free Coconut Curry"
                },
            },
            {
                "name": "GetRecipeIngredients",
                "arguments": {
                    "recipe_id": 433
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Firm Tofu"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 205,
                    "ingredient_id": 1003
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Canned Chickpeas"
                },
            },
            {
                "name": "GetGroceryListsByHouseholdId",
                "arguments": {
                    "household_id": 205
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 205,
                    "week_start_date": "2025-09-01",
                    "created_by_user_id": 105
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 205,
                    "meal_plan_id": 6003,
                    "user_id": 105
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1004,
                    "quantity": 400,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 205,
                    "user_id": 105,
                    "entity_type": "grocery_list_items",
                    "entity_id": 8114,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "Tofu out of stock, using chickpeas"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "079",
        "instruction": "You are providing support to the Davis Retirement household. They plan to prepare 'Heart-Healthy Baked Salmon' but are missing fresh 'Salmon Fillet'. Identify another healthy fish alternative. They require a new meal plan for the week commencing '2025-09-01' along with a grocery list. Generate a new grocery list linked to this updated meal plan. Include 500g of 'Cod Fillet' in their grocery list. Record this as a 'Substitution due to salmon availability'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Davis Retirement"
                },
            },
            {
                "name": "GetMembersByHouseholdId",
                "arguments": {
                    "household_id": 210
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Heart-Healthy Baked Salmon"
                },
            },
            {
                "name": "GetRecipeIngredients",
                "arguments": {
                    "recipe_id": 435
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Salmon Fillet"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 210,
                    "ingredient_id": 1002
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Cod Fillet"
                },
            },
            {
                "name": "GetGroceryListsByHouseholdId",
                "arguments": {
                    "household_id": 210
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 210,
                    "week_start_date": "2025-09-01",
                    "created_by_user_id": 110
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 210,
                    "meal_plan_id": 6003,
                    "user_id": 110
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1049,
                    "quantity": 500,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 210,
                    "user_id": 110,
                    "entity_type": "grocery_list_items",
                    "entity_id": 8114,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "Substitution due to salmon availability"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "083",
        "instruction": "You are aiding Emily Wang. She intends to cook 'Teriyaki Tofu Bowl' but lacks 'White Rice'. Locate a substitute grain. She needs a fresh meal plan for the week starting '2025-09-05' and a grocery list. Establish a new grocery list associated with this new meal plan. Insert 300g of 'Quinoa' into her grocery list. Document this as 'Rice out of stock, substituting with quinoa'.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Emily Wang"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 103
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Teriyaki Tofu Bowl"
                },
            },
            {
                "name": "GetRecipeIngredients",
                "arguments": {
                    "recipe_id": 405
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "White Rice"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 203,
                    "ingredient_id": 1006
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Quinoa"
                },
            },
            {
                "name": "GetGroceryListsByHouseholdId",
                "arguments": {
                    "household_id": 203
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 203,
                    "week_start_date": "2025-09-05",
                    "created_by_user_id": 103
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 203,
                    "meal_plan_id": 6003,
                    "user_id": 103
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1007,
                    "quantity": 300,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 203,
                    "user_id": 103,
                    "entity_type": "grocery_list_items",
                    "entity_id": 8114,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "Rice out of stock, substituting with quinoa"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "084",
        "instruction": "Assist the Rodriguez Household. They are preparing 'Chicken Tacos' and lack 'Romaine Lettuce'. Identify an alternative leafy green. Design a meal plan for the week commencing '2025-09-05' along with a grocery list. Create a new grocery list associated with this meal plan. Include 200g of 'Spinach' in their grocery list. Record this change as 'Lettuce unavailable, using spinach'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Rodriguez Household"
                },
            },
            {
                "name": "GetMembersByHouseholdId",
                "arguments": {
                    "household_id": 208
                },
            },
            {
                "name": "SearchRecipesByTitleSubstring",
                "arguments": {
                    "title_substring": "Chicken Tacos"
                },
            },
            {
                "name": "GetRecipeIngredients",
                "arguments": {
                    "recipe_id": 402
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Romaine Lettuce"
                },
            },
            {
                "name": "GetInventoryForHouseholdAndIngredientId",
                "arguments": {
                    "household_id": 208,
                    "ingredient_id": 1013
                },
            },
            {
                "name": "SearchIngredientsByName",
                "arguments": {
                    "name_query": "Spinach"
                },
            },
            {
                "name": "GetGroceryListsByHouseholdId",
                "arguments": {
                    "household_id": 208
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 208,
                    "week_start_date": "2025-09-05",
                    "created_by_user_id": 108
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 208,
                    "meal_plan_id": 6003,
                    "user_id": 108
                },
            },
            {
                "name": "AddItemToGroceryList",
                "arguments": {
                    "list_id": 8003,
                    "ingredient_id": 1070,
                    "quantity": 200,
                    "unit": "g"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 208,
                    "user_id": 108,
                    "entity_type": "grocery_list_items",
                    "entity_id": 8114,
                    "action_enum": "create",
                    "payload_json": {
                        "reason": "Lettuce unavailable, using spinach"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "085",
        "instruction": "Facilitate the creation of a grocery order for the Bennett Family. They require a new meal plan for the week beginning '2025-09-08' and a matching grocery list. Develop the meal plan followed by the list. Subsequently, generate an order from this list at 'GreenGrocer Digital'. The subtotal is 4200 cents and the total is 4550 cents. Document the order entry in the audit logs.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Bennett Family"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 201,
                    "week_start_date": "2025-09-08",
                    "created_by_user_id": 101
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 201,
                    "meal_plan_id": 6003,
                    "user_id": 101
                },
            },
            {
                "name": "SearchStoresByName",
                "arguments": {
                    "name_query": "GreenGrocer Digital"
                },
            },
            {
                "name": "CreateOrderFromGroceryList",
                "arguments": {
                    "household_id": 201,
                    "store_id": 9001,
                    "list_id": 8003,
                    "subtotal_cents": 4200,
                    "total_cents": 4550
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "orders",
                    "entity_id": 10003,
                    "action_enum": "place_order"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "086",
        "instruction": "Craft a grocery order for the Martinez Household. They require a new meal plan commencing '2025-09-08' and also a comprehensive grocery list. Generate a new grocery list associated with this meal plan. Formulate an order based on this list at 'FoodExpress'. The subtotal amounts to 1800 cents and the total is 2000 cents. Record the order placement within the audit logs.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Martinez Household"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 202,
                    "week_start_date": "2025-09-08",
                    "created_by_user_id": 102
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 202,
                    "meal_plan_id": 6003,
                    "user_id": 102
                },
            },
            {
                "name": "SearchStoresByName",
                "arguments": {
                    "name_query": "FoodExpress"
                },
            },
            {
                "name": "CreateOrderFromGroceryList",
                "arguments": {
                    "household_id": 202,
                    "store_id": 9002,
                    "list_id": 8003,
                    "subtotal_cents": 1800,
                    "total_cents": 2000
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "orders",
                    "entity_id": 10003,
                    "action_enum": "place_order"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "087",
        "instruction": "Assemble a grocery order for Emily Wang. She needs a fresh meal plan beginning the week of '2025-09-15' along with a detailed grocery list. Develop a new grocery list connected to this meal plan. Form an order from this list at 'Natural Farm Collective'. The subtotal is 5500 cents and the total comes to 5950 cents. Document the order placement in the audit logs.",
        "actions": [
            {
                "name": "SearchUsersByName",
                "arguments": {
                    "name_query": "Emily Wang"
                },
            },
            {
                "name": "GetHouseholdByUserId",
                "arguments": {
                    "user_id": 103
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 203,
                    "week_start_date": "2025-09-15",
                    "created_by_user_id": 103
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 203,
                    "meal_plan_id": 6003,
                    "user_id": 103
                },
            },
            {
                "name": "SearchStoresByName",
                "arguments": {
                    "name_query": "Natural Farm Collective"
                },
            },
            {
                "name": "CreateOrderFromGroceryList",
                "arguments": {
                    "household_id": 203,
                    "store_id": 9003,
                    "list_id": 8003,
                    "subtotal_cents": 5500,
                    "total_cents": 5950
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 203,
                    "user_id": 103,
                    "entity_type": "orders",
                    "entity_id": 10003,
                    "action_enum": "place_order"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "088",
        "instruction": "Handle the creation of a grocery order for the Brown-Brown Family. They require a new meal plan for the week commencing '2025-09-15' and an associated grocery list. Construct a new grocery list linked to this meal plan. Proceed to make an order from this list at 'Wellness Foods Hub'. The subtotal amounts to 6200 cents, and the total is 6650 cents. Record the order placement in the audit logs.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Brown-Brown Family"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 204,
                    "week_start_date": "2025-09-15",
                    "created_by_user_id": 104
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 204,
                    "meal_plan_id": 6003,
                    "user_id": 104
                },
            },
            {
                "name": "SearchStoresByName",
                "arguments": {
                    "name_query": "Wellness Foods Hub"
                },
            },
            {
                "name": "CreateOrderFromGroceryList",
                "arguments": {
                    "household_id": 204,
                    "store_id": 9006,
                    "list_id": 8003,
                    "subtotal_cents": 6200,
                    "total_cents": 6650
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 204,
                    "user_id": 104,
                    "entity_type": "orders",
                    "entity_id": 10003,
                    "action_enum": "place_order"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "089",
        "instruction": "Coordinate the creation of a grocery order for the Peterson Couple. They require a meal plan for the week initiating '2025-09-22'. Develop a new grocery list tied to the new plan. Organize an order from this list at 'Value Groceries Direct'. The subtotal is 2800 cents, and the total is 3100 cents. Document the order placement.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Peterson Couple"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 206,
                    "week_start_date": "2025-09-22",
                    "created_by_user_id": 106
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 206,
                    "meal_plan_id": 6003,
                    "user_id": 106
                },
            },
            {
                "name": "SearchStoresByName",
                "arguments": {
                    "name_query": "Value Groceries Direct"
                },
            },
            {
                "name": "CreateOrderFromGroceryList",
                "arguments": {
                    "household_id": 206,
                    "store_id": 9004,
                    "list_id": 8003,
                    "subtotal_cents": 2800,
                    "total_cents": 3100
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 206,
                    "user_id": 106,
                    "entity_type": "orders",
                    "entity_id": 10003,
                    "action_enum": "place_order"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "090",
        "instruction": "Handle the creation of a grocery order for the Brown Large Family. They require a new meal plan for the week beginning '2025-09-22'. Design a grocery list for them. Arrange an order based on this list using 'Harvest Direct Service'. Ensure the subtotal is 9500 cents and the final total comes to 10150 cents. Document the order submission.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Brown Large Family"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 207,
                    "week_start_date": "2025-09-22",
                    "created_by_user_id": 107
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 207,
                    "meal_plan_id": 6003,
                    "user_id": 107
                },
            },
            {
                "name": "SearchStoresByName",
                "arguments": {
                    "name_query": "Harvest Direct Service"
                },
            },
            {
                "name": "CreateOrderFromGroceryList",
                "arguments": {
                    "household_id": 207,
                    "store_id": 9007,
                    "list_id": 8003,
                    "subtotal_cents": 9500,
                    "total_cents": 10150
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 207,
                    "user_id": 107,
                    "entity_type": "orders",
                    "entity_id": 10003,
                    "action_enum": "place_order"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "091",
        "instruction": "Coordinate a grocery order for the Rodriguez Household. They require a meal plan for the week starting '2025-09-29'. Formulate a new grocery list from this plan. Organize an order from this list via 'SpeedyMart Online'. Verify the subtotal amounts to 4800 cents and that the complete total reaches 5200 cents. Record the order entry.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Rodriguez Household"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 208,
                    "week_start_date": "2025-09-29",
                    "created_by_user_id": 108
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 208,
                    "meal_plan_id": 6003,
                    "user_id": 108
                },
            },
            {
                "name": "SearchStoresByName",
                "arguments": {
                    "name_query": "SpeedyMart Online"
                },
            },
            {
                "name": "CreateOrderFromGroceryList",
                "arguments": {
                    "household_id": 208,
                    "store_id": 9008,
                    "list_id": 8003,
                    "subtotal_cents": 4800,
                    "total_cents": 5200
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 208,
                    "user_id": 108,
                    "entity_type": "orders",
                    "entity_id": 10003,
                    "action_enum": "place_order"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "092",
        "instruction": "Handle the creation of a grocery order for the Lee-Anderson Family. Establish a meal plan for the week commencing '2025-09-29'. Develop a grocery list based on this plan. Formulate an order from this list at 'GreenGrocer Digital'. The subtotal amounts to 5100 cents and the complete total is 5500 cents. Record the order.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Lee-Anderson Family"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 209,
                    "week_start_date": "2025-09-29",
                    "created_by_user_id": 109
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 209,
                    "meal_plan_id": 6003,
                    "user_id": 109
                },
            },
            {
                "name": "SearchStoresByName",
                "arguments": {
                    "name_query": "GreenGrocer Digital"
                },
            },
            {
                "name": "CreateOrderFromGroceryList",
                "arguments": {
                    "household_id": 209,
                    "store_id": 9001,
                    "list_id": 8003,
                    "subtotal_cents": 5100,
                    "total_cents": 5500
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 209,
                    "user_id": 109,
                    "entity_type": "orders",
                    "entity_id": 10003,
                    "action_enum": "place_order"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "093",
        "instruction": "Organize a grocery order for the Davis Retirement household. Prepare a new meal plan for the week beginning '2025-10-06'. Generate a fresh grocery list derived from the new plan. Create an order from this list at 'FoodExpress'. The subtotal stands at 3200 cents and the overall total is 3500 cents. Document the order placement.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Davis Retirement"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 210,
                    "week_start_date": "2025-10-06",
                    "created_by_user_id": 110
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 210,
                    "meal_plan_id": 6003,
                    "user_id": 110
                },
            },
            {
                "name": "SearchStoresByName",
                "arguments": {
                    "name_query": "FoodExpress"
                },
            },
            {
                "name": "CreateOrderFromGroceryList",
                "arguments": {
                    "household_id": 210,
                    "store_id": 9002,
                    "list_id": 8003,
                    "subtotal_cents": 3200,
                    "total_cents": 3500
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 210,
                    "user_id": 110,
                    "entity_type": "orders",
                    "entity_id": 10003,
                    "action_enum": "place_order"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "094",
        "instruction": "Handle another grocery order arrangement for the Shah Extended Family. They require a plan for the week of '2025-10-06'. Assemble a grocery list from that plan. Afterward, coordinate an order at 'Natural Farm Collective'. The subtotal is 7500 cents and the total is 8100 cents. Document the order placement.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Shah Extended Family"
                },
            },
            {
                "name": "CreateMealPlan",
                "arguments": {
                    "household_id": 205,
                    "week_start_date": "2025-10-06",
                    "created_by_user_id": 105
                },
            },
            {
                "name": "CreateGroceryListFromMealPlan",
                "arguments": {
                    "household_id": 205,
                    "meal_plan_id": 6003,
                    "user_id": 105
                },
            },
            {
                "name": "SearchStoresByName",
                "arguments": {
                    "name_query": "Natural Farm Collective"
                },
            },
            {
                "name": "CreateOrderFromGroceryList",
                "arguments": {
                    "household_id": 205,
                    "store_id": 9003,
                    "list_id": 8003,
                    "subtotal_cents": 7500,
                    "total_cents": 8100
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 205,
                    "user_id": 105,
                    "entity_type": "orders",
                    "entity_id": 10003,
                    "action_enum": "place_order"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "095",
        "instruction": "As the meal plan manager for the Martinez Household, locate their meal plan for the week of August 25th. Identify the entry with the note 'Blend half for smoother texture'. Amend the notes for this particular entry (ID 6111) to read 'Blend half for smoother texture and add a dollop of yogurt before serving'. Record this note update in the audit trail with the explanation 'User added a serving suggestion'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Martinez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6002,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Blend half"
                },
            },
            {
                "name": "UpdateMealPlanEntryNotes",
                "arguments": {
                    "entry_id": 6111,
                    "new_notes": "Blend half for smoother texture and add a dollop of yogurt before serving"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6111,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "notes",
                        "reason": "User added a serving suggestion"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "096",
        "instruction": "As a meal plan manager for the Bennett Family, locate the meal plan for the week of August 25th. Identify the entry with the note 'Reduce chili powder for child'. Modify the notes for this entry to read 'Reduce chili powder for child and serve with a side of mild salsa'. Record this change with the reason 'User added a side dish suggestion'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Bennett Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6001,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Reduce chili powder"
                },
            },
            {
                "name": "UpdateMealPlanEntryNotes",
                "arguments": {
                    "entry_id": 6101,
                    "new_notes": "Reduce chili powder for child and serve with a side of mild salsa"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6101,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "notes",
                        "reason": "User added a side dish suggestion"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "097",
        "instruction": "Being a meal plan manager for the Martinez Household, access their meal plan for the week of August 25th. Find the entry with the note 'Peanut-free confirmed'. Alter the notes for this entry to state 'Peanut-free confirmed. Serve with avocado slices.'. Document this adjustment with the reason 'User requested a serving addition'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Martinez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6002,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Peanut-free confirmed"
                },
            },
            {
                "name": "UpdateMealPlanEntryNotes",
                "arguments": {
                    "entry_id": 6113,
                    "new_notes": "Peanut-free confirmed. Serve with avocado slices."
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6113,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "notes",
                        "reason": "User requested a serving addition"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "098",
        "instruction": "As the meal plan manager for the Bennett Family, retrieve their meal plan for the week of August 25th. Identify the entry marked with 'Flake salmon'. Amend the notes for this entry to state 'Flake salmon carefully to remove all bones for Maya'. Record this clarification citing the reason 'User added specific instruction for child'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Bennett Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6001,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Flake salmon"
                },
            },
            {
                "name": "UpdateMealPlanEntryNotes",
                "arguments": {
                    "entry_id": 6103,
                    "new_notes": "Flake salmon carefully to remove all bones for Maya"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6103,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "notes",
                        "reason": "User added specific instruction for child"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "099",
        "instruction": "Acting as the meal plan manager for the Martinez Household, access their meal plan for the week of August 25th. Find the entry that contains the note 'Flake salmon'. Modify the notes for this entry to read 'Flake salmon and serve with a lemon wedge for the adults'. Document this update with the reason 'User added a serving note'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Martinez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6002,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Flake salmon"
                },
            },
            {
                "name": "UpdateMealPlanEntryNotes",
                "arguments": {
                    "entry_id": 6114,
                    "new_notes": "Flake salmon and serve with a lemon wedge for the adults"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6114,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "notes",
                        "reason": "User added a serving note"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "100",
        "instruction": "Manage the Bennett Family's meal plan. Retrieve their plan for the week of August 25th. Identify the entry that includes the note 'Mild curry'. Amend the notes for this entry to read 'Mild curry, and serve with rice instead of naan'. Record this modification citing the reason 'User specified a side dish'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Bennett Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6001,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Mild curry"
                },
            },
            {
                "name": "UpdateMealPlanEntryNotes",
                "arguments": {
                    "entry_id": 6104,
                    "new_notes": "Mild curry, and serve with rice instead of naan"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6104,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "notes",
                        "reason": "User specified a side dish"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "101",
        "instruction": "Oversee the meal plan for the Martinez Household. Access their meal plan for the week of August 25th. Pinpoint the entry containing the note 'Tofu well-cooked'. Modify the notes for this entry to indicate 'Tofu well-cooked and garnish with sesame seeds'. Document this adjustment with the justification 'User added garnish instruction'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Martinez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6002,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Tofu well-cooked"
                },
            },
            {
                "name": "UpdateMealPlanEntryNotes",
                "arguments": {
                    "entry_id": 6115,
                    "new_notes": "Tofu well-cooked and garnish with sesame seeds"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6115,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "notes",
                        "reason": "User added garnish instruction"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "102",
        "instruction": "As the meal plan manager for the Bennett Family, identify their meal plan for the week of August 25th. Find the entry with the note 'Less lemon for child'. Modify the notes for this entry to read 'Less lemon for child, and add some crumbled feta'. Record this modification with the reason 'User added an ingredient'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Bennett Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6001,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Less lemon"
                },
            },
            {
                "name": "UpdateMealPlanEntryNotes",
                "arguments": {
                    "entry_id": 6106,
                    "new_notes": "Less lemon for child, and add some crumbled feta"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6106,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "notes",
                        "reason": "User added an ingredient"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "103",
        "instruction": "As the meal plan manager for the Martinez Household, locate their meal plan for the week of August 25th. Identify the entry with the note 'Add cheese for child'. Alter the notes for this entry to say 'Add cheese for child and also some chopped cucumbers'. Document this change with the reason 'User added another ingredient for child'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Martinez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6002,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Add cheese"
                },
            },
            {
                "name": "UpdateMealPlanEntryNotes",
                "arguments": {
                    "entry_id": 6116,
                    "new_notes": "Add cheese for child and also some chopped cucumbers"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6116,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "notes",
                        "reason": "User added another ingredient for child"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "104",
        "instruction": "As a meal plan manager for the Bennett Family, identify their meal plan for the week of August 25th. Seek the entry containing the note 'Reduce spice'. Amend the notes for this entry to 'Reduce spice and add more bell peppers'. Document this update with the reason 'User requested vegetable addition'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Bennett Family"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 201
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6001,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Reduce spice"
                },
            },
            {
                "name": "UpdateMealPlanEntryNotes",
                "arguments": {
                    "entry_id": 6107,
                    "new_notes": "Reduce spice and add more bell peppers"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 201,
                    "user_id": 101,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6107,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "notes",
                        "reason": "User requested vegetable addition"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "105",
        "instruction": "As a meal plan manager for the Martinez Household, retrieve their meal plan for the week of August 25th. Identify the entry marked with the note 'Low spice'. Revise the notes for this entry to 'Low spice and add a lime wedge for serving'. Record this modification with the reason 'User added a garnish idea'.",
        "actions": [
            {
                "name": "SearchHouseholdsByName",
                "arguments": {
                    "name_query": "Martinez Household"
                },
            },
            {
                "name": "GetMealPlansByHouseholdId",
                "arguments": {
                    "household_id": 202
                },
            },
            {
                "name": "SearchMealPlanEntries",
                "arguments": {
                    "meal_plan_id": 6002,
                    "start_date": "2025-08-25",
                    "end_date": "2025-08-31",
                    "notes_substring": "Low spice"
                },
            },
            {
                "name": "UpdateMealPlanEntryNotes",
                "arguments": {
                    "entry_id": 6117,
                    "new_notes": "Low spice and add a lime wedge for serving"
                },
            },
            {
                "name": "AddAuditLog",
                "arguments": {
                    "household_id": 202,
                    "user_id": 102,
                    "entity_type": "meal_plan_entries",
                    "entity_id": 6117,
                    "action_enum": "update",
                    "payload_json": {
                        "field": "notes",
                        "reason": "User added a garnish idea"
                    }
                }
            }
        ],
        "outputs": []
    }
]
