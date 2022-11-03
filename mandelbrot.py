#!/usr/bin/env python3
from dataclasses import dataclass
from math import log

@dataclass
class Mandelbrot:
    """I don't really understand how this dataclass decorator works, but it is
    required in order for smoothing to work correctly. If using the normal
    def __init__(self) etc. syntax, banding is still present. Presumably it is
    something to do with defining the escape_radiues as a float here?
    """
    max_iterations: int
    escape_radius: float = 2.0

    def __contains__(self, c):
        """
        This is what makes it possible to use the `in` and `not in` checks.
        The stability() function returns 1 if the number does not diverge
        within max_iterations. As such, this special __contains__ method will
        return True if the number has not diverged and is, therefore, part of
        the Mandelbrot set.
        """
        return self.stability(c) == 1

    def stability(self, c, smooth=False, clamp=True):
        value = self.escape_count(c, smooth) / self.max_iterations
        if clamp:  # Prevents pixel intensities wrapping around min/max values
            return max(0.0, min(value, 1.0))
        else:
            return value

    def escape_count(self, c, smooth=False):
        z = 0
        for iteration in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) > self.escape_radius:
                if smooth:  # Returns a floating-point number.
                    return iteration + 1 - log(log(abs(z))) / log(2)
                return iteration
        return self.max_iterations
