from contextlib import contextmanager

from serasa_challenge.db.base import session


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def get_batch_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
