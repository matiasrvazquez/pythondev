# Example of entrypoint for an application using our brand new Python module
import collections
import os
from typing import Any, List

import pandas


def main(x: int, y: str, z: Any) -> List:
    """This is a test function

    Args:
        x (int): _description_
        y (str): _description_
        z (Any): _description_

    Returns:
        List: _description_
    """
    return x + y


main(1, 2, 3)
