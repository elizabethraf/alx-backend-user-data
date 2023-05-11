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

    def add_user(self, mail, str, hashed_password: str) -> User:
        """create a new session"""
        session = Session()

        user = User(email=email, hashed_password=hashed_password)

        session.add(user)
        session.commit()

        return user

   def find_user_by(**kwargs) -> User:
    """create a new session"""
    session = Session()

    try:
        user = session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound("No user found with the given criteria")

        session.close()
        return user
    except InvalidRequestError as i:
        session.close()
        raise i

   def update_user(self, user_id: int, **kwargs) -> None:
        """Returns: None"""
        user = self.find_user_by(id=user_id)

        column_names = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in column_names:
                raise ValueError

        for key, value in kwargs.items():
            setattr(user, key, value)

        self._session.commit()
