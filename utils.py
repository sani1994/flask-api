from flask import request


def get_context_data() -> tuple:
    """
    get context data from parameter
    :return: tuple of context data
    """
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    date_to = request.args.get('date_to')
    date_from = request.args.get('date_from')
    return origin, destination, date_to, date_from
