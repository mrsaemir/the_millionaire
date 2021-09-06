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


Some useful curl commands
^^^^^^^^^^^^^^^^^^^^^^^^^

* A postman collection exists in the source code.
* You can also use curl to test some functionalities.

* Create a user::

    $  curl -d '{"username":"user1", "password": "passsword", "name": "Name1"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/api/users/users/

* Get Token::

    $  curl -d '{"username":"user1", "password": "passsword"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/auth-token/


* Top Users::

    $  curl -H "Content-Type: application/json" -X GET http://127.0.0.1:8000/api/questions/top-users/


* Other apis are in postman
