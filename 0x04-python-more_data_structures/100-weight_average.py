#!/usr/bin/python3
def weight_average(my_list=[]):
    """calc weigh avg"""
    if  len(my_list) == 0:
        return 0
    
    sum = 0
    avg = 0
    
    for tup in my_list:
        sum += tup[0] * tup[1]
        avg += tup[1]
    return sum / avg

 #n1 = sum(map(lambda i: i[0] * i[1], my_list))
 #n2 = sum(map(lambda i: i[1], my_list))
        