from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ExampleDTO(BaseModel):
    id: Optional[int]
    example_string: str
    example_number: Optional[int]
    example_datetime: Optional[datetime]
    example_boolean: Optional[bool]
