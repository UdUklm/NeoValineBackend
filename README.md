# NeoValineBackend
[NeoValine](https://github.com/UdUklm/NeoValine/) 的后端，使用 Django + Xadmin + Django-REST-framework 实现

## How to use???

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
python manage.py runserver
```

## 更多

- [关于自建带有人工审核功能的评论系统的计划](https://www.ohmysites.com/archives/11/)
- [NeoValine：一个基于 Valine 开发的支持人工审核的评论系统](https://www.ohmysites.com/archives/15/)
