#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """"replaces all occurrences of an element 
    by another in a new list.
    serach: element we want to replace
    replace: new element"""
    
    new_list = my_list[:]
   
    for i in range(len(my_list)):
        if new_list[i] == search :
            new_list[i] = replace
    return (new_list)    

     
     