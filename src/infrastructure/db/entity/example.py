from sqlalchemy.dialects.mysql import BOOLEAN, DATETIME, INTEGER, VARCHAR
from sqlalchemy.schema import Column

from src.infrastructure import Base


class Example(Base):
    __tablename__ = "example"

    id = Column(INTEGER, primary_key=True)
    example_string = Column(VARCHAR, nullable=False)
    example_number = Column(INTEGER, nullable=True)
    example_datetime = Column(DATETIME, nullable=True)
    example_boolean = Column(BOOLEAN, nullable=True)
