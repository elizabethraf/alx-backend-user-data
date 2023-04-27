#!/usr/bin/env python3
"""Display  function called filter_datum"""
import re


def filter_datum(fields, redaction, message, separator):
    """Display filter_datum"""
    pattern = re.compile(separator.join(f'({field}=.+?)' for field in fields))
    return pattern.sub(f'{redaction}', message)
