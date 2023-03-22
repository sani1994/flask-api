from dataclasses import dataclass
from typing import Union, List

import psycopg2

from custome_decorators import handle_connection_error_exceptions


@dataclass
class ConnectDB:
    host: str
    database: str
    user: str
    password: str
    port: str = None

    def __post_init__(self):
        self.connection = self.create_connection()

    @handle_connection_error_exceptions
    def create_connection(self) -> psycopg2.connect:
        """
        create db connection
        :return: db connection cursor
        """
        return psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)

    @handle_connection_error_exceptions
    def get_object(self, query: str) -> Union[str, int, float]:
        """
        to fetch a single object from database by using fetchone
        :param query: valid sql query string
        :return: single data
        """
        _cursor = self.connection.cursor()
        _cursor.execute(query)
        _data = _cursor.fetchone()
        _cursor.close()
        return _data[0] if _data else None

    @handle_connection_error_exceptions
    def get_object_list(self, query: str) -> List[Union[str, int, float]]:
        """
        to fetch data list from database by using fetchall
        :param query: valid sql query string
        :return: list of data
        """
        _cursor = self.connection.cursor()
        _cursor.execute(query)
        _data = _cursor.fetchall()
        _cursor.close()
        return _data
