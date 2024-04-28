#!/usr/bin/python3
"""find peak module"""


def find_peak(n_list):
    left, right = 0, len(n_list) - 1
    while (left <= right):
        med = left + (right - left) // 2
        # go to left neigh
        if med > 0 and n_list[med] < n_list[med - 1]:
            right = med - 1
        # go to right neigh
        elif med < len(n_list)- 1 and n_list[med] < n_list[med + 1]:
            left = med + 1
        else:
            return n_list[med]   
