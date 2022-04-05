from typing import List, NoReturn, Optional

from sqlalchemy.orm import Session

from src.api.application.dto.example_dto import ExampleDTO
from src.infrastructure.db.connection import db_connection
from src.infrastructure.db.entity.example import Example
from src.infrastructure.db.repository import example_repository


@db_connection()
def find_all(db_session: Session) -> List[ExampleDTO]:
    examples = example_repository.find_all(db_session)
    return [ExampleDTO(**example.dict()) for example in examples]


@db_connection()
def create(example_dto: ExampleDTO, db_session: Session) -> NoReturn:
    example_repository.create(db_session, Example(**example_dto.dict()))


@db_connection()
def find_by_id(example_id: int, db_session: Session) -> Optional[ExampleDTO]:
    example = example_repository.find_by_id(db_session, example_id)
    if not example:
        return None

    return ExampleDTO(**example.dict())


@db_connection()
def update(example_id: int, example_dto: ExampleDTO, db_session: Session) -> NoReturn:
    example_repository.update(db_session, example_id, Example(**example_dto.dict()))


@db_connection()
def delete(example_id: int, db_session: Session) -> NoReturn:
    example_repository.delete(db_session, example_id)
