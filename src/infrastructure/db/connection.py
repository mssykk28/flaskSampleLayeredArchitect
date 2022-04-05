from functools import wraps

from sqlalchemy.engine import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="mysql+pymysql",
    database="test_db",
    host="127.0.0.1",
    username="test",
    password="test",
    port="3306",
    query={"charset": "utf8"},
)

engine = create_engine(
    url=url,
    pool_size=10,
    max_overflow=100,
    pool_recycle=10,
    echo=True,
)


def _create_session():  # noqa
    return sessionmaker(bind=engine)()


def db_connection():  # noqa
    def decorator(func):  # noqa
        @wraps(func)  # noqa
        def wrapper(*args, **kwargs):  # noqa
            session = None
            try:
                session = _create_session()
                response = func(*args, **kwargs, db_session=session)
                session.commit()
                return response

            except Exception as e:
                if session:
                    session.rollback()
                raise e

            finally:
                if session:
                    session.close()

        return wrapper

    return decorator
