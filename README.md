# SW API GraphQL

## Starting:rocket:
These instructions will allow you to get a copy of the project running on your local machine for development and testing purposes.


## Requirements:blue_book:
* [Python](https://www.python.org/) (realizado en python 3.8)
* [Django](https://github.com/django/django)
* [Django Filter](https://github.com/carltongibson/django-filter)
* [Django model utils](https://github.com/jazzband/django-model-utils)
* [Graphene](https://github.com/graphql-python/graphene-django)
* [.EVN](https://github.com/theskumar/python-dotenv)

## Setup:wrench:

Clone the project
```
git clone https://github.com/jhondil/backend-test
```

Creating Virtual Environments
```
python3 -m venv tutorial-env
```

## Once you’ve created a virtual environment, you may activate it.
On Windows, run:
```
tutorial-env\Scripts\activate.bat
```
On Unix or MacOS, run:
```
source tutorial-env/bin/activate
```
------------

> The project is in 'deployment' mode, it must be passed to 'development'

------------

## Deployment to development:steam_locomotive:
###### Move into de repo


- Locate us in the following file swap / settings.py
```
		- DEBUG = True  switch to  DEBUG = False
```
- uncomment lines 67 to 72
```
		DATABASES = {
		     'default': {
		         'ENGINE': 'django.db.backends.sqlite3',
		          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		      }
		 }
```
- comment lines 74 to 
```
		# DATABASES = {
		#     'default': dj_database_url.config(
		#             default=config('DATABASE_URL')
		#         )
		# }
		
```



Move into de repo and install dependencies

```
pip install -r requirements.txt
```


Run migrations and load fixtures
```
python manage.py migrate
python manage.py load_fixtures
```


Run migrations and load fixtures
```
python manage.py migrate
python manage.py load_fixtures
```

### Running the server:eyes:
```
python manage.py runserver
```
If you want to check it out, access the graphi explorer here: `127.0.0.1:8000/explore`.

The service should be available in the URL: `127.0.0.1:8000/graphql`.

### Runing the tests
```
pytest
```
# Accessing the project in heroku:heavy_check_mark:
Deploy application [app-swapi](https://app-swapi-b.herokuapp.com/explore/)
### Accessing the project in heroku admin
Application admin [app-swapi](https://app-swapi-b.herokuapp.com/admin)
##### User: Admin
##### Password: Admin

### Collection in Postman
```
 file swapi-back.postman_collection.json
```

## Built with :nut_and_bolt:
- [Python](https://www.python.org/ "Python")
- [Django](https://www.djangoproject.com/ "Django")
- [GraphQl](https://graphql.org/ "GraphQl")

## Authors:bust_in_silhouette:
- [ Jhonatan Ibarra ](https://github.com/jhondil/ " Jhonatan Ibarra ")- New implementations
- [ LQN ](https://github.com/LQNTech/)  - Initial project










