"""
Pre-generation hook for gridh-cutter.

Validates user input before generating the project.
"""

import re
import sys

PROJECT_SLUG = "{{ cookiecutter.project_slug }}"

# Validate project_slug is a valid Python identifier
if not re.match(r'^[a-z][a-z0-9_]+$', PROJECT_SLUG):
    print(f"ERROR: '{PROJECT_SLUG}' is not a valid project slug.")
    print("Project slug must start with a lowercase letter and contain only")
    print("lowercase letters, numbers, and underscores.")
    sys.exit(1)

# Warn about reserved Python/Django names
RESERVED = {"test", "tests", "site", "django", "admin", "api", "app", "config"}
if PROJECT_SLUG in RESERVED:
    print(f"WARNING: '{PROJECT_SLUG}' may conflict with Python/Django reserved names.")
