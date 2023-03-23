from typing import List

from flask import Flask, request

from database_credential import DATABASE_CREDENTIAL
from db_connection import ConnectDB
from sql import get_price_sql, get_code_from_region_slug_sql
from utils import get_context_data

app = Flask(__name__)

connection = ConnectDB(**DATABASE_CREDENTIAL)

CODE_LENGTH = 5


@app.route('/rates', methods=['GET'])
def get_rate() -> List[dict]:
    """
    get daily average price
    :exception:
    origin: ex:CNSGH
    destination: ex:north_europe_main
    date_to: ex:2016-01-01
    date_from: ex:2016-01-30
    :return: list of dictionary data
    :url: [host address]/rates?date_from=2016-01-01&date_to=2016-01-30&origin=CNSGH&destination=north_europe_main
    """
    result_list = []
    origin_code, destination_code, date_to, date_from = get_context_data()

    if not all([origin_code, destination_code, date_to, date_from]):
        return [{'error': "Parameter missing: origin/destination/date_to/date_from"}]

    if len(origin_code) > CODE_LENGTH:
        origin_code = connection.get_object(get_code_from_region_slug_sql.format(region_slug=origin_code))
        if not origin_code:
            return [{'error': 'Origin code not found'}]
    if len(destination_code) > CODE_LENGTH:
        destination_code = connection.get_object(get_code_from_region_slug_sql.format(region_slug=destination_code))
        if not destination_code:
            return [{'error': 'Destination code not found'}]

    price_query = get_price_sql.format(origin=origin_code, destination_code=destination_code, date_from=date_from,
                                       date_to=date_to)
    data_list = connection.get_object_list(query=price_query)

    if not data_list:
        return [{'error': "No data available"}]
    for data in data_list:
        day_price_dict = {}
        day, avg_price, count = data
        day_price_dict['day'] = str(day)
        day_price_dict['average_price'] = int(avg_price) if count >= 3 else None
        result_list.append(day_price_dict)
    return result_list


if __name__ == '__main__':
    app.run()
