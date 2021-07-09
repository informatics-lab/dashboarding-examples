# Generate trigonometric patterns.

import numpy as np


def trigonometric_1(n, m, k=1, w=0, b=0):
    """
    Generate a trigonometric pattern.

    Args:
      * n: number of points to generate the pattern with
      * m: number of points multiplier

    Kwargs:
      * k: frequency adjustment for pattern
      * w: phase adjustment for pattern
      * b: offset adjustment for pattern

    """
    t = np.linspace(-m*np.pi, m*np.pi, n)
    r = t % n
    x = r * np.sin(k*t + w) + b
    y = r * np.cos(k*t + w) + b
    return x, y


def trigonometric_2(n, m, k=1, w=0, b=0):
    """
    Generate a trigonometric pattern.

    Args:
      * n: number of points to generate the pattern with
      * m: number of points multiplier

    Kwargs:
      * k: frequency adjustment for pattern
      * w: phase adjustment for pattern
      * b: offset adjustment for pattern

    """
    t = np.linspace(-m*n, m*n, n)
    r = t // n
    x = r * np.sin(k*t + w) + b
    y = r * np.cos(k*t + w) + b
    return x, y


trigonometric = trigonometric_1


def spirograph(n, m,
               rnx=1, rny=1,
               rmx=1, rmy=1,
               kn=1, km=1,
               wn=0, wm=0):
    """
    Generate a spirograph pattern by extruding circles around a central ring.

    Args:
      * n: number of points to generate the central ring with
      * m: number of points to generate each circle with

    Kwargs:
      * rnx: amplitude of central ring x-component
      * rny: amplitude of central ring y-component
      * rmx: amplitude of circles' x-component
      * rmy: amplitude of circles' y-component
      * kn: frequency adjustment of central ring (x and y)
      * km: frequency adjustment of circles (x and y)
      * wn: phase adjustment of central ring (x and y)
      * wm: phase adjustment of circles (x and y)

    Args must be supplied as a single integer value. Kwargs can be supplied either
    as a single numeric value or an array that can be broadcast to the shape (n, m).

    """
    t_ring = np.linspace(0, 2*np.pi, n*m)
    t_circle = np.linspace(0, 2*np.pi, m)
    
    x_ring = rnx * np.sin(t_ring*kn).reshape(n, m)
    y_ring = rny * np.cos(t_ring*kn).reshape(n, m)
    xp = rmx * np.sin(t_circle*km) + x_ring
    yp = rmy * np.cos(t_circle*km) + y_ring

    return xp.reshape(-1), yp.reshape(-1)