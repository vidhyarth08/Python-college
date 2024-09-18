s = {4,8,2,6}

print(len(s))#gives the length of the set.
print(s.remove(8))#removes the element in the set.
print(s.pop())#returns the removed element.
print(s.clear())#empty the set.
print(s.union({8,11}))#returns a new set from both the sets.
print(s.intersection({8,11}))#returns the common element from both the sets.