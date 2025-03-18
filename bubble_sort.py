#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bubble Sort Implementation in Python

This module provides a simple implementation of the bubble sort algorithm,
which is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they are in the wrong order.
"""

def bubble_sort(arr):
    """
    Sorts an array using bubble sort algorithm.
    
    Args:
        arr (list): The list to be sorted
        
    Returns:
        list: The sorted list
    
    Time Complexity:
        - Best Case: O(n) when the array is already sorted
        - Average Case: O(n^2)
        - Worst Case: O(n^2)
    
    Space Complexity: O(1) as it's an in-place sorting algorithm
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize if no swapping occurs in a pass
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if current element is greater than next
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swapping occurred in this pass, array is sorted
        if not swapped:
            break
    
    return arr


def main():
    """
    Example usage of the bubble sort algorithm.
    """
    # Test cases
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [],  # Empty array
        [1]   # Single element
    ]
    
    for i, arr in enumerate(test_arrays):
        original = arr.copy()
        sorted_arr = bubble_sort(arr)
        print(f"Test case {i+1}:")
        print(f"Original array: {original}")
        print(f"Sorted array:   {sorted_arr}")
        print("-" * 40)


if __name__ == "__main__":
    main()