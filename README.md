# BACKUP SAFTONLINE

A webscrapy to store all the information available on saftonline daily.

## REQUIREMENTS

Before starting, make sure you have Python, pip and Git installed on your system.
- You can check by running:

 ```bash
python --version
pip --version
git --version
```
or, on Linux:

 ```bash
python3 --version
pip3 --version
git --version
```

### WINDOWS INSTALLATION

```bash
#powershell
git clone https://github.com/brenoportella/backup_saftonline
cd backupsaftonline
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python backup.py

```

### LINUX INSTALLATION

```bash
git clone https://github.com/brenoportella/backup_saftonline
cd backupsaftonline
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 backup.py
```

# POSTGRESSQL DOCKER

This project uses Docker and Docker Compose to setup quickly an environment for the database PostgresSQL.

### PostgresSQL

- **Image**: `postgres:latest`
- **Container name**: `postgres_saftonline`
- **Banco de dados**: `bd_saftonline`
- **Usuário**: `user` 
- **Senha**: `password123`
- **Port**: `5432`

## How to use

You will need a initial database to put it online on docker. So, in the `/database` you have the "create_database.py"

### Requirements

Check if Docker and Docker Compose are installed.

- On Linux (debian based) you can check by:

```bash
docker --version
docker-compose --version
```

If you do not have it, install by sudo:

```bash
sudo apt update
sudo apt install docker.io docker-compose -y
```
### Start container

Before install the container, you need go to `/database` folder and edit the `docker-compose.yml`. Change the "container name", "database", "user", "password" and "port" as well as your needs.

To install the container (in `/database`):

```bash
docker-compose up -d
```
This will download the latest official image of postegressql, create a volume `./postegres_data`, where all the data will be storaged and expose the database on the port that you choosed.

### Stop container

```bash
docker-compose down
```

### Connect with database

You can connect with the database using whatever postgresSQL client that you have, like DBeaver, psql, etc.

Use the `docker-compose.yml` information to make login. "HOST IP", "Port", "User", "Password", "Database".

> **IMPORTANT**: The database's data will be locally storage on the folder 'postgres_data'. This volume will not be deleted by the 'docker-compose down', only if you use 'docker-compose down -v'.