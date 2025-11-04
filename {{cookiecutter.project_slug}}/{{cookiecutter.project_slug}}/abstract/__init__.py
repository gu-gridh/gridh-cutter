"""
Abstract Package

Abstract models, views, and utilities for digital humanities projects.
"""

# Make key classes easily importable
from .models import (
    AbstractBaseModel,
    AbstractTagModel, 
    AbstractImageModel,
    AbstractTIFFImageModel,
    AbstractDocumentModel,
    CINameField,
)

from .views import (
    GenericModelViewSet,
    DynamicDepthViewSet,
    GeoViewSet,
    GenericPagination,
)

from .serializers import (
    GenericSerializer,
    DynamicDepthSerializer,
    CountSerializer,
)

from .mixins import GenderedMixin

__all__ = [
    # Models
    'AbstractBaseModel',
    'AbstractTagModel', 
    'AbstractImageModel',
    'AbstractTIFFImageModel',
    'AbstractDocumentModel',
    'CINameField',
    
    # Views
    'GenericModelViewSet',
    'DynamicDepthViewSet', 
    'GeoViewSet',
    'GenericPagination',
    
    # Serializers
    'GenericSerializer',
    'DynamicDepthSerializer',
    'CountSerializer',
    
    # Mixins
    'GenderedMixin',
]
