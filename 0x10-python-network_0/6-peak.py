#!/usr/bin/python3
"""
This script finds the peak in a list of unsorted integers
"""
def find_peak(list_of_integers):
    """
    This function would find the peak of a given numbers
    """
    try:
        largestNumber = max(list_of_integers)
        return largestNumber
    except ValueError:
        return None
