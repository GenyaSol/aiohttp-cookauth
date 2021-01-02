from .abc import AbstractAuthorizationPolicy, AbstractIdentityPolicy
from .api import (authorized_userid, forget, has_permission,
                  is_anonymous, login_required, permits, remember,
                  setup_security, check_authorized, check_permission,
                  forget_all)
from .session_identity import SessionIdentityPolicy
from .session import Session, get_session, new_session, setup_session
from .storage import RedisStorage


def setup(app, identity_policy, autz_policy, storage):
    setup_security(app, identity_policy, autz_policy)
    setup_session(app, storage)


__all__ = ('AbstractIdentityPolicy', 'AbstractAuthorizationPolicy',
           'SessionIdentityPolicy', 'RedisStorage',
           'remember', 'forget', 'authorized_userid',
           'permits', 'setup', 'is_anonymous',
           'login_required', 'has_permission',
           'check_authorized', 'check_permission',
           'Session', 'get_session', 'new_session', 'forget_all')
