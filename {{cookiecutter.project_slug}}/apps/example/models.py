{% if cookiecutter.create_example_app == 'y' -%}
"""
Example Models

Demonstrates how to use the abstract base models from the framework.
"""

from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from {{ cookiecutter.project_slug }}.abstract.models import (
    AbstractBaseModel,
    AbstractTagModel,
    AbstractImageModel,
)


class Place(AbstractBaseModel):
    """
    Example model: a place with a name, description, and optional geometry.
    Inherits created_at, updated_at, and published from AbstractBaseModel.
    """

    name = models.CharField(
        max_length=256,
        verbose_name=_("Name"),
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("Description"),
    )
{%- if cookiecutter.use_geospatial == 'y' %}
    geometry = models.PointField(
        blank=True,
        null=True,
        verbose_name=_("Location"),
    )
{%- endif %}

    class Meta:
        verbose_name = _("Place")
        verbose_name_plural = _("Places")
        ordering = ["name"]

    def __str__(self):
        return self.name


class Tag(AbstractTagModel):
    """
    Example tag model.
    Inherits text field from AbstractTagModel.
    """

    class Meta(AbstractTagModel.Meta):
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class PlaceImage(AbstractImageModel):
    """
    Example image model linked to a Place.
    Inherits uuid and file fields from AbstractImageModel.
    """

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name=_("Place"),
    )
    caption = models.CharField(
        max_length=512,
        blank=True,
        verbose_name=_("Caption"),
    )

    class Meta:
        verbose_name = _("Place Image")
        verbose_name_plural = _("Place Images")
{%- endif %}
