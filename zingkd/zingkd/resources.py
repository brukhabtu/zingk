from cornice.resource import resource, view

_USERS = {1: {'name': 'gawel'}, 2: {'name': 'tarek'}}


@resource(collection_path='/users', path='/users/{id}')
class User(object):

    def __init__(self, request):
        self.request = request

    def collection_get(self):
        return {'users': _USERS.keys()}

    @view(renderer='json')
    def get(self):
        return _USERS.get(int(self.request.matchdict['id']))

    @view(renderer='json', accept='text/json')
    def collection_post(self):
        print(self.request.json_body)
        _USERS[len(_USERS) + 1] = self.request.json_body
        return True
