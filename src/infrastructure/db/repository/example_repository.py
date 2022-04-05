from typing import List, NoReturn

from src.infrastructure.db.entity.example import Example
from src.utils.dict import to_dict


def find_all(db_session) -> List[Example]:
    return db_session.query(Example).all()


def create(db_session, payload) -> Example:
    example = Example(
        example_string=payload.example_string,
        example_number=payload.example_number,
        example_datetime=payload.example_datetime,
        example_boolean=payload.example_boolean,
    )
    db_session.add(example)
    db_session.commit()
    return example


def find_by_id(db_session, example_id) -> Example:
    return db_session.query(Example).filter(Example.id == example_id).one_or_none()


def update(db_session, example_id, example) -> NoReturn:
    db_session.query(Example).filter(Example.id == example_id).update(to_dict(example))
    db_session.commit()


def delete(db_session, example_id) -> NoReturn:
    db_session.query(Example).filter(Example.id == example_id).delete()
