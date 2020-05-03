# NeoValineBackend
NeoValine 的后端，使用 Django + Xadmin + Django-REST-framework 实现

## Run

```bash
# add hidden options file firstly

sqlite3 db.sqlite3  # create db

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py makemigrations user
python manage.py makemigrations comment
python manage.py makemigrations
python manage.py migrate user
python manage.py migrate comment
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```
