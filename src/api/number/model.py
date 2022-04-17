from flask_restx import fields


class NumberModel:
    def __init__(self, api):
        self.api = api

    def request_model(self):
        return self.api.model("numberRequestModel", {
            "number": fields.Integer(required=True, description="Number to be converted"),
            "number2": fields.Integer(required=True, description="Number to be converted"),
            "number3": fields.Integer(required=True, description="Number to be converted"),
        })

    def response_model(self):
        return self.api.model("numberResponseModel", {
            "result": fields.Integer(required=True, description="Result of the operation"),
        })
