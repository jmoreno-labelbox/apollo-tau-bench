# Recipes & Shopping List Simulation Dataset

This dataset simulates a recipe and shopping system to support agent workflows described in `proposal.md`. It is organized as JSON tables representing a relational schema, with cross-linked identifiers and realistic values to enable full end-to-end task simulations.

## Files and Schemas

- `users.json` (user_id, email, full_name, created_at)
- `households.json` (household_id, household_name, timezone, primary_user_id)
- `members.json` (member_id, household_id, full_name, birthdate, is_child, activity_level, dietary_notes, allergies_json, target_calories, target_protein)
- `ingredients.json` (ingredient_id, ingredient_name, grocery_section, pantry_staple_flag, peanut_free_flag, default_unit)
- `recipes.json` (recipe_id, recipe_title, meal_type, cuisine, servings_default, prep_minutes, cook_minutes, is_peanut_free, calories_per_serving, protein_g_per_serving, instructions_json, notes)
- `recipe_ingredients.json` (ri_id, recipe_id, ingredient_id, quantity, unit)
- `meal_plans.json` (meal_plan_id, household_id, week_start_date, created_by_user_id, created_at)
- `meal_plan_entries.json` (entry_id, meal_plan_id, plan_date, meal_type, recipe_id, servings_adult, servings_child, notes)
- `meal_history.json` (history_id, household_id, plan_date, recipe_id, was_prepared, rating_int)
- `inventory_items.json` (inv_item_id, household_id, ingredient_id, quantity, unit, location_enum, best_by_date)
- `grocery_lists.json` (list_id, household_id, source_meal_plan_id, created_by_user_id, created_at, status_enum)
- `grocery_list_items.json` (item_id, list_id, ingredient_id, quantity, unit, grocery_section, pantry_staple_flag, overlap_last_month_flag)
- `stores.json` (store_id, store_name, platform_enum, base_url)
- `store_products.json` (product_id, store_id, ingredient_id, product_name, package_size_qty, package_unit, price_cents, stock_status_enum)
- `orders.json` (order_id, household_id, store_id, list_id, status_enum, subtotal_cents, total_cents, placed_ts, scheduled_slot_start_ts, scheduled_slot_end_ts)
- `order_items.json` (order_item_id, order_id, product_id, requested_qty, fulfilled_qty, substitute_product_id)
- `audit_logs.json` (audit_id, household_id, user_id, entity_type, entity_id, action_enum, payload_json, created_at)

## Referential Integrity Overview

- `households.primary_user_id` → `users.user_id`
- `members.household_id` → `households.household_id`
- `recipe_ingredients.recipe_id` → `recipes.recipe_id`
- `recipe_ingredients.ingredient_id` → `ingredients.ingredient_id`
- `meal_plans.household_id` → `households.household_id`
- `meal_plans.created_by_user_id` → `users.user_id`
- `meal_plan_entries.meal_plan_id` → `meal_plans.meal_plan_id`
- `meal_plan_entries.recipe_id` → `recipes.recipe_id`
- `meal_history.household_id` → `households.household_id`
- `meal_history.recipe_id` → `recipes.recipe_id`
- `inventory_items.household_id` → `households.household_id`
- `inventory_items.ingredient_id` → `ingredients.ingredient_id`
- `grocery_lists.household_id` → `households.household_id`
- `grocery_lists.source_meal_plan_id` → `meal_plans.meal_plan_id`
- `grocery_lists.created_by_user_id` → `users.user_id`
- `grocery_list_items.list_id` → `grocery_lists.list_id`
- `grocery_list_items.ingredient_id` → `ingredients.ingredient_id`
- `stores` independent catalog
- `store_products.store_id` → `stores.store_id`
- `store_products.ingredient_id` → `ingredients.ingredient_id`
- `orders.household_id` → `households.household_id`
- `orders.store_id` → `stores.store_id`
- `orders.list_id` → `grocery_lists.list_id`
- `order_items.order_id` → `orders.order_id`
- `order_items.product_id` → `store_products.product_id`
- `order_items.substitute_product_id` → `store_products.product_id` (nullable)
- `audit_logs` reference the acting `user_id`, affected `household_id`, and target entity by `entity_type` + `entity_id`

## How Each Task Uses the Dataset

