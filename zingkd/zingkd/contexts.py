from __future__ import absolute_import, unicode_literals
import logging

log = logging.getLogger(__name__)


_NOTES = {
    1: {'note_id': 1,
        'title': 'Foo Note',
        'created_date': '2016-01-01',
        'modified_date': '2016-01-02',
        'colour': '#CCCCCC',
        'archived': False,
        'content': 'Random content in note'},
    2: {'note_id': 2,
        'title': 'Bar Note',
        'created_date': '2016-04-01',
        'modified_date': '2016-04-02',
        'colour': '#DDDDDD',
        'archived': True,
        'content': 'Random content in note'}
}


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
        self.note_id = request.matchdict.get('note_id')

    def get_notes(self):
        # Note that python3's dict.values method returns a view type which is not json serializable.
        return list(_NOTES.values())

    def get_note(self):
        return _NOTES[int(self.note_id)]
