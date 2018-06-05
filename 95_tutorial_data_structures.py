from __init__ import *

# --------- TUPLES ---------
############################
# tup = 'blah',45,89.63
# print(tup)
# print(type(tup))
# tup = tup[1:] + ('blah2',true)
# print('blah' in tup)
# multi_tup = tuple(t*2 for t in tup)
# filtered_tup = tuple(t for t in tup if type(t) not in (str,bool))
# print (len(multi_tup), filtered_tup)

# a = 'A'
# b = 'A'
# print (a is b, a == b)

# t1 = (1,2,3)
# t2 = (1,2,3)
# print (t1 is t2, t1 == t2)

# l1 = [1,2,3]
# l2 = [1,2,3]
# l3 = l1
# print (l1 is l2, l1 == l2, l1 is l3)
# print (t1[-1],t1[-3])

# print ("tup: ",tup)
# print("All: ",all(tup))
# print("Any: ",all(tup))
# print(tuple(enumerate(tup)))
# print(sorted(filtered_tup, reverse = true))
############################

# --------- LISTS ---------
###########################
# odd = [1,3,9]
# print(odd)
# #print(odd.clear())
# print(odd.copy())
# print(odd.count(3))
# odd.insert(2,5)
# print(odd)
# odd[3:] = [7,9,11]
# print(odd)
# print(odd.pop())
# odd.sort(reverse = true)
# print(odd)

# --------- DICTIONARIES ---------
##################################
# my_dict = dict([(1,'apple'), (2,'ball')])
# print(my_dict)
# copy_dict = my_dict.copy()
# my_dict[3] = "cat"
# print(copy_dict)
# print(my_dict)

# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

# print(people)

# peoplel = [{'name': 'John', 'age': '27', 'sex': 'Male'},
#           {'name': 'Marie', 'age': '22', 'sex': 'Female'},"Last"]

# for p in peoplel:
#     print(type(p),end=" ")

# --------- SETS ---------
###########################
my_set = {1,3}
print(my_set)
my_set.add(2)
print(my_set)
my_set.discard(3)
print(my_set)
my_set.update([x for x in range(10)])
print(my_set)
a = set("apple")
print(a)
