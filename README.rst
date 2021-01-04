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

Example
--------
::

 from aiohttp import web
 from aioredis import create_redis_pool
 from aiohttp_cookauth import check_permission, \
     is_anonymous, remember, forget, \
     setup as setup_cookauth, RedisStorage, forget_all
 from aiohttp_cookauth.abc import AbstractAuthorizationPolicy


 # Demo authorization policy for only one user.
 # User 'jack' has only 'listen' permission.
 class SimpleJack_AuthorizationPolicy(AbstractAuthorizationPolicy):
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


 async def handler_root(request):
     is_logged = not await is_anonymous(request)
     return web.Response(text='''<html><head></head><body>
             Hello, I'm Jack, I'm {logged} logged in.<br /><br />
             <a href="/login">Log me in</a><br />
             <a href="/logout">Log me out</a><br />
             <a href="/logout/all">Log out for all</a><br /><br />
             Check my permissions,
             when i'm logged in and logged out.<br />
             <a href="/listen">Can I listen?</a><br />
             <a href="/speak">Can I speak?</a><br />
         </body></html>'''.format(
             logged='' if is_logged else 'NOT',
         ), content_type='text/html')


 async def handler_login_jack(request):
     redirect_response = web.HTTPFound('/')
     await remember(request, redirect_response, 'jack')
     return redirect_response


 async def handler_logout(request):
     redirect_response = web.HTTPFound('/')
     await forget(request, redirect_response)
     return redirect_response


 async def handler_logout_all(request):
     redirect_response = web.HTTPFound('/')
     await forget_all(request, identity='jack')
     return redirect_response


 async def handler_listen(request):
     await check_permission(request, 'listen')
     return web.Response(body="I can listen!")


 async def handler_speak(request):
     await check_permission(request, 'speak')
     return web.Response(body="I can speak!")


 async def make_app():
     # make app
     app = web.Application()

     # add the routes
     app.add_routes([
         web.get('/', handler_root),
         web.get('/login', handler_login_jack),
         web.get('/logout', handler_logout),
         web.get('/logout/all', handler_logout_all),
         web.get('/listen', handler_listen),
         web.get('/speak', handler_speak)])

     # set up policies
     redis = await create_redis_pool(('localhost', 6379))
     storage = RedisStorage(redis, cookie_name='MY_SESSION', max_age=900)
     setup_cookauth(app, SimpleJack_AuthorizationPolicy(), storage)

     return app


 if __name__ == '__main__':
     web.run_app(make_app(), port=9000)

Documentation
-------------
Use aiohttp_security documentation:

https://aiohttp-security.readthedocs.io/


License
-------

``aiohttp_cookauth`` is offered under the Apache 2 license.
