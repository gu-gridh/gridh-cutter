{% if cookiecutter.create_example_app == 'y' -%}
"""
Example Views

Demonstrates how to use the abstract viewsets.
"""

from {{ cookiecutter.project_slug }}.abstract.views import DynamicDepthViewSet{% if cookiecutter.use_geospatial == 'y' %}, GeoViewSet{% endif %}

from .models import Place, Tag
from .serializers import PlaceSerializer, TagSerializer


class PlaceViewSet({% if cookiecutter.use_geospatial == 'y' %}GeoViewSet{% else %}DynamicDepthViewSet{% endif %}):
    """API endpoint for Places"""
    queryset = Place.objects.filter(published=True)
    serializer_class = PlaceSerializer
{%- if cookiecutter.use_geospatial == 'y' %}
    bbox_filter_field = "geometry"
{%- endif %}


class TagViewSet(DynamicDepthViewSet):
    """API endpoint for Tags"""
    queryset = Tag.objects.filter(published=True)
    serializer_class = TagSerializer
{%- endif %}
