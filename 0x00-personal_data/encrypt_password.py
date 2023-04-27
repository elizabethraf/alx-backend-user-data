#!/usr/bin/env python3
"""Display  Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Display password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Display is valid"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

