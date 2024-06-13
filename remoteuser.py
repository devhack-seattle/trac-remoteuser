from trac.core import *
from trac.config import Option
from trac.web.api import IRequestFilter

import sys

class RemoteUserAuthenticator(Component):
    implements(IRequestFilter)

    remote_user_header = Option('trac', 'remote_user_header', 'remote-user',
               """What header should be read from for auth""")

    def pre_process_request(self, req, handler):
        if self.remote_user_header:
            req.environ['REMOTE_USER'] = req.get_header(self.remote_user_header)
        return handler

    def post_process_request(self, req, template, data, metadata):
        return template, data
