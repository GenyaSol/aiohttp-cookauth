from .session import get_session, delete_all_sessions, Session

from .abc import AbstractIdentityPolicy


class SessionIdentityPolicy(AbstractIdentityPolicy):

    def __init__(self, session_key='AIOHTTP_SECURITY'):
        self._session_key = session_key
        self._identity_key = 'AIOHTTP_SESSION_IDENTITY'

    async def identify(self, request):
        session = await get_session(request)
        return session.get(self._session_key)

    async def remember(self, request, response, identity, **kwargs):
        session = await get_session(request)
        request[self._identity_key] = identity
        session[self._session_key] = identity

    async def forget(self, request, response):
        session = await get_session(request)
        session.pop(self._session_key, None)

    async def forget_all(self, request, identity):
        session_or_identity = await delete_all_sessions(request, identity)
        if isinstance(session_or_identity, Session):
            session_or_identity.pop(self._session_key, None)
