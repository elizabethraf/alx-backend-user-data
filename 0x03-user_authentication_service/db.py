#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base

engine = create_engine('database_uri')
Session = sessionmaker(bind=engine)


class DB:
    """DB class
    """

    def __init__(self):
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(mail, hashed_password):
        """create a new session"""
        session = Session()

        user = User(email=email, hashed_password=hashed_password)

        session.add(user)
        sessiion.commit()

        return user

   def find_user_by(self, **kwargs) -> User:
        """Display a find_user_by"""
        if not kwargs or any(x not in VALID_FIELDS for x in kwargs):
            raise InvalidRequestError
        session = self._session
        try:
            return session.query(User).filter_by(**kwargs).one()
        except Exception:
            raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """Display an update_user"""
        session = self._session
        user = self.find_user_by(id=user_id)
        for a, b in kwargs.items():
            if a not in VALID_FIELDS:
                raise ValueError
            setattr(user, a, b)
        session.commit()

