the_millionaire
===============

Who Wants to Be a Millionaire?

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

:License: MIT


Basic Commands
--------------

To Start Development Server
^^^^^^^^^^^^^^^^^^^^^
* To start the development server you will need `docker` and `docker-compose`::

    $ docker-compose -f local.yml up


Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* In order to create a superuser account you need to get a shell from django container.

* To do so, run the following commands::

    $ docker exec -it django bash
    $ python manage.py createsuperuser


