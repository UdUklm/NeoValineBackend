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

# In this case you should add you domain in the list for use your api
# 可以使用该api的域名白名单列表 (example https://example.com https://www.example.com)
# 需要加https 或者http
# 最后需要以逗号结尾,不然会报错
DOMAIN_WHITE_LIST = (
    'http://127.0.0.1:4000',
    'http://localhost:4000',
    'http://127.0.0.1:8000',
)

# 受信任域名列表不需要加https 或者http
# 最后需要以逗号结尾,不然会报错
TRUSTED_ORGINS = (
    'localhost',
)

# 如果出现api访问错误请把debug模式打开
DEBUG_CONTROL = False

# python3 manage.py makemigrations user
# python3 manage.py makemigrations comment
# python3 manage.py makemigrations
# python3 manage.py migrate user
# python3 manage.py migrate comment
# python3 manage.py migrate
# python3 manage.py createsuperuser
# python3 manage.py collectstatic
# python3 manage.py runserver 127.0.0.1:8080