aiohttp_cookauth
================
.. image:: https://img.shields.io/pypi/v/aiohttp-cookauth.svg
    :target: https://pypi.python.org/pypi/aiohttp-cookauth

The library is a fork of `aiohttp_session`__ and `aiohttp_security`__. The fork provides identity and authorization for `aiohttp.web`__ only via cookies using redis storage. `Added the ability to forget all user sessions`.

.. _aiohttp_web: http://aiohttp.readthedocs.org/en/latest/web.html

__ aiohttp_web_

.. _aiohttp_session: https://github.com/aio-libs/aiohttp-session

__ aiohttp_session_

.. _aiohttp_security: https://github.com/aio-libs/aiohttp-security

__ aiohttp_session_

Installation
------------
::

    $ pip install aiohttp_cookauth

Setup
--------
::

 from aiohttp import web
 from aioredis import create_redis_pool
 from aiohttp_cookauth import (
     setup as setup_cookauth, RedisStorage
 )
 from aiohttp_cookauth.abc import AbstractAuthorizationPolicy


 class SimpleAuthorizationPolicy(AbstractAuthorizationPolicy):
     async def authorized_userid(self, identity):
         """Retrieve authorized user id.
         Return the user_id of the user identified by the identity
         or 'None' if no user exists related to the identity.
         """
         if identity == 'jack':
             return identity

     async def permits(self, identity, permission, context=None):
         """Check user permissions.
         Return True if the identity is allowed the permission
         in the current context, else return False.
         """
         return identity == 'jack' and permission in ('listen',)


 app = web.Application()
 redis = await create_redis_pool(('localhost', 6379))
 storage = RedisStorage(redis, cookie_name='MY_SESSION', max_age=900)
 setup_cookauth(app, SimpleAuthorizationPolicy(), storage)

Documentation
-------------
Use aiohttp_security documentation:

https://aiohttp-security.readthedocs.io/


License
-------

``aiohttp_cookauth`` is offered under the Apache 2 license.
