# Django + Celery (and Docker)

- forked from: [GitHub - testdrivenio/django-celery: Example of how to handle background processes with Django, Celery, and Docker](https://github.com/testdrivenio/django-celery)

- see Tutorial [testdriven.io: Asynchronous Tasks with Django and Celery](https://testdriven.io/blog/django-and-celery/)

I have added some notes, comments and code to better describe its working.

## Global Iterpreter Lock: Python is basically a single thread language (apart from IO)

The Python interpreter can only execute one thread at a time making it essentially a single threaded language with the only exception of when it's waiting for an IO operation. The mechanism at the heart of this limitation is called GIL that stands for Global Interpreter Lock. You can find a good explanation of GIL here: [What Is the Python Global Interpreter Lock (GIL)? – Real Python](https://realpython.com/python-gil/).

## An external worker solution: Celery

In a typical **web server** you need to respond to multiple requests as soon as possible without waiting for the previous one to finish being served. Usually, being typically bounded only by network communications and database data retrieval (both IO operations), a normal python web application can be quite fast and responsive even with the single thread limitation, but, as soon as some heavy CPU work is involved the situation might change dramatically. Or maybe an API call activates a long task that is required to be executed outside of the main application while a response is returned back to the user.

[Celery](https://github.com/celery/celery) allows to externalize python tasks and executes them in a separate (but somewhat linked) environment (see [Celery User Guide](https://docs.celeryq.dev/en/stable/userguide/index.html)). It also supports input queue, persisting results, logging and has a nice web monitor application called [Flower](https://github.com/mher/flower).

## Docker

[Docker](https://www.docker.com/) is a virtualization engine that allows to separate the actual bare system from the one in which the application is executed. A virtual application is then called conteinerized. A conteinerized application will always be executed in the same configurable environment with a lot of additional benefits.

To run the application spin up the containers:

```sh
$ docker-compose up -d --build
```

Open your browser to http://localhost:1337 to view the app or to http://localhost:5555 to view the Flower dashboard.

Trigger a new task:

```sh
$ curl -F type=0 http://localhost:1337/tasks/
```

Check the status:

```sh
$ curl http://localhost:1337/tasks/<TASK_ID>/
```

## Bibliography

- [Asynchronous Tasks with Django and Celery | TestDriven.io](https://testdriven.io/blog/django-and-celery/)

- [Asynchronous Tasks With Django and Celery – Real Python](https://realpython.com/asynchronous-tasks-with-django-and-celery/)

- [Celery and Django and Docker: Oh My!](https://www.revsys.com/tidbits/celery-and-django-and-docker-oh-my/)

- [Threading Vs Celery in Django. In our Django projects we have a very… | by Radwan Hijazi | Medium](https://medium.com/@radwanhijazi/threading-vs-celery-in-django-56ae4f86438e)

- [First steps with Django — Celery 5.5.0rc4 documentation](https://docs.celeryq.dev/en/latest/django/first-steps-with-django.html)

- [Flower — Flower 2.0.0 documentation](https://flower.readthedocs.io/en/latest/index.html)
