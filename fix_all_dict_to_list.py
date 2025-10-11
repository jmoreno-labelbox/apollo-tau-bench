#!/usr/bin/env python3
"""
Fix: data.get('key', []) -> list(data.get('key', {}).values())

This fixes the bug where code expects lists but data is actually dicts.
"""
