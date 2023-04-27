#!/usr/bin/env python3
"""Display  function called filter_datum"""
import re
import logging


def filter_datum(fields, redaction, message, separator):
    """Display filter"""
    pattern = '|'.join(map(re.escape, fields))
    return re.sub(pattern, redaction, message).rstrip(separator) + separator


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """display init"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Display format"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Display get logger"""

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Display get"""
    psw = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    username = os.environ.get('PERSONAL_DATA_DB_USERNAME', "root")
    host = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.environ.get('PERSONAL_DATA_DB_NAME')
    conn = mysql.connector.connect(
        host=host,
        database=db_name,
        user=username,
        password=psw)
    return conn


def main() -> None:
    """Display main"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        message = f"name={row[0]}; email={row[1]}; phone={row[2]}; " +\
            f"ssn={row[3]}; password={row[4]};ip={row[5]}; " +\
            f"last_login={row[6]}; user_agent={row[7]};"
        print(message)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
