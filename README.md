# gridh-cutter
This is a Django backend template based on cookiecutter for quickly setting up a new project with essential configurations and dependencies. This template is based on Diana framework but for independent use. This gives you a solid starting point for building scalable web applications with Django.


## Features
- Pre-configured Django settings for development and production environments.
- Integration with essential Django apps and middleware.
- Ready-to-use Docker and Docker Compose configurations for containerized deployments.
- Environment management with Conda for consistent development setups.
- Basic project structure with templates for models, views, and URLs.

## Project Structure
The project structure includes the following key components:
- `{{cookiecutter.project_slug}}/`: Main Django project directory containing settings, URLs, and WSGI configuration.
- `apps/`: Directory for Django apps to organize your application logic.
- `templates/`: Directory for HTML templates.
- `static/`: Directory for static files like CSS, JavaScript, and images.
- `Dockerfile` and `docker-compose.yml`: Configuration files for Docker containerization.

## Installation and Setup
1. **Clone the Repository**: Start by cloning this template repository to your local machine.
   ```bash
   git clone
    ```
2. **Create a Conda Environment**: Use the provided `environment.yml` file to create a Conda environment with all necessary dependencies.
   ```bash
   conda env create -f environment.yml
   conda activate {{cookiecutter.project_slug}}
   ```
3. **Configure Environment Variables**: Set up your environment variables for development and production as needed
4. **Run the Development Server**: Navigate to the project directory and start the Django development server.
   ```bash
   cd {{cookiecutter.project_slug}}
   python manage.py runserver
   ```


## create a new project using this template
```bash 
cookiecutter "{{cookiecutter.project_slug}}" --no-input project_name="Digital Manuscripts Archive" project_slug="digital_manuscripts" author_name="Archive Team" author_email="team@archive.edu"
```