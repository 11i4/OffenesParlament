# OffenesParlament

An open-data framework for the public data of the Austrian Parliament

## Quick-And-Dirty installation instructions

Follow these instructions (updates pending!) to set up the project as is.

1. Clone the github repository (duh)
2. Install python [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) (if you don't have it yet):

 ```
 pip install virtualenv
 pip install virtualenvwrapper
 ```
 Depending on your operating system, you might have to do some additional setup as explained [here](https://virtualenvwrapper.readthedocs.org/en/latest/#introduction).
3. Create a new python virtualenv for your project:

 ```
 mkvirtualenv openparliament
 ```
 If all went well, your shell should have activated the environment already.
4. Install the projects dependencies:

 ```
 pip install -r requirements.txt
 ```
5. Have django create the DB-models:

 ```
 cd offenesparlament
 python manage.py makemigrations
 python manage.py migrate
 ```

6. Create a superuser to log in to the backend with

 ```
 python manage.py createsuperuser
 ```

7. Try it out!

 ```
 python manage.py runserver
 ```

  Navigate to the [Django Admin Tool](http://127.0.0.1:8000/admin/) and check out your sweet, sweet models!

And you're done!

## Resetting the database

In case you need to reset the database (delete all migrations, flush the db content, recreate all objects etc.), run these commands in the django project folder 'offenesparlament':

```
python remove_migrations.py && rm db.sqlite3 && python manage.py makemigrations && python manage.py migrate
```

## Initial scraping

The current scraper for the laws and initiatives pages (for instance, [ÖBIB-Gesetz 2015 (458 d.B.)](http://www.parlament.gv.at/PAKT/VHG/XXV/I/I_00458/index.shtml)) of the Austrian Parliament can be run by doing this:

```
python manage.py scrape crawl laws_initiatives
```

The current scraper for Persons (including Parties, their mandates and functions and bio-data), for instance [Rudolf Anschober](http://www.parlament.gv.at/WWER/PAD_00024/index.shtml) can be run by doing this:

```
python manage.py scrape crawl persons
```
