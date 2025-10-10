from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="user_20001",
        instruction="As Aiden Mercer (user 101), you are preparing for the week for household 201. Your task is to first check your current inventory. Then, review your existing meal plan (ID 6001) and make two changes: remove the entry for Monday, August 25th (entry ID 6101) and add a new dinner, Lentil Soup (recipe 408), for that same date. Based on the updated plan and your inventory, you will then generate an optimized grocery list, place an order at FreshMart Online (store 9001), and confirm the order's status. Return the final order ID and its status.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 201}),
            Action(name="get_meal_plan_for_week", kwargs={"meal_plan_id": 6001}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6101, "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6001, "recipe_id": 408, "plan_date": "2025-08-25", "user_id": 101}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6001, "household_id": 201, "user_id": 101}),
            Action(name="place_grocery_order", kwargs={"household_id": 201, "store_id": 9001, "list_id": 8003, "user_id": 101}),
            Action(name="get_order_status", kwargs={"order_id": 10003}),
        ],
        outputs=["10003", "placed"]
    ),
    Task(
        annotator="0",
        user_id="user_20002",
        instruction="You are assisting the Thompson retirees (household 210, user 110). They are cleaning out their pantry. Your task is to update their inventory to reflect that they are removing all their Brown Rice (ingredient 1056) and have just used 150g of their Greek Yogurt (ingredient 1023). After the inventory is updated, you need to create a 2-day dinner plan for the week of 2026-03-23 using recipes 435 and 408 and then generate the grocery list based on their new inventory situation. Return the ID of the new grocery list.",
        actions=[
            Action(name="remove_item_from_inventory", kwargs={"household_id": 210, "ingredient_id": 1056, "user_id": 110}),
            Action(name="use_item_from_inventory", kwargs={"household_id": 210, "ingredient_id": 1023, "quantity": 150, "user_id": 110}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2026-03-23", "user_id": 110}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2026-03-23", "user_id": 110}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 408, "plan_date": "2026-03-24", "user_id": 110}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 210, "user_id": 110}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_20003",
        instruction="As Aiden Mercer (user 101), you need to review a past order for household 201. Your task is to get the full details and status of order 10001. You also need to retrieve the details of the grocery list (ID 8001) that was the source for this order. Based on this information, you will then create a new, 2-day dinner plan for the week of 2026-03-30 using recipes 423 and 424. Return the new meal plan ID.",
        actions=[
            Action(name="get_order_status", kwargs={"order_id": 10001}),
            Action(name="get_grocery_list_details", kwargs={"list_id": 8001}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-03-30", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 423, "plan_date": "2026-03-30", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 424, "plan_date": "2026-03-31", "user_id": 101}),
        ],
        outputs=["6003"]
    ),
    Task(
        annotator="0",
        user_id="user_20004",
        instruction="As Priya Patel (user 105), you need to add a new member, 'Rohan Patel' (born 2010-04-10, child, 'medium' activity), to your household (205). Immediately after, you must update his activity level to 'high' and his target calories to 2000. Once the new member is set up, you need to create a 3-day dinner plan for the whole family for the week of 2026-04-06 using recipes 403, 429, and 424, and then generate the grocery list. Return the new member's ID and the new grocery list ID.",
        actions=[
            Action(name="add_household_member", kwargs={"household_id": 205, "new_member_data": {"full_name": "Rohan Patel", "birthdate": "2010-04-10", "is_child": True, "activity_level": "medium"}, "user_id": 105}),
            Action(name="update_member_preferences", kwargs={"member_id": 332, "updates": {"activity_level": "high", "target_calories": 2000}, "user_id": 105}),
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2026-04-06", "user_id": 105}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 403, "plan_date": "2026-04-06", "user_id": 105}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 429, "plan_date": "2026-04-07", "user_id": 105}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 424, "plan_date": "2026-04-08", "user_id": 105}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 205, "user_id": 105}),
        ],
        outputs=["332", "8003"]
    ),
    Task(
        annotator="0",
        user_id="user_20005",
        instruction="You are helping the Mercer household (201, user 101) clear out their pantry and decide on dinner for tonight, September 1st. Your goal is to identify a recipe they can make with their current inventory, allowing for at most 3 missing ingredients. Having found that recipe 402 (Chicken Tacos) is a suitable option, you must then create a new meal plan for the current week and add this recipe to it for tonight's dinner. Return the new meal plan ID and the new meal plan entry ID.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 201}),
            Action(name="find_recipes_by_ingredients", kwargs={"available_ingredient_ids": [1001, 1005, 1006, 1008, 1010, 1011, 1012, 1015, 1024, 1027, 1028, 1029, 1037, 1066], "max_missing_ingredients": 3}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2025-09-01", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2025-09-01", "user_id": 101}),
        ],
        outputs=["6003", "6118"]
    ),
    Task(
        annotator="0",
        user_id="user_10001",
        instruction="As Aiden Mercer (user 101), you need to get groceries for the week for your household (201), based on your existing meal plan (ID 6001). Your goal is to get an order placed at FreshMart Online (store 9001) for only the items you're missing from your current inventory. You also need to confirm the final status of the order once it's placed. Return the order ID and its status.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 201}),
            Action(name="get_meal_plan_for_week", kwargs={"meal_plan_id": 6001}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6001, "household_id": 201, "user_id": 101}),
            Action(name="place_grocery_order", kwargs={"household_id": 201, "store_id": 9001, "list_id": 8003, "user_id": 101}),
            Action(name="get_order_status", kwargs={"order_id": 10003}),
        ],
        outputs=["10003", "placed"]
    ),
    Task(
        annotator="0",
        user_id="user_10002",
        instruction="You are assisting Lina Alvarez (user 102) with household 202. She needs a 3-day dinner plan for the week of 2026-01-19. You will schedule recipe 401 for Monday the 19th, recipe 402 for Tuesday the 20th, and recipe 404 for Wednesday the 21st. Your goal is to finalize this plan, generate the complete grocery list, and then place the order at GrocerDash (store 9002). Please return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2026-01-19", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2026-01-19", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2026-01-20", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 404, "plan_date": "2026-01-21", "user_id": 102}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "user_id": 102}),
            Action(name="place_grocery_order", kwargs={"household_id": 202, "store_id": 9002, "list_id": 8003, "user_id": 102}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_10003",
        instruction="You are helping the Garcia household (208, user 108) figure out dinner for tonight, September 1st. Your task is to check their inventory and find a recipe that is missing at most 3 ingredients. Having identified recipe 424 (Vegetarian Chili), you need to get the full details for that recipe to review the instructions. After reviewing, you will log that the meal was prepared today with a rating of 4. Return the new meal history ID.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 208}),
            Action(name="find_recipes_by_ingredients", kwargs={"available_ingredient_ids": [1008, 1009, 1018, 1019, 1052, 1087, 1104], "max_missing_ingredients": 3}),
            Action(name="get_recipe_details", kwargs={"recipe_id": 424}),
            Action(name="log_meal_as_prepared", kwargs={"household_id": 208, "recipe_id": 424, "plan_date": "2025-09-01", "rating_int": 4, "user_id": 108}),
        ],
        outputs=["6301"]
    ),
    Task(
        annotator="0",
        user_id="user_10004",
        instruction="As James Thompson (user 110) for household 210, you are adding a new recipe for 'Garlic Shrimp Scampi'. It is a 2-serving, American dinner, 10 mins prep, 15 mins cook, 450 calories, 30g protein, and is peanut-free. Instructions: ['Saute garlic in butter', 'Add shrimp and cook', 'Toss with linguine']. It requires 400g of Shrimp (1048) and 300g of Linguine (1063). After adding this recipe, you must create a meal plan for the week of 2026-01-26 and add only your new recipe to it for the first day. Return the new recipe ID and the new meal plan entry ID.",
        actions=[
            Action(name="add_new_recipe", kwargs={
                "user_id": 110,
                "recipe_data": {
                    "recipe_title": "Garlic Shrimp Scampi", "meal_type": "Dinner", "cuisine": "American", "servings_default": 2,
                    "prep_minutes": 10, "cook_minutes": 15, "is_peanut_free": True, "calories_per_serving": 450,
                    "protein_g_per_serving": 30, "instructions_json": ["Saute garlic in butter", "Add shrimp and cook", "Toss with linguine"], "notes": ""
                },
                "ingredients_list": [
                    {"ingredient_id": 1048, "quantity": 400, "unit": "g"},
                    {"ingredient_id": 1063, "quantity": 300, "unit": "g"}
                ]
            }),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2026-01-26", "user_id": 110}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 454, "plan_date": "2026-01-26", "user_id": 110}),
        ],
        outputs=["454", "6118"]
    ),
    Task(
        annotator="0",
        user_id="user_10005",
        instruction="As Priya Patel (user 105) for household 205, you need to stock up on pantry staples. Your goal is to place an order at Budget Foods Express (store 9004) that contains exactly these items: 1000g of White Rice (1006), 500g of Dried Lentils (1053), and 2000g of All-Purpose Flour (1027). To track this ad-hoc purchase, you should associate it with the upcoming week of 2026-02-02. Please handle the necessary list creation and ordering, then return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2026-02-02", "user_id": 105}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 205, "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1006, "quantity": 1000, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1053, "quantity": 500, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1027, "quantity": 2000, "unit": "g", "user_id": 105}),
            Action(name="place_grocery_order", kwargs={"household_id": 205, "store_id": 9004, "list_id": 8003, "user_id": 105}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_9001",
        instruction="As Aiden Mercer (user 101), you are preparing for the week. Your task is to check your household's (201) current inventory and then review your existing meal plan (ID 6001). Based on this information, you will generate an optimized grocery list. After creating the list, you must place an order for all the items at FreshMart Online (store 9001) and then confirm the order's status. Return the final order ID and its status.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 201}),
            Action(name="get_meal_plan_for_week", kwargs={"meal_plan_id": 6001}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6001, "household_id": 201, "user_id": 101}),
            Action(name="place_grocery_order", kwargs={"household_id": 201, "store_id": 9001, "list_id": 8003, "user_id": 101}),
            Action(name="get_order_status", kwargs={"order_id": 10003}),
        ],
        outputs=["10003", "placed"]
    ),
    Task(
        annotator="0",
        user_id="user_9002",
        instruction="You are assisting Lina Alvarez (user 102) with household 202. She needs a 3-day dinner plan for the week of 2026-01-19. You will schedule recipe 401 for Monday the 19th, recipe 402 for Tuesday the 20th, and recipe 404 for Wednesday the 21st. Your goal is to finalize this plan, generate the complete grocery list, and then place the order at GrocerDash (store 9002). Please return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2026-01-19", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2026-01-19", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2026-01-20", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 404, "plan_date": "2026-01-21", "user_id": 102}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "user_id": 102}),
            Action(name="place_grocery_order", kwargs={"household_id": 202, "store_id": 9002, "list_id": 8003, "user_id": 102}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_9003",
        instruction="You are assisting Antonio Garcia (user 108) of household 208. He has settled on making Vegetarian Chili (recipe 424) for dinner tonight, September 1st, believing it's a good match for his current inventory (requiring at most 3 missing ingredients). Your goal is to validate his choice, review the recipe's instructions, and then log the meal as prepared today with a rating of 4. Please return the ID for the new meal history entry.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 208}),
            Action(name="find_recipes_by_ingredients", kwargs={"available_ingredient_ids": [1008, 1009, 1018, 1019, 1052, 1087, 1104], "max_missing_ingredients": 3}),
            Action(name="get_recipe_details", kwargs={"recipe_id": 424}),
            Action(name="log_meal_as_prepared", kwargs={"household_id": 208, "recipe_id": 424, "plan_date": "2025-09-01", "rating_int": 4, "user_id": 108}),
        ],
        outputs=["6301"]
    ),
    Task(
        annotator="0",
        user_id="user_9004",
        instruction="You are assisting David Kowalski (user 106) with household 206. He needs a dinner plan for recipe 435 for Monday, March 9th, 2026. Your goal is to create the plan and order the groceries from FreshMart Online (store 9001). You must handle the fact that Salmon (ingredient 1002) is out of stock by finding and approving a Cod substitute. Return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2026-03-09", "user_id": 106}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2026-03-09", "user_id": 106}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 206, "user_id": 106}),
            Action(name="check_product_availability_at_store", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="find_substitute_products", kwargs={"store_id": 9001, "problem_items": [{"ingredient_id": 1002, "status": "out_of_stock"}]}),
            Action(name="place_grocery_order", kwargs={"household_id": 206, "store_id": 9001, "list_id": 8003, "user_id": 106, "substitutions": [{"original_ingredient_id": 1002, "substitute_product_id": 9182}]}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_9005",
        instruction="As Priya Patel (user 105) for household 205, you need to stock up on pantry staples. Your goal is to place an order at Budget Foods Express (store 9004) that contains exactly these items: 1000g of White Rice (1006), 500g of Dried Lentils (1053), and 2000g of All-Purpose Flour (1027). To track this ad-hoc purchase, you should associate it with the upcoming week of 2026-02-02. Please handle the necessary list creation and ordering, then return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2026-02-02", "user_id": 105}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 205, "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1006, "quantity": 1000, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1053, "quantity": 500, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1027, "quantity": 2000, "unit": "g", "user_id": 105}),
            Action(name="place_grocery_order", kwargs={"household_id": 205, "store_id": 9004, "list_id": 8003, "user_id": 105}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_8001",
        instruction="As Aiden Mercer (user 101), you are preparing for the week. Your task is to check your household's (201) current inventory and then review your existing meal plan (ID 6001). Based on this information, you will generate an optimized grocery list. After creating the list, you must place an order for all the items at FreshMart Online (store 9001) and then confirm the order's status. Return the final order ID and its status.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 201}),
            Action(name="get_meal_plan_for_week", kwargs={"meal_plan_id": 6001}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6001, "household_id": 201, "user_id": 101}),
            Action(name="place_grocery_order", kwargs={"household_id": 201, "store_id": 9001, "list_id": 8003, "user_id": 101}),
            Action(name="get_order_status", kwargs={"order_id": 10003}),
        ],
        outputs=["10003", "placed"]
    ),
    Task(
        annotator="0",
        user_id="user_8002",
        instruction="You are assisting Lina Alvarez (user 102) with household 202. She needs a complete grocery order for a 3-day dinner plan for the week of 2026-02-23. The plan will use recipe 402 for Monday the 23rd, 404 for Tuesday the 24th, and 407 for Wednesday the 25th. Your goal is to create this plan, generate an optimized grocery list that accounts for her current inventory, verify item availability at FreshMart Online (store 9001), and place the final order. Return the order ID.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 202}),
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2026-02-23", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2026-02-23", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 404, "plan_date": "2026-02-24", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 407, "plan_date": "2026-02-25", "user_id": 102}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "user_id": 102}),
            Action(name="check_product_availability_at_store", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="place_grocery_order", kwargs={"household_id": 202, "store_id": 9001, "list_id": 8003, "user_id": 102}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_8003",
        instruction="You are assisting Antonio Garcia (user 108) of household 208. He has settled on making Vegetarian Chili (recipe 424) for dinner tonight, September 1st, believing it's a good match for his current inventory (requiring at most 3 missing ingredients). Your goal is to validate his choice, review the recipe's instructions, and then log the meal as prepared today with a rating of 4. Please return the ID for the new meal history entry.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 208}),
            Action(name="find_recipes_by_ingredients", kwargs={"available_ingredient_ids": [1008, 1009, 1018, 1019, 1052, 1087, 1104], "max_missing_ingredients": 3}),
            Action(name="get_recipe_details", kwargs={"recipe_id": 424}),
            Action(name="log_meal_as_prepared", kwargs={"household_id": 208, "recipe_id": 424, "plan_date": "2025-09-01", "rating_int": 4, "user_id": 108}),
        ],
        outputs=["6301"]
    ),
    Task(
        annotator="0",
        user_id="user_8004",
        instruction="You are assisting David Kowalski (user 106) with household 206. He needs a dinner plan for recipe 435 for Monday, March 9th, 2026. Your goal is to create the plan and order the groceries from FreshMart Online (store 9001). You must handle the fact that Salmon (ingredient 1002) is out of stock by finding and approving a Cod substitute. Return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2026-03-09", "user_id": 106}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2026-03-09", "user_id": 106}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 206, "user_id": 106}),
            Action(name="check_product_availability_at_store", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="find_substitute_products", kwargs={"store_id": 9001, "problem_items": [{"ingredient_id": 1002, "status": "out_of_stock"}]}),
            Action(name="place_grocery_order", kwargs={"household_id": 206, "store_id": 9001, "list_id": 8003, "user_id": 106, "substitutions": [{"original_ingredient_id": 1002, "substitute_product_id": 9182}]}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_8005",
        instruction="As Priya Patel (user 105) for household 205, you need to stock up on pantry staples. Your goal is to place an order at Budget Foods Express (store 9004) that contains exactly these items: 1000g of White Rice (1006), 500g of Dried Lentils (1053), and 2000g of All-Purpose Flour (1027). To track this ad-hoc purchase, you should associate it with the upcoming week of 2026-02-02. Please handle the necessary list creation and ordering, then return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2026-02-02", "user_id": 105}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 205, "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1006, "quantity": 1000, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1053, "quantity": 500, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1027, "quantity": 2000, "unit": "g", "user_id": 105}),
            Action(name="place_grocery_order", kwargs={"household_id": 205, "store_id": 9004, "list_id": 8003, "user_id": 105}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_7001",
        instruction="As user 101 for the Mercer household (201), you've noticed your child Maya (member_id 302) has been more active. Your first task is to check her current profile. After reviewing it, you must update her activity level to 'high' and her target protein to 40g. Based on these new goals, you will then create a 2-day dinner plan for the week of 2026-03-02, using recipes 401 and 402, and generate the grocery list. Return the new list ID.",
        actions=[
            Action(name="get_member_details", kwargs={"member_id": 302}),
            Action(name="update_member_preferences", kwargs={"member_id": 302, "updates": {"activity_level": "high", "target_protein": 40}, "user_id": 101}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-03-02", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2026-03-02", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2026-03-03", "user_id": 101}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "user_id": 101}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_7002",
        instruction="As James Thompson (user 110), you need to update your household (210) inventory because you just discarded your expired Brown Rice (ingredient 1056). With your updated pantry, you need to plan a simple dinner, recipe 404, for the night of 2026-03-09. Your goal is to create the plan, generate a list for any missing items, place an order at FreshMart Online (store 9001), and finally confirm the status of that new order. Return the final order ID and its status.",
        actions=[
            Action(name="remove_item_from_inventory", kwargs={"household_id": 210, "ingredient_id": 1056, "user_id": 110}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2026-03-09", "user_id": 110}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 404, "plan_date": "2026-03-09", "user_id": 110}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 210, "user_id": 110}),
            Action(name="place_grocery_order", kwargs={"household_id": 210, "store_id": 9001, "list_id": 8003, "user_id": 110}),
            Action(name="get_order_status", kwargs={"order_id": 10003}),
        ],
        outputs=["10003", "placed"]
    ),
    Task(
        annotator="0",
        user_id="user_7003",
        instruction="You are assisting Sarah Chen (user 103) from household 203. She wants to plan to bake Chocolate Chip Cookies (recipe 414) for the week of 2026-04-27, but she knows she has no eggs (ingredient 1030). Your goal is to act as a salvage expert by identifying a valid substitute for the eggs. After confirming a banana is a good option, you must create a new meal plan for that week and add the cookie recipe for Monday, April 27th, including a note that a banana will be used as a substitute. Return the new meal plan entry ID.",
        actions=[
            Action(name="get_recipe_details", kwargs={"recipe_id": 414}),
            Action(name="get_recipe_substitutions", kwargs={"recipe_id": 414, "ingredient_id_to_replace": 1030}),
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2026-04-27", "user_id": 103}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 414, "plan_date": "2026-04-27", "meal_type": "Dessert", "user_id": 103, "notes": "Using banana as a substitute for eggs."}),
        ],
        outputs=["6118"]
    ),
    Task(
        annotator="0",
        user_id="user_7004",
        instruction="You are assisting David Kowalski (user 106) with household 206. He wants to make Heart-Healthy Baked Salmon (recipe 435) for dinner on Wednesday, April 15th, 2026. Your goal is to create a meal plan for that week, add the single 2-serving meal, and order the groceries from FreshMart Online (store 9001). You must handle the fact that the Salmon (ingredient 1002) is out of stock by finding and approving a Cod substitute. Return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2026-04-13", "user_id": 106}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2026-04-15", "servings_adult": 2, "user_id": 106}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 206, "user_id": 106}),
            Action(name="check_product_availability_at_store", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="find_substitute_products", kwargs={"store_id": 9001, "problem_items": [{"ingredient_id": 1002, "status": "out_of_stock"}]}),
            Action(name="place_grocery_order", kwargs={"household_id": 206, "store_id": 9001, "list_id": 8003, "user_id": 106, "substitutions": [{"original_ingredient_id": 1002, "substitute_product_id": 9182}]}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_7005",
        instruction="As user 109 for the dairy-free Kim-Smith household (209), you need to create a 2-day dinner plan for the week of 2026-04-20. You will use recipe 404 (Grilled Salmon) for the 20th and recipe 405 (Teriyaki Tofu Bowl) for the 21st. Your goal is to order the groceries from FreshMart Online (store 9001). You must handle the fact that the Salmon (ingredient 1002) is out of stock by finding and approving an available fish substitute. Return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2026-04-20", "user_id": 109}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 404, "plan_date": "2026-04-20", "user_id": 109}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 405, "plan_date": "2026-04-21", "user_id": 109}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 209, "user_id": 109}),
            Action(name="check_product_availability_at_store", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="find_substitute_products", kwargs={"store_id": 9001, "problem_items": [{"ingredient_id": 1002, "status": "out_of_stock"}]}),
            Action(name="place_grocery_order", kwargs={"household_id": 209, "store_id": 9001, "list_id": 8003, "user_id": 109, "substitutions": [{"original_ingredient_id": 1002, "substitute_product_id": 9182}]}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_6001",
        instruction="As Aiden Mercer (user 101), you are preparing for the week. Your task is to check your household's (201) current inventory and then review your existing meal plan (ID 6001). Based on this information, you will generate an optimized grocery list. After creating the list, you must place an order for all the items at FreshMart Online (store 9001) and then confirm the order's status. Return the final order ID and its status.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 201}),
            Action(name="get_meal_plan_for_week", kwargs={"meal_plan_id": 6001}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6001, "household_id": 201, "user_id": 101}),
            Action(name="place_grocery_order", kwargs={"household_id": 201, "store_id": 9001, "list_id": 8003, "user_id": 101}),
            Action(name="get_order_status", kwargs={"order_id": 10003}),
        ],
        outputs=["10003", "placed"]
    ),
    Task(
        annotator="0",
        user_id="user_6002",
        instruction="You are assisting Lina Alvarez (user 102) with household 202. She needs a 3-day dinner plan for the week of 2026-01-19. You will schedule recipe 401 for Monday the 19th, recipe 402 for Tuesday the 20th, and recipe 404 for Wednesday the 21st. Your goal is to finalize this plan, generate the complete grocery list, and then place the order at GrocerDash (store 9002). Please return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2026-01-19", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2026-01-19", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2026-01-20", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 404, "plan_date": "2026-01-21", "user_id": 102}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "user_id": 102}),
            Action(name="place_grocery_order", kwargs={"household_id": 202, "store_id": 9002, "list_id": 8003, "user_id": 102}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_6003",
        instruction="You are helping the Garcia household (208, user 108) figure out dinner for tonight, September 1st. Your task is to check their inventory and find a recipe that is missing at most 3 ingredients. Having identified recipe 424 (Vegetarian Chili), you need to get the full details for that recipe to review the instructions. After reviewing, you will log that the meal was prepared today with a rating of 4. Return the new meal history ID.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 208}),
            Action(name="find_recipes_by_ingredients", kwargs={"available_ingredient_ids": [1008, 1009, 1018, 1019, 1052, 1087, 1104], "max_missing_ingredients": 3}),
            Action(name="get_recipe_details", kwargs={"recipe_id": 424}),
            Action(name="log_meal_as_prepared", kwargs={"household_id": 208, "recipe_id": 424, "plan_date": "2025-09-01", "rating_int": 4, "user_id": 108}),
        ],
        outputs=["6301"]
    ),
    Task(
        annotator="0",
        user_id="user_6004",
        instruction="As James Thompson (user 110) for household 210, you are adding a new recipe for 'Garlic Shrimp Scampi'. It is a 2-serving, American dinner, 10 mins prep, 15 mins cook, 450 calories, 30g protein, and is peanut-free. Instructions: ['Saute garlic in butter', 'Add shrimp and cook', 'Toss with linguine']. It requires 400g of Shrimp (1048) and 300g of Linguine (1063). After adding this recipe, you must create a meal plan for the week of 2026-01-26 and add only your new recipe to it for the first day. Return the new recipe ID and the new meal plan entry ID.",
        actions=[
            Action(name="add_new_recipe", kwargs={
                "user_id": 110,
                "recipe_data": {
                    "recipe_title": "Garlic Shrimp Scampi", "meal_type": "Dinner", "cuisine": "American", "servings_default": 2,
                    "prep_minutes": 10, "cook_minutes": 15, "is_peanut_free": True, "calories_per_serving": 450,
                    "protein_g_per_serving": 30, "instructions_json": ["Saute garlic in butter", "Add shrimp and cook", "Toss with linguine"], "notes": ""
                },
                "ingredients_list": [
                    {"ingredient_id": 1048, "quantity": 400, "unit": "g"},
                    {"ingredient_id": 1063, "quantity": 300, "unit": "g"}
                ]
            }),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2026-01-26", "user_id": 110}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 454, "plan_date": "2026-01-26", "user_id": 110}),
        ],
        outputs=["454", "6118"]
    ),
    Task(
        annotator="0",
        user_id="user_6005",
        instruction="As Priya Patel (user 105) for household 205, you need to stock up on pantry staples. Your goal is to place an order at Budget Foods Express (store 9004) that contains exactly these items: 1000g of White Rice (1006), 500g of Dried Lentils (1053), and 2000g of All-Purpose Flour (1027). To track this ad-hoc purchase, you should associate it with the upcoming week of 2026-02-02. Please handle the necessary list creation and ordering, then return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2026-02-02", "user_id": 105}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 205, "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1006, "quantity": 1000, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1053, "quantity": 500, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1027, "quantity": 2000, "unit": "g", "user_id": 105}),
            Action(name="place_grocery_order", kwargs={"household_id": 205, "store_id": 9004, "list_id": 8003, "user_id": 105}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_5001",
        instruction="As Aiden Mercer (user 101), you just used up all of your Spaghetti (1005) and Tomato Sauce (1012) for household 201. You must update your inventory to show these items are gone. Your goal is to re-stock for another Spaghetti night (recipe 401) by creating a new meal plan for the week of 2026-04-20 with that recipe, generating a list for the missing items, and placing an order at FreshMart Online (store 9001). Return the final order ID.",
        actions=[
            Action(name="remove_item_from_inventory", kwargs={"household_id": 201, "ingredient_id": 1005, "user_id": 101}),
            Action(name="remove_item_from_inventory", kwargs={"household_id": 201, "ingredient_id": 1012, "user_id": 101}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-04-20", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2026-04-20", "user_id": 101}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "user_id": 101}),
            Action(name="place_grocery_order", kwargs={"household_id": 201, "store_id": 9001, "list_id": 8003, "user_id": 101}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_5002",
        instruction="You are assisting Lina Alvarez (user 102) with household 202. She needs a 3-day dinner plan for the week of 2026-01-19. You will schedule recipe 401 for Monday the 19th, recipe 402 for Tuesday the 20th, and recipe 404 for Wednesday the 21st. Your goal is to finalize this plan, generate the complete grocery list, and then place the order at GrocerDash (store 9002). Please return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2026-01-19", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2026-01-19", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2026-01-20", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 404, "plan_date": "2026-01-21", "user_id": 102}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "user_id": 102}),
            Action(name="place_grocery_order", kwargs={"household_id": 202, "store_id": 9002, "list_id": 8003, "user_id": 102}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_5003",
        instruction="You are helping the Garcia household (208, user 108) figure out dinner for tonight, September 1st. Your task is to check their inventory and find a recipe that is missing at most 3 ingredients. Having identified recipe 424 (Vegetarian Chili), you need to get the full details for that recipe to review the instructions. After reviewing, you will log that the meal was prepared today with a rating of 4. Return the new meal history ID.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 208}),
            Action(name="find_recipes_by_ingredients", kwargs={"available_ingredient_ids": [1008, 1009, 1018, 1019, 1052, 1087, 1104], "max_missing_ingredients": 3}),
            Action(name="get_recipe_details", kwargs={"recipe_id": 424}),
            Action(name="log_meal_as_prepared", kwargs={"household_id": 208, "recipe_id": 424, "plan_date": "2025-09-01", "rating_int": 4, "user_id": 108}),
        ],
        outputs=["6301"]
    ),
    Task(
        annotator="0",
        user_id="user_5004",
        instruction="As David Kowalski (user 106) for household 206, you have a new roommate, 'Maria Garcia' (born 1995-05-20, non-child, medium activity), who is vegan. Your first task is to add her to the household. Immediately after, you must update her profile to set her target protein to 90g. With her profile set up, your goal is to create a 2-day dinner plan for her for the week of 2026-04-27 using suitable vegan recipes: 432 and 405. Finally, generate the grocery list for her meals. Return the new member's ID and the new grocery list ID.",
        actions=[
            Action(name="add_household_member", kwargs={"household_id": 206, "new_member_data": {"full_name": "Maria Garcia", "birthdate": "1995-05-20", "is_child": False, "activity_level": "medium"}, "user_id": 106}),
            Action(name="update_member_preferences", kwargs={"member_id": 332, "updates": {"target_protein": 90}, "user_id": 106}),
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2026-04-27", "user_id": 106}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 432, "plan_date": "2026-04-27", "servings_adult": 1, "user_id": 106}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 405, "plan_date": "2026-04-28", "servings_adult": 1, "user_id": 106}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 206, "user_id": 106}),
        ],
        outputs=["332", "8003"]
    ),
    Task(
        annotator="0",
        user_id="user_5005",
        instruction="As Priya Patel (user 105) for household 205, you need to stock up on pantry staples. Your goal is to place an order at Budget Foods Express (store 9004) that contains exactly these items: 1000g of White Rice (1006), 500g of Dried Lentils (1053), and 2000g of All-Purpose Flour (1027). To track this ad-hoc purchase, you should associate it with the upcoming week of 2026-02-02. Please handle the necessary list creation and ordering, then return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2026-02-02", "user_id": 105}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 205, "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1006, "quantity": 1000, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1053, "quantity": 500, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1027, "quantity": 2000, "unit": "g", "user_id": 105}),
            Action(name="place_grocery_order", kwargs={"household_id": 205, "store_id": 9004, "list_id": 8003, "user_id": 105}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_4001",
        instruction="You are assisting Sarah Chen (user 103), a vegetarian, with planning dinners for her household (203). She has chosen recipe 403 (Chickpea Curry), as it's a light meal under 460 calories. Your goal is to create a meal plan for the week of 2026-03-02, schedule this single-serving recipe for both Monday, March 2nd, and Tuesday, March 3rd, and then generate the complete grocery list for the plan. Return the final list ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2026-03-02", "user_id": 103}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 403, "plan_date": "2026-03-02", "servings_adult": 1, "user_id": 103}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 403, "plan_date": "2026-03-03", "servings_adult": 1, "user_id": 103}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 203, "user_id": 103}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_4002",
        instruction="You are assisting the Thompson household (210, user 110). They want to make Chocolate Chip Cookies (recipe 414), but they don't have any Unsalted Butter (ingredient 1029). Your task is to act as a salvage expert: first, confirm the recipe's ingredients, then check the household inventory to see what's available. Based on that, find a valid substitute for the butter that they already have in stock. Having confirmed that Greek Yogurt (ingredient 1023) is a viable and available substitute, you should log that the cookies were successfully prepared today, September 1st, 2025, with a rating of 5 and a note about the substitution. Return the new meal history ID.",
        actions=[
            Action(name="get_recipe_details", kwargs={"recipe_id": 414}),
            Action(name="get_household_inventory", kwargs={"household_id": 210}),
            Action(name="get_recipe_substitutions", kwargs={"recipe_id": 414, "ingredient_id_to_replace": 1029}),
            Action(name="log_meal_as_prepared", kwargs={"household_id": 210, "recipe_id": 414, "plan_date": "2025-09-01", "rating_int": 5, "user_id": 110, "notes": "Substituted butter with Greek Yogurt"}),
        ],
        outputs=["6301"]
    ),
    Task(
        annotator="0",
        user_id="user_4003",
        instruction="As Aiden Mercer (user 101) for household 201, you need to plan a 3-day dinner schedule for the week of 2026-03-16. To avoid repetition, your first step is to review the household's meal history for the last 30 days. After confirming which meals are recent, you will create a plan using three recipes that have not been eaten recently: 423, 425, and 426, scheduled for the first three days of the week. Finally, generate the grocery list for this new plan. Return the list ID.",
        actions=[
            Action(name="get_meal_history", kwargs={"household_id": 201, "days_back": 30}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-03-16", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 423, "plan_date": "2026-03-16", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 425, "plan_date": "2026-03-17", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 426, "plan_date": "2026-03-18", "user_id": 101}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "user_id": 101}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_4004",
        instruction="You are assisting the Alvarez household (202, user 102). You need to create a 2-day dinner plan for the week of 2026-04-13, using recipe 401 for Monday the 13th and recipe 404 for Tuesday the 14th. After generating the list for these meals, you must also manually add 500g of Peanut Butter (ingredient 1041) for school lunches. Your goal is to place a single, complete order for all these items at GrocerDash (store 9002). Return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2026-04-13", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2026-04-13", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 404, "plan_date": "2026-04-14", "user_id": 102}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "user_id": 102}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1041, "quantity": 500, "unit": "g", "user_id": 102}),
            Action(name="place_grocery_order", kwargs={"household_id": 202, "store_id": 9002, "list_id": 8003, "user_id": 102}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_4005",
        instruction="As Marcus Williams (user 104), you need to create a 3-day dinner plan for household 204 for the week of 2026-04-20, accommodating the family's gluten-free needs. The top priority is to confirm the members' dietary restrictions by reviewing the full household profile. The plan should use recipes 431, 432, and 435 for the first three days. Your overall goal is to deliver this finalized plan and a placed grocery order from Health First Market (store 9006). Return the final order ID.",
        actions=[
            Action(name="get_household_profile", kwargs={"household_id": 204}),
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2026-04-20", "user_id": 104}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 431, "plan_date": "2026-04-20", "user_id": 104}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 432, "plan_date": "2026-04-21", "user_id": 104}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2026-04-22", "user_id": 104}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 204, "user_id": 104}),
            Action(name="place_grocery_order", kwargs={"household_id": 204, "store_id": 9006, "list_id": 8003, "user_id": 104}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_3001",
        instruction="As Aiden Mercer (user 101), you need to make final adjustments to your household's (201) meal plan (ID 6001) for the week of August 25, 2025. You've decided to replace the meal on Monday (entry 6101) with a new one: Lentil Soup (recipe 408). Your main goal is to get a grocery order placed at FreshMart Online (store 9001) that accurately reflects this updated plan and your current inventory. Please also confirm the final status of the order. Return the order ID and its status.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 201}),
            Action(name="get_meal_plan_for_week", kwargs={"meal_plan_id": 6001}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6101, "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6001, "recipe_id": 408, "plan_date": "2025-08-25", "user_id": 101}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6001, "household_id": 201, "user_id": 101}),
            Action(name="place_grocery_order", kwargs={"household_id": 201, "store_id": 9001, "list_id": 8003, "user_id": 101}),
            Action(name="get_order_status", kwargs={"order_id": 10003}),
        ],
        outputs=["10003", "placed"]
    ),
    Task(
        annotator="0",
        user_id="user_3002",
        instruction="You are assisting Lina Alvarez (user 102) with her household (202). She needs a 2-day dinner plan for the week of 2026-01-19 using recipes 401 and 402. You must create this plan and add the recipes. In the same session, she also wants to know the current status of her previous order (ID 10002). Return the new meal plan ID and the status of the old order.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2026-01-19", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2026-01-19", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2026-01-20", "user_id": 102}),
            Action(name="get_order_status", kwargs={"order_id": 10002}),
        ],
        outputs=["6003", "delivered"]
    ),
    Task(
        annotator="0",
        user_id="user_3003",
        instruction="You are helping the Garcia household (208, user 108) figure out dinner for tonight, September 1st. Your task is to check their inventory and find a recipe that is missing at most 3 ingredients. Having identified recipe 424 (Vegetarian Chili), you need to get the full details for that recipe to review the instructions. After reviewing, you will log that the meal was prepared today with a rating of 4. Return the new meal history ID.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 208}),
            Action(name="find_recipes_by_ingredients", kwargs={"available_ingredient_ids": [1008, 1009, 1018, 1019, 1052, 1087, 1104], "max_missing_ingredients": 3}),
            Action(name="get_recipe_details", kwargs={"recipe_id": 424}),
            Action(name="log_meal_as_prepared", kwargs={"household_id": 208, "recipe_id": 424, "plan_date": "2025-09-01", "rating_int": 4, "user_id": 108}),
        ],
        outputs=["6301"]
    ),
    Task(
        annotator="0",
        user_id="user_3004",
        instruction="As James Thompson (user 110) for household 210, you are adding a new recipe for 'Garlic Shrimp Scampi'. It is a 2-serving, American dinner, 10 mins prep, 15 mins cook, 450 calories, 30g protein, and is peanut-free. Instructions: ['Saute garlic in butter', 'Add shrimp and cook', 'Toss with linguine']. It requires 400g of Shrimp (1048) and 300g of Linguine (1063). After adding this recipe, you must create a meal plan for the week of 2026-01-26 and add only your new recipe to it for the first day. Return the new recipe ID and the new meal plan entry ID.",
        actions=[
            Action(name="add_new_recipe", kwargs={
                "user_id": 110,
                "recipe_data": {
                    "recipe_title": "Garlic Shrimp Scampi", "meal_type": "Dinner", "cuisine": "American", "servings_default": 2,
                    "prep_minutes": 10, "cook_minutes": 15, "is_peanut_free": True, "calories_per_serving": 450,
                    "protein_g_per_serving": 30, "instructions_json": ["Saute garlic in butter", "Add shrimp and cook", "Toss with linguine"], "notes": ""
                },
                "ingredients_list": [
                    {"ingredient_id": 1048, "quantity": 400, "unit": "g"},
                    {"ingredient_id": 1063, "quantity": 300, "unit": "g"}
                ]
            }),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2026-01-26", "user_id": 110}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 454, "plan_date": "2026-01-26", "user_id": 110}),
        ],
        outputs=["454", "6118"]
    ),
    Task(
        annotator="0",
        user_id="user_3005",
        instruction="As Priya Patel (user 105) for household 205, you need to stock up on pantry staples. Your goal is to place an order at Budget Foods Express (store 9004) that contains exactly these items: 1000g of White Rice (1006), 500g of Dried Lentils (1053), and 2000g of All-Purpose Flour (1027). To track this ad-hoc purchase, you should associate it with the upcoming week of 2026-02-02. Please handle the necessary list creation and ordering, then return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2026-02-02", "user_id": 105}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 205, "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1006, "quantity": 1000, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1053, "quantity": 500, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1027, "quantity": 2000, "unit": "g", "user_id": 105}),
            Action(name="place_grocery_order", kwargs={"household_id": 205, "store_id": 9004, "list_id": 8003, "user_id": 105}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_2001",
        instruction="As Aiden Mercer (user 101), you are preparing for the week for household 201. Your task is to first check your current inventory. Then, review your existing meal plan (ID 6001) and make two changes: remove the entry for Monday, August 25th (entry ID 6101) and add a new dinner, Lentil Soup (recipe 408), for that same date. Based on the updated plan and your inventory, you will then generate an optimized grocery list, place an order at FreshMart Online (store 9001), and confirm the order's status. Return the final order ID and its status.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 201}),
            Action(name="get_meal_plan_for_week", kwargs={"meal_plan_id": 6001}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6101, "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6001, "recipe_id": 408, "plan_date": "2025-08-25", "user_id": 101}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6001, "household_id": 201, "user_id": 101}),
            Action(name="place_grocery_order", kwargs={"household_id": 201, "store_id": 9001, "list_id": 8003, "user_id": 101}),
            Action(name="get_order_status", kwargs={"order_id": 10003}),
        ],
        outputs=["10003", "placed"]
    ),
    Task(
        annotator="0",
        user_id="user_2002",
        instruction="You are assisting Lina Alvarez (user 102) with her household (202). She needs a 2-day dinner plan for the week of 2026-01-19 using recipes 401 and 402. You must create this plan and add the recipes. In the same session, she also wants to know the current status of her previous order (ID 10002). Return the new meal plan ID and the status of the old order.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2026-01-19", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2026-01-19", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2026-01-20", "user_id": 102}),
            Action(name="get_order_status", kwargs={"order_id": 10002}),
        ],
        outputs=["6003", "delivered"]
    ),
    Task(
        annotator="0",
        user_id="user_2003",
        instruction="You are helping the Garcia household (208, user 108) figure out dinner for tonight, September 1st. Your task is to check their inventory and find a recipe that is missing at most 3 ingredients. Having identified recipe 424 (Vegetarian Chili), you need to get the full details for that recipe to review the instructions. After reviewing, you will log that the meal was prepared today with a rating of 4. Return the new meal history ID.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 208}),
            Action(name="find_recipes_by_ingredients", kwargs={"available_ingredient_ids": [1008, 1009, 1018, 1019, 1052, 1087, 1104], "max_missing_ingredients": 3}),
            Action(name="get_recipe_details", kwargs={"recipe_id": 424}),
            Action(name="log_meal_as_prepared", kwargs={"household_id": 208, "recipe_id": 424, "plan_date": "2025-09-01", "rating_int": 4, "user_id": 108}),
        ],
        outputs=["6301"]
    ),
    Task(
        annotator="0",
        user_id="user_2004",
        instruction="As James Thompson (user 110) for household 210, you are adding a new recipe for 'Garlic Shrimp Scampi'. It is a 2-serving, American dinner, 10 mins prep, 15 mins cook, 450 calories, 30g protein, and is peanut-free. Instructions: ['Saute garlic in butter', 'Add shrimp and cook', 'Toss with linguine']. It requires 400g of Shrimp (1048) and 300g of Linguine (1063). After you add this recipe, you must create a meal plan for the week of 2026-01-26 and add your new recipe to it for the first day. Return the new recipe ID and the new meal plan entry ID.",
        actions=[
            Action(name="add_new_recipe", kwargs={
                "user_id": 110,
                "recipe_data": {
                    "recipe_title": "Garlic Shrimp Scampi", "meal_type": "Dinner", "cuisine": "American", "servings_default": 2,
                    "prep_minutes": 10, "cook_minutes": 15, "is_peanut_free": True, "calories_per_serving": 450,
                    "protein_g_per_serving": 30, "instructions_json": ["Saute garlic in butter", "Add shrimp and cook", "Toss with linguine"], "notes": ""
                },
                "ingredients_list": [
                    {"ingredient_id": 1048, "quantity": 400, "unit": "g"},
                    {"ingredient_id": 1063, "quantity": 300, "unit": "g"}
                ]
            }),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2026-01-26", "user_id": 110}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 454, "plan_date": "2026-01-26", "user_id": 110}),
        ],
        outputs=["454", "6118"]
    ),
    Task(
        annotator="0",
        user_id="user_2005",
        instruction="As Priya Patel (user 105) for household 205, you need to stock up on pantry staples. Your goal is to place an order at Budget Foods Express (store 9004) that contains exactly these items: 1000g of White Rice (1006), 500g of Dried Lentils (1053), and 2000g of All-Purpose Flour (1027). To track this ad-hoc purchase, you should associate it with the upcoming week of 2026-02-02. Please handle the necessary list creation and ordering, then return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2026-02-02", "user_id": 105}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 205, "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1006, "quantity": 1000, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1053, "quantity": 500, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1027, "quantity": 2000, "unit": "g", "user_id": 105}),
            Action(name="place_grocery_order", kwargs={"household_id": 205, "store_id": 9004, "list_id": 8003, "user_id": 105}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_1005",
        instruction="You are helping the Mercer household (201, user 101) decide on dinner for tonight, September 1st, by using ingredients they already have. Your task is to find a recipe they can make that is missing at most 3 ingredients. Having identified recipe 402 (Chicken Tacos) as a suitable option, you must then create a new meal plan for the current week and add this recipe to it for tonight's dinner. Return the new meal plan ID and the new meal plan entry ID.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 201}),
            Action(name="find_recipes_by_ingredients", kwargs={"available_ingredient_ids": [1001, 1005, 1006, 1008, 1010, 1011, 1012, 1015, 1024, 1027, 1028, 1029, 1037, 1066], "max_missing_ingredients": 3}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2025-09-01", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2025-09-01", "user_id": 101}),
        ],
        outputs=["6003", "6118"]
    ),
    Task(
        annotator="0",
        user_id="user_1001",
        instruction="As Marcus Williams (user 104) for the Williams-Brown household (204), you need to create a 3-day meal plan for the week of 2026-02-09. Your first priority is to review Zoe's profile (member_id 309) to confirm her dietary needs. Then, you will create the plan, adding a gluten-free breakfast for her (recipe 440) on the first day, followed by two dinners for the whole family on that same day and the next (recipes 431 and 432). After the plan is finalized, you must generate the complete grocery list. Return the new list ID.",
        actions=[
            Action(name="get_member_details", kwargs={"member_id": 309}),
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2026-02-09", "user_id": 104}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 440, "plan_date": "2026-02-09", "meal_type": "Breakfast", "user_id": 104}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 431, "plan_date": "2026-02-09", "meal_type": "Dinner", "user_id": 104}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 432, "plan_date": "2026-02-10", "meal_type": "Dinner", "user_id": 104}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 204, "user_id": 104}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_1002",
        instruction="You are assisting the Thompson retirees (household 210, user 110). They are cleaning out their pantry. Your task is to update their inventory to reflect that they are removing all their Brown Rice (ingredient 1056) and have just used 150g of their Greek Yogurt (ingredient 1023). After the inventory is updated, you need to create a 2-day dinner plan for the week of 2026-03-23 using recipes 435 and 408 and then generate the grocery list based on their new inventory situation. Return the ID of the new grocery list.",
        actions=[
            Action(name="remove_item_from_inventory", kwargs={"household_id": 210, "ingredient_id": 1056, "user_id": 110}),
            Action(name="use_item_from_inventory", kwargs={"household_id": 210, "ingredient_id": 1023, "quantity": 150, "user_id": 110}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2026-03-23", "user_id": 110}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2026-03-23", "user_id": 110}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 408, "plan_date": "2026-03-24", "user_id": 110}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 210, "user_id": 110}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_1003",
        instruction="As Aiden Mercer (user 101), you need to review a past order for household 201. Your task is to get the full details and status of order 10001. You also need to retrieve the details of the grocery list (ID 8001) that was the source for this order. Based on this information, you will then create a new, 2-day dinner plan for the week of 2026-03-30 using recipes 423 and 424. Return the new meal plan ID.",
        actions=[
            Action(name="get_order_status", kwargs={"order_id": 10001}),
            Action(name="get_grocery_list_details", kwargs={"list_id": 8001}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-03-30", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 423, "plan_date": "2026-03-30", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 424, "plan_date": "2026-03-31", "user_id": 101}),
        ],
        outputs=["6003"]
    ),
    Task(
        annotator="0",
        user_id="user_1004",
        instruction="As Priya Patel (user 105), you need to add a new member, 'Rohan Patel' (born 2010-04-10, child, 'medium' activity), to your household (205). Immediately after, you must update his activity level to 'high' and his target calories to 2000. Once the new member is set up, you need to create a 3-day dinner plan for the whole family for the week of 2026-04-06 using recipes 403, 429, and 424, and then generate the grocery list. Return the new member's ID and the new grocery list ID.",
        actions=[
            Action(name="add_household_member", kwargs={"household_id": 205, "new_member_data": {"full_name": "Rohan Patel", "birthdate": "2010-04-10", "is_child": True, "activity_level": "medium"}, "user_id": 105}),
            Action(name="update_member_preferences", kwargs={"member_id": 332, "updates": {"activity_level": "high", "target_calories": 2000}, "user_id": 105}),
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2026-04-06", "user_id": 105}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 403, "plan_date": "2026-04-06", "user_id": 105}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 429, "plan_date": "2026-04-07", "user_id": 105}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 424, "plan_date": "2026-04-08", "user_id": 105}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 205, "user_id": 105}),
        ],
        outputs=["332", "8003"]
    ),
    Task(
        annotator="0",
        user_id="user_801",
        instruction="As Lina Alvarez (user 102), you need to plan two peanut-free dinners for your child in household 202 for the week of 2026-02-16, using recipes 401 and 403. You will schedule recipe 401 for Monday, February 16th, and recipe 403 for Tuesday, February 17th. Your goal is to create this brief plan and then review the full, detailed grocery list that results from it. Please return the ID of the generated grocery list.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2026-02-16", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2026-02-16", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 403, "plan_date": "2026-02-17", "user_id": 102}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "user_id": 102}),
            Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_802",
        instruction="You are assisting Lina Alvarez (user 102) with her household (202). For the week of 2026-02-23, she wants to create a 3-day dinner plan using recipes 402, 404, and 407. Your task is to generate a grocery list that intelligently subtracts the ingredients the household already has in stock and then place an order for the remaining items at FreshMart Online (store 9001). Return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2026-02-23", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2026-02-23", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 404, "plan_date": "2026-02-24", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 407, "plan_date": "2026-02-25", "user_id": 102}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "user_id": 102}),
            Action(name="place_grocery_order", kwargs={"household_id": 202, "store_id": 9001, "list_id": 8003, "user_id": 102}),
        ],
        outputs=["10003"]
    ),
     Task(
        annotator="0",
        user_id="user_803",
        instruction="As Emma Johnson (user 107), you need to manage the Johnson household (207). You have a guest, 'Carol Peletier', so you must add her as a non-child member (born '1970-01-01', 'low' activity). After adding her, you need to plan two single-serving dinners for her for the week of 2026-03-02: recipe 424 for Monday, March 2nd, and recipe 425 for Tuesday, March 3rd. You also need to log that the family ate recipe 428 last night, August 31, 2025, with a rating of 5. Return the new member's ID and the new meal plan ID.",
        actions=[
            Action(name="add_household_member", kwargs={"household_id": 207, "new_member_data": {"full_name": "Carol Peletier", "birthdate": "1970-01-01", "is_child": False, "activity_level": "low"}, "user_id": 107}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2026-03-02", "user_id": 107}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 424, "plan_date": "2026-03-02", "servings_adult": 1, "user_id": 107}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 425, "plan_date": "2026-03-03", "servings_adult": 1, "user_id": 107}),
            Action(name="log_meal_as_prepared", kwargs={"household_id": 207, "recipe_id": 428, "plan_date": "2025-08-31", "rating_int": 5, "user_id": 107}),
        ],
        outputs=["332", "6003"]
    ),
    Task(
        annotator="0",
        user_id="user_804",
        instruction="You are assisting David Kowalski (user 106) with household 206. He needs a 2-day dinner plan for the week of 2026-03-09, using recipes 435 and 425. Your goal is to create this plan and order the groceries from FreshMart Online (store 9001). You must handle the fact that Salmon (ingredient 1002) from recipe 435 is out of stock by finding and approving a Cod substitute. Return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2026-03-09", "user_id": 106}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2026-03-09", "user_id": 106}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 425, "plan_date": "2026-03-10", "user_id": 106}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 206, "user_id": 106}),
            Action(name="check_product_availability_at_store", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="find_substitute_products", kwargs={"store_id": 9001, "problem_items": [{"ingredient_id": 1002, "status": "out_of_stock"}]}),
            Action(name="place_grocery_order", kwargs={"household_id": 206, "store_id": 9001, "list_id": 8003, "user_id": 106, "substitutions": [{"original_ingredient_id": 1002, "substitute_product_id": 9182}]}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_805",
        instruction="You are helping the Garcia household (208, user 108). They need a 2-day dinner plan for the week of 2026-03-16 using recipes 402 and 424. After generating the list for these meals, they also want to stock up on staples. You must manually add 2kg of All-Purpose Flour (1027) and 1kg of White Sugar (1028) to the same grocery list. Finally, place the complete order at Budget Foods Express (store 9004). Return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 208, "week_start_date": "2026-03-16", "user_id": 108}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2026-03-16", "user_id": 108}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 424, "plan_date": "2026-03-17", "user_id": 108}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 208, "user_id": 108}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1027, "quantity": 2000, "unit": "g", "user_id": 108}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1028, "quantity": 1000, "unit": "g", "user_id": 108}),
            Action(name="place_grocery_order", kwargs={"household_id": 208, "store_id": 9004, "list_id": 8003, "user_id": 108}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_901",
        instruction="As user 102 for the Alvarez household (202), you want to see who is in your household. You then want to learn more about a new item, Tahini (ingredient 1130). After reviewing it, you need to add 250g of it to your inventory. With the inventory updated, you must create a meal plan for 2025-12-15 containing recipe 446 (Buddha Bowl) and generate the corresponding grocery list. Return the new list ID.",
        actions=[
            Action(name="list_household_members", kwargs={"household_id": 202}),
            Action(name="get_ingredient_info", kwargs={"ingredient_id": 1130}),
            Action(name="add_item_to_inventory", kwargs={"household_id": 202, "ingredient_id": 1130, "quantity": 250, "unit": "g", "user_id": 102}),
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2025-12-15", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 446, "plan_date": "2025-12-15", "user_id": 102}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "user_id": 102}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_902",
        instruction="You are assisting the Chen household (203, user 103), which is a solo household. You will create a 2-day, single-serving dinner plan for the week of 2025-12-08 using vegetarian recipes 403 and 405. After planning, you must generate the grocery list and place the order at Organic Valley Co-op (store 9003). Return the order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-12-08", "user_id": 103}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 403, "plan_date": "2025-12-08", "servings_adult": 1, "user_id": 103}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 405, "plan_date": "2025-12-09", "servings_adult": 1, "user_id": 103}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 203, "user_id": 103}),
            Action(name="place_grocery_order", kwargs={"household_id": 203, "store_id": 9003, "list_id": 8003, "user_id": 103}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_903",
        instruction="You are assisting Lina Alvarez (user 102) of household 202. She is planning to make a Buddha Bowl (recipe 446) on 2025-12-15. Before she finalizes the plan, she wants to review her list of household members and get information on a new ingredient she bought, Tahini (1130). Your goal is to provide her with the requested information, ensure 250g of the new Tahini is logged in her inventory, and then produce an accurate grocery list for the planned meal. Return the final list ID.",
        actions=[
            Action(name="list_household_members", kwargs={"household_id": 202}),
            Action(name="get_ingredient_info", kwargs={"ingredient_id": 1130}),
            Action(name="add_item_to_inventory", kwargs={"household_id": 202, "ingredient_id": 1130, "quantity": 250, "unit": "g", "user_id": 102}),
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2025-12-15", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 446, "plan_date": "2025-12-15", "user_id": 102}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "user_id": 102}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_904",
        instruction="As user 101 for household 201, you need to manage your inventory and plan a dinner. You just used 400g of Chicken Breast (ingredient 1001), so you must update your inventory. Next, you will create a meal plan for Monday, 2026-01-12, with a single meal: Heart-Healthy Baked Salmon (recipe 435). Your final task is to order the groceries for this meal from FreshMart Online (store 9001), handling the out-of-stock Salmon by approving a Cod substitute. Return the final order ID.",
        actions=[
            Action(name="use_item_from_inventory", kwargs={"household_id": 201, "ingredient_id": 1001, "quantity": 400, "user_id": 101}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-01-12", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2026-01-12", "user_id": 101}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "user_id": 101}),
            Action(name="check_product_availability_at_store", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="find_substitute_products", kwargs={"store_id": 9001, "problem_items": [{"ingredient_id": 1002, "status": "out_of_stock"}]}),
            Action(name="place_grocery_order", kwargs={"household_id": 201, "store_id": 9001, "list_id": 8003, "user_id": 101, "substitutions": [{"original_ingredient_id": 1002, "substitute_product_id": 9182}]}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_905",
        instruction="You are assisting the Garcia household (208, user 108) figure out dinner for tonight, September 1st. Your task is to check their inventory and find a recipe that is missing at most 3 ingredients. Having identified recipe 424 (Vegetarian Chili), you need to get the full details for that recipe to review the instructions. After reviewing, you will log that the meal was prepared today with a rating of 4. Return the new meal history ID.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 208}),
            Action(name="find_recipes_by_ingredients", kwargs={"available_ingredient_ids": [1008, 1009, 1018, 1019, 1052, 1087, 1104], "max_missing_ingredients": 3}),
            Action(name="get_recipe_details", kwargs={"recipe_id": 424}),
            Action(name="log_meal_as_prepared", kwargs={"household_id": 208, "recipe_id": 424, "plan_date": "2025-09-01", "rating_int": 4, "user_id": 108}),
        ],
        outputs=["6301"]
    ),
    Task(
        annotator="0",
        user_id="user_701",
        instruction="As Aiden Mercer (user 101), you need to get groceries for the week for your household (201), based on your existing meal plan (ID 6001). Your goal is to get an order placed at FreshMart Online (store 9001) for only the items you're missing from your current inventory. You also need to confirm the final status of the order once it's placed. Return the order ID and its status.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 201}),
            Action(name="get_meal_plan_for_week", kwargs={"meal_plan_id": 6001}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6001, "household_id": 201, "user_id": 101}),
            Action(name="place_grocery_order", kwargs={"household_id": 201, "store_id": 9001, "list_id": 8003, "user_id": 101}),
            Action(name="get_order_status", kwargs={"order_id": 10003}),
        ],
        outputs=["10003", "placed"]
    ),
    Task(
        annotator="0",
        user_id="user_702",
        instruction="You are assisting Lina Alvarez (user 102) with household 202. She needs a 3-day dinner plan for the week of 2026-01-19. You will schedule recipe 401 for Monday the 19th, recipe 402 for Tuesday the 20th, and recipe 404 for Wednesday the 21st. Your goal is to finalize this plan, generate the complete grocery list, and then place the order at GrocerDash (store 9002). Please return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2026-01-19", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2026-01-19", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2026-01-20", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 404, "plan_date": "2026-01-21", "user_id": 102}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "user_id": 102}),
            Action(name="place_grocery_order", kwargs={"household_id": 202, "store_id": 9002, "list_id": 8003, "user_id": 102}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_703",
        instruction="You are assisting Antonio Garcia (user 108) of household 208. He has settled on making Vegetarian Chili (recipe 424) for dinner tonight, September 1st, believing it's a good match for his current inventory (requiring at most 3 missing ingredients). Your goal is to validate his choice, review the recipe's instructions, and then log the meal as prepared today with a rating of 4. Please return the ID for the new meal history entry.",
        actions=[
            Action(name="get_household_inventory", kwargs={"household_id": 208}),
            Action(name="find_recipes_by_ingredients", kwargs={"available_ingredient_ids": [1008, 1009, 1018, 1019, 1052, 1087, 1104], "max_missing_ingredients": 3}),
            Action(name="get_recipe_details", kwargs={"recipe_id": 424}),
            Action(name="log_meal_as_prepared", kwargs={"household_id": 208, "recipe_id": 424, "plan_date": "2025-09-01", "rating_int": 4, "user_id": 108}),
        ],
        outputs=["6301"]
    ),
    Task(
        annotator="0",
        user_id="user_704",
        instruction="As James Thompson (user 110) for household 210, you are adding a new recipe for 'Garlic Shrimp Scampi'. It is a 2-serving, American dinner, 10 mins prep, 15 mins cook, 450 calories, 30g protein, and is peanut-free. Instructions: ['Saute garlic in butter', 'Add shrimp and cook', 'Toss with linguine']. It requires 400g of Shrimp (1048) and 300g of Linguine (1063). After you add this recipe, you must create a meal plan for the week of 2026-01-26 and add your new recipe to it for the first day. Return the new recipe ID and the new meal plan entry ID.",
        actions=[
            Action(name="add_new_recipe", kwargs={
                "user_id": 110,
                "recipe_data": {
                    "recipe_title": "Garlic Shrimp Scampi", "meal_type": "Dinner", "cuisine": "American", "servings_default": 2,
                    "prep_minutes": 10, "cook_minutes": 15, "is_peanut_free": True, "calories_per_serving": 450,
                    "protein_g_per_serving": 30, "instructions_json": ["Saute garlic in butter", "Add shrimp and cook", "Toss with linguine"], "notes": ""
                },
                "ingredients_list": [
                    {"ingredient_id": 1048, "quantity": 400, "unit": "g"},
                    {"ingredient_id": 1063, "quantity": 300, "unit": "g"}
                ]
            }),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2026-01-26", "user_id": 110}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 454, "plan_date": "2026-01-26", "user_id": 110}),
        ],
        outputs=["454", "6118"]
    ),
    Task(
        annotator="0",
        user_id="user_705",
        instruction="As Priya Patel (user 105) for household 205, you need to stock up on pantry staples. Your goal is to place an order at Budget Foods Express (store 9004) that contains exactly these items: 1000g of White Rice (1006), 500g of Dried Lentils (1053), and 2000g of All-Purpose Flour (1027). To track this ad-hoc purchase, you should associate it with the upcoming week of 2026-02-02. Please handle the necessary list creation and ordering, then return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2026-02-02", "user_id": 105}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 205, "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1006, "quantity": 1000, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1053, "quantity": 500, "unit": "g", "user_id": 105}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1027, "quantity": 2000, "unit": "g", "user_id": 105}),
            Action(name="place_grocery_order", kwargs={"household_id": 205, "store_id": 9004, "list_id": 8003, "user_id": 105}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_601",
        instruction="As user 101 for household 201, you need to check the dietary needs for Maya Mercer (member_id 302). Based on her profile, you are to create a 2-day dinner plan for the week of 2025-12-01 using recipes 401 and 405, which are suitable for a picky eater. After creating the plan, you must generate the grocery list and return its ID.",
        actions=[
            Action(name="get_member_details", kwargs={"member_id": 302}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2025-12-01", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2025-12-01", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 405, "plan_date": "2025-12-02", "user_id": 101}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "user_id": 101}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_602",
        instruction="As James Thompson (user 110) for household 210, you want to bake Butter Shortbread (recipe 416). Your task is to figure out if you can make it, possibly with a substitution from your inventory. You must check the recipe's ingredients, check your inventory, and if Unsalted Butter (1029) is missing, find a valid substitute that you currently have. Having confirmed that you have Greek Yogurt (1023) as a substitute, you will then create a meal plan for the week of 2026-01-19 and add the Butter Shortbread recipe to it for the first day, with a note confirming the substitution. Return the new meal plan entry ID.",
        actions=[
            Action(name="get_recipe_details", kwargs={"recipe_id": 416}),
            Action(name="get_household_inventory", kwargs={"household_id": 210}),
            Action(name="get_recipe_substitutions", kwargs={"recipe_id": 416, "ingredient_id_to_replace": 1029}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2026-01-19", "user_id": 110}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 416, "plan_date": "2026-01-19", "meal_type": "Dessert", "user_id": 110, "notes": "Using Greek Yogurt as a substitute for butter."}),
            Action(name="get_meal_plan_for_week", kwargs={"meal_plan_id": 6003}),
        ],
        outputs=["6118"]
    ),
    Task(
        annotator="0",
        user_id="user_603",
        instruction="As user 102 for the Alvarez household (202), you want to see who is in your household. You then want to learn more about a new item, Tahini (ingredient 1130). After reviewing it, you need to add 250g of it to your inventory. With the inventory updated, you must create a meal plan for 2025-12-15 containing recipe 446 (Buddha Bowl) and generate the corresponding grocery list. Return the new list ID.",
        actions=[
            Action(name="list_household_members", kwargs={"household_id": 202}),
            Action(name="get_ingredient_info", kwargs={"ingredient_id": 1130}),
            Action(name="add_item_to_inventory", kwargs={"household_id": 202, "ingredient_id": 1130, "quantity": 250, "unit": "g", "user_id": 102}),
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2025-12-15", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 446, "plan_date": "2025-12-15", "user_id": 102}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "user_id": 102}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_604",
        instruction="You are creating a 4-day dinner plan for the Johnson family (household 207, user 107) for the week of 2026-01-05. The top priority is ensuring the meals are safe for Sophia's (member_id 320) shellfish allergy, which you must confirm by checking her profile. The family has requested recipes 401, 402, 403, and 404 for the plan. Your overall goal is to deliver a finalized plan and a placed grocery order from Farm Fresh Delivery (store 9007). Return the final order ID.",
        actions=[
            Action(name="get_member_details", kwargs={"member_id": 320}),
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2026-01-05", "user_id": 107}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2026-01-05", "user_id": 107}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2026-01-06", "user_id": 107}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 403, "plan_date": "2026-01-07", "user_id": 107}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 404, "plan_date": "2026-01-08", "user_id": 107}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 207, "user_id": 107}),
            Action(name="place_grocery_order", kwargs={"household_id": 207, "store_id": 9007, "list_id": 8003, "user_id": 107}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_605",
        instruction="As user 101 for household 201, you need to manage your inventory and plan a dinner. You just used 400g of Chicken Breast (ingredient 1001), so you must update your inventory. Next, you will create a meal plan for Monday, 2026-01-12, with a single meal: Heart-Healthy Baked Salmon (recipe 435). Your final task is to order the groceries for this meal from FreshMart Online (store 9001), handling the out-of-stock Salmon by approving a Cod substitute. Return the final order ID.",
        actions=[
            Action(name="use_item_from_inventory", kwargs={"household_id": 201, "ingredient_id": 1001, "quantity": 400, "user_id": 101}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2026-01-12", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2026-01-12", "user_id": 101}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "user_id": 101}),
            Action(name="check_product_availability_at_store", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="find_substitute_products", kwargs={"store_id": 9001, "problem_items": [{"ingredient_id": 1002, "status": "out_of_stock"}]}),
            Action(name="place_grocery_order", kwargs={"household_id": 201, "store_id": 9001, "list_id": 8003, "user_id": 101, "substitutions": [{"original_ingredient_id": 1002, "substitute_product_id": 9182}]}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_501",
        instruction="As Marcus Williams (user 104) for household 204, you need to plan two high-protein dinners. First, get the full details for recipes 425 and 435. After reviewing them, you will create a meal plan for the week of 2025-12-01 and add both recipes to the plan for the first two days. You should also log that you prepared recipe 425 yesterday, August 31, 2025, with a rating of 5. Return the new meal plan ID and the new history entry ID.",
        actions=[
            Action(name="get_recipe_details", kwargs={"recipe_id": 425}),
            Action(name="get_recipe_details", kwargs={"recipe_id": 435}),
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2025-12-01", "user_id": 104}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 425, "plan_date": "2025-12-01", "user_id": 104}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2025-12-02", "user_id": 104}),
            Action(name="log_meal_as_prepared", kwargs={"household_id": 204, "recipe_id": 425, "plan_date": "2025-08-31", "rating_int": 5, "user_id": 104}),
        ],
        outputs=["6003", "6301"]
    ),
    Task(
        annotator="0",
        user_id="user_502",
        instruction="You are assisting Lina Alvarez (user 102) with planning school lunches for her child in household 202, which has a strict peanut restriction. You need to create a 3-day lunch plan for the week of 2025-12-08 using only recipes that are explicitly peanut-free. You will use recipes 409, 410, and 412. After creating the plan, generate the grocery list and return its ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2025-12-08", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 409, "plan_date": "2025-12-08", "meal_type": "Lunch", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 410, "plan_date": "2025-12-09", "meal_type": "Lunch", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 412, "plan_date": "2025-12-10", "meal_type": "Lunch", "user_id": 102}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "user_id": 102}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_503",
        instruction="As David Kowalski (user 106) from household 206, you need to order groceries for a special dinner on 2025-12-15. Your main dish will be Mushroom Risotto (recipe 426). In addition to all the ingredients for the risotto, you must also ensure that 1 Lemon (ingredient 1022) is included in the final order from GrocerDash (store 9002). Please handle the necessary planning and list creation to make this happen and return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2025-12-15", "user_id": 106}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 426, "plan_date": "2025-12-15", "user_id": 106}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 206, "user_id": 106}),
            Action(name="add_item_to_grocery_list", kwargs={"list_id": 8003, "ingredient_id": 1022, "quantity": 1, "unit": "pcs", "user_id": 106}),
            Action(name="place_grocery_order", kwargs={"household_id": 206, "store_id": 9002, "list_id": 8003, "user_id": 106}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_504",
        instruction="As Priya Patel (user 105), you have a new recipe for 'Simple Lentil Wraps' you want to add for your household (205). It's a 4-serving, peanut-free, Indian dinner with 350 calories and 18g protein. Prep is 10 mins, cook is 15 mins. Instructions are ['Cook lentils with spices', 'Serve in warm tortillas']. It needs 250g Dried Lentils (1053) and 8 Corn Tortillas (1008). After you add this recipe, you must create a meal plan for the week of 2025-12-22 and add your new recipe to it for the first night. Return the new recipe ID and the new meal plan entry ID.",
        actions=[
            Action(name="add_new_recipe", kwargs={
                "user_id": 105,
                "recipe_data": {
                    "recipe_title": "Simple Lentil Wraps", "meal_type": "Dinner", "cuisine": "Indian", "servings_default": 4,
                    "prep_minutes": 10, "cook_minutes": 15, "is_peanut_free": True, "calories_per_serving": 350,
                    "protein_g_per_serving": 18, "instructions_json": ["Cook lentils with spices", "Serve in warm tortillas"], "notes": ""
                },
                "ingredients_list": [
                    {"ingredient_id": 1053, "quantity": 250, "unit": "g"},
                    {"ingredient_id": 1008, "quantity": 8, "unit": "pcs"}
                ]
            }),
            Action(name="create_meal_plan", kwargs={"household_id": 205, "week_start_date": "2025-12-22", "user_id": 105}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 454, "plan_date": "2025-12-22", "user_id": 105}),
        ],
        outputs=["454", "6118"]
    ),
    Task(
        annotator="0",
        user_id="user_505",
        instruction="As Marcus Williams (user 104), you need to create a 2-day gluten-free dinner plan for your family (household 204) for the week of 2025-12-29. You will add recipe 435 for Monday, December 29th, and recipe 440 for Tuesday, December 30th. After planning, you will order the groceries from FreshMart Online (store 9001). You must handle the fact that Salmon (ingredient 1002) is out of stock by finding and approving a valid substitute. Return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2025-12-29", "user_id": 104}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2025-12-29", "user_id": 104}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 440, "plan_date": "2025-12-30", "user_id": 104}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 204, "user_id": 104}),
            Action(name="check_product_availability_at_store", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="find_substitute_products", kwargs={"store_id": 9001, "problem_items": [{"ingredient_id": 1002, "status": "out_of_stock"}]}),
            Action(name="place_grocery_order", kwargs={"household_id": 204, "store_id": 9001, "list_id": 8003, "user_id": 104, "substitutions": [{"original_ingredient_id": 1002, "substitute_product_id": 9182}]}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_401",
        instruction="You are assisting Aiden Mercer (user 101) with household 201's existing meal plan (ID 6001). He wants to make several changes for the week of August 25, 2025: 1) remove the Chicken Tacos (entry 6101), 2) replace the Spaghetti (entry 6102) with Grilled Salmon (recipe 404), and 3) add a new dinner, Heart-Healthy Baked Salmon (recipe 435), to the now-empty slot on Monday, August 25. After these plan updates, you must generate the new grocery list, order the items from FreshMart Online (store 9001), and handle the out-of-stock Salmon by finding and approving a fish substitute. Return the new order ID.",
        actions=[
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6101, "user_id": 101}),
            Action(name="update_meal_plan_entry", kwargs={"entry_id": 6102, "updates": {"recipe_id": 404}, "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6001, "recipe_id": 435, "plan_date": "2025-08-25", "user_id": 101}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6001, "household_id": 201, "user_id": 101}),
            Action(name="check_product_availability_at_store", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="find_substitute_products", kwargs={"store_id": 9001, "problem_items": [{"ingredient_id": 1002, "status": "out_of_stock"}]}),
            Action(name="place_grocery_order", kwargs={"household_id": 201, "store_id": 9001, "list_id": 8003, "user_id": 101, "substitutions": [{"original_ingredient_id": 1002, "substitute_product_id": 9182}]}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_402",
        instruction="You are assisting Sarah Chen (user 103), a vegetarian. She needs a 2-day dinner plan for herself for the week of 2025-11-17. You should select two single-serving vegetarian meals: recipe 405 (Teriyaki Tofu Bowl) and recipe 403 (Chickpea Curry). After creating the plan, your task is to order the necessary groceries from Organic Valley Co-op (store 9003). Please return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-11-17", "user_id": 103}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 405, "plan_date": "2025-11-17", "servings_adult": 1, "user_id": 103}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 403, "plan_date": "2025-11-18", "servings_adult": 1, "user_id": 103}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 203, "user_id": 103}),
            Action(name="place_grocery_order", kwargs={"household_id": 203, "store_id": 9003, "list_id": 8003, "user_id": 103}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_403",
        instruction="You are assisting Aiden Mercer (user 101) with household 201. He has just purchased 1kg of Quinoa (ingredient 1007) which needs to be added to his inventory. He wants you to create a 3-day dinner plan for the week of 2025-09-08 that includes recipe 406 (to use the new quinoa), along with recipes 401 and 402. Your goal is to ensure the inventory is updated and then produce an accurate grocery list for this entire plan. Return the final list ID.",
        actions=[
            Action(name="add_item_to_inventory", kwargs={"household_id": 201, "ingredient_id": 1007, "quantity": 1000, "unit": "g", "user_id": 101}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2025-09-08", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 406, "plan_date": "2025-09-08", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2025-09-09", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2025-09-10", "user_id": 101}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "user_id": 101}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_404",
        instruction="You need to create a 4-day, dairy-free dinner plan for the Kim-Smith family (household 209, user 109) for the week of 2025-11-24, using recipes 433, 432, 425, and 431. After planning, you must generate a grocery list and place an order at Specialty Ingredients Direct (store 9005). Return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2025-11-24", "user_id": 109}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 433, "plan_date": "2025-11-24", "user_id": 109}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 432, "plan_date": "2025-11-25", "user_id": 109}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 425, "plan_date": "2025-11-26", "user_id": 109}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 431, "plan_date": "2025-11-27", "user_id": 109}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 209, "user_id": 109}),
            Action(name="place_grocery_order", kwargs={"household_id": 209, "store_id": 9005, "list_id": 8003, "user_id": 109}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_405",
        instruction="You are assisting James Thompson (user 110) of household 210. He wants to prepare recipe 435 (Heart-Healthy Baked Salmon) for dinner on 2025-11-17. Your task is to create a meal plan for that day, generate the grocery list, and place an order at FreshMart Online (store 9001). You must handle the out-of-stock Salmon by finding and approving an available fish substitute. Please return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2025-11-17", "user_id": 110}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2025-11-17", "user_id": 110}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 210, "user_id": 110}),
            Action(name="check_product_availability_at_store", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="find_substitute_products", kwargs={"store_id": 9001, "problem_items": [{"ingredient_id": 1002, "status": "out_of_stock"}]}),
            Action(name="place_grocery_order", kwargs={"household_id": 210, "store_id": 9001, "list_id": 8003, "user_id": 110, "substitutions": [{"original_ingredient_id": 1002, "substitute_product_id": 9182}]}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_301",
        instruction="As Rachel Kim (user 109), you need to create a 3-day meal plan for your household (209) for the week of 2025-10-20, using recipes 401, 402, and 403. After creating the plan, you realize you'd rather have Grilled Salmon (recipe 404) instead of the Spaghetti (recipe 401) on the first day, and you want to cancel the meal for the third day entirely. You must update the first day's entry (ID 6118) and remove the third day's entry (ID 6120). Return the meal plan ID and the updated entry ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2025-10-20", "user_id": 109}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2025-10-20", "user_id": 109}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2025-10-21", "user_id": 109}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 403, "plan_date": "2025-10-22", "user_id": 109}),
            Action(name="update_meal_plan_entry", kwargs={"entry_id": 6118, "updates": {"recipe_id": 404}, "user_id": 109}),
            Action(name="remove_recipe_from_meal_plan", kwargs={"entry_id": 6120, "user_id": 109}),
        ],
        outputs=["6003", "6118"]
    ),
    Task(
        annotator="0",
        user_id="user_302",
        instruction="You are helping Aiden Mercer (user 101) manage household (201). His partner, Jamie (member_id: 303), is starting a fitness program. First, you must update Jamie's profile to a 'high' activity level, with new targets of 2200 calories and 120g protein. After that, create a 3-day high-protein dinner plan for the week of 2025-11-17 using recipes 402, 404, and 407. Finally, generate the grocery list for this new plan and return the list ID.",
        actions=[
            Action(name="update_member_preferences", kwargs={"member_id": 303, "updates": {"activity_level": "high", "target_calories": 2200, "target_protein": 120}, "user_id": 101}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2025-11-17", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2025-11-17", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 404, "plan_date": "2025-11-18", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 407, "plan_date": "2025-11-19", "user_id": 101}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "user_id": 101}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_303",
        instruction="As James Thompson (user 110), you are organizing the pantry for your household (210). You need to remove the Brown Rice (ingredient 1056) entirely. You also just used 150g of Greek Yogurt (ingredient 1023) for a snack. After you update the inventory, you should create a 2-day dinner plan for the week of 2025-10-27 using recipes 435 and 408, and then generate the grocery list. Return the new grocery list ID.",
        actions=[
            Action(name="remove_item_from_inventory", kwargs={"household_id": 210, "ingredient_id": 1056, "user_id": 110}),
            Action(name="use_item_from_inventory", kwargs={"household_id": 210, "ingredient_id": 1023, "quantity": 150, "user_id": 110}),
            Action(name="create_meal_plan", kwargs={"household_id": 210, "week_start_date": "2025-10-27", "user_id": 110}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2025-10-27", "user_id": 110}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 408, "plan_date": "2025-10-28", "user_id": 110}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 210, "user_id": 110}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_304",
        instruction="As user 107, you need to create a 3-day dinner plan for the Johnson family (household 207) for the week of 2025-11-03, ensuring all recipes are shellfish-free. You will use recipes 401, 402, and 403. Once the plan is complete, you must generate the grocery list and place an order at Farm Fresh Delivery (store 9007). Return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2025-11-03", "user_id": 107}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2025-11-03", "user_id": 107}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2025-11-04", "user_id": 107}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 403, "plan_date": "2025-11-05", "user_id": 107}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 207, "user_id": 107}),
            Action(name="place_grocery_order", kwargs={"household_id": 207, "store_id": 9007, "list_id": 8003, "user_id": 107}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_305",
        instruction="As Aiden Mercer (user 101), you need a 2-day dinner plan for your household (201) for the week of 2025-11-10, using recipes 401 and 435. After planning, you will generate a grocery list for an order at FreshMart Online (store 9001). If the Salmon (ingredient 1002) for recipe 435 is out of stock, you should approve a substitution for Cod. Place the final order, including the substitution if necessary, and return the order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2025-11-10", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2025-11-10", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2025-11-11", "user_id": 101}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "user_id": 101}),
            Action(name="check_product_availability_at_store", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="find_substitute_products", kwargs={"store_id": 9001, "problem_items": [{"ingredient_id": 1002, "status": "out_of_stock"}]}),
            Action(name="place_grocery_order", kwargs={"household_id": 201, "store_id": 9001, "list_id": 8003, "user_id": 101, "substitutions": [{"original_ingredient_id": 1002, "substitute_product_id": 9182}]}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_205",
        instruction="You are assisting Aiden Mercer (user 101) from household 201. He just informed you that he has used up all of his tomato sauce (ingredient 1012). Despite this, he wants to schedule Spaghetti (recipe 401) for dinner on Monday, 2025-10-20. Your task is to ensure his inventory is correct and that an order is placed at FreshMart Online (store 9001) for any ingredients needed for that meal. Please provide the final order ID.",
        actions=[
            Action(name="remove_item_from_inventory", kwargs={"household_id": 201, "ingredient_id": 1012, "user_id": 101}),
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2025-10-20", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 401, "plan_date": "2025-10-20", "user_id": 101}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "user_id": 101}),
            Action(name="place_grocery_order", kwargs={"household_id": 201, "store_id": 9001, "list_id": 8003, "user_id": 101}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_104",
        instruction="As user 105 for the Patel family (household 205), you need to add a new child member, 'Rohan Patel', born on 2010-04-10 with medium activity. Immediately update his activity level to 'high'. You also need to log that he ate recipe 403 on 2025-08-31 with a rating of 5. Return the new member ID and the meal log ID.",
        actions=[
            Action(name="add_household_member", kwargs={"household_id": 205, "new_member_data": {"full_name": "Rohan Patel", "birthdate": "2010-04-10", "is_child": True, "activity_level": "medium"}, "user_id": 105}),
            Action(name="update_member_preferences", kwargs={"member_id": 332, "updates": {"activity_level": "high"}, "user_id": 105}),
            Action(name="log_meal_as_prepared", kwargs={"household_id": 205, "recipe_id": 403, "plan_date": "2025-08-31", "rating_int": 5, "user_id": 105}),
        ],
        outputs=["332", "6301"]
    ),
    Task(
        annotator="0",
        user_id="user_201",
        instruction="As David Kowalski (user 106), you need to plan a dinner for your Keto diet. You should create a meal plan for household 206 for the week of 2025-09-22 and add recipe 434 for one adult serving on the first day. Once the plan is made, you must generate the corresponding grocery list and return its ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 206, "week_start_date": "2025-09-22", "user_id": 106}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 434, "plan_date": "2025-09-22", "servings_adult": 1, "user_id": 106}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 206, "user_id": 106}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_202",
        instruction="As Emma Johnson (user 107), you need to create a 3-day dinner plan for your family (household 207) for the week starting 2025-09-29, ensuring all recipes are shellfish-free. You should use recipes 422, 428, and 425 for the first three days. After planning, you must order the groceries from Farm Fresh Delivery (store 9007) and return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 207, "week_start_date": "2025-09-29", "user_id": 107}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 422, "plan_date": "2025-09-29", "user_id": 107}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 428, "plan_date": "2025-09-30", "user_id": 107}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 425, "plan_date": "2025-10-01", "user_id": 107}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 207, "user_id": 107}),
            Action(name="place_grocery_order", kwargs={"household_id": 207, "store_id": 9007, "list_id": 8003, "user_id": 107}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_203",
        instruction="As Antonio Garcia (user 108), you just bought 500g of chicken breast (ingredient 1001) and need to add it to your household's (208) inventory. You want to cook recipe 402, so you must now create a meal plan for tonight, September 1st, add recipe 402 to it, and generate a grocery list which should only contain the items you're missing. Finally, order the items on that list from QuickShop Express (store 9008) and return the order ID.",
        actions=[
            Action(name="add_item_to_inventory", kwargs={"household_id": 208, "ingredient_id": 1001, "quantity": 500, "unit": "g", "user_id": 108}),
            Action(name="create_meal_plan", kwargs={"household_id": 208, "week_start_date": "2025-09-01", "user_id": 108}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2025-09-01", "user_id": 108}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 208, "user_id": 108}),
            Action(name="place_grocery_order", kwargs={"household_id": 208, "store_id": 9008, "list_id": 8003, "user_id": 108}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_204",
        instruction="As Rachel Kim (user 109), you need a 2-day, dairy-free dinner plan for your family (household 209) starting 2025-10-06. You will use recipes 435 and 433. After planning, generate the grocery list and prepare to order from FreshMart Online (store 9001). If Salmon (ingredient 1002) is unavailable, you should approve a substitution for Cod. You must place the final order, making the substitution if necessary, and return the order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 209, "week_start_date": "2025-10-06", "user_id": 109}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2025-10-06", "user_id": 109}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 433, "plan_date": "2025-10-07", "user_id": 109}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 209, "user_id": 109}),
            Action(name="check_product_availability_at_store", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="find_substitute_products", kwargs={"store_id": 9001, "problem_items": [{"ingredient_id": 1002, "status": "out_of_stock"}]}),
            Action(name="place_grocery_order", kwargs={"household_id": 209, "store_id": 9001, "list_id": 8003, "user_id": 109, "substitutions": [{"original_ingredient_id": 1002, "substitute_product_id": 9182}]}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_101",
        instruction="As user 101 for household 201, you are to create a meal plan for the week starting September 8, 2025. Add dinner recipes 402, 404, and 405 for the dates 2025-09-08, 2025-09-10, and 2025-09-12 respectively. Then, generate the complete grocery list for this plan and return the final list_id.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 201, "week_start_date": "2025-09-08", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2025-09-08", "meal_type": "Dinner", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 404, "plan_date": "2025-09-10", "meal_type": "Dinner", "user_id": 101}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 405, "plan_date": "2025-09-12", "meal_type": "Dinner", "user_id": 101}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 201, "user_id": 101}),
            Action(name="get_grocery_list_details", kwargs={"list_id": 8003}),
        ],
        outputs=["8003"]
    ),
    Task(
        annotator="0",
        user_id="user_102",
        instruction="You need to set up Lina Alvarez (household 202) with high-protein dinners for the first two days of the week starting 2025-09-15, since she's training for a 10k. You will use recipes 402 and 404. Once the plan is set, you need to order all the required groceries from GrocerDash (store 9002) and provide the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 202, "week_start_date": "2025-09-15", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 402, "plan_date": "2025-09-15", "meal_type": "Dinner", "user_id": 102}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 404, "plan_date": "2025-09-16", "meal_type": "Dinner", "user_id": 102}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 202, "user_id": 102}),
            Action(name="place_grocery_order", kwargs={"household_id": 202, "store_id": 9002, "list_id": 8003, "user_id": 102}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_103",
        instruction="As Sarah Chen (user 103), a vegetarian, you need a dinner plan for yourself for the week of 2025-09-22. You will add two single-serving meals: recipe 405 for the 22nd and recipe 403 for the 23rd. After finalizing the plan, you must order the groceries from Organic Valley Co-op (store 9003) and return the order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 203, "week_start_date": "2025-09-22", "user_id": 103}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 405, "plan_date": "2025-09-22", "meal_type": "Dinner", "servings_adult": 1, "user_id": 103}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 403, "plan_date": "2025-09-23", "meal_type": "Dinner", "servings_adult": 1, "user_id": 103}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 203, "user_id": 103}),
            Action(name="place_grocery_order", kwargs={"household_id": 203, "store_id": 9003, "list_id": 8003, "user_id": 103}),
        ],
        outputs=["10003"]
    ),
    Task(
        annotator="0",
        user_id="user_105",
        instruction="As user 104, you need to set up a 2-day dinner plan for the Williams-Brown family (household 204) for the week of 2025-09-08, accommodating their gluten and dairy allergies. You should use recipes 435 and 431. After planning, you need to order the groceries from FreshMart Online (store 9001). Be aware that salmon might be out of stock; if so, you should find and approve a suitable fish substitute. Return the final order ID.",
        actions=[
            Action(name="create_meal_plan", kwargs={"household_id": 204, "week_start_date": "2025-09-08", "user_id": 104}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 435, "plan_date": "2025-09-08", "user_id": 104}),
            Action(name="add_recipe_to_meal_plan", kwargs={"meal_plan_id": 6003, "recipe_id": 431, "plan_date": "2025-09-09", "user_id": 104}),
            Action(name="generate_grocery_list_from_meal_plan", kwargs={"meal_plan_id": 6003, "household_id": 204, "user_id": 104}),
            Action(name="check_product_availability_at_store", kwargs={"list_id": 8003, "store_id": 9001}),
            Action(name="find_substitute_products", kwargs={"store_id": 9001, "problem_items": [{"ingredient_id": 1002, "status": "out_of_stock"}]}),
            Action(name="place_grocery_order", kwargs={"household_id": 204, "store_id": 9001, "list_id": 8003, "user_id": 104, "substitutions": [{"original_ingredient_id": 1002, "substitute_product_id": 9182}]}),
        ],
        outputs=["10003"]
    )
]
