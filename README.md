# DICT Project Management System

![Project Demo](docs/demo.gif)

### Setup

Prerequisites:

- In Windows/Mac, simply install Docker Desktop
- In Linux, install Docker Engine and Docker Compose

Steps:

- Build the project. (**NOTE**: You only need to do this once. If you have already done this, skip this step)

  - Clone the project

    `git clone https://github.com/darren-sm/DICT-PMS.git`

  - Navigate to the project directory and create data folders for volumes

    `mkdir data data/postgres data/grafana data/pgadmin`

  - Build and run the project

    - `docker compose build`
    - `docker compose up -d`

  - Perform the Migration and Ingest the data

    ```bash
    docker exec -it system bash -c "python manage.py makemigrations myapp && python manage.py migrate myapp" 
    docker cp ./setup/ system:/tmp
    docker exec -it system bash -c "cd /tmp/setup && python setup.py"
    ```

- Run the project

  `docker compose up`
