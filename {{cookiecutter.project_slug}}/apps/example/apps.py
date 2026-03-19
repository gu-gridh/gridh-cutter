{% if cookiecutter.create_example_app == 'y' -%}
from django.apps import AppConfig


class ExampleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.example'
    verbose_name = 'Example App'
{%- endif %}
