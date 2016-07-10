"""Main entry point
"""
from pyramid.config import Configurator

from zingkd.contexts import RootContext
from zingkd.models.meta import create_database_session


def main(global_config, **settings):
    config = Configurator(
        settings=settings,
        root_factory=RootContext)

    config.add_request_method(_get_db, 'db', reify=True)

    config.include("cornice")
    config.scan("zingkd.resources")
    config.scan(ignore='zinkgd.tests')
    return config.make_wsgi_app()


def _get_db(request):
    """
    Retrieve the database session instance from the registry object found on
    the request or create it.

    :param request: Request object.
    :type request: :class:`pyramid.request.Request`
    :return: SQLAlchemy database session.
    :rtype: :class:`sqlalchemy.orm.session.Session`
    """
    registry = request.registry
    try:
        db = registry.db
    except AttributeError:
        db = registry.db = create_database_session(registry.settings)

    return db
