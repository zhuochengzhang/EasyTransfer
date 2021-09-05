# EasyTransfer

whenever there's a new model created or existing models being updated, run:
```shell
python manager.py makemigrations
python manager.py migrate
```

to start the program, run:
```
python manager.py runserver
```

to create a new app:
first, run: python manager.py startapp *[appname]*

then add the *[appname]* to the INSTALLED_APPS list
