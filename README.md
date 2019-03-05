# flask-login-register
Flask login register with SqlAlchemy Postgresql bcrypt
 
### Create new virtualenviroment on Python 3 ###
Bellow command you can create new virtualenv
```bash
python3 -m venv .venv
```
### Dotenv file make to .env file ###
Create new .env file and source enviroment variables
```bash
cp dotenv .env
source .env
```

### Migrate database ###
Create Postgresql database with migration
#####If first time to migrate database run this command
```bash
python manage.py db init
```
#####Then if you want to migrate database use this command
```bash
python manage.py db migrate
python manage.py db upgrade
```
### Runserver App ###

```bash
python run.py
```