### Task 1: Weekly Dinner Meal Plan with Child Modifications
- Read: `users`, `households`, `members` (targets for user and child), `recipes`, `recipe_ingredients`, `meal_history`, `inventory_items`
- Compute/filter: nutritional targets from `members.target_calories`/`target_protein`; avoid repeats using `meal_history` within 14 days; ensure max 3 unique ingredients overlap and cuisine cap using `recipes` and `recipe_ingredients`.
- Write: `meal_plans`, `meal_plan_entries` (7 dinners), `grocery_lists`, `grocery_list_items`
- Flags: pantry staples via `ingredients.pantry_staple_flag`; overlap-last-month via comparing `meal_history` dates
- Audit: `audit_logs` entries for plan creation and list creation

### Task 2: Tonight’s Dinner From Inventory (≥10g protein, exclude last week)
- Read: `inventory_items` (current pantry/fridge/freezer), `recipes`, `recipe_ingredients`, `meal_history`
- Filter: exclude recipes eaten in last 7 days from `meal_history`; ensure protein threshold via `recipes.protein_g_per_serving`; balance assumption derived from `recipe_ingredients` groupings and `ingredients.grocery_section`
- Output: chosen recipe and steps from `recipes.instructions_json`; alternatives derived by minimal extra ingredients
- Optional: record into `meal_history` if you simulate preparation

### Task 3: Peanut-Free School Lunches, Grocery Order and Substitutions
- Read: `recipes` (Lunch, no-heat, minimal prep), `recipe_ingredients`, `ingredients` (peanut flags), `stores`, `store_products`
- Write: `grocery_lists`, `grocery_list_items`
- Stock: check `store_products.stock_status_enum` and map to list items; when `out_of_stock`/`low`, find substitutes by same `ingredient_id` alternative product or compatible ingredient
- Order: create `orders`, `order_items` with `substitute_product_id` when substitution occurs
- Audit: log list generation, substitutions, order placement and delivery in `audit_logs`

### Task 4: Cookie Recovery When Eggs Are Missing
- Read: `recipes` (original cookie), `recipe_ingredients`, `inventory_items` (egg quantity 0), `ingredients`
- Substitute search: consider swaps like applesauce, banana, yogurt (available in `ingredients` + inventory for plausibility)
- Alternate desserts: use `recipes` that are egg-free such as `No-Bake Oatmeal Cocoa Cookies`, `Butter Shortbread`, `Banana Nice Cream`
- Output: instructions from `recipes.instructions_json`; record optional decision in `audit_logs`

## Notes on Diversity and Coverage
- **10 households** with diverse compositions: single person, couples, small families, large families (up to 5 members), extended families, and retirees
- **31 household members** spanning ages from newborn to elderly (75+ years) with distinct activity levels (low/medium/high), dietary restrictions (vegetarian, vegan, keto, gluten-free, dairy-free), and comprehensive allergy profiles (peanut, gluten, dairy, shellfish)
- **53 recipes** across 15+ cuisines (Italian, Mexican, Indian, Chinese, Korean, Thai, Moroccan, Mediterranean, etc.) and 5 meal types (Breakfast, Lunch, Dinner, Snack, Dessert) with protein range 1-40g and calorie range 90-520 per serving
- **143 ingredients** including specialty items, international ingredients, dietary alternatives (dairy-free milk, gluten-free flour, vegan cheese), and comprehensive spice/herb selection
- **8 stores** representing different market segments: budget grocers, organic co-ops, specialty ingredient suppliers, health food markets, and farm-to-table delivery services
- **Geographic diversity** across multiple US timezones with realistic regional preferences
- **Comprehensive dietary support**: recipes and ingredients specifically designed for celiac, lactose intolerance, peanut allergies, heart-healthy diets, and athletic nutrition needs
- **Realistic household inventories** reflecting dietary preferences and cooking habits, with proper expiration date management
- **3+ months of meal history** showing authentic cooking patterns, recipe ratings, and preparation success/failure rates
- Pantry staples marked to drive UI flags and list annotation
- Inventory includes strategic zeros (e.g., eggs) to drive recovery flows and substitution scenarios
- Store products vary in `stock_status_enum` with realistic pricing across different store types to test substitution logic
- Orders include examples of out-of-stock items substituted at fulfillment with compatible alternatives

## Getting Started
- Agents can load all JSON files from this folder and construct in-memory indexes by ID for joins.
- Use `week_start_date` and `plan_date` in ISO formats for date logic.
- Treat `instructions_json` as ordered step strings.
- Units are harmonized per `ingredients.default_unit`, but lists may request package-based units (e.g., loaf, bulb) to imitate real-world shopping.
