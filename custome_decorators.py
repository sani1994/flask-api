def handle_connection_error_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ConnectionError:
            raise ConnectionError

    return wrapper
