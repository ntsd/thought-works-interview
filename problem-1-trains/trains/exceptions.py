class NoSuchRouteException(KeyError):
    """Exception raised when no target to get route"""
    def __init__(self, message):
        self.message = message

class RouteNotPossibleException(Exception):
    """Exception raised when no route to destination"""
    def __init__(self, message):
        self.message = message
