# GRIDH Cutter

A [Cookiecutter](https://cookiecutter.readthedocs.io/) template for quickly scaffolding Django backend projects at [GRIDH](https://www.gu.se/en/digital-humanities) (Gothenburg Research Infrastructure in Digital Humanities). Built on patterns from the Diana framework, adapted for standalone use.

It generates a ready-to-run Django project with REST APIs, PostgreSQL/PostGIS support, IIIF image handling, Conda environment management, and optional Docker deployment — so you can focus on your research application instead of boilerplate.

---

## Features

| Feature | Description |
|---|---|
| **Abstract base models** | Reusable models for common DH patterns: base entities, tags, images, IIIF pyramid TIFFs |
| **REST API** | Django REST Framework with filtering, pagination, dynamic depth serialization, and GeoJSON support |
| **PostgreSQL + PostGIS** | Geospatial database support out of the box (optional) |
| **Conda environment** | `environment.yml` generated with all dependencies pinned to your chosen Python version |
| **Docker** | Dockerfile and docker-compose.yml with PostgreSQL, Redis, and Celery services (optional) |
| **Multi-database routing** | Built-in database routers for projects that need multiple databases |
| **Admin enhancements** | Admin interface with color fields, range filters, CKEditor, map widgets |
| **IIIF support** | Storage classes and utilities for IIIF image serving |
| **Testing** | pytest setup with fixtures, coverage, and example tests (optional) |
| **Pre-commit hooks** | Code formatting with Black, isort, flake8 (optional) |
| **i18n** | Internationalization setup with English and Swedish locales |
| **API documentation** | DRF Spectacular for OpenAPI schema generation (optional) |

---

## Requirements

- Python 3.8+
- [Cookiecutter](https://cookiecutter.readthedocs.io/) (install once, use everywhere)
- [Conda](https://docs.conda.io/) or [Miniconda](https://docs.anaconda.com/miniconda/) (recommended for environment management)

---

## Quick Start

### 1. Install Cookiecutter

Using pip:
```bash
pip install cookiecutter
```

Or using [uv](https://docs.astral.sh/uv/):
```bash
uv tool install cookiecutter
```

### 2. Generate Your Project

```bash
cookiecutter https://github.com/gu-gridh/gridh-cutter
```

You will be prompted with configuration options:

```
project_name [My Digital Humanities Project]: Maritime Heritage Archive
project_slug [maritime_heritage_archive]:
project_short_description [...]: A digital archive for maritime heritage data
author_name [Your Name]: GRIDH Team
author_email [your.email@example.com]: gridh@gu.se
version [0.1.0]:
license [MIT]:
python_version [3.11]:
django_version [4.2]:
use_postgresql [y]:
use_docker [y]:
use_celery [n]:
use_redis [n]:
use_geospatial [y]:
use_drf_spectacular [y]:
use_pytest [y]:
use_pre_commit [y]:
create_example_app [y]:
```

Or generate non-interactively:
```bash
cookiecutter https://github.com/gu-gridh/gridh-cutter \
  --no-input \
  project_name="Maritime Heritage Archive" \
  author_name="GRIDH Team" \
  use_geospatial=y \
  use_docker=y
```

### 3. Set Up Your Environment

```bash
cd maritime_heritage_archive

# Create and activate Conda environment
conda env create -f environment.yml
conda activate maritime_heritage_archive-env

# Configure environment variables
cp .env.example .env
# Edit .env with your database credentials and secret key
```

### 4. Set Up the Database

```bash
# If using Docker for PostgreSQL:
docker compose up db -d

# Run migrations and create admin user
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run the Server

```bash
python manage.py runserver
```

Visit:
- **Admin panel**: http://localhost:8000/admin/
- **API root**: http://localhost:8000/

---

## Generated Project Structure

```
your_project_slug/
├── manage.py                    # Django management script
├── environment.yml              # Conda environment definition
├── requirements.txt             # pip alternative to environment.yml
├── .env.example                 # Environment variables template
├── .gitignore
├── configs/
│   └── apps.json                # App registry for multi-app projects
├── your_project_slug/           # Django project package
│   ├── settings/
│   │   ├── base.py              # Shared settings
│   │   ├── dev.py               # Development overrides
│   │   └── production.py        # Production overrides
│   ├── abstract/                # Reusable framework components
│   │   ├── models.py            # Abstract base models
│   │   ├── views.py             # Generic viewsets
│   │   ├── serializers.py       # Generic serializers
│   │   ├── mixins.py            # Model mixins
│   │   ├── schemas.py           # OpenAPI schema customization
│   │   └── test.py              # Test utilities and base classes
│   ├── urls.py                  # URL configuration
│   ├── routers.py               # Multi-database routing
│   ├── storages.py              # IIIF and file storage classes
│   └── utils.py                 # Utility functions
├── apps/                        # Your application modules go here
│   └── example/                 # Example app (if selected)
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       ├── urls.py
│       ├── admin.py
│       └── tests.py
├── Dockerfile                   # (if Docker selected)
├── docker-compose.yml           # (if Docker selected)
├── pytest.ini                   # (if pytest selected)
├── conftest.py                  # (if pytest selected)
└── .pre-commit-config.yaml      # (if pre-commit selected)
```

---

## How to Use

### Creating a New App

Create your app inside the `apps/` directory:

```bash
cd apps
django-admin startapp my_new_app
```

Then in `my_new_app/models.py`, use the abstract base models:

```python
from django.contrib.gis.db import models
from your_project.abstract.models import AbstractBaseModel, AbstractImageModel

class Artifact(AbstractBaseModel):
    """Inherits created_at, updated_at, published fields automatically."""
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    location = models.PointField(blank=True, null=True)

class ArtifactImage(AbstractImageModel):
    """Inherits uuid and file fields. Supports IIIF pyramid TIFF generation."""
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE, related_name="images")
```

Create a serializer in `my_new_app/serializers.py`:

```python
from your_project.abstract.serializers import DynamicDepthSerializer
from .models import Artifact

class ArtifactSerializer(DynamicDepthSerializer):
    class Meta(DynamicDepthSerializer.Meta):
        model = Artifact
        fields = "__all__"
```

Create a viewset in `my_new_app/views.py`:

```python
from your_project.abstract.views import GeoViewSet
from .models import Artifact
from .serializers import ArtifactSerializer

class ArtifactViewSet(GeoViewSet):
    queryset = Artifact.objects.filter(published=True)
    serializer_class = ArtifactSerializer
    bbox_filter_field = "location"
```

Wire up URLs in `my_new_app/urls.py`:

```python
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"artifacts", views.ArtifactViewSet)

urlpatterns = [
    path("api/my_app/", include(router.urls)),
]
```

### Registering Apps

**Option A — Manual:** Add your app to `INSTALLED_APPS` in `settings/base.py`.

**Option B — Dynamic (multi-app):** Add an entry to `configs/apps.json`:

```json
[
  {
    "name": "my_new_app",
    "config": "MyNewAppConfig",
    "managed": true
  }
]
```

Apps with `"managed": true` use the default database. Apps with `"managed": false` get their own database via the `AppRouter`.

### Abstract Models Reference

| Model | Fields Provided | Use Case |
|---|---|---|
| `AbstractBaseModel` | `created_at`, `updated_at`, `published` | Base for all models |
| `AbstractTagModel` | `text` (unique, case-insensitive) | Tags, categories, keywords |
| `AbstractMetaDataModel` | `text`, `translation` | Metadata with translations |
| `AbstractImageModel` | `uuid`, `file` (with storage) | Image uploads |
| `AbstractTIFFImageModel` | Extends image with IIIF TIFF | IIIF image serving |

### Abstract Views Reference

| ViewSet | Features | Use Case |
|---|---|---|
| `GenericModelViewSet` | Read-only, filtering, pagination, count | Basic API endpoints |
| `DynamicDepthViewSet` | Configurable `?depth=N` serialization | Nested relationship control |
| `GeoViewSet` | Bounding box filter, GeoJSON pagination | Geospatial data APIs |

### Running Tests

```bash
# Run all tests
pytest

# Run tests for a specific app
python run_tests.py --app example

# Run with coverage
python run_tests.py --coverage

# Run only API tests
python run_tests.py --api
```

---

## Configuration Options

| Option | Default | Description |
|---|---|---|
| `project_name` | My Digital Humanities Project | Human-readable project name |
| `project_slug` | *(auto-generated)* | Python package name (lowercase, underscores) |
| `python_version` | 3.11 | Python version for Conda environment |
| `django_version` | 4.2 | Django version constraint |
| `use_postgresql` | y | Use PostgreSQL (vs SQLite) |
| `use_docker` | y | Generate Dockerfile and docker-compose.yml |
| `use_celery` | y | Include Celery for background tasks |
| `use_redis` | y | Include Redis for caching/message broker |
| `use_geospatial` | y | PostGIS, GDAL, GeoJSON support |
| `use_drf_spectacular` | y | OpenAPI/Swagger documentation |
| `use_pytest` | y | pytest configuration and test utilities |
| `use_pre_commit` | y | Pre-commit hooks (Black, isort, flake8) |
| `create_example_app` | y | Generate an example app with models, views, tests |

---

## Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
# Required
SECRET_KEY=your-secret-key-here          # Generate: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
DB_LOCAL_NAME=your_project_dev
DB_LOCAL_USER=your_project_user
DB_LOCAL_PASS=your_password
DB_HOST=localhost
DB_PORT=5432

# Optional
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:8080
```

---

## Deployment

### With Docker

```bash
# Build and start all services
docker compose up --build -d

# Run migrations inside container
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

### Without Docker (Production)

```bash
# Set environment
export DJANGO_SETTINGS_MODULE=your_project.settings.production

# Collect static files
python manage.py collectstatic --noinput

# Run with Gunicorn
gunicorn your_project.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

---

## License

BSD 3-Clause License. See [LICENSE](LICENSE) for details.

Developed by [GRIDH](https://www.gu.se/en/digital-humanities) — Gothenburg Research Infrastructure in Digital Humanities.
