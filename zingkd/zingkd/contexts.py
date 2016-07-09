from __future__ import absolute_import, unicode_literals
import logging

log = logging.getLogger(__name__)


class RootContext(object):
    """
    Base context which all others extend.

    :param request: HTTP request object.
    :type request: :class:`pyramid.request.Request`
    """

    def __init__(self, request):
        self._db = request.db
        self._request = request
        self._settings = request.registry.settings
