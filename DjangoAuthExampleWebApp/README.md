# SimpleWebApp
Simple Full Stack Django Web Application With Auth

# First time setup
## Requirements
1.Docker installed ('brew install --cask docker')
2.Install postgres docker image
3.Create you own "authsite.env" file with SECRET_KEY, POSTGRES_PASSWORD, DB_HOST, TAG

[Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction)
```
make help
```

## Setup Admin
'python authsite/manage.py createsuperuser'
user:admin
email:admin@example.com
password:1
