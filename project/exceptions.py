class ItemNotFound(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class NoUserFound(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class UserAlreadyExists(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class IncorrectPassword(Exception):
    def __init__(self, message=None):
        super().__init__(message)
