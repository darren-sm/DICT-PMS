# DICT Project Management System

### Setup

Prerequisites:

- In Windows/Mac, simply install Docker Desktop
- In Ubuntu, install Docker Engine and Docker Compose

Steps:

1. Clone the project repository
2. Navigate to the project directory on the terminal and run:

   - `mkdir data data/postgres data/grafana data/pgadmin`
   - `docker compose up --build`

​	3. Open the web app in your browser at http://localhost:8000/

### Development

1. At project root, create a virtual environment and enable it

   `python -m venv venv && source venv/bin/activate`

2. Navigate to the web directory

   `cd web`

3. Install the dependencies

   `pip install -r requirements.txt`

From here, you can continue the development, for example by creating another app:

`python manage.py startapp someapp`



