workers = 2
errorlog = "./logs/mysite.gunicorn.error"
accesslog = "./logs/mysite.gunicorn.access"
loglevel = "debug"

# 127.0.0.1 means only accept request within container
bind = ["0.0.0.0:9001"]