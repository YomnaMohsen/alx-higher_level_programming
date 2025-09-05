#!/usr/bin/python3
"""LinkedlIst class"""


class Node:
    """This class defines Node in linkedlist"""
    def __init__(self, data, next_node=None):
        """Initializes a node object.
        Args:
            data (int): set data
            next_node: ref to next_node

        """
        self.data = data
        self.next_node = next_node
        
    @property
    def data(self):
        """Return data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
        
    @property
    def next_node(self):
        """Return Node"""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """Set node value"""
        if value == None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")    


class SinglyLinkedList:
    """This class defines singly linkedlist"""
    def __init__(self):
        """Initializes singly linkedlist object.
        Args:
            head
        """
        self.__head = None
        
        
    def sorted_insert(self, value):
        """ inserts a new Node into the correct 
        sorted position in the list (increasing order)
        
        Args:
            value (Node): The new Node to insert."""
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            """insert first element"""
            new.next_node = self.__head
            self.__head = new 
            
        else:
            tmp = self.__head
            while(tmp.next_node and tmp.next_node.data < value):
                    tmp =tmp.next_node
                  
            new.next_node = tmp.next_node
            tmp.next_node =new
                   
    
    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        f_str = ""
        tmp = self.__head
        while(tmp):
            f_str += (str(tmp.data) +("\n" if tmp.next_node
                                      else ""))
            tmp = tmp.next_node
        return  f_str   
        
 