{% if cookiecutter.use_docker == 'y' -%}
FROM python:{{ cookiecutter.python_version }}-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
{%- if cookiecutter.use_postgresql == 'y' %}
    libpq-dev \
{%- endif %}
{%- if cookiecutter.use_geospatial == 'y' %}
    gdal-bin \
    libgdal-dev \
    libgeos-dev \
    libproj-dev \
{%- endif %}
    libvips-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

CMD ["gunicorn", "{{ cookiecutter.project_slug }}.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
{%- endif %}
