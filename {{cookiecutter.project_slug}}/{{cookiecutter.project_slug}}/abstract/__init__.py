"""
Abstract Package

Abstract models, views, and utilities for digital humanities projects.
"""

__all__ = [
    # Models
    'AbstractBaseModel',
    'AbstractTagModel', 
    'AbstractImageModel',
{%- if cookiecutter.use_iiif == 'y' %}
    'AbstractTIFFImageModel',
{% endif -%}
    'AbstractDocumentModel',
    'CINameField',
    
    # Views
    'GenericModelViewSet',
    'DynamicDepthViewSet',
{%- if cookiecutter.use_geospatial == 'y' %}
    'GeoViewSet',
{% endif -%}
    'GenericPagination',
    
    # Serializers
    'GenericSerializer',
    'DynamicDepthSerializer',
    'CountSerializer',
    
    # Mixins
    'GenderedMixin',
]
