from .abc import AbstractAuthorizationPolicy, AbstractIdentityPolicy
from .api import (authorized_userid, forget, has_permission,
                  is_anonymous, login_required, permits, remember,
                  setup_security, check_authorized, check_permission,
                  forget_all)
from .session_identity import SessionIdentityPolicy
from .session import Session, get_session, new_session, setup_session
from .storage import RedisStorage


__version__ = '0.1.0'


def setup(app, autz_policy, redis_pool):
    setup_security(app, SessionIdentityPolicy(), autz_policy)
    setup_session(app, redis_pool)


__all__ = ('AbstractIdentityPolicy', 'AbstractAuthorizationPolicy',
           'SessionIdentityPolicy', 'RedisStorage',
           'remember', 'forget', 'authorized_userid',
           'permits', 'setup', 'is_anonymous',
           'login_required', 'has_permission',
           'check_authorized', 'check_permission',
           'Session', 'get_session', 'new_session', 'forget_all')
