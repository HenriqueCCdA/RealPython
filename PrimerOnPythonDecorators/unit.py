def set_unit(unit):
    """Register a unit on a function"""
    def decorator_set_unit(func):
        func.unit = unit
        return func
    return decorator_set_unit

import math

@set_unit('cm³')
def volume(radius, height):
    return math.pi * height ** 2 * height
