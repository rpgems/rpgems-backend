class DatabaseError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class DatabaseNotFoundError(DatabaseError):
    def __init__(self, table_name: str, details: str):
        message = f"Item not found on table {table_name}. \n\n Details: {details}"
        super().__init__(message)
