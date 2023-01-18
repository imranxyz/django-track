![Language](https://img.shields.io/badge/Python-v3.10-important)&nbsp;
![Django](https://img.shields.io/badge/Django-v4.1-important)&nbsp;
![Update](https://img.shields.io/badge/Last%20Update-January%2018,%202023-brightgreen)&nbsp;

- Pipenv Doc — https://pipenv-fork.readthedocs.io/
- Pipenv: The Future of Python Dependency Management — https://www.youtube.com/watch?v=GBQAKldqgZs

## Installation via Virtualenv

- Go to the directory and type `pip install pipenv`
- After installed successfully type `pipenv install` (create virtualenv)
- For activate virtualenv type `pipenv shell`
- Install django type `pipenv install django` | `pip install django==x.x.x`
- type `pipenv --venv` to check is there any venv for this current project & if satisfied it will show location else return no venv has been created
- Exit virtual env type `exit` or `CTRL + d` & terminal back to normal prompt
- Create Django project `django-admin startproject "NameOfProject" .`
- Create django app `python manage.py startapp "NameofApp"`
- Migration command `python manage.py makemigrations` then `python manage.py migrate`
- Remove venv `pipenv --rm`.. It will be deleted virtualenv for this current project
- Create requirements.txt file --> `pip freeze > requirements.txt`
- Install all dependencis after clone -> `pip install` -> `pipenv install -r requirements.txt`
- Check Django version `python -m django --version`

## Tips & Tricks/Cheatsheet

- [Classy Class-Based Views](https://ccbv.co.uk/)
- [Classy Django REST Framework](https://www.cdrf.co/)
- [Classy Django Forms](https://cdf.9vo.lt/)
- [adamghill/django-fbv](https://github.com/adamghill/django-fbv)

## Commonly Used Apps

- [model_bakery](https://github.com/model-bakers/model_bakery)
- [factory-boy](https://github.com/FactoryBoy/factory_boy) `fetching fake data`
- [django-braces](https://github.com/brack3t/django-braces) `classed based view`
- [djang-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) `awesome`
- [django-guardian](https://github.com/django-guardian/django-guardian)
- [django-jimmypage](https://github.com/yourcelf/django-jimmypage) `caching`
- [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django)
- [pytest](https://github.com/pytest-dev/pytest)
- [coveragepy](https://github.com/nedbat/coveragepy)
