HIDDEN_SECRET_KEY = 'xxxxxxxx'  # generate django secret_key by youself

MAIL_SETTINGS = {
    'SMTP_SERVER': 'smtp.qq.com',
    'PORT': '25',
    'SSL_PORT': '465',              # if not QQ mail, change it
    'USERNAME': 'xxxxxxxx',         # Your qq number
    'ADDRESS': 'xxxxxx@qq.com',     # Your qq email address
    'PASSWORD': 'xxxxxxxxx',        # Your qq email SMTP_PASS_WORD
}

SITE_INFO = {
    'SITE_URL': 'xxxxx',            # Your site address
    'SITE_NAME': 'XXXXXXXXXXX',     # Your site name
    'ADMIN_MAIL': 'XXXXXXXXXXXXX',  # Your admin mail address you received an email when your blog have new comment
    'ADMIN_NAME': 'XXXXXX',         # Your Blog name
}

# python3 manage.py makemigrations user
# python3 manage.py makemigrations comment
# python3 manage.py makemigrations
# python3 manage.py migrate user
# python3 manage.py migrate comment
# python3 manage.py migrate
# python3 manage.py createsuperuser
# python3 manage.py collectstatic
# python3 manage.py runserver 127.0.0.1:8080