## How to setup the project

- make virtual env using ```python -m venv venv```
- activate virtual env
  - Linux ```source venv/bin/activate```
  - Windows ```./venv/scripts/activate```
- Install necessary packages ```pip install -r requirements.txt``` 

- make ```.env``` file
- copy ```.env.example``` to ```.env``` file
- change your database name and password in the .env file
- migrate database ```python manage.py migrate```

- run the app ```python manage.py runserver```


This is a test to for Github Desktop pushing changes