from flask_restful import Resource, reqparse

from quipit.db import db
from quipit.models import Quip, Circle
from quipit.middleware import authenticate


class AuthenticatedResource(Resource):
    method_decorators = [authenticate]


class QuipsResource(AuthenticatedResource):
    def get(self, user):
        return {'quips': user.quips.all()}

    def post(self, user):
        parser = reqparse.RequestParser()
        parser.add_argument('text', required=True)
        parser.add_argument('circle', dest='circle_ids', action='append', type=int)
        args = parser.parse_args()

        text = args['text']
        circle_ids = args['circle_ids']

        quip = Quip(text, user)
        if circle_ids:
            circles = user.circles.filter(Circle.id.in_(circle_ids)).all()
            for circle in circles:
                quip.add_to_circle(circle)

        db.session.add(quip)
        db.session.commit()

        return {'thangs': True}
