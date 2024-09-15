# if comment is #/ it is commented to not interfere with code

#Creating a set (Using ->{}<- brackets)
attendance = {'John', 'Bob', 'Sally'}

#Adding elements to a set
attendance.add('Bob')

#Printing Set
#/ print(attendance)

#Iterating Through a set
#/ for element in attendance:
    #/ print(element)

#Removing elements from a set
attendance.remove('John')
    #/ print(attendance)

#Checking if an element exists in a set
#/ print('Rosy'in attendance)

#Using "Union" (Like the same union in roblox) in a set
#Union: Combines all elements from two sets, with duplicates removed
Set1 = {1,2,3,4}
Set2 = {4,5,6,7}
union_set = Set1.union(Set2)
#/ print(union_set)

#Intersection: Returns elements common to both sets
intersection_set = Set1.intersection(Set2)
#/ print(intersection_set)

#Difference: Returns elements in the first set but not in the second.
difference_set = Set1.difference(Set2)
#/ print(difference_set)

#Symmetric Difference: Removes simillarites bewteen 2 sets
symdiff = Set1.symmetric_difference(Set2)
#/ print(symdiff)

#Different ways to remove elements in sets
# remove() method: Removes a specific element. If the element is not found, it raises a KeyError.
# discard() method: Removes a specific element. If the element is not found, it does nothing.
# pop() method: Removes and returns an arbitrary element from the set.
# clear() method: Removes all elements from the set, making it empty.

#Len: Prints the number of elements in a set
#/ print(len(Set1))

#Copy: returns a shallow copy of the set(replaces)
Copiedset = Set1.copy()
print(Copiedset)
