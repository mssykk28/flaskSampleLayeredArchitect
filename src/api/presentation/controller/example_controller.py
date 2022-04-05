from typing import NoReturn

from flask_restx import Namespace, Resource, abort

from src.api.application.dto.example_dto import ExampleDTO
from src.api.application.service import example_service
from src.api.presentation.schema.example_schema import ExampleSchema

api = Namespace("examples", description="サンプル")

_example_schema = ExampleSchema(api)


@api.route("")
class Examples(Resource):
    @api.doc(description="取得APIサンプル")
    @api.marshal_list_with(_example_schema.example_get_response_model())
    def get(self):  # noqa: ANN201
        """取得APIサンプル"""
        return example_service.find_all()

    @api.doc(description="登録APIサンプル")
    @api.expect(_example_schema.example_post_request_model())
    @api.response(201, "登録成功")
    def post(self):  # noqa: ANN201
        """登録APIサンプル"""
        example_service.create(ExampleDTO(**api.payload))
        return "登録成功", 201


@api.route("/<int:example_id>")
class Example(Resource):
    @api.doc(description="詳細取得APIサンプル")
    @api.marshal_with(_example_schema.example_get_response_model())
    def get(self, example_id: int):  # noqa: ANN201
        """詳細取得APIサンプル"""
        _validation(example_id)
        return example_service.find_by_id(example_id)

    @api.doc(description="更新APIサンプル")
    @api.expect(_example_schema.example_put_request_model(), validate=True)
    @api.response(204, "更新成功")
    def put(self, example_id: int):  # noqa: ANN201
        """更新APIサンプル"""
        _validation(example_id)
        example_service.update(example_id, ExampleDTO(**api.payload))
        return "更新成功", 204

    @api.doc(description="更新APIサンプル")
    @api.expect(_example_schema.example_patch_request_model(), validate=True)
    @api.response(204, "更新成功")
    def patch(self, example_id: int):  # noqa: ANN201
        """更新APIサンプル"""
        _validation(example_id)
        example_service.update(example_id, ExampleDTO(**api.payload))
        return "更新成功", 204

    @api.doc(description="削除APIサンプル")
    @api.response(204, "削除成功")
    def delete(self, example_id: int):  # noqa: ANN201
        """削除APIサンプル"""
        _validation(example_id)
        example_service.delete(example_id)
        return "削除成功", 204


def _validation(example_id: int) -> NoReturn:
    example = example_service.find_by_id(example_id)
    if not example:
        abort(404, f"Example {example_id} not found")
