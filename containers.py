# Lecture 2
# 03.12.2021
"""
Task 1
to create doubly linked list (methods: insert, delete, reverse)
A doubly linked list in Python is a related data structure
with a collection of sequentially related nodes.
Each node has 3 fields: two link fields that are references to the address
of the previous and next nodes in the sequence.
Another one data field refers to the data for that particular node.
"""


import time
import sys



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class MyDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_beginning(self, new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_the_end(self, new_val):
        new_node = Node(new_val)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def insert_before_item(self, x, new_val):
        if self.head is None:
            print("List is empty!")
            return
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.next
            if n is None:
                print("There isn't such item in the list!")
            else:
                new_node = Node(new_val)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.next = new_node
                n.prev = new_node

    def insert_after_item(self, x, new_val):
        if self.head is None:
            print("List is empty!")
            return
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.next
            if n is None:
                print("There isn't such element in the list!")
            else:
                new_node = Node(new_val)
                new_node.prev = n
                new_node.next = n.next
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node

    def delete_at_the_beginning(self):
        if self.head is None:
            print("There isn't any elements to delete!")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_at_the_end(self):
        if self.head is None:
            print("There isn't any elements to delete!")
            return
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def delete_element_by_value(self, x):
        if self.head is None:
            print("There isn't any elements to delete!")
            return
        if self.head.next is None:
            if self.head.data == x:
                self.head = None
            else:
                print("There isn't such element in the list!")
            return

        if self.head.data == x:
            self.head = self.head.next
            self.head.prev = None
            return

        n = self.head
        while n.next is not None:
            if n.data == x:
                break
            n = n.next
        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            if n.data == x:
                n.prev.next = None
            else:
                print("There isn't such item in the list!")

    def reverse(self):
        if self.head is None:
            print("List is empty!")
            return
        p = self.head
        q = p.next
        p.next = None
        p.prev = q
        while q is not None:
            q.prev = q.next
            q.next = p
            p = q
            q = q.prev
        self.head = p

    def print_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, " ")
                n = n.next


my_doubly_linked_list = MyDoublyLinkedList()

print("insert_at_the_beginning")
my_doubly_linked_list.insert_at_the_beginning(0)
my_doubly_linked_list.insert_at_the_beginning(1)
my_doubly_linked_list.print_list()

print("insert_at_the_end")
my_doubly_linked_list.insert_at_the_end(2)
my_doubly_linked_list.insert_at_the_end(3)
my_doubly_linked_list.print_list()

print("reverse")
my_doubly_linked_list.reverse()
my_doubly_linked_list.print_list()

print("delete_at_the_beginning")
my_doubly_linked_list.delete_at_the_beginning()
my_doubly_linked_list.print_list()

print("delete_at_the_end")
my_doubly_linked_list.delete_at_the_end()
my_doubly_linked_list.print_list()

print("delete_element_by_value")
my_doubly_linked_list.delete_element_by_value(0)
my_doubly_linked_list.print_list()


# 1.2.
# to add 1 000 000 000 items to two lists (self-created and built-in one)
# and check how much memory is used
amount_of_elements_in_the_list = 1000000000

built_in_list = []
iterator = 0
start_time = time.time()
while iterator < amount_of_elements_in_the_list:
    built_in_list.append(iterator)
    iterator += 1
print("--- For built_in_list %s seconds ---" % (time.time() - start_time))

memory_for_built_in_list = sys.getsizeof(built_in_list)
print("--- For built_in_list %s bytes ---" % memory_for_built_in_list)


my_doubly_linked_list_to_compare = MyDoublyLinkedList()
iterator = 0
start_time = time.time()
while iterator < amount_of_elements_in_the_list:
    my_doubly_linked_list_to_compare.insert_at_the_end(iterator)
    iterator += 1
print("--- For my_doubly_linked_list_to_compare %s seconds ---" % (time.time() - start_time))

memory_for_my_doubly_linked_list_to_compare = sys.getsizeof(my_doubly_linked_list_to_compare)
print("--- For my_doubly_linked_list_to_compare %s bytes ---" % memory_for_my_doubly_linked_list_to_compare)


# Task 2
# to hack dictionary
my_dict = {True: 'True', 1: 'Also True', 'True': 'String True',
           False: 'False', 0: 'Also False', 'False': 'String False'}

for key, value in my_dict.items():
  print("{0}: {1}".format(key, value))
# output:
# True: Also True
# True: String True
# False: Also False
# False: String False

len_of_my_dict = len(my_dict)
print(len_of_my_dict)
# output: 4

print(my_dict[True])
# output: Also True
# but not True, as it was expected

# conclusion
# integers (1 and 0) values are understood as boolean ones
# if they are used as the keys in dictionaries, which contain boolean and integer keys
# this can lead to further errors


# Task 3
# to hack set
my_set_bool_and_int = {False, True, 0, 1}
print(my_set_bool_and_int)
# output:
# {False, True}

print(len(my_set_bool_and_int))
# output:
# 2

my_set_int = {0, 1}
print(True or False in my_set_int)
# output:
# True

# here is the same problem as in previous task


# Task 4
# to try to put set in another set

# 1-st way using two sets and method add (leads to the error)
set_hello_world = {"hello", "world"}
set_of_punctuation_marks = {"!!!", ")))"}

# the error is here
# set_hello_world.add(set_of_punctuation_marks)
print(set_hello_world)

# 2-nd way (leads to the error too)
# nonsense_set = { 1, 2, { 3, 4 }, 5, 6 }

# Why the errors occurs?
# There is a limitation that only Hashable objects could be added to the set.
# This is due to the fact that the internal implementation of set is based on hash tables.
# For example, lists and dictionaries are mutable objects, so they could not be added to the set.
# Most of the immutable types in Python (int, float, str, bool, etc.) are hashable.
# Immutable collections, such as tuple, are hashable if all of their elements are hashable.

# so, putting one set in the another one is impossible
