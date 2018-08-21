# -*- coding: utf-8 -*-
"""
Binary Search Tree 
https://www.laurentluce.com/posts/binary-search-tree-library-in-python/comment-page-1/
Created on Thu Feb 22 11:38:50 2018

@author: Alex
"""

class Node:
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self, data):
        """
        Node constructor
        @param data node object
        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        """
        Insert new node with data
        @param data node data object to insert
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            