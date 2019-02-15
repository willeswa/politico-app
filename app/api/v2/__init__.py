""" Creates blueprints and registers routes for version 2 """

# Thirdy party
from flask import Blueprint

# Local imports
from app.api.v2.views.user_views import SignupViews, LoginViews

# Create blueprint
V2 = Blueprint('version2', __name__, url_prefix='/api/v2')

def define_routes(view, endpoint, url, identifier='id', identifier_type='int'):
    """ Creates an api endpoint and assigns route"""
    
    view_func = view.as_view(endpoint)
    V2.add_url_rule(url, view_func=view_func,
                    defaults={identifier: None}, methods=['GET', ])
    V2.add_url_rule(url, view_func=view_func, methods=['POST', ])
    V2.add_url_rule('%s/<%s:%s>' % (url, identifier_type, identifier),
                    view_func=view_func, methods=['GET'])
    V2.add_url_rule('%s/<%s:%s>/name' % (url, identifier_type, identifier),
                    view_func=view_func, methods=['PUT'])
    V2.add_url_rule('%s/<%s:%s>' % (url, identifier_type,
                                    identifier), view_func=view_func, methods=['DELETE'])


define_routes(SignupViews, 'signup', '/auth/signup', identifier='user_id')
define_routes(LoginViews, 'login', '/auth/signin', identifier='user_id')