"""
Post-generation hook for gridh-cutter.

Removes files and directories based on cookiecutter options.
"""

import os
import shutil

PROJECT_DIR = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    """Remove a file if it exists."""
    full_path = os.path.join(PROJECT_DIR, filepath)
    if os.path.isfile(full_path):
        os.remove(full_path)


def remove_dir(dirpath):
    """Remove a directory tree if it exists."""
    full_path = os.path.join(PROJECT_DIR, dirpath)
    if os.path.isdir(full_path):
        shutil.rmtree(full_path)


# Remove Docker files if not using Docker
if "{{ cookiecutter.use_docker }}" != "y":
    remove_file("Dockerfile")
    remove_file("docker-compose.yml")

# Remove pre-commit config if not using pre-commit
if "{{ cookiecutter.use_pre_commit }}" != "y":
    remove_file(".pre-commit-config.yaml")

# Remove pytest files if not using pytest
if "{{ cookiecutter.use_pytest }}" != "y":
    remove_file("pytest.ini")
    remove_file("conftest.py")
    remove_file("run_tests.py")

# Remove example app if not requested
if "{{ cookiecutter.create_example_app }}" != "y":
    remove_dir("apps/example")

print("Project {{ cookiecutter.project_name }} generated successfully!")
print("")
print("Next steps:")
print("  1. cd {{ cookiecutter.project_slug }}")
print("  2. conda env create -f environment.yml")
print("  3. conda activate {{ cookiecutter.project_slug }}-env")
print("  4. cp .env.example .env  (and edit with your settings)")
print("  5. python manage.py migrate")
print("  6. python manage.py createsuperuser")
print("  7. python manage.py runserver")
