from logging import getLogger

from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm import Session

from app.shema.models import BaseModel

log = getLogger()


class DBSession:

    _session: Session

    def __init__(self, session: Session) -> None:
        self._session = session

    def query(self, *entities, **kwargs):
        return self._session.query(*entities, **kwargs)

    def add_model(self, model: BaseModel, need_flush: bool = False) -> None:
        self._session.add(model)

        if need_flush:
            self._session.flush([model])

    def delete_model(self, model: BaseModel) -> None:
        if model is None:
            log.warning('%s: model is None', __name__)

        try:
            self._session.delete(model)
        except IntegrityError as e:
            log.error('`%s` %s', __name__, e)
        except DataError as e:
            log.error('`%s` %s', __name__, e)

    def commit_session(self, need_close: bool = False) -> None:
        try:
            self._session.commit()
        except IntegrityError as e:
            log.error('`%s` %s', __name__, e)
            raise
        except DataError as e:
            log.error('`%s` %s', __name__, e)
            raise

        if need_close:
            self.close_session()

    def close_session(self) -> None:
        try:
            self._session.close()
        except IntegrityError as e:
            log.error('`%s` %s', __name__, e)
            raise
        except DataError as e:
            log.error('`%s` %s', __name__, e)
            raise
