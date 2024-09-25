#!/usr/bin/python3
"""
This module provides a function to calculate the amount of water trapped after it rains.
"""

def calculate_water_trap(elevations):
    """
    Given a list of wall heights (elevations), calculate how much water is trapped after rainfall.
    
    Args:
        elevations (list of int): List representing wall heights.
    
    Returns:
        int: The total amount of trapped water.
    """
    if not elevations or len(elevations) < 3:
        return 0

    total_water = 0

    for idx in range(1, len(elevations) - 1):
        # Maximum height to the left of the current wall
        max_left = max(elevations[:idx])
        # Maximum height to the right of the current wall
        max_right = max(elevations[idx + 1:])

        # Calculate the possible water level above the current wall
        water_level = min(max_left, max_right)

        # Water is only trapped if the current wall is lower than the water level
        if elevations[idx] < water_level:
            total_water += water_level - elevations[idx]

    return total_water

