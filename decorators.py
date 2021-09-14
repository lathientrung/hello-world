def goo(a, L=[]):
    L.append(a)
    return L

print(goo(1), end=",")
print(goo(2), end=",")
print(goo(3))