a={1,2,3}
b={2,4,1}

print(a.intersection(b))
print(a.union(b))
# print(a.isdisjoint(b))
# print(a.difference(b))
print(a.symmetric_difference(b))
c=a.intersection(b)
d=a.union(b)
print(a-b)
print(b.union(a.intersection(b)))

# print(a.difference_update(b))
