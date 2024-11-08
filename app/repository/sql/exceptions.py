"""
app.adapters.repositories.exceptions module
"""
class DatabaseError(Exception):
    """
    Database exception class
    """
    def __init__(self, message: str):
        super().__init__(message)
