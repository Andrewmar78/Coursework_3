class ItemNotFound(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class NoUserFound(Exception):
    def __init__(self, message=None):
        super().__init__(message)
