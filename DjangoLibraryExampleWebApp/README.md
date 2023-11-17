# SimpleWebApp
Simple Full Stack Django Web Application to Build a Library Website

# First time setup
## Requirements
1.Docker installed ('brew install --cask docker')
2.Install postgres docker image
3.Create you own "libsite.env" file with SECRET_KEY, POSTGRES_PASSWORD, DB_HOST, TAG

[Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side)
```
make help
```

## Setup Admin
'python authsite/manage.py createsuperuser'
user:admin
email:admin@example.com
password:1
