# SimpleWebApp
Simple Full Stack Django Web Application For User

# First time setup
## Requirements
1.Docker installed ('brew install --cask docker')
2.Install postgres docker image
3.Create you own "usersite.env" file with SECRET_KEY, POSTGRES_PASSWORD, DB_HOST, TAG

[Tutorial](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=2)
```
make help
```

## Setup Admin
'python usersite/manage.py createsuperuser'
user:admin
email:admin@example.com
password:1
