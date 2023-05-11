#!/usr/bin/env python3
"""Display DB.find_user_by method"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

engine = create_engine('database_uri')
Session = sessionmaker(bind=engine)

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
