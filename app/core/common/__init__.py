"""
app.core.common module
"""
def not_implemented_error(method_name: str):
    """

    :param method_name:
    """
    return NotImplementedError(f"Error! {method_name} not implemented.")
