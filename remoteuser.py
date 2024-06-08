from trac.core import *
from trac.config import Option
from trac.web.api import IAuthenticator

import sys

class RemoteUserAuthenticator(Component):
    implements(IAuthenticator)

    remote_user_header = Option('trac', 'remote_user_header', 'remote-user',
               """What header should be read from for auth""")

    def authenticate(self, req):
        if self.remote_user_header:
            return req.get_header(self.remote_user_header)
        return None
