#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    l_tup = []
    for i in range(len(tuple_a)):
        l_tup.append(tuple_a[i] + tuple_b[i])
    tuple_c = tuple(l_tup)
    return tuple_c
