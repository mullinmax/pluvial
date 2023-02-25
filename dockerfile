# Set the syntax version for this Dockerfile
# This enables the use of a newer syntax version if available
# More info: https://docs.docker.com/engine/reference/builder/#syntax
# syntax=docker/dockerfile:1

# Use the Python 3.11 image as the base image
FROM python:3.11

# Sets the maintainer of the project
MAINTAINER Maxwell Mullin "inbox@max-was-here.com"

# Set the working directory for the container
# This is the directory where commands will be executed
WORKDIR /beryl

# Copy the contents of the current directory to the container's working directory
COPY . /beryl

# Install the project's dependencies
# If there is a "setup.py" file in the directory, install the project in editable mode
# Otherwise, install the dependencies listed in "requirements.txt"
RUN if [ -f setup.py ]; then pip install -e .; else pip install -r requirements.txt; fi

# Set the default command to run when the container starts
# In this case, run the "main.py" script using the Python interpreter
CMD [ "python", "beryl/main.py" ]

