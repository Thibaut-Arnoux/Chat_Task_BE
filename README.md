
## Set MySQL

```shell
# Connexion to mysql

sudo mysql -u root -p

# Create chat_task database

CREATE DATABASE chat_task;

# Be sure it is created

SHOW DATABASES;

# Create User for this database (update password)

CREATE USER 'chattask'@'localhost' IDENTIFIED BY 'password';

# Give Access for this database

GRANT ALL PRIVILEGES ON chat_task.* TO 'chattask'@'localhost';
```

## Set env

```
pip install -r requirements.txt

# if problem with mysqlclient install :

sudo apt-get install libmysqlclient-dev
```

## Start App

Linux
```
export FLASK_APP=app.py
export ENV_FILE_LOCATION=./.env

flask run
```

Windows
```
set FLASK_APP=app.py
set ENV_FILE_LOCATION=./.env
```