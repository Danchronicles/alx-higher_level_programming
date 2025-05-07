#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    ordered_keys = sorted(a_dictionary)
    print(f"{ordered_keys}: {a_dictionary[ordered_keys]}")