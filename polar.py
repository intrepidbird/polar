import math

def rectangular_to_polar(x: float, y: float) -> tuple:
    """
    Converts rectangular coordinates (x, y) to polar coordinates (r, theta).

    Parameters:
    - x: float
        The x-coordinate in rectangular coordinates.
    - y: float
        The y-coordinate in rectangular coordinates.

    Returns:
    - tuple:
        A tuple containing the polar coordinates (r, theta), where:
        - r: float
            The magnitude or distance from the origin to the point.
        - theta: float
            The angle (in radians) between the positive x-axis and the line connecting the origin to the point.

    Examples:
    >>> rectangular_to_polar(3, 4)
    (5.0, 0.9272952180016122)
    >>> rectangular_to_polar(-2, -2)
    (2.8284271247461903, -2.356194490192345)
    """

    # Calculate the magnitude (r) using the Pythagorean theorem
    r = math.sqrt(x**2 + y**2)

    # Calculate the angle (theta) using the arctangent function
    theta = math.atan2(y, x)

    # Return the polar coordinates as a tuple
    return r, theta
