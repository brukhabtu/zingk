from cornice.resource import resource, view


@resource(collection_path='/notes', path='/notes/{note_id}')
class NotesResource(object):

    def __init__(self, request):
        self._request = request
        self._context = request.context

    def collection_get(self):
        return self._context.get_notes()

    @view(renderer='json', accept='text/json')
    def collection_post(self):
        return self.get_notes()

    @view(renderer='json')
    def get(self):
        return self._context.get_note()
