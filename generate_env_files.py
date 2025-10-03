#!/usr/bin/env python3
"""
Script to generate env.py files for each domain variation.

This script creates tau-bench style env.py files in each variation directory
within the domains/ folder structure.
"""

import os
from pathlib import Path
import re


def get_domain_class_name(domain_name: str) -> str:
    """Convert domain folder name to class name format."""
    # Split on underscores and hyphens, capitalize each word
    parts = re.split(r'[_-]', domain_name)
    class_name = ''.join(word.capitalize() for word in parts)
    return class_name


def get_service_class_name(service_path: Path) -> str:
    """Extract the service class name from service.py."""
    if not service_path.exists():
        return None
    
    with open(service_path, 'r') as f:
        content = f.read()
    
    # Look for class that inherits from BaseDomain
    match = re.search(r'class\s+(\w+)\s*\(\s*BaseDomain\s*\)', content)
    if match:
        return match.group(1)
    return None


def create_env_file(variation_path: Path, domain_name: str, service_class_name: str):
    """Create an env.py file for a specific variation."""
    
    # Determine the class name for the environment
    domain_class_name = get_domain_class_name(domain_name)
    env_class_name = f"Mock{domain_class_name}DomainEnv"
    
    # Create the env.py content
    env_content = f'''# Copyright Sierra

from tau_bench.envs.base import Env
from domains.{domain_name}.service import {service_class_name}
from domains.{domain_name}.variations.{variation_path.name}.rules import RULES
from domains.{domain_name}.variations.{variation_path.name}.tools import TOOLS
from typing import Optional, Union
from tau_bench.envs.user import UserStrategy


class {env_class_name}(Env):
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
                from domains.{domain_name}.variations.{variation_path.name}.tasks_test import TASKS as tasks
            case _:
                raise ValueError(f"Unknown task split: {{task_split}}")
        
        # Create service instance to get load_data function
        service = {service_class_name}(tools=TOOLS)
        
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
'''
    
    # Write the file
    env_path = variation_path / "env.py"
    with open(env_path, 'w') as f:
        f.write(env_content)
    
    print(f"✓ Created: {env_path}")


def main():
    """Main function to process all domains and variations."""
    domains_path = Path("/Users/sebastianalgharaballi-yanow/apollo-tau-bench/domains")
    
    if not domains_path.exists():
        print(f"Error: domains path not found: {domains_path}")
        return
    
    # Track statistics
    total_created = 0
    total_skipped = 0
    domains_processed = []
    
    # Iterate through all domain directories
    for domain_dir in sorted(domains_path.iterdir()):
        if not domain_dir.is_dir():
            continue
        
        domain_name = domain_dir.name
        
        # Skip special directories
        if domain_name in ['__pycache__', '.git']:
            continue
        
        # Check for service.py and variations/
        service_path = domain_dir / "service.py"
        variations_path = domain_dir / "variations"
        
        if not service_path.exists() or not variations_path.exists():
            print(f"⊘ Skipping {domain_name}: missing service.py or variations/")
            total_skipped += 1
            continue
        
        # Get the service class name
        service_class_name = get_service_class_name(service_path)
        if not service_class_name:
            print(f"⊘ Skipping {domain_name}: couldn't find service class")
            total_skipped += 1
            continue
        
        print(f"\n📁 Processing domain: {domain_name}")
        print(f"   Service class: {service_class_name}")
        
        # Process each variation
        variation_count = 0
        for variation_dir in sorted(variations_path.iterdir()):
            if not variation_dir.is_dir():
                continue
            
            variation_name = variation_dir.name
            
            # Check if required files exist
            required_files = ['rules.py', 'tools.py', 'tasks_test.py']
            missing_files = [f for f in required_files if not (variation_dir / f).exists()]
            
            if missing_files:
                print(f"   ⊘ Skipping {variation_name}: missing {', '.join(missing_files)}")
                continue
            
            # Create env.py
            try:
                create_env_file(variation_dir, domain_name, service_class_name)
                variation_count += 1
                total_created += 1
            except Exception as e:
                print(f"   ✗ Error creating env.py for {variation_name}: {e}")
        
        if variation_count > 0:
            domains_processed.append(f"{domain_name} ({variation_count} variations)")
    
    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total env.py files created: {total_created}")
    print(f"Total variations skipped: {total_skipped}")
    print(f"\nDomains processed:")
    for domain in domains_processed:
        print(f"  • {domain}")


if __name__ == "__main__":
    main()

