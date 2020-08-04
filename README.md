# test-deploy
**Example Django project for testing deployment in Heroku.**

This project only display a home page.

Users could be created via admin site.


### To run project
Package **django-dotenv** is used, then, in local environment a file `.env` must exists in `test_deploy` directory (where `setting.py` file is placed).
This `.env` file should contains DEBUG and SECRET_KEY definitions. In Heroku, those keys are defined in settings.

To generate a secret key, execute: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`


### Notes:
- The `main` app uses a non-recommended structure for templates, it's just for example; recommended way is used in `accounts` app.
- Used Python version: 3.7.7
