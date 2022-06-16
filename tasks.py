"""Task file for the SCRIBES project.
"""
from invoke import task


@task
def install_backend(c):
    """Install the Python backend of the SCRIBES application.
    """


@task
def run_backend(c):
    """Run the Python backend of the SCRIBES application.
    """


@task
def deploy_backend(c):
    """Deploy the backend of the SCRIBES application as a docker container.
    """


@task
def install_frontend(c):
    """Install the frontend of the SCRIBES application.
    """


@task
def run_frontend(c):
    """Run the frontend of the SCRIBES application.
    """


@task
def deploy_frontend(c):
    """Deploy the frontend of the SCRIBES application as a docker container.
    """


@task
def install(c):
    """Install the frontend and the backend of the SCRIBES application as a docker container.
    """


@task
def run(c):
    """Run the frontend and the backend of the SCRIBES application as a docker container.
    """


@task
def deploy(c):
    """Deploy the frontend and the backend of the SCRIBES application as a docker container.
    """
