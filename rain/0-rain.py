#!/usr/bin/python3
"""
rain module
"""


def rain(walls):
    """
    Calculates the amount of rainwater retained between walls.
    
    Args:
        walls (list of int): List of non-negative integers representing wall heights.
    
    Returns:
        int: Total amount of rainwater retained.
    """
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n
    water_retained = 0

    # Fill left_max
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Fill right_max
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate water retained
    for i in range(1, n - 1):
        water_retained += max(0, min(left_max[i], right_max[i]) - walls[i])

    return water_retained
