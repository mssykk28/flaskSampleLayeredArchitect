from copy import deepcopy

from src.utils.custom_fields import Boolean, DateTime, Integer, String


class ExampleSchema:
    def __init__(self, api):  # noqa: ANN001
        self.api = api

    id = Integer(
        title="id",
        description="id",
        required=False,
        example=1,
        min=1,
        max=4294967295,
        readonly=True,
    )

    example_string = String(
        title="example_string",
        description="文字列サンプル",
        required=True,
        example="文字列サンプル",
        min_length=1,
        max_length=128,
        nullable=False,
    )

    example_number = Integer(
        title="example_number",
        description="数値サンプル",
        required=True,
        example=123,
        min=1,
        max=4294967295,
        nullable=True,
    )

    example_datetime = DateTime(
        title="example_datetime",
        description="日時サンプル",
        required=True,
        example="2022-03-01T08:09:10",
        nullable=True,
    )

    example_boolean = Boolean(
        title="example_boolean",
        description="真偽値サンプル",
        required=True,
        example=False,
        nullable=True,
    )

    def example_get_response_model(self) -> dict:
        return self.api.model(
            "ExampleGetResponse",
            {
                "id": self.id,
                "example_string": self.example_string,
                "example_number": self.example_number,
                "example_datetime": self.example_datetime,
                "example_boolean": self.example_boolean,
            },
        )

    def example_post_request_model(self) -> dict:
        return self.api.model(
            "ExamplePostRequest",
            {
                "example_string": self.example_string,
                "example_number": self.example_number,
                "example_datetime": self.example_datetime,
                "example_boolean": self.example_boolean,
            },
        )

    def example_put_request_model(self) -> dict:
        return self.api.model(
            "ExamplePutRequest",
            {
                "example_string": self.example_string,
                "example_number": self.example_number,
                "example_datetime": self.example_datetime,
                "example_boolean": self.example_boolean,
            },
        )

    def example_patch_request_model(self) -> dict:
        _example_string = deepcopy(self.example_string)
        _example_string.required = False

        _example_number = deepcopy(self.example_number)
        _example_number.required = False

        _example_datetime = deepcopy(self.example_datetime)
        _example_datetime.required = False

        _example_boolean = deepcopy(self.example_boolean)
        _example_boolean.required = False

        return self.api.model(
            "ExamplePatchRequest",
            {
                "example_string": _example_string,
                "example_number": _example_number,
                "example_datetime": _example_datetime,
                "example_boolean": _example_boolean,
            },
        )
