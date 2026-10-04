# B7_Task1_Identity.py
# Lab Task B7: Identity Operators

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2 :", list1 == list2) # True: they have equal contents
print("list1 is list2 :", list1 is list2) # False: they are separate objects in memory
print("list1 is not list2:", list1 is not list2)

print("\nlist1 == list3 :", list1 == list3) # True: they have equal contents
print("list1 is list3 :", list1 is list3) # True: they refer to the exact same object
print("list1 is not list3:", list1 is not list3)

print("\nid(list1):", id(list1))
print("id(list2):", id(list2))
print("id(list3):", id(list3))

# Comments:
# list1 and list2 have the same contents, so list1 == list2 is True.
# However, they are two separate lists created independently, so they reside at different memory addresses. 
# Therefore, list1 is list2 is False.
# list3 is directly assigned list1, which means it simply points to the same list object in memory as list1.
# Therefore, list1 is list3 is True, and their id() values are identical.
