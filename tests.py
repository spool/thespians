"""
>>> from django.test import Client
>>> from thespians.models import Person
>>> from django.contrib.auth.models import User

>>> c = Client()
>>> u = User(first_name="Nathan", last_name="Borror", email="nathan@borrorblows.com")
>>> u.save()
>>> p = Person.objects.create(slug='nathan-borror', user=u)

>>> r = c.get('/people/')
>>> r.status_code
200

>>> r = c.get('/people/nathan-borror/')
>>> r.status_code
200
"""
