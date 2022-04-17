from flask_restx import Resource, Namespace
from flask import request

from src.api.number.model import NumberModel

api = Namespace("number", description="Number related operations")

_model = NumberModel(api)


@api.route("")
class Number(Resource):
    @api.marshal_with(_model.response_model())
    @api.expect(_model.request_model())
    def post(self):
        request_data = request.get_json()
        number = request_data["number"]
        number2 = request_data["number2"]
        number3 = request_data["number3"]
        return {"result": _add_number(number, number2, number3)}


def _add_number(number, number2, number3) -> int:
    return number + number2 + number3
