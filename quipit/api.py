from flask_restful import Api

from quipit.resources import QuipsResource

api = Api()
api.add_resource(QuipsResource, '/quips')
