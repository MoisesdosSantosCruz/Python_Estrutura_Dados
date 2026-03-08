L = [42, 3.7, "A", True, None]

#A
print(type(L[0]))
print(type(L[1]))
print(type(L[2]))
print(type(L[3]))
print(type(L[4]))

#B
print(L[0], L[4])

#C
L[1] = 99 
print(L)

#D
del L[2]
print(L)

