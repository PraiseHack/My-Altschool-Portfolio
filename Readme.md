
# Dockerized PostgreSQL Database with psycopg2

This project demonstrates how to set up a Dockerized PostgreSQL database and use psycopg2 to execute queries from a Python application.

## Prerequisites

Before running the project, ensure that you have the following prerequisites installed on your system:

[Docker](https://www.docker.com/products/docker-desktop/)

[Python](https://www.python.org/downloads/)

### Getting Started

Follow these steps to get the project up and running:

1. Clone the Repository: Clone this repository to your local machine using the following command:

git clone (https://github.com/PraiseHack/Alt-DE-Projects.git)

2. Navigate to the Project Directory: Change to the project directory:

cd your_project

3. Set Up Docker Container: Use Docker Compose to set up a PostgreSQL container. Run the following command:

docker-compose up

This command will create and start a Docker container running PostgreSQL using the configuration specified in docker-compose.yml

4. Create a virtual environment for the python code using the following command for windows users:

.\venv\Scripts\Activate

5. Create a requirements.txt file with the command echo > requirements.txt for windows users, this is where dependencies for the project will be stored.
pip install psycopg2 and dotenv modules and then pip freeze. Also pip install black for code reformatting.

pip freeze > requirements.txt at root directory to include all recent pip installations.

6. Run the Python Script: Execute the Python script main.py to perform database operations using psycopg2:

python main.py

This script connects to the PostgreSQL database running in the Docker container, executes some sample queries, and prints the results.

7. Verify Results: Check the output of the Python script to verify that the queries were executed successfully.

### Project Structure
The project directory contains the following files:

1. init.sql: SQL create schema and table script.
2. docker-compose.yml: Docker Compose configuration file for setting up PostgreSQL.
3. requirements.txt: Python dependencies required for the project.
4. main.py: Python script demonstrating database operations using psycopg2.
5. db_manager.py: Python script to manage connection to PostgreSQL database
6. README.md: This README file providing instructions and project information.

### Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create a GitHub issue or submit a pull request.












