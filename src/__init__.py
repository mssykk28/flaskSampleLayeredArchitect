from flask import Blueprint
from flask_restx import Api

from src.api.presentation.controller.example_controller import api as examples_api

blueprint = Blueprint("api", __name__)

api = Api(
    app=blueprint,
    doc="/",
    version="0.0.1",
    title="API Title",
    description="API Description",
    validate=True,
    ordered=False,
)


api.namespaces.clear()
api.add_namespace(examples_api)
