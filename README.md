# DICT Project Management System

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

  - Build 

    `docker compose build`

  - Run the project

    `docker compose up -d`

  - Perform the Migration

    `docker ps`

    - Get the container id of the service with the name "system" (e.g. `9040225fb1aa`)

    - Open the container with bash

      `docker exec -it 9040225fb1aa bash`

    - Make migrations

      `python manage.py makemigrations myapp`

    - Create the tables

      `python manage.py migrate myapp`

    - Exit from the container

      `exit`

  - Stop the app

    `docker compose down`

- Run the project

  `docker compose up`

  > Stop with CTRL + C
